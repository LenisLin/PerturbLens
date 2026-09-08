#!/usr/bin/env python
"""Resident Tahoe-x1 embedding worker for Task1 FM preparation."""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import traceback
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


def _prepend(path: Path) -> None:
    text = str(path)
    if path.exists() and text not in sys.path:
        sys.path.insert(0, text)


def _build_protocol_writer() -> Any:
    protocol_stream = os.fdopen(os.dup(sys.stdout.fileno()), "w", buffering=1, encoding="utf-8")
    sys.stdout = sys.stderr
    return protocol_stream


def _reply(protocol_stream: Any, payload: dict[str, Any]) -> None:
    protocol_stream.write(json.dumps(payload, ensure_ascii=True) + "\n")
    protocol_stream.flush()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resident Tahoe-x1 worker")
    parser.add_argument("--protocol-version", default="1")
    return parser.parse_args()


class ResidentTahoeWorker:
    def __init__(self) -> None:
        self.initialized = False
        self.model = None
        self.vocab = None
        self.model_cfg = None
        self.collator_cfg = None
        self.loader_from_adata = None
        self.trainer = None
        self.anndata_mod = None
        self.sparse_mod = None
        self.torch = None
        self.output_dim: int | None = None

    def init(self, request: dict[str, Any]) -> dict[str, Any]:
        code_root = Path(str(request["code_root"])).resolve()
        model_dir = Path(str(request["model_dir"])).resolve()
        _prepend(code_root)

        import anndata as ad
        from scipy import sparse
        import torch

        from composer import Trainer
        from tahoe_x1.utils.util import load_model
        from tahoe_x1.utils.util import loader_from_adata

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model, vocab, model_cfg, collator_cfg = load_model(
            str(model_dir),
            device=device,
            return_gene_embeddings=False,
            use_chem_inf=False,
        )

        self.model = model
        self.vocab = vocab
        self.model_cfg = model_cfg
        self.collator_cfg = collator_cfg
        self.loader_from_adata = loader_from_adata
        self.trainer = Trainer(model=model, device="gpu" if torch.cuda.is_available() else "cpu")
        self.anndata_mod = ad
        self.sparse_mod = sparse
        self.torch = torch
        self.initialized = True

        return {
            "ok": True,
            "resident_runtime": True,
            "worker_pid": os.getpid(),
            "protocol_version": "1",
            "device": str(device),
            "cuda_available": bool(torch.cuda.is_available()),
            "model_dir": str(model_dir),
            "code_root": str(code_root),
            "output_dim": self.output_dim,
        }

    def encode_chunk(self, request: dict[str, Any]) -> dict[str, Any]:
        if not self.initialized:
            raise RuntimeError("Worker must be initialized before encode_chunk.")
        assert self.model is not None
        assert self.vocab is not None
        assert self.model_cfg is not None
        assert self.collator_cfg is not None
        assert self.loader_from_adata is not None
        assert self.trainer is not None
        assert self.anndata_mod is not None
        assert self.sparse_mod is not None
        assert self.torch is not None

        payload_path = Path(str(request["payload_path"])).resolve()
        output_path = Path(str(request["output_path"])).resolve()
        batch_size = max(1, int(request.get("batch_size") or 1))
        max_length = int(request.get("seq_len_dataset") or 2048)
        num_workers = int(request.get("num_workers") or 8)
        prefetch_factor = int(request.get("prefetch_factor") or 48)
        gene_id_key = str(request.get("gene_id_key") or "ensembl_id")
        cell_type_key = str(request.get("cell_type_key") or "cell_type")
        default_cell_type = str(request.get("default_cell_type") or "NA")

        with np.load(payload_path, allow_pickle=False) as payload:
            counts = np.asarray(payload["counts"], dtype=np.float32)
            cell_ids = payload["cell_ids"].astype(str).tolist()
            gene_symbols = payload["gene_symbols"].astype(str).tolist()
            ensembl_ids = payload["ensembl_ids"].astype(str).tolist()

        obs = pd.DataFrame(index=pd.Index(cell_ids, name="cell_id"))
        obs[cell_type_key] = [default_cell_type] * len(cell_ids)
        var = pd.DataFrame(index=pd.Index(gene_symbols, name="gene_symbol"))
        var[gene_id_key] = ensembl_ids
        adata = self.anndata_mod.AnnData(
            X=self.sparse_mod.csr_matrix(counts),
            obs=obs,
            var=var,
        )
        adata.var_names_make_unique()

        id_in_vocab = [self.vocab[gene] if gene in self.vocab else -1 for gene in adata.var[gene_id_key]]
        adata.var["id_in_vocab"] = id_in_vocab
        keep = np.asarray(id_in_vocab, dtype=np.int64) >= 0
        if not np.any(keep):
            raise RuntimeError("Tahoe-x1 resident worker found no payload genes in vocabulary.")
        adata = adata[:, keep].copy()
        gene_ids = np.asarray([self.vocab[gene] for gene in adata.var[gene_id_key].tolist()], dtype=int)
        if not np.all(gene_ids >= 0):
            raise RuntimeError("Tahoe-x1 resident worker produced invalid vocabulary gene ids.")

        row_sums = np.asarray(adata.X.sum(axis=1)).reshape(-1)
        valid_rows = np.isfinite(row_sums) & (row_sums > 0.0)
        valid_index = np.where(valid_rows)[0].astype(np.int64)
        if valid_index.size == 0:
            if self.output_dim is None:
                raise RuntimeError("Tahoe-x1 resident worker found no nonzero rows after vocabulary filtering.")
            matrix = np.full((len(cell_ids), int(self.output_dim)), np.nan, dtype=np.float32)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            np.save(output_path, matrix, allow_pickle=False)
            return {
                "ok": True,
                "n_rows": int(matrix.shape[0]),
                "embedding_dim": int(matrix.shape[1]),
                "used_batch_size": int(batch_size),
                "output_dim": self.output_dim,
                "n_genes_in_vocab": int(len(gene_ids)),
                "n_rows_zero_after_vocab": int(len(cell_ids)),
            }

        adata_valid = adata[valid_index, :].copy()
        self.collator_cfg["do_mlm"] = False
        loader = self.loader_from_adata(
            adata=adata_valid,
            collator_cfg=self.collator_cfg,
            vocab=self.vocab,
            batch_size=batch_size,
            max_length=max_length,
            gene_ids=gene_ids,
            num_workers=num_workers,
            prefetch_factor=prefetch_factor,
        )
        predictions = self.trainer.predict(loader, return_outputs=True)
        cell_embs = []
        for out in predictions:
            cell_embs.append(out["cell_emb"].cpu())
        if not cell_embs:
            raise RuntimeError("Tahoe-x1 resident worker produced no embeddings.")
        encoded = self.torch.cat(cell_embs, dim=0).numpy()
        encoded = encoded / np.linalg.norm(encoded, axis=1, keepdims=True)
        encoded = np.asarray(encoded, dtype=np.float32)
        if encoded.ndim != 2:
            raise RuntimeError(f"Tahoe-x1 resident worker output must be 2D, got shape={encoded.shape}")
        if int(encoded.shape[0]) != int(valid_index.size):
            raise RuntimeError(
                f"Tahoe-x1 resident worker row mismatch: got={encoded.shape[0]} expected={valid_index.size}"
            )
        matrix = np.full((len(cell_ids), int(encoded.shape[1])), np.nan, dtype=np.float32)
        matrix[valid_index, :] = encoded
        output_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(output_path, matrix, allow_pickle=False)
        self.output_dim = int(matrix.shape[1])
        return {
            "ok": True,
            "n_rows": int(matrix.shape[0]),
            "embedding_dim": int(matrix.shape[1]),
            "used_batch_size": int(batch_size),
            "output_dim": self.output_dim,
            "n_genes_in_vocab": int(len(gene_ids)),
            "n_rows_zero_after_vocab": int(len(cell_ids) - int(valid_index.size)),
        }

    def close(self) -> dict[str, Any]:
        try:
            self.trainer = None
            self.model = None
            if self.torch is not None and self.torch.cuda.is_available():
                self.torch.cuda.empty_cache()
        except Exception:
            pass
        self.initialized = False
        return {"ok": True}


def main() -> None:
    _parse_args()
    protocol_stream = _build_protocol_writer()
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    worker = ResidentTahoeWorker()

    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            command = str(request.get("command", ""))
            if command == "init":
                response = worker.init(request)
            elif command == "encode_chunk":
                response = worker.encode_chunk(request)
            elif command == "close":
                response = worker.close()
                _reply(protocol_stream, response)
                break
            else:
                response = {"ok": False, "error": f"Unsupported command: {command}"}
        except Exception as exc:  # noqa: BLE001
            logging.getLogger(__name__).exception("Tahoe resident worker command failed")
            response = {
                "ok": False,
                "error": str(exc),
                "error_type": exc.__class__.__name__,
                "traceback_excerpt": traceback.format_exc(limit=8)[-4000:],
            }
        _reply(protocol_stream, response)


if __name__ == "__main__":
    main()

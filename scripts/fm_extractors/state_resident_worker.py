#!/usr/bin/env python
"""Resident STATE embedding worker for Task1 FM preparation.

This worker runs inside the dedicated STATE runtime environment. It loads the
STATE model once and serves repeated chunk-encoding requests over a JSON-lines
stdin/stdout protocol.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import logging
import os
import site
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


def _infer_state_src(model_folder: Path) -> None:
    for parent in [model_folder, *model_folder.parents]:
        candidate = parent / "src"
        if (candidate / "state").is_dir():
            _prepend(candidate)
            return


def _bootstrap_site_packages() -> None:
    prefix = Path(sys.prefix)
    version_tag = f"python{sys.version_info.major}.{sys.version_info.minor}"
    candidates = [
        prefix / "lib" / version_tag / "site-packages",
        prefix / "Lib" / "site-packages",
    ]
    for candidate in candidates:
        if candidate.is_dir():
            site.addsitedir(str(candidate))


def _ensure_optional_deps() -> None:
    missing = []
    for module_name in [
        "omegaconf",
        "antlr4",
        "geomloss",
        "lightning",
        "lightning_utilities",
        "torchmetrics",
    ]:
        if importlib.util.find_spec(module_name) is not None:
            continue
        missing.append(module_name)
    if missing:
        logging.getLogger(__name__).warning(
            "STATE optional dependency precheck reported missing modules: %s",
            missing,
        )


def _disable_torch_compile() -> None:
    import torch

    def identity_compile(fn=None, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003
        if fn is None:
            return lambda inner: inner
        return fn

    torch.compile = identity_compile  # type: ignore[assignment]


def _build_protocol_writer() -> Any:
    protocol_stream = os.fdopen(os.dup(sys.stdout.fileno()), "w", buffering=1, encoding="utf-8")
    sys.stdout = sys.stderr
    return protocol_stream


def _reply(protocol_stream: Any, payload: dict[str, Any]) -> None:
    protocol_stream.write(json.dumps(payload, ensure_ascii=True) + "\n")
    protocol_stream.flush()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resident STATE worker")
    parser.add_argument("--protocol-version", default="1")
    return parser.parse_args()


class ResidentStateWorker:
    def __init__(self) -> None:
        self.inferer = None
        self.create_dataloader = None
        self.get_precision_config = None
        self.omega_conf = None
        self.anndata_mod = None
        self.sparse_mod = None
        self.torch = None
        self.current_embed_key = "X_state"
        self.output_dim: int | None = None
        self.initialized = False

    def init(self, request: dict[str, Any]) -> dict[str, Any]:
        model_folder = Path(str(request["model_folder"])).resolve()
        _infer_state_src(model_folder)
        _bootstrap_site_packages()
        _ensure_optional_deps()
        os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-state")
        _disable_torch_compile()

        from omegaconf import OmegaConf
        import anndata as ad
        from scipy import sparse
        import torch

        from state.emb.inference import Inference, create_dataloader, get_precision_config

        checkpoint = request.get("checkpoint")
        checkpoint_path = None if checkpoint in {None, ""} else str(Path(str(checkpoint)).resolve())
        config_path = request.get("config_path")
        cfg = None
        if config_path not in {None, ""}:
            cfg = OmegaConf.load(str(Path(str(config_path)).resolve()))

        protein_embeds = None
        protein_embeddings_override = request.get("protein_embeddings")
        protein_embeddings_path = None
        if protein_embeddings_override not in {None, ""}:
            candidate = Path(str(protein_embeddings_override)).resolve()
            if candidate.is_file():
                protein_embeddings_path = candidate
        else:
            exact_path = model_folder / "protein_embeddings.pt"
            if exact_path.is_file():
                protein_embeddings_path = exact_path
            else:
                matches = sorted(model_folder.glob("protein_embeddings*.pt"))
                if matches:
                    protein_embeddings_path = matches[-1]
        if protein_embeddings_path is not None:
            protein_embeds = torch.load(protein_embeddings_path, weights_only=False, map_location="cpu")

        inferer = Inference(cfg=cfg, protein_embeds=protein_embeds)
        inferer.load_model(checkpoint_path)

        self.inferer = inferer
        self.create_dataloader = create_dataloader
        self.get_precision_config = get_precision_config
        self.omega_conf = OmegaConf
        self.anndata_mod = ad
        self.sparse_mod = sparse
        self.torch = torch
        self.current_embed_key = str(request.get("embed_key") or "X_state")
        self.initialized = True

        return {
            "ok": True,
            "resident_runtime": True,
            "worker_pid": os.getpid(),
            "protocol_version": "1",
            "embed_key": self.current_embed_key,
            "output_dim": self.output_dim,
            "protein_embeddings_path": None
            if protein_embeddings_path is None
            else str(protein_embeddings_path),
        }

    def _encode_adata(self, *, adata: Any, dataset_name: str, batch_size: int | None) -> np.ndarray:
        assert self.inferer is not None
        assert self.create_dataloader is not None
        assert self.get_precision_config is not None
        assert self.omega_conf is not None
        assert self.torch is not None

        adata = self.inferer._convert_to_csr(adata)
        gene_column = self.inferer._auto_detect_gene_column(adata)
        device_type = "cuda" if self.torch.cuda.is_available() else "cpu"
        precision = self.get_precision_config(device_type=device_type)

        dataloader_cfg = self.inferer._vci_conf
        if batch_size is not None:
            try:
                dataloader_cfg = self.omega_conf.create(
                    self.omega_conf.to_container(self.inferer._vci_conf, resolve=True)
                )
                if not hasattr(dataloader_cfg, "model"):
                    dataloader_cfg["model"] = {}
                dataloader_cfg.model.batch_size = int(batch_size)
            except Exception:
                try:
                    dataloader_cfg.model.batch_size = int(batch_size)
                except Exception:
                    pass

        shape_dict = {str(dataset_name): (int(adata.n_obs), int(adata.n_vars))}
        dataloader = self.create_dataloader(
            dataloader_cfg,
            adata=adata,
            adata_name=str(dataset_name),
            shape_dict=shape_dict,
            data_dir="/tmp",
            shuffle=False,
            protein_embeds=self.inferer.protein_embeds,
            precision=precision,
            gene_column=gene_column,
        )

        all_embeddings: list[np.ndarray] = []
        all_ds_embeddings: list[np.ndarray] = []
        for embeddings, ds_embeddings in self.inferer.encode(dataloader):
            all_embeddings.append(np.asarray(embeddings, dtype=np.float32))
            if ds_embeddings is not None:
                all_ds_embeddings.append(np.asarray(ds_embeddings, dtype=np.float32))

        if not all_embeddings:
            raise RuntimeError("STATE resident worker produced no embeddings.")
        merged = np.concatenate(all_embeddings, axis=0).astype(np.float32, copy=False)
        if all_ds_embeddings:
            ds_merged = np.concatenate(all_ds_embeddings, axis=0).astype(np.float32, copy=False)
            merged = np.concatenate([merged, ds_merged], axis=-1)
        return merged

    def encode_chunk(self, request: dict[str, Any]) -> dict[str, Any]:
        if not self.initialized or self.inferer is None:
            raise RuntimeError("Worker must be initialized before encode_chunk.")
        assert self.anndata_mod is not None
        assert self.sparse_mod is not None

        payload_path = Path(str(request["payload_path"])).resolve()
        output_path = Path(str(request["output_path"])).resolve()
        dataset_name = str(request.get("dataset_name") or payload_path.stem)
        batch_size = request.get("batch_size")
        batch_size = None if batch_size in {None, ""} else int(batch_size)

        with np.load(payload_path, allow_pickle=False) as payload:
            counts = np.asarray(payload["counts"], dtype=np.float32)
            cell_ids = payload["cell_ids"].astype(str).tolist()
            gene_symbols = payload["gene_symbols"].astype(str).tolist()

        obs = pd.DataFrame(index=pd.Index(cell_ids, name="cell_id"))
        var = pd.DataFrame(index=pd.Index(gene_symbols, name="gene_symbol"))
        var["gene_name"] = np.asarray(gene_symbols, dtype=str)
        adata = self.anndata_mod.AnnData(
            X=self.sparse_mod.csr_matrix(counts),
            obs=obs,
            var=var,
        )
        adata.var_names_make_unique()

        matrix = self._encode_adata(adata=adata, dataset_name=dataset_name, batch_size=batch_size)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(output_path, matrix.astype(np.float32, copy=False), allow_pickle=False)
        self.output_dim = int(matrix.shape[1])
        return {
            "ok": True,
            "n_rows": int(matrix.shape[0]),
            "embedding_dim": int(matrix.shape[1]),
            "used_batch_size": batch_size,
            "output_dim": self.output_dim,
        }

    def close(self) -> dict[str, Any]:
        if self.inferer is not None:
            try:
                if getattr(self.inferer, "model", None) is not None:
                    self.inferer.model = None
            except Exception:
                pass
            self.inferer = None
        try:
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
    worker = ResidentStateWorker()

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
            response = {
                "ok": False,
                "error": str(exc),
                "error_type": exc.__class__.__name__,
                "traceback_excerpt": traceback.format_exc(limit=8)[-4000:],
            }
        _reply(protocol_stream, response)


if __name__ == "__main__":
    main()

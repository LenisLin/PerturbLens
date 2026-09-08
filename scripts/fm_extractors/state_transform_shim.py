#!/usr/bin/env python
"""Compatibility shim for running STATE embedding transform in repo demos.

The upstream ``state`` console entry imports the full CLI surface, which pulls
extra dependencies not needed for ``emb transform``. This shim imports only the
embedding transform path and patches ``torch.compile`` before STATE model import
so the Python 3.12 demo environment can load the model code.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path


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
        raise RuntimeError(
            "STATE optional dependencies are missing from the active Python environment. "
            "Install them into the active conda environment before running STATE. "
            f"missing={missing}"
        )


def _disable_torch_compile() -> None:
    import torch

    def identity_compile(fn=None, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003
        if fn is None:
            return lambda inner: inner
        return fn

    torch.compile = identity_compile  # type: ignore[assignment]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="STATE emb transform compatibility shim")
    parser.add_argument("--model-folder", required=True)
    parser.add_argument("--checkpoint", required=False)
    parser.add_argument("--config", required=False)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--embed-key", default="X_state")
    parser.add_argument("--protein-embeddings", required=False)
    parser.add_argument("--lancedb", required=False)
    parser.add_argument("--lancedb-update", action="store_true")
    parser.add_argument("--lancedb-batch-size", type=int, default=1000)
    parser.add_argument("--batch-size", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model_folder = Path(args.model_folder).resolve()
    _infer_state_src(model_folder)
    _ensure_optional_deps()
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-state")
    _disable_torch_compile()

    from state._cli._emb._transform import run_emb_transform

    run_emb_transform(args)


if __name__ == "__main__":
    main()

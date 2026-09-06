# Gene Representation Contract

## Role

`Gene` is a benchmark-wide representation space. This document defines the
current Task1 source-local and final-snapshot Gene surfaces, including feature
order, row alignment, and storage. Task-specific lawful units remain in the
[Task1 contract](../../tasks/task1.md).

## Representation Semantics

One row in a Gene matrix is one delta instance and one column is one
standardized gene feature. Gene values remain in delta space:

- LINCS uses the retained Level5 signature directly, with no additional
  normalization or clipping in its preprocessing stage.
- scPerturb uses `x_treat - mean(sampled_controls)`, with no z-score
  transformation or clipping in its preprocessing stage.

Source-specific preprocessing writes native Gene surfaces first. The final
Task1 shared Gene surface is assembled downstream by `task1_scope_merge.py`
after source-local feature axes have been standardized.

## Source-Local LINCS Surface

The LINCS source bundle carries:

- `gene/gene_delta.npy`
- `gene/gene_meta.csv`
- `gene/gene_feature_index.csv`

`gene_meta.csv` is matrix-near metadata and is strictly row-aligned with
`gene_delta.npy`. Its minimal columns are `instance_id`, `dataset`,
`cell_line`, `perturbation_type`, `perturbation_gene`, `time_hr`, and
`dose_um`. The feature index is a one-column table named `feature_id`, and its
row order matches the matrix column order.

The full LINCS source-local behavior, including native Level5 feature space,
retained signatures, chemical target mapping, and source-specific audit fields,
is defined in the [LINCS preprocessing contract](../preprocessing/lincs.md).

## Source-Local scPerturb Surface

The scPerturb source bundle carries one global feature index, one global shard
routing table, and deterministic Arrow shards:

- `gene/gene_feature_index.csv`
- `gene/gene_shard_index.csv`
- `gene/shards/shard_000000/gene_delta.arrow`
- `gene/shards/shard_000000/gene_meta.csv`
- additional shard directories as routed

Each `gene_delta.arrow` is an Arrow IPC file using zstd compression with one
`delta` column encoded as `fixed_size_list(float32, n_features)`. Each shard's
`gene_meta.csv` is strictly row-aligned with its same-shard matrix. The global
feature index row order matches the feature order of every shard. Each shard
contains at most `1,000,000` instances, and shard order is deterministic.

The source-local scPerturb feature index stores standardized gene symbols in
one `feature_id` column. Pairing, treated/control handoff, resume validation,
and source-specific metadata remain owned by the [scPerturb preprocessing
contract](../preprocessing/scperturb.md).

## Canonical Shared Task1 Surface

`task1_scope_merge.py` owns the final shared feature table at:

```text
master/representations/Gene/feature_index.csv
```

The canonical table is the union of standardized uppercase gene symbols across
retained active Task1 LINCS and scPerturb instances, sorted in uppercase
alphabetical order. Final snapshot Gene matrices are aligned to this feature
order. Missing source-specific genes are handled by the snapshot assembly
contract when projecting into the shared universe.

The final snapshot stores dense `float32` `NPY` matrices under
`representations/Gene/` with `matrix.npy`, `row_index.csv`, and
`feature_index.csv`. `row_index.csv` is keyed by `instance_id`; matrix row
order need not equal `master/instance_registry.csv` order.

## Feature Alignment Rules

- Feature order is part of the representation contract and must be recorded by
  the feature index, never inferred from a matrix position alone.
- Matrix metadata and matrix rows must remain aligned at every matrix-near
  source-local surface.
- Source-specific feature indexes may differ before the final Task1 union.
- The final shared Task1 feature index is built once before block slicing so
  `lincs_internal`, `scperturb_internal`, and `cross` use the same canonical
  Gene axis where the representation is lawful.
- No ortholog mapping is performed in the current Figure 2 Task1 freeze; the
  current scPerturb source bundle is human-only.

## Scope Boundary

`Gene` and `Pathway` are the benchmark-wide primary representation spaces.
This contract preserves the current Task1 data surfaces and does not authorize
FM in Figure 2 panels. FM is a separate scPerturb representation family with
its own [contract](fm.md) and the manuscript-facing scope specified by the
project and task documents.

The current Task1 data snapshot is specified in the [snapshot contract](../snapshots/task1.md).
The task-level use of Gene, including internal and cross slices, is specified
in the [Task1 contract](../../tasks/task1.md).

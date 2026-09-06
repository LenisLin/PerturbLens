# Task1 Data Snapshot Contract

## Role

This contract defines the Task1 data snapshot surface that connects
source-local preprocessing bundles to the final Task1 snapshot under
`/mnt/NAS_21T/ProjectData/M2M/data/task1`.

## Scientific Purpose

This contract freezes the directory layout, script handoff, routing semantics,
and core registry ownership needed to build one reusable Task1 task-data
surface for Figure 2 analysis. It does not freeze downstream metric tables,
panel-ready exports, or full field-by-field column inventories.

## Active Root Layout

- active Task1 data root = `/mnt/NAS_21T/ProjectData/M2M/data/task1`
- top-level required items:
  `snapshot_manifest.json`, `representation_registry.csv`, `sources/`,
  `master/`, `blocks/`
- source-local bundles:
  `sources/lincs/`, `sources/scperturb/`
- final block exports:
  `blocks/lincs_internal/`, `blocks/scperturb_internal/`, `blocks/cross/`

## Script Handoff

- `task1_lincs_prep.py` writes the source-local `LINCS` bundle under
  `sources/lincs/`
- `task1_scperturb_prep.py` writes the source-local `scPerturb` bundle under
  `sources/scperturb/`; the written source-local bundle is human-only and
  contains only rows with `organism == human`
- for `task1_scperturb_prep.py`, `--overwrite` means clean rebuild of the
  outputs owned by that stage rather than reuse of stale source-local files
- for `task1_scperturb_prep.py`, the overwrite cleanup boundary covers:
  `runs/<run_id>/task1_scperturb_prep/`,
  `sources/scperturb/bundle_manifest.json`,
  `sources/scperturb/registry/instance_registry.csv`,
  `sources/scperturb/registry/pairing_index.csv`,
  `sources/scperturb/registry/fm_cell_registry.csv`,
  `sources/scperturb/gene/gene_feature_index.csv`,
  `sources/scperturb/gene/gene_shard_index.csv`, and
  `sources/scperturb/gene/shards/`
- `task1_scperturb_fm_prep.py` writes FM outputs back into the same
  `sources/scperturb/` bundle
- `task1_scperturb_fm_prep.py` uses the formal source-local `Gene` shard scope
  as its legal instance anchor; registry-only or smoke-like `sources/scperturb/`
  roots without `gene_shard_index.csv` and referenced shard files are invalid
- `sources/scperturb/fm/` remains owned by `task1_scperturb_fm_prep.py` and is
  outside the `task1_scperturb_prep.py` overwrite cleanup boundary
- `task1_scope_merge.py` reads the two source-local bundles and materializes the
  final snapshot under `master/`, `blocks/`, and the root-level
  `representation_registry.csv`
- `task1_scope_merge.py` owns the final canonical shared `Gene` feature table at
  `master/representations/Gene/feature_index.csv`
- when a source-local `gene_feature_index.csv` contains standardized gene
  symbols not yet present in that canonical table,
  `task1_scope_merge.py` expands the canonical table by union over
  standardized uppercase gene symbols, sorts the final table in uppercase
  alphabetical order, and aligns final snapshot `Gene` representations to the
  updated table

## Source-local Bundle Layout

- every source-local bundle root carries `bundle_manifest.json`
- both source-local bundles use `registry/` and `gene/`
- only `sources/scperturb/` uses `fm/`
- source-local bundle naming is explicit rather than final-snapshot
  representation naming
- `sources/lincs/gene/` uses:
  `gene_delta.npy`, `gene_meta.csv`, `gene_feature_index.csv`
- `sources/scperturb/gene/` uses:
  `gene_feature_index.csv`, `gene_shard_index.csv`, `shards/`
- `sources/scperturb/gene/shards/` uses one shard directory per routed block:
  `shard_000000/gene_delta.arrow`, `shard_000000/gene_meta.csv`, ...
- the frozen source-local `scPerturb` `Gene` surface is:
  `sources/scperturb/gene/gene_feature_index.csv`,
  `sources/scperturb/gene/gene_shard_index.csv`,
  `sources/scperturb/gene/shards/shard_000000/gene_delta.arrow`, and
  `sources/scperturb/gene/shards/shard_000000/gene_meta.csv`
- source-local `scPerturb` `Gene` deltas are Arrow IPC files with zstd
  compression and a single `delta` column encoded as
  `fixed_size_list(float32, n_features)`
- `fm/` remains model-specific under `fm/<model>/` and uses explicit `fm_*`
  names
- both source-local bundles carry a core `registry/instance_registry.csv`
- source-local instance registries use a shared harmonized core plus
  source-specific extension columns
- source-specific files are allowed in addition to the shared core
- `scPerturb` may carry pairing and FM-prep registry files not present in
  `LINCS`

## Snapshot Route Vocabulary

- the snapshot-layer routing field is `block`
- frozen block names are:
  `lincs_internal`, `scperturb_internal`, `cross`
- `scope` and `dataset_or_direction` are not the primary routing fields inside
  the snapshot layer
- downstream stage outputs derive `scope` and `dataset_or_direction` from
  `block`

## Final Snapshot Layout

- `master/` is the canonical Task1 snapshot source
- `master/` keeps complete
  `instance_registry.csv`, `unit_registry.csv`, `unit_membership.parquet`, and
  `representations/`
- `blocks/` provides block-scoped analysis-ready exports for
  `lincs_internal`, `scperturb_internal`, and `cross`
- each block keeps `unit_registry.csv`, `unit_membership.parquet`, and
  block-sliced `representations/` for the representations lawful on that block
- blocks do not require `block_manifest.json`
- the root-level `representation_registry.csv` is the single canonical
  representation directory table for `master/` and all block surfaces
- each representation surface uses `row_index_path` keyed by `instance_id`
  and does not require matrix row order to match
  `master/instance_registry.csv`
- representation paths are stored relative to the Task1 root
- `master/representations/Gene/feature_index.csv` is deterministic:
  `task1_scope_merge.py` takes the union of standardized uppercase gene
  symbols from source-local bundles and writes the final canonical order in
  uppercase alphabetical order
- all representation directories use:
  `matrix.npy`, `row_index.csv`, `feature_index.csv`
- final snapshot representation storage uses
  `representations/<representation>/...`
- final snapshot representation matrices are dense `float32` arrays in `NPY`
  format

## Manifest Structure

Both `bundle_manifest.json` and `snapshot_manifest.json` use the same top-level
sections:

- `identity`
- `build`
- `inputs`
- `artifacts`

`counts` is not required as a top-level section in the current freeze.

The frozen `identity` fields are:

- `manifest_type`
- `task`
- `object_name`
- `schema_version`

The frozen `build` fields are:

- `builder_script`
- `built_at`
- `upstream_inputs`
- `contract_parameters`

Each `build.upstream_inputs` entry uses:

- `input_type`
- `input_name`

When a manifest covers `sources/scperturb/` or any snapshot built from that
bundle, `build.contract_parameters` must include:

- `scperturb_human_only = true`
- `scperturb_pairing_seed = 619`
- `scperturb_local_context_priority = ["sample", "batch", "plate", "gemgroup", "lane", "replicate"]`

When `task1_scperturb_fm_prep.py` updates `sources/scperturb/bundle_manifest.json`,
`build.contract_parameters` must also record:

- `active_fm_families`
- `active_fm_families_source`
- `fm_models_materialized`
- `fm_min_instance_coverage`

`active_fm_families_source` is the `## Active FM Families` section of
`../representations/fm.md`.
`fm_models_materialized` is a materialized-state list for valid
contract-approved FM directories on disk, not the authority for discovering the
active FM model universe.

The `inputs` section records source-type plus source-path evidence and remains
distinct from the direct dependency objects listed in `build.upstream_inputs`.

Each `inputs` entry uses:

- `source_type`
- `source_path`

The `artifacts` section explicitly lists key output files and directories using
entries of the form:

- `artifact_type`
- `artifact_path`

For both manifests, artifact paths are stored as paths relative to the Task1
root.

The frozen minimal `artifact_type` vocabulary is:

- `instance_registry`
- `unit_registry`
- `unit_membership`
- `gene_delta_matrix`
- `gene_meta`
- `gene_feature_index`
- `gene_shard_index`
- `gene_shards_root`
- `pairing_index`
- `fm_cell_registry`
- `fm_delta_matrix`
- `fm_delta_meta`
- `fm_feature_index`
- `representation_registry`
- `representation_matrix`
- `representation_row_index`
- `representation_feature_index`

For `bundle_manifest.json`, the artifact list must explicitly cover the key
source-local registry and gene outputs, plus `scPerturb`-specific pairing and
`FM` outputs when present.

For the `scPerturb` source-local `Gene` surface, `bundle_manifest.json` must
explicitly cover:

- `sources/scperturb/gene/gene_feature_index.csv`
- `sources/scperturb/gene/gene_shard_index.csv`
- `sources/scperturb/gene/shards/`

For `task1_scperturb_prep.py`, a successful overwrite run must leave those
manifest-listed `Gene` artifacts aligned with the current run contents and must
not rely on stale shard directories from earlier runs.

For `snapshot_manifest.json`, the artifact list must explicitly cover root-level
snapshot artifacts, canonical `master/` artifacts, block-level unit tables, and
block-level representation roots.

## Core Registry Structure

- `instance_registry.csv` stores one row per delta-space Task1 instance
- the persisted instance-level primary key is `instance_id`
- `instance_id` uses the readable composite format:
  `{dataset}::{cell_line}::{perturbation_type}::{perturbation_gene}::{time_hr_or_NA}::{dose_um_or_NA}::{source_trace}`
- `source_trace` is `sig_id` for `LINCS` and `cell_id` for `scPerturb`
- missing `time_hr` or `dose_um` values are written as `NA`
- do not require a separate persisted `row_id` field in the minimal contract;
  any source-local row numbering remains an internal construction and ordering
  helper
- source-local instance registries use the shared harmonized core:
  `instance_id`, `dataset`, `cell_line`, `perturbation_type`,
  `perturbation_gene`, `time_hr`, `dose_um`
- standardized numeric metadata columns are `time_hr` and `dose_um`
- `time_hr` is populated only from explicit numeric time fields and is recorded
  in hours
- sentinel, invalid, or missing source time values are written as `NA`
- `dose_um` is populated only when the source provides an explicit numeric dose
  with a unit that can be converted into molar concentration
- accepted dose units for standardization are:
  `uM`, `µM`, `micromolar`, and `nM`
- `nM` values are converted to `uM`
- mass-based units, volume units, unitless dose values, and other
  non-convertible dose encodings are written as `NA` in `dose_um`
- raw source time and dose fields remain preserved in source-specific extension
  columns
- for `sources/scperturb/`, shard-local `gene_meta.csv` is the matrix-near
  row-metadata table for the same-shard `gene_delta.arrow`
- for `task1_scperturb_fm_prep.py`, the concatenated shard-local
  `gene_meta.csv` rows define the formal Gene delta instance scope used for FM
  coverage
- for `sources/scperturb/`, the row order of each shard `gene_meta.csv` must
  match the row order of the same-shard `gene_delta.arrow`
- the minimal shard `gene_meta.csv` columns are:
  `instance_id`, `dataset`, `cell_line`, `perturbation_type`,
  `perturbation_gene`, `time_hr`, `dose_um`
- `sources/scperturb/gene/gene_feature_index.csv` is the global single
  column-index table for all source-local `scPerturb` `Gene` shards
- the row order of `gene_feature_index.csv` must match the column order of
  every shard `gene_delta.arrow`
- `sources/scperturb/gene/gene_shard_index.csv` is the source-local shard
  routing table
- `task1_scperturb_prep.py --resume-stage-dir` remains compatible with legacy
  dataset-local `parallel_shards/<dataset>.gene_delta.npy` payloads after
  validation, but newly computed dataset-local payloads and final shards use
  `.arrow`
- `gene_shard_index.csv` keeps the frozen minimal columns:
  `shard_id`, `dataset`, `shard_seq`, `n_instances`, `gene_delta_path`,
  `gene_meta_path`
- each `scPerturb` shard keeps at most `1,000,000` instances
- final `scPerturb` shard order is deterministic
- `gene_feature_index.csv` keeps one column:
  `feature_id`
- for the `Gene` representation, `feature_id` stores the source-local
  standardized gene symbol used by the preprocessing bundle
- the final canonical shared `Gene` feature table lives at:
  `master/representations/Gene/feature_index.csv`
- `task1_scope_merge.py` owns union-based expansion of that canonical table,
  sorts the final feature order in uppercase alphabetical order, and aligns
  final snapshot `Gene` representations to the updated shared feature space
- source-specific trace and audit fields stay source-local by default
- `LINCS` keeps `sig_id` as the source trace key
- `scPerturb` keeps `cell_id` as the treated-cell trace key
- `cell_id` is the `scPerturb` source-local raw-cell trace key rather than the
  benchmark instance key
- `cell_id` is frozen as:
  `{dataset}::{raw_internal_cell_name}`
- `raw_internal_cell_name` means the source-native treated-cell identifier used
  to build `cell_id`
- source-local `scPerturb` extraction of `cell_id`, `cell_line`, raw
  `perturbation_type`, chemical identity, genetic multi-gene tokens, `time_hr`,
  `dose_um`, local-context columns, and control rows is frozen in
  `../preprocessing/scperturb.md#active-human-dataset-mapping-freeze`
- the frozen scPerturb pairing base pool is:
  same `dataset` + same `cell_line` + same normalized `perturbation_type`
- the frozen scPerturb pairing mode is deterministic with replacement
- the dedicated `scPerturb` pairing index path is:
  `sources/scperturb/registry/pairing_index.csv`
- within the `scPerturb` source-local bundle, `cell_id` remains the canonical
  raw-cell trace key for `instance_registry.csv`, `pairing_index.csv`,
  `fm_cell_registry.csv`, and `fm_delta_meta.csv`
- downstream delta-instance and benchmark-facing analysis layers continue to use
  `instance_id`
- `scPerturb` detailed pairing facts live in a dedicated pairing index rather
  than inside the instance registry
- `master/instance_registry.csv` keeps the harmonized core plus the minimal
  trace extension columns `sig_id` and `cell_id`
- `unit_membership.parquet` is the canonical unit fact table
- the canonical `unit_membership.parquet` is carried by `master/`
- the minimal `unit_membership.parquet` columns are:
  `unit_id`, `instance_id`, `block`, `dataset`, `cell_line`,
  `perturbation_type`, `perturbation_gene`
- `unit_registry.csv` is the unit summary table derived from membership
- the canonical `unit_registry.csv` is carried by `master/`
- all three blocks retain actual units only and do not enumerate empty
  candidate units
- `cross` retains only units with exact
  `(cell_line, perturbation_type, perturbation_gene)` agreement across sources
- under the current active cross slice, this means matched single-gene genetic
  units only
- `unit_id` uses a block-prefixed readable format such as
  `lincs_internal::A375::chemical::EGFR|PIK3CA`
  and `cross::A375::genetic::MYC`
- the minimal `unit_registry.csv` columns are:
  `unit_id`, `block`, `cell_line`, `perturbation_type`,
  `perturbation_gene`, `n_instances_lincs`, `n_instances_scperturb`,
  `n_instances_total`
- do not require additional complex unit-status fields in the minimal contract
- the root-level `representation_registry.csv` is a technical directory table
- it stores one row per `surface + representation`
- `surface` is frozen to:
  `master`, `lincs_internal`, `scperturb_internal`, `cross`
- `master` retains all active Task1 representations
- `lincs_internal` retains `Gene` and `Pathway`
- `scperturb_internal` retains `Gene`, `Pathway`, and all active Task1 `FM`
  representations
- `cross` retains `Gene` and `Pathway` only
- the minimal table columns are:
  `surface`, `representation`, `matrix_path`, `row_index_path`,
  `feature_index_path`, `dtype`

## Scope Boundary

- this contract freezes task-data layout, routing semantics, and registry
  ownership
- full field-by-field column inventories remain to be finished in a later
  field-level freeze
- no downstream group or retrieval metric table freeze
- no `2A` panel-specific R handoff
- no panel-ready exports

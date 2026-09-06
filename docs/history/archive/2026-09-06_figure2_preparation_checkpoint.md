# Archived: Figure 2 Task1 Data Preparation Freeze Checkpoint

Archived on 2026-09-06. This consolidated checkpoint is historical, not an
active contract. Current preparation and representation owners are indexed in
[the documentation entry](../../README.md); open work is tracked in
[state](../../governance/state.md). Original references below are retained for
historical interpretation rather than current execution. Inventory link labels
retain the former filenames; their destinations point to migrated successors.

Status: current freeze checkpoint for Figure 2 Task1 data preparation design.

## Role

This checkpoint freezes the Figure 2 Task1 data preparation layer. It now
covers dataset-specific preprocessing, source-local Task1 bundles, and the
structural handoff into the final Task1 task-data snapshot under
`/mnt/NAS_21T/ProjectData/M2M/data/task1`.

It does not freeze the `2A` interface, downstream
`group/retrieval/metrics/export`, or panel-level R scripts. Full
field-by-field registry inventories also remain incomplete, even though the
structural task-data ownership of `task1_scope_merge.py` is now frozen.

Task1 internal and cross unit definitions remain controlled by
`docs/contracts/task1_spec.md`.

## Scientific Question

Figure 2 Task1 data preparation asks how lawful Task1 units are constructed
from raw `LINCS` and `scPerturb` inputs, how source-local delta bundles are
prepared, and how those bundles hand off into one reusable Task1 task-data
snapshot for Figure 2 analysis. It does not answer comparative performance
questions.

## Controlling Sources

The current checkpoint is grounded against:

- `docs/redesign_checkpoint.md`
- `docs/contracts/task1_spec.md`
- `docs/contracts/output-schemas.md`
- `docs/manuscript_master.md`
- `docs/plotting/plotting_preparation_freeze.md`
- `docs/plotting/manuscript_figure_legends.md`
- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/`
- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/scPerturb_Processed`
- `/mnt/NAS_21T/ProjectData/OSMOSIS/resource/OmniPath_annotations/HALLMARK_human.csv`

## Current Checkpoint Coverage

Covered in the current freeze:

- `task1_lincs_prep.py`
- `task1_scperturb_prep.py`
- `task1_scperturb_fm_prep.py`
- structural task-data handoff into `task1_scope_merge.py`
- shared `Pathway` contract
- Task1 source-bundle and snapshot layout
- Task1 core registry structure
- `scPerturb` source-bundle human-only filtering
- no ortholog mapping in the current Figure 2 Task1 freeze
- fixed `scPerturb` chemical identity rules, including the sole `sciplex4`
  token-based exception
- `scPerturb` internal-only multi-gene genetic retention and canonicalization
- fixed deterministic pairing seed `619`
- fixed single-field local-context priority chain and
  `local_context_key_used` vocabulary
- minimal per-active-human-dataset extraction mapping freeze
- deterministic canonical shared `Gene` alphabetical order after union
- Task1 `scPerturb` FM delta semantics

Not covered in the current freeze:

- exhaustive full field-level registry inventories
- `2A` twin-panel interface
- downstream `group/retrieval/metrics/export`
- panel-level R scripts

## Locked Decisions Summary

- `LINCS` chemical = `trt_cp` only
- `LINCS` genetic = `trt_xpr` only
- `scPerturb` source-bundle scope = human-only
- the current Figure 2 Task1 freeze does not perform ortholog mapping
- Hallmark50 pathway source =
  `/mnt/NAS_21T/ProjectData/OSMOSIS/resource/OmniPath_annotations/HALLMARK_human.csv`
- `Pathway` representation = one signed scalar per hallmark
- general `scPerturb` chemical rows must resolve to one canonical target-set
  string or they are excluded from lawful Task1 scope
- `sciplex4` remains the sole retained token-based chemical identity exception
- `scPerturb` internal may retain canonicalized multi-gene genetic rows
- multi-gene genetic canonicalization is uppercase + dedup + alphabetical + `|`
- Task1 cross remains the matched single-gene genetic slice
- all `scPerturb` pairing uses fixed seed `619`
- local-context matching uses the frozen single-field priority chain
  `sample > batch > plate > gemgroup > lane > replicate`
- `local_context_key_used` is frozen to
  `sample`, `batch`, `plate`, `gemgroup`, `lane`, `replicate`, `base_pool`
- minimal per-active-human-dataset extraction mapping is now frozen
- formal `task1_scperturb_prep.py` CLI parameters are frozen to
  `--project-root`, `--run-id`, `--task1-root`, `--runs-root`, `--seed`,
  `--workers`, `--overwrite`, `--scperturb-raw-root`
- the canonical shared `Gene` feature table is written in uppercase
  alphabetical order after union expansion
- `FM` deltas may be materialized upstream for all-reps raw analysis support,
  but `FM` does not enter manuscript-facing Figure 2 panels

## Latest Confirmed Defaults

- `Pathway` canonical feature order is fixed alphabetical over the `50`
  Hallmark features
- duplicate gene-symbol collapse for `Pathway` projection uses `mean`
- `LINCS` retains only `trt_cp` and `trt_xpr` rows with `qc_pass == 1`
- one retained `LINCS` `sig_id` row equals one benchmark instance
- `LINCS` `Gene delta` uses the retained Level5 signature vector directly
- retained `LINCS` genetic identity uses `uppercase(cmap_name)`
- preprocessors output native `Gene delta`; `LINCS` keeps a single matrix while
  `scPerturb` keeps deterministic source-local shards with one global
  `gene_feature_index.csv`, one global `gene_shard_index.csv`, shard-local
  `gene_meta.csv`, and an instance registry; final shared `Pathway` and the
  final canonical shared `Gene` feature table are owned downstream by
  `task1_scope_merge.py`
- `scPerturb` source-local bundle retains only `organism == human` rows and
  excludes non-human-only sources
- the current Figure 2 Task1 freeze does not perform ortholog mapping
- `scPerturb` uses local-context matching with fallback to the base control
  pool
- local-context matching falls back only after the frozen single-field chain
  fails to find at least `2` eligible controls
- frozen `scPerturb` local-context priority is
  `sample > batch > plate > gemgroup > lane > replicate`
- `plate_id` is normalized to canonical `plate`
- `local_context_key_used` is frozen to:
  `sample`, `batch`, `plate`, `gemgroup`, `lane`, `replicate`, `base_pool`
- `well` and `well_id` are excluded from the default global local-context rule
- `scPerturb` `Gene delta` uses raw subtraction:
  `x_treat - mean(sampled_controls)`
- `scPerturb` deterministic control sampling uses fixed-seed sampling with
  replacement
- all `scPerturb` pairing uses fixed global seed `619`
- `scPerturb` implementation may use dataset-level multiprocessing, dataset
  size ascending scheduling, bucketized pairing, and chunked matrixized
  `Gene delta` compute while preserving the frozen contract semantics
- default `scPerturb` behavior does not apply secondary-background matching
- general `scPerturb` chemical rows must resolve to one canonical target-set
  string to remain lawful
- if a chemical row does not have a usable and standardizable target-set, it
  is excluded from lawful Task1 scope
- chemical `perturbation_gene` canonicalization uses uppercase + dedup +
  alphabetical + `|`
- `sciplex4` is the only retained combo exception and now uses canonicalized
  `perturbation` tokens (`uppercase + dedup + alphabetical + |`) together with
  the frozen `nperts 0/1/2` row split; `target` does not define chemical
  identity for `sciplex4`
- `scPerturb` internal may retain canonicalized multi-gene genetic rows
- multi-gene genetic rows do not enter the current Task1 cross block
- active Task1 data root layout is `sources/ + master/ + blocks/`
- `sources/lincs/` carries `bundle_manifest.json`, `registry/`, and `gene/`
- `sources/scperturb/` carries `bundle_manifest.json`, `registry/`, `gene/`,
  and `fm/`
- final snapshot block names are
  `lincs_internal`, `scperturb_internal`, and `cross`
- final snapshot routing uses `block`; downstream `scope` and
  `dataset_or_direction` are derived later
- `master/` is the canonical Task1 source
- the canonical shared `Gene` feature table lives at
  `master/representations/Gene/feature_index.csv`
- `task1_scope_merge.py` expands that canonical table by union over
  standardized uppercase gene symbols, writes the final order in uppercase
  alphabetical order, and aligns final `Gene` representations to the updated
  table
- blocks are block-scoped analysis-ready exports rather than duplicated copies
  of all source-local objects
- one root-level `representation_registry.csv` is the canonical representation
  directory table for `master` and all blocks
- `master` retains all active Task1 representations
- `lincs_internal` retains `Gene` and `Pathway`
- `scperturb_internal` retains `Gene`, `Pathway`, and all active Task1 `FM`
  representations
- `cross` retains `Gene` and `Pathway` only
- each block materializes block-sliced representation matrices for the
  representations lawful on that block
- final snapshot representation storage uses
  `representations/<representation>/...`
- representation paths are stored relative to the Task1 root
- every representation directory uses:
  `matrix.npy`, `row_index.csv`, `feature_index.csv`
- final snapshot matrices use dense `float32` `NPY`
- final representation surfaces use `row_index_path` keyed by `instance_id`
  and do not require matrix row order to match `master/instance_registry.csv`
- source-local `instance_registry.csv` uses a shared harmonized core plus
  source-specific extension columns
- the harmonized instance core is:
  `instance_id`, `dataset`, `cell_line`, `perturbation_type`,
  `perturbation_gene`, `time_hr`, `dose_um`
- `instance_id` is the only persisted instance-level key in the minimal
  contract; `row_id` remains an internal construction and ordering helper
- `LINCS` keeps `sig_id` as the source trace key
- `scPerturb` keeps one canonical treated-cell trace key `cell_id`
- `cell_id` is the `scPerturb` source-local raw-cell trace key rather than the
  benchmark instance key
- `cell_id` is frozen as:
  `{dataset}::{raw_internal_cell_name}`
- `raw_internal_cell_name` means the source-native treated-cell identifier used
  to build `cell_id`
- active human datasets now carry a frozen minimal extraction mapping for
  `cell_id`, `cell_line`, raw `perturbation_type`, identity, `time_hr`,
  `dose_um`, local-context columns, and control rows
- `instance_id` uses the readable composite format
  `{dataset}::{cell_line}::{perturbation_type}::{perturbation_gene}::{time_hr_or_NA}::{dose_um_or_NA}::{source_trace}`,
  with `sig_id` as the `LINCS` source trace and `cell_id` as the `scPerturb`
  source trace
- `sources/scperturb/gene/gene_feature_index.csv` is the global single
  feature-index table for source-local `scPerturb` `Gene` shards
- `sources/scperturb/gene/gene_shard_index.csv` is the source-local shard
  routing table
- each `sources/scperturb/gene/shards/shard_XXXXXX/gene_meta.csv` is
  matrix-near and strictly row-aligned with the same-shard `gene_delta.arrow`
- each `gene_delta.arrow` is an Arrow IPC file with zstd compression
- each `scPerturb` shard has at most `1,000,000` instances and shard order is
  deterministic
- the final canonical shared `Gene` feature table is
  `master/representations/Gene/feature_index.csv`, and `task1_scope_merge.py`
  owns its union-based expansion, uppercase alphabetical ordering, and final
  alignment
- `time_hr` is standardized only from explicit numeric time fields and recorded
  in hours; sentinel, invalid, or missing values are written as `NA`
- `dose_um` is standardized only from explicit numeric doses with convertible
  molar-concentration units (`uM`, `µM`, `micromolar`, `nM`), with `nM`
  converted to `uM`; mass-based units, volume units, unitless dose values, and
  other non-convertible encodings are written as `NA`
- raw source time and dose fields remain preserved in source-specific extension
  columns
- `scPerturb` pairing details live in a dedicated pairing index; the instance
  registry keeps only lightweight pairing summaries
- the dedicated `scPerturb` pairing index lives at
  `sources/scperturb/registry/pairing_index.csv` and is shared by both `Gene`
  delta construction and `FM` handoff
- within the `scPerturb` source-local bundle, `cell_id` remains the canonical
  raw-cell trace key for source-local trace and FM handoff surfaces, while
  downstream delta-instance and benchmark-facing analysis layers continue to use
  `instance_id`
- `scPerturb` FM preparation is owned by `task1_scperturb_fm_prep.py` and
  writes back into the same `scPerturb` bundle
- FM outputs remain delta-space vectors rather than raw embeddings or scalar
  distances
- all active Task1 FM models share one flow-space displacement operator from
  paired controls to treated cells
- per-model `FM` preparation skips failed instances and continues, with final
  `fm_delta` outputs retaining successful instances only
- `unit_membership.parquet` is the canonical unit fact table and
  `unit_registry.csv` is its summary table
- all three Task1 blocks retain actual units only; `cross` contains only units
  with exact `(cell_line, perturbation_type, perturbation_gene)` agreement
  across sources
- under the current active cross slice, this means matched single-gene genetic
  units only
- `unit_registry.csv` is a lightweight identity-plus-counts summary rather than
  a complex unit-status table
- `representation_registry.csv` is a technical directory table with one row per
  `surface + representation`
- `representation_registry.csv` uses fixed `surface` values:
  `master`, `lincs_internal`, `scperturb_internal`, `cross`
- the minimal `representation_registry.csv` columns are:
  `surface`, `representation`, `matrix_path`, `row_index_path`,
  `feature_index_path`, `dtype`
- `master/instance_registry.csv` keeps the harmonized core plus the minimal
  trace extension columns `sig_id` and `cell_id`
- both `bundle_manifest.json` and `snapshot_manifest.json` use the top-level
  sections `identity`, `build`, `inputs`, and `artifacts`
- manifest artifact entries use `artifact_type` plus `artifact_path`
- this checkpoint now freezes the structural task-data ownership of
  `task1_scope_merge.py`, while full field-level registry inventories, the `2A`
  interface, downstream `group/retrieval/metrics/export`, and panel-level
  R scripts remain pending

## Document Inventory

- [01_task1_lincs_prep.md](../../data/preprocessing/lincs.md): dataset-specific `LINCS`
  preprocessing dossier for the current Task1 freeze
- [02_task1_scperturb_prep.md](../../data/preprocessing/scperturb.md): dataset-specific
  `scPerturb` preprocessing dossier for the current Task1 freeze
- [03_shared_pathway_contract.md](../../data/representations/pathway.md): shared
  Hallmark pathway preprocessing contract
- [04_task1_data_snapshot_contract.md](../../data/snapshots/task1.md):
  merged Task1 task-data contract covering source-local bundles, final snapshot
  layout, routing semantics, and core registry ownership
- [06_task1_scperturb_fm_contract.md](../../data/representations/fm.md):
  Task1 `scPerturb` FM delta-preparation contract
- [pending_items.md](2026-09-06_figure2_pending_items.md): intentionally unresolved items that
  remain outside the freeze

## Pending Items

Pending items that remain intentionally unresolved in this checkpoint are
tracked in [pending_items.md](2026-09-06_figure2_pending_items.md). The remaining pending surface
is limited to richer audit payloads, exhaustive full field-level inventories
beyond the now-frozen minimal per-active-human-dataset mapping, `2A`, downstream
`group/retrieval/metrics/export`, and panel-level R scripts. This directory
should not be read as a full Figure 2 phase freeze.

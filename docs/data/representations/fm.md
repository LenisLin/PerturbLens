# Task1 scPerturb FM Representation Contract

## Role

This contract defines the FM-specific representation and data-preparation
boundary for the Task1 `scPerturb` source-local bundle.

## Scientific Purpose

- FM remains a Task1 internal representation family on `scPerturb`
- FM does not enter manuscript-facing Figure 2 panels
- FM data preparation stays consistent with the benchmark rule that each
  instance is a delta-space object

## Script Ownership

- `task1_scperturb_prep.py` filters lawful treated rows, builds `Gene` delta
  objects, and prepares pairing context for FM
- `task1_scperturb_fm_prep.py` performs FM-specific preparation and writes
  outputs back into the same `sources/scperturb/` bundle
- FM extraction may reuse logic patterns from `scripts/fm_extractors/`, but the
  Task1 contract is not required to reuse Task2 file names

## FM Key Model

- final FM outputs are keyed by `instance_id`
- `instance_id` uses the readable composite format:
  `{dataset}::{cell_line}::{perturbation_type}::{perturbation_gene}::{time_hr_or_NA}::{dose_um_or_NA}::{source_trace}`
- for `scPerturb` FM outputs, `source_trace` is the treated `cell_id`
- FM contract surfaces are keyed by source-local canonical `cell_id`
- `cell_id` is the `scPerturb` source-local raw-cell trace key rather than the
  benchmark instance key
- `cell_id` is frozen as:
  `{dataset}::{raw_internal_cell_name}`
- `raw_internal_cell_name` means the source-native treated-cell identifier used
  to build `cell_id`
- default extraction prefers the per-cell name carried by the primary `h5ad`
  object when available; otherwise use the source-native cell-name field from
  the paired observation table
- exact source-specific fallback column detection remains an implementation
  detail rather than a frozen minimal-contract item
- one FM output row corresponds to one successful Task1 instance
- FM output for one retained instance is one vector, not a raw cell embedding
- FM output for one retained instance is not a single scalar distance
- FM values live in delta space and represent perturbation effect
- FM delta is constructed from paired controls and the treated cell in model
  latent space
- when the treated cell embedding exists but a subset of paired control
  embeddings are unavailable, the current FM delta uses the remaining available
  paired control embeddings only if at least `25` paired control embeddings
  remain; otherwise the instance is skipped
- the frozen operator is a flow-space displacement vector from the paired
  control set to the treated cell
- all active FM models share the same delta operator family

## Bundle Inputs Needed By FM

- FM runs only on cells that survive Task1 `scPerturb` filtering
- the legal FM instance anchor is the formal source-local `Gene` shard scope
  written by `task1_scperturb_prep.py`
- the formal source-local `Gene` shard scope is read from:
  `sources/scperturb/gene/gene_shard_index.csv` plus each referenced
  shard-local `gene_meta.csv` and `gene_delta.arrow`
- each referenced `gene_delta.arrow` is an Arrow IPC file with zstd
  compression
- `task1_scperturb_fm_prep.py` must reject registry-only or smoke-like
  `sources/scperturb/` roots that do not contain the formal `Gene` shard scope
- FM embedding reads the selected treated cells plus any required paired control
  cells from the raw single-cell inputs
- Task1 UCE embedding must not apply additional UCE-side gene or cell filtering
  after Task1 lawful cell selection and raw-cell resolution
- Task1 UCE resident sentence sampling is deterministic and order-independent:
  the per-cell sampling RNG is keyed by `(seed, dataset, cell_id)` rather than
  global execution order
- `sources/scperturb/registry/fm_cell_registry.csv` is the canonical worklist
  for FM cell encoding
- `fm_cell_registry.csv` keeps one row per unique raw cell that needs FM
  encoding
- the canonical raw-cell key is `cell_id`
- the minimal `fm_cell_registry.csv` columns are:
  `cell_id`, `dataset`, `cell_line`, `cell_role`, `source_obs_path`
- `cell_role` is frozen to:
  `treated`, `control`
- `source_obs_path` is stored as a path relative to
  `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/scPerturb_Processed`

## Pairing Handoff

- FM preparation consumes the dedicated pairing index and FM-ready raw-cell
  registry written by `task1_scperturb_prep.py`
- `task1_scperturb_prep.py` is the stage that guarantees treated/control role
  semantics and same `dataset`, `cell_line`, and `perturbation_type` pairing
  semantics for fresh builds and validated resume reuse
- `task1_scperturb_fm_prep.py` validates the handoff shape, Gene-scope
  pairing coverage, treated `cell_id` linkage, required raw-cell availability,
  and `cell_role` vocabulary; it does not repeat the upstream same-role and
  same-context semantic proof as a blocking duplicate check
- the dedicated pairing index path is:
  `sources/scperturb/registry/pairing_index.csv`
- the FM-ready raw-cell registry path is:
  `sources/scperturb/registry/fm_cell_registry.csv`
- the pairing index has one row per retained treated instance
- the minimal pairing-index columns are:
  `instance_id`, `cell_id`, `control_cell_ids`
- `cell_id` in the pairing index is the treated-cell id
- within the `scPerturb` source-local bundle, `cell_id` remains the canonical
  raw-cell trace key for `fm_cell_registry.csv`, `pairing_index.csv`, and
  `fm_delta_meta.csv`
- downstream benchmark-facing analysis layers continue to use `instance_id`
- `control_cell_ids` is stored as a `|`-delimited list of paired control
  `cell_id` values

## FM Output Organization

- per-model FM outputs live under `sources/scperturb/fm/<model>/`
- source-local FM naming remains explicit rather than final-snapshot
  representation syntax
- each per-model directory must include:
  `fm_delta.npy`, `fm_delta_meta.csv`, `fm_feature_index.csv`
- `fm_delta_meta.csv` remains row-aligned with `fm_delta.npy`
- the minimal `fm_delta_meta.csv` columns are:
  `instance_id`, `dataset`, `cell_line`, `perturbation_type`,
  `perturbation_gene`, `time_hr`, `dose_um`, `cell_id`
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
- no `fm_delta_failures.csv`, JSONL sidecar, line-level failure sidecar, or
  other formal failure artifact is defined in the current freeze
- if FM extraction fails for a subset of retained instances, skip failed
  instances and continue building the per-model outputs
- `fm_delta.npy` and `fm_delta_meta.csv` contain successful instances only
- failure details may remain in runtime logs, stage metadata, model-runtime
  summaries, console errors, or summary statistics
- `fm_feature_index.csv` keeps one column:
  `feature_id`
- for FM representations, `feature_id` stores the `0-based` latent dimension
  index
- `task1_scperturb_fm_prep.py --overwrite` deletes and rebuilds only requested
  per-model directories under `sources/scperturb/fm/<model>/`
- without `--overwrite`, complete valid per-model outputs are reused and
  recorded as `reused_existing`; invalid requested model outputs are deleted
  before rebuild
- `sources/scperturb/bundle_manifest.json` records the current valid FM state on
  disk rather than append-only stage history
- `bundle_manifest.json` is not an authority for discovering the active FM
  model universe
- `fm_models_materialized` lists currently valid outputs for contract-approved
  active FM families only, including valid unrequested approved model
  directories and excluding stale, failed, or contract-unapproved model
  directories

## Acceptance Gate

- FM acceptance is evaluated against the formal source-local `Gene` shard
  instance scope
- formal active-FM materialization is complete only when every formally
  requested active FM family succeeds its per-model acceptance gate
- partial active-model success is a `failed` or `partial_failure` stage state;
  any valid model outputs left on disk are diagnostic current disk state only
  and are not a formal completed materialization
- `fm_delta_meta.csv` may contain successful FM rows only
- every `fm_delta_meta.csv.instance_id` must be a subset of the formal `Gene`
  shard scope
- `task1_scperturb_fm_prep.py` records:
  `gene_scope_instances`, `successful_instances`, `instance_coverage`,
  and `fm_min_instance_coverage`
- `instance_coverage = successful_instances / gene_scope_instances`
- the current runtime threshold is the explicit parameter
  `--min-instance-coverage`; the current default is `0.50`
- empty FM outputs fail the coverage gate
- the FM acceptance gate does not compare `Gene` delta values with `FM` delta
  values

## Active FM Families

This section is the only authoritative active FM model universe for
`task1_scperturb_fm_prep.py`. The script reads active families from the bullets
below. Adding or removing an active FM family requires editing this section.

- `scgpt`
- `geneformer`
- `scbert`
- `scfoundation`
- `uce`
- `state`
- `tahoe-x1`

## Out Of Scope

- final `master/` and `blocks/` snapshot layout
- downstream group and retrieval metric tables
- manuscript-facing FM panel contracts outside the approved Figure `3F` scope

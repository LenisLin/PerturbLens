# Runbook

## Execution Stage Crosswalk

These identifiers describe the retained stage/output mapping, not completion
status or the top-level documentation organization. See
[state](state.md) for execution limitations and [the index](../README.md) for
current contract owners.

| Stage | Purpose | Primary outputs |
| --- | --- | --- |
| `S0` | data inventory | `task1_data_inventory_long.csv`, `data_source_manifest.csv` |
| `S1` | Task1 internal metrics | `task1_group_concordance_long.csv`, `task1_retrieval_per_query.parquet`, `task1_retrieval_summary.csv`, `task1_leaderboard_long.csv` |
| `S2` | Task1 cross metrics | `task1_group_concordance_long.csv`, `task1_retrieval_per_query.parquet`, `task1_retrieval_summary.csv`, `task1_cross_alignment_proof.csv` |
| `S3` | Task2 multisource cohort build | `task2_pairs_coverage.csv`, `task2_row_membership.parquet`, `delta_meta.csv`, `representation_availability_registry.csv`, `snapshot_manifest.json` |
| `S4` | Task2 group concordance | `task2_group_concordance_long.csv`, `task2_group_leaderboard.csv` |
| `S5` | Task2 retrieval | `task2_retrieval_per_query.parquet`, `task2_retrieval_summary_long.csv`, `task2_retrieval_leaderboard.csv` |
| `S6` | Task2 synthesis | `task2_benchmark_summary_long.csv` |
| `S7` | project synthesis | `project_input_registry.csv`, `project_benchmark_summary_long.csv`, `project_axis_score_inputs_long.csv`, `project_representation_scorecard.csv` |

## Active Roots

Use the canonical roots in the [storage policy](storage_policy.md). The
task-specific paths below describe how those roots are used by the existing
local preparation interfaces.

## Execution Environment

- The default local source checkout and command-invocation path is:
  `/home/lenislin/Experiment/projects/M2M`
- The local checkout remains source-only. Task data, stage runs, and plot
  exports must not be written back into the repo working tree.
- The current Task1 data-prepare scripts run on the host in the
  `OSMOSIS_V2` conda environment.
- In `task1_scperturb_fm_prep.py`, the non-`tahoe-x1` FM families run in the
  host `OSMOSIS_V2` environment, except `STATE` may use one dedicated Python
  runtime created or maintained by `uv` under the local STATE model tree.
- `STATE` runtime invocation must be explicit: use `--state-python` or the
  auto-discovered `<benchmark-root>/state/.venv/bin/python`. Runtime
  `uv run state` commands remain disallowed; `uv` is only for one-time
  environment creation/maintenance, and the selected Python executable path is
  recorded in model-runtime summaries without resolving away the dedicated
  `.venv/bin/python` entrypoint.
- In `task1_scperturb_fm_prep.py`, `tahoe-x1` runs through the local named
  Docker container `my_experiment_container`, not through direct host-Python
  inference.
- If `my_experiment_container` exists but is stopped, start it before
  `docker exec`; if it does not exist, fail explicitly.
- `task1_scperturb_fm_prep.py` reads the active FM model universe only from
  `docs/data/representations/fm.md` under
  `## Active FM Families`.
- `sources/scperturb/bundle_manifest.json` records valid materialized FM model
  state only; it is not used for active model discovery.
- Full Task1 scPerturb FM production runs should use
  `task1_scperturb_fm_prep.py --model <family>` one family at a time. The
  legacy `--models` multi-family path remains for compatibility and smoke
  checks, but single-model runs are the recommended resource-control boundary.
- For Task1 UCE runs, `task1_scperturb_fm_prep.py` now uses the external UCE
  resident runtime API directly rather than the old per-segment
  `eval_single_anndata.py` subprocess path. The CLI wrapper remains available
  for external use, but Task1 no longer uses per-segment `h5ad` roundtrips.
- Task1 UCE resident runs keep additional UCE-side filtering disabled, use
  default `cell_chunk_size=32768`, and when `--batch-size` is omitted default
  to the conservative resident batch size `128` inferred from current host
  validation. Explicit `--auto-batch-size` remains available for diagnostic
  tuning only.
- `task1_scperturb_fm_prep.py` writes internal per-dataset fragments under the
  stage-local `working/<model>/dataset_fragments/` tree before final assembly.
  These fragments are recovery inputs, not formal source-bundle artifacts.
- For recovery, use `--resume-stage-dir <previous task1_scperturb_fm_prep stage>`
  plus optional `--datasets <dataset,...>` to re-encode selected datasets and
  assemble from the current fragments first, then read-only previous fragments.
- For `scgpt`, production runs should keep `--num-workers 1` unless a smaller
  smoke test proves the host DataLoader path is stable with a higher value.
  This limits upstream worker fanout through CPU-affinity control.

## Task1 Data-Prepare Paths

- The final Task1 task-data snapshot writes to:
  `/mnt/NAS_21T/ProjectData/M2M/data/task1`
- The Task1 data-prepare source-local bundle outputs write under:
  `/mnt/NAS_21T/ProjectData/M2M/data/task1/sources/lincs` and
  `/mnt/NAS_21T/ProjectData/M2M/data/task1/sources/scperturb`
- The merged Task1 snapshot outputs write under:
  `/mnt/NAS_21T/ProjectData/M2M/data/task1/master` and
  `/mnt/NAS_21T/ProjectData/M2M/data/task1/blocks`
- The Task1 data-prepare run working root is:
  `/mnt/NAS_21T/ProjectData/M2M/runs/<run_id>`
- Each Task1 data-prepare stage writes one isolated working directory at:
  `/mnt/NAS_21T/ProjectData/M2M/runs/<run_id>/<stage_name>`
- The current Task1 data-prepare stage names are:
  `task1_lincs_prep`, `task1_scperturb_prep`, `task1_scperturb_fm_prep`, and
  `task1_scope_merge`

## Stage Bundle Rule

Every stage writes:

- `run_manifest.json`
- `audit_assertions.json`
- `manifest.json`
- the stage tables defined in `docs/tasks/output_schemas.md`

## Stage Execution Rules

- One stage writes to one run directory.
- One Task1 data-prepare attempt uses one `run_id`, and its four stage working
  directories share that `run_id`.
- For Task1 data-prepare stages, `--overwrite` means a clean rebuild of the
  outputs owned by that stage rather than reuse of stale files.
- For `task1_scperturb_prep.py`, the clean-rebuild overwrite boundary includes:
  `/mnt/NAS_21T/ProjectData/M2M/runs/<run_id>/task1_scperturb_prep/`,
  `sources/scperturb/bundle_manifest.json`,
  `sources/scperturb/registry/instance_registry.csv`,
  `sources/scperturb/registry/pairing_index.csv`,
  `sources/scperturb/registry/fm_cell_registry.csv`,
  `sources/scperturb/gene/gene_feature_index.csv`,
  `sources/scperturb/gene/gene_shard_index.csv`, and
  `sources/scperturb/gene/shards/`.
- For `task1_scperturb_prep.py`, `sources/scperturb/fm/` remains outside the
  current overwrite cleanup boundary because it is owned by
  `task1_scperturb_fm_prep.py`.
- For `task1_scperturb_fm_prep.py`, the overwrite and rebuild boundary is
  limited to requested `sources/scperturb/fm/<model>/` directories. It must not
  modify `sources/scperturb/gene/`, `sources/scperturb/registry/`, or
  unrequested FM model directories.
- For `task1_scperturb_fm_prep.py`, the legal input anchor is the formal
  `sources/scperturb/gene/gene_shard_index.csv` scope and the referenced
  `gene_meta.csv`/`gene_delta.arrow` shard files. Registry-only roots are
  invalid FM inputs even if `bundle_manifest.json` exists.
- For `task1_scperturb_fm_prep.py`, the FM acceptance gate uses successful
  `fm_delta_meta.csv.instance_id` coverage over that formal Gene shard scope.
  It does not compare `Gene` delta values with `FM` delta values. The runtime
  parameter `--min-instance-coverage` is recorded in manifest/audit metadata.
- For formal `task1_scperturb_fm_prep.py` active-FM materialization, every
  formally requested active FM family must complete. Partial active-model
  success is a `failed` or `partial_failure` stage state; valid per-model
  outputs left on disk are diagnostic/current disk state, not formal
  completion.
- The formal `task1_scperturb_fm_prep.py` stage gate is `py_compile`/contract
  tests, per-model completion, and coverage validation. Additional automated
  backend smoke outputs are not part of the formal stage bundle or formal gate.
- FM failure triage stays log/metadata based: use runtime logs, stage metadata,
  model-runtime summaries, and console errors. Do not add
  `fm_delta_failures.csv`, JSONL sidecars, or other formal failure artifacts.
- Common FM failures include CUDA OOM and instance/cell mismatch. Triage OOM
  through batch, cell chunk, and runtime settings; triage instance/cell
  mismatch against the Gene shard scope, `pairing_index`, `fm_cell_registry`,
  and raw h5ad obs-name alignment.
- For `task1_scperturb_prep.py`, `--resume-stage-dir` may point to a previous
  `runs/<old_run_id>/task1_scperturb_prep/` stage. Resume only reuses
  dataset-local stage payloads after validating fragment columns, dataset
  identity, row alignment, treated/control handoff semantics, current raw-input
  `perturbation_type` consistency, and `gene_delta.arrow` shape against the
  current source-local feature index. Legacy `gene_delta.npy` resume payloads
  are accepted only through the same validation path and are converted to final
  Arrow shards. The current run still rebuilds the final `sources/scperturb/`
  bundle from validated reused payloads plus newly computed dataset payloads.
- `--resume-stage-dir` must differ from the current stage directory, and
  `--overwrite` cleanup must not delete the referenced historical stage.
- Task2 core metrics stay within each `dataset` and `cell_line`.
- `C2G` and `G2C` stay separate in Task2 retrieval outputs.
- The local checkout is source-only.

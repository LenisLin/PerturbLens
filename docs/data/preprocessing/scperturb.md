# Task1 scPerturb Preprocessing Contract

## Manuscript Anchor

This data contract defines the upstream human-only `scPerturb` preprocessing
inputs used by the Task1 analyses. It does not map to a standalone Figure 2
panel; the current Figure 2 panel mapping remains an output concern.

## Scientific Purpose

This contract defines how human-only `scPerturb` inputs are ingested, paired
against controls, and converted into lawful Task1 delta objects and registries
without expanding manuscript-facing Figure 2 scope.

## Raw Inputs

The authoritative raw directory for the current freeze is:

- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/scPerturb_Processed`

The source-bundle evaluator scans the directory-wide ingest surface:

- all `Cleaned_*_obs.csv`
- paired `Cleaned_<dataset>.h5ad`

The current Task1 `scPerturb` source bundle is human-only at source-bundle
time:

- retain only rows with `organism == human`
- if a raw source mixes species, retain only its human rows
- if a raw source is entirely non-human, it does not enter the current Task1
  `scPerturb` source bundle
- the current Figure 2 Task1 freeze does not perform ortholog mapping

## Ingest Freeze

- formal source ingest scans the raw root for `Cleaned_*_obs.csv` and paired
  `Cleaned_<dataset>.h5ad`
- dataset entry into the current Task1 `scPerturb` source bundle is controlled
  by the frozen human dataset mapping table below
- the source-bundle evaluator matches raw files against that frozen mapping and
  rejects incomplete `obs/h5ad` pairs for datasets that otherwise match the
  freeze
- row-level lawful filtering runs only on human dataset files selected through
  that frozen mapping
- after the human-only filter, raw `perturbation_type` values are normalized
  into the benchmark vocabulary:
  - `drug` and equivalent compound modes map to `chemical`
  - `CRISPR`, `CRISPRa`, `CRISPRi`, and equivalent genetic modes such as
    `CRISPR-cas9` and `CRISPR-cas13` map to `genetic`
- rows that do not normalize to `chemical` or `genetic` do not enter lawful
  Task1 scope

## Formal CLI Surface

The frozen formal CLI parameter set is:

- `--project-root`
- `--run-id`
- `--task1-root`
- `--runs-root`
- `--seed`
- `--workers`
- `--overwrite`
- `--datasets`
- `--resume-stage-dir`
- `--scperturb-raw-root`

For `task1_scperturb_prep.py`, `--overwrite` is frozen as clean rebuild
semantics for stage-owned outputs. An overwrite run rebuilds
`runs/<run_id>/task1_scperturb_prep/` from empty state and also rebuilds the
current stage-owned `sources/scperturb/` registry plus `Gene` surface from
empty state. The overwrite cleanup boundary covers:

- `sources/scperturb/bundle_manifest.json`
- `sources/scperturb/registry/instance_registry.csv`
- `sources/scperturb/registry/pairing_index.csv`
- `sources/scperturb/registry/fm_cell_registry.csv`
- `sources/scperturb/gene/gene_feature_index.csv`
- `sources/scperturb/gene/gene_shard_index.csv`
- `sources/scperturb/gene/shards/`

`--datasets` is an operational subset filter for side-run recovery: it limits
which dataset payloads are computed and emitted by the current run, but the
stage feature index and gene-delta feature axis remain based on the full lawful
scPerturb dataset set so the resulting fragments can be reused by a later
full-scope assemble run.

`--resume-stage-dir` may be provided multiple times. Reusable dataset-local
payloads are searched in CLI order, and the first semantically valid payload for
each dataset is reused.

`sources/scperturb/fm/` remains outside this overwrite cleanup boundary and is
owned by `task1_scperturb_fm_prep.py`.

`--resume-stage-dir` is an optional safety mechanism for failed
`task1_scperturb_prep.py` attempts. It points to a previous
`runs/<old_run_id>/task1_scperturb_prep/` stage and may reuse only
dataset-local payloads under `parallel_shards/`:

- `parallel_shards/<dataset>.gene_delta.arrow`
- `parallel_shards/<dataset>.gene_meta.csv`
- `parallel_shards/dataset_fragments/<dataset>.instance_registry.csv`
- `parallel_shards/dataset_fragments/<dataset>.pairing_index.csv`
- `parallel_shards/dataset_fragments/<dataset>.fm_cell_registry.csv`

Historical resume stages may still contain legacy
`parallel_shards/<dataset>.gene_delta.npy`; validators may reuse those payloads
after shape and semantic validation, but final source-local shards are
materialized as Arrow IPC + zstd. Reuse is not based on file existence alone. A
dataset payload is reusable only
when all fragment schemas, dataset identity fields, row alignment across
`instance_registry.csv`, `pairing_index.csv`, and `gene_meta.csv`, matrix row
count, matrix feature count, treated `cell_id` linkage, pairing
`control_cell_ids`, and `fm_cell_registry.csv` treated/control role semantics
match the current run contract. The resume validator must reject payloads whose
treated rows no longer match the current raw-input semantics, whose paired
controls are not recorded as `control` cells in the FM cell registry, whose
paired control registry rows do not match the treated row's `dataset` and
`cell_line`, or whose paired controls do not match the treated row's current
`perturbation_type`. Invalid or incomplete payloads are recomputed by the
current scheduler. Resume never reuses a final `sources/scperturb/` bundle
directly; the current run always assembles a complete bundle from the union of
validated reused dataset payloads and newly computed dataset payloads.

## Treated-Control Pairing Contract

- each treated cell is paired to `50` controls
- all pairing uses fixed global seed `619`
- base eligible control pool = same `dataset` + same `cell_line` + same
  normalized `perturbation_type`
- local context is matched through the frozen single-field priority chain
  before fallback to the base control pool
- if no local-context field yields at least `2` eligible controls, fallback to
  the base eligible control pool before deterministic sampling
- control selection uses deterministic sampling with replacement
- repeated runs with the same inputs must be stable
- fresh-build pairing semantics are guaranteed by this stage, not by the FM
  materialization stage
- the implementation may materialize pairing through stable integer control
  positions and a deterministic `(n_treated, 50)` control-index matrix, but
  the persisted pairing contract remains one treated row plus `50`
  with-replacement controls
- `pairing_index.csv` stores the final `control_cell_ids`; the matrixized
  pairing core may keep integer positions until final write-out
- control selection must be deterministic and stable under repeated runs
- resume reuse must validate that reused treated rows, pairing rows, and
  `fm_cell_registry.csv` rows preserve the treated/control handoff semantics
  that fresh-build pairing would have produced
- the pairing seed must be written into source-local bundle build metadata and
  carried into snapshot build metadata
- chosen control ids must be written into the pairing index
- the control pool does not require the same target gene as the treated cell
- default behavior does not apply secondary-background matching
- hash / hashtag / oligo related columns do not enter the current pairing
  contract
- implementation may use dataset-local index or bucket routing and matrixized
  pairing compute, but the contract semantics above are unchanged

## Local Experimental Context

`local experimental context` means explicit technical, acquisition, or
blocking variables that may affect expression distributions independently of
the perturbation identity.

Eligible default local-context fields are:

- `sample`
- `batch`
- `plate`
- `gemgroup`
- `lane`
- `replicate`

If a raw dataset uses `plate_id`, it is normalized to canonical `plate` before
matching and before writing `local_context_key_used`.

The frozen priority order is:
`sample > batch > plate > gemgroup > lane > replicate`.

The matching algorithm is fixed:

- test the fields above one at a time in that order
- as soon as one field yields at least `2` eligible controls, use that field
  and stop
- if none of the fields yields at least `2` eligible controls, use
  `base_pool`

`local_context_key_used` is frozen to the vocabulary:

- `sample`
- `batch`
- `plate`
- `gemgroup`
- `lane`
- `replicate`
- `base_pool`

`well` and `well_id` do not enter the default global local-context rule.

## Delta Operator

- `Gene delta = x_treat - mean(sampled_controls)`
- no z-score transformation is applied in this preprocessing stage
- no clipping is applied in this preprocessing stage

## Implementation Freeze

- dataset scheduling may use dataset-level multiprocessing with `spawn`
- dataset execution priority may use ascending `h5ad` file size so smaller
  datasets finish and expose errors earlier
- pairing may use dataset-level multiprocessing together with dataset-local
  base-pool indexing on `(dataset, cell_line, perturbation_type)`, local bucket
  routing, and matrixized control-index construction while preserving the
  frozen pairing semantics above
- `Gene delta` compute may use chunked matrixized subtraction on treated rows
  and sampled control-index matrices before projection into the source-local
  feature union

## Perturbation Identity Freeze

All lawful `scPerturb` rows in the current Task1 scope normalize to the
benchmark `perturbation_type` values `chemical` or `genetic`.

Chemical identity is frozen as:

- general chemical rows must resolve to one canonical target-set string to
  remain lawful
- if a chemical row does not have a usable and standardizable target-set, it
  is excluded from lawful Task1 scope
- chemical `perturbation_gene` canonicalization is: uppercase, dedup,
  alphabetical order, `|` delimiter

Genetic identity is frozen as:

- the default genetic `perturbation_gene` is one perturbed gene
- `scPerturb` internal may retain multi-gene genetic rows
- retained multi-gene genetic rows canonicalize raw gene tokens into one
  gene-set string using: uppercase, dedup, alphabetical order, `|` delimiter
- canonicalization example:
  `MMAB_MAT2A -> MAT2A|MMAB`
- this multi-gene genetic extension is valid for `scPerturb` internal only
- the current Task1 cross block accepts matched single-gene genetic rows only
- multi-gene genetic rows do not enter the current Task1 cross block

## Combo Handling

- true multi-factor rows with non-control-equivalent `perturbation_2` are
  excluded by default
- if `perturbation_2` is a semantic control-equivalent background state, the
  row remains lawful and `perturbation_2` does not define `perturbation_gene`
- control-equivalent examples include `control` and `unstimulated`
- the only retained exception is
  `Cleaned_SrivatsanTrapnell2020_sciplex4_obs.csv` drug-drug combinations
- excluded multi-factor families include `CRISPR + TCR stimulation` and
  `CRISPR + IFN-gamma stimulation`

## sciplex4 Special Case

- `sciplex4` remains the only retained combo exception in the current Figure 2
  preprocessing freeze
- `sciplex4` also remains the only chemical identity exception in the current
  Figure 2 Task1 freeze
- `target` does not define `perturbation_gene` identity for `sciplex4`
- chemical `perturbation_gene` for `sciplex4` uses canonicalized tokens from
  the `perturbation` column
- canonicalization uses: split `perturbation` on `_`, uppercase tokens,
  remove duplicates, sort alphabetically, join with `|`
- row classification is frozen as:
  `nperts == 0` and `perturbation == control` = untreated controls
- row classification is frozen as:
  `nperts == 1` and `perturbation != control` = lawful single-drug treated
  rows
- row classification is frozen as:
  `nperts == 2` = lawful combo treated rows
- rows such as `control + Pracinostat` and `control + Abexinostat` are lawful
  single-drug treated rows and do not enter the untreated control pool

## Active Human Dataset Mapping Freeze

This table replaces open-ended source-specific fallback detection. The listed
`cell_id` source is the frozen `raw_internal_cell_name` extraction source for
that dataset. Chemical identity uses the listed source only. Genetic
multi-gene rows use `perturbation` tokenization only; guide-level columns stay
as audit trace fields rather than `perturbation_gene` identity sources.

The current active human source files on this ingest surface are:

| Dataset(s) | `cell_id` source | `cell_line` source | Raw `perturbation_type` -> normalized | Chemical identity source | Genetic multi-gene token source | `time_hr` source | `dose_um` source | Local-context candidate columns | Control-row definition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AdamsonWeissman2016_GSM2406675_10X001`, `AdamsonWeissman2016_GSM2406677_10X005`, `AdamsonWeissman2016_GSM2406681_10X010` | `obs.csv cell_barcode` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | none | `perturbation == control` |
| `AissaBenevolenskaya2021` | `obs.csv cell_barcode` | `cell_line` | `drug -> chemical` | `perturbation` as canonical target-set string | `NA` | `time` | `NA` | `batch` | `perturbation == control` |
| `ChangYe2021` | `obs.csv Unnamed: 0` | `sample` | `drug -> chemical` | `perturbation` as canonical target-set string | `NA` | `NA` | `dose_value + dose_unit` | `sample` | `perturbation == control` |
| `DatlingerBock2017` | `obs.csv cell_barcode` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene; `perturbation_2` lawfulness follows `Combo Handling` | `NA` | `NA` | `replicate` | `perturbation == control` |
| `DatlingerBock2021` | `obs.csv cell_barcode` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene; `perturbation_2` lawfulness follows `Combo Handling` | `NA` | `NA` | `sample` | `perturbation == control` |
| `FrangiehIzar2021_RNA` | `obs.csv cell_name` | `celltype` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene; `perturbation_2` lawfulness follows `Combo Handling` | `NA` | `NA` | none | `perturbation == control` |
| `LotfollahiTheis2023` | `obs.csv cell_barcode` | `cell_line` | `drug -> chemical` | `perturbation` as canonical target-set string | `NA` | `NA` | `NA` | none | `perturbation == control` |
| `McFarlandTsherniak2020` | `obs.csv Unnamed: 0` | `cell_line` | `drug -> chemical`; `CRISPR -> genetic` | chemical rows use `perturbation` as canonical target-set string | genetic rows use `perturbation`, split on `_` when multi-gene | `time` | `dose_value + dose_unit` | none | `perturbation == control` |
| `NadigOConner2024_hepg2`, `NadigOConner2024_jurkat` | `obs.csv cell_barcode` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | `batch` | `perturbation == control` |
| `NormanWeissman2019_filtered` | `obs.csv Unnamed: 0` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | `gemgroup` | `perturbation == control` |
| `PapalexiSatija2021_eccite_RNA`, `PapalexiSatija2021_eccite_arrayed_RNA` | `obs.csv Unnamed: 0` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | none | `perturbation == control` |
| `ReplogleWeissman2022_K562_essential`, `ReplogleWeissman2022_rpe1` | `obs.csv cell_barcode` | `cell_line` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | `batch` | `perturbation == control` |
| `ShifrutMarson2018` | `obs.csv Unnamed: 0` | `celltype` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene; `perturbation_2` lawfulness follows `Combo Handling` | `NA` | `NA` | `sample` | `perturbation == control` |
| `SrivatsanTrapnell2020_K562` | `obs.csv Unnamed: 0` | `cell_line` | `drug -> chemical` | `target`; rows without a standardizable canonical target-set are excluded | `NA` | `time` | `dose_value + dose_unit` | `plate`, `replicate` | `perturbation == control` |
| `SrivatsanTrapnell2020_sciplex2` | `obs.csv cell_barcode` | `cell_line` | `drug -> chemical` | `perturbation` as canonical target-set string | `NA` | `NA` | `dose_value` only, so `dose_um = NA` when no convertible unit is present | none | `perturbation == control` |
| `SrivatsanTrapnell2020_sciplex4` | `obs.csv cell_barcode` | `cell_line` | `drug -> chemical` | `perturbation` token canonicalization on `_`; this is the sole token-based exception and does not use `target` | `NA` | `NA` | `dose_value` only, so `dose_um = NA` when no convertible unit is present | `plate_id -> plate` | `nperts == 0` and `perturbation == control` |
| `SunshineHein2023` | `obs.csv cell_barcode` | `cell_line` | `CRISPR-cas9 -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | none | `perturbation == control` |
| `TianKampmann2019_day7neuron`, `TianKampmann2021_CRISPRa`, `TianKampmann2021_CRISPRi` | `obs.csv Unnamed: 0` | `celltype` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | `batch` | `perturbation == control` |
| `TianKampmann2019_iPSC` | `obs.csv Unnamed: 0` | `celltype` | `CRISPR -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | `batch` | `perturbation == control` |
| `WesselsSatija2023` | `obs.csv cell_barcode` | `cell_line` | `CRISPR-cas13 -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | none | `perturbation == control` |
| `XuCao2023` | `obs.csv cell_barcode` | `cell_line` | `CRISPRi -> genetic` | `NA` | `perturbation`, split on `_` when multi-gene | `NA` | `NA` | none | `perturbation == control` |
| `ZhaoSims2021` | `obs.csv cell_barcode` | `sample` | `drug -> chemical` | `perturbation` as canonical target-set string | `NA` | `NA` | `dose_value + dose_unit` | `sample` | `perturbation == control` |

## FM Reuse Rule

- `FM` extraction logic may reuse code patterns from
  [`scripts/fm_extractors`](../../../scripts/fm_extractors)
- `task1_scperturb_prep.py` does not own final `FM` delta materialization
- `task1_scperturb_fm_prep.py` writes model-specific `FM` delta outputs back
  into the same `scPerturb` source-local bundle after lawful treated-cell
  filtering and pairing preparation are complete

## Output Contract

This preprocessing stage materializes:

- native `Gene` delta shards
- single-column global `gene_feature_index.csv` for the `Gene` representation
- global `gene_shard_index.csv`
- pairing index
- preprocessing registries
- instance registry / metadata table
- FM-ready cell and pairing handoff surfaces

This preprocessing stage does not materialize the final manuscript-valid shared
`Pathway` representation or the final canonical shared `Gene` feature table.
Final shared `Pathway` ownership and final shared `Gene` feature-table
ownership remain downstream in `task1_scope_merge.py`, which deterministically
unions standardized uppercase gene symbols and writes the final canonical
shared `Gene` order in uppercase alphabetical order.

This preprocessing stage also does not materialize final model-specific `FM`
delta outputs. Final `FM` delta materialization is owned by
`task1_scperturb_fm_prep.py`, which writes model-specific outputs back into the
same `scPerturb` source-local bundle.

The frozen source-local `Gene` layout is:

- `sources/scperturb/gene/gene_feature_index.csv`
- `sources/scperturb/gene/gene_shard_index.csv`
- `sources/scperturb/gene/shards/shard_000000/gene_delta.arrow`
- `sources/scperturb/gene/shards/shard_000000/gene_meta.csv`
- `sources/scperturb/gene/shards/shard_000001/...`

For this layout:

- each shard `gene_meta.csv` is the matrix-near row-metadata table for the
  same-shard `gene_delta.arrow`
- each shard `gene_meta.csv` is strictly row-aligned with the same-shard
  `gene_delta.arrow`
- each `gene_delta.arrow` is an Arrow IPC file using zstd compression with a
  single `delta` column of `fixed_size_list(float32, n_features)`
- `gene_feature_index.csv` is the global single column-index table for all
  `scPerturb` source-local `Gene` shards
- `gene_shard_index.csv` is the source-local shard routing table
- `instance_registry.csv` remains one global source-local registry
- `pairing_index.csv` remains one global source-local pairing registry
- `fm_cell_registry.csv` remains one global source-local FM-ready raw-cell
  registry
- each shard has at most `1,000,000` instances
- shard order is deterministic
- under `--overwrite`, this stage clean-rebuilds the stage-owned source-local
  registry and `Gene` outputs from empty state before writing the current run
- after a successful overwrite run, `bundle_manifest.json`,
  `instance_registry.csv`, `pairing_index.csv`, `fm_cell_registry.csv`,
  `gene_feature_index.csv`, `gene_shard_index.csv`, and the shard directories
  must correspond one-to-one to the current run contents

The minimal per-shard `gene_meta.csv` columns are:

- `instance_id`
- `dataset`
- `cell_line`
- `perturbation_type`
- `perturbation_gene`
- `time_hr`
- `dose_um`

The row order of `gene/gene_feature_index.csv` must match the column order of
every shard `gene_delta.arrow`.

`gene_feature_index.csv` keeps one column:

- `feature_id`

For the `Gene` representation, `feature_id` stores the source-local
standardized gene symbol used by this preprocessing bundle. The final canonical
shared `Gene` feature table is owned downstream by `task1_scope_merge.py`.

The harmonized core must include at least:

- `instance_id`
- `dataset`
- `cell_line`
- `perturbation_type`
- `perturbation_gene`
- `time_hr`
- `dose_um`

`scPerturb`-specific extension columns must include at least:

- treated-cell trace:
  `cell_id`
- lightweight pairing summary:
  `local_context_key_used`, `n_sampled_controls`
- raw source time and dose fields when present
- source row identifier as an audit trace field

`instance_id` is the only persisted instance-level key in the minimal contract.

`instance_id` uses the readable composite format:
`{dataset}::{cell_line}::{perturbation_type}::{perturbation_gene}::{time_hr_or_NA}::{dose_um_or_NA}::{source_trace}`.

For `scPerturb`, `source_trace` is `cell_id`.

`cell_id` is the `scPerturb` source-local raw-cell trace key rather than the
benchmark instance key.

`cell_id` is frozen as:
`{dataset}::{raw_internal_cell_name}`.

`raw_internal_cell_name` means the source-native treated-cell identifier used
to build `cell_id`. Its source is frozen per dataset in
`Active Human Dataset Mapping Freeze`. Source-specific fallback detection does
not remain open in this contract.

Missing `time_hr` or `dose_um` values are written as `NA`.

`time_hr` is populated only from explicit numeric time fields and is recorded in
hours.

Sentinel, invalid, or missing source time values are written as `NA`.

`dose_um` is populated only when the source provides an explicit numeric dose
with a unit that can be converted into molar concentration.

Accepted dose units for standardization are:
`uM`, `µM`, `micromolar`, and `nM`.

`nM` values are converted to `uM`.

Mass-based units, volume units, unitless dose values, and other non-convertible
dose encodings are written as `NA` in `dose_um`.

Raw source time and dose fields remain preserved in source-specific extension
columns.

Any contiguous treated-instance row numbering remains an internal construction
and ordering helper rather than a required persisted field.

The detailed treated-control pairing contract is carried by the dedicated
pairing index. The source-local `instance_registry.csv` must not inline the full
sampled control-id list.

The dedicated pairing index path is:
`sources/scperturb/registry/pairing_index.csv`.

The pairing index is generated upstream of both `Gene` delta construction and
`FM` extraction handoff. It is not an `FM`-only artifact.

Within the `scPerturb` source-local bundle, `cell_id` remains the canonical
raw-cell trace key for `instance_registry.csv`, `pairing_index.csv`,
`fm_cell_registry.csv`, and `fm_delta_meta.csv`.

The dedicated pairing index is a treated-instance-level table. Its minimal
columns are:

- `instance_id`
- treated `cell_id`
- `control_cell_ids`

When present in `instance_registry.csv`, `local_context_key_used` must use one
of the frozen values from `Local Experimental Context`.

`control_cell_ids` is stored as a `|`-delimited list of paired control
`cell_id` values.

Task1 unit semantics remain:
`(dataset, cell_line, perturbation_type, perturbation_gene)` for internal
analysis, with later cross matching defined on
`(cell_line, perturbation_type, perturbation_gene)` for matched single-gene
genetic rows only.

## QC Surface

Additional review outputs may include:

- control-pool review tables
- pairing summary tables
- delta validity review tables

These outputs are non-manuscript QC surfaces and do not define
manuscript-facing panel inputs.

## Figure 2 Guardrail

`FM` may be materialized at preprocessing time for all-reps raw analysis
support, but `FM` does not enter manuscript-facing Figure 2 panel contracts.

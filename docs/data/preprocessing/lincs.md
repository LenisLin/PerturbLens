# Task1 LINCS Preprocessing Contract

## Manuscript Anchor

This data contract defines the upstream `LINCS` preprocessing inputs used by
the Task1 analyses. It does not map to a standalone Figure 2 panel; the
current Figure 2 panel mapping remains an output concern.

## Scientific Purpose

This contract defines how raw `LINCS` signatures are converted into lawful Task1
delta-space objects and registries for the current Figure 2 preprocessing
freeze.

## Raw Inputs

- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/level5_beta_all_n1201944x12328.gctx`
- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/siginfo_beta.txt`
- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/cellinfo_beta.txt`
- `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/geneinfo_beta.txt`

## Field Mapping To Task1

- `cell_iname -> cell_line`
- `pert_type` maps the retained signature into the Task1
  `perturbation_type` family
- retained `trt_cp -> chemical`
- retained `trt_xpr -> genetic`
- retained `trt_xpr` genetic identity uses `uppercase(cmap_name)` as
  `perturbation_gene`
- `pert_idose` and `pert_time` remain metadata only and do not enter the
  Task1 unit

## Inclusion Rules

- retain only `trt_cp` and `trt_xpr` rows with `qc_pass == 1`
- retained `trt_cp -> chemical`
- retained `trt_xpr -> genetic`
- other `pert_type` families do not enter the current Figure 2 preprocessing
  contract

## Signature Retention Rule

- one retained `sig_id` row equals one benchmark instance for this
  preprocessing layer
- deterministic output row order follows filtered `siginfo_beta.txt`
  source-file order

## Gene Delta Contract

- `Gene delta` is the retained Level5 signature vector directly
- no additional normalization is applied in this preprocessing stage
- no clipping is applied in this preprocessing stage
- `task1_lincs_prep.py` keeps `Gene delta` in native `LINCS` Level5 gene
  space
- this preprocessing stage does not project `LINCS` `Gene delta` into the
  benchmark-wide shared gene universe; shared projection remains downstream of
  this contract

## Chemical Target Mapping

Retained `trt_cp` signatures resolve chemical identity through the following
cascade:

1. `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/compoundinfo_beta_processed.txt`
2. `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/compoundinfo_beta.txt`
3. `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/repurposing_drugs_20200324_process.txt`

The resolved Task1 chemical identity is canonicalized with:

- uppercase tokens
- duplicate removal
- stable ordering
- `|` delimiter
- exact target-set equality for Task1 chemical identity

If a retained `trt_cp` signature cannot be resolved to a canonical target-set
string after the full cascade, it is excluded from Task1 chemical lawful units.

## Output Contract

This preprocessing stage materializes:

- native `Gene` delta in `LINCS` Level5 gene space
- matrix-near `gene_meta.csv`
- single-column `gene_feature_index.csv` for the `Gene` representation
- instance registry / metadata table
- preprocessing metadata for downstream analysis

This preprocessing stage does not materialize the final manuscript-valid shared
`Pathway` representation or the final canonical shared `Gene` feature table.
Final shared `Pathway` ownership and final shared `Gene` feature-table
ownership remain downstream in `task1_scope_merge.py`.

The source-local `instance_registry.csv` must remain row-aligned with
`gene/gene_delta.npy`.

`gene/gene_meta.csv` is the matrix-near row-metadata table for
`gene/gene_delta.npy`.

The row order of `gene/gene_meta.csv` must match the row order of
`gene/gene_delta.npy`.

The minimal `gene_meta.csv` columns are:

- `instance_id`
- `dataset`
- `cell_line`
- `perturbation_type`
- `perturbation_gene`
- `time_hr`
- `dose_um`

The row order of `gene/gene_feature_index.csv` must match the column order of
`gene/gene_delta.npy`.

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

`LINCS`-specific extension columns must include at least:

- source trace:
  `sig_id`
- source metadata:
  `pert_id`, `cmap_name`, raw `pert_time`, raw `pert_idose`
- audit trace:
  `qc_pass`, `is_hiq`, `is_ncs_sig`, `is_exemplar_sig`,
  `target_mapping_source`, and the original `siginfo_beta.txt` source row
  number

`instance_id` is the only persisted instance-level key in the minimal contract.

`instance_id` uses the readable composite format:
`{dataset}::{cell_line}::{perturbation_type}::{perturbation_gene}::{time_hr_or_NA}::{dose_um_or_NA}::{source_trace}`.

For `LINCS`, `source_trace` is `sig_id`.

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

Any contiguous source-local row numbering remains an internal construction and
ordering helper rather than a required persisted field.

Task1 unit semantics remain:
`(dataset, cell_line, perturbation_type, perturbation_gene)` for internal
analysis, with chemical `time` and `dose` retained as metadata only. Cross-unit
matching remains `(cell_line, perturbation_type, perturbation_gene)` when both
datasets are present.

## Out Of Scope

- no direct R handoff
- no panel-ready outputs
- no `FM` outputs for `LINCS` in Figure 2 preprocessing

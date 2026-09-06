# Data Sources

## Role

This document is the index of data sources used by the current benchmark
implementation. It records source identity, readout modality, provenance, and
scope boundaries. Dataset-specific filtering and transformation rules remain
in the linked preprocessing contracts; this file is not a second preprocessing
contract.

## Current Source Set

| Source | Raw input surface | Experimental readout | Current Task1 use | Detailed contract |
| --- | --- | --- | --- | --- |
| `LINCS` | `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/` | Level5 bulk gene-expression signatures | Internal chemical and genetic slices; matched single-gene genetic cross slice | [LINCS preprocessing](preprocessing/lincs.md) |
| `scPerturb` | `/mnt/NAS_21T/ProjectData/OSMOSIS/raw/scPerturb_Processed/` | Single-cell gene-expression observations with paired `h5ad` and observation tables | Human-only internal chemical and genetic slices; matched single-gene genetic cross slice | [scPerturb preprocessing](preprocessing/scperturb.md) |

The current Task1 source bundle contains only the source rows that pass the
active Task1 contracts. The source roots themselves are not benchmark tables;
the source-local bundles and the final snapshot are derived data surfaces.

## LINCS Inputs

The current LINCS preprocessing reads the following Level5 inputs:

- `level5_beta_all_n1201944x12328.gctx`
- `siginfo_beta.txt`
- `cellinfo_beta.txt`
- `geneinfo_beta.txt`

Chemical target resolution uses the ordered mapping cascade documented in the
[LINCS preprocessing contract](preprocessing/lincs.md). The retained Level5
signature is the native source-local Gene delta. The preprocessing contract
also defines the retained `pert_type` families, quality filter, source trace,
and source-specific audit fields.

## scPerturb Inputs

The formal scPerturb ingest surface scans the raw root for:

- `Cleaned_*_obs.csv`
- paired `Cleaned_<dataset>.h5ad`

Dataset entry is controlled by the active human dataset mapping in the
[scPerturb preprocessing contract](preprocessing/scperturb.md). That contract
defines human-only filtering, normalized perturbation types, treated-control
pairing, local-context matching, source-specific identity extraction, the
`sciplex4` exception, and the FM handoff.

## Data Layers

The benchmark keeps three distinct data layers:

1. Raw source files are immutable inputs under the source roots above.
2. Source-local bundles preserve source-specific feature axes, registries,
   pairing facts, and model-specific outputs where applicable.
3. The Task1 snapshot combines lawful source-local objects into canonical
   `master/` and block-scoped surfaces.

The snapshot layout, routing fields, manifest structure, and registry ownership
are defined in the [Task1 snapshot contract](snapshots/task1.md). The object
identity and delta-space terminology are defined in the
[data object model](object_model.md).

## Provenance And Storage

The local checkout is source-only. Raw inputs, source bundles, snapshots, run
metadata, and plot exports remain on the NAS-backed roots defined by the
[storage policy](../governance/storage_policy.md) and [runbook](../governance/runbook.md).

Each source-local bundle and Task1 snapshot carries a manifest with source
paths, upstream inputs, contract parameters, and artifact paths. Manifest
requirements are part of the [Task1 snapshot contract](snapshots/task1.md);
audited manifests and stage outputs are authoritative for materialized data
facts.

## Scope Boundaries

- `scPerturb` human-only filtering and the absence of ortholog mapping are
  current Task1 source-bundle rules, not universal assumptions about every
  possible future source.
- The current Task1 source bundle supports `Gene`, `Pathway`, and scoped FM
  surfaces as specified by the linked contracts.
- No Task2 snapshot contract is created here. Task2 data definitions remain in
  [Task2](../tasks/task2.md) until a dedicated Task2 data snapshot is defined.
- Adding a source, species, assay, or representation requires a documented
  scope decision and corresponding contract update; source presence alone does
  not expand a task's lawful comparison set.

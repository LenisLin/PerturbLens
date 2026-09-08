# PerturbLens Data Sources

## Purpose

This document defines source families and entry requirements. Source presence does not make a comparison lawful; task contracts define lawful matching and splits.

New and historical sources follow the [data architecture](architecture.md),
[intake workflow](intake.md) and [eligibility contract](eligibility.md).
Expression profiles and images with treatment/control metadata form the source
preservation base. Traceable precomputed profiles/embeddings can be retained and
adopted as state artifacts under the [matrix contract](matrix_semantics.md).
Source-native files may already be processed; their semantics remain explicit.

## Current transcriptomic source families

### LINCS

Primary input surface:

```text
/mnt/NAS_21T/ProjectData/OSMOSIS/raw/CMap_LINCS/LINCS_level5/beta/
```

Readout: bulk/L1000 Level 5 perturbational expression signatures.

Perturbation families used by PerturbLens:

- chemical (`trt_cp`)
- genetic expression perturbation (`trt_xpr`)

LINCS supplies large-scale chemical and genetic signatures, cell-context metadata, time/dose metadata where available, and chemical target annotations through source mapping resources.

### scPerturb-derived human datasets

Primary input surface:

```text
/mnt/NAS_21T/ProjectData/OSMOSIS/raw/scPerturb_Processed/
```

Readout: single-cell transcriptomic perturbation observations with dataset-specific controls and metadata.

Perturbation families include CRISPR/CRISPRi/CRISPRa-like genetic interventions and drug perturbations. Exact intervention mode is preserved rather than discarded after family normalization.

## Morphology source class

R5 requires perturbational morphology data with sufficient matching to transcriptomic perturbations. Candidate sources must be frozen in a source-inventory decision before production analysis.

Required source metadata include, where applicable:

- perturbation/compound identity;
- target annotation;
- genetic intervention identity and mode;
- cellular context;
- plate/well/batch;
- time and dose;
- replicate identity;
- image channels and acquisition metadata;
- relationship to any transcriptomic assay.

Three matching tiers are recognized:

1. **same-assay paired** — morphology and transcriptomics measured from the same experimental system with direct pairing;
2. **condition-matched** — same perturbation/context/time/dose in independent readout experiments;
3. **label-matched** — same perturbation or target annotation without full experimental matching.

R5 claims must state the tier used.

The canonical stored values are `paired_assay`, `condition_matched` and
`label_matched`; the source/proposal alias `same_assay_paired` is normalized to
`paired_assay` with its raw label retained. Shared schema and evidence requirements
are owned by [relations](relations.md).

## Combination source class

R6 requires explicit multi-perturbation observations with constituent single perturbations and matched controls in the same or a sufficiently compatible experimental system.

Required fields:

- constituent identities;
- combination order/stoichiometry if meaningful;
- intervention type;
- context;
- time/dose or perturbation strength;
- matched single-perturbation availability;
- control and replicate identifiers.

Genetic and chemical combinations are analyzed separately unless a specific cross-intervention combination comparison is approved.

## Source inventory gate

Before any R2-R6 production run, materialize a source inventory recording:

- source version/path/hash;
- organism and assay;
- readout modality;
- intervention types/modes;
- contexts;
- perturbation/compound/target counts;
- replicate support;
- time/dose coverage;
- combination coverage;
- representation availability;
- exclusion reasons.

The inventory is descriptive evidence, not proof that a downstream task is sufficiently powered.

The inventory is materialized through `file_inventory.parquet`,
`coverage_summary.parquet` and `task_eligibility.parquet` before localization or
formal processing. A documented include decision precedes prepared/state/response
builds. Source-specific appendices must freeze unresolved metadata, normalization,
matching and support rules before the affected operation.

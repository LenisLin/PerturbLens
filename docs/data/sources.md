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
/mnt/NAS_21T/ProjectData/PerturbLens/data/sources/lincs/local_snapshot_20260909/transcriptomics/lincs/LINCS_level5/beta/
```

Readout: bulk/L1000 Level 5 perturbational expression signatures.

Perturbation families used by PerturbLens:

- chemical (`trt_cp`)
- genetic expression perturbation (`trt_xpr`)

LINCS supplies large-scale chemical and genetic signatures, cell-context metadata, time/dose metadata where available, and chemical target annotations through source mapping resources.

The 2026-09-09 preservation move also retained Level 3, GSE92742 and annotation
files under the same `transcriptomics/lincs/` root, preserving their original
subdirectories. Their preservation does not extend the active Level 5 beta
analysis contract or reinterpret signatures as raw counts. Resolve moved paths
through the inventory in [local preservation](../governance/records/2026-09-09-local-preservation.md).

### scPerturb-derived human datasets

Source-native human expression surface:

```text
/mnt/NAS_21T/ProjectData/PerturbLens/data/sources/scperturb/local_snapshot_20260909/transcriptomics/<dataset>/<dataset>.h5ad
```

Readout: single-cell transcriptomic perturbation observations with dataset-specific controls and metadata.

Perturbation families include CRISPR/CRISPRi/CRISPRa-like genetic interventions and drug perturbations. Exact intervention mode is preserved rather than discarded after family normalization.

Historical cleaned human expression and paired observation tables are preserved
separately under `data/prepared/scperturb/<dataset>/legacy_cleaned_20260909/`.
These are imported historical preparations with `materialized` status, not
certified new canonical preprocessing. Raw and cleaned source semantics remain
distinct; an intended task must still pass intake and revalidation.

## Morphology source class

### Preserved CPG0016 assets

The `cpg0016-jump-assembled` preservation copy contains 22 files
(23,956,828,208 bytes): nine profile parquet files and 13 companion
metadata/provenance files. Source/destination SHA256 checks passed and remote
originals were retained. The destination root is:

```text
/mnt/NAS_21T/ProjectData/PerturbLens/data/sources/cpg0016-jump-assembled/
```

Profiles cover compound v1.0, ORF/CRISPR v1.0a and ALL v1.0b; ALL is not a
compound-only cohort. No images were copied. Context, time/dose, independent
support and preprocessing fit scope remain unresolved admission requirements.
CRISPR PCA-corrected rows require keyed alignment on `Metadata_Source`,
`Metadata_Plate` and `Metadata_Well`, not positional alignment.

The operation evidence is `COPY_SUMMARY.md`, `copy_complete.json` and
`finalization_complete.json` under:

```text
/mnt/NAS_21T/ProjectData/PerturbLens/data/intake/cpg0016-jump-assembled/remote_snapshot_20260909/copy_73_20260909/
```

This is preserved source/profile availability, not an eligible R5 cohort or a
validated canonical state build.

### Source admission requirements

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

# Task2: Mechanism Concordance

## Status and ownership

This document is the Task2 task contract. It defines the chemical-genetic
comparison, lawful membership, directions, and required outputs. It does not
duplicate dataset construction, representation construction, metric formulas,
or storage policy.

The current baseline is preserved from the former Task2 contract. Dataset and
representation construction are defined in:

- `docs/data/sources.md`
- `docs/data/object_model.md`
- `docs/data/preprocessing/lincs.md`
- `docs/data/preprocessing/scperturb.md`
- `docs/data/representations/gene.md`
- `docs/data/representations/pathway.md`
- `docs/data/representations/fm.md`

Task2 cohort and membership surfaces are rooted at the active Task2 data root
and are listed below. Metric definitions are owned by
`docs/metrics/concordance.md` and `docs/metrics/retrieval.md`. Output fields
are owned by `docs/tasks/output_schemas.md`; validation requirements are owned
by `docs/tasks/validation.md`.

## Scientific question

Task2 evaluates mechanism concordance between chemical and genetic cohorts
inside one dataset. It asks whether chemical perturbations involving an
`anchor_gene` and genetic perturbations of that gene produce concordant
responses. Task2 is distinct from Task1 modality concordance and must remain a
separate task in the manuscript and evidence registry.

## Active scope

### Datasets

- `LINCS`
- `scPerturb`

### Representations

- `LINCS`: `Gene`, `Pathway`
- `scPerturb/K562`: `Gene`, `Pathway`, `scgpt`, `geneformer`, `scbert`,
  `scfoundation`, `uce`, `state`, `tahoe-x1`

`Gene` and `Pathway` are the benchmark-wide representation spaces. FM
representations are scoped to the approved `scPerturb/K562` local-only
Figure 3F panel for manuscript-facing absolute-performance reporting. Their
availability in upstream data or a local Task2 computation does not authorize
FM as a general cross-dataset or general manuscript representation.

## Unit and membership

The Task2 unit is:

```text
(dataset, cell_line, anchor_gene)
```

`anchor_gene` is the Task2 unit field. A lawful unit contains at least one
chemical member and at least one genetic member.

- A chemical row joins a Task2 unit when `anchor_gene` belongs to the chemical
  target set encoded in `perturbation_gene`.
- `perturbation_gene` remains the row identity field, including the complete
  canonical target-set string for a multi-target chemical.
- `query_instance_id` is the retrieval query identifier.
- Membership expansion is performed at cohort construction; it does not
  rewrite the chemical row identity.

The data object model and preprocessing contracts define target-set
canonicalization, source traceability, and delta construction. This document
defines only the Task2 membership relation and lawful unit.

## Active data surface

The active Task2 data root and storage semantics are owned by
`docs/governance/storage_policy.md`. Stage and run locations are owned by
`docs/governance/runbook.md`.

The current cohort and membership surfaces are:

- `task2_pairs_coverage.csv`
- `task2_row_membership.parquet`
- `delta_meta.csv`
- `representation_availability_registry.csv`
- `snapshot_manifest.json`

These are data-stage artifacts, not substitutes for Task2 result tables. Their
actual presence and validation status must be established from manifests and
the evidence index.

## Group analysis

Group analysis compares chemical and genetic cohorts within each lawful
`(dataset, cell_line, anchor_gene)` unit.

- Group analysis is directionless.
- Core group metrics are cosine similarity, `PCC`, and bias-corrected
  `e_distance`, as defined in `docs/metrics/concordance.md`.
- Core metrics are computed within each `dataset` and `cell_line`.
- Chemical and genetic instance counts used in each comparison are retained
  as denominator fields.

The current contract does not approve a confidence-interval method,
hypothesis test, multiple-comparison procedure, or cross-dataset pooling rule.
Those details remain pending and must not be inferred from the metric names.

## Directional retrieval

Task2 retrieval keeps the two directions separate in every output table.

### C2G

`C2G` means chemical-to-genetic retrieval:

- query: one chemical instance keyed by `query_instance_id`
- gallery: lawful genetic centroids keyed by `anchor_gene`
- positive: the lawful genetic key associated with the query's Task2 unit

### G2C

`G2C` means genetic-to-chemical retrieval:

- query: one genetic instance keyed by `query_instance_id`
- gallery: lawful chemical centroids
- positive: the chemical centroid for the same
  `(dataset, cell_line, anchor_gene)` unit

Primary retrieval metrics in both directions are corrected `Hit@1`, corrected
`Hit@3`, corrected `Hit@5`, and corrected `MRR`; raw metrics may be retained in
the per-query table. `gallery_size`, `n_positive_keys`, and `rank_true` must
remain available for chance correction and audit.

The exact positive-key construction for every lawful gallery, tie behavior,
invalid-query handling, correction transform, and summary pooling are not all
specified by the current contract. They must be approved before production
analysis; no fallback to a scPerturb-only output is permitted for a corrected
multisource Task2 result.

## Analysis stages

The current stage labels locate the Task2 evidence chain:

- `S3`: multisource Task2 cohort and membership build
- `S4`: Task2 group concordance
- `S5`: Task2 retrieval
- `S6`: Task2 synthesis

Stage labels do not change Task2 units or directions. Actual run status and
verification evidence are maintained in `docs/governance/state.md` and
`docs/tasks/evidence_index.md`.

## Synthesis rule

Task2 synthesis combines the group and retrieval summaries produced under the
Task2 contract. It must not change unit definitions, direction labels, or
denominator fields. A synthesis output is not evidence that an upstream stage
was audited unless the corresponding manifests and assertions establish it.

## Required outputs

Task2 produces the following result surfaces:

- `task2_pairs_coverage.csv`
- `task2_group_concordance_long.csv`
- `task2_group_leaderboard.csv`
- `task2_retrieval_per_query.parquet`
- `task2_retrieval_summary_long.csv`
- `task2_retrieval_leaderboard.csv`
- `task2_benchmark_summary_long.csv`

Field-level schemas, denominator fields, S7 interfaces, and manifest
requirements are defined in `docs/tasks/output_schemas.md`.

## Claim boundary

Task2 is a benchmark comparison within the active datasets and cell contexts;
it does not by itself establish causal equivalence between chemical and
genetic perturbations. Results must preserve direction, representation,
coverage, exclusions, and uncertainty once those analysis details are
approved.

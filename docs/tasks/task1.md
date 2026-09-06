# Task1: Modality Concordance

## Status and ownership

This document is the Task1 task contract. It defines what is compared, which
objects are lawful, how the two Task1 settings differ, and which outputs are
required. It does not duplicate dataset construction, representation
construction, metric formulas, or storage policy.

The current baseline is preserved from the former Task1 contract. Dataset and
representation construction are defined in:

- `docs/data/sources.md`
- `docs/data/object_model.md`
- `docs/data/preprocessing/lincs.md`
- `docs/data/preprocessing/scperturb.md`
- `docs/data/representations/gene.md`
- `docs/data/representations/pathway.md`
- `docs/data/representations/fm.md`
- `docs/data/snapshots/task1.md`

Metric definitions are owned by `docs/metrics/concordance.md` and
`docs/metrics/retrieval.md`. Output fields are owned by
`docs/tasks/output_schemas.md`; validation requirements are owned by
`docs/tasks/validation.md`.

## Scientific question

Task1 evaluates modality concordance while holding `perturbation_type` fixed.
It asks whether perturbation-response representations agree within a source
and across the matched `LINCS` and `scPerturb` genetic slice. Task1 does not
test chemical-to-genetic mechanism concordance; that is Task2.

The benchmark object is a delta-space perturbation response. A raw row is
eligible only after it has been converted to one aggregated delta instance by
the applicable data contract.

## Active scope

### Dataset and setting slices

The current Task1 slices are:

- `LINCS` internal chemical
- `LINCS` internal genetic
- `scPerturb` internal chemical
- `scPerturb` internal genetic
- matched `LINCS` to `scPerturb` single-gene genetic cross slice

The current `scPerturb` source-bundle scope is human-only. The current Figure 2
Task1 freeze does not perform ortholog mapping. These are scope constraints,
not general claims about the source databases.

### Active representations

- `LINCS` internal: `Gene`, `Pathway`
- `scPerturb` internal: `Gene`, `Pathway`, `scgpt`, `geneformer`, `scbert`,
  `scfoundation`, `uce`, `state`, `tahoe-x1`
- Task1 cross: `Gene`, `Pathway`

`Gene` and `Pathway` are the benchmark-wide representation spaces. FM output
may be materialized upstream for the `scPerturb` source bundle and internal
Task1 analysis, but FM is not authorized in manuscript-facing Figure 2 panels.
The manuscript-facing FM analysis remains limited to the approved
`scPerturb/K562` local-only Figure 3F panel.

## Unit and identity

### Internal unit

The Task1 internal unit is:

```text
(dataset, cell_line, perturbation_type, perturbation_gene)
```

`dataset` and `cell_line` identify the source context. `perturbation_type` is
either `chemical` or `genetic`. `perturbation_gene` is the perturbation
identity field. Chemical `time` and `dose` remain metadata and do not enter the
Task1 unit.

### Cross unit

The Task1 cross unit is:

```text
(cell_line, perturbation_type, perturbation_gene)
```

Both datasets must be present for the matched cross slice. The current cross
slice is restricted to single-gene genetic rows. Multi-gene genetic rows are
not admitted to the current cross block.

### Identity rules

- A chemical `perturbation_gene` is one canonical target-set string.
- Chemical target sets use uppercase tokens, duplicate removal, stable
  alphabetical ordering, and `|` as the delimiter.
- A multi-target chemical remains one instance row; it is not split into
  separate Task1 instances.
- A genetic `perturbation_gene` is one perturbed gene by default.
- The current `scPerturb` internal slice may retain canonicalized multi-gene
  genetic values as a scoped exception, using the same uppercase, deduplicated,
  alphabetical, `|`-delimited representation.
- `instance_id` is the source-agnostic persisted instance key. Retrieval rows
  carry it through `query_instance_id`.

The data object model defines source trace keys and the construction of
`instance_id`; this document only defines the identity required by Task1
matching and retrieval.

## Lawful comparisons

An internal comparison holds `dataset`, `cell_line`, `perturbation_type`, and
`perturbation_gene` fixed while comparing independent cohorts or instances
within that lawful unit. A cross comparison requires exact agreement on
`cell_line`, `perturbation_type`, and `perturbation_gene` across `LINCS` and
`scPerturb`.

For chemical rows, exact canonical target-set equality is required for Task1
matching. Chemical target-set membership expansion is a Task2 cohort rule and
does not change Task1 identity.

## Group analysis

Group analysis is directionless. The current design requires:

- Internal group analysis uses deterministic split-half cohorts.
- Cross group analysis uses units shared by `LINCS` and `scPerturb`.
- Group metrics are cosine similarity, `PCC`, and bias-corrected
  `e_distance`, as defined in `docs/metrics/concordance.md`.
- The output records the number of instances used by each comparison.
- A comparison side with fewer than `2` instances is marked
  `underpowered_for_e_distance=true`.

The exact split-half implementation, estimator settings, uncertainty
procedure, and pooling rules are not fully approved by the current contract.
They must be specified before production analysis in the task-specific
analysis section and referenced by the run manifest. No inferential procedure
or threshold is implied here.

## Instance retrieval

Retrieval is directional and uses single-instance queries against lawful
centroid galleries.

- Retrieval queries are single instances.
- Retrieval galleries are centroids built from lawful Task1 units.
- Task1 retrieval is single-positive.
- Task1 internal retrieval uses leave-one-out true centroids, so the query
  instance is excluded from its true centroid.
- `n_positive_keys = 1` for every lawful Task1 query.
- Task1 cross alignment uses `instance_id` as the source-agnostic instance key
  on both the `LINCS` and `scPerturb` sides.
- Primary metrics are corrected `Hit@1`, corrected `Hit@3`, corrected
  `Hit@5`, and corrected `MRR`. Raw metrics may be retained in the same
  per-query table.

The ranking and chance-correction rules are defined in
`docs/metrics/retrieval.md`. Exact handling of ties, invalid ranks, and
aggregation of per-query values remains pending unless an approved task
analysis record specifies it.

## Analysis stages

The historical stage labels remain useful for locating Task1 evidence:

- `S0`: data inventory and source eligibility
- `S1`: Task1 internal metrics
- `S2`: Task1 cross metrics

Stage labels do not change the Task1 scientific definition. Actual run status
and verification evidence are maintained in `docs/governance/state.md` and
`docs/tasks/evidence_index.md`.

## Required outputs

Task1 produces the following result surfaces:

- `task1_group_concordance_long.csv`
- `task1_retrieval_per_query.parquet`
- `task1_retrieval_summary.csv`
- `task1_leaderboard_long.csv`
- `task1_cross_alignment_proof.csv`

Field-level schemas, denominator fields, and manifest requirements are defined
in `docs/tasks/output_schemas.md`.

## Statistical and exploratory analysis status

The current contract does not approve a confidence-interval method, hypothesis
test, multiple-comparison procedure, split-half pooling rule, or sensitivity
analysis hierarchy. These details are required for a complete journal study,
but remain pending until explicitly approved. A future analysis may be
exploratory without changing this Task1 contract if it preserves the lawful
unit, positive, and leakage rules and is labeled accordingly.

Task1 results must report coverage and exclusions alongside metric values. A
result may support only claims within the active datasets, cell contexts,
perturbation types, representations, and lawful slices.

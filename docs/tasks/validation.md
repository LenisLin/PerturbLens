# Task Validation and Audit Requirements

This document defines the minimum validation contract for Task1, Task2, and
their project-level synthesis. It is normative about checks, but it does not
claim that a current run has passed them. Actual status and evidence locations
are maintained in `docs/governance/state.md` and
`docs/tasks/evidence_index.md`.

## Validation gates

Every stage presented as audited must pass all three gates:

1. Input integrity: hashes, schemas, row alignment, and required files.
2. Metric integrity: metric family, denominator fields, and aggregation rules.
3. Leakage integrity: leave-one-out or disjoint-gallery behavior required by
   the applicable task contract.

Each assertion must be falsifiable through concrete files and table rows. A
successful process exit or a non-empty output file is not, by itself, a passed
gate.

## Stage bundle contract

Each stage bundle includes:

- `run_manifest.json`
- `audit_assertions.json`
- `manifest.json`
- the stage tables defined in `docs/tasks/output_schemas.md`

The table manifest must include the common fields in
`docs/tasks/output_schemas.md`. The run manifest identifies the input roots,
contract versions, runtime parameters, and stage identity. The assertions file
records the checks and their outcomes. A missing assertion is not equivalent to
an assertion that passed.

## Input integrity

The input gate verifies, as applicable to the stage:

- required source, snapshot, and representation artifacts exist at the active
  roots;
- source and snapshot manifests identify the inputs actually consumed;
- table schemas and required columns match the versioned output contract;
- primary keys are unique at their declared result level;
- matrix rows and row-index identifiers agree without silent reordering;
- Task1 cross alignment uses the declared
  `(cell_line, perturbation_type, perturbation_gene)` unit;
- Task2 membership and coverage tables agree on
  `(dataset, cell_line, anchor_gene)` and the chemical/genetic counts;
- representation availability is checked before a metric is emitted.

Input facts must be checked against manifests inside the active data roots. The
repository checkout remains source-only.

## Metric integrity

The metric gate verifies:

- each `metric_name` belongs to the metric family allowed by the task;
- metric input representations and dimensions match their declared indices;
- denominator fields are emitted with the metric value;
- Task1 `underpowered_for_e_distance` follows the fewer-than-two rule;
- Task2 `n_chem_sub` and `n_gen_sub` describe the instances used by
  `e_distance`;
- raw and corrected retrieval fields are not interchanged;
- corrected retrieval values retain the `gallery_size` and
  `n_positive_keys` context needed for chance correction;
- summary tables do not drop the unit, direction, representation, or
  denominator fields required by the task contract.

Metric formulas and the current boundary of approved calculation details are
defined in `docs/metrics/concordance.md`,
`docs/metrics/retrieval.md`, and `docs/metrics/aggregation.md`.

## Leakage integrity

The leakage gate verifies the gallery construction used by the stage:

- Task1 internal true centroids are leave-one-out with respect to each query;
- Task1 cross comparisons use the source-agnostic `instance_id` alignment and
  do not use the query as an unintended target-side training observation;
- Task2 C2G and G2C preserve their separate query and gallery cohorts;
- a query is not silently included in a centroid used as its true comparison
  when the applicable contract requires exclusion;
- every reported positive rank is traceable to a lawful positive key.

The exact disjoint-gallery construction for settings not fully specified by the
current contracts remains pending and must be stated in the stage manifest
before results are treated as final.

## Task-specific checks

### Task1

- Internal and cross scopes use their declared units.
- Internal `scPerturb` multi-gene genetic rows remain internal-only.
- The cross slice contains only matched single-gene genetic units.
- Chemical identity matching uses exact canonical target-set equality.
- Each lawful retrieval query has `n_positive_keys = 1`.
- `query_instance_id` traces to the upstream `instance_id`.
- Internal true centroids exclude the query instance.

### Task2

- Every lawful unit has at least one chemical and one genetic member.
- Chemical membership is based on `anchor_gene` belonging to the canonical
  target set, while the row identity remains `perturbation_gene`.
- Group outputs are scoped to the declared dataset and cell line.
- Retrieval rows preserve `C2G` and `G2C` as separate directions.
- C2G queries are chemical instances and G2C queries are genetic instances.
- Synthesis does not alter upstream units, directions, or denominators.
- Corrected multisource outputs are not replaced by a scPerturb-only path.

### S7

- Every direct input is registered in `project_input_registry.csv`.
- Each input has a stage directory, manifest, and audit-assertions path.
- S7 summaries preserve the upstream task and analysis-family identity.
- Scorecard inputs are traceable to the project summary and representation.

## Pending validation details

The following are not silently filled by this migration:

- exhaustive source-specific registry inventories beyond the frozen minimum;
- richer per-artifact audit payloads;
- exact estimator and bias-correction details for `e_distance`;
- tie, invalid-rank, zero-denominator, missing-value, and correction behavior
  where the task and metric contracts do not specify it;
- confidence intervals, hypothesis tests, resampling units, multiple
  comparisons, and pooling rules;
- panel-specific `2A` fields and panel-level rendering checks.

These items are completion criteria for the relevant future analysis protocol,
not implicit defaults.

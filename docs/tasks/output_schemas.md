# Task and Project Output Schemas

This document is the canonical owner of result-table schemas for Task1, Task2,
and S7 project synthesis. It defines required table identities, key fields,
metric fields, denominator fields, and minimum manifest payloads. It does not
define how a metric is calculated; those rules are owned by `docs/metrics/`.

Task definitions are owned by `docs/tasks/task1.md` and
`docs/tasks/task2.md`. Data-stage snapshot schemas are owned by `docs/data/`.
The tables listed here are result or synthesis interfaces and must not silently
change when a figure layout changes.

## Common manifest fields

Every result table ships with a table-specific manifest that includes:

- `table_name`
- `table_path`
- `result_family`
- `result_level`
- `primary_key_fields`
- `dynamic_field_list`
- `constant_fields`
- `metric_columns`
- `schema_version`

Manifest values must describe the emitted table rather than an intended table.
If a required field or key changes, increment the schema version and update the
owning task contract and validation checks together.

## Task1 schemas

Task1 key vocabulary:

- `scope`: `internal` or `cross`
- `dataset_or_direction`: `LINCS` or `scPerturb` for internal rows;
  `LINCS_to_scPerturb` for cross rows

### `task1_group_concordance_long.csv`

- one row per Task1 unit, representation, and metric
- key fields:
  `scope, dataset_or_direction, perturbation_type, perturbation_gene, representation, metric_name`
- metric field: `metric_value`
- denominator fields:
  `n_instances_used, n_instances_split_a, n_instances_split_b, n_instances_subsampled`
- quality field: `underpowered_for_e_distance`

The quality field is `true` when a comparison side has fewer than `2` instances,
as required by the Task1 contract. Its presence and value must be auditable
from the emitted denominator fields.

### `task1_retrieval_per_query.parquet`

- one row per Task1 retrieval query
- key fields:
  `scope, dataset_or_direction, perturbation_type, representation, query_instance_id`
- `query_instance_id` uses the upstream `instance_id` value directly
- required fields:
  `cell_line, perturbation_gene, gallery_size, n_positive_keys, rank_true`
- retrieval metric fields:
  `mrr_raw, hit1_raw, hit3_raw, hit5_raw, mrr_corrected, hit1_corrected, hit3_corrected, hit5_corrected`

### `task1_retrieval_summary.csv`

- one row per Task1 retrieval slice
- key fields:
  `scope, dataset_or_direction, perturbation_type, representation`
- denominator fields:
  `n_total, n_valid, n_excluded, gallery_size_mean, gallery_size_max`

### `task1_leaderboard_long.csv`

- one row per Task1 slice and summary metric
- key fields:
  `scope, dataset_or_direction, perturbation_type, representation, metric_name`
- value field: `metric_value`

### `task1_cross_alignment_proof.csv`

- one row per Task1 cross slice
- key fields:
  `dataset_or_direction, perturbation_type`
- required fields:
  `alignment_unit_definition, n_matched_units`
- `alignment_unit_definition` is fixed to:
  `(cell_line, perturbation_type, perturbation_gene)`

## Task2 schemas

Task2 key vocabulary:

- `direction`: `C2G` or `G2C`
- `analysis_family`: `group` or `retrieval`

### `task2_pairs_coverage.csv`

- one row per Task2 unit
- key fields:
  `dataset, cell_line, anchor_gene`
- denominator fields:
  `n_chem_instances, n_gen_instances`

### `task2_group_concordance_long.csv`

- one row per Task2 unit, representation, and metric
- key fields:
  `dataset, cell_line, anchor_gene, representation, metric_name`
- value field: `metric_value`
- denominator fields:
  `n_chem_instances_used, n_gen_instances_used, n_chem_sub, n_gen_sub`
- `n_chem_sub` and `n_gen_sub` are the subsampled instance counts used by
  `e_distance`

### `task2_group_leaderboard.csv`

- one row per Task2 dataset, cell line, and representation
- key fields:
  `dataset, cell_line, representation`
- summary fields:
  `mean_cosine_centroid, mean_pcc_centroid, mean_e_distance`

### `task2_retrieval_per_query.parquet`

- one row per Task2 retrieval query
- key fields:
  `dataset, cell_line, direction, representation, query_instance_id`
- required fields:
  `anchor_gene, perturbation_gene, gallery_size, n_positive_keys, rank_true`
- retrieval metric fields:
  `mrr_raw, hit1_raw, hit3_raw, hit5_raw, mrr_corrected, hit1_corrected, hit3_corrected, hit5_corrected`

### `task2_retrieval_summary_long.csv`

- one row per Task2 retrieval slice and summary metric
- key fields:
  `dataset, cell_line, direction, representation, metric_name`
- value field: `metric_value`
- denominator fields:
  `n_valid, gallery_size_mean, gallery_size_max, n_positive_keys_mean`

### `task2_retrieval_leaderboard.csv`

- one row per Task2 retrieval slice
- key fields:
  `dataset, cell_line, direction, representation`
- summary fields:
  `mean_mrr_corrected, mean_hit1_corrected, mean_hit3_corrected, mean_hit5_corrected`

### `task2_benchmark_summary_long.csv`

- one row per Task2 synthesis output metric
- key fields:
  `analysis_family, dataset, cell_line, direction, representation, metric_name`
- value field: `metric_value`

## S7 project synthesis schemas

S7 combines audited upstream Task1 and Task2 outputs. An otherwise explicitly
verified but unaudited input is not a substitute for the audited stage
requirement. S7 does not redefine upstream task units, directions,
representations, or denominator fields.

S7 key vocabulary:

- `analysis_family`: `group` or `retrieval`

### `project_input_registry.csv`

- one row per direct stage input to project synthesis
- key fields:
  `task, stage_name, run_id`
- required fields:
  `stage_dir, manifest_path, audit_assertions_path`

### `project_benchmark_summary_long.csv`

- one row per project synthesis metric
- key fields:
  `task, analysis_family, dataset, cell_line, direction, representation, metric_name`
- value field: `metric_value`

### `project_axis_score_inputs_long.csv`

- one row per scorecard input family
- key fields:
  `task_axis, family_id, representation`
- value field: `metric_value`

### `project_representation_scorecard.csv`

- one row per representation
- key field: `representation`
- summary fields:
  `task1_axis_value_raw, task2_axis_value_raw, overall_axis_value_raw`

The scorecard does not authorize a new weighting, normalization, or pooling
rule. Such a rule must be separately approved and recorded with its inputs and
version.

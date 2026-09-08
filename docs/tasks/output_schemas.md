# PerturbLens Output Schemas

## Common keys

All result tables include enough fields to identify:

- `result_id`
- `result_family`: `population_similarity`, `retrieval`, or `prediction`
- `result_section`: `R2`-`R6`
- `task_name`
- `split_name`
- `source`
- `readout_modality`
- `intervention_type`
- `state_representation`
- `response_view`
- `metric_name`
- support/denominator fields
- manifest/schema version

Task-specific identity fields (context, target, compound, query, combination, direction) are retained rather than collapsed into opaque labels.

## Population similarity table

`population_similarity_long.parquet`

One row per lawful comparison x representation x response view x metric.

Required fields include:

- comparison IDs/keys;
- `metric_value`;
- left/right observation counts;
- replicate/support counts;
- matching tier where applicable.

## Retrieval table

`retrieval_per_query.parquet`

One row per query x representation x response view x retrieval subtask.

Required fields:

- `query_id`
- direction
- positive key(s)
- `gallery_size`
- `n_positive_keys`
- `rank_best_positive`
- MRR/Hit@K fields or derivable rank
- exclusion/validity status

`retrieval_summary_long.csv` aggregates only after per-query storage.

## Prediction table

`prediction_per_condition.parquet`

One row per predicted condition x model x representation/response target x metric.

Required fields:

- condition identity;
- split/fold;
- model ID/version;
- metric raw value;
- calibrated value when defined;
- baseline/reference IDs;
- valid/excluded status.

`prediction_summary_long.csv` preserves macro/micro level and denominators.

## Covariate table

`covariate_analysis_long.csv`

Used primarily for R3 time/dose and exploratory context/target analyses. It records model formula/version, covariates, coefficient/effect, uncertainty, p/FDR where inferential, and eligible-unit count.

## R4 support-link table

`cross_intervention_support.csv`

Links each anchor-target/context unit to its R2/R3 measured-response support and R4 cross-intervention outputs.

## R5 matching table

`cross_readout_matching.parquet`

Persists transcriptomic-morphology unit pairs, matching tier, condition agreement fields, and exclusion reasons.

This is a task-selected projection of
`data/relations/<relation_build_id>/cross_readout_links.parquet`, retaining
`link_id` and `relation_build_id`. The [data relation contract](../data/relations.md)
owns shared fields; this output records the exact cohort used by the run.

## R6 residual table

`combination_residual_long.parquet`

Records combination identity, constituents, null model, observed/null/residual summaries, replicate support, representation, response view, and metric.

## Manifest rule

Every table has a manifest containing path/hash, schema version, primary key, dynamic/constant fields, source run ID, input/response/split/metric manifests, and validation status.

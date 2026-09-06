# Metric Aggregation and Summary Rules

## Scope

This document owns the boundary between per-unit or per-query metric values and
summary tables. It does not add an estimator or pooling rule that is absent
from the Task1 and Task2 contracts.

The basic reporting order is:

```text
lawful instances or cohorts
  -> per-unit group metric or per-query rank metric
  -> task-level summary table
  -> project synthesis input
```

Per-query retrieval values must be retained before summary so that query counts,
gallery sizes, positive-key counts, exclusions, and rank values remain
auditable.

## Fixed aggregation boundaries

- Task1 internal and cross results retain their `scope`,
  `dataset_or_direction`, `perturbation_type`, and representation.
- Task2 core group metrics are computed within each `dataset` and `cell_line`.
- Task2 retrieval retains `direction` as `C2G` or `G2C` at every result level.
- S7 combines upstream Task1 and Task2 summaries without changing their units,
  directions, representations, or denominator fields.
- No document in `docs/metrics/` authorizes pooling across datasets, cell lines,
  directions, or representations.

## Denominator preservation

Summary output must preserve the denominator context required by its owning
schema. This includes, as applicable:

- Task1 instance and split counts;
- Task1 retrieval total, valid, excluded, and gallery-size fields;
- Task2 chemical and genetic instance counts;
- Task2 `e_distance` subsample counts;
- Task2 retrieval valid-query, gallery-size, and positive-key fields.

A summary value without its declared denominator fields is incomplete evidence.

## Named summary fields

The current output contract includes fields such as:

- `mean_cosine_centroid`
- `mean_pcc_centroid`
- `mean_e_distance`
- `mean_mrr_corrected`
- `mean_hit1_corrected`
- `mean_hit3_corrected`
- `mean_hit5_corrected`

These names indicate the intended summary quantity but do not, on their own,
freeze weighting, invalid-row handling, missing-value policy, or aggregation
order. Those choices must be explicitly approved in the task analysis plan and
recorded in the relevant run manifest.

## Pattern summaries

`pair_mean_enrichment` is the signed summary used to rank entities in the
current Figure 2 and Figure 3 pattern panels. The pattern entity and support
context are task- and visualization-owned. The exact pairing, sign convention,
weighting, missing-value handling, and enrichment formula are not specified by
the current metric contract and remain pending.

No pattern ranking may be used to imply a result outside the support and
threshold rules approved by `docs/visualization/figure_plan.md`.

## Pending inferential choices

The following require an explicit approved analysis decision before they become
canonical:

- macro versus micro aggregation;
- weighting by units, queries, or gallery size;
- handling of invalid or missing metric values;
- confidence intervals and resampling units;
- hypothesis tests and multiple-comparison control;
- correction before versus after summary;
- cross-dataset or cross-cell-line synthesis.

These are unresolved methodological choices, not implementation defaults.

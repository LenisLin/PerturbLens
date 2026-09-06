# Retrieval Metrics

## Scope

Retrieval analysis is directional. A query representation is ranked against a
lawful gallery of target keys or centroids. The per-query output records the
gallery and positive-key context needed to interpret the rank.

Task1 and Task2 define the lawful query, gallery, and positive relation. This
document owns the metric vocabulary and the chance-correction boundary.

## Required ranking fields

Every retrieval row retains:

- `query_instance_id`
- `gallery_size`
- `n_positive_keys`
- `rank_true`
- raw and corrected retrieval metric fields where emitted

`rank_true` must be traceable to a lawful positive key. The direction and
representation are part of the result key.

## Raw metrics

For a valid query with a defined true-positive rank, the standard per-query
metrics are:

```text
MRR_raw = 1 / rank_true
Hit@K_raw = 1 when rank_true <= K, otherwise 0
```

The active benchmark reports `Hit@1`, `Hit@3`, `Hit@5`, and `MRR`. The output
field names are `hit1_raw`, `hit3_raw`, `hit5_raw`, and `mrr_raw`.

The current contracts do not fully specify multiple-positive rank selection,
tie handling, invalid ranks, or zero-denominator behavior. Those cases must be
resolved in an approved task analysis record before implementation; this
document does not add defaults.

## Chance correction

Corrected retrieval metrics adjust raw performance against a uniform random
ranking over the lawful gallery. The chance reference is conditioned on:

- `gallery_size`
- `n_positive_keys`

The corrected output fields are `hit1_corrected`, `hit3_corrected`,
`hit5_corrected`, and `mrr_corrected`. Raw metrics may be stored alongside
them.

The current benchmark fixes the random-ranking conditioning variables but does
not specify the exact correction transform, clipping or normalization, or
aggregation order. These must be approved and versioned before corrected
values are treated as canonical. A corrected multisource Task2 output must not
be replaced by a scPerturb-only path.

## Task-specific retrieval contracts

### Task1

- queries are single instances;
- galleries are centroids from lawful Task1 units;
- internal true centroids are leave-one-out;
- retrieval is single-positive;
- `n_positive_keys = 1` for every lawful query;
- cross alignment uses source-agnostic `instance_id`, carried as
  `query_instance_id`.

### Task2

- `C2G`: one chemical instance query, with lawful genetic centroids keyed by
  `anchor_gene` as the target gallery;
- `G2C`: one genetic instance query, with the chemical centroid for the same
  `(dataset, cell_line, anchor_gene)` unit as the positive;
- `C2G` and `G2C` remain separate in every output table.

The task contracts own any further positive-key or gallery eligibility rules.

## Aggregation boundary

Per-query fields are retained before summary. Summary metric names and
denominators are defined in `docs/metrics/aggregation.md` and
`docs/tasks/output_schemas.md`. The current benchmark does not silently assume
micro-averaging, macro-averaging, weighting, or pooling across datasets or cell
lines.

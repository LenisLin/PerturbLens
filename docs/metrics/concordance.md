# Group Concordance Metrics

## Scope

Group analysis is directionless: it compares two cohorts or group summaries
without assigning a query direction. The current benchmark group metric family
is:

- cosine similarity
- `PCC` (Pearson correlation coefficient)
- bias-corrected `e_distance`

Task-specific cohort construction and denominators are defined in
`docs/tasks/task1.md` and `docs/tasks/task2.md`. This document owns the metric
meaning and calculation inputs, not the choice of which task comparisons are
lawful.

## Common inputs

For every metric, the two compared objects must be in the same declared
representation space and have aligned feature identity. The task contract must
identify the cohorts, the comparison unit, and the number of instances used.
The emitted result retains `metric_name`, `metric_value`, and the denominator
fields required by the task output schema.

`Gene`, `Pathway`, and FM are distinct representations. A metric value must not
be compared across representations without the representation label and its
availability context.

## Cosine similarity

For aligned non-zero vectors `x` and `y` in one representation, cosine
similarity is:

```text
cosine(x, y) = (x dot y) / (||x||_2 ||y||_2)
```

The task contract determines whether `x` and `y` are cohort centroids or other
lawful group summaries. The current documents do not approve a zero-vector
policy, missing-feature imputation, or an alternative normalization. Those
cases must be specified before implementation if they occur.

## PCC

For aligned vectors with `m` coordinates, PCC is:

```text
PCC(x, y) = sum_i((x_i - mean(x)) * (y_i - mean(y)))
            / sqrt(sum_i((x_i - mean(x))^2) * sum_i((y_i - mean(y))^2))
```

The coordinates and any preprocessing applied before this calculation are
owned by the representation and task data contracts. The current benchmark
does not specify a constant-vector or missing-coordinate policy.

## Bias-corrected e_distance

The current benchmark contract fixes two facts:

- the reported metric is bias-corrected `e_distance`;
- `e_distance` uses cell-wise squared Euclidean distances.

The exact estimator, bias-correction expression, pairing or subsampling
procedure, and aggregation rule are not defined by the current contract. They
must be approved and versioned before a production implementation is treated
as canonical. Implementers must not silently substitute raw Euclidean distance
or an uncorrected estimator.

Task-specific denominator requirements are already fixed:

- Task1 marks `underpowered_for_e_distance=true` when either comparison side
  has fewer than `2` instances.
- Task2 emits `n_chem_sub` and `n_gen_sub` as the subsampled instance counts
  used by `e_distance`.

The presence of these fields does not determine the unresolved estimator or
the policy for an invalid value.

## Interpretation boundary

These metrics quantify concordance of the declared response representations.
They do not, by themselves, establish causal equivalence, biological mechanism,
or generalization beyond the lawful datasets, cell contexts, perturbation
types, and representations used by the task.

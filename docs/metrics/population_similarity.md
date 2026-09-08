# Population Similarity Metrics

## Question

Population similarity asks whether two declared perturbation responses have similar geometry or distributions. It is directionless unless a task explicitly defines an asymmetric statistic.

## Primary centroid metrics

### Cosine similarity

For aligned nonzero response vectors `x` and `y`:

```text
cosine(x,y) = x·y / (||x|| ||y||)
```

It emphasizes response direction rather than absolute magnitude.

### Pearson correlation

Pearson correlation compares coordinate-wise response patterns after centering across features.

### Response-strength ratio/difference

Response norms may be compared separately from direction:

```text
strength(x) = ||x||
```

Do not interpret norm as response identity.

## Distributional secondary metrics

When lawful single-cell or morphology distributions are available, secondary analyses may use:

- standard energy distance using Euclidean norm;
- MMD with a frozen kernel/bandwidth rule;
- Sinkhorn/OT distance with frozen cost/regularization.

A distribution metric must retain its sampling level and estimator settings. The project does not use a squared-Euclidean energy expression that collapses in expectation to a mean-only quantity as evidence for general distributional differences.

## Cross-representation comparison

Raw distances from Gene, Pathway, FM, CellProfiler, and deep morphology spaces are not numerically comparable across spaces. Compare standardized effect/calibration, paired ranks, or task-level outcomes rather than raw units.

## Required output context

Each metric row preserves:

- biological relation/task;
- comparison unit(s);
- readout modality;
- intervention type;
- state representation;
- response view;
- metric name/value;
- observation counts/support;
- source/context/time/dose fields required by the task.
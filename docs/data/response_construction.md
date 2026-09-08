# PerturbLens Response Construction

## Purpose

State representation describes an observed state. Response construction describes how that state changes relative to an explicit reference. Response construction is upstream of similarity/retrieval/prediction metrics.

Primary response views are `Delta` and `SystemaResidual`.

## 1. Delta

For condition `k` in state representation `r`:

```text
Delta(k,r) = mean_state(perturbed k,r) - mean_state(matched controls k,r)
```

For source-native perturbational signatures already expressed as an effect relative to controls, the source-native effect may instantiate `Delta` if the source contract records that semantics.

### Matched-control requirements

Control references must be lawful for the source and task. Matching priority is declared before response construction and may include source/dataset, biological context, experimental block, time, and assay design.

A response manifest records the exact control pool and counts for every condition.

## 2. SystemaResidual

Systema-style evaluation asks whether a perturbation differs from the broader perturbed population rather than only from control.

For a condition `k`:

```text
SystemaResidual(k,r) = mean_state(k,r) - mean_state(lawful perturbed reference pool,r)
```

The perturbed reference pool is task-specific but must be fixed before scoring. It should match biological context/readout/source constraints required by the task and must avoid unintended target/query leakage where relevant.

SystemaResidual is a **perturbation-specific view**, not a corrected biological truth. Shared stress, cell-cycle, toxicity, or acquisition effects may be removed or downweighted even when biologically real.

## Reference-pool registry

Every response object references a persisted registry containing:

- `reference_id`
- pool eligibility rule
- included condition/observation IDs
- excluded IDs and reasons
- context/readout/source/time/dose constraints
- leave-one-condition-out behavior where applicable
- observation count

## Morphology variants

The same response views apply in CellProfiler or fixed deep-morphology state spaces after morphology-specific normalization:

```text
MorphDelta = perturbed morphology state - matched control morphology state
MorphSystemaResidual = perturbed morphology state - lawful perturbed morphology reference
```

No direct numeric comparison is made between transcriptomic and morphology vector norms without within-space calibration.

## Response strength

For a vector response `R`, `||R||` may summarize magnitude after the representation's declared scaling. Response strength is not response identity. Equal norm can accompany orthogonal or opposite biological changes.

## Single-cell/distributional information

Primary Delta/SystemaResidual objects are directional centroid responses. When single-cell or single-image distributions are used, distributional summaries are retained separately rather than being mislabeled as centroid deltas.

## Provenance

Every response build records source/state manifests, representation version, response view, reference registry, feature index, seed/subsampling where relevant, and output hash.
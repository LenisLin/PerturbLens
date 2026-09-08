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

## Scope and reusable response bundles

Response bundles follow the [data architecture](architecture.md) and
[common manifest](manifests.md). Required additional manifest fields are
`response_build_id`, `response_view`, `response_scope`, `task_name`, `split_id`,
`reference_spec_id`, state artifact IDs, relation artifact IDs where applicable,
and the exact aggregation/weighting rule.

| `response_scope` | Required binding | Reuse boundary |
| --- | --- | --- |
| `source_global` | Source/state/reference specification; task and split may be null | Only if references and state preprocessing are independent of the downstream task/split |
| `task_global` | Non-null `task_name` and task-frozen reference specification | Only within compatible task cohorts; split may be null only if it cannot change pool legality |
| `split_specific` | Non-null `task_name`, `split_id` and fold/partition bindings | Only within that split and its allowed reference access |

Delta can be source-global when experimental controls, preprocessing and
aggregation are fixed independently of the task. It is not automatically
source-global if fitted normalization or control availability depends on a split.
SystemaResidual is at least task-global; it is split-specific whenever held-out
identities, query exclusions or allowed reference access change the pool.
SystemaResidual is not published as an unrestricted source-global response.

The scope describes response reuse; `fit_scope` describes how statistics were
estimated. Both must be recorded. Evaluation-only references are never passed as
model inputs or used to fit training transformations. Predictions and observed
responses use the declared same legal coordinate/reference system at scoring;
that does not authorize accessing held-out outcomes during prediction.

`reference_registry.parquet` has primary key `reference_id` and records
`reference_spec_id`, `reference_kind` (`control`, `perturbed`, `source_native`),
`response_scope`, `task_name?`, `split_id?`, `fold_id?`, eligibility rule,
source/context/readout/time/dose constraints, leave-one-condition-out behavior,
`n_conditions?`, `n_observations?`, `membership_path?` and source-reference evidence.

`reference_membership.parquet` has primary key
`(reference_id, member_level, member_id)` with `condition_id`,
`experimental_unit_id?`, `included` (bool), `weight?`, and `exclusion_reason?`.
`member_level` names observation, experimental unit, or condition. Enumerate
included members and rejected candidates under the declared reference universe;
weights and aggregation order must reproduce the reference. Source-native
signatures whose provider does not expose control membership record that
limitation and upstream normalization/reference documentation, not fictional
members or counts. Only tasks accepting that source contract may use them.

`response_index.parquet` extends the logical matrix index with `response_id`,
`condition_id`, `reference_id`, representation and response-view identity,
condition/reference counts and validity/exclusion status. Feature axes follow
the [matrix contract](matrix_semantics.md). Row-specific exclusions remain
auditable; an excluded response does not receive a fabricated zero vector.

For split-specific operations, freeze membership from condition/entity metadata
before building fitted states or references. The lifecycle diagram is a logical
dependency map, not permission to build all responses before split definition;
see the [workflow](workflow.md).

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

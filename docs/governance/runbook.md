# PerturbLens Runbook

The [data workflow](../data/workflow.md) owns intake, preparation and build gates.
This runbook owns scientific run isolation, manifests, execution and result
handoff. Register validated result evidence under the
[evidence index](evidence_index.md); a completed preservation operation is not a
completed scientific run.

## Run families

| Run family | Purpose |
| --- | --- |
| `r1_framework` | source inventory, state/response representation QC, metric calibration |
| `r2_genetic` | genetic inner, unseen-context, unseen-target analyses |
| `r3_chemical` | chemical inner, unseen-context, unseen-compound, unseen-target analyses and time/dose covariates |
| `r4_cross_intervention` | chemical-genetic matched target/context analyses |
| `r5_cross_readout` | transcriptomic-morphological matched response analyses |
| `r6_combination` | genetic and chemical combination compositionality analyses |

## Required run bundle

Each run directory must include:

- `run_manifest.json`
- `input_manifest.json`
- `split_manifest.json` where a split is used
- `response_manifest.json`
- `metric_manifest.json`
- result tables defined by `docs/tasks/output_schemas.md`
- `validation_assertions.json`

Prediction runs also include `model_manifest.json` describing training data, model inputs, hyperparameters, and checkpoint provenance.

## Execution rules

1. One scientific run uses one immutable `run_id`.
2. Input source hashes/versions and contract versions are recorded before computation.
3. Response objects are built before task metrics; a metric cannot silently redefine control or Systema references.
4. Split manifests are materialized before model fitting.
5. Held-out contexts, targets, compounds, or combinations may not influence model fitting except through explicitly allowed external prior representations.
6. Cross-intervention and cross-readout matching tables are materialized before similarity/retrieval/prediction.
7. Combination null predictions are materialized separately from learned-model predictions.
8. Figures consume validated plot-ready tables; rendering code does not recompute scientific statistics.

## Active roots

Use `docs/governance/storage_policy.md` only.

Recommended paths:

```text
/mnt/NAS_21T/ProjectData/PerturbLens/data/<source_or_object>/
/mnt/NAS_21T/ProjectData/PerturbLens/runs/<run_id>/<run_family>/
/mnt/NAS_21T/ProjectData/PerturbLens/artifacts/<run_id>/
```

## Failure rule

Partial outputs may be retained for diagnostics but cannot be promoted into the evidence index unless the owning run's required validation gates pass.

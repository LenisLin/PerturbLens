# PerturbLens Response Construction

## Role

This document owns the project-level vocabulary for constructing perturbation responses from state representations. Source-specific preprocessing still owns how raw observations become lawful state vectors. Task contracts own legal control/reference pools and comparison units.

The response object is conceptually:

```text
R = Response(state_perturbed, reference_state)
```

Response construction is separate from the downstream similarity, retrieval, or prediction metric.

## Status

The two primary response views below are scientifically approved for PerturbLens. Exact task-specific reference pools, standardization rules, zero-vector handling, and distributional extensions remain implementation details to freeze before production analyses.

Legacy M2M Task1/Task2 delta objects keep their historical semantics until explicitly migrated.

## State Representation Families

Transcriptomics:

- Gene;
- Pathway;
- FM embeddings.

Morphology, once a formal source/representation contract is approved:

- CellProfiler features;
- fixed deep morphology embeddings.

All response comparisons require a fixed representation definition and aligned feature identity within that representation.

## Control-Referenced Response

For a lawful condition `k`, define the population centroid in representation space:

```text
mu_pert(k) = mean state of perturbation condition k
mu_ctrl(k) = mean state of the matched legal control pool
```

The basic control-referenced response is:

```text
Delta_control(k) = mu_pert(k) - mu_ctrl(k)
```

This view measures the total state displacement associated with the perturbation relative to control.

### Interpretation

- direction identifies which coordinates/programs/features change;
- norm or other magnitude summaries measure response strength;
- similarity between two delta vectors measures whether their response geometry aligns.

Response strength is not equivalent to response specificity.

### Transcriptomics

For Gene/Pathway spaces, coordinate-wise effects are interpretable at the corresponding feature resolution.

For FM spaces, delta is a displacement in a fixed learned representation. Its coordinates are not automatically treated as biological variables.

### Morphology

For CellProfiler features, control-based normalization/sphering must be defined upstream of or jointly with the delta contract. The response may then be expressed as a standardized feature displacement.

For deep image embeddings, the encoder and image aggregation procedure must be fixed before response construction.

## Systema-Style Perturbation-Specific Reference

Systema motivates evaluating perturbation-specific effects relative to the average of perturbation-specific centroids rather than only the control centroid.

For a task-defined lawful reference set `P_ref` of perturbations:

```text
mu_perturbed_ref = mean_{p in P_ref}(mu_pert(p))
Delta_systema(k) = mu_pert(k) - mu_perturbed_ref
```

The task contract must define `P_ref` so that the reference is leakage-safe and comparable across queries/splits.

### Interpretation

`Delta_systema` emphasizes how perturbation `k` differs from the average perturbed state. It suppresses a component shared by many perturbations and therefore focuses evaluation on perturbation-specific landscape structure.

It is **not** called a corrected biological truth. The removed systematic component may contain technical bias, selection effects, or real shared biology.

Reference: Viñas Torné et al., Systema, https://doi.org/10.1038/s41587-025-02777-8

## Control And Systema Views Must Be Parallel

Where feasible, key claims should be checked under both views:

- control view: total perturbation-associated effect;
- Systema view: perturbation-specific effect relative to the perturbed landscape.

A result that appears only under one view is scale/reference-dependent and should be interpreted accordingly.

## Response Magnitude

For a response vector `Delta` in a fixed representation:

```text
response_strength = ||Delta||
```

The norm definition must be representation-specific and versioned.

Do not compare raw norms across Gene, Pathway, FM, CellProfiler, and deep morphology spaces as if they had common units.

Cross-representation comparisons should use within-space calibration, rank/quantile summaries, or task-specific anchors.

## Standardized Effects

A standardized response may be useful when features have strongly different background scales:

```text
Delta_std_j = (mu_pert_j - mu_ref_j) / s_ref_j
```

The reference variance `s_ref` must be estimated from an independent/legal pool and its zero/near-zero policy must be explicit.

Standardization changes the estimand from absolute displacement to displacement relative to background variability.

## Distributional Response Extensions

Centroid deltas cannot distinguish all population-distribution changes. Where the scientific question concerns heterogeneity or state occupancy, supplementary response objects may include:

- changes in state/cluster occupancy;
- changes in feature variance or covariance;
- MMD/kernel mean embeddings;
- OT/Sinkhorn transport summaries;
- other explicitly distribution-sensitive statistics.

These extensions require separate metric and inference contracts. They must not be inferred from the label `e_distance` alone.

## Time And Dose

For chemical analyses, a response is indexed by time and dose when those values are available:

```text
R(compound, context, time, dose)
```

The primary R3 task treats time/dose as explanatory covariates. It must not pool incompatible conditions and then interpret their variability purely as measurement error.

A dedicated dynamic response task requires dense enough time/dose coverage and a separate approval.

## Combination Response Boundary

A combination response is constructed from the observed combination condition in the same representation/reference view as its constituent singles.

A compositional null is a separate object:

```text
R_expected(A+B) = Null(R_A, R_B)
```

The interaction residual is then:

```text
I(A,B) = R_observed(A+B) - R_expected(A+B)
```

The null depends on the response scale. Simple vector addition is not automatically valid for every transformed, standardized, occupancy, or nonlinear embedding space.

Systema's matching-mean baseline is one precedent for a strong simple combination reference. Exact R6 nulls belong in the combination task contract.

## Required Provenance Fields

Every emitted response object should be traceable to at least:

- source dataset;
- cellular context;
- perturbation identity and intervention type;
- representation name/version;
- response view (`control` or `systema` or approved extension);
- control/reference pool definition;
- time/dose when available;
- aggregation level;
- source instance/replicate identifiers;
- response-construction version.

## Pending Implementation Decisions

Before production PerturbLens analyses, freeze:

- task-specific legal Systema reference pools;
- morphology normalization and aggregation;
- response-norm choices per representation;
- zero/constant/missing-feature handling;
- any standardized-effect definition;
- any distributional response family;
- interaction nulls for R6;
- migration rules from existing Task1/Task2 delta objects.

# R6 Combination Compositionality Contract

## Scientific question

Can observed combination perturbation responses be explained by response structure learned from their constituent single perturbations, and when do reproducible residual components remain?

## Scope

Genetic and chemical combinations are primary separate strata. A combination is eligible only when:

- all constituent identities are known;
- corresponding single perturbations are measured in a compatible context/assay;
- matched controls exist;
- time/dose/strength compatibility is sufficient for the declared null;
- replicate support is recorded.

## Nulls

Each analysis declares a phenotype/response-scale-appropriate null before scoring.

Candidate vector null:

```text
R_null(A+B) = R(A) + R(B)
```

Alternative matching-mean or dose-aware nulls may be used when justified. No universal additive null is assumed across nonlinear representations or phenotype scales.

## Interaction residual

```text
I(A,B) = R_observed(A+B) - R_null(A+B)
```

Residual magnitude alone is insufficient. R6 asks whether residual direction/program structure is reproducible across replicates, contexts, representations, or readouts.

## Prediction

Compare simple null/additive baselines, linear models, and predeclared complex combination models under:

- both constituents seen;
- one constituent unseen;
- both constituents unseen;

when coverage supports those splits.

## Cross-representation/readout analyses

A candidate emergent response is stronger evidence when supported in interpretable Pathway/CellProfiler features or replicated across transcriptomic and morphology spaces. Deep latent residuals alone are not labeled biological programs.

## Claim boundary

Non-additivity is relative to the declared response scale and null. It is not automatically pharmacological synergy, genetic epistasis, or a novel mechanism.
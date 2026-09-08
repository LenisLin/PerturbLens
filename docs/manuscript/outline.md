# PerturbLens Manuscript Outline

## Central thesis

PerturbLens maps how cellular perturbation-response information is preserved, lost, or reorganized across increasingly difficult biological boundaries: within perturbation classes, across cellular contexts and targets, across intervention modality, across transcriptomic/morphological readouts, and under perturbation composition.

## Introduction

1. Perturbation-response prediction is central to virtual-cell and phenotypic profiling.
2. Complex models often provide limited gains over strong baselines in stringent generalization settings.
3. Standard scores can be dominated by shared/systematic response structure.
4. Existing work separately studies response decomposition, cross-context prediction, chemical-genetic translation, RNA-morphology integration, and combinations.
5. The missing unifying question is what **response information** survives each biological boundary.
6. Introduce PerturbLens as a descriptive response-centric framework.

## Results

### R1 — A unified framework for perturbation-response characterization

Define sources, state representations, response construction, evidence families, and coverage.

### R2 — Genetic perturbation responses reveal a hierarchy of learnable information

Inner -> unseen context -> unseen target; characterize which response properties stop transferring.

### R3 — Chemical perturbation responses separate compound-, target-, and context-level learnability

Inner -> unseen context -> unseen compound -> unseen target; time/dose as explanatory covariates.

### R4 — Target-linked responses are partially conserved across chemical and genetic interventions

Use internally supported response structure to quantify cross-intervention conservation and biological resolution.

### R5 — Transcriptomic and morphological readouts preserve overlapping and distinct response information

Compare response strength, geometry, retrieval, prediction, and intervention x readout conservation.

### R6 — Combination perturbations define the compositional boundary of response space

Test single-response nulls, residual reproducibility, and combination prediction.

## Discussion

Interpret the boundary ladder rather than a single overall score. Discuss shared versus specific response information, context/target novelty, intervention-specific divergence, readout-specific observability, and combination non-compositionality. Explicitly separate empirical learnability from absolute predictability and association from mechanism.

## Methods order

1. data/source inventory;
2. condition and state object model;
3. state representations;
4. Delta/SystemaResidual construction;
5. task splits/matching/nulls;
6. population similarity;
7. retrieval;
8. prediction metrics/models/baselines;
9. statistics/aggregation;
10. validation/provenance.
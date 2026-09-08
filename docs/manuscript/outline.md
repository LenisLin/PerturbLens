# Manuscript Outline

## Current Paper Shape

PerturbLens is a response-centric characterization study of cellular perturbation information. The manuscript is organized by biological boundaries rather than by model family or legacy Task number.

The current main-text sequence is:

1. R1 framework and measurement definition;
2. R2 genetic response learnability;
3. R3 chemical response learnability;
4. R4 chemical-genetic cross-intervention conservation;
5. R5 transcriptomic-morphological cross-readout conservation;
6. R6 combination compositionality;
7. discussion of the hierarchy of response-information conservation and evidence boundaries.

This outline defines argument responsibilities. It must not contain invented numerical results.

## Argument Spine

```text
research question
  -> state representation
  -> response construction
  -> biological boundary
  -> geometry / retrieval / prediction evidence
  -> bounded interpretation
```

The repeated question across Results is:

> Which perturbation-response information survives the next biological boundary?

## Section Responsibilities

### Title And Abstract

Position PerturbLens as a response-centric study rather than a model leaderboard. State only claims supported by validated outputs.

### Introduction

Motivate the gap between virtual-cell prediction performance and understanding of what response information is actually stable, specific, transferable, cross-modal, and compositional. Establish that strong baselines, response decomposition, cross-context prediction, multimodal profiling, and combination prediction already have substantial precedent; end with the boundary-conservation question that unifies PerturbLens.

### Methods

Methods should define, in order:

1. data sources and comparison metadata;
2. state representations;
3. response construction, including control and Systema-style reference views;
4. lawful task/generalization splits;
5. population similarity;
6. instance retrieval;
7. model prediction metrics and baselines;
8. inference, aggregation, validation, and evidence traceability.

Authoritative formulas and units belong in `docs/data/`, `docs/tasks/`, and `docs/metrics/`.

### Results 1 — Framework

Define what is measured and compared. Introduce data, representation families, response views, evaluation layers, and the boundary ladder. Do not turn R1 into a representation leaderboard.

### Results 2 — Genetic Learnability

Present inner/replicate, cross-context, and unseen-target settings. Emphasize what response information is lost or retained rather than only the change in aggregate prediction score.

### Results 3 — Chemical Learnability

Present inner compound, cross-context, cross-compound/same-target, unseen-compound, and unseen-target settings. Time and dose are explanatory covariates and sensitivity analyses unless a future dense design justifies a dedicated dynamic Result.

### Results 4 — Cross-Intervention Conservation

Use the Chem2Gen lineage to ask what target-linked response information survives switching between chemical and genetic intervention. Integrate within-intervention learnability from R2/R3 with C2G/G2C geometry/retrieval.

### Results 5 — Cross-Readout Conservation

Compare transcriptomic and morphology response structure. The highest-priority synthesis is the intervention x readout map, asking whether chemical-genetic conservation itself is conserved across readout modalities.

### Results 6 — Combination Compositionality

Use genetic and chemical combinations as a final stress test. Compare observed combinations against strong constituent-based nulls and determine whether residual response information is stable and structured.

### Discussion

Synthesize the boundary ladder rather than recap model rankings. Discuss which response information appears robust at which biological resolution, where it becomes intervention- or readout-specific, and where combination responses exceed single-perturbation structure. Separate descriptive evidence from causal explanation.

## Figure And Table Handoff

The current main-figure roles are maintained in `docs/visualization/figure_plan.md`. Each Result must consume versioned task outputs and retain representation, response view, denominators, split identity, and evidence provenance.

## Writing Sequence

1. stabilize response, metric, and task definitions;
2. complete R2/R3 backbone analyses;
3. migrate/extend R4 Chem2Gen evidence;
4. contract and execute R5 multimodal analyses;
5. contract and execute R6 combination analyses;
6. write Results around validated evidence;
7. synthesize the hierarchy of response-information conservation in Discussion.

# PerturbLens Main Result Architecture

## Argument spine

The manuscript is organized by biological boundaries, not by representation or metric.

```text
R1: What do we measure?
  -> R2/R3: What is learnable within intervention classes?
  -> R4: What survives changing intervention modality?
  -> R5: What survives changing readout modality?
  -> R6: Can the learned response structure compose?
```

## R1 — Framework

### Question

What is the response object and how is it compared?

### Main figure responsibilities

- data/readout/intervention landscape;
- state representations: Gene, Pathway, FM, CellProfiler, DeepMorphology;
- response views: Delta and SystemaResidual;
- three evidence families: population similarity, retrieval, prediction;
- biological boundary ladder and source coverage.

### Boundary

R1 is methods/data characterization. It does not claim that one representation or metric is biologically superior.

## R2 — Genetic learnability

### Question

What genetic response information remains learnable from inner splits to unseen contexts and unseen targets?

### Main progression

1. inner/replicate response structure;
2. unseen cellular context;
3. unseen target;
4. response-property decomposition of performance loss.

### Supporting analyses

intervention mode, target family, response strength, Systema sensitivity, representation sensitivity, independent-support thresholds.

## R3 — Chemical learnability

### Question

What chemical response information is compound-specific, target-linked, context-dependent, or transferable to unseen targets?

### Main progression

1. inner compound response;
2. unseen context;
3. unseen compound with known target structure;
4. unseen target;
5. explanatory time/dose and multi-target analyses.

Time/dose remain covariates unless a matched dynamic dataset motivates a separate future study.

## R4 — Cross-intervention conservation

### Question

Given internal response support in chemical and genetic perturbations, what target-linked information survives changing intervention modality?

### Main progression

1. matched target/context coverage;
2. population similarity;
3. C2G and G2C retrieval;
4. internal learnability versus cross-intervention conservation;
5. Gene versus Pathway versus FM resolution.

### Key interpretation

Internally supported but cross-intervention divergent targets are intervention-specific response candidates, not automatically evidence of off-target pharmacology or causal inequivalence.

## R5 — Cross-readout conservation

### Question

Which response information is shared between transcriptomic and morphological readouts?

### Main progression

1. matched multimodal coverage tier;
2. response-strength correspondence;
3. perturbation-geometry correspondence;
4. cross-modal retrieval;
5. cross-modal prediction;
6. intervention-by-readout interaction: does chemical-genetic conservation agree in RNA and morphology?

### Key interpretation

Readout discordance is a scientific result when reproducible; it is not automatically a failed robustness check.

## R6 — Combination compositionality

### Question

Can combined responses be explained by constituent single-perturbation response structure?

### Main progression

1. source and combination coverage;
2. lawful additive/matching nulls;
3. observed-versus-null response similarity;
4. interaction residual reproducibility;
5. learned combination prediction versus simple nulls;
6. cross-representation/readout support for residual programs.

### Key interpretation

An interaction residual is always interpreted relative to the declared response scale and null.

## Cross-result synthesis

The synthesis is not a single overall score. It maps response information across:

```text
learnability
transferability
cross-intervention conservation
cross-readout conservation
compositionality
```

Each major conclusion should state the state representation, response view, biological boundary, evidence family, support/coverage, and validation status.
# PerturbLens Project Definition

## Research position

PerturbLens is a descriptive and characterization study of cellular perturbation responses. It studies **response information** rather than treating model performance as the scientific object.

## Central question

> What information in cellular perturbation responses is reproducible within perturbation classes, transferable across cellular contexts and targets, conserved across intervention and readout modalities, and compositional under combined perturbations?

The project asks how response information changes as increasingly difficult biological boundaries are crossed:

```text
within perturbation
-> cellular context
-> target / compound novelty
-> intervention modality
-> readout modality
-> perturbation composition
```

## Conceptual layers

### 1. Data

A perturbation observation is defined by intervention identity, target annotation where applicable, cellular context, readout modality, time, dose or perturbation strength, replicate/source information, and combination membership where applicable.

### 2. State representation

Primary transcriptomic representations:

- `Gene`
- `Pathway`
- `FM`

Primary morphology representations:

- `CellProfiler`
- `DeepMorphology`

No representation is assumed to be the biological truth. Each is a lens that preserves and compresses different response information.

### 3. Response construction

Primary response views:

- `Delta`: perturbation state relative to matched control;
- `SystemaResidual`: perturbation state relative to an explicitly lawful perturbed reference pool, emphasizing perturbation-specific structure.

The response view is separate from the downstream metric.

### 4. Evidence family

Every major biological relation is studied through three complementary evidence families where lawful:

- population similarity: is response geometry conserved?
- instance retrieval: is perturbation or target identity retained?
- model prediction: can response information be learned out of sample?

## Main Results

### R1 — Framework

Defines data, state representations, response construction, metrics, comparison axes, and coverage. R1 does not use model ranking as a biological conclusion.

### R2 — Genetic response learnability

Tests inner/replicate structure, unseen cellular context, and unseen target. The scientific output is which components of genetic response remain learnable as novelty increases.

### R3 — Chemical response learnability

Tests inner structure, unseen cellular context, unseen compound with known target information, and unseen target. Time and dose are explanatory covariates rather than a standalone main result.

### R4 — Cross-intervention conservation

Tests what target-linked response information is preserved between chemical and genetic perturbations.

### R5 — Cross-readout conservation

Tests what perturbation-response information is shared or modality-specific between transcriptomics and morphology.

### R6 — Combination compositionality

Tests whether combined perturbation responses are explained by lawful single-perturbation references and whether reproducible interaction residuals remain.

## Active source scope

Current transcriptomic source families are LINCS and human scPerturb-derived datasets. Morphology and combination source sets must pass explicit source/coverage freezes before R5 or R6 production analysis. Source availability does not imply a lawful task.

## Contribution boundary

PerturbLens does not claim that:

- a complex model's failure establishes a mathematical prediction ceiling;
- a state embedding is a complete representation of cellular state;
- chemical-genetic similarity establishes causal equivalence;
- cross-readout association establishes a causal RNA-to-morphology mapping;
- a non-additive vector residual is automatically biological synergy.

The intended contribution is a response-centric map of what information is observed, identifiable, transferable, cross-boundary conserved, and compositional under explicitly defined representations and comparison regimes.
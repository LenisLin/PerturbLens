# PerturbLens Research Proposal

## Working title

**PerturbLens: mapping the information structure of cellular perturbation responses across biological boundaries**

## Motivation

Modern perturbation biology increasingly uses transcriptomic and morphological readouts to predict cellular responses to genetic or chemical interventions. Yet recent virtual-cell evaluations show that complex models often provide limited gains over simple baselines under stringent unseen-context or unseen-perturbation settings. At the same time, response-decomposition studies show that apparently high performance can be driven by generic or shared response components rather than perturbation-specific information.

These observations motivate a more basic descriptive question: **what response information is actually present, identifiable, transferable, and compositional in existing perturbation data?**

PerturbLens therefore treats the measured perturbation response—not the model—as the primary scientific object.

## Central question

> What information in cellular perturbation responses is reproducible within perturbation classes, transferable across cellular contexts and targets, conserved across intervention and readout modalities, and compositional under combined perturbations?

## Conceptual framework

A perturbation observation is represented as:

```text
raw observation
-> state representation
-> response construction relative to an explicit reference
-> biological relation / evaluation
```

### State representations

Transcriptomics:

- Gene-level expression space;
- Pathway/program space;
- Foundation-model embedding space.

Morphology:

- interpretable CellProfiler feature space;
- deep-image embedding space.

The representations are alternative lenses. Higher model complexity does not imply higher biological validity.

### Response views

`Delta` describes the change from matched control.

`SystemaResidual` describes deviation from an explicitly defined perturbed reference pool and is used to reduce dominance by shared systematic response structure.

These are response constructions, not evaluation metrics.

### Evidence families

**Population similarity** measures whether response geometry is conserved.

**Instance retrieval** measures whether perturbation/target identity remains identifiable.

**Model prediction** measures whether response information can be learned out of sample under a declared generalization split.

Together they separate similarity, specificity, and learnability.

## Scientific progression

### R1 — What do we measure?

Establish source coverage, representations, response views, metrics, baselines, and split axes. R1 is the methodological coordinate system.

### R2 — What can be learned from genetic perturbations?

Move from inner/replicate comparisons to unseen cellular contexts and unseen targets. The goal is not merely to show performance degradation, but to identify which response properties—magnitude, direction, responding-gene structure, pathway structure, or target identity—cease to transfer.

### R3 — What can be learned from chemical perturbations?

Separate compound-specific, target-linked, context-dependent, and unseen-target generalization. Unseen compound with a known target is distinct from a genuinely unseen target. Dose and time are explanatory covariates that may alter magnitude, direction, or response specificity.

### R4 — What survives a change in intervention modality?

Compare target-matched chemical and genetic responses after establishing each intervention class's internal learnability. The key quantity is not raw chemical-genetic similarity alone, but the fraction and biological resolution of internally supported target-linked information that survives the intervention boundary.

### R5 — What survives a change in readout modality?

Compare transcriptomic and morphological response strength, perturbation geometry, retrieval, and cross-modal predictability. The aim is to determine which response information is shared and which is readout-specific, especially in relation to target/context structures established in R2-R4.

A particularly distinctive analysis is the intervention-by-readout matrix:

| | Transcriptomics | Morphology |
| --- | --- | --- |
| Genetic | genetic molecular response | genetic morphological response |
| Chemical | chemical molecular response | chemical morphological response |

This asks whether chemical-genetic conservation is itself readout-dependent.

### R6 — Are perturbation responses compositional?

Use genetic and chemical combinations as the strongest stress test. Compare observed combination responses with explicit single-perturbation nulls. Determine whether residuals are reproducible and whether any apparent emergent component is supported across representations or readouts.

## Primary analyses

Across R2-R6, primary state representations and response views are fixed before result inspection. Each major conclusion should be classified as:

- representation-consistent;
- resolution-dependent (for example Pathway-conserved but Gene-divergent);
- readout-specific;
- intervention-specific;
- context-specific;
- non-compositional relative to a declared null.

This classification turns representation differences into scientific interpretation rather than a leaderboard.

## Expected contribution

PerturbLens aims to provide a map of **response-information conservation across biological boundaries**:

```text
within
-> context
-> target/compound
-> intervention
-> readout
-> composition
```

The strongest contribution would not be a single metric or best model. It would be a coherent empirical account of what cellular response information persists as increasingly difficult biological boundaries are crossed, and which biological scales or modalities retain information lost by others.

## Claim boundary

PerturbLens is descriptive. It can identify reproducible response structure and its empirical transfer limits. It does not by itself establish causal pathway mechanisms, clinical efficacy, an absolute prediction ceiling, or direct causal mapping between transcriptomic and morphological changes.
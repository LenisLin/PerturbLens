# PerturbLens Project Definition

## Research Position

PerturbLens is a response-centric characterization study of cellular perturbations. Its primary scientific object is the **perturbation response**, not a specific prediction model or embedding.

The study asks how perturbation-response information is organized and how much of it remains reproducible, identifiable, learnable, transferable, cross-modal, and compositional as biological novelty increases.

## Central Question

> What information in cellular perturbation responses is reproducible within perturbation classes, transferable across cellular contexts and targets, conserved across intervention and readout modalities, and compositional under combined perturbations?

The study uses a boundary ladder:

```text
within
  -> cellular context
  -> target / compound
  -> intervention modality
  -> readout modality
  -> composition
```

Each boundary adds a stronger biological change. The study does not equate a drop in model score with a single failure mechanism; it asks which response information is lost or retained at each boundary.

## Four-Layer Analysis Framework

### 1. Data

Current transcriptomic sources are LINCS and scPerturb. Candidate extensions include matched transcriptomic-morphological perturbation resources and genetic/chemical combination datasets. Candidate sources do not enter production scope until a data contract is approved.

Dose and time are retained as explanatory covariates for chemical analyses unless a future dense dose-time design justifies a dedicated dynamic task.

### 2. State Representation

Primary transcriptomic families:

- `Gene`
- `Pathway`
- transcriptomic foundation-model (`FM`) embeddings

Primary morphology families:

- interpretable CellProfiler-derived morphology features
- fixed deep morphology embeddings

A representation is an observation lens. No representation is assumed to be a complete or privileged description of biological state.

### 3. Response Construction

Primary response views:

- control-referenced delta response;
- Systema-style perturbation-specific reference response.

The response-construction contract is maintained in [data/response_construction.md](data/response_construction.md). These views are not interchangeable: the control view measures total perturbation-associated displacement, whereas the Systema-style view emphasizes perturbation-specific structure relative to the average perturbed state.

### 4. Evaluation

Three evidence families are used throughout the study:

- **population similarity**: whether two response structures are geometrically similar;
- **instance retrieval**: whether response identity/specificity is retained;
- **model prediction**: whether response information can be learned out of sample under a declared generalization regime.

Metric ownership remains in `docs/metrics/`.

## Main Result Architecture

- **R1 — Framework**: data, state representations, response construction, comparison units, and evaluation definitions.
- **R2 — Genetic learnability**: inner split -> cross-cellular-context -> cross-target.
- **R3 — Chemical learnability**: inner split -> cross-context -> cross-compound/same-target -> unseen compound -> unseen target; dose/time as explanatory covariates.
- **R4 — Cross-intervention**: chemical-genetic conservation of target-linked response information.
- **R5 — Cross-readout**: transcriptomic-morphological conservation, shared geometry, cross-modal retrieval/prediction, and modality-specific response structure.
- **R6 — Combination**: compositionality, interaction residuals, and response components not explained by constituent single perturbations.

The detailed manuscript logic is maintained in [research/result_architecture.md](research/result_architecture.md).

## Relationship To M2M-Bench

M2M-Bench is the historical execution core from which PerturbLens grows.

- Retained Task1 provides existing within-source and cross-source concordance infrastructure.
- Retained Task2 provides the current chemical-genetic target-matched comparison infrastructure.
- Existing Task1/Task2 outputs keep their original semantics and names.
- New generalization, prediction, morphology, cross-readout, expanded-FM, and combination analyses require explicit PerturbLens contracts.

The mapping is maintained in [tasks/study_map.md](tasks/study_map.md).

## Contribution Boundary

PerturbLens is not primarily a new virtual-cell predictor and is not a representation leaderboard. Its intended contribution is a common response-centric framework for asking what biological information survives increasingly difficult boundaries.

A successful study may contain positive, negative, or uncertain findings. The framework does not assume that response structure is low-dimensional, that chemical and genetic interventions are equivalent, that transcriptomics and morphology encode the same biology, or that combination responses are additive.

## Claim Boundary

Similarity does not establish causal mechanism equivalence. Cross-modal correspondence does not establish an RNA-to-morphology causal mapping. A learned embedding is not treated as the true cellular state. A combination residual is not automatically molecular synergy. Model performance is not treated as an absolute information-theoretic ceiling.

Claims remain bounded by the datasets, representations, response constructions, legal comparison units, evaluation protocols, and evidence actually used.

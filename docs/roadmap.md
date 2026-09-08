# PerturbLens Research Roadmap

## Purpose

This roadmap translates the approved PerturbLens scientific reframing into staged execution. It separates project-level approval from implementation and evidence. Existing M2M runs are preserved; new result families become production-active only after their data, task, response, metric, and validation contracts are complete.

## Migration Principles

1. Preserve historical Task1/Task2 semantics, output names, manifests, and NAS provenance.
2. Make PerturbLens the active scientific framing before renaming code or storage paths.
3. Migrate one result family at a time; do not build an exhaustive representation-by-metric factorial benchmark.
4. Treat morphology, expanded FM coverage, prediction metrics, and combination tasks as explicit additions requiring contracts and source inventories.
5. Allow null and negative results; completion criteria are evidence quality, not favorable performance.

## Phase 0 — Scientific and Documentation Reframing

**Status:** approved and initiated.

Deliverables:

- project definition changed from Task1/Task2-centered M2M-Bench to response-centric PerturbLens;
- research proposal and literature landscape added;
- R1-R6 result architecture frozen at manuscript level;
- `docs/research/` added as a scientific-rationale domain;
- legacy task mapping documented.

This phase does not certify new numerical results.

## Phase 1 — Shared Response Infrastructure

### 1A. Response construction contract

Freeze:

- control-referenced delta semantics by representation;
- Systema-style perturbed-reference semantics and legal reference pools;
- response strength versus response identity fields;
- treatment of zero/constant vectors and missing features;
- distributional response extensions, if retained.

### 1B. Prediction metric contract

Freeze the PerturbLens prediction metric family using the VCC2026/Cell-Eval2 conceptual groups:

- perturbation discrimination;
- expression/profile error;
- direction fidelity;
- direction reach;
- significant-feature overlap;
- effect-size accuracy.

Define morphology analogues separately for interpretable CellProfiler features and deep embeddings.

### 1C. Generalization split vocabulary

Approve exact train/test legality for:

- inner/replicate splits;
- unseen cellular contexts;
- unseen genetic targets;
- unseen chemical compounds with seen targets;
- unseen chemical targets;
- cross-intervention mapping;
- cross-readout mapping;
- combinations.

## Phase 2 — R2 Genetic Learnability

Build a new genetic-learnability task contract rather than silently stretching legacy Task1.

Primary sequence:

```text
inner -> unseen context -> unseen target
```

Primary outputs must separate:

- response magnitude;
- response direction/geometry;
- perturbation discrimination/retrieval;
- prediction performance;
- representation and response-construction views.

Legacy Task1 genetic analyses may be reused only through an explicit alignment proof.

## Phase 3 — R3 Chemical Learnability

Primary sequence:

```text
inner
  -> unseen context
  -> new compound / seen target
  -> unseen compound
  -> unseen target
```

Time and dose enter as explanatory covariates, not as a separate main result unless a dense factorial source is later approved.

Chemical multi-target membership and target-confidence rules must be explicit before target-level generalization.

## Phase 4 — R4 Cross-Intervention

Migrate the scientific core of Chem2Gen/M2M Task2 into the PerturbLens boundary framework.

Required additions beyond legacy Task2:

- joint within-intervention learnability versus cross-intervention conservation analysis;
- representation-resolution analysis across Gene/Pathway/FM where lawful;
- explicit distinction between target-linked concordance and causal equivalence.

Legacy Task2 group/retrieval evidence remains reusable when its exact units match the new contract.

## Phase 5 — R5 Cross-Readout

### 5A. Data/source selection

Inventory candidate transcriptomic-morphology resources and classify them as:

- perturbation-label matched;
- context/dose/time matched;
- truly paired multimodal assays.

### 5B. Morphology representation contract

Approve:

- CellProfiler feature extraction/normalization;
- fixed deep image encoders;
- plate/batch/control normalization;
- treatment- and replicate-level aggregation.

### 5C. Cross-readout analyses

Primary questions:

- response-strength correspondence;
- perturbation-geometry correspondence;
- same-perturbation/same-target cross-modal retrieval;
- cross-modal prediction under held-out perturbation/context/target settings;
- shared versus readout-specific response structure.

A high-priority extension is the 2x2 intervention/readout map:

```text
                  Transcriptomics     Morphology
Genetic                 G,T               G,M
Chemical                C,T               C,M
```

This asks whether chemical-genetic conservation is itself conserved across readouts.

## Phase 6 — R6 Combination

Treat combinations as a compositional stress test of single-perturbation response structure.

Required design choices:

- separate genetic and chemical combination tasks;
- define the null/reference appropriate to each response scale;
- retain additive/matching-mean baselines;
- distinguish magnitude non-additivity from new response direction/programs;
- require replicate or cross-representation evidence before calling an interaction component stable.

## Phase 7 — Manuscript Synthesis

Once R2-R6 evidence is available, synthesize by biological boundary rather than by model family.

The manuscript should answer:

1. what response information is stable within a perturbation modality;
2. what survives context/target novelty;
3. what survives intervention change;
4. what survives readout change;
5. what remains compositional under combinations.

## Immediate Execution Queue

1. Implement/document the shared response-construction contract.
2. Implement/document prediction metrics and morphology metric analogues.
3. Build a dataset inventory for R2/R3/R5/R6 coverage before adding more models.
4. Draft exact task contracts for R2 and R3.
5. Map legacy Task1/Task2 outputs into the new result architecture without recomputation where lawful.
6. Only after those steps, expand FM or add morphology/combination pipelines.

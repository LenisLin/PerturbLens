# Decision: Reframe M2M-Bench As PerturbLens

Date: 2026-09-08

## Decision

The human lead approved reframing the scientific project from the Task1/Task2-centered **M2M-Bench** benchmark into **PerturbLens**, a response-centric characterization study.

The active scientific question becomes:

> What perturbation-response information is reproducible, learnable, transferable across contexts and targets, conserved across intervention and readout modalities, and compositional under combinations?

The main Results are organized as R1-R6:

1. framework;
2. genetic learnability;
3. chemical learnability;
4. chemical-genetic cross-intervention conservation;
5. transcriptomic-morphological cross-readout conservation;
6. combination compositionality.

## Rationale

The field has rapidly become crowded around virtual-cell model leaderboards, unseen-context/target generalization, response decomposition, and representation benchmarking. The project therefore requires a broader scientific unit of analysis than model performance or standalone Chem2Gen concordance.

PerturbLens keeps the existing Chem2Gen/M2M intellectual core but places it inside a hierarchy of biological boundaries. State representations and response constructions become observation lenses; geometry, retrieval, and prediction become complementary evidence levels.

## Compatibility Decision

Scientific naming changes before implementation/storage naming.

The following remain unchanged during staged migration:

- GitHub repository identifier `M2M-Bench`;
- Python package identifier `m2mbench`;
- historical Task1/Task2 contracts and output names;
- existing NAS `M2M` roots and run manifests;
- legacy script interfaces until explicitly migrated.

This preserves provenance and prevents documentation reframing from invalidating audited or in-progress execution artifacts.

## New Documentation Ownership

A new `docs/research/` domain owns:

- complete scientific proposal;
- literature/ecosystem analysis;
- R1-R6 result architecture.

Executable semantics remain owned by data, task, and metric contracts.

## New Shared Method Boundaries

The reframing approves the following project-level categories:

- transcriptomic state representations: Gene, Pathway, FM;
- morphology representations: CellProfiler features and fixed deep embeddings;
- response construction: control delta and Systema-style perturbation-specific reference;
- evaluation: population similarity, retrieval, and model prediction;
- dose/time: chemical explanatory covariates rather than a standalone Result by default.

Exact formulas, source inventories, split rules, and metric parameters remain implementation contracts and are not silently filled by this decision.

## Legacy Task Mapping

- Task1 supplies partial infrastructure/evidence candidates for R2/R3.
- Task2 supplies the primary legacy infrastructure/evidence candidate for R4.
- R5 and R6 require new contracts.
- No legacy output is renamed or automatically reclassified as PerturbLens evidence.

## Verification Boundary

This decision certifies the scientific and documentation reframing only. It does not certify:

- new numerical results;
- morphology data availability;
- VCC2026 metric implementation;
- expanded FM coverage;
- new generalization splits;
- combination analyses;
- manuscript readiness.

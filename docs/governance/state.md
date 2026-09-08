# PerturbLens Project State

Last updated: 2026-09-08

## Active scientific architecture

The project is fully defined as PerturbLens. The active main-result sequence is R1 Framework, R2 Genetic, R3 Chemical, R4 Cross-intervention, R5 Cross-readout, and R6 Combination.

There are no active historical Task1/Task2 contracts in the current architecture.

## Design status

Approved conceptual components:

- transcriptomic state representations: Gene, Pathway, FM;
- morphology state representations: CellProfiler and deep morphology embeddings;
- response views: control Delta and SystemaResidual;
- evidence families: population similarity, instance retrieval, model prediction;
- R2 genetic split ladder: inner -> unseen context -> unseen target;
- R3 chemical split ladder: inner -> unseen context -> unseen compound -> unseen target;
- time/dose as R3 explanatory covariates;
- R4 chemical-genetic target-linked conservation;
- R5 transcriptomic-morphological response conservation;
- R6 genetic/chemical combination compositionality.

## Execution status

The architectural reset does not certify any new R2-R6 production analysis. Source inventories, response-build manifests, split manifests, prediction runs, morphology ingestion, and combination runs must be generated under the PerturbLens contracts and storage roots.

Existing raw external source files can be reused only through new source manifests; prior project-specific derived outputs are not active PerturbLens evidence.

## Immediate execution blockers

1. exact source/coverage inventory for R2-R6;
2. final Systema reference-pool semantics per task;
3. frozen Cell-Eval2/VCC2026 package/version/configuration;
4. model registry and allowed input information for each split;
5. morphology dataset selection and matching tier;
6. combination source selection and interaction null definitions.

## Evidence boundary

Only artifacts produced or explicitly revalidated under current PerturbLens contracts may support PerturbLens manuscript claims.
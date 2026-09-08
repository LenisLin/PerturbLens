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

## Local checkout alignment — 2026-09-08

The checkout is synchronized with the PerturbLens architectural reset at
`c66fb7d`. Unpublished preparation code and tests tied to the retired contracts
are preserved in the Git-ignored `.local/legacy-pre-perturblens/` source tree,
alongside their original contracts. They are not active R2-R6 implementations.
Existing local FM extractor and worker changes remain available for reuse.

The retained extractor snapshot CLIs require adaptation to the current
state-build and run contracts. Repository synchronization and syntax checks do
not validate extraction, prediction, or scientific results.

At this alignment check, the NAS root declared in the storage policy does not
yet exist. No prior derived data or runs are moved or relabelled by this
source-checkout update.

## Source verification — 2026-09-08

- The active checkout and a separate publishable-tree preview each pass all
  12 maintained tests, including project identity and skill discovery checks.
- The `perturblens` 0.5.0 wheel builds offline and installs and imports in an
  isolated environment with the current repository metadata.
- All 15 pre-existing modified or untracked files are preserved byte-for-byte
  in the local source snapshot. The seven active extractor implementations
  retain their prior logic apart from project identity and CLI status strings;
  the three local worker files remain byte-identical.
- The STATE interpreter override and CLI/configuration precedence are checked
  without loading a model. The new identity tests pass Ruff lint and formatting.
- Full-tree Ruff checks still report the same eight lint findings and four
  formatting findings present in the pre-existing local extractor/worker work.
  They are not changed by project-name synchronization.

## Pre-screening data contract freeze — 2026-09-08

The `perturblens-data-v1` documentation in [data contracts](../data/README.md)
defines catalog/entity identity, intake/eligibility, experimental units and
controls, common manifests, logical matrix semantics, shared relations,
response-scope binding and the staged processing workflow. High-cost traceable
profiles/embeddings have an explicit retention and revalidation route.

This is a design/documentation freeze, not implemented schema validation, source
admission or production execution. Source-specific support thresholds, pipelines,
matching rules and Systema pools remain execution prerequisites.

A subsequent read-only local inventory found that the NAS project root now exists
and contains historical `data/task1`, `runs`, `_staging` and `old` content. This
supersedes the earlier root-absence observation, not its historical record. No
data was moved, deleted or promoted to current evidence by this contract update.

## Evidence boundary

Only artifacts produced or explicitly revalidated under current PerturbLens contracts may support PerturbLens manuscript claims.

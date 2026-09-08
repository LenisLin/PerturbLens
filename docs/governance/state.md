# PerturbLens Project State

Last updated: 2026-09-08

## Scientific Reframing

The human lead approved reframing the project from the Task1/Task2-centered M2M-Bench benchmark into **PerturbLens**, a response-centric study of cellular perturbation information across biological boundaries.

The active scientific architecture is now:

```text
R1 framework
R2 genetic learnability
R3 chemical learnability
R4 cross-intervention chemical/genetic conservation
R5 cross-readout transcriptomics/morphology conservation
R6 combination compositionality
```

The three shared evaluation families are population similarity, instance retrieval, and model prediction. Primary state-representation families are Gene/Pathway/FM for transcriptomics and CellProfiler/deep embeddings for morphology. Primary response views are control delta and a Systema-style perturbed reference.

See [project](../project.md), [proposal](../research/proposal.md), [result architecture](../research/result_architecture.md), and [study map](../tasks/study_map.md).

## Migration Status

### Completed in the current reframing change

- PerturbLens scientific scope and R1-R6 manuscript logic documented.
- Literature/ecosystem analysis added with current competitive risks.
- `docs/research/` introduced as a research-rationale domain.
- Shared response-construction and prediction-evaluation vocabularies introduced.
- Legacy Task1/Task2 mapped to the new Result architecture without changing their existing output semantics.

### Retained legacy execution core

Existing Task1/Task2 contracts, scripts, schemas, runbook stages, NAS paths, and historical artifacts remain valid under their original meanings.

No existing `task1_*` or `task2_*` file is automatically a PerturbLens result. Reuse requires an explicit alignment proof or a new task contract.

The repository/package/storage identifiers containing `M2M` or `m2mbench` are retained during migration for provenance and implementation compatibility. Scientific naming has changed before source/storage renaming.

## Not Yet Implemented Or Verified

The following are approved research directions but **not completed analyses**:

- R2 unseen-context and unseen-target prediction tasks;
- R3 new-compound, unseen-compound, and unseen-target prediction tasks;
- VCC2026/Cell-Eval2 prediction metric implementation in this repository;
- task-specific legal Systema reference pools across all result families;
- morphology data ingestion, CellProfiler extraction, deep image embeddings, or morphology response contracts;
- transcriptomic-morphological cross-readout analyses;
- expanded FM manuscript coverage beyond currently materialized/approved legacy surfaces;
- genetic or chemical combination task contracts and interaction nulls;
- new PerturbLens result tables, figures, or numerical claims.

Documentation presence is not evidence of execution.

## Immediate Work Queue

1. Freeze task-specific response-construction semantics and Systema reference pools.
2. Freeze the Cell-Eval2/VCC2026 version and morphology metric analogues.
3. Build a source/coverage inventory for R2, R3, R5, and R6.
4. Write executable task contracts for genetic and chemical learnability.
5. Verify which legacy Task1/Task2 outputs can lawfully feed R2-R4.
6. Select and contract morphology sources before implementing R5.
7. Select combination sources and null models before implementing R6.

## Evidence Boundary

The existing [evidence index](../tasks/evidence_index.md) remains authoritative for legacy Task1/Task2 evidence. New PerturbLens evidence entries must point to task contracts, split manifests, response-construction versions, metric versions, result tables, and validation assertions.

No benchmark performance or manuscript conclusion is certified by the reframing itself.

# PerturbLens Documentation

## Start here

1. [Project definition](project.md) — active scientific question and scope.
2. [Research proposal](research/proposal.md) — scientific rationale and full study design.
3. [Competitive landscape](research/landscape.md) — literature position and novelty risks.
4. [Result architecture](research/result_architecture.md) — R1-R6 argument flow.
5. [Project state](governance/state.md) — what is designed, implemented, and verified.
6. [Roadmap](roadmap.md) — execution order and entry conditions.

## Domain owners

| Domain | Canonical entry points |
| --- | --- |
| Research rationale | [Proposal](research/proposal.md), [landscape](research/landscape.md), [result architecture](research/result_architecture.md) |
| Tasks | [Genetic](tasks/genetic_learnability.md), [chemical](tasks/chemical_learnability.md), [cross-intervention](tasks/cross_intervention.md), [cross-readout](tasks/cross_readout.md), [combination](tasks/combination.md), [schemas](tasks/output_schemas.md), [validation](tasks/validation.md), [evidence](tasks/evidence_index.md) |
| Data | [Sources](data/sources.md), [object model](data/object_model.md), [response construction](data/response_construction.md), [preprocessing](data/preprocessing/), [representations](data/representations/) |
| Metrics | [Population similarity](metrics/population_similarity.md), [retrieval](metrics/retrieval.md), [prediction](metrics/prediction.md), [aggregation](metrics/aggregation.md) |
| Visualization | [Figure plan](visualization/figure_plan.md), [standards](visualization/standards.md) |
| Manuscript | [Outline](manuscript/outline.md), [writing standards](manuscript/writing_standards.md), [figure legends](manuscript/figure_legends.md) |
| Governance | [State](governance/state.md), [runbook](governance/runbook.md), [storage](governance/storage_policy.md), [scientific standards](governance/scientific_standards.md), [documentation policy](governance/documentation_policy.md), [collaboration](governance/collaboration.md) |

## Ownership rule

A definition has one owner. Data transformations belong in data contracts; comparison units and splits belong in task contracts; calculations belong in metric contracts; scientific motivation belongs in research; figure placement belongs in visualization/manuscript.

The repository contains only the current PerturbLens architecture. Prior project structure remains recoverable through Git history rather than active documentation.
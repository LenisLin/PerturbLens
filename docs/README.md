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
| Data | [Data contracts](data/README.md), [architecture](data/architecture.md), [workflow](data/workflow.md), [intake](data/intake.md), [sources](data/sources.md), [object model](data/object_model.md) |
| State representations | [Representation contracts](representations/README.md) |
| Response construction | [Response contracts](responses/README.md) |
| Tasks | [R2-R6 contracts](tasks/README.md), [schemas](tasks/output_schemas.md), [validation](tasks/validation.md) |
| Metrics | [Population similarity](metrics/population_similarity.md), [retrieval](metrics/retrieval.md), [prediction](metrics/prediction.md), [aggregation](metrics/aggregation.md) |
| Visualization | [Figure plan](visualization/figure_plan.md), [standards](visualization/standards.md) |
| Manuscript | [Outline](manuscript/outline.md), [writing standards](manuscript/writing_standards.md), [figure legends](manuscript/figure_legends.md) |
| Governance | [State](governance/state.md), [runbook](governance/runbook.md), [evidence](governance/evidence_index.md), [records](governance/records/README.md), [storage](governance/storage_policy.md), [scientific standards](governance/scientific_standards.md), [documentation policy](governance/documentation_policy.md), [collaboration](governance/collaboration.md) |

## Read by execution stage

1. Framework closure: [roadmap Phase 1](roadmap.md#phase-1--framework-closure),
   [data workflow](data/workflow.md), [representations](representations/README.md),
   [responses](responses/README.md), and [task validation](tasks/validation.md).
2. R2-R6: follow the [task index](tasks/README.md) and the roadmap's dependency
   order; early source preparation does not authorize production analysis.
3. Synthesis: use the [evidence index](governance/evidence_index.md),
   [figure plan](visualization/figure_plan.md), and [manuscript outline](manuscript/outline.md).

The [project state](governance/state.md) distinguishes completed preservation
and checks from pending scientific execution.

## Ownership rule

A definition has one owner. Intake, prepared data and shared schemas belong in
data; state feature construction belongs in representations; references and
response construction belong in responses; comparison units and splits belong
in tasks; metric calculations belong in metrics. Research owns scientific
motivation, governance owns execution/evidence rules, and visualization/manuscript
consume validated evidence.

The repository contains only the current PerturbLens architecture. Prior project structure remains recoverable through Git history rather than active documentation.

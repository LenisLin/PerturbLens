# PerturbLens Documentation

## Start Here

1. Read [the project definition](project.md) for the active scientific question and scope.
2. Read [the research proposal](research/proposal.md) for the full study rationale and design.
3. Read [the literature landscape](research/landscape.md) for ecological positioning and direct competitors.
4. Read [the result architecture](research/result_architecture.md) for the R1-R6 manuscript logic.
5. Read [the task/result migration map](tasks/study_map.md) before reusing legacy Task1/Task2 outputs.
6. Read [the roadmap](roadmap.md) for migration and execution order.
7. Read [project state](governance/state.md) for what is approved, implemented, and verified.

## Domain Owners

| Domain | Canonical entry points |
| --- | --- |
| Research rationale and positioning | [Research index](research/README.md), [proposal](research/proposal.md), [landscape](research/landscape.md), [result architecture](research/result_architecture.md) |
| Tasks and analysis | [Study map](tasks/study_map.md), retained [Task1](tasks/task1.md), retained [Task2](tasks/task2.md), [output schemas](tasks/output_schemas.md), [validation](tasks/validation.md), [evidence index](tasks/evidence_index.md) |
| Data | [Sources](data/sources.md), [object model](data/object_model.md), [response construction](data/response_construction.md), source preprocessing contracts |
| Representations | [Gene](data/representations/gene.md), [Pathway](data/representations/pathway.md), [FM](data/representations/fm.md); morphology representation contract is an implementation milestone before R5 production |
| Metrics | [Concordance](metrics/concordance.md), [retrieval](metrics/retrieval.md), [prediction](metrics/prediction.md), [aggregation](metrics/aggregation.md) |
| Visualization | [Standards](visualization/standards.md), [figure plan](visualization/figure_plan.md) |
| Manuscript | [Writing standards](manuscript/writing_standards.md), [outline](manuscript/outline.md), [figure legends](manuscript/figure_legends.md) |
| Governance | [Scientific standards](governance/scientific_standards.md), [documentation policy](governance/documentation_policy.md), [runbook](governance/runbook.md), [storage policy](governance/storage_policy.md), [state](governance/state.md) |
| History | [Changelog](history/CHANGELOG.md), [PerturbLens reframing decision](history/decisions/2026-09-08_perturblens_reframing.md) |

## Architecture Boundary

`docs/research/` owns scientific rationale, literature/ecosystem positioning, and manuscript-level research questions. It does **not** define executable metric formulas or lawful task units.

Executable semantics remain owned by `docs/tasks/`, `docs/data/`, and `docs/metrics/`. Existing M2M Task1/Task2 contracts remain valid for their historical outputs until a PerturbLens task contract explicitly supersedes or incorporates them.

The root still contains only this navigation page, `project.md`, and `roadmap.md`. Data and run artifacts remain outside the source checkout.

# M2M-Bench Documentation

## Start Here

1. Read [the project definition](project.md) for the current research question
   and approved scope.
2. Read [the roadmap](roadmap.md) for proposed work, dependencies, and entry
   conditions.
3. Read [project state](governance/state.md) for implementation and evidence
   status. A written contract is not proof of a completed analysis.
4. Read the relevant domain contract before changing data, methods, or figures.

## Domain Owners

| Domain | Canonical entry points |
| --- | --- |
| Tasks and analysis | [Task1](tasks/task1.md), [Task2](tasks/task2.md), [output schemas](tasks/output_schemas.md), [validation](tasks/validation.md), [evidence index](tasks/evidence_index.md) |
| Data | [Sources](data/sources.md), [object model](data/object_model.md), [LINCS preparation](data/preprocessing/lincs.md), [scPerturb preparation](data/preprocessing/scperturb.md), [Task1 snapshot](data/snapshots/task1.md) |
| Representations | [Gene](data/representations/gene.md), [Pathway](data/representations/pathway.md), [FM](data/representations/fm.md) |
| Metrics | [Concordance](metrics/concordance.md), [retrieval](metrics/retrieval.md), [aggregation](metrics/aggregation.md) |
| Visualization | [Standards](visualization/standards.md), [figure plan](visualization/figure_plan.md) |
| Manuscript | [Writing standards](manuscript/writing_standards.md), [outline](manuscript/outline.md), [figure legends](manuscript/figure_legends.md) |
| Governance | [Scientific standards](governance/scientific_standards.md), [documentation policy](governance/documentation_policy.md), [runbook](governance/runbook.md), [storage policy](governance/storage_policy.md), [collaboration](governance/collaboration.md) |
| History | [Changelog](history/CHANGELOG.md), [architecture decision](history/decisions/2026-09-06_documentation_architecture.md) |

## Boundaries

Task documents own task-specific analysis and statistical plans; there is no
separate analysis domain. Figure assignments are maintained in the figure plan,
not used to organize shared preprocessing or metrics.

The project document describes approved scope, the roadmap describes future
work, and state records observed progress. Archived documents preserve context
but are not current contracts.

Only these three Markdown files live at this root: this navigation page,
`project.md`, and `roadmap.md`. Data and run artifacts remain outside the source
checkout under the roots defined by the storage policy.

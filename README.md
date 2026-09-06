# M2M-Bench

M2M-Bench is a benchmark for transcriptome-centered perturbation-response
concordance. Its approved scope is defined in [the project document](docs/project.md).

## Core Scope

- `Task1`: modality concordance with `perturbation_type` held fixed.
- `Task2`: mechanism concordance between chemical and genetic cohorts inside one
  dataset.
- `Gene` and `Pathway` are the benchmark-wide representation spaces.
- `FM` enters the main manuscript only through the `scPerturb/K562`
  `Figure 3F` local-only panel.
- Figure 1 defines the benchmark.
- Figure 2 carries Task1 main evidence.
- Figure 3 carries Task2 main evidence.
- Task1 and Task2 stay separate in the main text.

## Start Here

- `AGENTS.md`
- `docs/README.md`
- `docs/project.md`
- `docs/roadmap.md`
- `docs/governance/state.md`
- `docs/governance/runbook.md`
- `docs/tasks/task1.md`
- `docs/tasks/task2.md`
- `docs/tasks/output_schemas.md`
- `docs/visualization/figure_plan.md`
- `docs/manuscript/outline.md`
- `docs/manuscript/figure_legends.md`

## Active Roots

The [storage policy](docs/governance/storage_policy.md) defines the NAS-backed
data, run, manuscript-analysis, and plot-export roots.

## Repo Layout

- `docs/`: project definition and roadmap, plus task, data, metric,
  visualization, manuscript, governance, and history domains
- `.agents/skills/`: repo-scoped operating workflows
- `scripts/fm_extractors/`: FM extraction utilities

## Local Checkout

The local checkout is source-only. Audited data, stage outputs, and manuscript
analysis live on NAS-backed roots.

Some Task1 preparation interfaces documented here currently exist only in the
local development working tree. See [project state](docs/governance/state.md)
for the distinction between published source, local implementation, and
validated evidence.

# Figure Plan

## Purpose

This file maps the current benchmark questions to the manuscript figures. It
is a presentation plan, not a replacement for task definitions or metric
contracts. The scientific definitions are maintained in:

- docs/project.md
- docs/tasks/task1.md
- docs/tasks/task2.md
- docs/data/sources.md
- docs/data/object_model.md
- docs/metrics/concordance.md
- docs/metrics/retrieval.md
- docs/metrics/aggregation.md

Figure numbers are manuscript organization. They do not determine where data
preprocessing, task logic, or metric definitions are maintained.

## Main Figure Roles

| Figure | Role | Evidence family |
| --- | --- | --- |
| Figure 1 | Benchmark definition, workflow, and lawful comparison scope | Overview schematic |
| Figure 2 | Task1 main evidence | Modality concordance |
| Figure 3 | Task2 main evidence | Mechanism concordance |

Task1 and Task2 remain separate in the main text. Gene and Pathway are the
benchmark-wide representation spaces. FM appears in the main manuscript only
through the scPerturb/K562 Figure 3F local-only panel.

## Figure 1

Figure 1 is the benchmark overview. It defines the two scenario questions,
shows how shared sources become task-specific lawful units, and summarizes the
four evaluation views:

- Group concordance
- directional Retrieval
- Representation comparison across Gene and Pathway
- ranked Enrichment summaries using pair_mean_enrichment

The controlling visual design is in figures/benchmark_overview.md. The draft
legend is in manuscript/figure_legends.md and is explicitly not an approved
result claim.

## Figure 2: Task1

Figure 2 carries Task1 main evidence:

- 2A: Task1 lawful-scope composition
- 2B: Task1 shared matched-unit scoreboard
- 2C: Task1 internal-to-cross degradation
- 2D: Task1 paired Gene versus Pathway comparison
- 2E: Task1 cell-line pattern ranked by pair_mean_enrichment
- 2F: Task1 perturbation_gene pattern ranked by pair_mean_enrichment

The detailed panel design, data requirements, and interpretation boundaries are
in figures/task1_results.md. Figure 2 uses n_pairs >= 3 for 2D and support_n
>= 3 for 2E and 2F. FM is not a Figure 2 panel.

## Figure 3: Task2

Figure 3 carries Task2 main evidence:

- 3A: Task2 lawful-scope composition
- 3B: Task2 performance backbone
- 3C: Task2 cell-line pattern ranked by pair_mean_enrichment
- 3D: Task2 anchor_gene pattern ranked by pair_mean_enrichment
- 3E: Task2 C2G paired Gene versus Pathway comparison
- 3F: scPerturb/K562 FM local-only absolute-performance panel

The detailed panel design, data requirements, and interpretation boundaries are
in figures/task2_results.md. Figure 3 uses C2G as the first Task2 retrieval
direction and G2C as the second direction, n_pairs >= 3 for 3E, support_n
>= 3 for 3C and 3D, and the approved scPerturb/K562 scope only for 3F.

## Shared Plot Workflow

The panel workflow is:

1. An approved task analysis produces source tables and manifests.
2. Python selects lawful rows, computes approved panel summaries, joins
   approved significance information, applies thresholds, and writes
   plot-ready tables.
3. R reads those tables, applies ordering and visual composition, and exports
   the final panels.
4. Review checks the rendered panel against the panel definition, manifest,
   denominator fields, and draft or approved legend.

The workflow does not permit R to recompute panel-defining statistics. Shared
requirements are in visualization/standards.md.

## Panel Cross-References

Each panel document must state:

- the question the panel addresses;
- the task and analysis family;
- the exact plot-ready input family;
- the lawful scope and denominator cues;
- the inclusion threshold, when applicable;
- the visual encoding and ordering rule;
- the conclusion boundary;
- the evidence and legend status.

The panel document may summarize these items but must link to the authoritative
task, data, and metric documents rather than restating their full contracts.

## Figure And Manuscript Handoff

The manuscript outline and writing requirements are in:

- docs/manuscript/outline.md
- docs/manuscript/writing_standards.md
- docs/manuscript/figure_legends.md

Figure legends describe what is shown and how it was computed at the level
needed to interpret the panel. They do not introduce a claim unsupported by
the task output or evidence record.

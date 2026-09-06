# Visualization Standards

## Purpose

This document defines the current shared requirements for assembling and
rendering M2M-Bench figures. It governs visual presentation and plot assembly;
it does not redefine Task1, Task2, data objects, metrics, or scientific claims.

The current benchmark-wide semantic sources are:

- docs/project.md
- docs/tasks/task1.md
- docs/tasks/task2.md
- docs/metrics/concordance.md
- docs/metrics/retrieval.md
- docs/metrics/aggregation.md
- docs/data/sources.md
- docs/data/object_model.md

Figure-specific design is maintained in visualization/figures/. The manuscript
expression of a figure is maintained in manuscript/figure_legends.md.

## Current Style Direction

The active Figure 1 visual direction is a layered scientific overview rather
than a rounded-card collage. Its style references have explicit priority:

1. /home/lenislin/Experiment/projects/M2M/reference/image.png controls the
   overall layered composition, side label zones, broad container geometry,
   arrow language, pastel palette, and evaluation-strip rhythm.
2. The latest local mockup is a secondary reference for current icon
   vocabulary, local element arrangement, and compact pseudo-visualization
   cues.

The intended appearance is a polished scientific schematic with broad layered
containers, balanced spacing, compact English labels, consistent heatmap
language, and clear top-to-bottom scientific storytelling. These are design
requirements, not evidence about benchmark performance.

## Semantic Presentation Rules

- Keep Task1 and Task2 visually separate in the main manuscript.
- Keep Gene and Pathway as the benchmark-wide representation comparison.
- Keep FM limited to the scPerturb/K562 Figure 3F local-only panel.
- Use anchor_gene for the Task2 unit field.
- Use perturbation_gene for row identity.
- Use query_instance_id for retrieval query rows.
- Use pair_mean_enrichment for ranked pattern summaries.
- Preserve the distinction between directionless Group analysis and directional
  Instance retrieval.
- Show C2G before G2C when both Task2 retrieval directions are presented.
- Do not imply that a visual cue is a result when the source table or legend
  does not define it as one.
- Do not add a panel, threshold, comparison, or representation because it
  improves visual balance.

## Assembly And Rendering Boundary

Python assembles plot-ready tables and owns:

- lawful pairing and comparison membership
- thresholding and panel membership
- ranking
- significance joins, when an approved analysis table supplies them
- panel-defining summaries

R renders final panels and owns:

- factor ordering
- labels
- themes
- panel composition
- vector export

R does not recompute panel-defining summaries or change benchmark semantics.
Plotting code consumes approved plot-ready tables and does not become a second
analysis implementation.

## Active Roots

The current manuscript-facing analysis and review roots are:

- Manuscript analysis:
  /mnt/NAS_21T/ProjectData/M2M/runs/manuscript_active/analysis
- Plot review export:
  /mnt/NAS_21T/ProjectData/M2M/runs/_staging/manuscript_visual_revision_current

These locations identify evidence and review artifacts. The local checkout
contains source and documentation only. Storage and provenance requirements
are defined in docs/governance/storage_policy.md and
docs/governance/runbook.md.

## Rendering Thresholds

The following thresholds are current visual inclusion rules:

- Figure 2D and Figure 3E render surfaces with n_pairs >= 3.
- Figure 2E, Figure 2F, Figure 3C, and Figure 3D render entities with
  support_n >= 3.
- Figure 3F uses the approved scPerturb/K562 scope only.

Thresholding occurs during Python plot-ready assembly. A renderer must not
silently lower, raise, or reinterpret these thresholds.

## Figure Integrity

Every rendered panel must be traceable to:

1. a panel definition in visualization/figure_plan.md or the relevant
   visualization/figures/ file;
2. an approved task, data, and metric definition;
3. a plot-ready input table and its manifest or evidence location; and
4. a manuscript legend or explicit statement that the legend remains draft.

Panel labels, axis labels, units, denominators, exclusions, and uncertainty
annotations must agree with the source table. Missing evidence is represented
as missing or unresolved; it is not replaced with a favorable default.

## Export And Review

Final panel composition should preserve readable labels, stable dimensions,
consistent scales for direct comparisons, and legible legends at the intended
output size. Review should check:

- no panel changes its defined comparison or direction;
- no labels imply a broader scope than the data;
- all displayed thresholds and denominator cues are correct;
- the FM restriction is visible wherever FM appears;
- vector output remains editable and raster references are embedded or
  provenance-traceable;
- the rendered panel corresponds to the reviewed plot-ready table.

Specific dimensions, fonts, and journal submission settings remain unresolved
until a target journal and final production format are selected. They are not
specified here.

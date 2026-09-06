# Manuscript Figure Legends

## Status

The text in this document is a migrated draft. It is not approved final
manuscript prose and must not be treated as evidence or as authorization for a
new analysis. Panel definitions and thresholds are linked to
docs/visualization/figure_plan.md and the panel documents under
docs/visualization/figures/.

## Figure 1: Draft

Figure 1. Benchmark overview of M2M-Bench. The scenarios layer defines two
benchmark questions: Task 1 evaluates modality concordance by asking whether
the same cell context under the same perturbation aligns internally and across
datasets, whereas Task 2 evaluates mechanism concordance by asking whether Drug
and CRISPR perturbation outcomes align within one dataset around a shared
anchor_gene. The data layer is organized as a shared source band, a
task-specific unit-construction field, and a shared representation band. The
source band summarizes LINCS and scPerturb as common upstream datasets. In the
unit-construction field, Task 1 funnels source-side perturbation cues into a
boxed Task 1 unit defined by cell_line, perturbation_gene, and fixed
perturbation type, whereas Task 2 funnels Drug and CRISPR cohort cues into a
centered Task 2 unit organized by shared cell_line and anchor_gene, with time
and dose retained as secondary metadata on the Drug side. The representation
band shows the common Gene and Pathway spaces used for benchmark-wide
comparison. The metrics layer is presented as an evaluation summary strip with
four views: group concordance, directional retrieval, representation
comparison across Gene and Pathway spaces, and pair_mean_enrichment-style
ranked summaries across cell line and gene-level entities. Group analysis is
quantified by PCC, cosine similarity, and bias-corrected e_distance, and
retrieval is quantified by corrected Hit@1, Hit@3, Hit@5, and MRR. Retrieval
is single-positive in Task 1 and retains separate C2G and G2C directions in
Task 2.

## Figure 2: Draft

### Panel 2A

Task1 lawful-scope composition panel showing the active Task1 slices and their
support.

### Panel 2B

Task1 shared matched-unit scoreboard showing the directly comparable Task1
slice across Gene and Pathway.

### Panel 2C

Task1 internal-to-cross degradation panel showing how matched-unit performance
changes from internal to cross evaluation.

### Panel 2D

Task1 paired Gene versus Pathway comparison on surfaces with n_pairs >= 3.

### Panel 2E

Task1 cell-line pattern panel ranked by pair_mean_enrichment on entities with
support_n >= 3.

### Panel 2F

Task1 perturbation_gene pattern panel ranked by pair_mean_enrichment on
entities with support_n >= 3.

## Figure 3: Draft

### Panel 3A

Task2 lawful-scope composition panel showing the active Task2 dataset,
cell_line, and representation surfaces.

### Panel 3B

Task2 performance backbone panel showing Task2 Group and retrieval performance
by dataset and cell_line.

### Panel 3C

Task2 cell-line pattern panel ranked by pair_mean_enrichment on entities with
support_n >= 3.

### Panel 3D

Task2 anchor_gene pattern panel ranked by pair_mean_enrichment on entities with
support_n >= 3.

### Panel 3E

Task2 C2G paired Gene versus Pathway comparison on surfaces with n_pairs >= 3.

### Panel 3F

scPerturb/K562 FM local-only absolute-performance panel shown on the native
metric scale with Gene as the baseline.

## Legend Review Requirements

Before approval, each legend must be checked against:

- the corresponding panel definition;
- the task, data, and metric contracts;
- the plot-ready table manifest and denominator fields;
- the rendered panel;
- the scope and threshold requirements; and
- the evidence location recorded by governance and task documents.

The final legend must not add result direction, effect size, biological
mechanism, or generalization that is absent from the audited evidence.

# Manuscript Outline

## Current Paper Shape

M2M-Bench is a benchmark/evaluation paper for transcriptome-centered
perturbation-response concordance. The current main-text sequence is:

1. benchmark definition and scope;
2. Task1 modality-concordance evidence;
3. Task2 mechanism-concordance evidence; and
4. discussion of evidence boundaries, limitations, and future work.

Figure 1 defines the benchmark. Figure 2 presents Task1 main evidence. Figure 3
presents Task2 main evidence. Task1 and Task2 remain separate in the main text.
FM enters the main manuscript only through the scPerturb/K562 Figure 3F
local-only panel.

This is an outline of argument responsibilities, not a draft of results. It
must not contain invented effect sizes, sample counts, citations, or final
claims.

## Argument Spine

The manuscript should connect:

research question -> task definition -> lawful data object -> approved metric
and analysis -> audited evidence -> bounded interpretation

The project-level question and current contribution boundary are defined in
docs/project.md. Future candidates remain in docs/roadmap.md and must not be
written as current evidence.

## Section Responsibilities

### Title And Abstract

Identify the benchmark and the perturbation-response concordance problem. The
abstract should state the evaluation gap, introduce the two task families at a
high level, and summarize only results supported by audited outputs. Do not
include unverified numerical or priority claims.

### Introduction

Establish the field context, identify the evaluation gap, explain why
modality- and mechanism-concordance questions matter, and motivate a benchmark
that keeps the two task families explicit. End by defining the current scope
and the evidence sequence without presenting future roadmap items as completed
work.

### Methods

Methods should introduce the data sources and object model before describing
Task1 and Task2. It should then define:

- lawful task units and matching;
- Gene and Pathway representation handling;
- the approved Group and directional retrieval analyses;
- metrics, aggregation, and chance correction;
- validation and evidence traceability; and
- the restricted scope of the FM representation.

Authoritative details belong in docs/data/, docs/tasks/, docs/metrics/, and
docs/governance/. The manuscript should cite or link those records as the
project's internal source of truth.

### Results: Benchmark Definition

Use Figure 1 to introduce the scenarios, data object construction, shared
representation context, and four readout families. The prose should explain
the benchmark question rather than treat the schematic's pseudo-visualization
cues as result evidence.

### Results: Task1

Use Figure 2 to present Task1 lawful scope, shared matched-unit evidence,
internal-to-cross comparison, Gene versus Pathway comparison, and the two
ranked pattern views. Keep internal and cross settings distinct. State
thresholds and support where the corresponding panels exclude low-support
surfaces or entities.

### Results: Task2

Use Figure 3 to present Task2 lawful scope, performance backbone, ranked
cell-line and anchor_gene patterns, and the C2G Gene versus Pathway comparison.
Keep C2G and G2C separate. Present Figure 3F only as the approved
scPerturb/K562 FM local comparison and do not generalize it to other panels or
datasets.

### Discussion

Interpret the observed evidence within the active data and task boundaries.
Separate what is observed from why it may have occurred. Discuss limitations
that affect matching, support, representation coverage, dataset or cell-line
generalization, and the separation of Task1 from Task2. Tie future work to
specific entries in docs/roadmap.md.

## Figure And Table Handoff

The current figure responsibilities are maintained in
docs/visualization/figure_plan.md and the panel documents under
docs/visualization/figures/. The current draft legends are maintained in
docs/manuscript/figure_legends.md.

Each result paragraph should be traceable to an approved plot-ready table or
other audited output through the task evidence index and governance state. A
figure reference alone is not evidence provenance.

## Writing Sequence

The current drafting order is:

1. stabilize project, task, data, and metric definitions;
2. assemble the methods argument from those definitions;
3. write results around audited Task1 and Task2 outputs;
4. write the discussion with explicit limitations and evidence boundaries; and
5. perform terminology, quantitative consistency, claim-strength, and
   figure-legend checks.

The exact journal-specific article structure remains deferred. No submission
scaffold is created by this outline.

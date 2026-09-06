# Manuscript Writing Standards

## Purpose

This document defines the current scientific writing requirements for
M2M-Bench. It governs how approved methods and evidence are expressed; it does
not create new analyses, numerical results, citations, or journal-specific
submission requirements.

The manuscript must remain consistent with:

- docs/project.md
- docs/roadmap.md
- docs/tasks/task1.md
- docs/tasks/task2.md
- docs/data/sources.md
- docs/data/object_model.md
- docs/metrics/concordance.md
- docs/metrics/retrieval.md
- docs/metrics/aggregation.md
- docs/visualization/figure_plan.md
- docs/governance/scientific_standards.md

## Evidence-Bounded Language

Write each claim so that its strength matches the study design and evidence:

- distinguish observation, interpretation, recommendation, and conclusion;
- state association rather than causation unless the design supports causal
  language;
- report effect estimates with uncertainty where available;
- report null, negative, excluded, and unresolved findings when they affect
  interpretation;
- state population, dataset, cell-line, perturbation, representation, and
  endpoint limits when they affect generalizability;
- do not use favorable secondary or exploratory findings to replace the
  prespecified primary result;
- do not describe an analysis as robust, general, or reproducible without
  naming the design or verification evidence supporting that description.

When support is missing, state Insufficient evidence and identify the next
verification step. Do not replace missing data, mechanism, or citation support
with plausible prose.

## Locked Terminology

Use the following terms consistently:

- Task1: modality concordance with perturbation_type held fixed.
- Task2: mechanism concordance between chemical and genetic cohorts within one
  dataset.
- anchor_gene: Task2 unit identity.
- perturbation_gene: perturbation-row identity.
- query_instance_id: retrieval query identifier.
- C2G: chemical-to-genetic retrieval.
- G2C: genetic-to-chemical retrieval.
- pair_mean_enrichment: ranked pattern summary used in the relevant panels.
- Gene and Pathway: benchmark-wide representation spaces.
- FM: representation shown in the scPerturb/K562 Figure 3F local-only panel.

Define abbreviations on first use in the manuscript text unless the target
journal specifies a different rule. Keep Task1 and Task2 distinct in headings,
results prose, and figure references.

## Quantitative Reporting

For every reported comparison:

- identify the comparison unit and lawful scope;
- name the metric and its direction;
- report the relevant denominator or support;
- include uncertainty or statistical support when the approved analysis
  supplies it;
- use the same value and wording across text, tables, and legends;
- avoid superiority language unless the effect size and statistical support are
  available and appropriate;
- do not infer a result from a visualization whose threshold or missingness is
  not stated.

Use exact field names in Methods and figure legends when they are part of the
analysis contract. Do not silently translate anchor_gene,
perturbation_gene, query_instance_id, or pair_mean_enrichment into competing
identities.

## Section Requirements

### Title

The title should identify the benchmark or method, its evaluation object, and
the relevant field of application without claiming an unsupported advance.
Exact title wording remains open.

### Abstract

The abstract should state the field context, the unresolved evaluation gap,
the benchmark design at high level, the two task families, and the bounded
implication of the evidence. Keep detailed preprocessing, model-family lists,
and panel-specific thresholds out of the abstract unless required for
interpretation.

### Introduction

Build from the field context to the evaluation gap, explain why the gap matters,
and introduce M2M-Bench as the response. The introduction should not imply that
Task1 and Task2 answer the same question, and should not present future
roadmap items as current findings.

### Methods

Define the data sources, object model, task units, lawful membership, primary
analysis families, metrics, aggregation, validation, and evidence roots by
linking to the authoritative project documents. Keep implementation details
that do not affect interpretation out of the scientific narrative.

### Results

Organize the results around the benchmark story:

1. benchmark definition and lawful scope;
2. Task1 modality-concordance evidence;
3. Task2 mechanism-concordance evidence; and
4. restricted or exploratory representation evidence where approved.

One paragraph should carry one main finding. Link each finding to the relevant
figure, table, metric, denominator, and uncertainty. Do not write result
direction or magnitude before the audited evidence is available.

### Discussion

Explain what the observed benchmark evidence means, why it may arise, and
where it does not generalize. State limitations tied to data coverage,
matching, representations, support, and task design when applicable. Future
work should be tied to a stated limitation or unresolved question in
docs/roadmap.md.

## Figure And Table Text

Figure legends must be self-contained enough to identify:

- the task or overview role;
- the displayed scope and direction;
- the representation and metric;
- panel-specific thresholds and support fields;
- relevant exclusions or local-only restrictions; and
- the evidence or computation boundary needed for interpretation.

The current legends are drafts in docs/manuscript/figure_legends.md. Do not
promote them to approved text merely because a panel renders.

## Tone And Editing

Use direct, neutral sentences with one substantive claim where possible.
Prefer verbs such as supports, indicates, suggests, and is associated with
when stronger language is not justified. Avoid empty intensifiers, sales-like
phrasing, and unsupported priority claims. Keep terminology, capitalization,
units, and comparison phrasing consistent across the manuscript.

## Deferred Requirements

Target-journal word limits, section names, reference style, figure dimensions,
cover-letter language, and submission checklists are intentionally deferred
until a journal and article type are selected. They must be added as a
separate approved requirement rather than inferred here.

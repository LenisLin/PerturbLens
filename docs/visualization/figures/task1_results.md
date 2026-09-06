# Figure 2: Task1 Results

## Role And Scope

Figure 2 carries the main manuscript evidence for Task1. Task1 evaluates
modality concordance while holding perturbation_type fixed. The task definition,
lawful slices, unit keys, and analysis design are maintained in
docs/tasks/task1.md. This file defines only the panel presentation and
interpretation boundaries.

Figure 2 does not authorize FM as a manuscript-facing representation. FM
remains limited to the scPerturb/K562 Figure 3F local-only panel.

## Panel Map

| Panel | Scientific role | Required visual scope |
| --- | --- | --- |
| 2A | Task1 lawful-scope composition | Active Task1 slices and their support |
| 2B | Task1 shared matched-unit scoreboard | Directly comparable matched-unit slice |
| 2C | Task1 internal-to-cross degradation | Change between internal and cross evaluation |
| 2D | Task1 representation comparison | Paired Gene versus Pathway surfaces |
| 2E | Task1 cell-line pattern | Ranked cell-line summaries |
| 2F | Task1 perturbation pattern | Ranked perturbation_gene summaries |

The current Figure 2 panel meanings are fixed. A new scientific question,
comparison, representation, or metric requires a task or metric document
decision before it is added to this figure.

## Shared Presentation Requirements

- Keep internal and cross settings visibly distinguishable.
- Preserve the distinction between Group analysis and directional Instance
  retrieval when both are represented in a panel or panel group.
- Use Gene and Pathway as the current Task1 cross-representation comparison.
- Use perturbation_gene for the row or pattern identity field.
- Use pair_mean_enrichment for ranked pattern summaries in 2E and 2F.
- Display or otherwise document the denominator and support fields needed to
  interpret each panel.
- Apply the current thresholds during Python plot-ready assembly.
- Let R control visual ordering and composition without recomputing summaries.

The underlying metric definitions and aggregation rules are in
docs/metrics/concordance.md, docs/metrics/retrieval.md, and
docs/metrics/aggregation.md.

## Panel Specifications

### 2A: Lawful-Scope Composition

Question: which active Task1 slices and representation contexts enter the
current benchmark?

Show the active Task1 internal chemical and genetic slices for LINCS and
scPerturb, together with the matched LINCS-to-scPerturb single-gene genetic
cross slice, at a level that makes support and scope inspectable.

The panel is a composition and coverage view. It must not be interpreted as a
performance comparison. It should retain the human-only scPerturb source-bundle
scope and the current no-ortholog-mapping boundary where those facts affect
the displayed scope.

Inputs and denominator fields come from the Task1 data and result contracts;
the panel document does not redefine lawful membership.

### 2B: Shared Matched-Unit Scoreboard

Question: how do directly comparable Task1 matched units summarize across the
active representation comparison?

Show the shared matched-unit slice with the approved Task1 summary measures,
including the Gene and Pathway comparison where available. Keep the matched
unit definition and scope explicit in labels or legend text.

This panel is a scoreboard of an approved slice. It must not present unmatched
internal units as if they were part of the cross comparison, and it must not
mix FM rows into the benchmark-wide Gene or Pathway comparison.

### 2C: Internal-To-Cross Degradation

Question: how does the Task1 comparison change between an internal evaluation
and the matched cross-dataset evaluation?

Place the internal and cross summaries in a directly comparable layout. Use
the same representation and metric conventions on both sides when the source
tables support that comparison. Preserve the lawful matched slice and show
denominator differences rather than treating them as invisible missingness.

The panel may show a difference or change, but its design does not prespecify
the direction or magnitude of that change.

### 2D: Paired Gene Versus Pathway Comparison

Question: how do Gene and Pathway representations compare on paired Task1
surfaces?

Render the approved paired comparison using the source table produced for
Task1 representation comparison. Only render surfaces with:

    n_pairs >= 3

The threshold applies to panel inclusion and is not a substitute for reporting
the underlying support. A surface below this threshold remains excluded from
the rendered panel; it is not reclassified as a null result.

### 2E: Cell-Line Pattern

Question: how do Task1 summaries vary across cell-line entities?

Render the approved ranked cell-line pattern using pair_mean_enrichment as the
ranking summary. Include only entities with:

    support_n >= 3

The ranking is generated during Python plot-ready assembly. R applies the
approved factor order and visual encoding. The panel must not imply that rank
alone establishes biological mechanism or generalization beyond the active
Task1 scope.

### 2F: perturbation_gene Pattern

Question: how do Task1 summaries vary across perturbation_gene entities?

Render the approved ranked perturbation pattern using pair_mean_enrichment as
the ranking summary. Include only entities with:

    support_n >= 3

Use the exact perturbation_gene identity field from the Task1 output. Do not
silently split a canonical multi-target chemical identity or merge identities
that the task contract keeps distinct.

## Plot-Ready Inputs And Rendering

Python must provide panel-ready rows with panel membership, ranking, threshold
decisions, metric values, and denominator or support fields from approved
upstream tables. R may order labels, apply themes, compose panels, and export
vectors. R must not recompute pair_mean_enrichment, threshold membership, or
other panel-defining summaries.

The current manuscript analysis and plot review roots are defined in
docs/governance/storage_policy.md and docs/governance/runbook.md.

## Interpretation Boundary

Figure 2 can show the observed Task1 concordance summaries and their lawful
internal or cross scope. It does not by itself establish a causal effect,
clinical utility, cross-species validity, or performance outside the active
datasets, cell contexts, perturbation types, representations, and support
thresholds.

The draft legend is maintained in docs/manuscript/figure_legends.md. Evidence
locations and verification status are maintained by the task and governance
documents, not inferred from the rendered image.

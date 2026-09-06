# Figure 3: Task2 Results

## Role And Scope

Figure 3 carries the main manuscript evidence for Task2. Task2 evaluates
mechanism concordance between chemical and genetic cohorts within one dataset.
The task definition, lawful membership, directions, and analysis design are
maintained in docs/tasks/task2.md. This file defines panel presentation and
interpretation boundaries.

The active Task2 datasets are LINCS and scPerturb. Core metrics are computed
within each dataset and cell_line. FM appears only in the scPerturb/K562
Figure 3F local-only panel.

## Panel Map

| Panel | Scientific role | Required visual scope |
| --- | --- | --- |
| 3A | Task2 lawful-scope composition | Lawful dataset, cell_line, and anchor_gene units |
| 3B | Task2 performance backbone | Group and retrieval summaries by dataset and cell_line |
| 3C | Task2 cell-line pattern | Ranked cell-line summaries |
| 3D | Task2 anchor-gene pattern | Ranked anchor_gene summaries |
| 3E | Task2 representation comparison | C2G paired Gene versus Pathway surfaces |
| 3F | Local FM comparison | scPerturb/K562 FM absolute performance |

The panel meanings are fixed. Adding another direction, representation, or
dataset requires a task or metric decision before it enters Figure 3.

## Shared Presentation Requirements

- Keep Task2 separate from Task1 in the main figure and manuscript narrative.
- Keep C2G as the first Task2 retrieval direction and G2C as the second.
- Use anchor_gene for the Task2 unit identity.
- Use perturbation_gene for perturbation-row identity.
- Use query_instance_id for retrieval query rows.
- Use pair_mean_enrichment for ranked pattern summaries in 3C and 3D.
- Show dataset and cell_line context wherever aggregation could otherwise be
  ambiguous.
- Apply n_pairs >= 3 and support_n >= 3 exactly where specified below.
- Keep FM out of 3A through 3E and keep 3F within its approved local scope.

The underlying metric definitions and aggregation rules are in
docs/metrics/concordance.md, docs/metrics/retrieval.md, and
docs/metrics/aggregation.md.

## Panel Specifications

### 3A: Lawful-Scope Composition

Question: which Task2 dataset, cell_line, and anchor_gene units are lawful for
the current comparison?

Show the active dataset and cell-line surfaces, with lawful units defined by
the presence of at least one chemical member and at least one genetic member.
The panel should make the available scope and support inspectable without
turning coverage into a performance claim.

Chemical membership is organized around anchor_gene membership in the chemical
target set; this panel must not substitute a different matching rule.

### 3B: Performance Backbone

Question: how do the approved Task2 Group and retrieval summaries vary by
dataset and cell_line?

Show the main Task2 performance summaries in a layout that keeps the analysis
families and retrieval directions identifiable. When retrieval is shown, place
C2G before G2C and retain direction labels. When Group and retrieval metrics
share a visual region, use distinct encodings and labels so that their
different directionality is not obscured.

The panel does not prestate which dataset, cell_line, direction, or
representation has the highest value.

### 3C: Cell-Line Pattern

Question: how do Task2 summaries vary across cell-line entities?

Render the approved ranked cell-line pattern using pair_mean_enrichment. Include
only entities with:

    support_n >= 3

The ranking and support filter are applied in Python. The visual ordering in R
must follow the approved plot-ready order. Rank is descriptive within the
active Task2 scope and does not establish mechanism or generalizability.

### 3D: anchor_gene Pattern

Question: how do Task2 summaries vary across anchor_gene entities?

Render the approved ranked anchor_gene pattern using pair_mean_enrichment.
Include only entities with:

    support_n >= 3

Use anchor_gene for this unit-level pattern and retain perturbation_gene as the
row identity in any underlying detail table. Do not collapse chemical target
sets or reinterpret membership at render time.

### 3E: C2G Paired Gene Versus Pathway Comparison

Question: how does the C2G comparison differ between Gene and Pathway
representations?

Render the approved paired C2G comparison on surfaces with:

    n_pairs >= 3

Keep C2G explicit in the panel label or legend. G2C is a separate direction
and must not be silently combined into this panel.

The threshold defines the displayed surface support. It does not imply that
excluded surfaces are negative or uninformative.

### 3F: scPerturb/K562 FM Local-Only Panel

Question: how does the approved local FM comparison appear on its native
absolute-performance scale in scPerturb/K562?

Restrict the panel to scPerturb/K562 and the approved FM families. Show Gene as
the baseline and keep the metric on its native absolute-performance scale.
This panel is local-only: it does not generalize FM coverage to LINCS, other
cell lines, other datasets, or Figure 2.

The panel must visibly identify the scPerturb/K562 scope and FM representation.
Any model-family list and availability restriction come from the approved Task2
and data representation contracts.

## Plot-Ready Inputs And Rendering

Python provides panel-ready rows with lawful membership, direction, ranking,
threshold decisions, metric values, and denominator or support fields from
approved upstream tables. R handles factor ordering, labels, themes, panel
composition, and vector export. R does not recompute panel-defining summaries
or combine C2G and G2C.

The current manuscript analysis and plot review roots are defined in
docs/governance/storage_policy.md and docs/governance/runbook.md.

## Interpretation Boundary

Figure 3 can show observed mechanism-concordance summaries within the active
dataset and cell_line units, and the restricted local FM comparison. It does
not establish causal equivalence between chemical and genetic perturbations,
model superiority outside the displayed scope, or validity beyond the active
data, representations, and support thresholds.

The draft legend is maintained in docs/manuscript/figure_legends.md. Evidence
locations and verification status are maintained by task and governance
documents, not inferred from the rendered image.

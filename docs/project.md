# M2M-Bench Project Definition

## Research Position

M2M-Bench is a benchmark/evaluation study of transcriptome-centered
perturbation-response concordance. It asks how consistently perturbation
signals align under explicitly defined comparison settings.

## Approved Questions

- [Task1](tasks/task1.md) evaluates modality concordance with
  `perturbation_type` held fixed, using internal comparisons and a matched
  LINCS/scPerturb single-gene genetic cross slice.
- [Task2](tasks/task2.md) evaluates mechanism concordance between chemical and
  genetic cohorts inside one dataset, with core metrics within each dataset
  and cell line.

These questions remain separate in analysis outputs and in the manuscript.
Task definitions, membership rules, and comparison units are owned by the task
documents, not redefined in this overview.

## Data And Representation Scope

[LINCS and scPerturb](data/sources.md) supply the current data. Benchmark objects
are delta-space perturbation responses, as defined by the
[object model](data/object_model.md) and source-specific preparation contracts.
Data sources, perturbation types, and representation spaces are distinct
concepts.

Gene and Pathway are the benchmark-wide representation spaces. FM appears in
the main manuscript only in the scPerturb/K562 Figure 3F local-only panel.
Preparing FM representations upstream for Task1 does not authorize their use
in manuscript-facing Figure 2 panels.

## Study Structure

Tasks define comparisons and their analysis requirements. Data contracts define
the input objects and transformations. Metric contracts define calculations.
Validation and the [evidence index](tasks/evidence_index.md) connect analysis
requirements to actual runs and results. Visualization and manuscript documents
consume those results without changing benchmark semantics.

The [figure plan](visualization/figure_plan.md) retains the current assignments:
Figure 1 defines the benchmark, Figure 2 presents Task1, and Figure 3 presents
Task2. Those assignments do not determine ownership of method documents.

## Contribution And Claim Boundaries

The intended contribution is a defined and auditable evaluation framework for
these concordance questions. Whether particular representations or settings
perform differently must be established by the task evidence, not assumed from
the project design.

Benchmark concordance alone does not establish causal mechanism equivalence
or clinical utility. Claims remain bounded by the evaluated datasets, cell
backgrounds, perturbations, representations, and valid comparison scope.
Missing or incomplete evidence is reported as such.

## Changes To Scope

The [roadmap](roadmap.md) holds candidate extensions. A proposed dataset,
analysis, representation scope, or task becomes active only after the relevant
scientific decision and contract revision are approved. The current
[state](governance/state.md) distinguishes approved design from implementation
and verified evidence.

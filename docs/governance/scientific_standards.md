# Scientific Standards

## Role

These requirements govern research planning, review, and reporting. They do
not choose new estimators, tests, resampling schemes, or numerical thresholds.
Those choices belong in an approved task or metric contract.

## Questions And Scope

- State the research question, target comparison, analysis unit, and population
  or data slice to which the result applies.
- Separate Task1 modality concordance from Task2 mechanism concordance.
- Separate source modality, perturbation type, and representation space.
- Distinguish the approved design from candidate extensions in the roadmap.

## Analysis Planning

1. Define primary outcomes and comparisons before the corresponding evaluation.
   Identify subsequent or exploratory choices explicitly.
2. Identify which observations are independent and which share a dataset,
   cell background, perturbation, control pool, or other dependence structure.
3. Specify lawful matching, denominators, representation availability, and
   exclusion rules before making comparative claims.
4. Record the approved uncertainty and multiplicity procedures in the task
   contract. Do not substitute an unapproved default when they are unresolved.
5. Connect robustness analyses to a specific assumption, potential bias, or
   claim boundary rather than adding analyses solely to increase result count.

## Evidence And Interpretation

- Use auditable inputs, output tables, and checks for quantitative claims.
- Report effect estimates and uncertainty when supported by the approved
  analysis; do not use a significance label as the complete result.
- Report null, negative, and uncertain findings alongside favorable findings.
- State exclusions, missing coverage, and likely interpretation consequences.
- Distinguish observation from interpretation. Concordance alone does not
  establish causal mechanism equivalence or clinical utility.
- Do not extend conclusions beyond the evaluated data, perturbations, cell
  contexts, representations, or comparison design without supporting evidence.

## Verification And Reproducibility

Apply the [task validation protocol](../tasks/validation.md), preserve the
specified audit artifacts, and identify the code and input versions used by a
run. Add checks or provenance only when a contract or concrete risk requires
them. The existence of a script, directory, or manifest alone is not evidence
that a full analysis passed its validation gates.

If evidence is insufficient, name the missing check. Documentation, software
implementation, validated runs, and manuscript readiness are separate states.

## Reporting

The [writing standards](../manuscript/writing_standards.md) apply these
requirements to manuscript sections and legends. The
[visual standards](../visualization/standards.md) apply them to the presentation
of results without changing their statistical meaning.

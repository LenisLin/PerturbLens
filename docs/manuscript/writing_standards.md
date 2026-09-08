# PerturbLens Manuscript Writing Standards

## Purpose

These standards govern how PerturbLens methods and evidence are expressed. They do not create new analyses or numerical claims.

## Evidence-bounded language

- distinguish observation, inference, hypothesis, and recommendation;
- use causal language only when the design supports it;
- report effect estimates with uncertainty where available;
- retain null, negative, excluded, and unresolved findings when relevant;
- state source, context, perturbation, representation, response view, and split limits;
- do not call an analysis robust/general/reproducible without naming the supporting design.

## Locked scientific vocabulary

- **State representation**: Gene, Pathway, FM, CellProfiler, or DeepMorphology.
- **Response view**: Delta or SystemaResidual.
- **Population similarity**: measured response geometry/distribution comparison.
- **Retrieval**: response specificity/identity in a lawful gallery.
- **Prediction**: out-of-sample learnability under a declared split.
- **Cross-intervention**: chemical/genetic boundary.
- **Cross-readout**: transcriptomics/morphology boundary.
- **Combination residual**: deviation from a declared combination null; not automatically synergy.

## Quantitative reporting

For every comparison identify:

- biological unit and split/matching/null;
- state representation and response view;
- metric and direction;
- denominator/support and exclusions;
- uncertainty/statistical support where applicable;
- baseline/reference calibration for prediction.

Do not compare raw distances across unrelated feature spaces as if they shared units.

## Results organization

Results follow R1-R6 scientific questions rather than representation/model sections:

1. framework;
2. genetic learnability;
3. chemical learnability;
4. cross-intervention conservation;
5. cross-readout conservation;
6. combination compositionality.

Representation/model sweeps generally belong in supplementary material unless they change the biological interpretation.

## Claim boundaries

Do not infer:

- absolute unpredictability from model failure;
- causal equivalence from chemical-genetic similarity;
- direct RNA-to-morphology causality from cross-readout association;
- biological superiority from a higher embedding score;
- synergy/epistasis solely from vector non-additivity.

## Figures and tables

Every figure/table statement must be traceable to a validated result table and manifest. Legends state the comparison scope, representation, response view, metric, split/matching tier/null, support, and exclusions needed for interpretation.

## Style

Use direct, neutral language. Prefer `supports`, `indicates`, or `is associated with` when causality or universality is not established. Avoid unsupported priority claims and sales-like language.
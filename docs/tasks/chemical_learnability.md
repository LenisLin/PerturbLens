# R3 Chemical Learnability Contract

## Scientific question

What chemical perturbation-response information is compound-specific, target-linked, context-dependent, or transferable to unseen compounds and unseen targets?

## Chemical identity

`perturbation_id` identifies the compound. `target_set` is separate annotation and may contain multiple targets. A multi-target compound remains one compound condition.

## Primary split families

### `chemical_inner`

Compound and context are seen; independent replicate/condition partitions are used where available.

### `chemical_unseen_context`

Held-out cell contexts have no perturbed chemical observations in training. Allowed control-state information must be declared.

### `chemical_unseen_compound_known_target`

Held-out compounds have no outcomes in training, while one or more of their annotated targets may appear through other compounds or genetic perturbations according to the model-input contract. This split measures molecule novelty separately from target novelty.

### `chemical_unseen_target`

All compounds whose relevant target membership includes the held-out target are excluded from training under the frozen target-membership rule. Multi-target compounds require explicit eligibility handling to prevent target leakage.

## Time and dose

Time and dose are explanatory covariates rather than standalone main tasks. Primary analyses ask whether they explain response magnitude, direction, retrieval specificity, or prediction performance after preserving compound/target/context structure.

Dose/time comparisons require comparable metadata and cannot treat unmatched compound-specific schedules as causal dose-response evidence.

## Response/state views

Primary transcriptomic tracks mirror R2: Gene, Pathway, and one frozen primary FM family under Delta and paired SystemaResidual analyses.

## Evaluation families

- population similarity;
- compound/target retrieval where lawful;
- prediction with pinned Cell-Eval2/VCC2026 metrics and split-specific baselines.

## Primary interpretation

R3 distinguishes whether a model learns compound identity, target-linked response regularity, context adaptation, or generalizes to biologically novel targets.

## Claim boundary

Target annotations are imperfect and condition-dependent. Failure of a target-linked prediction does not prove target inactivity or off-target pharmacology without independent evidence.
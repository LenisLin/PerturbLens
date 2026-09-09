# PerturbLens Agent Guide

Start with `docs/README.md`, `docs/project.md`, and `docs/governance/state.md`.

## Source hierarchy

When project documents or outputs disagree, use this order:

1. audited manifests, result tables, and validation assertions;
2. active contracts in `docs/data/`, `docs/representations/`, `docs/responses/`, `docs/tasks/`, and `docs/metrics/`;
3. `docs/governance/`;
4. scientific rationale in `docs/research/`;
5. manuscript and visualization plans.

A proposal is not execution evidence. A path is not proof that a run completed.

## Scientific architecture

PerturbLens separates four layers:

1. **Data** — perturbation observations and matched controls.
2. **State representation** — Gene/Pathway/FM or CellProfiler/deep morphology features.
3. **Response construction** — control Delta or Systema-style perturbation-specific response.
4. **Biological relation/evaluation** — population similarity, retrieval, and prediction under a declared split or boundary.

Do not collapse these layers into one generic “metric”.

## Main result contracts

- R2: `docs/tasks/genetic_learnability.md`
- R3: `docs/tasks/chemical_learnability.md`
- R4: `docs/tasks/cross_intervention.md`
- R5: `docs/tasks/cross_readout.md`
- R6: `docs/tasks/combination.md`

R1 is the project/framework definition and does not require a separate prediction task.

## Evidence discipline

Every non-trivial scientific statement must be traceable to a source manifest, response build, split manifest, metric/model run, result table, and validation assertion. Preserve representation, response view, split, context, target/compound identity, readout modality, denominators, and exclusions.

## Active storage

Use only the roots in `docs/governance/storage_policy.md`. The repository checkout is source-only.

## Change discipline

- Update the owning contract before changing units, splits, response semantics, metric formulas, or figure claims.
- Treat time/dose as chemical explanatory covariates unless an explicitly matched dynamic task is approved.
- Do not claim causal equivalence from chemical-genetic similarity.
- Do not claim direct molecular-to-morphological causality from cross-readout association.
- Do not call a combination residual “synergy” without a phenotype-appropriate interaction definition.
- State representation comparison is a lens on response information, not a leaderboard by default.

## Repo skills

- `.agents/skills/perturblens-grounding/SKILL.md`
- `.agents/skills/perturblens-evidence/SKILL.md`
- `.agents/skills/perturblens-execution/SKILL.md`

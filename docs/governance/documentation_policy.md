# Documentation Policy

## Active domains

The documentation root contains exactly three Markdown entry files (`README.md`, `project.md`, `roadmap.md`) and seven active domains:

- `research`
- `tasks`
- `data`
- `metrics`
- `visualization`
- `manuscript`
- `governance`

Prior architectures are not retained in the active tree; Git history provides project history.

## Source hierarchy

1. audited manifests, result tables, and validation assertions;
2. active task/data/metric contracts;
3. governance rules and state;
4. research rationale;
5. manuscript and visualization consumers.

## Ownership

- research owns motivation, novelty, and scientific argument design;
- data owns observations, metadata, state representations, and response construction;
- tasks own lawful biological comparisons, splits, model-input regimes, and task-level statistics;
- metrics own calculations;
- governance owns run/evidence/storage rules;
- visualization and manuscript consume evidence without changing semantics.

## Status discipline

Design, implementation, execution, validation, and manuscript claim status are separate. Planned analyses are never described as observed results.

## Change rule

Changes to units, split semantics, target/compound matching, control or Systema references, model inputs, metric formulas, cross-modal matching, combination nulls, or claim boundaries require an owning-contract update in the same change.
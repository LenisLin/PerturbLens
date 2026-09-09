# Documentation Policy

## Active domains

The documentation root contains exactly three Markdown entry files (`README.md`, `project.md`, `roadmap.md`) and nine active domains:

- `research`
- `tasks`
- `data`
- `representations`
- `responses`
- `metrics`
- `visualization`
- `manuscript`
- `governance`

Prior architectures are not retained in the active tree; Git history provides project history.

## Source hierarchy

1. audited manifests, result tables, and validation assertions;
2. active data/representation/response/task/metric contracts;
3. governance rules and state;
4. research rationale;
5. manuscript and visualization consumers.

## Ownership

- research owns motivation, novelty, and scientific argument design;
- data owns observations, metadata, intake, prepared assets, shared object schemas, manifests and the NAS data layout;
- representations owns state feature construction, feature QC, normalization and model-specific input requirements;
- responses owns Delta/SystemaResidual construction, reference pools and response reuse scopes;
- tasks own lawful biological comparisons, splits, model-input regimes, and task-level statistics;
- metrics own calculations;
- governance owns run/evidence/storage rules;
- visualization and manuscript consume evidence without changing semantics.

Each rule has one canonical owner. Other modules link to that rule rather than
maintaining a second normative definition. Data owns shared state/response IDs
and artifact envelopes; representations and responses own their method semantics.
Tasks own lawful comparisons and splits; metrics own their calculations.

The roadmap orders scientific dependencies and links to module contracts; phases
do not duplicate the module tree. `governance/records/` holds dated maintenance
records and evidence locators, not retired architectures or alternative contracts.
Current status belongs in `state.md`; a historical record is not current execution
authority. Document moves update all consumers without retaining duplicate bodies.

## Status discipline

Design, implementation, execution, validation, and manuscript claim status are separate. Planned analyses are never described as observed results.

## Change rule

Changes to units, split semantics, target/compound matching, control or Systema references, model inputs, metric formulas, cross-modal matching, combination nulls, or claim boundaries require an owning-contract update in the same change.

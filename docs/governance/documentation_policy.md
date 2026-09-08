# Documentation Policy

## Source Hierarchy

When docs disagree, use this order:

1. Audited manifests and stage outputs for claims about what an execution produced.
2. Active executable contracts under `docs/tasks/`, `docs/data/`, and `docs/metrics/`.
3. `docs/project.md` and `docs/governance/*.md` for approved scope, execution state, and evidence boundaries.
4. `docs/research/` for scientific rationale, literature positioning, and result architecture.
5. `docs/manuscript/` and `docs/visualization/` for presentation.

Audited outputs establish what a run actually produced. Approved executable contracts establish required behavior. A disagreement must be reported and resolved; do not rewrite a requirement to make a nonconforming output appear valid.

The [project definition](../project.md) owns active scientific scope. The [roadmap](../roadmap.md) owns future execution. Research documents justify and organize the questions but do not silently create executable task semantics.

## Ownership

- Each formal definition has one domain owner. Other documents link to it or use a compatible, non-authoritative summary.
- `docs/research/` owns scientific motivation, literature/ecosystem positioning, and main-result logic.
- Data objects, state representations, and response construction belong in data.
- Comparison units, legal generalization splits, and task-specific statistical plans belong in tasks.
- Metric calculations belong in metrics.
- Task output schemas and shared verification belong in tasks.
- Storage roots and execution stages belong in governance.
- Figure assignments belong in the figure plan; legend prose belongs in manuscript.

## Documentation Domains

The active documentation domains are:

- `research/`
- `tasks/`
- `data/`
- `metrics/`
- `visualization/`
- `manuscript/`
- `governance/`
- `history/`

Only `README.md`, `project.md`, and `roadmap.md` live directly under `docs/`.

## Status And Change Control

- Distinguish scientific approval from implementation and verified evidence.
- A proposal or result architecture is not an executable contract.
- Scope, units, denominators, response semantics, metric semantics, train/test legality, and figure claims require human-lead approval before production implementation.
- Existing M2M Task1/Task2 outputs retain their historical semantics during PerturbLens migration. Do not rename or reinterpret them in place.
- A legacy artifact may support a new PerturbLens Result only through an explicit alignment proof or a new task contract.
- Record substantive scientific/architecture changes in `docs/history/decisions/` and `docs/history/CHANGELOG.md`.
- Preserve historical run manifests and recorded source paths.

## Evidence-First Reporting

- Cite file paths, manifests, tables, or command output for observed execution facts.
- If evidence is incomplete, state the missing check directly.
- Null, negative, and uncertain outcomes are valid results and must not be filtered from the evidence chain.

## README Policy

The repository `README.md` is maintained manually as the repo entry document. `docs/README.md` is the documentation navigation and active-owner index.

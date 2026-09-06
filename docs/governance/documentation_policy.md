# Documentation Policy

## Source Hierarchy

When docs disagree, use this order:

1. Audited manifests and stage outputs
2. Active domain contracts under `docs/tasks/`, `docs/data/`, and `docs/metrics/`
3. `docs/governance/*.md`
4. `docs/manuscript/` and `docs/visualization/`

Audited outputs establish what a run actually produced. Approved contracts
establish required behavior. A disagreement must be reported and resolved; do
not rewrite a requirement to make a nonconforming output appear valid.

The [project definition](../project.md) summarizes approved scope. The
[roadmap](../roadmap.md) is not a source of active task requirements. Archived
documents preserve historical context and are not current contracts.

## Ownership

- Each formal definition has one domain owner. Other documents link to it or
  use a compatible, non-authoritative summary.
- Data objects and transformations belong in data; comparison units and
  task-specific statistical plans belong in tasks; calculations belong in
  metrics.
- Task output schemas and shared verification belong in tasks. Storage roots
  are maintained in the [storage policy](storage_policy.md).
- Figure assignments belong in the figure plan; technical designs belong in
  the corresponding figure file; legend text belongs in manuscript.
- The root contains only `README.md`, `project.md`, and `roadmap.md`.

## Documentation Rules

- Use the field owners and figure plan linked from [the index](../README.md).
- Define every field, metric, stage, and panel when it first appears.
- Remove inactive names instead of carrying multiple names for one object.

## Status And Change Control

- Distinguish draft, approved, and superseded requirements from planned,
  implemented, and verified execution states.
- A file may retain approved rules alongside explicitly identified pending
  sections. Do not present the pending sections as executable requirements.
- Record the scope and decision basis of substantive changes. Dates describe
  actual decisions or checks, not inferred completion dates.
- Scope, units, denominators, metric semantics, and figure claims require
  human-lead approval before implementation changes. Update the controlling
  contract as part of that approved change.
- Update consumers when moving a contract. Markdown paths, headings, and lists
  read by code are interfaces and require corresponding checks.
- Retire an old document only after its active content and consumers have
  successors. Record important reasons in history without duplicating Git's
  line-by-line history.
- Preserve historical run manifests and their recorded source paths.

## Evidence-First Reporting

- Cite file paths, manifests, tables, or command output.
- If evidence is incomplete, state the missing check directly.

## README Policy

The repository `README.md` is maintained manually as the repo entry document.
`docs/README.md` is the documentation navigation and active-contract index.

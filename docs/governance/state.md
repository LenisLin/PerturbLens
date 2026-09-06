# M2M-Bench Project State

Last updated: 2026-09-06

## Role And Approved Scope

This page records current work and unresolved requirements. Approved scope is
defined by [project](../project.md), [Task1](../tasks/task1.md), and
[Task2](../tasks/task2.md). Research extensions belong in the
[roadmap](../roadmap.md).

## Documentation And Implementation Status

- The human lead approved the domain-based documentation architecture and
  publication of the migration. See the
  [decision](../history/decisions/2026-09-06_documentation_architecture.md) and
  [changelog](../history/CHANGELOG.md) for its scope and checks.
- Existing Task1 source preparation, snapshot, and FM contracts are retained.
  Their presence does not certify that a final snapshot or downstream analysis
  has passed validation.
- The local working tree contains Task1 preparation/merge scripts and their
  tests that are not part of the published baseline. This documentation release
  does not publish that unrelated implementation work. Runtime contracts may
  therefore describe local interfaces not yet available in the GitHub checkout.
- The `S0` to `S7` mapping in the [runbook](runbook.md) is an execution
  crosswalk, not a statement that those stages have completed.
- Consult the [evidence index](../tasks/evidence_index.md) for specific checked
  artifacts and the limits of those checks. The migration itself does not
  establish benchmark performance or manuscript readiness.

## Unresolved Work

| Item | Controlling owner | Current boundary |
| --- | --- | --- |
| Exhaustive source audit-column inventories and richer artifact audits | [Task1 snapshot](../data/snapshots/task1.md) and source preparation documents | Core structure and minimum extraction mapping are retained; exhaustive detail is not frozen |
| Additional model-specific QC sidecars | [FM representation](../data/representations/fm.md) | Instance keys, pairing handoff, minimum files, and existing acceptance gate remain defined; broader sidecars are not approved by this migration |
| Task-specific statistical procedures and remaining numerical edge rules | [Task1](../tasks/task1.md), [Task2](../tasks/task2.md), and metric documents | Record missing definitions before implementation; do not fill them with unapproved defaults |
| Task1 group-table key sufficiency | [Output schemas](../tasks/output_schemas.md) | The inherited `task1_group_concordance_long.csv` key omits `cell_line` although the task unit includes it; assess uniqueness for multi-cell-line outputs and approve any schema revision separately |
| Figure 2 panel-ready interfaces and downstream exports | [Task1 results design](../visualization/figures/task1_results.md) | Detailed 2A twin-panel csv/json handoff and downstream export preparation remain unresolved |
| Panel-level R scripts | [Figure plan](../visualization/figure_plan.md) | Figure roles and current thresholds are retained; the migration does not certify rendering implementation |

## Storage And Evidence

The [storage policy](storage_policy.md) owns the canonical data and run roots.
The checkout remains source-only. Do not infer stage completion from a path
listed in that policy, or use documentation updates as substitutes for audited
run evidence.

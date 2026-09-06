# Task Evidence Index

This is a thin locator for task and project-synthesis evidence. No run is
certified here: this index has not audited NAS-backed artifacts, and it must not
be read as a completion or audit result. Current status is maintained in
`docs/governance/state.md` from concrete manifests and assertions.

## Canonical locators

- Storage roots, retention, and repository/source-only boundaries:
  `docs/governance/storage_policy.md`
- Stage names, execution order, and stage-output locations:
  `docs/governance/runbook.md`
- Task semantics: `docs/tasks/task1.md` and `docs/tasks/task2.md`
- Result-table fields and project-synthesis interfaces:
  `docs/tasks/output_schemas.md`
- Validation gates: `docs/tasks/validation.md`
- Metric meaning and calculation boundaries: `docs/metrics/`
- Figure and manuscript placement:
  `docs/visualization/figure_plan.md` and
  `docs/manuscript/figure_legends.md`

The runbook is the only stage crosswalk. The storage policy is the only active
root registry. This index intentionally does not duplicate either one.

## Required evidence entry

Every evidence item registered for a task, stage, or synthesis claim should
provide, at minimum:

- `task` and stage identifier;
- `run_id` and artifact path relative to the applicable active root;
- source or snapshot manifest path used as input;
- stage `run_manifest.json`, table `manifest.json`, and
  `audit_assertions.json` paths when applicable;
- contract and schema versions used to produce the artifact;
- result level, primary-key fields, representation, and direction where
  applicable;
- denominator, coverage, valid-query, and exclusion fields required by the
  owning schema;
- validation status with a pointer to the concrete assertion or table rows;
- downstream figure or manuscript location, if the artifact is used there.

Exact run IDs, artifact paths, and verification outcomes are evidence facts.
They must be read from manifests or audit records, not inferred or populated
from this template.

## Traceability boundary

The minimum traceability chain is:

```text
source or snapshot manifest
  -> stage run manifest
  -> table manifest and output table
  -> audit assertions
  -> figure or manuscript location
```

An evidence pointer supports locating an artifact; it does not establish a
result, an audit pass, or a scientific conclusion. A claim is reportable only
when the corresponding artifact, schema, denominator fields, and validation
assertions are available and consistent. Missing evidence must be recorded as
missing rather than replaced with an inferred value.

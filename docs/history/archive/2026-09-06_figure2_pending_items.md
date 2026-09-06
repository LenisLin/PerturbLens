# Archived: Figure 2 Pending Items

Archived on 2026-09-06. This is the pre-migration pending registry, not an
active task list. Current unresolved work is indexed in
[state](../../governance/state.md). Archiving this record does not approve or
complete any pending item.

This registry records items that remain intentionally unresolved in the current
Figure 2 Task1 data preparation freeze. It does not introduce new design work.

## Pending Registry

- `task1_scope_merge.py`: source-local instance alignment, canonical membership
  truth, minimal unit summaries, exact representation coverage by surface,
  block-sliced representation export, manifest top-level structure, and the
  minimal `representation_registry.csv` directory semantics are now frozen, and
  active human datasets now have a frozen minimal extraction mapping, but
  exhaustive source-specific audit-column inventories and richer per-artifact
  audit payloads are not yet frozen
- source-local `LINCS` / `scPerturb` registries: exhaustive source-specific
  extension columns remain narrower than a full field-level freeze; the
  harmonized core plus the implementation-required minimum extraction mapping
  are frozen, but exhaustive full field-level inventories are not yet frozen
- `task1_scperturb_fm_prep.py`: the FM instance-key model, raw-cell worklist
  schema, pairing handoff shape, and per-model minimum file set are now frozen,
  but broader model-specific QC sidecars remain outside the current freeze
- `2A` twin-panel interface: panel-specific `csv/json` fields and R handoff are
  not yet frozen
- downstream `group/retrieval/metrics/export`: not yet discussed in
  freeze-ready detail
- panel-level R scripts: not yet specified in Figure 2 phase docs

## Do Not Promote Yet

These items are intentionally pending and should not be silently filled by
implementers.

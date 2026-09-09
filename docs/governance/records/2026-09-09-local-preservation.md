# Local Preservation — 2026-09-09

## Verified relocation

Preservation build: `relocate_inputs_20260909`. This is a file-level relocation,
not a new scientific analysis or validated source/prep/state build.

| Asset | Files | Destination under `data/` |
| --- | --- | --- |
| LINCS expression/signature levels and metadata | 17 | `sources/lincs/local_snapshot_20260909/` |
| Human scPerturb source H5ADs | 41 | `sources/scperturb/local_snapshot_20260909/transcriptomics/<dataset>/` |
| Historical cleaned human expression and obs tables | 58 across 29 datasets | `prepared/scperturb/<dataset>/legacy_cleaned_20260909/` |
| Legacy K562 state exports, inputs, row/feature metadata and configurations | 53 | `sources/legacy-k562/local_snapshot_20260909/` |
| Historical run provenance and three copied builder scripts | 317 | `sources/legacy-execution-provenance/local_snapshot_20260909/` |

Total preserved payload: 222,679,964,078 bytes, approximately 207.39 GiB.
483 files were moved by same-filesystem rename; three historical source scripts
were copied without removing their originals. Entire directories were not moved.
Source-native file contents, controls and existing metadata were not filtered or
recomputed. CPG0016 files preserved in the earlier copy remain unchanged.

## Evidence and checks

The full evidence root is:

```text
/mnt/NAS_21T/ProjectData/PerturbLens/data/intake/local-preservation/local_snapshot_20260909/relocate_inputs_20260909/
```

- `selection.json` and `decision.json`: selected paths and preservation decision.
- `relocation_inventory.parquet`: old/new locations, SHA256, device/inode, size,
  modification time, role and operation for every retained file.
- `relocation_journal.jsonl`: completed file operations.
- `destination_readability.parquet`: 110 H5AD/GCTX/NPY format/shape inspections;
  H5AD observation and available embedding axes were checked, including
  dataframe-encoded `obsm` entries. This is not a full numerical/QC validation.
- `updated_symlinks.json`: ten `_staging/` links retargeted to preserved files.
- `validation_assertions.json`, `completion.json`, `finalization_complete.json`:
  operation and preservation checks; scientific admission remains separate.
- `file_inventory.parquet`, `metadata_profile/columns.parquet`,
  `coverage_summary.parquet`, `schema_mapping.yaml`, `task_eligibility.parquet`,
  `intake_report.md`, `intake_manifest.json`: intake evidence and unresolved uses.

SHA256 was computed before each move. Same device/inode, size and modification
time were verified after rename, without claiming a second full-file hash read.
The three copies were checked by matching source/destination SHA256. A new
catalog snapshot at `data/catalog/snapshots/relocate_inputs_20260909/` registers
33 preservation bundles and the intake artifact, retaining prior catalog entries.

## Reuse boundaries

Imported preparations and embeddings remain `materialized`, not scientifically
validated. Exact upstream normalization, model/checkpoint, fit scope, canonical
metadata, independent support and lawful task inputs must be audited before use.
The UCE Drug embedded H5AD contains 30,813 rows, while the top-level aligned export
contains 30,829 rows; preserve their different row indices rather than assuming
positional equivalence. Historical Delta outputs are not reclassified as states.

Historical manifests preserve their original paths as provenance. Use the
relocation inventory to resolve them; do not overwrite historical records to
suggest they originally ran from the new roots. Active source documentation now
points to preserved locations. Other projects' references are not certified by
this project-local update.

## Cleanup status

No old result/cache/source file was deleted by the preservation build itself.
The user authorized cleanup following relocation, but the execution permission
review rejected the assistant's initial cleanup preflight command. A separate
file-only deletion command was subsequently supplied for the user to run with
sudo. That command did not remove directories or write a deletion journal.

`excluded_inventory.parquet` is a disposition inventory, not an unconditional
deletion list. Mouse and protein-readout data remain in `OSMOSIS/raw/`; hidden
`.git`, `.agents` and `.codex` directories are outside scientific cleanup scope.
The approved file selection was narrower than deletion of these entire roots.

The read-only `cleanup_preview.json` in the evidence root enumerates 1,225
then-present deletion candidates (542,816,891,993 bytes, approximately 505.54 GiB):
229 old-result/cache files, 992 run/cache files and four temporary download files.
It separately retains 27 mouse/protein source or metadata files. The two
scFoundation working-directory exports match their preserved top-level exports
by SHA256; complete counterparts of the four temporary downloads are readable.
No accessible process had selected files open, but other-user file-descriptor
visibility is incomplete; no claim of exhaustive host-wide non-use is made.

### Subsequent verification and empty-directory cleanup

Read-only inspection on 2026-09-09 found all 1,225 listed candidates absent and
all 27 retained files present with their recorded sizes. It found no files in
the historical `old/` and `runs/` trees. This establishes filesystem state, not
the deleting process's identity, exact execution time or a full deletion journal.
The historical preview and preservation manifests are not rewritten as deletion
execution evidence.

With explicit user approval, the assistant then used an empty-directory-only
deletion operation within `old/`, `runs/` and `OSMOSIS/raw/`, excluding `.git`,
`.agents` and `.codex` and their descendants. Post-operation inspection confirmed
that `old/` and `runs/` no longer exist and the 27 retained files still have their
recorded sizes. No data files were removed by that empty-directory operation.
`OSMOSIS/raw/` retains its populated scPerturb directories and the hidden
administrative directories. The allowed future run root remains defined by the
[storage policy](../storage_policy.md); removing an empty historical tree does
not retire that root.

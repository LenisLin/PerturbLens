# Source Intake Workflow

Version: `perturblens-data-v1`. Intake answers what a source contains, not how well
its responses perform. It ends at eligibility and a recorded decision.

## Discovery and inspection boundary

1. Register a candidate source/release/dataset and its provider, accession,
   custodian, access terms and candidate locations.
2. Inspect metadata, directory/file listings and bounded headers or documented
   samples sufficient to establish structure, units and coverage.
3. Record actual accessible evidence, inspection limits and unresolved questions.
4. Evaluate [eligibility](eligibility.md) per task/split, then record
   `include`, `defer`, or `exclude` with decision authority and reasons.
5. Localize/register source payloads only after inclusion and any required access
   or transfer authorization.

Metadata retrieval or small header inspection is allowed when authorized; intake
is not permission for bulk downloads, migration, full CellProfiler/FM extraction,
normalization, response construction or task scoring. Do not infer missing
targets, time or dose, or select sources by downstream outcomes. Imported
profiles/embeddings can be inventoried without recomputation.

## Intake bundle

Use `data/intake/<source_id>/<release>/<intake_id>/`. The common manifest has
`artifact_type=intake`, `fit_scope=null`, and parameters recording inspection
method, inspected files/rows, sampling limits, catalog version and task-contract
versions. Required outputs are:

| File | Required schema/content |
| --- | --- |
| `file_inventory.parquet` | One row per discovered file: `file_id`, `location`, `source_id`, `dataset_id?`, `role`, `format`, `size_bytes?`, `availability`, `inspection_status`, `source_version?`, `sha256?`, `inspection_note?` |
| `metadata_profile/columns.parquet` | `dataset_id`, `table_name`, `column_name`, `source_dtype`, `n_inspected`, `n_missing`, `n_distinct?`, `inspection_scope`, `units_raw?` |
| `schema_mapping.yaml` | Source-to-canonical field mappings and explicit unresolved fields |
| `coverage_summary.parquet` | Counts and denominator/sampling evidence per declared stratum |
| `task_eligibility.parquet` | One row per dataset/task/split/rule assessment |
| `intake_report.md` | Evidence, limitations, proposed uses, blocked uses and decision |
| `validation_assertions.json` | Checks of inventory, mapping, denominators and decision consistency |

`availability` is `available`, `inaccessible`, or `unverified`;
`inspection_status` is `listed`, `header_checked`, `metadata_checked`, or
`uninspected`. File `role` distinguishes expression, image, metadata, profile,
embedding, mapping, model, report and other. Metadata-only discovery does not
require reading every large payload for a checksum; missing integrity evidence
blocks payload promotion, not candidate discovery.

## Mapping specification

`schema_mapping.yaml` requires `schema_version`, `mapping_id`, `source_id`,
`release`, `dataset_id`, `source_tables`, `id_rules`, `fields`, `entity_mappings`,
`unresolved_fields`. Each field mapping records source table/column, canonical
table/column, source and destination types, transformation rule, units,
missing tokens and evidence. The mapping is a declarative specification, not
arbitrary executable code. A mapping may be unresolved; no inferred substitution.

```yaml
schema_version: perturblens-data-v1
mapping_id: example_mapping_v1
source_id: example_source
release: v1
dataset_id: example_dataset
source_tables:
  - path: metadata.csv
id_rules:
  observation_id: source_release_dataset_plus_source_cell_id
fields:
  - source_table: metadata.csv
    source_column: dose_uM
    target_table: conditions
    target_column: dose_molar
    source_type: float64
    target_type: float64
    transform: multiply_by_1e-6
    source_unit: uM
    target_unit: mol/L
    missing_tokens: [""]
    evidence: source_data_dictionary
entity_mappings: []
unresolved_fields: [replicate_group_id]
```

This is an illustrative fragment of a mapping, not a complete accepted source.

## Coverage summary

Long-form primary key: `(dataset_id, stratum_id, measure, unit)`.
Fields: `stratum_definition` (JSON string), `measure`, `unit`, `n_total?`,
`n_known?`, `n_missing?`, `value?`, `coverage_scope`, `evidence_path`,
`inspection_method`. Counts are int64; `value` is float64 for ranges/fractions.
`coverage_scope` is `full_metadata`, `provider_reported`, or `sampled`.
Sample counts must never be presented as total-source counts.

Report datasets, intervention modes, compounds, mapped/unmapped targets,
contexts, cells/wells/signatures, biological/technical/unresolved replicates,
controls, time/dose values and missingness, combinations and constituent singles,
channels, paired modalities, image availability and precomputed representation
availability. Preserve context/intervention/time/dose strata; a source-wide count
does not establish support within a task unit. Include annotation confidence and
source/assay matching coverage when relevant.

## Decision record and re-entry

The report records `decision_id`, `decision`, `decided_at`, `decided_by`,
`decision_basis`, included dataset/task scope, deferred/excluded scope and reason
codes, required access/localization actions, and unresolved blockers. These fields
also occur in intake manifest parameters. An inclusion decision does not convert
`partial` or `blocked` task rows into eligible rows. A new source release or new
mapping/support evidence creates a new intake ID linked to the prior assessment.

## Known candidate handoffs

LINCS and scPerturb locations are recorded in [sources](sources.md). CPG0016
compound/ORF/CRISPR profile paths on the reported server 73 are user-provided
discovery leads, not verified inventories, releases or image locations. Identify
the host/access method, custodian, metadata, source release, image availability
and pipeline provenance before localization. Experiment reports describe prior
work; they are not automatic PerturbLens validation or production results.

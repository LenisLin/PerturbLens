# Data Storage Architecture

Version: `perturblens-data-v1`. The [storage policy](../governance/storage_policy.md)
owns the active root `/mnt/NAS_21T/ProjectData/PerturbLens`. The layout below is
normative for new builds, not a description of the current disk contents.

## Layout

```text
data/
  catalog/
    catalog_manifest.json
    source_registry.parquet
    dataset_registry.parquet
    artifact_registry.parquet
    entities/
      cell_contexts.parquet
      perturbations.parquet
      compounds.parquet
      targets.parquet
      perturbation_target_edges.parquet
      entity_aliases.parquet
    snapshots/<catalog_build_id>/
  intake/<source_id>/<release>/<intake_id>/
    intake_manifest.json
    file_inventory.parquet
    metadata_profile/
    schema_mapping.yaml
    coverage_summary.parquet
    task_eligibility.parquet
    intake_report.md
  sources/<source_id>/<release>/
    source_manifest.json
    files.parquet
    metadata/
      observations.parquet
      experimental_units.parquet
      conditions.parquet
      perturbations.parquet
      controls.parquet
    transcriptomics/<dataset_id>/
    morphology/
      images/
      image_index.parquet
  prepared/<source_id>/<dataset_id>/<prep_id>/
    prep_manifest.json
    metadata/
    matrices/<matrix_id>/
    qc/
  states/<readout>/<source_id>/<dataset_id>/<representation_id>/<build_id>/
    state_manifest.json
    matrix_manifest.json
    index.parquet
    features.parquet
    values/
  relations/<relation_build_id>/
    relation_manifest.json
    target_membership.parquet
    cross_intervention_links.parquet
    cross_readout_links.parquet
    combination_membership.parquet
    combination_single_links.parquet
  responses/<response_build_id>/
    response_manifest.json
    response_index.parquet
    reference_registry.parquet
    reference_membership.parquet
    matrix_manifest.json
    features.parquet
    values/
  splits/<task_name>/<split_family>/<split_id>/
    split_manifest.json
    membership.parquet
    excluded_membership.parquet
runs/<run_id>/<run_family>/
  run_manifest.json
  input_manifest.json
  response_manifest.json
  split_manifest.json
  metric_manifest.json
  model_manifest.json
  logs/
  outputs/
  validation_assertions.json
artifacts/<run_id>/
  plot_ready/
  figures/
  exports/
manuscript/<manuscript_build_id>/
```

`readout` is `transcriptomics` or `morphology`. `task_name` uses the canonical
task IDs in [eligibility](eligibility.md). Representation path labels are safe
slugs such as `fm-scgpt`; manifests retain the scientific name `FM:scgpt`.
Source/dataset identifiers and releases must be registered before localization.
Dataset IDs are globally unique, including when a source has several releases.

Only applicable relation tables and modality payloads are materialized. Their
presence/absence and reason are declared in the manifest; absence never means
zero eligible pairs. Every materialized build also has
`validation_assertions.json`. Run split/model manifests are conditional on use;
all other run requirements remain as specified in the runbook.

## Layer boundaries

| Layer | Allowed contents | Boundary |
| --- | --- | --- |
| Catalog | Entity identity, source/dataset discovery and artifact registration | No expression or image payloads |
| Intake | Metadata inspection, file inventory, coverage, mapping and decisions | No formal normalization, state extraction or response scoring |
| Sources | Immutable source files or explicit external references; source-faithful metadata projections | Preserve original values and provenance |
| Prepared | Canonical metadata, QC, expression/image preparation and normalization | No task reference pool or split silently chosen here |
| States | Reusable representations at a declared sampling/aggregation level | No control subtraction disguised as a state |
| Relations | Evidence-bearing links and compatibility decisions | Task rules still determine lawful use |
| Responses | Responses and exact reference membership | Scope can depend on task and split |
| Splits/runs | Frozen memberships, fitting, evaluation and validation | Not source data |

Source metadata projections use the common schema but preserve source labels and
unresolved mappings. They do not alter source matrices. Harmonized/QC-filtered
tables live in prepared builds with links to the source rows.

`sources/.../files.parquet` has primary key `file_id` and fields `source_id`,
`release`, `dataset_id?`, `source_relative_path`, `location`, `role`, `format`,
`size_bytes`, `sha256`, `storage_mode`, `availability`, `checked_at`,
`custodian?` and `source_processing_description?`. Sizes are int64; `checked_at`
is UTC. Required file integrity is established before source validation.
Source metadata tables resolve observations to these IDs rather than assuming
that one filename is one biological sample. Original metadata files are also
listed as payloads, separate from canonical projections.

## Physical formats

Parquet is the canonical table format; JSON is used for manifests and YAML for
intake field mappings. Matrix formats follow [matrix semantics](matrix_semantics.md),
not one mandatory binary format. CSV may be retained as a source-native file or
export, but is not the canonical registry. Images retain their source-native
encoding, channel layout and bit depth. No lossy transcoding for convenience.

## Retention and localization

Preserve source expression profiles and images, both treated and controls, their
metadata, provenance and processing history. FASTQ acquisition is not required by
the expression-profile scope. LINCS Level 5 is a source-derived signature, not raw
expression counts. Image-derived profiles do not replace the image preservation
base; an image-unavailable source may receive narrower, explicit profile-only
eligibility without being called a complete imaging source.

Retain high-cost CellProfiler profiles and FM/deep embeddings when their input
identity, row/feature mapping, model/pipeline, normalization, sampling level and
fit scope can be audited. Imported precomputed profiles enter as immutable source
assets, then become state builds by validated reference or transformation, without
duplicating bytes unnecessarily. A legacy Delta remains a response candidate,
not an embedding/state candidate.

`storage_mode` is `localized` or `external_reference` for each file. External
records include resolvable location, custodian, access requirements without
credentials, availability check and preservation responsibility. Project builds
may reference versioned OSMOSIS inputs. A remote path alone does not establish
availability, authorization or an immutable version. Record file identity before
promoting an external reference to a validated source.

Use one registered physical payload where reuse is valid. Build lineage may
reference the payload; do not silently hard-link mutable working files or copy
source datasets into each model run. Changes in values or interpretation require
a new build. `latest` may be a convenience pointer, never scientific provenance.

Old outputs, duplicate shards and temporary caches are cleanup candidates, not
automatic deletion targets. Before an authorized cleanup, list exact paths,
retained replacements, dependencies, unique assets and unresolved provenance.
Confirm retained assets are readable and references resolve. This contract does
not authorize deletion or relocation, including of hidden administrative folders.

## Catalog publication

The top-level catalog tables are a current discovery view. Each publication also
preserves an immutable snapshot under `snapshots/<catalog_build_id>/` with its
manifest and validation. Consumers pin a snapshot/artifact ID, never a mutable
catalog path alone. Publish the new current view only after the snapshot passes
its checks. Historical IDs and snapshots are not rewritten or recycled.

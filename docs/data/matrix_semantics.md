# Logical Matrix And Image Contract

Version: `perturblens-data-v1`. Freeze logical identity and semantics, not one
physical format. Every prepared/state/response matrix has a matrix manifest.

## Matrix descriptor

`matrix_manifest.json` contains:

| Field | Type | Rule |
| --- | --- | --- |
| `matrix_id`, `artifact_id`, `schema_version` | string | Matrix identity and containing artifact |
| `storage_format` | enum | `npy`, `zarr`, `arrow_ipc`, `parquet`, `h5ad`, `gctx`, `mtx` |
| `values_path`, `dataset_key` | string, string? | Payload path and layer/dataset, e.g. H5AD `X` or `layers/counts` |
| `dtype`, `shape` | string, object | Value type and nonnegative `n_rows`, `n_features` |
| `row_level` | enum | `observation`, `experimental_unit`, `condition`, `response` |
| `row_index`, `feature_index` | string | Versioned index paths |
| `sparse_format` | string or null | CSR/CSC/COO when sparse |
| `partitioning` | object or null | Shards/chunks, offsets, compression, axis order and keys |
| `matrix_semantics` | object | Value/normalization/transform/unit/zero/gene/feature semantics below |
| `aggregation` | object or null | Input membership, statistic, weighting and aggregation level |
| `missing_value_policy` | object | Missingness representation, non-finite handling and exclusions |

`partitioning` references a shard inventory with `shard_id`, `path`,
`row_start`, `n_rows`, `n_features`, `sha256`, `size_bytes`; Zarr records chunk
shape, compressor, codec/library versions and its file inventory. Shards cannot
overlap row positions or omit rows silently. The logical row axis is rows first,
features second regardless of source-native storage orientation.

## Row and feature indices

The row-index primary key is `row_id`; `(shard_id, row_offset)` is unique for
sharded storage and `row_position` is unique across the matrix. Required columns:
`row_id`, `row_position`, `condition_id`, `observation_id?`,
`experimental_unit_id?`, `response_id?`, `shard_id?`, `row_offset?`,
`n_observations`, `membership_path?`. The non-null biological ID must agree with
`row_level`. Aggregated rows require exact constituent membership and weights.
`n_observations` may be null only for a source-aggregated signature whose provider
does not report its contributing count; that limitation is recorded, not set to
one independent replicate. Source signatures may reference upstream aggregation
documentation instead of enumerated constituent cells when these are unavailable.
In source-native matrices, an index projection may be generated without changing
the payload. `index.parquet` is the standard state index;
`response_index.parquet` extends it with the response keys.

`features.parquet` has primary key `feature_id` and unique `feature_position`;
also retain `feature_name`, `feature_namespace`, `feature_version`,
`feature_family?`, `source_feature_id?`, `mapping_rule_id?`.
Latent coordinates have explicit positional IDs without invented gene semantics.
Duplicate gene mappings use the approved Gene rule and retain the mapping table.
Row count, feature count and order must match each payload and all partitions.

## Value semantics

Every `matrix_semantics` object requires:

- `value_type`: `counts`, `normalized_expression`, `log1p_normalized_expression`,
  `source_level5_signature`, `morphology_measurement`, `normalized_morphology`,
  `embedding`, `pathway_score`, `delta`, or `systema_residual`;
- `normalization`: ordered methods, parameters and fitted-statistic artifact IDs,
  or an explicit no-normalization/source-unknown declaration;
- `transform`: ordered transforms including logarithm base and pseudocount, or
  explicit identity;
- `unit`: source unit, dimensionless status or per-feature unit index;
- `zero_semantics`: observed zero, implicit sparse zero, centered value, missing
  placeholder or other documented meaning;
- `gene_identifier`: namespace/version/mapping when applicable, otherwise null;
- `feature_selection`: rule, retained/excluded features and fit scope.

Do not infer counts from the extension `.h5ad`, treat missing genes as biological
zero, or feed Level 5 signatures into an FM expecting counts without an approved
input contract. Preserve counts and transformed layers separately when both exist.
Imported normalized profiles record their source normalization and fitting scope;
they are not silently normalized again. Unknown source processing limits reuse.

Delta/residual matrices belong to response artifacts, not state embeddings.
Source-native Level 5 effects are retained as source signature surfaces and may
instantiate Delta only through the documented source-native reference exception.
Pathway state scores and scores projected from responses retain their different
input lineage even if the feature names agree.

## Physical format selection

| Payload | Preferred storage |
| --- | --- |
| Small/medium dense matrix | NPY with explicit row/feature indices |
| Large embeddings | Chunked Zarr or Arrow IPC shards; NPY shards acceptable with declared access rationale |
| CellProfiler wide profiles | Partitioned Parquet with explicit feature columns/order, separate metadata columns |
| scRNA expression | H5AD or Zarr, preserving sparse structure and layers |
| LINCS input | Source-native GCTX and metadata |
| Images | Source-native encoding and acquisition structure |

Choose partitions by dataset/plate or bounded row chunks according to access and
scale; record the choice. Do not force large matrix conversion merely to unify
extensions. Dtype downcasting, compression or image conversions must preserve
required information and be documented; lossy image conversion is not the
preservation copy. Validate each shard before registering a complete build.

## Images and morphology sampling levels

`image_index.parquet` has primary key `image_id`. Required fields are `file_id`,
`source_id`, `dataset_id`, `condition_id`, `experimental_unit_id`, `source_trace`,
`channel_layout`, `availability`; nullable source-dependent fields are `plate_id`,
`well_id`, `field_id`, `channel`, `z_plane`, `timepoint`, `pixel_size`,
`pixel_size_unit`, `width`, `height`, `bit_depth`, `acquisition_id`, `dataset_key`.
`channel_layout` is `single_channel`, `multichannel`, or `unknown`. A multichannel
file needs its channel mapping; no duplicate physical copies per channel.
Link image IDs to observation IDs explicitly in the observation table.

CellProfiler preserves pipeline/version, segmentation objects, channels, feature
definitions and cell-to-image/well membership. DeepMorphology preserves encoder
checkpoint, channels, crop/resize/intensity preprocessing, embedding layer and
pooling. Well-level aggregates are separate builds from cell/image features with
their own row level and membership. A large number of fields or cells does not
create independent wells or biological replicates.

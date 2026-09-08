# PerturbLens Data Object Model

Version: `perturblens-data-v1`. See the [data index](README.md) for contract owners.

## Core objects

| Object | Meaning |
| --- | --- |
| Raw observation | Source-native cell, image, or signature before PerturbLens transformations |
| Experimental unit | Recorded well/sample/signature/replicate unit to which observations belong; independence is assessed by the task |
| Condition | A perturbation/control condition with biological and experimental metadata |
| State representation | A vector or distribution describing observed cellular state in a declared feature space |
| Reference set | Controls or perturbed reference observations used to construct a response |
| Response object | The change of a condition relative to a declared reference in one state representation |
| Comparison unit | A task-defined group of response objects used for similarity, retrieval, or prediction |
| Split | A materialized train/validation/test partition with an explicit held-out biological axis |

## Schema conventions and canonical IDs

Canonical tables are Parquet. IDs and labels are UTF-8 strings, counts/positions
are int64, measurements are float64 unless a matrix declares another dtype,
flags are boolean, timestamps are UTC, and multi-valued fields are typed lists.
Required columns always exist; fields marked `?` may be null. Missing source
metadata remain null with a reason in the mapping/QC table, never the strings
`NA`/`unknown`, a guessed value or a substituted zero. Enumerated `unknown` states
are used only where a contract explicitly defines them. Source-native files and
raw labels remain unchanged.

In the shared schemas, ID/path/version/label fields are strings, `*_ids` and
reason/evidence collections are lists of strings, positions/counts are int64,
physical measurements are float64, and agreement flags are booleans. Explicit
field types override this convention. `source_trace` is a source-native record
identifier resolved through its dataset/file inventory, never a display label
alone. Unknown values in nullable fields need a mapped missingness reason.

Identifiers are immutable and independent of filesystem paths. Namespace local
IDs by source/release/dataset and preserve `source_trace`; register global entity
IDs rather than constructing them from display names. Allowed path components
use ASCII letters, digits, dot, underscore and hyphen, excluding `.` and `..`.
Build IDs use a descriptive prefix plus a unique timestamp or registered suffix;
they are not inferred from current directory names. Do not recycle IDs.
Each mapper records its ID-generation rule, including escaping and collision
checks. Mapping changes create a new version, not silent reassignment.

There is no universal biological `condition_key`. `condition_id` identifies an
exact source experimental condition, preserving its block/time/dose distinctions.
Separate source conditions are not merged because labels agree. Multiple
experimental units may share a condition. `comparison_key`, `matching_key` and
`positive_key` belong to a versioned relation/task rule, not source identity.

## Observation and experimental-unit tables

`observations.parquet`: one row per measured cell, image, profile or signature.
Required fields: `observation_id` (primary key), `source_id`, `release`,
`dataset_id`, `condition_id`, `experimental_unit_id`, `observation_type`,
`readout_modality`, `source_trace`, `file_id`, `source_row_key`.
`observation_type` is `cell`, `image`, `profile`, or `signature`. Optional fields
include `parent_observation_id`, `field_id`, `channel`, `z_plane`, `timepoint`,
`source_cell_id` and `segmentation_object_id`. Image/profile identity must retain
its relation to the well and, where applicable, segmented object.

`experimental_units.parquet`: one row per unit, primary key
`experimental_unit_id`. Required fields: `source_id`, `dataset_id`, `condition_id`,
`experimental_unit_type`, `source_trace`, `independence_status`.
Nullable fields: `parent_experimental_unit_id`, `replicate_group_id`,
`replicate_type`, `batch_id`, `plate_id`, `well_id`, `sample_id`,
`donor_id`, `organoid_id`, `source_replicate_count`, `aggregation_description`.
`experimental_unit_type` is `well`, `sample`, `signature`, `replicate`,
`organoid`, or `other`; `replicate_type` is `biological`, `technical`, or `unknown`;
`independence_status` is `documented` or `unresolved`.

A source-native measurement ID may identify an unresolved experimental unit, but
does not certify independent replication. Parent unit links must be acyclic and
within the recorded condition; a plate containing several conditions is a block
field, not a parent condition. Cells/fields share a well; wells may share donors
or biological replicates. LINCS signatures may already aggregate replicates;
record aggregation instead of inventing independent wells. Tasks choose the
appropriate grouping/resampling level from this hierarchy.

## Condition identity

A harmonized condition registry preserves at least:

- `condition_id`
- `source`
- `readout_modality`: `transcriptomics` or `morphology`
- `intervention_type`: `genetic`, `chemical`, `control`, or `combination`
- `intervention_mode`: source-specific normalized mode such as `CRISPRi`, `CRISPRa`, `expression`, `compound`
- `perturbation_id`: compound/reagent/combination identity
- `target_set`: canonical target set when known
- `cell_context`
- `time_hr`
- `dose_value`
- `dose_unit`
- `replicate_id`
- `batch_id`
- `source_trace`

`conditions.parquet` has primary key `condition_id`. Required non-null fields are
`source_id`, `release`, `dataset_id`, `readout_modality`, `intervention_type`,
`perturbation_id`, `treatment_raw`, `source_trace` and `is_control` (bool).
`intervention_mode`, `perturbation_entity_id`, `cell_context_id`, `cell_context`,
`target_set`, `replicate_id`, `batch_id` and covariates may be null when unknown;
eligibility rules determine whether that prevents a task. `source` is the
source-ID projection retained for result-schema compatibility.
`target_membership_rule_id` and `catalog_build_id` accompany non-null target sets.
`treatment_raw` preserves the source treatment label; normalized treatment is
represented by intervention type/mode and perturbation identity, not guessed
from filename. Technical fields shared with experimental units must agree.

`metadata/perturbations.parquet` maps `(source_id, release, perturbation_id)` to
`perturbation_entity_id?`, with `perturbation_label_raw`, `intervention_mode_raw?`,
`mapping_status`, `mapping_version` and `source_trace`. It is the source-local
mapping table, distinct from the global canonical entity catalog.

Combination conditions additionally preserve `combination_members` and any interpretable constituent strengths.

`combination_members` is a derived list from the versioned
[combination membership table](relations.md), not a parsed `A+B` string used as
the sole evidence of composition.

## Time and dose

Required columns in conditions, nullable when not measured:

| Field | Type | Semantics |
| --- | --- | --- |
| `time_raw`, `time_unit_raw` | string? | Unmodified source duration and unit |
| `time_hr` | float64? | Exposure duration in hours, not collection date or culture age |
| `dose_raw`, `dose_unit_raw` | string? | Original dose and unit |
| `dose_value_std`, `dose_unit_std` | float64?, string? | Parsed value in a declared standardized unit |
| `dose_molar` | float64? | Chemical molar concentration in mol/L only |
| `time_conversion_status`, `dose_conversion_status` | enum | `converted`, `already_standard`, `missing`, `unconvertible`, `not_applicable` |
| `conversion_rule_id` | string? | Versioned parsing/unit rule |

`dose_value` and `dose_unit` are compatibility projections of the standardized
fields, not a second independent value. Molar units convert to `mol/L`; e.g.
1 uM is `1e-6` mol/L. Mass concentration requires documented molecular mass and
compound form before molar conversion. Percent, MOI and genetic strengths retain
their own units; `dose_molar` remains null. Controls are not assigned dose zero
unless the source establishes it. Missing time is not a default exposure time.
Unknown schedules, ranges or multiple administrations retain raw values and need
a source-specific schedule table before dynamic interpretation. Culture age and
sampling time are separate metadata. R3 time/dose remain explanatory covariates.

## Controls

`controls.parquet` has primary key `condition_id`, referencing an `is_control=true`
condition. Required columns: `control_type`,
`compatible_intervention_type: list<string>?`, `cell_context_id?`, `cell_context?`,
`batch_id?`, `plate_id?`, `time_hr?`, `source_trace`, `compatibility_evidence`.
`control_type` is `untreated`, `vehicle`, `non_targeting`, `mock`, `other`, or
`unknown`; preserve `control_label_raw`. Unknown compatibility is null, not an
empty permissive list. For unit-specific compatibility retain
`experimental_unit_ids: list<string>?` rather than merging different plates.

This table records control candidates from experimental design, not a selected
response reference. Exact pools, exclusions and weights belong to response
construction. Source-native effect signatures without exported controls retain
their upstream reference description and availability limitation; do not create
synthetic control rows.

## State representation identity

Every state object records:

- `condition_id`
- `state_representation`
- `feature_index_version`
- `n_observations`
- aggregation/distribution semantics
- source build manifest

Primary representation vocabulary:

Transcriptomics:

- `Gene`
- `Pathway`
- `FM:<model>`

Morphology:

- `CellProfiler`
- `DeepMorphology:<model>`

## Response identity

Every response object records:

- `response_id`
- `condition_id`
- `reference_id`
- `state_representation`
- `response_view`: `Delta` or `SystemaResidual`
- `feature_index_version`
- numerator/condition observation count
- reference observation count
- response-construction version

A response object is not a scalar distance. It retains direction/coordinates in its representation space unless the representation itself is a distributional object.

## Target identity

A target set is a sorted unique list of stable target IDs under a pinned
membership rule; human gene-symbol labels remain uppercase under the Gene
contract. [Evidence-bearing edges](catalog.md) are the authoritative annotation
records. Multi-target compounds remain multi-target conditions. Task-specific
membership expansion never rewrites source perturbation identity.

## Context identity

`cell_context` is the biological context used by a task split or match, normally a cell line/type. Dataset, batch, plate, source, and replicate are separate fields and may not be silently conflated with biological context.

## Independence

Cells, images, wells, signatures, compounds, targets, and experiments are different sampling levels. Task contracts identify which level defines independent resampling or generalization.

# PerturbLens Data Object Model

## Core objects

| Object | Meaning |
| --- | --- |
| Raw observation | Source-native cell, image, or signature before PerturbLens transformations |
| Condition | A perturbation/control condition with biological and experimental metadata |
| State representation | A vector or distribution describing observed cellular state in a declared feature space |
| Reference set | Controls or perturbed reference observations used to construct a response |
| Response object | The change of a condition relative to a declared reference in one state representation |
| Comparison unit | A task-defined group of response objects used for similarity, retrieval, or prediction |
| Split | A materialized train/validation/test partition with an explicit held-out biological axis |

## Condition identity

A harmonized condition registry should preserve at least:

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

Combination conditions additionally preserve `combination_members` and any interpretable constituent strengths.

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

A target set is canonicalized as uppercase stable tokens. Multi-target compounds remain multi-target conditions. Task-specific target membership may expand a condition into multiple target-linked comparison units, but expansion never rewrites the source perturbation identity.

## Context identity

`cell_context` is the biological context used by a task split or match, normally a cell line/type. Dataset, batch, plate, source, and replicate are separate fields and may not be silently conflated with biological context.

## Independence

Cells, images, wells, signatures, compounds, targets, and experiments are different sampling levels. Task contracts identify which level defines independent resampling or generalization.
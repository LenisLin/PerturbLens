# Morphology Preprocessing Contract

## Scope

This contract defines the minimum processing requirements for R5/R6 morphology sources. A source-specific appendix is required once a concrete imaging dataset is frozen.

Apply the [frozen workflow](../workflow.md), [object schema](../object_model.md),
[matrix/image semantics](../matrix_semantics.md) and [manifest](../manifests.md)
contracts. Intake inventories images, metadata and precomputed profiles/embeddings
separately. High-cost external profiles may be adopted after provenance, feature,
row-level and fit-scope validation; a profile-only source does not establish image
availability. Full extraction is not an intake operation.

## Required inputs

- raw or normalized perturbational images;
- plate/well/field/cell identifiers;
- perturbation and control metadata;
- cellular context;
- acquisition channels and imaging metadata;
- replicate/batch fields;
- time/dose where available.

## Prepared assets and state handoff

Prepared assets retain image locations, acquisition metadata, condition and
experimental-unit identity, and QC/exclusion records. Precomputed profiles and
embeddings retain their source provenance and require explicit adoption checks.

[Morphology representations](../../representations/morphology.md) owns
segmentation/feature extraction, feature QC and normalization, and deep-encoder
construction. These state-build operations follow intake and prepared processing;
their availability is not established by an image or profile inventory alone.

## Matching tier

Every cross-readout link is assigned an R5 matching tier under
[shared relations](../relations.md). A morphology condition can have different
tiers for different RNA counterparts, or no counterpart; tier is not an intrinsic
condition label. Cross-readout claims preserve the selected links and tiers.

## Outputs

- condition registry;
- image/acquisition registry and cell-image-well membership where available;
- QC/exclusion table;
- prepared-build manifest.

Keep prepared image/metadata/QC assets separate from CellProfiler and
DeepMorphology state builds. Their row/feature indices and cell-image-well
membership follow the matrix contract. Field/cell counts do not replace
independent well/biological-replicate support. State outputs and their manifests
are defined by the morphology representation contract.

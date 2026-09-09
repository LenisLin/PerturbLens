# Morphology Representations

## CellProfiler

`CellProfiler` is the primary interpretable morphology feature space. It contains versioned, QC-filtered measurements from cell/nucleus/cytoplasm/organelle objects. Features retain semantic identity and are grouped by feature family for interpretation.

Primary response construction occurs after declared plate/batch-aware normalization.

## DeepMorphology

`DeepMorphology:<model>` is a fixed learned image embedding. The model/checkpoint, image channels, crop/aggregation definition, and embedding dimension are frozen in the state-build manifest.

Feature-wise DE-style interpretation is primary only for CellProfiler, because deep embedding coordinates do not have stable biological semantics by default.

## Cross-readout role

Transcriptomic and morphology feature dimensions are not compared coordinate-by-coordinate. R5 compares response strength, perturbation geometry, retrieval identity, and predictive mappings between the two spaces.

## Segmentation and CellProfiler surface

The primary interpretable morphology representation is built with a versioned
CellProfiler pipeline. The output retains cell-level features spanning, as available:

- size/area/diameter and shape;
- intensity;
- texture;
- granularity;
- spatial relationships;
- nucleus/cytoplasm/organelle feature families.

Feature extraction metadata include CellProfiler version, pipeline file hash,
segmentation object definitions, image channels, and failed-well/cell QC.

## Feature QC and normalization

Before response construction:

- remove non-finite and invariant features;
- record missingness;
- identify extreme technical artifacts;
- use plate/batch-aware normalization anchored to controls when justified;
- avoid feature selection using downstream target labels.

The exact normalization is versioned and stored in the state-build manifest.
Plate/control normalization records its fit scope and exact allowed units under
the [common manifest contract](../data/manifests.md).

## Deep encoder fitting boundary

The encoder must not be trained on the exact downstream positive relation and
then evaluated on that same relation without a disjoint split.

## State outputs

- cell/well profile registry;
- CellProfiler feature matrix and index;
- deep-embedding matrix and index when requested;
- feature QC/exclusion table;
- state-build manifest.

[Prepared image and metadata assets](../data/preprocessing/morphology.md) remain
separate from these states. Row/feature indices and cell-image-well membership
follow the [matrix/image contract](../data/matrix_semantics.md). Responses are
built under the [response contract](../responses/construction.md), not by feature
extraction or downstream scoring.

# Morphology Preprocessing Contract

## Scope

This contract defines the minimum processing requirements for R5/R6 morphology sources. A source-specific appendix is required once a concrete imaging dataset is frozen.

## Required inputs

- raw or normalized perturbational images;
- plate/well/field/cell identifiers;
- perturbation and control metadata;
- cellular context;
- acquisition channels and imaging metadata;
- replicate/batch fields;
- time/dose where available.

## Segmentation and CellProfiler surface

The primary interpretable morphology representation is built with a versioned CellProfiler pipeline. The output retains cell-level features spanning, as available:

- size/area/diameter and shape;
- intensity;
- texture;
- granularity;
- spatial relationships;
- nucleus/cytoplasm/organelle feature families.

Feature extraction metadata include CellProfiler version, pipeline file hash, segmentation object definitions, image channels, and failed-well/cell QC.

## Feature QC

Before response construction:

- remove non-finite and invariant features;
- record missingness;
- identify extreme technical artifacts;
- use plate/batch-aware normalization anchored to controls when justified;
- avoid feature selection using downstream target labels.

The exact normalization is versioned and stored in the state-build manifest.

## Deep morphology surface

A fixed image encoder may produce `DeepMorphology:<model>` embeddings. The build records model/checkpoint identity, input channels, image/cell crop definition, aggregation rule, and embedding dimensionality.

The encoder must not be trained on the exact downstream positive relation and then evaluated on that same relation without a disjoint split.

## Matching tier

Every morphology condition is assigned an R5 matching tier from `docs/data/sources.md`. Cross-readout claims preserve the tier in outputs.

## Outputs

- condition registry;
- cell/well profile registry;
- CellProfiler feature matrix and index;
- deep-embedding matrix and index when requested;
- QC/exclusion table;
- state-build manifest.
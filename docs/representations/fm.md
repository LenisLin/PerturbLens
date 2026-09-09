# Transcriptomic Foundation-Model Representation

## Meaning

`FM:<model>` denotes a fixed learned transcriptomic state representation generated from an explicit model/checkpoint. FM is a representation family, not a single canonical cellular-state space.

## Registered extractor families

The repository currently provides extraction utilities for:

- `scgpt`
- `geneformer`
- `scbert`
- `scfoundation`
- `uce`
- `state`
- `tahoe-x1`

These utilities retain legacy K562 snapshot entrypoints; they are not current
R2-R6 run adapters. See the [extractor interface status](../../scripts/fm_extractors/README.md).
Their reusable state-extraction routines still require the current state-build
and response-construction contracts before producing PerturbLens evidence.

Availability of an extractor does not require every model to appear in every main-text comparison. A primary FM panel must be frozen before result inspection to avoid model shopping.

## Build contract

Each FM surface records:

- model family and checkpoint/version;
- tokenizer/gene vocabulary where applicable;
- input normalization assumptions;
- cell aggregation or pooling rule;
- embedding layer/shape;
- runtime environment;
- successful condition coverage and exclusions.

FM state embeddings are generated before task evaluation. Delta or SystemaResidual response objects are computed in the fixed FM state space by the shared response-construction contract.

## Interpretation

An FM embedding may emphasize or suppress biological variation relative to Gene/Pathway space. Higher task scores do not establish that the embedding is a more complete representation of cell state.

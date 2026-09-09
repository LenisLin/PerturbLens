# State Representation Contracts

State representations describe observed cellular states, separately from
[response construction](../responses/construction.md) and downstream evaluation.

| Family | Contract | Meaning |
| --- | --- | --- |
| Gene | [Gene](gene.md) | Gene-level coordinates and shared feature support |
| Pathway | [Pathway](pathway.md) | Versioned pathway aggregation and coverage |
| FM | [Transcriptomic FM](fm.md) | Fixed model/checkpoint state embeddings |
| Morphology | [CellProfiler and DeepMorphology](morphology.md) | Interpretable image measurements and learned image embeddings |

## Build interfaces

1. Resolve prepared observations, feature identity and experimental units under
   the [data object model](../data/object_model.md) and
   [matrix/image contract](../data/matrix_semantics.md).
2. Apply the family-specific feature construction and QC contract. Record model,
   resource, normalization and exact fit scope in the
   [artifact manifest](../data/manifests.md); split-dependent fitting follows
   frozen membership under the [workflow](../data/workflow.md).
3. Register states under the [data architecture](../data/architecture.md), then
   pass them to response construction. Source-native effects retain their declared
   value semantics rather than being relabeled as untreated state measurements.

These contracts do not certify existing extractors or imported embeddings as
validated state builds. Model selection and task eligibility remain explicit
pre-execution decisions, not conclusions from model availability.

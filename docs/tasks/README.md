# Scientific Task Contracts

Tasks define lawful biological comparisons, matching, splits and allowed model
information. [Research](../research/result_architecture.md) owns the argument;
the [roadmap](../roadmap.md) owns execution dependency order.

| Result | Contract | Biological boundary |
| --- | --- | --- |
| R1 | [Project framework](../project.md) | Shared data, state, response and evaluation definitions; no separate prediction task |
| R2 | [Genetic learnability](genetic_learnability.md) | Inner, unseen context, unseen target |
| R3 | [Chemical learnability](chemical_learnability.md) | Inner, unseen context, unseen compound, unseen target |
| R4 | [Cross-intervention](cross_intervention.md) | Genetic versus chemical responses |
| R5 | [Cross-readout](cross_readout.md) | Transcriptomic versus morphological responses |
| R6 | [Combination](combination.md) | Constituents versus combined responses under a declared null |

## Shared interfaces

- [Data relations](../data/relations.md) define reusable matching schemas; each
  task selects its lawful cohort and preserves relation lineage.
- [Representations](../representations/README.md) and
  [responses](../responses/README.md) own shared state and response methods.
- [Population similarity](../metrics/population_similarity.md),
  [retrieval](../metrics/retrieval.md), [prediction](../metrics/prediction.md), and
  [aggregation](../metrics/aggregation.md) own calculations.
- [Output schemas](output_schemas.md) and [validation](validation.md) own task
  result interfaces and acceptance rules; the
  [evidence index](../governance/evidence_index.md) owns evidence registration.

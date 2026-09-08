# Instance Retrieval Metrics

## Question

Retrieval asks whether a response retains enough specificity to identify the correct perturbation, target, intervention counterpart, or cross-readout counterpart from a lawful gallery.

## Required objects

Each query records:

- `query_id`
- task/relation and direction
- state representation
- response view
- gallery definition/version
- `gallery_size`
- positive key(s)
- `n_positive_keys`
- rank(s)

The task contract defines what counts as a positive and which candidates are lawful negatives.

## Primary metrics

- rank of best lawful positive;
- MRR;
- Hit@1;
- Hit@3;
- Hit@5;
- normalized rank percentile or PDS-style discrimination where appropriate.

## Multi-positive settings

Multi-target compounds or multiple lawful counterparts require an explicitly declared rule (best-positive rank, average-positive rank, or set retrieval). Multiple positives are not silently converted to duplicate independent single-positive queries.

## Chance/context calibration

Summary tables retain gallery size and positive count. Chance-aware summaries may compare observed ranks against permutation or uniform-ranking references matched to gallery structure.

## Leakage

Leave-one-out is required when the query could otherwise contribute to its own reference/centroid. Cross-context/target/readout galleries are materialized before scoring, and model-trained representations must respect the corresponding split.
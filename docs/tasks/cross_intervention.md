# R4 Cross-Intervention Contract

## Scientific question

Given internally supported genetic and chemical response structure, what target-linked response information is conserved when intervention modality changes?

## Unit

Primary unit:

```text
(source_scope, cell_context, anchor_target)
```

A lawful unit has at least one eligible single-target genetic response and one target-linked chemical response under the task's target-membership rule.

Chemical conditions retain compound identity. Multi-target compounds may enter multiple anchor-target units only through a persisted membership table; dependence across those memberships is preserved in inference/aggregation.

Genetic intervention mode is retained and can be restricted or stratified when directionality makes a chemical-genetic comparison inappropriate.

## Matching

Primary comparisons require matched cell context and compatible readout/state/response definitions. Time/dose are retained and may be restricted or modeled but do not become target identity.

## Population similarity

Compare chemical and genetic response centroids within each lawful anchor-target/context unit using paired state representations and response views.

## Retrieval

### C2G

Chemical response query against a genetic target gallery.

### G2C

Genetic response query against a chemical/target gallery defined before scoring.

Directions remain separate. Multi-positive handling is explicit for multi-target compounds.

## Prediction / translation

Cross-intervention predictive mapping may be evaluated as a secondary family when train/test target/context splits are explicit. Measured-response concordance remains distinct from learned translation.

## Internal-support stratification

Each R4 unit should be linked to R2/R3 internal measured-response support. This enables categories such as:

- internally supported and cross-intervention conserved;
- internally supported and cross-intervention divergent;
- internally weak/uncertain.

This is a response taxonomy, not a reliability correction formula.

## Primary interpretation

Compare Gene, Pathway, and FM levels to determine whether conservation occurs at precise gene-level response or only at coarser program/latent levels.

## Claim boundary

Cross-intervention similarity is not causal equivalence. Divergence is not automatically off-target pharmacology.
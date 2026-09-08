# PerturbLens Research Roadmap

The roadmap expresses dependency order. Completion is recorded only in `docs/governance/state.md` and evidence manifests.

## Phase 1 — Framework closure

Freeze before production analysis:

1. source inventory and metadata coverage;
2. state-representation contracts;
3. control Delta and SystemaResidual reference semantics;
4. population similarity and retrieval metrics;
5. Cell-Eval2/VCC2026 prediction metric version and configuration;
6. unified result schemas and validation assertions.

Deliverable: R1-ready methods/data surfaces and executable shared contracts.

## Phase 2 — R2 genetic learnability

Build and validate:

- inner/replicate split;
- unseen-context split;
- unseen-target split;
- baseline and model registry;
- Gene/Pathway/FM response views;
- population, retrieval, and prediction outputs.

Primary question: which genetic response information stops being transferable as biological novelty increases?

## Phase 3 — R3 chemical learnability

Build and validate:

- inner compound response;
- unseen context;
- unseen compound with target stratification;
- unseen target;
- multi-target annotation handling;
- time/dose explanatory models.

Primary question: what response structure is compound-specific, target-linked, context-dependent, or transferable?

## Phase 4 — R4 cross-intervention

Construct matched target-context cohorts and evaluate chemical-to-genetic and genetic-to-chemical conservation under matched response views and representations.

Primary question: how much target-linked response information survives a change in intervention modality?

## Phase 5 — R5 cross-readout

Before execution, freeze morphology sources and matching tiers. Then materialize CellProfiler and deep-morphology features, construct response views, and evaluate response strength, geometry, retrieval, and cross-modal prediction.

Primary question: which response information is shared between transcriptomic and morphological readouts, and which is modality-specific?

## Phase 6 — R6 combination

Freeze eligible genetic and chemical combination sources and phenotype-appropriate nulls. Compare observed combination responses with additive or matching references and evaluate residual reproducibility and predictability.

Primary question: where does single-perturbation response compositionality break down?

## Phase 7 — Synthesis

Integrate R2-R6 without collapsing them into a single leaderboard. Synthesis should emphasize the boundary ladder:

```text
learnable
-> context/target transferable
-> cross-intervention conserved
-> cross-readout conserved
-> compositional
```

## Stop conditions

A result family is deferred rather than forced when matching support, independent replicates, source metadata, or lawful split sizes are insufficient. Negative or null results are valid outcomes if the comparison is adequately powered and auditable.
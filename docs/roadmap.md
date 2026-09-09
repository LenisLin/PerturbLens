# PerturbLens Research Roadmap

The roadmap expresses dependency order. Completion is recorded only in `docs/governance/state.md` and evidence manifests.

## Preparation versus production

Source discovery, metadata coverage audits and matching feasibility assessments
for morphology and combinations can begin during framework closure. They do not
authorize R5/R6 production analyses or waive their source and task freezes.
Scientific dependencies below govern claims and analysis entry, not a requirement
to postpone all downstream data preparation until preceding results are complete.

| Stage | Canonical implementation contracts | Entry or handoff |
| --- | --- | --- |
| Framework | [Data workflow](data/workflow.md), [representations](representations/README.md), [responses](responses/README.md), [validation](tasks/validation.md) | Frozen shared definitions and executable gates before production |
| R2/R3 | [Genetic](tasks/genetic_learnability.md), [chemical](tasks/chemical_learnability.md) | Eligible sources, lawful splits, declared models and references |
| R4 | [Cross-intervention](tasks/cross_intervention.md) | Matched cohort and internal-support evidence |
| R5 | [Cross-readout](tasks/cross_readout.md) | Frozen morphology sources, state builds and matching tiers |
| R6 | [Combination](tasks/combination.md) | Eligible combinations, constituent support and declared nulls |
| Synthesis | [Evidence index](governance/evidence_index.md), [figure plan](visualization/figure_plan.md) | Validated result tables with preserved boundaries and denominators |

Organoid source preparation follows the existing
[workflow extension](data/workflow.md#organoid-extension). Organoid is a culture
model/context rather than a readout modality; these requirements do not freeze a
specific organoid source, split or new result family.

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

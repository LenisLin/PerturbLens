# Figure Plan

## Purpose

This file maps PerturbLens scientific questions to main figures. Figure numbering organizes presentation; executable definitions remain in `docs/data/`, `docs/tasks/`, and `docs/metrics/`.

## Main Figure Roles

| Figure | Main Result | Role |
| --- | --- | --- |
| Figure 1 | R1 | PerturbLens framework, data, state/response representations, evaluation layers, boundary ladder |
| Figure 2 | R2 | Genetic perturbation learnability: inner -> unseen context -> unseen target |
| Figure 3 | R3 | Chemical perturbation learnability: inner -> context -> compound -> target; dose/time covariates |
| Figure 4 | R4 | Chemical-genetic cross-intervention conservation |
| Figure 5 | R5 | Transcriptomic-morphological cross-readout conservation |
| Figure 6 | R6 | Combination compositionality and interaction residual structure |

No figure is evidence by itself. Every panel requires a versioned task/result table and validation chain.

## Figure 1 — Framework

Recommended panel responsibilities:

- **1A** data/source landscape and coverage;
- **1B** state representation families: Gene, Pathway, FM, CellProfiler, deep morphology;
- **1C** response construction: control delta versus Systema-style perturbation-specific reference;
- **1D** three evaluation layers: population similarity, retrieval, prediction;
- **1E** boundary ladder: within -> context -> target/compound -> intervention -> readout -> composition.

R1 should define measurement, not rank representations.

## Figure 2 — Genetic Learnability

Recommended structure:

- inner/replicate information availability;
- cross-context transfer;
- unseen-target generalization;
- breakdown of performance changes by response-information family;
- selected Gene/Pathway/FM and control/Systema comparisons.

Supplementary figures can carry dataset-, target-family-, intervention-mode-, baseline-, and model-level detail.

## Figure 3 — Chemical Learnability

Recommended structure:

- inner compound response;
- cross-context transfer;
- new compound / same target;
- unseen compound;
- unseen target;
- time/dose explanatory analysis.

The main figure should visually distinguish compound novelty from target novelty.

## Figure 4 — Cross-Intervention Conservation

Recommended structure:

- target-matched chemical/genetic population similarity;
- C2G and G2C retrieval;
- within-intervention learnability versus cross-intervention conservation map;
- biological-resolution comparison across Gene/Pathway/FM where lawful;
- selected context/target patterns.

Legacy Task2 outputs may contribute only after alignment to the new R4 contract.

## Figure 5 — Cross-Readout Conservation

Recommended structure:

- transcriptomic versus morphology response strength;
- perturbation-geometry correspondence;
- cross-modal retrieval;
- cross-modal prediction;
- intervention x readout 2 x 2 analysis;
- shared versus readout-specific response structure.

The intervention x readout analysis is the highest-priority scientific differentiator and should receive main-panel space if data coverage supports it.

## Figure 6 — Combination Compositionality

Recommended structure:

- genetic combination observed versus expected response;
- chemical combination observed versus expected response;
- interaction residual structure;
- simple compositional baselines versus specialized prediction models;
- cross-representation or cross-modal residual conservation where available.

Do not label a non-zero residual as synergy without an explicitly appropriate biological null and supporting evidence.

## Shared Plot Workflow

1. A versioned task produces audited tables and manifests.
2. Python prepares panel-level summaries from lawful rows and pre-approved statistics.
3. R or another rendering layer performs ordering/composition without redefining statistics.
4. Review checks panel scope, denominators, representation, response view, split identity, and evidence provenance.

## Supplementary Philosophy

Use supplementary figures for robustness and breadth:

- alternative pathway libraries;
- additional FM/image encoders;
- metric sensitivity;
- distributional analyses;
- dose/time strata;
- batch/plate/source effects;
- target annotation confidence;
- detailed model leaderboards.

Main figures should remain organized around scientific questions, not exhaustive representation/model combinations.

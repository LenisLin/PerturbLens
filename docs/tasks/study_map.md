# PerturbLens Study Map And Legacy Task Crosswalk

## Purpose

This document maps the new R1-R6 PerturbLens scientific architecture onto the retained M2M Task1/Task2 execution core. It prevents legacy outputs from being silently reinterpreted as evidence for new analyses.

## Status Vocabulary

- **retained**: existing task contract and outputs keep their historical semantics;
- **reusable candidate**: an old output may support a new Result if an explicit alignment proof confirms identical units, representations, and metric semantics;
- **new contract required**: the analysis is scientifically approved but not executable until a versioned task contract exists;
- **not evidence**: proposal/figure prose alone does not establish completion.

## Main Result Crosswalk

| Result | Scientific question | Legacy support | Current execution status |
| --- | --- | --- | --- |
| R1 Framework | What is measured and compared? | data/object/metric contracts | documentation migration initiated; new response/prediction contracts pending implementation |
| R2 Genetic learnability | inner -> unseen context -> unseen target | Task1 internal/cross genetic surfaces provide partial geometry/retrieval support | new generalization/prediction task required |
| R3 Chemical learnability | inner -> context -> compound -> target | Task1 internal chemical surfaces provide partial geometry/retrieval support | new compound/target split and prediction task required |
| R4 Cross-intervention | what survives chemical vs genetic intervention change? | Task2 is the principal retained core | legacy group/retrieval may be reused where units align; new within-vs-cross synthesis required |
| R5 Cross-readout | transcriptomics vs morphology | none in current active contracts | new morphology data/representation/task contracts required |
| R6 Combination | compositionality and interaction residuals | some scPerturb source rows/combinatorial datasets may be relevant but are not currently a PerturbLens task | new combination contracts required |

## Legacy Task1

Retained scientific definition:

- fixed perturbation type;
- within-source and matched LINCS/scPerturb cross-source concordance;
- Gene/Pathway benchmark-wide representations;
- scoped FM analysis;
- population concordance and retrieval.

Potential PerturbLens reuse:

### R2

- genetic inner response geometry;
- matched cross-source genetic response comparison as a robustness/source-transfer analysis.

Legacy Task1 does **not** by itself define:

- unseen-cell prediction;
- unseen-target prediction;
- train/test model splits;
- VCC2026 prediction metrics.

### R3

- chemical inner response geometry/retrieval.

Legacy Task1 does **not** by itself define:

- new-compound/same-target splits;
- unseen compounds;
- unseen targets;
- chemical model-prediction evaluation.

## Legacy Task2

Retained scientific definition:

- within-dataset, within-cell-line target-linked chemical/genetic comparison;
- group concordance;
- C2G and G2C retrieval;
- target membership through `anchor_gene`.

Potential PerturbLens reuse:

### R4

Task2 provides the primary legacy evidence for the intervention boundary.

Before reuse, a migration record must verify:

- identical target membership semantics;
- exact cell/context scope;
- response construction used by each representation;
- gallery/positive construction;
- current versus PerturbLens reference view;
- denominator and exclusion handling.

PerturbLens R4 additionally requires a join to R2/R3 within-intervention learnability. That joint analysis is not part of the legacy Task2 contract.

## New Task Families To Create

Suggested contract names are descriptive rather than figure-numbered:

1. `genetic_learnability.md`
2. `chemical_learnability.md`
3. `cross_intervention.md`
4. `cross_readout.md`
5. `combination.md`

R1 is a framework/result-definition section and does not need a standalone empirical task unless a formal representation/metric benchmark is later approved.

## Shared Split Vocabulary To Freeze

### Inner

Independent replicate or lawful split within the same perturbation and cellular context. The split unit must reflect the desired independence level; cell-level splits must not be presented as independent experimental replication.

### Unseen context

Test cellular context is absent from perturbation training observations under the declared task. Whether its unperturbed state may be available must be explicit.

### Unseen genetic target

Target is absent from perturbation training observations. Models may use only target information available independently of the held-out response data.

### New compound / seen target

Compound identity is held out while its annotated target has response evidence from other perturbations.

### Unseen compound

Compound is absent from response training data. Structure or external annotations may be used only if allowed by the task.

### Unseen chemical target

The target itself is absent from response training data; this is a stronger generalization regime than unseen compound.

### Cross intervention

Query/target relation crosses chemical/genetic intervention type while preserving lawful target/context matching.

### Cross readout

The relation crosses transcriptomic/morphological readout. Matched condition level must be explicit: perturbation-only, perturbation+context, perturbation+context+dose/time, or truly paired assay.

### Combination

Test response contains multiple perturbations and is evaluated against a declared constituent-based null and/or prediction model.

## Migration Rule

No old output is renamed in place. PerturbLens result tables should either:

1. reference the exact legacy table plus an alignment proof; or
2. be recomputed under a new task contract and new schema.

Historical manifests and `task1_*`/`task2_*` identifiers remain immutable evidence facts.

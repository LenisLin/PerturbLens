# PerturbLens

PerturbLens is a response-centric framework for characterizing what information in cellular perturbation responses is reproducible, learnable, transferable across contexts and targets, conserved across intervention and readout modalities, and compositional under combined perturbations.

The project is a **descriptive/characterization study**, not a model leaderboard. Models are one measurement instrument for response learnability.

## Core framework

```text
Data
  -> State representation
  -> Response construction
  -> Biological relation / evaluation
```

Primary state representations:

- Transcriptomics: `Gene`, `Pathway`, `FM`
- Morphology: `CellProfiler`, `Deep morphology embedding`

Primary response views:

- control-referenced `Delta`
- Systema-style perturbation-specific residual view

Shared evidence families:

- population similarity
- instance retrieval
- model prediction

## Main Results

1. **R1 Framework** — data, representations, response construction, metrics, and comparison axes.
2. **R2 Genetic learnability** — inner split -> unseen cellular context -> unseen target.
3. **R3 Chemical learnability** — inner split -> unseen context -> unseen compound -> unseen target; time/dose are explanatory covariates.
4. **R4 Cross-intervention** — target-linked response conservation between chemical and genetic perturbations.
5. **R5 Cross-readout** — response conservation between transcriptomics and morphology.
6. **R6 Combination** — compositionality and interaction residuals under combined perturbations.

## Start here

Canonical repository: `https://github.com/LenisLin/PerturbLens`.

```bash
git clone git@github.com:LenisLin/PerturbLens.git
cd PerturbLens
python -m pip install -e ".[dev]"
```

- `AGENTS.md`
- `docs/README.md`
- `docs/project.md`
- `docs/research/proposal.md`
- `docs/research/landscape.md`
- `docs/research/result_architecture.md`
- `docs/governance/state.md`
- `docs/governance/runbook.md`

## Repository layout

- `docs/research/`: scientific rationale, proposal, and competitive landscape
- `docs/tasks/`: executable comparison contracts
- `docs/data/`: source, state-representation, and response-construction contracts
- `docs/metrics/`: population similarity, retrieval, prediction, and aggregation
- `docs/visualization/`: figure architecture and visual standards
- `docs/manuscript/`: manuscript argument and writing standards
- `docs/governance/`: execution, evidence, storage, and collaboration rules
- `scripts/fm_extractors/`: reusable transcriptomic FM extraction utilities
- `src/perturblens/`: project Python package surface

Derived data and run artifacts do not live in the source checkout.

See [the extractor interface status](scripts/fm_extractors/README.md) before
using the retained FM utilities. Their legacy snapshot CLIs are not R2-R6
production runners.

Local pre-reset implementation work, when present, is preserved separately in
the Git-ignored `.local/legacy-pre-perturblens/` tree. It is not part of the
active package, test suite, or scientific evidence.

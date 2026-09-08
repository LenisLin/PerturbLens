# PerturbLens Agent Guide

Start with `docs/README.md`, `docs/project.md`, and `docs/research/result_architecture.md`. They define the active scientific framing, documentation ownership, and the staged relationship between the new PerturbLens study and the retained M2M execution core.

## Always-Active Repo Rules

### Source Hierarchy

When repo documents disagree, use this order:

1. Audited manifests and stage outputs for claims about what a run actually produced.
2. Active contracts in `docs/tasks/`, `docs/data/`, and `docs/metrics/` for executable semantics.
3. `docs/project.md` and `docs/governance/*.md` for approved project scope and execution state.
4. `docs/research/` for scientific rationale, literature positioning, and main-result architecture.
5. `docs/manuscript/` and `docs/visualization/` for presentation.

The roadmap proposes future work. History preserves earlier decisions. Neither supersedes an active executable contract.

### Scientific Framing

PerturbLens is a response-centric characterization study, not primarily a model leaderboard. The central object is the perturbation response represented under explicit state and response spaces.

The primary study axes are:

- state representation: Gene, Pathway, transcriptomic FM, CellProfiler morphology, deep morphology embedding;
- response construction: control delta and Systema-style perturbation-specific reference;
- evaluation: population similarity, instance retrieval, model prediction;
- biological boundaries: within, cellular context, target/compound, intervention modality, readout modality, combination.

Main Results are organized as R1 framework, R2 genetic learnability, R3 chemical learnability, R4 chemical-genetic conservation, R5 transcriptomic-morphological conservation, and R6 combination compositionality.

### Legacy M2M Boundary

Existing Task1/Task2 contracts and their NAS-backed outputs are retained during migration. Do not silently reinterpret an old `task1_*` or `task2_*` table as evidence for a new PerturbLens result. Use `docs/tasks/study_map.md` for the mapping and create a new or revised task contract before production execution of new semantics.

Current M2M implementation names, package paths, and NAS roots may remain during migration for provenance. Renaming source code or storage roots is a separate change and must preserve historical traceability.

### Minimum Grounding Before Changes

Read the smallest relevant subset of:

- `docs/README.md`, `docs/project.md`, and `docs/research/result_architecture.md`;
- `docs/governance/state.md` and `docs/governance/runbook.md`;
- `docs/governance/documentation_policy.md`;
- `docs/data/object_model.md` and `docs/data/response_construction.md` when touching response objects;
- relevant representation contracts under `docs/data/representations/`;
- `docs/tasks/study_map.md` plus the relevant task contract;
- relevant metric contracts under `docs/metrics/`;
- `docs/manuscript/outline.md` and `docs/visualization/figure_plan.md` for manuscript or figure changes.

### Evidence And Storage Discipline

- Treat the checkout as source-only.
- Historical M2M NAS roots remain authoritative for existing runs until a migration decision creates new roots.
- Every result claim must point to a concrete manifest/table/assertion chain.
- Candidate morphology, cross-modal, prediction, expanded-FM, and combination analyses are not completed merely because they appear in the proposal.

### Change Discipline

- Update the controlling domain contract before changing analysis semantics.
- Keep project framing in `docs/project.md`, research rationale in `docs/research/`, future execution in `docs/roadmap.md`, observed status in `docs/governance/state.md`, and rationale in `docs/history/`.
- Keep representation, response-construction, metric, task, and figure responsibilities separate.
- Do not create an exhaustive representation-by-metric-by-task factorial benchmark unless a scientific question requires it.
- Preserve null, negative, and uncertain outcomes as valid completion states.

## Repo-Scoped Skills

Legacy repo-scoped skills remain available during migration:

- `.agents/skills/m2m-contract-grounding/SKILL.md`
- `.agents/skills/m2m-evidence-trace/SKILL.md`
- `.agents/skills/m2m-migration-runbook/SKILL.md`

Their names are retained for compatibility; use the active PerturbLens documents above as the scientific source of truth.

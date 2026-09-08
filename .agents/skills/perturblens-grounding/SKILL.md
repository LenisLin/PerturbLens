---
name: perturblens-grounding
description: Ground PerturbLens scientific scope, task semantics, response construction, and claim boundaries before changes.
---

# PerturbLens Grounding

Use this skill before changing scientific scope, task semantics, data objects, response construction, metrics, or figures.

1. Read `docs/project.md` and `docs/governance/state.md`.
2. Read the relevant research rationale under `docs/research/`.
3. Read the owning task contract under `docs/tasks/`.
4. Read the data and representation contracts under `docs/data/`.
5. Read the relevant metric contracts under `docs/metrics/`.
6. If a proposed change alters comparison units, split semantics, response references, metric definitions, or claim boundaries, update the owning contract before implementation.
7. Do not infer completed evidence from a planned task, path, figure, or proposal.

PerturbLens is response-centric: state representation, response construction, and biological comparison relation are separate concepts. Keep them separate in code and documentation.

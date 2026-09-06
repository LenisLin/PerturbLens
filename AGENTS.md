# M2M-Bench Agent Guide

Start with `docs/README.md` and `docs/project.md`. They identify the current
benchmark scope and the domain contracts that own its terminology and methods.

## Always-Active Repo Rules

### Source Hierarchy

When repo documents disagree, use this order:

1. Audited manifests and stage outputs
2. Active contracts in `docs/tasks/`, `docs/data/`, and `docs/metrics/`
3. `docs/governance/*.md`
4. `docs/manuscript/` and `docs/visualization/`

The roadmap proposes future work; history preserves earlier decisions. Neither
supersedes an active contract. Report disagreements between run outputs and
required behavior instead of silently rewriting either side.

### Minimum Grounding Before Changes

Read the smallest relevant subset of:

- `docs/README.md` and `docs/project.md`
- `docs/governance/state.md`
- `docs/governance/runbook.md`
- `docs/governance/documentation_policy.md`
- `docs/governance/storage_policy.md` for data or run roots
- `docs/data/object_model.md` and relevant preprocessing/representation/snapshot
  contracts when touching task data
- `docs/tasks/task1.md` for Task1 semantics
- `docs/tasks/task2.md` for Task2 semantics
- `docs/tasks/output_schemas.md` and `docs/tasks/validation.md` for outputs
- the relevant `docs/metrics/` contract for metric calculations
- `docs/manuscript/outline.md` and `docs/visualization/figure_plan.md` for
  manuscript or figure work

### Evidence And Storage Discipline

- Use NAS-backed roots for evidence discovery:
  - `/mnt/NAS_21T/ProjectData/M2M/runs`
  - `/mnt/NAS_21T/ProjectData/M2M/runs/manuscript_active/analysis`
  - `/mnt/NAS_21T/ProjectData/M2M/runs/_staging/manuscript_visual_revision_current`
- Treat the local checkout as source-only.
- Every non-trivial claim should cite a file path, manifest, table, or command
  result.
- If evidence is incomplete, say what still needs checking.

### Scientific Boundaries

- M2M-Bench is a benchmark/evaluation paper.
- Keep `Task1` and `Task2` separate.
- Keep `FM` scoped to the `scPerturb/K562` `Figure 3F` local-only panel.
- Update the relevant contract docs before changing benchmark semantics or
  figure meaning.

### Change Discipline

- Keep names, paths, and figure roles synchronized across docs.
- Remove inactive wording instead of layering alternate names on top of the
  current system.
- Do not fall back from corrected multisource Task2 outputs to a scPerturb-only
  path.
- Keep research direction in `docs/roadmap.md`, observed progress in
  `docs/governance/state.md`, and decision rationale in `docs/history/`.
- Organize shared methods by responsibility, not by figure number. Archived
  documents are not active implementation instructions.

## Repo-Scoped Skills

Use repo-local skills when the task needs deeper workflow guidance:

- `.agents/skills/m2m-contract-grounding/SKILL.md`
- `.agents/skills/m2m-evidence-trace/SKILL.md`
- `.agents/skills/m2m-migration-runbook/SKILL.md`

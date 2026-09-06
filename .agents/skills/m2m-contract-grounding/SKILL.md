---
name: m2m-contract-grounding
description: Ground benchmark semantics, claim boundaries, and task definitions before changing M2M code or docs.
---

# M2M Contract Grounding

Use this skill when the task touches benchmark semantics, task wording, result
meaning, or figure roles.

## Load Order

Read only the smallest relevant subset, in this order:

1. `docs/README.md` and `docs/project.md`
2. `docs/governance/state.md`
3. `docs/governance/documentation_policy.md`
4. the relevant task and metric contracts under `docs/tasks/` and `docs/metrics/`
5. `docs/data/object_model.md` and the relevant preprocessing, representation,
   or snapshot contract when task data or manifests are involved
6. `docs/manuscript/outline.md` and `docs/visualization/figure_plan.md` for
   manuscript or figure work

## Core Workflow

1. State the exact benchmark question or figure role the task touches.
2. Confirm whether the task belongs to `Task1`, `Task2`, or the
   `scPerturb/K562` `FM` panel.
3. Identify the highest-priority document that defines the behavior today.
4. Lock the active field names, unit keys, and panel meanings before editing.
5. Update docs or code only after the semantic boundary is clear.

## Guardrails

- Keep `Task1` and `Task2` separate.
- Keep `anchor_gene`, `perturbation_gene`, `query_instance_id`, and
  `pair_mean_enrichment` consistent across docs.
- Keep `FM` scoped to the `Figure 3F` local-only panel.
- Update contract docs before changing benchmark semantics.

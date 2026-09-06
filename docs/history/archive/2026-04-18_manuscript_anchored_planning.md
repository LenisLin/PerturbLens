# Archived: Manuscript-Anchored Stage Planning

Archived on 2026-09-06. This is historical discussion, not an active contract.
Its figure-anchored organizing principle is superseded by the
[documentation architecture decision](../decisions/2026-09-06_documentation_architecture.md).
Original dates and references below describe the earlier planning context.

Status: temporary working document for iterative discussion and freeze decisions.

Date: 2026-04-18

## Summary

This document records the current agreed planning frame for manuscript-anchored
stage design. It is a temporary freeze artifact for discussion, not yet a final
contract document.

The current goal is not to recover a complete existing stage-to-script surface.
The current goal is to define a manuscript-driven planning framework that can
support later script design, document cleanup, and freeze-item confirmation
without losing information across `stage`, `scripts`, `manuscript`, and
`document` layers.

## Current Decisions

- The historical `S0-S7` chain is not used as the primary planning framework for
  the next discussion rounds.
- The new top-level framework is manuscript-anchored and uses `Figure 1`,
  `Figure 2`, and `Figure 3` as the main phases.
- Non-manuscript-facing but analysis-critical upstream steps are still kept in
  scope.
- Those upstream steps are attached to the nearest manuscript figure phase
  rather than moved into a separate shared-foundation phase.
- `FM` remains local to the `Figure 3F` panel and is handled inside the
  `Figure 3` phase rather than as a top-level phase.
- R-based figure generation stays under the corresponding figure phase.
- Article writing and final manuscript assembly are deferred to a later step and
  are not part of the first-pass stage planning chain.

## Top-Level Phase Design

### Figure 1 Phase

- Purpose:
  define benchmark framing, lawful comparison scope, object boundaries, and the
  benchmark workflow narrative.
- Included support steps:
  inventory, eligibility boundary, scope control, validation boundary, and other
  upstream analysis objects that are closest to benchmark definition.
- Excluded from this phase:
  final manuscript writing.

### Figure 2 Phase

- Purpose:
  define the full `Task1` evidence chain that supports `Figure 2`.
- Included support steps:
  all upstream preparation, matching, metric computation, retrieval logic,
  summary assembly, and panel-ready object generation needed for `2A-2F`.
- Included rendering steps:
  R-based panel generation for `Figure 2`.

### Figure 3 Phase

- Purpose:
  define the full `Task2` evidence chain that supports `Figure 3`.
- Included support steps:
  cohort build, group concordance, retrieval, synthesis, panel-ready object
  generation, and local `FM` handling for `3A-3F`.
- Included rendering steps:
  R-based panel generation for `Figure 3`.
- Special rule:
  `FM` is treated as a local `Figure 3` sub-chain only and remains restricted to
  the approved `scPerturb/K562` `3F` scope.

## Stage Dossier Fields

Each later discussion unit should be organized as one stage dossier. The working
representation does not need to be a table, but each dossier should answer the
same fields:

- `stage_name`
- `manuscript_anchor`
- `analysis_purpose`
- `support_steps`
- `current_evidence`
- `target_scripts`
- `target_outputs`
- `authoritative_docs`
- `freeze_items`
- `gaps`

## Discussion Order

The default order for later confirmation is:

1. `Figure 1` phase
2. `Figure 2` phase
3. `Figure 3` phase
4. legacy crosswalk from historical `S0-S7` into the new manuscript-anchored
   framework

The legacy crosswalk is a secondary step. Historical stage identifiers can be
kept for reference, but they are not the canonical planning structure for the
current redesign discussion.

## Planning Constraints

- The framework must remain consistent with the benchmark split between `Task1`
  and `Task2`.
- `FM` must remain local to `Figure 3F`.
- The framework must support real analysis steps even when those steps are not
  described explicitly in manuscript-facing prose.
- Missing scripts or missing intermediate planning documents are treated as
  expected gaps to be designed, not as evidence that the phase should be
  removed.
- This document is temporary and may be rewritten as freeze decisions become
  more specific.

## Immediate Next Step

The next discussion starts from the `Figure 1` phase and should first confirm:

- the scientific boundary of the phase
- the support steps that belong under it
- the expected script responsibilities
- the authoritative documents that will control later freeze decisions

# Documentation Architecture Decision

Date: 2026-09-06

Status: approved architecture; implementation and verification are recorded in
[the changelog](../CHANGELOG.md).

## Decision

The human lead approved organizing the documentation by research questions and
method responsibilities rather than by figure-numbered phases. The lead also
approved combining analysis with tasks, keeping the project definition and
research roadmap at the documentation root, and publishing the migration to
GitHub after checks.

The root contains `README.md`, `project.md`, and `roadmap.md`. The seven domains
are `tasks`, `data`, `metrics`, `visualization`, `manuscript`, `governance`, and
`history`. Figure numbers remain manuscript assignments, not method ownership.

## Preserved Baseline

The migration uses the local working documents, including their existing
uncommitted Task1 preparation refinements, rather than replacing them with the
older published checkout. Task1 and Task2 remain separate. The manuscript FM
scope remains the scPerturb/K562 Figure 3F panel; upstream Task1 FM preparation
does not authorize FM in Figure 2.

This change does not modify benchmark units, metrics, denominators, active model
families, data or run roots, artifact names, or published figure meanings.
Unresolved statistical and implementation choices remain unresolved.

The previous state summary described `S0` to `S7` as an audited stage chain
without per-run evidence in that summary. It is retained as an execution
crosswalk rather than a certification of completion. Project metadata now
points to state instead of independently repeating a completion claim. This
migration does not reassess the validity of historical runs.

## Plan And Content Crosswalk

| Previous owner | Successor and retained responsibility |
| --- | --- |
| `docs/redesign_checkpoint.md` | Root project and navigation; object model, task definitions, metrics, execution crosswalk, and figure contracts move to their domain owners |
| `docs/contracts/project-positioning.md` | `docs/project.md`; reporting requirements also inform the writing standards |
| `docs/data_contracts.md` | Root navigation, data object definitions, and storage policy |
| `docs/contracts/task1_spec.md`, `task2_spec.md` | `docs/tasks/task1.md`, `task2.md`; task definitions and task-specific analysis requirements |
| `docs/contracts/output-schemas.md`, `audit-protocol.md` | `docs/tasks/output_schemas.md`, `validation.md`; all existing output fields and audit gates |
| `docs/contracts/figure2_phase/01_task1_lincs_prep.md`, `02_task1_scperturb_prep.md` | `docs/data/preprocessing/lincs.md`, `scperturb.md`; source-specific preparation and exceptions |
| `docs/contracts/figure2_phase/03_shared_pathway_contract.md`, `06_task1_scperturb_fm_contract.md` | `docs/data/representations/pathway.md`, `fm.md`; scoped representation construction and acceptance |
| `docs/contracts/figure2_phase/04_task1_data_snapshot_contract.md` | `docs/data/snapshots/task1.md`; source bundles, registries, and snapshot interfaces |
| `docs/contracts/figure2_phase/README.md`, `pending_items.md` | Active requirements retain their domain owners; unresolved work is indexed in state; the superseded checkpoint and pending registry are archived |
| `docs/contracts/figure1_phase/README.md` | Benchmark overview visual design and manuscript legend draft, with open design questions retained |
| `docs/plotting/plotting_preparation_freeze.md` | Visual standards, figure plan, and per-figure specifications |
| `docs/plotting/manuscript_figure_legends.md` | `docs/manuscript/figure_legends.md` |
| `docs/manuscript_master.md` | Project definition, manuscript outline, figure plan, and writing requirements |
| `docs/governance/repo_conventions.md`, `local_storage_policy.md`, `team-and-governance.md` | Documentation policy, storage policy, and collaboration respectively |
| `docs/governance/state.md`, `runbook.md` | Same operational responsibilities, with canonical references updated |
| `docs/tmp_stage_planning_freeze.md` | Archived figure-anchored planning; this decision replaces its organizing principle |

## Execution And Confirmation

1. Preserve a pre-migration working-tree snapshot and identify staged work.
   Confirm: existing implementation edits remain distinguishable from this
   migration, and the remote branch is checked before publication.
2. Move and consolidate documents by their domain responsibilities.
   Confirm: every active requirement has a successor; retired material is
   historical rather than a second active contract.
3. Update entry documents, repository skills, and executable documentation
   references.
   Confirm: the FM parser still reads the same active family section and list;
   project-root discovery uses the new project document.
4. Check architecture, links, contract preservation, and targeted tests.
   Confirm: independent review findings are resolved or explicitly reported.
5. Stage only the documentation migration and its tracked reference/check
   changes, then commit and push without force.
   Confirm: existing extractor edits and unpublished local Task1 implementation
   files are not included, and the remote branch contains the new commit.

## Review Constraints

- Scientific rigor: move approved rules without introducing new estimators,
  analysis approvals, or claims of completed experiments.
- Redundancy: formal rules have domain owners; entry documents and status pages
  link to them rather than independently redefining them.
- Conflicts: preserve scoped exceptions and report pre-existing disagreements;
  moving a Task1 document does not make its rules benchmark-wide.
- Engineering: Markdown paths and the active-FM heading are runtime interfaces.
  Update local consumers without publishing unrelated implementation work.
- Integration review also identified the legacy document path in `project.yaml`
  and the `data/` Git ignore rule hiding `docs/data/`. Update the metadata and
  exempt only the documentation directory while retaining artifact exclusions.
- Evidence: keep historical NAS manifests unchanged; their recorded old paths
  describe the inputs used at the time.

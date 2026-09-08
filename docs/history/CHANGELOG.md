# Research And Documentation Changelog

This file records substantive changes and their verification boundaries. Git retains line-level changes; decision records explain why changes were made; NAS-backed runs retain experiment evidence.

## 2026-09-08: PerturbLens Scientific Reframing

The human lead approved reframing the project from the Task1/Task2-centered M2M-Bench benchmark into **PerturbLens**, a response-centric characterization study of perturbation-response information across biological boundaries.

See [the decision](decisions/2026-09-08_perturblens_reframing.md), [project definition](../project.md), [research proposal](../research/proposal.md), [landscape](../research/landscape.md), and [result architecture](../research/result_architecture.md).

The reframing introduces:

- R1-R6 manuscript/result architecture;
- `docs/research/` as a research-rationale domain;
- Gene/Pathway/FM and CellProfiler/deep morphology state-representation families;
- control-delta and Systema-style response views;
- population similarity, retrieval, and prediction as complementary evidence levels;
- a staged legacy Task1/Task2 crosswalk rather than in-place reinterpretation.

Scientific naming changes before code/storage naming. Existing `M2M-Bench`, `m2mbench`, `task1_*`, `task2_*`, and NAS `M2M` identifiers remain for provenance and compatibility until separately migrated.

### Verification boundary

This change is documentation/scientific architecture only. It does not certify new model runs, morphology ingestion, VCC2026 metric implementation, new generalization splits, expanded FM scope, combination analyses, or manuscript results.

## 2026-09-06: Domain-Based Documentation Migration

The human lead approved replacing figure-numbered document ownership with three root entry documents and seven domains. Analysis is part of tasks, and the research roadmap is a root document. See the [architecture decision](decisions/2026-09-06_documentation_architecture.md) for the content crosswalk, preservation requirements, and check sequence.

The migration carries forward current local Task1 data-preparation contracts without adding datasets, tasks, numerical defaults, or FM manuscript scope. Superseded planning/checkpoint records are retained under `archive/`.

## Migration Verification

- The local architecture and source-smoke checks passed: `7 passed` for `tests/test_documentation_architecture.py` and `tests/test_repo_smoke.py`.
- The same seven checks passed in a separate staged-file preview, without the unpublished local Task1 implementation files.
- The local `OSMOSIS_V2` FM contract tests passed: `84 passed`, with one existing AnnData index-conversion warning. These tests exercise local implementation compatibility and do not certify a benchmark run.
- The actual FM contract parser reads the preserved active family list, and project-root discovery succeeds with `docs/project.md`.
- The new architecture test passes the configured Ruff lint and formatting checks. It covers root/domain layout, current document paths, local links, project metadata references, and the machine-readable active-FM section.
- A pre-migration comparison of all 19 existing Python files found only the intended documentation-path substitutions in five local Task1 scripts and one local test. Existing extractor implementation changes were preserved.
- Independent review found no drift in task separation, FM manuscript scope, audited-only S7 inputs, preprocessing rules, or retained figure design and legend content. Review findings on metadata, archived navigation, ignored data documentation, and trailing whitespace were addressed.
- Review also identified an inherited Task1 group-table key ambiguity: `cell_line` is part of the task unit but absent from the listed table key. This is recorded as pending in state; the migration does not alter the schema.

## Publication Scope

The release contains the domain documents, entry and skill references, project metadata alignment, the narrowly scoped `docs/data/` ignore exception, and the architecture regression test. Existing extractor changes and unpublished Task1 implementation files are excluded from the commit. Historical NAS artifacts are not moved or rewritten, and no benchmark or model-extraction run is performed by this migration.

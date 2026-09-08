# PerturbLens Data Contracts

## Pre-screening architecture freeze

Contract version: `perturblens-data-v1`. Effective date: 2026-09-08.

This is the normative design for new data intake and builds. It does not certify
an implemented pipeline, a migrated NAS tree, or an eligible dataset. Existing
assets enter through intake and explicit revalidation; renaming a directory does
not promote historical outputs into current evidence.

The four scientific layers remain data, state representation, response
construction, and biological relation/evaluation. Catalog, intake, and relations
are supporting data infrastructure, not additional main results.

## Contract owners

| Contract | Owner | Defines |
| --- | --- | --- |
| Storage architecture | [Architecture](architecture.md) | NAS layout, retention, versions and localization |
| Canonical objects and metadata | [Object model](object_model.md) | IDs, observations, experimental units, conditions, controls and covariates |
| Global catalog and entities | [Catalog](catalog.md) | Sources, datasets, artifacts, aliases and target evidence |
| Source screening | [Intake](intake.md) | Discovery, inventories, schema mapping and decision records |
| Task eligibility | [Eligibility](eligibility.md) | Coverage, status, reasons and task-specific entry gates |
| Common artifact envelope | [Manifests](manifests.md) | Lineage, fit scope, status, integrity and registration |
| Logical matrices | [Matrix semantics](matrix_semantics.md) | Row/feature alignment, values, storage formats and transformations |
| Shared biological relations | [Relations](relations.md) | R4/R5 links, combination membership and matching evidence |
| Response construction | [Responses](response_construction.md) | Delta/Systema references, scope and reuse |
| End-to-end processing | [Workflow](workflow.md) | Stage order, authorization boundaries and acceptance checks |
| Source-specific processing | [Sources](sources.md), [preprocessing](preprocessing/) | LINCS, scPerturb and morphology adaptations |
| State representations | [Representations](representations/) | Gene, Pathway, FM, CellProfiler and DeepMorphology |

The [storage policy](../governance/storage_policy.md) owns allowed roots. Task
contracts own scientific matching, split rules and permitted model inputs; data
contracts persist those rules and their evidence rather than replace them.
The [runbook](../governance/runbook.md), [result schemas](../tasks/output_schemas.md)
and [validation contract](../tasks/validation.md) continue to apply.

## Frozen boundaries

- Screening stops at intake and eligibility; no outcome-based source selection.
- Expression profiles, images, treatment/control metadata and source provenance
  form the preservation base. Source-native does not mean unprocessed counts.
- Traceable CellProfiler profiles and FM/deep-image state embeddings are reusable
  assets worth retaining; their reuse is conditional on matrix and fit semantics.
- Observations are not automatically independent experimental replicates.
- Exact experimental identity is separate from task-specific matching keys.
- Target sets are derived views of evidence-bearing target edges.
- Source-global Delta and task/split-specific SystemaResidual have different reuse
  boundaries. A directory name never establishes leakage-free reuse.
- A contract freeze is not an instruction to delete, move, download or run data.

## Changes and open decisions

Changes to field meaning, IDs, allowed values or required gates require a new
contract version and explicit compatibility mapping. Each build pins the relevant
contract files and versions; additive optional columns must be documented.

Source-specific normalization, confidence mapping, matching tolerances, minimum
support, model/checkpoint choice, Systema pools and allowed test-context controls
must be resolved in their owning source/task specifications before the affected
build. No universal numerical defaults are introduced by this freeze.

## Supplied proposal coverage

| Proposal requirement | Frozen owner |
| --- | --- |
| 1. Full NAS layout | Architecture: catalog/intake/sources/prepared/states/relations/responses/splits |
| 2. Global catalog | Catalog: source, dataset, artifact and entity registries |
| 3. Evidence-bearing target edges | Catalog: target-edge schema and target-set projection |
| 4. Experimental units | Object model: observations, units, aggregation and independence |
| 5. Exact condition versus matching keys | Object model and relations: separate identities and task projections |
| 6. Explicit controls | Object model: source control candidates versus selected response references |
| 7. Response reuse scope | Response construction: source/task/split scopes and legal reference membership |
| 8. Shared R4/R5/R6 relations | Relations: target links, readout matches and constituent/single links |
| 9. Intake artifacts | Intake: inventory, mapping, metadata profile, coverage and report |
| 10. Intake/prepared separation | Intake and workflow: selection without downstream outcome access |
| 11. Common artifact manifest | Manifests: envelope, lineage, integrity, status and fit scope |
| 12. Artifact registry and fixed versions | Catalog and architecture: snapshots, immutable IDs, no scientific latest |
| 13. Logical rather than single physical matrix format | Matrix semantics: shape, row/feature index, partitions and formats |
| 14. Matrix value semantics | Matrix semantics: counts/signatures/normalized states/responses remain distinct |
| 15. Raw and standardized time/dose | Object model: units, conversion status, mol/L and missingness |
| 16. Eight pre-screening contracts | Contract-owner table in this index |
| 17. Full data lifecycle | Workflow: stage gates and split-before-fit dependency refinement |

Two compatibility details are explicit: the proposal's `same_assay_paired` maps
to existing `paired_assay`, and split-dependent fitting/reference construction
occurs after split freezing even though responses precede evaluation in the
logical architecture. No existing metric formula or R1-R6 result scope changes.

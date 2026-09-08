# Frozen Data Processing Workflow

Version: `perturblens-data-v1`. This workflow specifies required behavior and
acceptance gates; it is not a claim that the corresponding automation exists.
No data operations are authorized merely by publishing this document.

## Lifecycle and ordering

```text
Discovery -> Intake -> Eligibility/Decision -> Source localization/registration
  -> Prepared identity + task-independent QC
      -> Relations from metadata and catalog
      -> Fixed/task-independent States -> lawful source-global Responses
      -> Frozen Split membership from conditions/entities/independent units
          -> train/control/split-specific preprocessing and States
          -> task/split-specific References and Responses
  -> Run -> Validated outputs -> Artifacts/manuscript
```

The logical objects remain source -> prepared -> state -> response -> split/run.
Execution respects dependencies: split definitions precede any split-dependent
fit/reference, not necessarily every fixed source-global response. Relations can
be built alongside states once metadata identity is resolved. Neither task
eligibility nor initial split assignment uses downstream performance.

## Stage contracts and observable gates

| Stage | Inputs and required actions | Output / acceptance gate |
| --- | --- | --- |
| Discovery | Record source/release, location, owner and access terms | Candidate registry; known versus unverified locations distinguished |
| Intake | Inventory files; inspect metadata/headers; map fields; count support | Complete intake bundle; raw values, missingness, inspection limits and denominators retained |
| Eligibility/decision | Apply frozen task-specific rules; identify partial scopes and blockers | Versioned eligibility rows and include/defer/exclude decision; no outcome-based screening |
| Localization | Authorized copy or register external immutable source; verify payload identity | Source manifest/files, source-faithful metadata, readable payloads, integrity/access evidence |
| Prepared identity/QC | Canonicalize entities/units, preserve controls/covariates, apply declared source QC | Prep manifest, metadata, matrices, QC/exclusion tables and post-QC support reassessment |
| Relations | Freeze target edges, matching tiers, compatibility and constituent singles | Relation tables with resolved endpoints, rules, candidate counts and rejected links |
| Split freeze | Assign independent units and held-out axes using metadata; declare model/control access | Immutable membership, leakage checks, pinned catalog/relations and seed |
| Fitted processing/states | Fit only permitted data; build/adopt Gene/Pathway/FM/CP/deep states | Matrix/fit semantics, exact row/feature alignment, model/pipeline lineage and coverage |
| Responses | Select legal controls/perturbed pools at declared scope; aggregate and subtract | Response manifest, exact references/weights, scope binding and response-integrity checks |
| Run | Use permitted inputs, frozen metric/model versions and baselines | Runbook bundle, per-unit outputs, all applicable task assertions pass |
| Export | Select validated result tables without recalculating scientific quantities | Plot-ready/artifact/manuscript lineage to validated runs |

Each stage references immutable input artifacts and contracts. Promotion requires
its own gates and passed upstream gates for that intended use. An `eligible`
intake does not override a failed post-QC gate; retain the failure and revise
scope through a new recorded decision. Null/negative scientific findings do not
justify changing inclusion rules. Retry failed builds under new IDs, retaining
diagnostic lineage without treating partial files as complete assets.

## Prepared build details

Before implementing a source adapter, its appendix under `docs/data/preprocessing/`
must specify source/release/dataset scope, source field mapping, treatment/control
labels, unit hierarchy, inclusion/QC rules, expression or image semantics,
time/dose parsing, feature mapping, normalization and fit scope, output schemas,
precomputed-asset adoption rules, expected validation gates and unresolved uses.
Any task-dependent minimum support, matching tolerance or null is referenced from
the owning task rule rather than guessed by the adapter. Required unresolved
settings block the affected stage; optional unavailable modalities remain explicit.

`metadata/` contains canonical observation, experimental-unit, condition,
perturbation and control tables. Retain source-row mappings and entity mapping
versions; unresolved fields remain explicit. `qc/exclusions.parquet` has
`object_type`, `object_id`, `rule_id`, `reason_code`, `evidence_path` and
`stage`; `qc/support.parquet` reuses the coverage schema on retained units.

Source-independent QC may precede splits only when it does not estimate a
transformation from forbidden test outcomes. Feature filtering, plate correction,
normalization and aggregation record fit scope even when conventionally called
preprocessing. Train-fitted operations create split-bound prep/state builds;
do not reuse globally fitted values for a strict held-out claim by relabeling.

## Modality-specific processing

### Transcriptomics

1. Preserve source expression/signature files, gene indices and original metadata.
2. Resolve organism, intervention/reagent/compound identity, context, blocks,
   independent units, treatment/control types and time/dose without inference.
3. Inspect matrix semantics and preserve counts/source-normalized layers; apply
   [scPerturb](preprocessing/scperturb.md) or [LINCS](preprocessing/lincs.md)
   inclusion and mapping rules with exclusions.
4. Materialize canonical matrix indices and versioned prepared states; do not
   select per-cell controls or create Delta at source-preparation time.
5. Build Gene/Pathway and the predeclared FM panel only when model input semantics
   match the source; source signatures are not automatically valid count inputs.
6. Build responses under their scope and task; preserve source-native reference
   limitations for LINCS instead of creating synthetic controls.

### Cellular morphology

1. Preserve images and acquisition index, treated/control metadata, channel and
   plate/well/field identity. Resolve availability separately for precomputed
   profiles, images and any existing embeddings.
2. Validate source-specific imaging/segmentation/QC rules under the
   [morphology contract](preprocessing/morphology.md). Record failed wells/cells,
   finite/invariant features and the control-anchored normalization specification.
3. Adopt a traceable external CellProfiler profile build or execute a versioned
   pipeline after authorization; retain cell/well aggregation and raw versus
   normalized feature semantics. Avoid recomputation solely for directory naming.
4. Adopt or extract DeepMorphology states with checkpoint/channel/crop/pooling
   lineage. Raw images are required for re-extraction, not presumed from parquet.
5. Fit transformations only on lawful data and construct morphology references
   within its feature space. Preserve cell/image-to-well membership and repeats.
6. Build RNA/morphology links using independent metadata evidence. The same
   perturbation label is not proof of time/dose/context pairing or direct causality.

### Organoid extension

Organoid is an experimental-system/context descriptor, not another readout.
Preserve donor, organoid line, tissue/cell type, culture model, sample/well,
individual organoid and technical acquisition levels where available. Exposure
time is separate from maturation age. No automatic claim of independent organoids
within one well or donor. An organoid source needs the same intake gates and a
task-specific context/split decision; distributional or spatial response analyses
require an owning-contract extension rather than relabeling centroid Delta.

## Split membership contract

`membership.parquet` has primary key `(fold_id, assignment_unit_id)` with
`split_id`, `assignment_unit_type`, `partition` (`train`, `validation`, `test`),
`condition_ids: list<string>`, `experimental_unit_ids: list<string>`,
`held_out_entity_ids: list<string>`, `rule_id` and `source_trace`.
`fold_id` is explicit even for one fold. The assignment level is frozen according
to the intended claim; dependent observations inherit membership. A separate
`excluded_membership.parquet` records unassigned candidate units and reasons.
Permitted controls/external priors are access rules in the split/model manifest,
not extra training rows that silently leak test perturbations. Repeated cells,
wells, target memberships and combination constituents obey task leakage rules.

## Execution acceptance checklist

- Primary/foreign keys resolve; exact experimental IDs are not task match keys.
- Original units/labels and mapping decisions survive canonicalization.
- Matrix shape, order, missingness, transformations and row level are explicit.
- Independent support, QC losses and exclusions have correct denominators.
- Every fitted operation and reference uses legal, enumerated membership.
- Relation tiers/target evidence and combination singles are auditable.
- Artifact versions, payload identities and validation assertions are registered.
- Run outputs obey existing metric, model, statistical and evidence contracts.

Implementations must test these gates before production use. This documentation
freeze does not implement validators, pin source-specific pipelines or complete
any R2-R6 analysis.

# Eligibility And Screening Contract

Version: `perturblens-data-v1`. This contract stores task admissibility without
replacing the scientific definitions in [task contracts](../tasks/).

## Assessment table

`task_eligibility.parquet` is long-form, not a collection of boolean task columns.
Primary key: `assessment_id`. Required fields:

| Fields | Type | Meaning |
| --- | --- | --- |
| `intake_id`, `source_id`, `release`, `dataset_id` | string | Assessed source scope |
| `task_name`, `result_section`, `split_family`, `scope_id` | string | Exact intended use, not an entire source claim |
| `rule_id`, `task_contract_version` | string | Frozen eligibility rule and authority |
| `status` | enum | `eligible`, `partial`, `blocked`, `excluded` |
| `reason_codes` | list<string> | Empty only when no limiting reason applies |
| `evidence_paths` | list<string> | Inventory/coverage/metadata evidence |
| `n_total_units`, `n_supported_units`, `n_excluded_units`, `n_unresolved_units` | int64? | Counts at named unit level, null if not established |
| `unit_type`, `scope_definition` | string | Unit and machine-readable JSON scope predicate |
| `remaining_requirements`, `eligible_scope` | string? | Conditions and restriction for partial/blocked uses |
| `assessed_at` | UTC timestamp | Assessment time |

`eligible` means the named use passes the specified metadata/design gates, not
that its analysis ran or is powered for every effect. `partial` requires a
concrete supported subset/use and explicitly restricted scope. `blocked` means
unresolved evidence or an unfrozen required rule prevents a decision. `excluded`
means available evidence fails the named rule. Do not mark a missing numerical
support threshold as eligible; freeze it before assessment. No universal minimum
replicate, target or context count is imposed here.

For established counts, total equals supported plus excluded plus unresolved.
Counts of cells, wells, targets and datasets have separate denominators. Reassess
actual QC-retained support before execution; structural intake eligibility is
not final post-QC authorization. Do not revise inclusion based on model scores.

## Task IDs and gate matrix

| `task_name` / section | `split_family` | Required design evidence |
| --- | --- | --- |
| `r2_genetic` / R2 | `genetic_inner` | Single-target genetic identity/mode, controls or lawful source-native effect, independent replicate/reagent/source support |
| `r2_genetic` / R2 | `genetic_unseen_context` | Context identities and sufficient cross-context target overlap under the approved split; allowed held-out controls declared |
| `r2_genetic` / R2 | `genetic_unseen_target` | Disjoint target identities and permitted external input information |
| `r3_chemical` / R3 | `chemical_inner` | Compound identities, references and independent repeat support |
| `r3_chemical` / R3 | `chemical_unseen_context` | Context-held-out support and lawful control access |
| `r3_chemical` / R3 | `chemical_unseen_compound_known_target` | Held-out compounds and known-target overlap through permitted training information |
| `r3_chemical` / R3 | `chemical_unseen_target` | Frozen target edges and exclusion of all compounds with prohibited target memberships |
| `r4_cross_intervention` / R4 | `not_applicable` for measured concordance; named split for translation | Matched context and target evidence, eligible genetic direction/mode, compatible responses and internal-support linkage |
| `r5_cross_readout` / R5 | `not_applicable` for measured concordance; named split for prediction | Documented matching tier and condition agreement, both readouts, repeat support, declared representation availability |
| `r6_combination` / R6 | `both_constituents_seen`, `one_constituent_unseen`, `both_constituents_unseen`, or `not_applicable` for measured residuals | Constituents, compatible singles/controls, dose/time/strength, repeats and response-scale-appropriate null |

Named R4/R5 prediction splits must be defined by their task before use; this
document does not invent them. R1 is framework/intake characterization, not a
separate prediction task. A single source can support one task and fail another.
Cross-source matches require explicit inventories on both sides; label overlap
alone cannot establish a condition-matched cohort.

## Reason codes

| Code | Meaning |
| --- | --- |
| `NO_CONTROL` | Required controls/reference semantics absent; source-native effects assessed under their source contract |
| `NO_REPLICATE` | Required independent repeat support absent |
| `SINGLE_CONTEXT` | Requested unseen-context use has only one supported context |
| `NO_TARGET_MAPPING` | Required target identity/evidence missing |
| `NO_SINGLE_CONSTITUENTS` | Compatible measured singles unavailable |
| `NO_MODALITY_MATCH` | No lawful counterpart for requested cross-readout use |
| `TIME_DOSE_UNUSABLE` | Required time/dose compatibility cannot be established |
| `IDENTITY_AMBIGUOUS` | Required source-to-entity mapping unresolved |
| `INSUFFICIENT_SUPPORT` | Frozen support rule fails within the requested scope |
| `RULE_NOT_FROZEN` | Matching, split, null, input or support rule not approved |
| `NO_IMAGE_ACCESS` | Images unavailable for an image-dependent use; profiles may have narrower eligibility |
| `PROVENANCE_INCOMPLETE` | Required source/build/processing evidence missing |
| `ACCESS_UNRESOLVED` | Required access or usage rights unresolved |
| `OUT_OF_SCOPE` | Organism, intervention, readout or intended claim outside current approved scope |

Multiple reasons are allowed; record the evidence for each. Time/dose missingness
does not exclude every task automatically, and absent images do not invalidate a
documented profile-only analysis. Scope restrictions must be explicit.

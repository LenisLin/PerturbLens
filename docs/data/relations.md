# Shared Relation And Matching Schema

Version: `perturblens-data-v1`. Relations persist biological links and their
evidence outside task scripts. [R4](../tasks/cross_intervention.md),
[R5](../tasks/cross_readout.md) and [R6](../tasks/combination.md) own lawful
comparisons and claims. A reusable relation table is not unrestricted task
eligibility.

## Common relation build

`relation_manifest.json` extends the common envelope with `relation_build_id`,
catalog/source/prep IDs, `target_membership_rule_id`, applicable `task_names`,
`matching_rule_id`, rules/tolerances, annotation confidence policy, unit level,
candidate-universe definition and exclusion counts. Split-conditioned relations
also pin `split_id` and fold. Relations can be built from metadata before states;
no response score may decide whether a source/match enters a confirmatory cohort.

All link tables retain `link_id` (primary key), `relation_build_id`, `rule_id`,
`eligibility` (`eligible`, `partial`, `blocked`, `excluded`),
`exclusion_reason: list<string>`, `evidence_paths: list<string>` and exact endpoint
IDs. Include rejected candidate links from the declared candidate universe and
their reasons; do not materialize every unrelated pair across whole atlases.
Count unknown/unassessed pairs separately from failed matches.

## Target membership

`target_membership.parquet` records `(perturbation_entity_id, target_id, edge_id)`
with rule/build IDs, inclusion boolean and exclusion reasons. It is required when
a relation/task projects catalog target edges into a target set. Multi-target
compounds keep one compound identity and multiple edge memberships; these rows
are not independent compound replicates. R3 exclusion of held-out targets must
use the same pinned membership rule, including multi-target compounds.

## Cross-intervention links

`cross_intervention_links.parquet` adds:

| Fields | Type | Meaning |
| --- | --- | --- |
| `chem_condition_id`, `genetic_condition_id` | string | Exact chemical/genetic endpoints |
| `target_id`, `cell_context_id`, `cell_context` | string | Anchor target and matched canonical context |
| `genetic_mode` | string | Preserved mode, e.g. CRISPRi versus ORF |
| `target_evidence` | list<string> | Selected target-edge IDs for both endpoints |
| `time_relation`, `dose_relation` | enum | `exact`, `compatible`, `incompatible`, `unknown`, `not_applicable` |
| `comparison_key` | string | Versioned task projection, not a replacement condition ID |

Chemical dose and genetic strength are not assumed to share a numerical scale.
Direction compatibility is explicit: inhibition and overexpression are not
automatically equivalent perturbations. A lawful target/context match still
requires compatible readout/state/response definitions and internal-support
linkage for interpretation. Internal-support measurement is downstream and cannot
be fabricated by the metadata link table.

## Cross-readout links

`cross_readout_links.parquet` adds `rna_condition_id`, `morph_condition_id`,
`rna_unit_id?`, `morph_unit_id?`, `pairing_id?`, `comparison_key`,
`same_perturbation`, `same_target`, `same_context`, `time_match`, `dose_match`,
`match_tier`, `pairing_evidence`, `target_evidence` and compatibility-rule ID.
Endpoint unit IDs are required when direct pairing is at unit rather than
condition level. Agreement flags are nullable booleans: null is unknown, not
agreement. Time/dose tolerances and target-overlap rule are predeclared in the
manifest; missing values never satisfy an exact match.

Canonical `match_tier` values preserve the existing R5 contract:

| Value | Evidence requirement |
| --- | --- |
| `paired_assay` | Documented direct pairing in the same experimental system; declare whether sample/well/condition pairing, not necessarily the same physical cell |
| `condition_matched` | Same perturbation and context with documented compatible time/dose in independent experiments |
| `label_matched` | Perturbation or target annotation agrees but full experimental matching is absent |

The proposal label `same_assay_paired` maps explicitly to `paired_assay` at intake;
it is not a fourth tier. Source text remains in `match_tier_raw`. A common source
name or publication does not establish direct pairing. Higher-tier labels do not
override recorded mismatches: every analysis applies its compatibility rule.

One-to-many matches are retained with endpoint IDs and task-declared weighting;
duplicating a profile into several links does not increase independent support.
`cross_readout_matching.parquet` in run outputs is the task-selected projection
of this relation table with link/build IDs retained, not a second independent
matching implementation. Profiles-only data and RNA overlap are assessed
separately from the ability to extract image embeddings.

## Combination membership

`combination_membership.parquet` has primary key
`(combination_condition_id, member_index)`. Fields:

- `combination_id`: canonical combination perturbation entity;
- `combination_condition_id`: exact combination condition;
- `member_index`: int64 position, unique within the condition;
- `member_id`: canonical constituent perturbation entity;
- `member_role`: source-described role, or `member` if no distinct role;
- `dose_raw`, `dose_unit_raw`, `dose_value_std`, `dose_unit_std`, `dose_molar`:
  member-specific covariates using the common dose contract;
- `administration_order?`, `strength_raw?`, `stoichiometry?`, `source_trace`,
  `relation_build_id`, `evidence_paths`.

Support two or more known constituents without encoding membership only as a
combined label. Order is only biological administration order when documented;
table row order is not evidence. Three-way combinations need no new table schema.

`combination_single_links.parquet` records `link_id`, `combination_condition_id`,
`member_index`, `single_condition_id`, compatibility-rule ID, time/dose/context
agreement, eligibility and exclusions. It is required for R6 eligibility so that
constituent identity alone is not mistaken for measured compatible singles.
Single and combination controls must be auditable. Null model/scale and residual
interpretation remain in R6; membership does not define synergy or additivity.

## Validation

Validate endpoint and evidence-edge foreign keys, canonical identity, context and
mode constraints, agreement flags, duplicate links, exact unit level, candidate
denominators and exclusion reasons. Reusing a relation build in another task or
split requires a compatibility check, not merely copying its link rows.

# Catalog And Entity Schema

Version: `perturblens-data-v1`. Table conventions and ID rules are defined in the
[object model](object_model.md). Fields below are required and non-null unless
marked `?`. All catalogs are versioned as defined in [architecture](architecture.md).

## Source and dataset registries

`source_registry.parquet`: one row per `(source_id, release)`.

| Fields | Type | Meaning |
| --- | --- | --- |
| `source_id`, `release`, `source_name` | string | Stable source family, version and title |
| `source_locator`, `citation` | string, string? | Provider location and publication/accession |
| `license`, `access_policy`, `custodian` | string? | Recorded terms and preservation contact; null is unresolved |
| `discovery_status` | enum | `candidate`, `included`, `deferred`, `excluded` |
| `source_artifact_id` | string? | Validated source build, absent before localization |
| `intake_artifact_id`, `decision_record` | string? | Latest screened evidence and explicit decision reference |

`dataset_registry.parquet`: one row per `(dataset_id, release)`, with
`source_id`, `dataset_name`, `organism`, `assay`, `readout_modality`,
`intervention_types: list<string>`, `source_trace`, `metadata_status`
(`uninspected`, `partial`, `mapped`), and nullable `source_artifact_id`.
Dataset denotes a source-defined cohort/assay subset, not a new task slice.
Accessions and catalog IDs do not prove eligibility. CPG0016 compound, ORF and
CRISPR subsets retain their source identities and processing versions separately.

## Artifact registry

`artifact_registry.parquet`: one row per immutable `artifact_id`.

| Fields | Type | Meaning |
| --- | --- | --- |
| `artifact_id`, `artifact_type`, `build_id`, `schema_version` | string | Common manifest identity |
| `source_id`, `dataset_id`, `representation` | string? | Null for a cross-source or non-representation artifact |
| `path`, `manifest_path` | string | Bundle and manifest locations |
| `manifest_sha256` | string | Digest of finalized manifest, stored outside that manifest |
| `status` | enum | Common manifest status |
| `created_at` | UTC timestamp | Build creation time |
| `supersedes_artifact_id` | string? | Explicit replacement; does not erase prior identity |

For multi-source artifacts, the manifest lists all source/dataset IDs; a nullable
registry summary must not drop that lineage. Selection of a primary build pins
its ID and declared coverage, not merely the newest timestamp or best score.

## Canonical entities

| Table / primary key | Required fields | Nullable fields |
| --- | --- | --- |
| `cell_contexts` / `cell_context_id` | `preferred_label`, `organism`, `context_type`, `evidence_source` | `cell_line`, `cell_type`, `tissue`, `disease`, `donor_id`, `organoid_line_id`, `culture_model`, `ontology_id` |
| `perturbations` / `perturbation_entity_id` | `entity_type`, `preferred_label`, `evidence_source` | `compound_id`, `reagent_id`, `intervention_mode` |
| `compounds` / `compound_id` | `preferred_label`, `evidence_source` | `source_structure`, `canonical_smiles`, `inchi_key`, `salt_form`, `stereochemistry` |
| `targets` / `target_id` | `organism`, `gene_symbol`, `identifier_namespace`, `identifier_version`, `evidence_source` | `ensembl_gene_id`, `entrez_gene_id` |

All entity fields are strings unless specified otherwise. `context_type` is
`cell_line`, `primary_cell`, `organoid`, `tissue`, or `other`;
`entity_type` is `compound`, `genetic_reagent`, `combination`, or `control`.
Organoid identity fields enable future intake, not a claim of an approved organoid
task or available dataset. Donor, tissue, culture system and cell type must not be
collapsed into a cell-line label. Sensitive donor identifiers must be deidentified.

Source perturbation IDs map to canonical entities; they are not overwritten.
Chemical synonyms, salts and stereoisomers are merged only under a documented
identity policy. A shared target or display name does not prove compound identity.
Genetic reagent identity is distinct from target gene and intervention mode.

## Aliases and unresolved identity

`entity_aliases.parquet`: primary key `alias_id`; fields `entity_type`,
`source_id`, `release`, `namespace`, `alias_raw`, `canonical_entity_id?`,
`mapping_status`, `mapping_method`, `evidence_source`, `evidence_record`,
`mapping_version`. All are strings. `mapping_status` is `resolved`, `ambiguous`,
or `unmapped`; only resolved rows have a canonical entity ID. Conflicting
candidate mappings remain separate evidence records, not an arbitrary first hit.
Task eligibility can be blocked by unresolved identity without excluding unrelated
uses of the same dataset.

## Perturbation-target evidence

`perturbation_target_edges.parquet`: one row per evidence assertion, key `edge_id`.

| Fields | Type | Rule |
| --- | --- | --- |
| `perturbation_entity_id`, `target_id` | string | Foreign keys to canonical entities |
| `relation` | enum | `inhibitor`, `activator`, `binder`, `knockout`, `knockdown`, `overexpression`, `annotated_target`, `other` |
| `direction` | enum | `negative`, `positive`, `unknown` |
| `evidence_source`, `evidence_version`, `evidence_record` | string | Annotation resource and resolvable record |
| `confidence` | enum | `high`, `medium`, `low`, `unknown` |
| `confidence_raw`, `confidence_rule_id` | string? | Source evidence and approved mapping; unknown if no rule |
| `primary_target` | bool? | Null means not established, not false |
| `context_id`, `time_hr`, `dose_molar` | string?, float64?, float64? | Evidence applicability, if actually known |
| `mapping_version` | string | Canonical mapping build |

Conflicting annotations are retained; no inferred direction or confidence from a
gene name, compound label or observed response. A source-specific relation value
can be preserved in `relation_raw` when mapped to `other`.

`target_set` is a sorted, unique list of target IDs projected from selected edges
under `target_membership_rule_id` and a pinned catalog build. It is a convenience
view, never the sole evidence record. Projection records selected and rejected
edge IDs and reasons in the relation build. Unresolved annotation is null; an
empty list is an explicitly established no-target set. Compound identity and
multi-target dependence survive every expansion into anchor-target units.

## Catalog checks

Before publication, validate primary-key uniqueness, foreign-key resolution,
alias ambiguity, target namespace/organism compatibility, evidence references,
artifact manifest alignment and snapshot immutability. A catalog may contain
candidate or unresolved entities; they cannot masquerade as resolved task links.

# Common Artifact Manifest

Version: `perturblens-data-v1`. This is a normative JSON contract, not an existing
runtime validator. It applies to catalog, intake, source, prep, state, relation,
response, split and run artifacts. Type-specific manifests extend this envelope.

## Required envelope

| Field | JSON type | Contract |
| --- | --- | --- |
| `artifact_id`, `artifact_type`, `schema_version`, `build_id` | string | Immutable registered identity; type is `catalog`, `intake`, `source`, `prep`, `state`, `relation`, `response`, `split`, or `run` |
| `created_at` | string | ISO 8601 UTC timestamp |
| `code_commit` | string or null | Exact commit for project processing; null for external builds with an explicit provenance reason |
| `code_dirty`, `code_snapshot` | boolean, object or null | Dirty code requires an archived source/patch path and SHA256, not a commit-only claim |
| `command` | array of strings or null | Actual argv, or null for an external/manual source; never fabricated |
| `environment` | object | Runtime name/version and lock/container digest when available; missing external runtime documented |
| `contracts` | array of objects | Each has `path`, `version`, `sha256` for applied contracts |
| `source_ids`, `dataset_ids` | arrays of strings | Complete source scope; empty for source-independent artifacts |
| `inputs` | array of objects | Registered artifact ID or source-native identity plus path/integrity evidence |
| `parameters`, `parameter_hash` | object, string | Complete effective parameters and their SHA256 |
| `outputs` | array of objects | Payload/table path, SHA256 and size, or a directory inventory reference |
| `shape` | object or null | `n_rows`, `n_features` for a single matrix; null for multi-object/nonmatrix bundles |
| `fit_scope` | string or null | Scope enum below; null only when no estimation/fitting/reference operation occurs |
| `fit_spec` | object or null | Exact fitted membership and access policy; required with non-null fit scope |
| `status` | string | `draft`, `materialized`, `validated`, `failed`, `superseded` |
| `validation` | object | Assertion path, overall status and blocking assertion IDs |
| `provenance_notes` | array of strings | Explicit unknown external provenance or source-native exceptions |

Inputs contain `artifact_id` (nullable only for source-native discovery/import),
`path`, `sha256`, `source_version` and `role`. A null hash during intake is marked
as unverified, not a completed integrity check. Local finalized outputs use
`path`, `sha256`, `size_bytes`, `role`; tables also record `primary_key` and
`table_schema_version`. Relative paths resolve against the containing manifest.
External paths include host/location explicitly without credentials.

## Integrity and finalization

For a finalized source or generated artifact, inventory every payload file with
its size and SHA256. Directory outputs such as Zarr or images may use
`inventory_path`, `inventory_sha256`, `size_bytes` rather than a fictional single
file digest; inventory rows carry per-file hashes. Intake inventories may leave
them null until localization/integrity verification. A provider digest can be
recorded as such but must not be described as a locally computed digest.

Compute parameter hashes from UTF-8 JSON with sorted object keys, compact
separators, finite numbers only and ordered arrays preserved. Hashes identify
bytes/parameters, not scientific validity. Use existing verified integrity records
for unchanged immutable files; no repeated full-data hashing at every read.

The manifest must not contain its own checksum. Write payloads and assertion
records, finalize the manifest, then register its checksum in the catalog.
Assertions likewise do not hash the manifest that references them. Validation
records contain `assertion_id`, `gate`, `status` (`pass`, `fail`, `not_checked`),
`evidence_path`, `expected`, `observed`, `reason`; overall pass requires all
applicable required assertions to pass. Runtime failures remain failed builds.

Draft/materialized status can advance before publication. Once a validated
manifest is registered, it is immutable; supersession is recorded by a new
catalog snapshot and replacement artifact, preserving the original record.
`materialized` means files exist, not passed validation. External assets with
unresolved necessary provenance may be retained as materialized but not promoted
to a validated state for the affected use.

## Fit scope and leakage

| `fit_scope` | Meaning |
| --- | --- |
| `external_pretrained` | Fixed external model/resource; training provenance and known overlap declared |
| `source_global` | Estimated using a declared full source cohort; not automatically safe for held-out evaluation |
| `control_only` | Estimated using explicit controls; permitted held-out-context controls must be declared |
| `train_only` | Fit solely on allowed training membership in a frozen split |
| `evaluation_reference_only` | Evaluation-only reference; cannot become a predictor input or training statistic |
| `split_specific` | Operation has fold/partition-specific lawful memberships beyond a single global fit |

`fit_spec` records `operation`, `task_name?`, `split_id?`, `fold_id?`,
`membership_artifact_id`, `membership_path`, `allowed_partitions`,
`held_out_control_policy`, `external_training_provenance?` and
`leakage_review`. Membership enumerates the units used, not merely a descriptive
label. External pretrained models instead pin the training provenance resource
when enumerated training members are unavailable and record overlap uncertainty.
Such uncertainty must be assessed against the intended claim.

For a multi-step build, `fit_spec.operations` lists each operation's scope and
membership. Do not hide global normalization behind an external-pretrained
encoder label. A split-dependent normalization, feature selection or reference
must wait for split freezing. Fixed deterministic transformations with no fitted
statistics can have null fit scope, with transformations recorded in parameters.

## Type extensions

| Artifact | Additional required information |
| --- | --- |
| Catalog | Snapshot ID, table schema versions and publication lineage |
| Intake | Inspection scope, mappings, coverage, eligibility and decision |
| Source | Release, source-native processing, file inventory, access/license, storage mode and custodian |
| Prep | Mapping/QC/normalization versions, matrix manifests, exclusions and actual retained support |
| State | Representation/model/pipeline version, checkpoint, preprocessing, pooling/layer, matrix manifests and coverage |
| Relation | Rule IDs, catalog/target-edge versions, matching tolerances and exclusions |
| Response | State/relation IDs, response view/scope, reference specification/membership, task/split bindings |
| Split | Task/split family, assignment unit, held-out identities, memberships, seed and allowed inputs |
| Run | Run family, source/response/relation/split/metric/model manifests, seed, outputs and assertions |

This envelope supplements, rather than removes, the separate input, response,
split, metric and model manifests required by the [runbook](../governance/runbook.md).
Run-local dependency manifests may be immutable copies of their registered
manifests with identity and digest preserved; do not rebuild data to satisfy a
run directory layout. Metric/model descriptors keep their owning contracts and
need not be independently registered unless materialized as reusable artifacts.

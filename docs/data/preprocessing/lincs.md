# LINCS Preprocessing Contract

Apply the [frozen workflow](../workflow.md), [object schema](../object_model.md),
[matrix semantics](../matrix_semantics.md) and [manifest](../manifests.md) contracts.
Intake/eligibility precede formal preparation; a source-native Level 5 effect is
not a count matrix or a newly computed PerturbLens response.

## Inputs

Primary files:

- `level5_beta_all_n1201944x12328.gctx`
- `siginfo_beta.txt`
- `cellinfo_beta.txt`
- `geneinfo_beta.txt`

under the LINCS Level 5 beta source root documented in `docs/data/sources.md`.

## Inclusion

Retain source signatures with `qc_pass == 1` for:

- `trt_cp` -> `chemical`
- `trt_xpr` -> `genetic`

Other perturbation families require a separate scope decision.

## Metadata mapping

- `cell_iname` -> `cell_context`
- `sig_id` -> source trace
- `pert_time` -> `time_hr` when parseable
- `pert_idose` -> dose fields when parseable
- source perturbation fields remain preserved for audit

Genetic intervention mode is preserved from LINCS metadata rather than reduced to target identity alone.

## Gene state surface

The retained Level 5 signature is treated as the LINCS source-native perturbational gene-expression state/effect surface. No extra clipping is introduced at ingest. Downstream Gene-space alignment is defined by the Gene representation contract.

## Chemical identity and targets

Chemical perturbation identity remains the compound identity. Target annotations are resolved through the available LINCS compound/repurposing metadata cascade and stored separately as canonical target sets.

A multi-target compound remains one chemical perturbation. Target-linked tasks may create target membership rows without splitting or relabeling the compound itself.

## Time and dose

Time and dose are retained as covariates. They do not become part of perturbation identity. R3 determines whether a comparison requires matched or adjusted time/dose.

## Outputs

The source-preparation bundle must include:

- condition registry;
- Gene matrix and feature index;
- raw-source/audit metadata;
- prep manifest referencing the immutable source manifest;
- exclusion table with reasons.

No task split, Systema reference pool, retrieval gallery, or model input is defined at preprocessing time.

Preserve observations/signatures, experimental-unit aggregation, raw/standardized
time and dose, and compound-to-entity/target-edge mappings. Exported control
candidates are recorded when available; unavailable upstream controls are
documented rather than synthesized. The Gene surface has
`value_type=source_level5_signature`. Any source-native Delta adoption is a
separate response build with upstream reference evidence.

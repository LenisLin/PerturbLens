# PerturbLens Validation Requirements

This contract owns task-result acceptance. The [data workflow](../data/workflow.md)
owns input/build gates; the [evidence index](../governance/evidence_index.md) owns
registration of validated results. Passing one layer does not certify the others.

## Universal gates

### 1. Input integrity

- source hashes/versions exist;
- condition/state/response rows align;
- feature indices match matrices;
- required metadata are present;
- exclusions are explicit.

### 2. Response integrity

- every Delta links to its matched-control reference registry;
- every SystemaResidual links to its perturbed reference registry;
- leave-one-condition-out/reference exclusion is applied where required;
- state representation and response feature axes are unchanged by metric code.

### 3. Split integrity

- held-out contexts/targets/compounds/combinations are absent from forbidden training outcomes;
- allowed external priors are declared;
- repeated cells/wells/replicates do not cross split boundaries when that would leak test outcomes;
- split manifests are immutable and hashed.

### 4. Metric integrity

- metric package/config/version is recorded;
- population/retrieval/prediction metric families are not interchanged;
- retrieval galleries and positives are traceable;
- VCC2026 metrics use the pinned Cell-Eval2 implementation or a tested equivalent;
- morphology variants use their own validated calibration rather than copied transcriptomic numerical anchors.

### 5. Statistical integrity

- inference/resampling level matches the biological claim;
- common-support representation comparisons are paired;
- coverage and exclusions accompany summaries;
- confirmatory multiple testing is controlled as declared.

## R4-specific gates

- target membership is persisted;
- multi-target compound dependence is not treated as independent replication;
- genetic intervention direction/mode eligibility is checked;
- C2G and G2C remain separate.

## R5-specific gates

- matching tier is present for every cross-readout unit;
- condition agreement fields are auditable;
- image-feature normalization is fit without downstream target leakage;
- cross-modal prediction splits are disjoint at the claimed biological boundary.

## R6-specific gates

- constituent singles are available under the declared compatibility rule;
- null model and response scale are versioned;
- residuals are not reported as synergy without a separate synergy definition;
- combination split leakage is checked at constituent identity level.

## Evidence status

A successful process exit or non-empty file is not a passed scientific gate. `validation_assertions.json` records each assertion and outcome.

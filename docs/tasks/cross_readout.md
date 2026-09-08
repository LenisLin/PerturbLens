# R5 Cross-Readout Contract

## Scientific question

Which perturbation-response information is shared between transcriptomic and morphological readouts, and which information is readout-specific?

## Eligible matched units

Every unit records a matching tier:

- `paired_assay`
- `condition_matched`
- `label_matched`

Primary claims prioritize higher matching tiers. Lower tiers may support broader but weaker association claims.

A matched unit preserves perturbation/compound identity, target annotation, intervention type/mode, cell context, time/dose compatibility, source, and replicate support.

Persist reusable links under the [shared relation schema](../data/relations.md).
`same_assay_paired` is an intake alias for canonical `paired_assay`, not a fourth
tier. The task-selected output retains relation/link IDs and applies this task's
compatibility and split rules; a reusable link does not bypass them.

## State representations

Transcriptomics:

- Gene
- Pathway
- frozen primary FM

Morphology:

- CellProfiler
- frozen primary DeepMorphology model

Response views are Delta and, where lawful, paired SystemaResidual views within each readout.

## Analysis families

### Response-strength correspondence

Compare within-readout standardized response strength, not raw cross-space norms.

### Perturbation geometry correspondence

Construct perturbation-by-perturbation similarity matrices separately in transcriptomics and morphology, then compare the relationship structure on matched conditions.

### Cross-modal retrieval

RNA -> morphology and morphology -> RNA retrieval with positives defined by same perturbation, target, or context according to a named retrieval subtask.

### Cross-modal prediction

Predict a post-perturbation response in one readout from the measured response in the other under held-out perturbation/context/target splits. This is distinct from virtual-cell prediction from control+perturbation inputs.

### Intervention x readout interaction

Compare R4 chemical-genetic conservation in transcriptomic and morphological spaces for matched targets/contexts. This is a primary differentiating analysis.

## Claim boundary

Cross-readout association or prediction does not establish direct causal direction between molecular and morphological changes. Readout discordance may reflect biology, timing, assay sensitivity, or experimental mismatch and is interpreted according to matching tier.

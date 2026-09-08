# R2 Genetic Learnability Contract

## Scientific question

What information in genetic perturbation responses remains learnable as the held-out biological novelty increases from repeated/inner settings to unseen cellular contexts and unseen targets?

## Intervention scope

Eligible conditions are single-target genetic perturbations with preserved intervention mode (`CRISPR`, `CRISPRi`, `CRISPRa`, expression, or other approved mode). Multi-target genetic perturbations are excluded from the primary R2 target-generalization analysis and may appear only in an explicit secondary analysis.

## Primary split families

### `genetic_inner`

Perturbation target and cellular context are seen on both sides; independent replicate/reagent or source partitions are used where available. The split unit must be more independent than random cell splitting when the claim concerns perturbation reproducibility.

### `genetic_unseen_context`

Held-out `cell_context` values have no perturbed observations in training. The task contract must state whether control/unperturbed state from the held-out context is allowed as model input.

### `genetic_unseen_target`

Held-out target genes have no perturbation outcomes in training. External target/gene representations are allowed only if fixed independently of test perturbation outcomes and declared in the model manifest.

## Primary response/state views

Transcriptomic primary tracks:

- Gene x Delta
- Pathway x Delta
- one frozen primary FM family x Delta

SystemaResidual is a paired response-view analysis across the same common-support units. Additional FM models are secondary unless predeclared.

## Evaluation families

### Population similarity

Use response similarity among lawful replicate/reagent/context pairs to characterize measured response conservation before model evaluation.

### Retrieval

Where a lawful gallery exists, query one measured response against target-keyed or perturbation-keyed galleries and report MRR/Hit@K/rank with gallery support.

### Prediction

Use the pinned Cell-Eval2/VCC2026 transcriptomic family plus task-appropriate baselines. Prediction outputs remain per condition before aggregation.

## Key explanatory variables

- response strength;
- intervention mode/direction;
- target family/pathway;
- source/experiment;
- representation and response view.

## Primary interpretation

The principal R2 result is not that harder splits score lower. It is which aspects of response information (magnitude, direction, responding genes, pathway/program structure, perturbation identity) remain transferable at each boundary.

## Claim boundary

R2 supports statements about empirical learnability under its declared inputs and source coverage. It does not establish an absolute prediction ceiling or intrinsic biological unpredictability.
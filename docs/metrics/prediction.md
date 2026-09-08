# PerturbLens Prediction Evaluation

## Role

This document owns the project-level prediction-evaluation vocabulary. Task contracts own train/test legality, available input information, baselines, and aggregation units. This document does not define model architectures.

Prediction is the third PerturbLens evidence level after population geometry and retrieval:

```text
population similarity -> response geometry
retrieval             -> response specificity
prediction            -> out-of-sample learnability
```

A high similarity score is not sufficient evidence of prediction, and a high prediction score may still be dominated by shared systematic response unless perturbation specificity is tested.

## VCC2026 / Cell-Eval2 Transcriptomic Metric Family

PerturbLens adopts the conceptual coverage of the 2026 Virtual Cell Challenge metric panel as the primary transcriptomic prediction family.

The current Cell-Eval2 `vcc2026` scored members are:

| Metric | Scientific role |
| --- | --- |
| `pds_cosine` | perturbation discrimination / separability |
| `expr_mse_unbiased_capped_norm` | overall expression-profile error adjusted for sampling noise and calibrated in the VCC2026 specification |
| `de_wilcoxon_direction_fidelity_yield_raw` | whether predicted perturbation-effect directions are correct |
| `de_wilcoxon_direction_reach_raw` | how deeply the ranked response preserves correct directions |
| `de_wilcoxon_sig_jaccard` | overlap of significant responding-gene sets |
| `de_wilcoxon_lfc_nmae` | log-fold-change effect-size accuracy |

Reference implementation/specification: https://github.com/ArcInstitute/cell-eval2

Exact PerturbLens parameterization must be versioned against a frozen Cell-Eval2 specification. Metric aliases must not be mixed across versions without provenance.

## Transcriptomic Interpretation Groups

The six metrics should not be treated as six arbitrary leaderboard numbers. They cover five response-information families:

1. **identity/specificity** — PDS;
2. **global profile accuracy** — expression error;
3. **direction** — direction fidelity and reach;
4. **responding-feature identity** — significant-set overlap;
5. **effect magnitude** — log-fold-change error.

Result sections should ask which information family fails under a harder biological boundary.

## Calibration And Anchors

VCC2026 uses baseline/replicate anchoring so that scores can be interpreted relative to a simple baseline and experimental-reference reproducibility.

PerturbLens may adopt analogous calibration where legal, but must record:

- the exact baseline;
- the exact replicate/reference anchor;
- whether calibration is per dataset/context/representation;
- direction of better performance;
- clipping or normalization rules.

A normalized value of `1` is an empirical reference anchor, not a mathematical ceiling. A value of `0` is baseline-relative, not biological absence of information.

## Morphology Prediction Analogues

Morphology requires conceptually matched rather than mechanically copied metrics.

### CellProfiler Feature Space

Candidate primary family:

#### Morphology perturbation discrimination

Rank the predicted morphology profile against measured perturbation profiles using cosine or another approved morphology distance.

#### Morphology profile error

Compare predicted and measured control-normalized morphology feature profiles using MSE/MAE or a covariance-aware error if justified.

#### Morphology direction fidelity

For each interpretable feature with a declared response direction, quantify whether predicted and measured effects share the sign/direction.

#### Morphology direction reach

Rank morphology features by observed or predicted effect strength under a frozen rule and quantify how deep correct directionality is retained.

#### Morphology significant-feature overlap

Compare sets of features declared responsive under an approved replicate-aware test. This metric requires a morphology inference contract; it must not be implemented by arbitrary thresholding.

#### Morphology effect-size error

Compare standardized or scale-appropriate feature-level effects. Raw features with incompatible units must not be averaged without normalization.

### Deep Morphology Embedding Space

Arbitrary latent dimensions are not assumed to have stable feature identity. Primary metrics should therefore emphasize:

- embedding profile error/distance;
- perturbation discrimination;
- same-perturbation/target retrieval;
- distributional agreement where object-level embeddings are retained.

Feature-significance Jaccard and direction metrics are secondary diagnostics unless the embedding coordinates have an explicit stable interpretation.

## Prediction Task Inputs

Every prediction task must specify exactly what information is available at inference.

Examples:

### Genetic unseen context

Possible allowed inputs:

- unperturbed state of the held-out context;
- target identity and approved external target representation.

The held-out context's perturbed responses must not leak into training or calibration.

### Genetic unseen target

One-hot target IDs cannot support true target extrapolation. A model evaluated on unseen targets must use target information available independently of the held-out perturbation responses, such as sequence or approved functional/network features.

### Chemical unseen compound / seen target

Allowed perturbation inputs may include molecular structure and independently sourced target annotation. Response evidence for the held-out compound is excluded.

### Chemical unseen target

Target-level response data for that target must be excluded according to the task contract. This is stricter than unseen compound.

### Cross-modal prediction

Two distinct tasks must not be conflated:

1. `observed post-perturbation readout A -> post-perturbation readout B`;
2. `control + perturbation information -> both post-perturbation readouts`.

The first measures cross-readout information. The second is de novo virtual-cell prediction.

### Combination prediction

The model must be compared against strong constituent-based baselines. The task must record whether zero, one, or both constituent singles were observed during training.

## Baseline Families

At minimum consider, where lawful:

- no-change/control baseline;
- mean perturbed response;
- target/compound mean response;
- nearest-neighbor response;
- simple linear/ridge model;
- matching-mean/additive combination baseline;
- complex/foundation-model predictor.

A baseline is part of the scientific estimand. It defines what additional information the model is claimed to recover.

## Aggregation

Do not silently pool across:

- datasets;
- cellular contexts;
- perturbation types;
- target novelty regimes;
- representations;
- response views;
- readout modalities.

Macro/micro averaging, weighting, missing-query handling, and confidence intervals belong in each task analysis contract.

## Required Prediction Output Context

Every prediction summary should preserve or be traceable to:

- task/generalization regime;
- dataset/source;
- cellular context;
- perturbation/target/compound identity;
- intervention type;
- readout modality;
- state representation;
- response view;
- model/baseline identity and version;
- allowed inference information;
- metric name/version;
- denominator and exclusion fields;
- train/test split manifest;
- calibration/anchor information if used.

## Pending Decisions

Before production implementation, freeze:

- exact Cell-Eval2 commit/version and metric parameters;
- baseline/replicate anchoring strategy outside VCC data;
- morphology feature significance testing;
- morphology feature normalization and metric formulas;
- deep morphology embedding metric family;
- confidence intervals and multiple-comparison strategy;
- model inclusion policy for R2/R3/R5/R6.

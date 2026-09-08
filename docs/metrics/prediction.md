# Model Prediction Evaluation

## Purpose

Prediction evaluation measures **learnability** under a declared out-of-sample split. It is distinct from population similarity and retrieval of measured responses.

## Versioned transcriptomic metric family

The primary transcriptomic prediction metric family follows the Arc Institute `cell-eval2` VCC2026 preset and must record the exact package version and preset/config digest used for every production run.

As of the current design freeze, the six scored VCC2026 members are:

- `pds_cosine` — perturbation discrimination/separability;
- `expr_mse_unbiased_capped_norm` — sampling-aware expression error;
- `de_wilcoxon_direction_fidelity_yield_raw` — correctness of predicted DE direction;
- `de_wilcoxon_direction_reach_raw` — depth over which predicted directions remain correct;
- `de_wilcoxon_sig_jaccard` — agreement of significant responding-gene sets;
- `de_wilcoxon_lfc_nmae` — normalized accuracy of predicted log-fold changes.

The repository should call the pinned `cell-eval2` implementation rather than reimplementing these metrics unless a compatibility test is provided.

## Baseline and reference calibration

Prediction results report both raw metric values and the VCC-style calibration when available. The calibrated scale uses an explicit low/no-information baseline and an empirical replicate/reference anchor; a score of 1 is a reference landmark, not a mathematical ceiling.

The exact scale/baseline artifacts and package semantics must be versioned because `cell-eval2` has evolved during VCC2026.

## Split-specific model inputs

Every task contract defines what information a model may use.

Examples:

- unseen context: context-specific control state may be allowed while perturbed test observations are forbidden;
- unseen target: external gene/target representations may be allowed if frozen independently of the test perturbation outcomes;
- unseen compound: chemical structure or target annotation may be allowed according to the split definition.

Model prediction without an explicit input-information contract is invalid.

## Required baselines

At minimum, each prediction task includes:

- context/control or mean-response baseline appropriate to the split;
- simple linear/ridge or additive baseline where lawful;
- task-relevant identity/target baseline if it can generalize without test leakage;
- complex models selected before test inspection.

## Morphology conceptual variants

CellProfiler feature prediction can mirror the VCC2026 concepts without pretending the metrics are numerically identical:

- `morph_pds_cosine`: perturbation discrimination in morphology response space;
- `morph_mse_norm`: normalized profile error after frozen morphology scaling;
- `morph_direction_fidelity`: correctness of signed feature effects;
- `morph_direction_reach`: depth of correctly directed feature ranking;
- `morph_sig_jaccard`: overlap of significantly responding morphology features;
- `morph_effect_nmae`: normalized morphology effect-size error.

These variants require a dedicated validation/calibration study before being treated as primary scored metrics.

For deep morphology embeddings, primary evaluation is limited to profile error/similarity, PDS/retrieval, and distributional/profile-level metrics; feature-significance semantics are not assumed for latent dimensions.

## Provenance

Every prediction run records:

- split manifest;
- model name/version/checkpoint;
- training sources;
- permitted input information;
- feature/response versions;
- metric package/config versions;
- random seeds;
- baseline/reference artifacts;
- per-condition and aggregate outputs.
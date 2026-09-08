# PerturbLens Research Proposal

**Working title:** PerturbLens: mapping the learnable, transferable, cross-modal, and compositional structure of cellular perturbation responses

**Status:** approved scientific framing; numerical results remain evidence-dependent.

**Last scientific review:** 2026-09-08.

## 1. Motivation

Large-scale perturbation datasets and virtual-cell models aim to predict how cells change after genetic, chemical, and other interventions. Yet recent evaluations show that complex models often perform near strong simple baselines, especially under strict unseen-perturbation or unseen-context settings. This raises a more basic question than model ranking:

> How much structured perturbation-response information is actually present in current datasets, what kind of information is it, and across which biological boundaries can it be retained or learned?

PerturbLens treats this as a response-characterization problem rather than a model-development problem.

The project grows from Chem2Gen-Bench/M2M-Bench. The earlier core asked whether matched perturbation responses agree within datasets and whether target-linked chemical and genetic perturbations are concordant. PerturbLens keeps those questions but embeds them in a broader hierarchy that also includes unseen-context/target generalization, transcriptomic-morphological readouts, and combinations.

## 2. Central Scientific Question

> **What information in cellular perturbation responses is reproducible within perturbation classes, transferable across cellular contexts and targets, conserved across intervention and readout modalities, and compositional under combined perturbations?**

The key word is **information**. The study does not equate a single similarity score with biological equivalence and does not use model performance as the only measurement of learnability.

The boundary ladder is:

```text
within
  -> cellular context
  -> target / compound
  -> intervention modality
  -> readout modality
  -> composition
```

Each step tests a stronger form of conservation.

## 3. Study Philosophy

PerturbLens remains fundamentally descriptive/characterization-oriented. It asks what response structure is empirically present before asking whether a particular model can exploit it.

Three evidence levels are deliberately separated:

1. **Geometry / population similarity** — are two responses similar as measured objects?
2. **Specificity / retrieval** — does the response retain enough identity information to distinguish the correct perturbation, target, or counterpart?
3. **Learnability / prediction** — can a model reconstruct that information out of sample under a declared generalization regime?

A response can be geometrically similar but non-specific, or specific but hard to predict from available inputs. These outcomes should not be collapsed.

## 4. Four-Layer Framework

### 4.1 Data layer

The response object is indexed conceptually by:

```text
perturbation x cellular_context x intervention_type x readout x time x dose
```

with optional replicate/source and combination metadata.

Current transcriptomic core:

- LINCS;
- scPerturb.

Candidate extensions:

- matched transcriptomic-morphological perturbation resources;
- genetic combination screens;
- chemical combination screens.

Time and dose are part of the chemical-response heterogeneity analysis rather than a standalone main result unless a later source provides sufficiently dense factorial coverage.

### 4.2 State representation

State representation describes the observed cell or population before response construction.

#### Transcriptomics

Primary families:

- **Gene-level**: direct expression feature space;
- **Pathway-level**: interpretable biological-program projection;
- **FM embedding**: fixed learned transcriptomic representation.

The project does not assume that Pathway is biologically superior to Gene or that FM embeddings preserve more perturbation-relevant information. Representation is treated as an observation lens whose effect on the visibility of response structure must itself be measured.

#### Morphology

Primary families:

- **CellProfiler-derived features**: interpretable size, area, shape, intensity, texture, granularity, and organelle/compartment measurements;
- **deep morphology embeddings**: fixed image encoders used as learned phenotype representations.

CellProfiler features support feature-wise effect/direction analyses. Deep embeddings primarily support geometry, retrieval, and distributional analyses because embedding coordinates do not necessarily have stable biological identities.

### 4.3 Response construction

The main object is not the post-perturbation state alone but a control- or reference-anchored response.

#### Control-referenced delta

For representation `z` and a lawful matched control pool:

```text
Delta_control = centroid(perturbed) - centroid(control)
```

or the representation-appropriate analogue.

This view retains the total perturbation-associated displacement relative to control.

#### Systema-style perturbation-specific reference

Systema showed that a systematic average perturbation shift can dominate reference-based evaluation. Its key alternative uses the average of perturbation-specific centroids as the reference rather than the control centroid, emphasizing how an individual perturbation differs from the broader perturbed population.

PerturbLens adopts this as a second response view:

```text
Delta_systema = centroid(perturbation) - centroid(reference perturbed population)
```

The exact legal reference pool must be task-specific and leakage-safe.

This is called a perturbation-specific view, not a corrected biological truth. Shared systematic shifts may reflect confounding, selection, or real shared biology such as stress or growth arrest.

#### Distributional response extensions

Where single-cell or single-object data justify it, secondary response views may capture distribution changes rather than only centroid shifts, for example through MMD/OT-type summaries or explicit changes in state occupancy. These are supplementary until a common distributional contract is approved.

## 5. Evaluation Families

### 5.1 Population similarity

Purpose: quantify response geometry.

Primary centroid-level metrics:

- cosine similarity;
- Pearson correlation where coordinate meaning supports it;
- response norm/strength as a separate magnitude statistic.

Distribution-level analyses may use MMD, energy distance with a distribution-sensitive distance choice, or OT/Sinkhorn when justified. Magnitude and identity must remain separate.

### 5.2 Instance retrieval

Purpose: quantify perturbation/target specificity.

Primary outputs:

- true rank;
- MRR;
- Hit@1/3/5;
- rank percentile or chance-corrected retrieval score;
- gallery size and number of lawful positives.

Possible positive relations vary by task:

- same perturbation;
- same target;
- chemical-genetic counterpart;
- transcriptomic-morphological counterpart;
- combination identity.

### 5.3 Model prediction

Purpose: quantify out-of-sample learnability.

PerturbLens adopts the conceptual coverage of the 2026 Virtual Cell Challenge / Cell-Eval2 metric panel for transcriptomic prediction. The VCC2026 scored set includes:

- perturbation discrimination (`pds_cosine`);
- sampling-noise-corrected expression MSE (`expr_mse_unbiased_capped_norm` in the current Cell-Eval2 specification);
- direction fidelity;
- direction reach;
- significant-DE-set Jaccard;
- log-fold-change normalized error.

These collectively test separability, overall profile accuracy, response direction, depth of correct direction, responding-feature identity, and effect magnitude.

PerturbLens will adapt the concepts to morphology rather than mechanically copying gene-specific metrics:

#### CellProfiler morphology

Candidate analogues:

- morphology PDS/retrieval;
- profile MSE or standardized feature error;
- morphology-feature direction fidelity;
- direction reach over ranked morphological effects;
- significant-feature-set overlap;
- normalized effect-size error.

#### Deep morphology embeddings

Primary evaluation should focus on:

- embedding distance/error;
- perturbation discrimination;
- retrieval;
- distributional agreement.

Feature-wise significance/direction metrics are not treated as directly interpretable for arbitrary latent dimensions.

## 6. Main Result Logic

### R1 — Framework: what do we measure and compare?

R1 establishes the data landscape, state representations, response constructions, comparison units, evaluation families, coverage, and evidence boundaries.

It should not be a representation leaderboard. Its role is to make later biological questions interpretable and reproducible.

### R2 — Genetic response learnability

Scientific question:

> As novelty increases, what genetic-perturbation response information remains stable and learnable?

Primary hierarchy:

```text
inner / replicate
  -> unseen cellular context
  -> unseen target
```

The main result is not merely monotonic performance degradation. Analyses should determine whether loss occurs mainly in response magnitude, direction/geometry, perturbation identity, responding genes, or pathway-level structure.

Representation and response views are used to determine at what biological resolution conservation persists.

### R3 — Chemical response learnability

Scientific question:

> Which chemical-response information is compound-specific, target-linked, context-dependent, or transferable to novel compounds and targets?

Primary hierarchy:

```text
inner compound response
  -> unseen context
  -> new compound / same target
  -> unseen compound
  -> unseen target
```

This separates compound identity from target biology. New-compound/same-target generalization is not equivalent to new-target generalization.

Dose and time are explanatory covariates. Their role is to test whether apparent generalization failures can be explained by magnitude shifts, direction changes, response specificity, or different experimental regimes.

### R4 — Cross-intervention conservation: chemical versus genetic

Scientific question:

> What target-linked response information survives changing the intervention modality?

This extends Chem2Gen-Bench from a standalone correspondence task into the intervention boundary of the PerturbLens ladder.

Primary analyses:

- target-matched population similarity;
- C2G and G2C retrieval;
- representation-resolution comparison;
- within-intervention learnability versus cross-intervention conservation.

The final joint map should distinguish targets that are internally stable and cross-intervention conserved from targets that are internally stable but intervention-specific, as well as targets for which within-intervention evidence is weak.

### R5 — Cross-readout conservation: transcriptomics versus morphology

Scientific question:

> Which perturbation-response information is shared across molecular and morphological readouts, and which is readout-specific?

Primary analyses:

1. response-strength correspondence;
2. perturbation-geometry correspondence within each readout;
3. cross-modal same-perturbation/same-target retrieval;
4. cross-modal prediction under held-out perturbation/context/target regimes;
5. shared versus readout-specific response programs or structures.

A central high-value design is the 2 x 2 intervention/readout map:

```text
                  Transcriptomics     Morphology
Genetic                 G,T               G,M
Chemical                C,T               C,M
```

This permits a question not answered by Chem2Gen or morphology studies alone:

> Is chemical-genetic response conservation itself conserved across readout modalities?

The study should not claim that cross-modal similarity implies an RNA-to-morphology causal pathway.

### R6 — Combination compositionality

Scientific question:

> Can combination responses be described from constituent single-perturbation responses, and what stable information remains outside that compositional expectation?

Genetic and chemical combinations should be treated separately unless a shared null model is explicitly justified.

A simple additive response reference can be written conceptually as:

```text
R_expected(A+B) = R(A) + R(B)
```

but the exact null must respect the response scale. Systema's matching-mean baseline provides an additional precedent for strong simple combination references.

Define an interaction residual only after the null is fixed:

```text
I(A,B) = R_observed(A+B) - R_expected(A+B)
```

The main question is whether this residual is reproducible and biologically structured, not merely non-zero.

Potential outcomes include dominance, buffering, amplification, program reweighting, and response components not represented by the constituent singles.

## 7. Cross-Result Scientific Spine

The Results are unified by the same question at increasing biological distance:

```text
R2/R3: what can be learned within an intervention modality?
R4: what survives an intervention change?
R5: what survives a readout change?
R6: what survives composition?
```

The project should report not only whether a score falls, but what response information disappears or persists.

Possible response-information categories include:

- magnitude;
- direction/geometry;
- perturbation identity;
- target-level specificity;
- biological-program structure;
- readout-specific structure;
- composition-specific residual structure.

These categories are analytical hypotheses rather than assumed biological components.

## 8. Baseline Philosophy

Strong baselines are scientific controls, not merely implementation checks.

Expected baseline families include:

- control/no-change;
- perturbed mean / mean-response baseline;
- matching mean or additive combination baseline where lawful;
- simple linear/ridge models;
- nearest-neighbor or target-average baselines;
- model families using increasingly rich perturbation/context representations.

For unseen-target evaluation, one-hot identifiers are insufficient by construction. Any model claiming target-level extrapolation must use information available for the held-out target, such as sequence, functional, network, pathway, or other external representations, with explicit leakage control.

## 9. Primary Versus Supplementary Scope

To avoid turning PerturbLens into an exhaustive factorial benchmark, the primary hierarchy is:

### Primary state representations

Transcriptomics:

1. Gene;
2. Pathway;
3. selected FM representations with lawful coverage.

Morphology:

1. CellProfiler;
2. selected fixed deep embedding.

### Primary response views

1. control delta;
2. Systema-style perturbation-specific reference.

### Primary evaluation families

1. population similarity;
2. retrieval;
3. prediction.

### Supplementary analyses

- alternative pathway libraries;
- alternative FM/image encoders;
- distributional response metrics;
- normalization sensitivity;
- batch/plate/source sensitivity;
- dose/time stratification;
- annotation-confidence and multi-target sensitivity;
- alternative gallery or null constructions.

## 10. Expected Scientific Contribution

The project should not claim novelty from any one of the following alone:

- showing that complex models can be close to baselines;
- showing that unseen contexts/targets are difficult;
- decomposing response into shared and specific components;
- showing morphology/transcriptomics are complementary;
- showing combination responses can be non-additive.

The intended contribution is the **unified response-centric boundary analysis**:

> PerturbLens maps how response information is conserved, lost, or reorganized across context/target novelty, intervention modality, readout modality, and perturbation composition using a common set of response representations and evidence levels.

## 11. Completion Criteria

The project is complete only when:

- each main result has a versioned task/data/metric contract;
- source coverage and exclusions are explicit;
- baselines and generalization splits are leakage-safe;
- numerical evidence is backed by manifests and validation assertions;
- conclusions distinguish geometry, specificity, and learnability;
- null, negative, and uncertain results are retained rather than filtered out;
- the manuscript claims remain within the support of the data and independent evidence.

## 12. Key External References

- Ahlmann-Eltze C, Huber W, Anders S. Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines. *Nature Methods* (2025). https://doi.org/10.1038/s41592-025-02772-6
- Viñas Torné R et al. Systema: a framework for evaluating genetic perturbation response prediction beyond systematic variation. *Nature Biotechnology* (2025/2026 issue). https://doi.org/10.1038/s41587-025-02777-8
- Wei et al. Benchmarking algorithms for generalizable single-cell perturbation response prediction. *Nature Methods* (2025/2026). https://doi.org/10.1038/s41592-025-02980-0
- Arc Institute. Virtual Cell Challenge 2026 and Cell-Eval2 metric specification. https://arcinstitute.org/news/virtual-cell-challenge-2026 and https://github.com/ArcInstitute/cell-eval2
- Haghighi M et al. High-dimensional gene expression and morphology profiles of cells across 28,000 genetic and chemical perturbations. *Nature Methods* (2022). https://doi.org/10.1038/s41592-022-01667-0
- Chandrasekaran SN et al. Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations. *Nature Methods* (2024). https://doi.org/10.1038/s41592-024-02241-6
- UniPert-G2CP. *Cell* (2026). https://doi.org/10.1016/j.cell.2026.06.005
- Roohani Y, Huang K, Leskovec J. GEARS. *Nature Biotechnology* (2023/2024). https://doi.org/10.1038/s41587-023-01905-6

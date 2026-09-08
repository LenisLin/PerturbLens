# PerturbLens Literature Landscape And Competitive Position

**Literature cutoff:** 2026-09-08.

**Purpose:** identify the ecological niche, direct competitors, novelty risks, and strategic requirements for PerturbLens. This document distinguishes published facts from project-level inference and recommendations.

## 1. Executive Position

The perturbation-response field is now crowded in three directions:

1. **virtual-cell prediction and generalization benchmarking**;
2. **response decomposition / shared-versus-specific structure**;
3. **representation benchmarking for transcriptomics or morphology**.

PerturbLens should therefore **not** position itself as a broader model benchmark, a new proof that simple baselines are strong, or a new discovery that perturbation responses contain shared and target-specific components.

The strongest remaining niche is:

> **response-centric perturbation cartography: mapping how perturbation-response information is conserved, lost, or reorganized as analysis crosses biological boundaries from context and target novelty to intervention modality, readout modality, and composition.**

The highest-value differentiator is the joint analysis of:

```text
intervention boundary x readout boundary
```

namely whether chemical-genetic conservation observed in transcriptomics is preserved, weakened, or reorganized in morphology.

R2/R3 genetic/chemical learnability remain necessary backbone analyses. R4/R5 should carry the main differentiation, with R6 combination acting as a stress test of the response structure inferred earlier.

## 2. Virtual-Cell Prediction Is Already A Dense Competitive Space

### 2.1 Simple baselines versus deep models

Ahlmann-Eltze, Huber, and Anders compared foundation/deep models against deliberately simple baselines for single- and double-gene perturbation prediction and found that the evaluated deep-learning methods did not consistently outperform the simple baselines.

Implication for PerturbLens:

- the statement "complex models can be close to simple baselines" is motivation, not novelty;
- a new model leaderboard without a new scientific estimand will be difficult to differentiate.

Reference: https://doi.org/10.1038/s41592-025-02772-6

### 2.2 Systematic variation and perturbation-specific evaluation

Systema demonstrated that common evaluation can be dominated by systematic differences between perturbed and control populations. It introduced a perturbed-centroid reference and centroid-accuracy style evaluation to emphasize perturbation-specific structure.

Implication:

- PerturbLens should include a Systema-style perturbation-specific view, but cannot claim novelty from merely residualizing the shared response;
- the value is to ask how conclusions change across *multiple biological boundaries and readout modalities* under both control and perturbation-specific response views.

Reference: https://doi.org/10.1038/s41587-025-02777-8

### 2.3 Large-scale generalization benchmarks

A recent *Nature Methods* benchmark evaluated 27 methods across 29 datasets and six complementary metrics, explicitly testing generalization across diverse unseen cellular contexts and perturbation scenarios.

The 2026 Virtual Cell Challenge further centers zero-shot context generalization: CRISPRi responses must be predicted in six cell lines never observed perturbed, using their unperturbed state and the target list. Its current Cell-Eval2 specification uses six scored metrics covering perturbation discrimination, profile error, effect direction, significant responding features, and effect size.

State, published online in *Cell* on 31 August 2026, directly targets perturbation prediction across diverse contexts and introduces Cell-Eval as a broad evaluation framework.

Implication:

- R2 `inner -> unseen context -> unseen target` is important but highly competitive;
- "performance declines OOD" is not a sufficient main finding;
- PerturbLens must identify *which response information* disappears or survives across the boundary.

References:

- https://doi.org/10.1038/s41592-025-02980-0
- https://arcinstitute.org/news/virtual-cell-challenge-2026
- https://github.com/ArcInstitute/cell-eval2
- https://doi.org/10.1016/j.cell.2026.07.052

## 3. Response Decomposition Is Also Becoming Crowded

### 3.1 Global, perturbation, context, and interaction components

Molina and Zhang (2026 preprint) explicitly decompose response into global, perturbation-specific, cell-line-specific, and perturbation-by-cell-line interaction components and study their distinct information requirements. They report a low-dimensional global component and harder-to-infer perturbation/context-specific components.

Reference: https://doi.org/10.64898/2026.07.24.740459

### 3.2 Shared and gene-specific response

COMPASS (2026 preprint) frames perturbation prediction as component-wise inference of shared and gene-specific response, motivated by the observation that mean-response baselines can score well while failing perturbation discrimination.

Reference: https://doi.org/10.64898/2026.08.03.742643

### 3.3 Global state manifolds and response programs

A 2026 preprint from Pan and colleagues develops global cell-state and gene-program representations to identify conserved and context-specific perturbation responses.

Reference: https://doi.org/10.64898/2026.05.16.725005

Implication for PerturbLens:

The following are necessary analyses but weak standalone novelty claims:

- response is partly shared and partly perturbation-specific;
- pathway/program spaces can reveal conserved structure;
- cell context changes perturbation responses;
- different response components have different predictability.

PerturbLens should instead use shared/specific structure as *one lens* for a broader conservation ladder.

## 4. Chemical Perturbation Prediction Is Rapidly Maturing

Chemical-response modeling now includes large-scale atlases, mechanism-aware zero-shot prediction, and context transfer.

MAP, published in *Nature Machine Intelligence* in 2026, evaluates two stringent regimes: unseen cell line-drug combinations and entirely unprofiled drugs, using gene-level and pathway-level readouts. It explicitly uses biological knowledge to create transferable compound and gene representations.

Implication:

- R3 cannot claim novelty from unseen-compound or unseen-context evaluation alone;
- a useful PerturbLens distinction is `new compound / known target` versus `new target`, because these ask different scientific questions;
- R3 becomes stronger when directly contrasted with R2 genetic generalization under a common response/evaluation framework.

Reference: https://doi.org/10.1038/s42256-026-01286-w

## 5. Chemical-Genetic Bridging Remains Valuable But Is No Longer Empty

### 5.1 Chem2Gen-Bench / M2M lineage

The current project lineage already contributes target-matched chemical-genetic response comparisons. PerturbLens should treat this as intellectual continuity rather than an external competitor.

The new opportunity is to stop treating Chem2Gen as an isolated benchmark and instead make it the **intervention boundary** of a broader response-information ladder.

### 5.2 Morphology-based chemical-genetic matching

CPJUMP1 was specifically constructed with matched chemical and genetic perturbations and showed that identifying morphology matches for target-linked chemical/genetic perturbations is difficult.

This makes a simple morphology version of Chem2Gen insufficiently novel.

Reference: https://doi.org/10.1038/s41592-024-02241-6

### 5.3 Genetic-to-chemical transfer models

UniPert-G2CP, published in *Cell* in 2026, unifies genetic and chemical perturbagens in a shared space and performs genetic-to-chemical phenotype transfer while analyzing context-specific effects.

Implication:

- PerturbLens should not compete by proposing another translation model;
- it can differentiate by measuring *what target-linked response information survives intervention change*, and by relating this to within-intervention learnability and to morphology.

Reference: https://doi.org/10.1016/j.cell.2026.06.005

## 6. Transcriptomics-Morphology Is Active, But A White Space Remains

### 6.1 Shared and complementary information is established

Haghighi and colleagues harmonized high-dimensional gene-expression and Cell Painting morphology profiles across more than 28,000 genetic and chemical perturbations. This resource established large-scale cross-readout analysis and demonstrated that both modalities can support biological applications.

Therefore, "transcriptomics and morphology contain shared and complementary information" is not a new claim.

Reference: https://doi.org/10.1038/s41592-022-01667-0

### 6.2 Multimodal virtual-cell prediction is already emerging

MVCBench (2026 preprint) evaluates 24 drug/gene representations across nearly 1.1 million drug-induced multimodal profiles and studies unseen compounds, cell lines, plates, and datasets. It reports modality-dependent asymmetry and gains from multimodal integration.

MultiVCDiff, published in *Cell Reports Methods* in 2026, jointly predicts morphology and transcriptomics from chemical/genetic perturbations and evaluates zero-shot unseen drugs.

Implication:

- PerturbLens cannot claim novelty from simply predicting both modalities or integrating them;
- R5 must focus on the *measured relationship of perturbation-response information across readouts*.

References:

- https://doi.org/10.64898/2026.04.22.720110
- https://doi.org/10.1016/j.crmeth.2026.101459

### 6.3 Morphology representation benchmarking is also crowded

MorphoHELM (2026 preprint) provides a broad Cell Painting representation benchmark and reports trade-offs among representation methods, with no universal deep representation dominating classical approaches.

Implication:

CellProfiler versus deep image features should be treated as representation lenses, not the scientific contribution.

Reference: https://arxiv.org/abs/2605.15383

### 6.4 Remaining high-value white space

The most differentiated cross-modal question is not:

```text
transcriptomics <-> morphology
```

in isolation, but:

```text
(intervention boundary) x (readout boundary)
```

The 2 x 2 map is:

| | Transcriptomics | Morphology |
| --- | --- | --- |
| Genetic | G,T | G,M |
| Chemical | C,T | C,M |

Key question:

> If a target shows strong chemical-genetic conservation in transcriptomics, does the same intervention correspondence appear in morphology?

Possible outcomes are scientifically distinct:

- conserved in both readouts;
- conserved only transcriptionally;
- conserved only morphologically;
- conserved only at pathway/coarse-response level;
- context-dependent readout-specific conservation.

This joint boundary structure is the strongest current differentiator found in this review.

## 7. Combination Prediction Is Important But Established

Norman et al. used rich single-cell phenotypes to study genetic interaction manifolds. GEARS predicts novel multigene perturbations and interaction subtypes. CPA explicitly models dose, cell type, and drug/gene combinations. Recent benchmarks show that additive/matching-mean baselines are strong and that non-additive effects remain difficult.

Implication:

- "combinations are non-additive" is not novelty;
- R6 should be the final **compositional stress test** of response structures established in R2-R5;
- the key question is whether residual response information beyond a strong compositional null is stable, specific, cross-representation, or cross-modal.

References:

- Norman et al., *Science* 2019: https://doi.org/10.1126/science.aax4438
- GEARS: https://doi.org/10.1038/s41587-023-01905-6
- CPA repository/documentation: https://github.com/theislab/cpa

## 8. Competitive Matrix

| PerturbLens Result | Competition | Standalone novelty risk | Strategic role |
| --- | --- | --- | --- |
| R1 framework | Systema, Cell-Eval2, MorphoHELM, MVCBench | high | necessary coordinate system |
| R2 genetic learnability | State, VCC2026, large benchmarks, COMPASS, response decomposition | very high | backbone; characterize information loss |
| R3 chemical learnability | MAP, Tahoe-scale models, State, MVCBench | high | backbone; separate compound versus target generalization |
| R4 chem-gen | Chem2Gen lineage, UniPert-G2CP, CPJUMP1 | medium-high | first major biological boundary |
| R5 RNA-morphology | Haghighi, MVCBench, MultiVCDiff, MorphoHELM | medium-high | strongest extension if tied to intervention/context structure |
| R6 combination | Norman, GEARS, CPA, Systema, modern chemical models | high | final compositional stress test |

## 9. What PerturbLens Should Not Claim

Avoid claims equivalent to:

- first benchmark showing foundation models do not beat baselines;
- first analysis of unseen cell-context or unseen target prediction;
- first decomposition of shared and specific perturbation responses;
- first comparison of Gene, Pathway, and embeddings;
- first demonstration that transcriptomics and morphology are complementary;
- first multimodal virtual-cell benchmark;
- first chemical-genetic matching benchmark;
- first demonstration of non-additive combination responses.

These spaces already have direct precedents.

## 10. What PerturbLens Can Plausibly Own

A stronger contribution is:

> **A common response-centric framework that measures how perturbation information survives successive biological boundaries and distinguishes geometry, specificity, and learnability at each boundary.**

The clearest scientific signature would be a **hierarchy of response-information conservation**, for example if evidence shows that:

- gene-level specificity decays rapidly across context/target novelty;
- pathway/program structure is more conserved;
- only part of the target-linked structure survives chemical-genetic intervention change;
- morphology preserves a different subset of that structure than transcriptomics;
- combination perturbations selectively disrupt or extend these conserved components.

This is a candidate narrative, not an assumed outcome.

## 11. Competitive Requirements For A Strong Paper

### Requirement 1: R2/R3 must diagnose information loss, not only score loss

A score drop is already expected. Main analyses should identify whether magnitude, direction, perturbation identity, target-level specificity, or program-level structure is lost.

### Requirement 2: R4 must connect internal learnability to cross-intervention conservation

This distinguishes targets that are stable-but-intervention-specific from targets that are simply poorly measured or weakly structured.

### Requirement 3: R5 must go beyond generic multimodal complementarity

The highest-value version directly links transcriptomic-morphological structure to the same targets, contexts, and intervention boundaries studied in R2-R4.

### Requirement 4: R6 must use strong compositional nulls

Complex combination predictors should be judged against additive/matching-mean baselines, and claims of emergence require reproducible structured residuals.

### Requirement 5: representation breadth must not become the paper

Gene/Pathway/FM and CellProfiler/deep features should reveal the resolution at which a conclusion holds. They should not generate an exhaustive leaderboard detached from the scientific questions.

## 12. Overall Competitiveness Assessment

### If executed as a broad benchmark catalog

**Competitiveness: moderate.**

A paper that combines many representations, metrics, generalization splits, modalities, and combinations without a central response-information argument risks being viewed as an aggregation of existing benchmark ideas.

### If executed as a boundary-conservation study

**Competitiveness: medium-high to strong.**

The project becomes more distinctive if R2/R3 establish a common response-information baseline, R4 measures the intervention boundary, R5 measures the readout boundary and their interaction, and R6 tests whether the inferred response structure is compositional.

### Likely journal ecology

Without claiming a specific submission target, the scientific framing aligns more naturally with systems/computational biology journals than with a pure benchmark paper. A strong, independently validated R4-R5 story could support journals in the Cell Systems / Genome Biology / Nature Communications range. A methods-tier venue would require the framework itself to become demonstrably reusable across datasets and research groups, not only internally coherent.

## 13. Literature Watchlist

Because the field is moving unusually quickly, this landscape should be refreshed before manuscript freeze. Priority watch areas:

- Virtual Cell Challenge 2026 final methods and winner analyses;
- updates to State / Cell-Eval;
- revisions or publication of Molina/Zhang, COMPASS, MVCBench, MorphoHELM, and related 2026 preprints;
- new multimodal perturbation datasets with matched genetic/chemical and RNA/morphology readouts;
- new response-decomposition or information-theoretic evaluation studies;
- combination-response benchmarks using strict unseen-target/context protocols.

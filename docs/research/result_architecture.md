# PerturbLens Main Result Architecture

## Purpose

This document defines the manuscript-level logic of the six main Results. A main Result may contain several main panels and supplementary figures, but each Result must answer one scientific question. Representation and metric sweeps are supporting axes, not the section organization.

## Overall Spine

```text
R1  What do we measure and compare?
     |
R2  What can be learned from genetic perturbations?
     |
R3  What can be learned from chemical perturbations?
     |
R4  What survives changing the intervention modality?
     |
R5  What survives changing the readout modality?
     |
R6  Can the response structure compose under combinations?
```

The repeated analytical question is:

> When a boundary becomes harder, which response information is retained, and which is lost or reorganized?

## Shared Analytical Axes

Every Result uses only the representation/evaluation views needed to answer its question.

### State representation

Transcriptomics:

- Gene;
- Pathway;
- selected FM embeddings.

Morphology:

- CellProfiler features;
- selected deep image embeddings.

### Response construction

- control delta;
- Systema-style perturbed reference.

### Evidence levels

- population similarity;
- instance retrieval;
- model prediction.

### Response-information categories

Candidate categories used to interpret performance changes:

- magnitude;
- direction/geometry;
- perturbation identity;
- target-level specificity;
- biological-program structure;
- readout-specific structure;
- combination-specific residual structure.

These are analysis dimensions, not assumed latent biological components.

# R1 — Framework, Data, Workflow, And Evaluation

## Scientific role

R1 defines the measurement problem. It does not claim that any representation, delta, or model is superior.

## Main questions

- Which data sources and perturbation classes are in scope?
- How is state represented in transcriptomics and morphology?
- How is a response constructed relative to control or the perturbed population?
- Which comparison units are lawful?
- What do similarity, retrieval, and prediction each measure?
- What coverage and evidence boundaries limit later claims?

## Expected main panels

- data/source and coverage landscape;
- state-representation schematic;
- response-construction schematic;
- population similarity versus retrieval versus prediction schematic;
- biological-boundary ladder.

## Supplementary support

- source QC and exclusions;
- feature coverage;
- replicate distributions;
- control/reference pool QC;
- metric calibration and null simulations;
- representation availability.

# R2 — Genetic Perturbation Response Learnability

## Core question

> What genetic-perturbation response information remains learnable as novelty increases?

## Primary ladder

```text
inner / replicate
  -> unseen cellular context
  -> unseen target
```

## Analytical logic

### R2A. Inner response structure

Hold target and context fixed. Establish the reproducible response information available within a perturbation class.

### R2B. Cross-context transfer

Hold target fixed and change cellular context. Determine whether the response changes mainly in magnitude, direction/program mixture, or target specificity.

### R2C. Cross-target generalization

Hold out target identity. Models must use information available for unseen targets rather than memorized identifiers.

## Main interpretation

Do not stop at `inner > context > target` performance. Attribute the drop to response-information classes where possible.

## Supplementary analyses

- dataset/source-specific results;
- CRISPR/CRISPRi/CRISPRa or other intervention-mode strata;
- target family/function;
- response strength;
- control-delta versus Systema view;
- Gene/Pathway/FM sensitivity;
- alternative baselines and external target representations.

# R3 — Chemical Perturbation Response Learnability

## Core question

> Which chemical-response information is compound-specific, target-linked, context-dependent, or transferable to novel compounds and targets?

## Primary ladder

```text
inner compound response
  -> unseen context
  -> new compound / same target
  -> unseen compound
  -> unseen target
```

## Analytical logic

### R3A. Inner compound response

Establish within-compound response structure under comparable conditions.

### R3B. Cross-context transfer

Test whether a compound or target produces conserved response structure across cellular backgrounds.

### R3C. Cross-compound / same-target

Use distinct compounds linked to the same target to separate compound identity from target-linked response structure.

### R3D. Unseen compound

Hold out a molecule while retaining information about a target or related mechanism where lawful.

### R3E. Unseen target

Hold out the target itself. This is biologically stronger than new-compound generalization.

## Dose/time covariates

Dose and time are explanatory analyses within R3. Ask whether they primarily alter response magnitude, rotate response direction, change perturbation specificity, or explain apparent context heterogeneity.

Do not create a standalone time/dose Result unless future data provide a dense target x context x dose x time design.

## Supplementary analyses

- target annotation confidence;
- single- versus multi-target compounds;
- dose/time strata and regression;
- source-specific results;
- structural/target representation comparisons;
- control-delta versus Systema view.

# R4 — Cross-Intervention Conservation: Chemical Versus Genetic

## Core question

> What target-linked response information survives changing the intervention modality?

## Intellectual role

R4 is the PerturbLens extension of the Chem2Gen/M2M core. It is no longer an isolated task; it is the intervention boundary after R2/R3 establish the structure available within each intervention type.

## Main analyses

### R4A. Target-matched population similarity

Compare chemical and genetic responses within lawful cell-target contexts.

### R4B. C2G and G2C retrieval

Measure whether target identity remains distinguishable across intervention types.

### R4C. Within-intervention learnability versus cross-intervention conservation

Jointly map:

```text
within genetic / chemical stability
              x
chemical-genetic conservation
```

Distinguish at minimum:

- internally stable and cross-intervention conserved;
- internally stable but intervention-specific;
- weak within-intervention evidence;
- mixed/uncertain cases.

### R4D. Biological resolution

Ask whether conservation persists at Gene, Pathway, or FM resolution. A Pathway-only match supports coarse program-level conservation, not gene-level equivalence.

## Supplementary analyses

- direction of genetic intervention versus drug mechanism;
- multi-target chemicals;
- dose/time effects;
- target classes;
- source-specific replication;
- alternative target annotations.

# R5 — Cross-Readout Conservation: Transcriptomics Versus Morphology

## Core question

> Which perturbation-response information is shared across molecular and morphological readouts, and which is readout-specific?

## Main analyses

### R5A. Response-strength correspondence

Compare transcriptomic and morphological perturbation strength. Identify RNA-high/Morph-low and RNA-low/Morph-high regimes rather than assuming monotonic correspondence.

### R5B. Perturbation-geometry correspondence

Build response-similarity matrices separately in transcriptomics and morphology and test whether perturbation-pair relationships are conserved across readouts.

### R5C. Cross-modal retrieval

Use transcriptomic response to retrieve the correct morphology perturbation/target counterpart and vice versa.

Possible positive definitions must be task-specific:

- same perturbation;
- same target;
- same context.

### R5D. Cross-modal prediction

Measure how much one *observed post-perturbation readout* predicts another under held-out perturbation/context/target regimes. Keep this distinct from de novo virtual-cell prediction from control + perturbation identity.

### R5E. Intervention x readout interaction

High-priority 2 x 2 analysis:

| | Transcriptomics | Morphology |
| --- | --- | --- |
| Genetic | G,T | G,M |
| Chemical | C,T | C,M |

Ask whether chemical-genetic conservation is itself conserved across readouts.

### R5F. Shared versus readout-specific response structure

Only after the geometry/retrieval evidence is established, interpret recurring shared or readout-specific programs.

## Supplementary analyses

- CellProfiler versus deep morphology representations;
- batch/plate normalization;
- assay matching level;
- context-specific cross-modal relations;
- gene/pathway-to-morphology feature associations;
- alternative image encoders.

# R6 — Combination Compositionality

## Core question

> Can combination responses be explained from constituent single perturbations, and what stable response information remains beyond a strong compositional null?

## Main analyses

### R6A. Genetic combinations

Compare observed double/multiple genetic perturbations against constituent-based baselines.

### R6B. Chemical combinations

Analyze drug combinations separately with scale-appropriate nulls.

### R6C. Strong simple nulls

Candidate nulls include additive response and matching-mean baselines. The null must be defined in the response scale being tested.

### R6D. Interaction residual

```text
I(A,B) = R_observed(A+B) - R_expected(A+B)
```

Measure whether the residual is reproducible, specific, and structured.

### R6E. Compositional prediction

Compare simple compositional baselines, linear models, and specialized predictors. The main scientific question is whether complex methods recover information that the strong null cannot.

### R6F. Cross-representation / cross-modal interaction structure

Where data permit, ask whether non-compositional response appears consistently at Gene/Pathway/FM levels or in both transcriptomics and morphology.

## Interpretation boundary

A non-zero residual is not automatically synergy. Claims of emergent biology require a stable response component with appropriate replicate and functional evidence.

# Cross-Result Synthesis

The final synthesis should avoid a single omnibus leaderboard. Instead summarize conservation across boundaries:

| Boundary | Geometry | Specificity | Learnability | Main interpretation |
| --- | --- | --- | --- | --- |
| within | response stability | identity within class | inner prediction | information available in measured response |
| context | cross-context similarity | target identity across contexts | unseen-context prediction | context transfer |
| target/compound | family/target geometry | target/compound retrieval | unseen target/compound | perturbation novelty |
| intervention | chem-gen similarity | C2G/G2C | cross-intervention mapping | intervention conservation |
| readout | RNA-morph geometry | cross-modal retrieval | cross-modal prediction | readout conservation |
| composition | observed-vs-null geometry | combination identity | combination prediction | compositional boundary |

The manuscript should conclude from this boundary map rather than from representation rankings alone.

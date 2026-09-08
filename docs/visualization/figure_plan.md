# PerturbLens Figure Plan

Figures are organized by scientific result rather than by representation or metric.

| Figure | Main question |
| --- | --- |
| Figure 1 | What data, state representations, response views, metrics, and biological boundaries are compared? |
| Figure 2 | What genetic response information remains learnable across inner, context, and target boundaries? |
| Figure 3 | What chemical response information is compound-, target-, context-, time-, or dose-dependent? |
| Figure 4 | What target-linked information survives changing chemical/genetic intervention modality? |
| Figure 5 | What response information is shared between transcriptomic and morphological readouts? |
| Figure 6 | Are perturbation responses compositional under combined perturbations? |

## Figure 1

Primary components:

- source/readout/intervention landscape;
- Gene/Pathway/FM and CellProfiler/DeepMorphology state lenses;
- Delta/SystemaResidual response construction;
- population similarity/retrieval/prediction evidence families;
- boundary ladder and coverage.

## Figures 2-3

Use consistent visual grammar across genetic and chemical learnability so differences in generalization hierarchy are directly comparable. Main panels emphasize response-information loss by metric family and biological resolution, not only model ranks.

## Figure 4

Show matched target/context support, population concordance, bidirectional retrieval, internal-support versus cross-intervention conservation, and resolution dependence.

## Figure 5

Show matching tiers, RNA/morphology response-strength correspondence, perturbation-geometry correspondence, cross-modal retrieval/prediction, and the intervention x readout comparison.

## Figure 6

Show combination coverage, null/compositional baselines, residual reproducibility, prediction relative to simple nulls, and cross-representation/readout evidence for residual components.

## Shared workflow

1. validated scientific run emits source tables/manifests;
2. Python generates plot-ready tables without changing metric definitions;
3. plotting code handles ordering/layout only;
4. rendered panels are checked against denominators, matching tiers, split/null definitions, and claim boundaries.

Supplementary figures carry representation/model sweeps, dataset-specific panels, time/dose details, sensitivity analyses, and expanded target/context scans.
# PerturbLens Visualization Standards

## Purpose

Visualization presents validated PerturbLens evidence without redefining tasks, response objects, or metrics.

## Semantic rules

- organize main figures by R1-R6 scientific questions;
- show representation and response view explicitly when results depend on them;
- keep population similarity, retrieval, and prediction visually distinguishable;
- preserve C2G/G2C direction where both are shown;
- preserve cross-readout matching tier;
- preserve combination null identity;
- show denominators/coverage for filtered summaries;
- do not add a model/representation because it improves visual balance.

## Comparison rules

- direct representation comparisons use common-support units;
- raw distance magnitudes from Gene/Pathway/FM/CellProfiler/DeepMorphology are not placed on a shared quantitative axis without explicit calibration;
- prediction panels show simple baselines and empirical/reference anchors where defined;
- readout/intervention discordance is displayed as a result rather than hidden by averaging.

## Plot-ready boundary

Scientific code owns:

- lawful membership/matching;
- split and null definitions;
- metric computation;
- aggregation and uncertainty;
- significance/FDR;
- plot-ready filtering.

Rendering code owns:

- ordering;
- labels;
- theme;
- composition;
- export.

Rendering code may not recompute panel-defining statistics.

## Active roots

Use the artifact/run roots in `docs/governance/storage_policy.md`.

## Figure integrity

Each panel records or links to:

1. result/task definition;
2. plot-ready table + manifest;
3. state representation and response view;
4. split/matching/null;
5. metric and aggregation level;
6. support/exclusion fields;
7. validation status.

## Supplementary figures

Use supplementary figures for dataset-specific breakdowns, additional FM/image models, time/dose covariate details, alternative response constructions, metric sensitivity, expanded target/context scans, and secondary distribution metrics.
# Metric Aggregation

## Principle

Aggregation follows the scientific estimand. The project does not silently pool across contexts, targets, compounds, sources, readouts, or representations.

## Levels

1. **Per-unit/per-query/per-condition** values are retained first.
2. **Slice summaries** aggregate within a declared task split, representation, response view, readout, intervention type, and source/context stratum.
3. **Macro summaries** average over biological units when each target/compound/context should contribute equally.
4. **Micro summaries** are used only when weighting by observations is scientifically intended and explicitly labeled.

## Uncertainty

Bootstrap or hierarchical resampling units must match the intended generalization claim. Resampling cells does not support a target-level generalization interval; resampling targets does not estimate within-target technical noise.

## Representation comparisons

Use paired common-support units when comparing Gene/Pathway/FM or morphology representations. Report both effect difference and coverage lost by the common-support restriction.

## Multiple comparisons

Confirmatory families declare primary metrics and contrasts before hypothesis testing. Exploratory target/pathway/context scans are labeled exploratory and use appropriate FDR control where inferential p-values are reported.

## Missingness

Every summary reports total, valid, excluded, and missing counts. Missing values are not converted to zero performance.
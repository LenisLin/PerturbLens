# Gene Representation

## Meaning

`Gene` is the primary transcriptomic coordinate space. It preserves gene-level perturbation information before pathway aggregation or learned embedding.

## Feature identity

Gene identifiers are normalized to uppercase gene symbols with an explicit mapping table. Duplicate symbols within a source are collapsed by a declared rule. Cross-source comparisons use a frozen shared feature universe and preserve source coverage.

Primary analyses should use a common-support feature set when directly comparing representations or sources. Missing source genes may not be silently treated as biological zero unless the projection contract explicitly defines that semantics.

## State and response

Gene state surfaces are source-specific expression/signature vectors aligned to the frozen feature index. Delta and SystemaResidual response vectors are built downstream by `docs/responses/construction.md`.

## Interpretation

Gene-space agreement is the highest-resolution primary transcriptomic comparison. Low Gene agreement with higher Pathway agreement is interpreted as coarse functional conservation rather than as failure of robustness by default.

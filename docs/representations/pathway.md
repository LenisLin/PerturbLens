# Pathway Representation

## Primary pathway system

The primary pathway representation uses the 50 human MSigDB Hallmark gene sets (or the project's versioned equivalent resource) in a frozen order and version.

## Construction

For each state or response input, pathway scores are computed using a declared signed aggregation rule over mapped member genes. The primary implementation uses equal-weight signed means unless a later approved contract replaces it.

Each pathway build records:

- pathway resource/version/hash;
- gene mapping;
- member coverage by source;
- score/aggregation method;
- feature order.

The build declares whether its input is a state or an already constructed
response. A score aggregated from a response remains a response-space projection,
not a newly observed state. [Response construction](../responses/construction.md)
owns reference semantics; this contract owns the pathway aggregation rule.

## Scientific role

Pathway is a lower-resolution biological lens. It tests whether response information that is unstable at individual genes remains conserved at the level of broad biological programs.

Pathway performance is not automatically “better biology”. Increased similarity can result from aggregation and information compression, so Gene and Pathway findings are interpreted jointly.

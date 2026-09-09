# Response Construction Contracts

[Construction](construction.md) is the canonical method contract for `Delta`
and `SystemaResidual`, including matched controls, perturbed reference pools,
morphology variants and source/task/split reuse boundaries.

## Build interfaces

1. Resolve [state representations](../representations/README.md), condition IDs
   and source-native value semantics from the [data contracts](../data/README.md).
2. Declare the response view, exact reference membership and lawful reuse scope.
   Freeze split membership before any split-dependent reference or fitting step,
   following the [workflow](../data/workflow.md).
3. Persist response identity, reference registry and lineage using the shared
   [object model](../data/object_model.md) and [manifest](../data/manifests.md).
4. Supply response objects to [tasks](../tasks/README.md); downstream metrics do
   not silently change the response definition or reference population.

Data owns NAS storage and common schemas. This module owns response semantics;
tasks constrain eligible references and comparisons. A documented reference rule
does not certify that a source-specific reference pool has been frozen or built.

# Collaboration Rules

## Scientific changes

Changes to project scope, task units, split definitions, response construction, metric semantics, model input allowances, cross-modal matching, or combination nulls require human-lead approval and an update to the owning contract.

## Implementation changes

Implementation may optimize storage, parallelism, or runtime behavior without scientific approval only when emitted objects are provably identical under the active contract.

## Review expectations

Every pull request that changes scientific semantics should state:

- the scientific question affected;
- controlling contracts changed;
- expected output/schema changes;
- validation updates;
- whether existing results remain interpretable under the new definition.

## Evidence communication

Do not report a run as complete from file existence alone. Use manifests and validation assertions.
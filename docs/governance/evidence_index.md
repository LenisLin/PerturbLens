# PerturbLens Evidence Index

This file is a registry format and locator. It does not certify a result by itself.

## Required evidence entry

Each registered result includes:

- result section and task;
- run ID/run family;
- source/input manifest;
- state and response manifests;
- split manifest where applicable;
- metric/model manifest;
- result table path/hash;
- validation assertions path/status;
- representation, response view, readout, intervention type, split/direction;
- denominators/coverage/exclusions;
- downstream figure/manuscript location.

## Traceability chain

```text
source
-> state representation
-> response construction
-> split/matching/null
-> metric/model run
-> result table
-> validation assertions
-> figure/manuscript claim
```

A missing link is reported as missing. No current numerical PerturbLens result is certified merely by the existence of the project architecture.

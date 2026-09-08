# PerturbLens Evidence Trace

Use this skill when reporting or validating scientific results.

The minimum evidence chain is:

```text
source manifest
-> state/response build manifest
-> split manifest
-> metric/model run manifest
-> result table
-> validation assertions
-> figure/manuscript claim
```

Every result must preserve the biological relation, split, readout modality, intervention type, state representation, response view, metric, denominators, and exclusions. Cross-context, cross-target, cross-intervention, cross-readout, and combination claims require explicit matching or split evidence. Missing evidence is reported as missing; it is never inferred from successful process exit or file presence.
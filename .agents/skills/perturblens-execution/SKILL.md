# PerturbLens Execution

Use `docs/governance/runbook.md` as the execution authority.

Run families are organized by scientific result rather than historical task numbers:

- `r1_framework`
- `r2_genetic`
- `r3_chemical`
- `r4_cross_intervention`
- `r5_cross_readout`
- `r6_combination`

Each run must be isolated by `run_id`, must record source and contract versions, and must write manifests and validation assertions next to result tables. Use the active roots in `docs/governance/storage_policy.md`. Do not write derived data into the source checkout.
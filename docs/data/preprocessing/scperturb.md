# scPerturb Preprocessing Contract

## Inputs

Primary source root:

```text
/mnt/NAS_21T/ProjectData/OSMOSIS/raw/scPerturb_Processed/
```

Eligible datasets provide a harmonizable observation table and expression matrix with perturbation/control annotations.

## Organism

The current PerturbLens transcriptomic scope is human. Mixed-species datasets retain only human observations unless a future ortholog-mapping contract is approved.

## Intervention normalization

Normalize broad intervention family while preserving exact intervention mode:

- CRISPR/CRISPR-Cas-like loss-of-function -> `genetic`, mode preserved;
- CRISPRi -> `genetic`, `CRISPRi`;
- CRISPRa -> `genetic`, `CRISPRa`;
- compound/drug -> `chemical`;
- untreated/non-targeting/source controls -> `control`.

Genetic directionality is therefore available for R2/R4 stratification rather than hidden inside a single `genetic` label.

## Context and technical metadata

Preserve source fields that can affect state distributions, including as available:

- sample
- batch
- plate / plate_id
- lane
- gemgroup
- replicate
- well

`cell_context` is stored separately from technical blocking variables.

## Control reference candidates

For control-referenced response construction, eligible controls must match source/dataset and cell context and should match intervention-compatible experimental blocks when the source design allows. Exact control-reference construction is versioned in `docs/data/response_construction.md` and the task run manifest.

No random control pairing is a universal source-preprocessing rule.

## Perturbation identity

Genetic conditions preserve reagent/guide identity where available and canonical target set separately.

Chemical conditions preserve compound identity separately from target annotations.

True combination conditions preserve constituent identities in `combination_members`. They are not coerced into single perturbations; R6 determines combination eligibility.

## State surfaces

The source bundle materializes state inputs needed downstream:

- Gene expression/state matrix or shards;
- condition/observation registry;
- control candidate registry;
- FM cell handoff registry where FM extraction is requested;
- source manifest and exclusions.

Delta or SystemaResidual response vectors are not frozen in source preprocessing; they are built by the shared response-construction stage.

## Determinism

Any subsampling used for computational tractability must be seeded, recorded, and repeated or sensitivity-checked when it affects a scientific estimand.
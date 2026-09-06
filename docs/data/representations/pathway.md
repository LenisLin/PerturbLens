# Shared Hallmark Pathway Representation Contract

## Role

This contract defines the shared `Pathway` representation used by the current
Task1 freeze across the `LINCS` and `scPerturb` preprocessing contracts.

Final manuscript-valid shared `Pathway` construction is owned by
`task1_scope_merge.py`, not by the dataset-specific preprocessors.

## Authoritative Pathway Source

- the sole authoritative Hallmark membership table for the current Figure 2
  preprocessing freeze is
  `/mnt/NAS_21T/ProjectData/OSMOSIS/resource/OmniPath_annotations/HALLMARK_human.csv`
- the current Task1 `scPerturb` source bundle is already upstream human-only
- the current Figure 2 Task1 freeze does not perform ortholog mapping before
  pathway projection
- the current contract uses the human Hallmark file, not
  `/mnt/NAS_21T/ProjectData/OSMOSIS/resource/OmniPath_annotations/HALLMARK_mouse.csv`

## Representation Shape

- `Pathway` is a `50`-dimensional signed scalar representation
- one signed scalar per hallmark
- total dimensionality = `50`
- sign encodes pathway direction
- absolute magnitude encodes pathway strength

## Canonical Feature Order

The canonical `Pathway` feature order is fixed alphabetical over the `50`
Hallmark names present in
`/mnt/NAS_21T/ProjectData/OSMOSIS/resource/OmniPath_annotations/HALLMARK_human.csv`.

The frozen canonical order is:

1. `ADIPOGENESIS`
2. `ALLOGRAFT_REJECTION`
3. `ANDROGEN_RESPONSE`
4. `ANGIOGENESIS`
5. `APICAL_JUNCTION`
6. `APICAL_SURFACE`
7. `APOPTOSIS`
8. `BILE_ACID_METABOLISM`
9. `CHOLESTEROL_HOMEOSTASIS`
10. `COAGULATION`
11. `COMPLEMENT`
12. `DNA_REPAIR`
13. `E2F_TARGETS`
14. `EPITHELIAL_MESENCHYMAL_TRANSITION`
15. `ESTROGEN_RESPONSE_EARLY`
16. `ESTROGEN_RESPONSE_LATE`
17. `FATTY_ACID_METABOLISM`
18. `G2M_CHECKPOINT`
19. `GLYCOLYSIS`
20. `HEDGEHOG_SIGNALING`
21. `HEME_METABOLISM`
22. `HYPOXIA`
23. `IL2_STAT5_SIGNALING`
24. `IL6_JAK_STAT3_SIGNALING`
25. `INFLAMMATORY_RESPONSE`
26. `INTERFERON_ALPHA_RESPONSE`
27. `INTERFERON_GAMMA_RESPONSE`
28. `KRAS_SIGNALING_DN`
29. `KRAS_SIGNALING_UP`
30. `MITOTIC_SPINDLE`
31. `MTORC1_SIGNALING`
32. `MYC_TARGETS_V1`
33. `MYC_TARGETS_V2`
34. `MYOGENESIS`
35. `NOTCH_SIGNALING`
36. `OXIDATIVE_PHOSPHORYLATION`
37. `P53_PATHWAY`
38. `PANCREAS_BETA_CELLS`
39. `PEROXISOME`
40. `PI3K_AKT_MTOR_SIGNALING`
41. `PROTEIN_SECRETION`
42. `REACTIVE_OXYGEN_SPECIES_PATHWAY`
43. `SPERMATOGENESIS`
44. `TGF_BETA_SIGNALING`
45. `TNFA_SIGNALING_VIA_NFKB`
46. `UNFOLDED_PROTEIN_RESPONSE`
47. `UV_RESPONSE_DN`
48. `UV_RESPONSE_UP`
49. `WNT_BETA_CATENIN_SIGNALING`
50. `XENOBIOTIC_METABOLISM`

## Gene Space Contract

- gene identifiers are normalized as uppercase symbols
- duplicate symbols are collapsed within each source using `mean` before
  projection
- the benchmark gene universe for the final Task1 shared `Pathway` surface is
  the observed union of gene symbols across all retained active Task1 `LINCS`
  and `scPerturb` instances, built once globally before block slicing
- retained `scPerturb` genes already come from the upstream human-only source
  bundle, and this contract does not introduce ortholog projection
- the contract must not collapse Figure 2 to `LINCS` landmark genes only

## Computation Rule

- `task1_scope_merge.py` owns final shared `Pathway` construction
- build a `50 x G` Hallmark weight matrix
- each row sums to `1`
- pathway values are computed as a signed weighted mean over the Task1-global
  shared benchmark gene universe
- genes absent from a source-specific delta object are treated as zero after
  projection into that shared benchmark gene universe

## Resource Exclusions

- `/mnt/NAS_21T/ProjectData/OSMOSIS/resource/OmniPath_annotations/OmniPath_Interaction_human.csv`
  is not part of the current Figure 2 pathway-delta contract
- no network propagation or interaction-graph smoothing is assumed in the
  current freeze

## Relation To MoA Priors

- `/mnt/NAS_21T/ProjectData/OSMOSIS/processed/MoA_Priors/MoA_Priors_Columns.json`
  documents an existing `100`-feature `50 sign + 50 abs` layout in another
  `OSMOSIS` flow
- its first `50` `_sign` feature names align with the frozen canonical order
  above, but that file is not an authority for the Figure 2 preprocessing
  contract
- the current Figure 2 preprocessing freeze does not bind `Pathway` outputs to
  that `100`-feature layout
- Figure 2 `Pathway` remains a `50`-dimensional signed representation in this
  contract

## Figure 2 Guardrail

This shared `Pathway` contract does not authorize `FM` to enter
manuscript-facing Figure 2 panels.

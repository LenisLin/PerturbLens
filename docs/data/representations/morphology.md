# Morphology Representations

## CellProfiler

`CellProfiler` is the primary interpretable morphology feature space. It contains versioned, QC-filtered measurements from cell/nucleus/cytoplasm/organelle objects. Features retain semantic identity and are grouped by feature family for interpretation.

Primary response construction occurs after declared plate/batch-aware normalization.

## DeepMorphology

`DeepMorphology:<model>` is a fixed learned image embedding. The model/checkpoint, image channels, crop/aggregation definition, and embedding dimension are frozen in the state-build manifest.

Feature-wise DE-style interpretation is primary only for CellProfiler, because deep embedding coordinates do not have stable biological semantics by default.

## Cross-readout role

Transcriptomic and morphology feature dimensions are not compared coordinate-by-coordinate. R5 compares response strength, perturbation geometry, retrieval identity, and predictive mappings between the two spaces.
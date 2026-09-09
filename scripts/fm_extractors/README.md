# PerturbLens FM Utilities

## Interface status

The registered extractor families are defined in
[the FM contract](../../docs/representations/fm.md). Model-specific state
extraction routines are retained for reuse, including unpublished local worker
improvements where present.

The standalone `extract_*.py` CLIs still implement a legacy K562 snapshot
interface. Their `task2_snapshot` fields, fixed snapshot layout, delta outputs,
and old configuration-file requirements are compatibility details, not current
PerturbLens task definitions. The retired configuration is not supplied by this
repository. These CLIs are not R2-R6 production entrypoints.

Current execution needs state-build adapters, separately constructed response
objects, NAS-backed output paths, and the manifests and validation assertions
defined in [the runbook](../../docs/governance/runbook.md). A successful legacy
extraction does not establish a valid PerturbLens response build or task run.

## Project naming

- New scFoundation subprocess task names use the `perturblens_` prefix.
- The STATE interpreter override is `PERTURBLENS_STATE_PYTHON`; explicit
  `--state-python` and model configuration take precedence.
- Tahoe-x1 still recognizes the verified external model assets under
  `M2MBench/benchmark/`. This is an existing external asset location, not a
  PerturbLens source, data, or run root. Use `--predict-script` and
  `--gene-map-pkl` when supplying different asset locations.
- Model-specific external runtime filenames and checkpoint identifiers retain
  their existing names; changing the project identity does not rename those
  external interfaces.

## Verification boundary

Repository smoke tests check Python syntax and interface metadata. They do not
load model checkpoints or certify any extraction output. Local code preserved
in `.local/legacy-pre-perturblens/` is outside the active test and package trees.

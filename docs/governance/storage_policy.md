# PerturbLens Storage Policy

The source checkout contains code and documentation only.

## Active project root

```text
/mnt/NAS_21T/ProjectData/PerturbLens
```

Canonical subroots:

```text
/mnt/NAS_21T/ProjectData/PerturbLens/data
/mnt/NAS_21T/ProjectData/PerturbLens/runs
/mnt/NAS_21T/ProjectData/PerturbLens/artifacts
/mnt/NAS_21T/ProjectData/PerturbLens/manuscript
```

## Layout

`data/` stores immutable or versioned prepared source bundles, state representations, response objects, and split registries.

`runs/<run_id>/<run_family>/` stores runtime manifests, logs, tables, model outputs, and validation assertions.

`artifacts/` stores plot-ready and export artifacts derived from validated results.

`manuscript/` stores manuscript-analysis handoffs that are too large or generated for the source repository.

External raw source locations may remain under their source-specific storage roots; they are referenced by manifest and never silently copied or reinterpreted.

No derived scientific result should be written into the Git checkout.
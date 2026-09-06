# Data Object Model

## Role

This document defines the shared names and relationships for benchmark data
objects. It does not define which objects are lawful members of Task1 or
Task2; those decisions belong to the corresponding task contracts.

## Object Layers

| Object | Meaning | Primary owner |
| --- | --- | --- |
| Raw observation | A source-native signature or single-cell row before benchmark aggregation | Source-specific preprocessing |
| Treated cell/signature | A retained perturbation observation linked to source metadata | Source-specific preprocessing |
| Control cell | A source-native control observation eligible for scPerturb pairing | [scPerturb preprocessing](preprocessing/scperturb.md) |
| Delta instance | One aggregated perturbation-response vector in delta space | Source preprocessing and [Task1](../tasks/task1.md) |
| Representation | A feature-space vector for one delta instance, such as `Gene`, `Pathway`, or scoped `FM` | [Gene](representations/gene.md), [Pathway](representations/pathway.md), [FM](representations/fm.md) |
| Unit | A task-defined comparison group or cohort | [Task1](../tasks/task1.md) or [Task2](../tasks/task2.md) |
| Snapshot surface | A manifest-backed collection of registries and representation matrices | [Task1 snapshot](snapshots/task1.md) |

Every perturbation row that enters the current source-local Task1 bundle maps
to one aggregated delta instance. A delta instance is not a raw observation,
a raw cell embedding, or a scalar distance.

## Shared Identity Fields

The harmonized instance metadata uses these fields:

| Field | Definition |
| --- | --- |
| `instance_id` | Persisted instance-level key with the readable composite format `{dataset}::{cell_line}::{perturbation_type}::{perturbation_gene}::{time_hr_or_NA}::{dose_um_or_NA}::{source_trace}` |
| `dataset` | Source dataset identity |
| `cell_line` | Harmonized cellular background field; source-specific extraction is defined by preprocessing contracts |
| `perturbation_type` | Benchmark vocabulary: `chemical` or `genetic` |
| `perturbation_gene` | Canonical perturbation identity; chemical rows use target-set strings, genetic rows use one gene by default |
| `time_hr` | Explicit numeric perturbation time in hours, or `NA` |
| `dose_um` | Explicit dose converted to micromolar when a convertible molar unit is provided, or `NA` |
| `source_trace` | Source-native trace used to construct the instance key: `sig_id` for LINCS and treated `cell_id` for scPerturb |

`instance_id` is the persisted instance-level key. Any contiguous source-local
row numbering is an internal construction and ordering helper, not a required
additional identity field.

## Source Trace Keys

LINCS retains `sig_id` as its source trace. scPerturb retains a separate raw-cell
trace key:

```text
cell_id = {dataset}::{raw_internal_cell_name}
```

`cell_id` identifies the source-native treated or control cell used by the
scPerturb pairing and FM handoff. It is not a replacement for the benchmark
`instance_id`; downstream benchmark-facing tables continue to use
`instance_id`.

The source-specific extraction of `raw_internal_cell_name`, cell line,
perturbation identity, time, dose, local context, and control rows is frozen in
the [scPerturb preprocessing contract](preprocessing/scperturb.md).

## Perturbation Identity

The shared perturbation vocabulary is:

- `chemical`
- `genetic`

Chemical target-set strings use uppercase tokens, duplicate removal, stable or
alphabetical canonical ordering as specified by the source contract, and `|`
as the delimiter. Multi-target chemicals remain one instance row. Task2
membership expansion is a cohort-construction operation and does not change
the row identity field.

Genetic rows use one perturbed gene by default. The current Task1 scPerturb
internal slice is the scoped exception that may retain canonicalized multi-gene
sets. The current Task1 cross slice accepts matched single-gene genetic rows
only. These are Task1 scope rules and must not be generalized to future tasks
without an explicit contract change.

## Metadata Normalization

- `time_hr` is populated only from explicit numeric source time fields and is
  recorded in hours.
- Sentinel, invalid, or missing source time values become `NA`.
- `dose_um` is populated only from explicit numeric doses with a convertible
  molar unit.
- Accepted standardization units are `uM`, `micromolar`, and `nM`; `nM` is
  converted to `uM`.
- Mass-based units, volume units, unitless values, and other non-convertible
  encodings become `NA` in `dose_um`.
- Raw time and dose values remain in source-specific extension columns.

## Delta-Space Semantics

The instance vector represents perturbation response after the source-specific
delta construction:

- LINCS `Gene delta` is the retained Level5 signature vector directly, without
  additional normalization or clipping in the preprocessing stage.
- scPerturb `Gene delta` is the treated cell expression minus the mean of its
  deterministically sampled paired controls, without z-scoring or clipping in
  the preprocessing stage.
- FM deltas are model-latent flow-space displacement vectors constructed from
  the paired controls and treated cell; their exact handoff and acceptance
  rules are in the [FM representation contract](representations/fm.md).

The shared [Gene representation contract](representations/gene.md) records the
feature-axis and storage rules. The [Pathway representation contract](representations/pathway.md)
records the projection-specific gene handling.

## Scope And Ownership

Task-specific membership, matching, comparison direction, and lawful units are
owned by [Task1](../tasks/task1.md) and [Task2](../tasks/task2.md). Source-local
preprocessing owns source ingestion and delta construction. Snapshot assembly
owns canonical registries, block routing, and shared feature alignment. Result
schemas are owned by [task output schemas](../tasks/output_schemas.md).

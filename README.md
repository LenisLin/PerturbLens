# PerturbLens

PerturbLens is a response-centric study of cellular perturbations. It characterizes what perturbation-response information is reproducible, learnable, transferable across cellular contexts and targets, conserved across intervention and readout modalities, and compositional under combined perturbations.

The repository retains the historical `M2M-Bench` GitHub/package identifiers during migration so existing scripts, NAS paths, and audited artifacts remain traceable. The scientific project name and active study definition are now **PerturbLens**.

## Scientific Spine

The study separates four layers:

1. **Data** — perturbations, cellular contexts, readout modalities, dose/time, and combinations.
2. **State representation** — Gene, Pathway, transcriptomic FM embeddings, CellProfiler morphology features, and deep morphology embeddings.
3. **Response construction** — control-referenced delta and a Systema-style perturbation-specific reference view.
4. **Evaluation** — population similarity, instance retrieval, and out-of-sample model prediction.

The main biological-boundary ladder is:

`within -> cellular context -> target/compound -> intervention modality -> readout modality -> composition`

## Main Result Architecture

- **R1**: framework, data, representations, response construction, and evaluation definitions.
- **R2**: genetic response learnability from inner splits to unseen contexts and unseen targets.
- **R3**: chemical response learnability from inner splits to unseen contexts, unseen compounds, and unseen targets; dose/time are explanatory covariates.
- **R4**: chemical-genetic response conservation across intervention modalities.
- **R5**: transcriptomic-morphological response conservation across readout modalities.
- **R6**: compositionality and interaction structure under combined perturbations.

## Start Here

- [Documentation index](docs/README.md)
- [Project definition](docs/project.md)
- [Research proposal](docs/research/proposal.md)
- [Literature landscape and competitive position](docs/research/landscape.md)
- [Result architecture](docs/research/result_architecture.md)
- [Task/result migration map](docs/tasks/study_map.md)
- [Roadmap](docs/roadmap.md)
- [Project state](docs/governance/state.md)

## Migration Boundary

Existing Task1/Task2 contracts, outputs, scripts, and NAS paths are not silently reinterpreted. They remain valid for the historical M2M execution core until each analysis is migrated into a PerturbLens result contract. New morphology, expanded FM, model-prediction, and combination analyses require their own data/task/metric contracts before production execution.

# Figure 1: Benchmark Overview

## Status And Scope

Status: current visual design record for the Figure 1 schematic. The visual
structure is frozen for continued design review; exact geometry and some
layout choices remain open as listed below.

Figure 1 defines M2M-Bench at the schematic level. It explains what the
benchmark compares, what data objects enter the benchmark, and which readout
families are used. The benchmark question is carried by the scenario design
and manuscript prose; it is not drawn as a standalone block.

This design does not change Task1 or Task2 semantics. Those semantics are
defined in docs/tasks/task1.md and docs/tasks/task2.md.

## Controlling Sources

The current design is grounded against:

- docs/project.md
- docs/tasks/task1.md
- docs/tasks/task2.md
- docs/data/sources.md
- docs/data/object_model.md
- docs/metrics/concordance.md
- docs/metrics/retrieval.md
- docs/metrics/aggregation.md
- docs/manuscript/outline.md
- docs/visualization/standards.md

## Three-Layer Structure

Figure 1 is a three-layer schematic:

1. Scenarios
2. Data
3. Metrics

### Scenarios

The top layer defines the two benchmark scenarios:

- Task1: modality concordance
- Task2: mechanism concordance

It should use reusable visual elements rather than prose blocks.

### Data

The middle layer defines how benchmark inputs are organized before evaluation.
It should read as:

- shared upstream data sources;
- task-specific unit construction; and
- shared representation context.

It shows how lawful benchmark objects are formed and carried into comparison.

### Metrics

The bottom layer defines the benchmark evaluation summary strip. It contains
two primary readout regions, Group and Retrieval, and two companion summary
regions, Representation and Enrichment. It uses compact
pseudo-visualization cues and metric names in a summary-strip layout.

## Style Reference

The visual direction uses two references with explicit priority:

- /home/lenislin/Experiment/projects/M2M/reference/image.png is the primary
  style reference for overall layered composition, side label zones, broad
  container geometry, arrow language, pastel palette, and evaluation-strip
  rhythm.
- The latest local mockup is the secondary local element reference for the
  current icon vocabulary, local arrangement of scenario elements, and compact
  pseudo-visualization cues.

The target visual direction is a layered scientific overview rather than a
rounded-card collage.

## Scenarios Layer

### Layout

- One top-layer container.
- Two side-by-side panels of similar visual weight.
- Left panel: Task1.
- Right panel: Task2.

### Shared Visual Vocabulary

Reuse the following elements across both panels:

- one cell icon for cell_line;
- one gene badge or gene label;
- one perturbation icon family;
- one expression-outcome glyph, fixed as a small heatmap; and
- one alignment marker, fixed as ?.

### Shared Panel Grammar

Both Task1 and Task2 follow the same left-to-right visual grammar:

cell -> gene -> perturbation -> heatmap

This grammar matches the reference figure style more closely than a
flowchart-style branch diagram.

### Task1 Panel

The Task1 panel communicates whether the same cell context under the same
perturbation aligns internally and across datasets.

Use a compact stacked-lane arrangement. Each lane reads left to right and
contains:

- one cell icon;
- one gene badge or gene label;
- one perturbation icon; and
- one outcome heatmap.

Use three horizontal lanes. Label the top two LINCS and the bottom lane
scPerturb.

Comparison cues:

- one ? between the top two LINCS heatmaps to indicate internal;
- one second ? between the upper LINCS group and the lower scPerturb heatmap
  to indicate cross.

Minimal text:

- Task1
- LINCS
- scPerturb
- internal
- cross

This is a generic Task1 schematic. It conveys comparison logic without
introducing additional data or result claims.

### Task2 Panel

The Task2 panel communicates whether chemical and genetic perturbation outcomes
align within one dataset.

Reuse the Task1 left-to-right lane grammar. Use two horizontal lanes, each
containing:

- one cell icon;
- one gene badge or gene label;
- one perturbation icon; and
- one outcome heatmap.

The upper lane uses a chemical perturbation icon. The lower lane uses a CRISPR
or genetic perturbation icon. Place one ? between the two heatmaps and a small
anchor_gene badge near the two lanes.

Minimal text:

- Task2
- anchor_gene

The main message is cross-mechanism alignment.

## Data Layer

### Layout

- One middle-layer container.
- One shared source band at the top.
- One task-specific unit construction field in the middle.
- One shared representation band at the bottom.
- The source and representation bands span both task halves.
- Downward arrows connect the source band to both task-specific constructions.
- Both task-specific constructions visually feed into the representation band.

The layer reads as:

shared sources -> task-specific unit construction -> shared representation
context

### Source Band

Use one horizontal shared source band at the top of the Data layer.

Minimal text:

- LINCS | scPerturb

Semantic role:

- shared upstream dataset sources used by both Task1 and Task2.

### Task1 Data Block

The left half of the unit construction field shows how Task1 lawful
comparisons are built from the shared source band.

Recommended structure:

- repeated perturbation cues beneath the source band to imply source-side
  slice diversity; and
- funnel arrows converging into one compact Task1 unit box.

Task1 unit box:

- one boxed field-combination schematic;
- one cell_line icon;
- one perturbation_gene badge; and
- one shared lightning icon for fixed perturbation_type.

Semantic role:

- foreground the comparison-defining fields shared after source-side filtering.

### Task2 Data Block

The right half of the unit construction field shows how Task2 lawful units are
built from the shared source band.

Recommended structure:

- grouped Drug and grouped CRISPR cohort cues beneath the source band; and
- funnel arrows converging into one centered Task2 unit structure.

Task2 unit structure:

- one shared cell_line cue;
- one central anchor_gene node;
- one grouped Drug cohort on the left;
- one grouped CRISPR cohort on the right; and
- one time badge and one dose badge attached to the Drug side as secondary
  metadata.

Semantic role:

- read as a shared-node cohort structure organized around a mechanism anchor,
  rather than a single perturbation identity.

### Representation Band

Use one horizontal shared representation band at the bottom of the Data layer.

Minimal text:

- Gene | Pathway

Semantic role:

- shared representation context used by both lawful task-specific units.

## Metrics Layer

### Layout

Use one bottom-layer container formatted as an evaluation summary strip with:

- two primary summary regions;
- two narrower companion summary regions;
- primary regions carrying the main visual weight; and
- companion regions reading as narrower summary subregions on the right.

Recommended arrangement:

- left primary region: Group;
- center primary region: Retrieval;
- right companion region: Representation; and
- far-right companion region: Enrichment.

The pseudo-visualization elements follow the compact evaluation language of
the primary style reference and the local element cues of the latest mockup.

### Group Block

Combine metric names with one abstract visual cue for concordance-style
comparison:

- two small heatmaps, centroids, or profile glyphs;
- one bidirectional comparison cue between them;
- one tiny summary card made of three short vertical bars.

Minimal text:

- Group
- PCC
- Cosine
- E-distance

The summary card reads as a compact concordance-style score summary.

### Retrieval Block

Combine metric names with one abstract visual cue for query-to-gallery ranking:

- one query object on the left;
- a ranked stack or row of gallery objects on the right;
- one highlighted match in the gallery; and
- one tiny ranking card using a compact top-k stack with one highlighted match.

Minimal text:

- Retrieval
- Hit@1
- Hit@3
- Hit@5
- MRR

Direction-specific retrieval details belong in the Figure 1 legend rather than
panel text.

### Representation Block

Summarize the benchmark-wide comparison across representation spaces with:

- one Gene badge;
- one Pathway badge;
- one paired comparison marker; and
- one tiny paired-summary card using two aligned mini strips or paired bars.

Minimal text:

- Representation
- Gene
- Pathway

The block reads as a compact representation-space comparison summary.

### Enrichment Block

Summarize ranked pattern analyses with two compact ranked pseudo-plots:

- one mini plot for cell line; and
- one parallel mini plot for gene-level.

Minimal text:

- Enrichment
- cell line
- gene-level

Use compact ranked dot-strip, bar-stack, or lollipop-like patterns. They should
read as pair_mean_enrichment-style ranked summaries.

## Frozen Pseudo-Visualization Elements

The Metrics layer uses four fixed pseudo-visualization elements:

### Group

- two small outcome heatmaps placed side by side;
- one bidirectional comparison cue; and
- one tiny three-bar summary card placed nearby.

### Retrieval

- one query tile on the left;
- one ranked gallery stack on the right;
- one highlighted match tile; and
- one tiny top-k summary stack placed nearby.

### Representation

- one Gene badge;
- one Pathway badge;
- one paired comparison cue; and
- one tiny paired-summary card with two aligned mini strips.

### Enrichment

- one mini ranked plot for cell line; and
- one mini ranked plot for gene-level, each using a compact ranked dot-strip or
  lollipop pattern.

## Unresolved Visual And Layout Decisions

These decisions remain open and must not be silently resolved during rendering:

- how much of time and dose should be visible in the Task2 Data layer;
- the exact relative height of the three layers; and
- whether Task1 scenario comparison marks should be arcs, brackets, or arrows.

The related governance question about whether nested documentation directories
should be named explicitly is tracked by the governance owner and does not
change this figure design.

## Nano Banana Prompt

Use /home/lenislin/Experiment/projects/M2M/reference/image.png as the primary
style reference and the latest local mockup as the secondary local element
reference.

    Create a publication-style scientific schematic figure for a benchmark paper. Use the primary reference image as the main guide for overall composition, layer hierarchy, left-side label zones, broad containers, downward arrow flow, pastel palette, and evaluation-summary rhythm. Use the latest local mockup as a secondary guide for local element arrangement, icon vocabulary, and compact pseudo-visualization cues.

    The figure is a three-layer overview of M2M-Bench.

    Overall layout: three broad horizontal layers with left-side label boxes reading "Scenarios", "Data", and "Metrics". Use spacious rounded layer containers, strong vertical progression from top to bottom, and light inner framing that feels like a layered scientific overview.

    Top layer: a light blue rounded container titled "Scenarios". Inside it, place two side-by-side panels with balanced visual weight.

    Left panel title: "Task 1 | Modality concordance". Use three compact horizontal lanes, each following the same left-to-right grammar: cell icon -> gene badge -> lightning perturbation icon -> expression heatmap. Label the top two lanes "LINCS" and the bottom lane "scPerturb". Use the same cell icon, the same gene badge, and the same lightning icon across all three lanes. Place a small question-mark comparison cue between the top two heatmaps and label it "internal". Place a second comparison cue between the upper pair and the lower scPerturb heatmap and label it "cross".

    Right panel title: "Task 2 | Mechanism concordance". Use two horizontal lanes with the same left-to-right grammar: cell icon -> gene badge -> perturbation icon -> expression heatmap. The upper lane uses a Drug icon. The lower lane uses a CRISPR icon. Place a small "anchor_gene" badge between the two lanes. Place a question-mark comparison cue between the two heatmaps to indicate alignment.

    Middle layer: a soft lavender rounded container titled "Data". Structure this layer as three horizontal bands: a top shared source band, a middle task-specific unit construction field, and a bottom shared representation band.

    At the top of the Data layer, place one shared horizontal source band labeled "LINCS | scPerturb".

    In the middle task-specific unit construction field, use the left half for Task 1 and the right half for Task 2.

    Task 1 data field: place repeated perturbation cues beneath the source band to imply source-side slice diversity, and route them with funnel arrows into a compact boxed "Task 1 unit". Inside the unit box, show a cell_line icon, a perturbation_gene badge, and a fixed lightning icon representing perturbation_type.

    Task 2 data field: place grouped Drug and grouped CRISPR cohort cues beneath the source band, and route them with funnel arrows into a centered "Task 2 unit" shared-node structure. Put a shared cell_line cue in the unit, a central anchor_gene node, a Drug cohort on the left, a CRISPR cohort on the right, and small time and dose metadata badges attached to the Drug side.

    At the bottom of the Data layer, place one shared horizontal representation band labeled "Gene | Pathway". Make the Task 1 and Task 2 unit structures visually feed into this band.

    Bottom layer: a pale rose rounded container titled "Metrics". Format this layer as an evaluation summary strip with two primary regions on the left and two narrower companion summary regions on the right.

    First primary region title: "Group". Show two transcriptomic outcome heatmaps or profile tiles with a bidirectional concordance cue between them. Add a tiny summary card made of three short vertical bars. Include the metric labels "PCC", "Cosine", and "E-distance".

    Second primary region title: "Retrieval". Show one query tile pointing to a ranked gallery of tiles, with one highlighted match. Add a tiny ranking summary card using a compact top-k stack. Include the metric labels "Hit@1", "Hit@3", "Hit@5", and "MRR".

    Third narrow companion region title: "Representation". Show a "Gene" badge paired with a "Pathway" badge, a paired comparison cue, and a tiny paired-summary card with two aligned mini strips.

    Fourth narrow companion region title: "Enrichment". Show two miniature ranked pseudo-plots, one labeled "cell line" and one labeled "gene-level", using compact ranked dot or lollipop patterns.

    Overall appearance: polished journal-ready scientific infographic, soft biomedical pastel colors, broad layered containers, balanced spacing, compact English labels, consistent heatmap language, elegant arrows, and clear top-to-bottom scientific storytelling.

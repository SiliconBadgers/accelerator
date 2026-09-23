# Cross-repository integration: current work

Provide the repository map and optional integration runner. Current work is assigned to seven teams; this repo supports their shared context and later integration.

## Assignment

No additional team assignment is created here. Support the [current seven-team work](https://github.com/SiliconBadgers/planning/blob/main/docs/team-start.md).

1. Use the team map and each repo's current issue links. Architecture owns the main diagram and shared contracts; Software owns recorded workload evidence.
2. Keep the existing MAC integration runner and its scope clear. A passing example does not validate the proposed full accelerator.
3. When integrating new components, record compatible revisions, configuration, real/stub status, commands and cross-boundary evidence.

## Starting evidence

- [Central diagram](https://github.com/SiliconBadgers/architecture/blob/main/docs/accelerator-diagram.md)
- [Recorded Software profiling package](https://github.com/SiliconBadgers/software/tree/main/experiments/llama-cpp/2026-09-22)

## Artifact locations

| Location | What belongs here |
|---|---|
| [docs/integration/](../docs/integration/README.md) | Revision manifests and reproducible combined-system evidence. Keep authoritative diagrams, RTL and recorded profiles in their owning repositories. |

## What runs today

The existing workspace runner connects the small MAC example. No full accelerator implementation or end-to-end workload result is supplied.


Follow [CONTRIBUTING.md](../CONTRIBUTING.md) before editing or committing.

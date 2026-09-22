# SiliconBadgers team repositories

These nine repositories are homes for team charters, shared understanding and
member-directed work on the accelerator project. Each explains why its team
exists, the outcomes it seeks and how its responsibilities connect to other
teams. Members decide what to investigate or build within that purpose.

## Start with the team

| Repository | Charter focus |
|---|---|
| [architecture](https://github.com/SiliconBadgers/architecture/blob/main/CHARTER.md) | Coherent system purpose, shared semantics and informed architectural choices |
| [rtl-compute](https://github.com/SiliconBadgers/rtl-compute/blob/main/CHARTER.md) | Useful arithmetic capabilities and understood compute tradeoffs |
| [rtl-memory](https://github.com/SiliconBadgers/rtl-memory/blob/main/CHARTER.md) | Storage, access and data movement that serve the workload |
| [rtl-control](https://github.com/SiliconBadgers/rtl-control/blob/main/CHARTER.md) | Understandable execution, scheduling, coordination and progress |
| [soc](https://github.com/SiliconBadgers/soc/blob/main/CHARTER.md) | Coherent hardware composition and host-visible system behavior |
| [software](https://github.com/SiliconBadgers/software/blob/main/CHARTER.md) | Workload profiling, numerical references, operation mapping, backend/runtime and host integration |
| [verification](https://github.com/SiliconBadgers/verification/blob/main/CHARTER.md) | Justified confidence in design claims and visible uncertainty |
| [physical-design](https://github.com/SiliconBadgers/physical-design/blob/main/CHARTER.md) | Physical feasibility and implementation tradeoffs |
| [accelerator](https://github.com/SiliconBadgers/accelerator/blob/main/CHARTER.md) | Combined-system understanding, integration and shared evidence |

Each team has a detailed `CHARTER.md`, high-level `OBJECTIVES.md` and a scaffold
for research, design, experiments and implementation. The RTL teams own hardware
blocks; other teams contribute across those blocks. These boundaries help
members collaborate while preserving clear ownership of shared work.

## Working from the charter

[The team guide](TEAM_GUIDE.md) explains member autonomy, the role of leads and
how teams coordinate shared decisions. Objectives describe enduring outcomes.
Members choose the questions, approaches and contribution formats that advance
them. A literature study, design explanation, experiment, prototype, useful
implementation or teaching resource can all be worthwhile contributions.

[The project layout](PROJECT_LAYOUT.md) explains where that work can live. Teams
can adapt the structure as their interests and contributions develop. There is
no assigned implementation backlog or predetermined first system milestone.

## Optional technical material

A working MAC example connects a small contract, Python reference, RTL,
independent checks and an integration runner. It is available for learning and
experimentation; it does not define the teams’ roadmap or the final accelerator.
[Example setup and scope](GETTING_STARTED.md) describes what actually runs.
Four components currently supply documentation and structure without component
implementations. This is a statement about available code, not team progress.

## Repositories and workspace

Each component is a private repository in the SiliconBadgers organization. The
initial publication contains one commit per repository with the reviewed charter
and scaffold. Draft iterations and source-reference history are not imported.
Keep checkouts as siblings when using the optional example. The
[workspace manifest](https://github.com/SiliconBadgers/accelerator/blob/main/workspace.json) describes the current files used
by that example. Shared guides are maintained in the accelerator repository.

[Validation results](VALIDATION.md) describe the checked technical scope.
[The content audit](PRIVACY-AUDIT.md) describes the privacy review and retained
source attribution.

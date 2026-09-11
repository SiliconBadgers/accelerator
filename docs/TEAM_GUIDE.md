# Working from team charters

The repositories give each team a clear purpose and a shared place to develop
knowledge. The charter explains why the team exists, the responsibilities it
stewards and the boundaries it shares with others. High-level objectives
express outcomes that can be advanced through many different contributions.

Members decide what they want to pursue within that purpose. The documents
provide context for those choices rather than a sequence of assigned projects.

## What a charter provides

Each `CHARTER.md` describes the team’s mission, responsibilities, decision
boundaries, collaborators and ways of recognizing progress. Each
`OBJECTIVES.md` expresses a small set of durable outcomes. The examples of
evidence show possible ways to learn about progress; they are not required
artifacts or measures of individual output.

Charters and objectives can evolve. A team can refine its understanding as
members learn, opportunities change or a line of inquiry proves less useful
than expected. Changes that affect another team’s responsibilities or a shared
commitment are worked through with those collaborators.

## Member-directed contributions

A member may choose a question that interests them and explain how it connects
to the charter. The work can take the form that suits the question: a literature
survey, a calculation, a design study, an experiment, a numerical model, a
prototype, an implementation, a debugging investigation, documentation or a
teaching resource. Members can also collaborate across team boundaries.

The scale can vary. A careful explanation of an assumption may be more useful
than a large implementation. An experiment that rules out an approach can
change a design decision. Making another member’s work understandable or
helping others learn a concept also contributes to the team’s capability.

Useful reflection connects the work to its purpose: what question matters,
what was learned, why it matters to the charter and how strong the supporting
evidence is. There is no prescribed set of tickets, output quota or mandatory
coding assignment.

## The role of team leads

Leads help maintain a clear charter, invite members’ ideas, connect related
interests and make the team’s context accessible. They help members find
collaborators, learning resources and a suitable scope for work they want to do.
They also help communicate findings and unresolved questions to other teams.

A lead can facilitate discussion of priorities and shared needs while leaving
members room to choose their contributions. When an effort depends on another
team, leads help the participants agree on expectations. Keeping the team’s
purpose understandable and supporting its learning are part of leadership;
maintaining an assigned coding or infrastructure backlog is not the organizing
model for these repositories.

## Autonomy and shared boundaries

Teams choose their internal methods, research directions and implementation
approaches within their charters. A local experiment can explore alternatives
without changing an established interface. Proposals become shared assumptions
when the affected teams agree to use them.

Behavior that other teams depend on needs a common understanding. Examples
include a numerical representation, command meaning, memory ordering rule,
host-visible behavior or platform constraint. Keep the agreed meaning in an
authoritative place and distinguish it from exploratory alternatives. This
allows research to remain open while collaborators can rely on established
behavior where needed.

Architecture stewards shared system definitions in collaboration with their
consumers. Component teams own their internals. Verification contributes
independent assessment. Accelerator connects system-level knowledge and evidence.
These roles do not create a hierarchy that assigns individual work across teams.

## How the responsibilities meet

| Boundary | Shared understanding |
|---|---|
| Architecture, ml-models and ml-compiler | Intended computations, representations, programming needs and system assumptions |
| Compute, memory and control | Arithmetic behavior, operand access, operation requests and progress |
| Control and SoC | Execution sequencing versus host access and hardware composition |
| SoC, software and FPGA | Reusable system behavior versus host interaction and board adaptation |
| Verification and design teams | Intended behavior, evidence supporting a claim and remaining uncertainty |
| Physical-design and design teams | Implementation assumptions, physical costs and interpreted feedback |
| Accelerator and all teams | What the combined system means, what has been demonstrated and which assumptions connect it |

Teams can refine these boundaries together as the design develops. A coupled
source module does not need to be duplicated to reflect an organizational
boundary; maintain one authoritative implementation while its ownership and
interfaces are being understood.

## Structure that supports the work

`research/` holds studies and source interpretation. `docs/` holds design
explanations, proposals and learning material. `experiments/` holds exploratory
work and its interpretation. Component-specific directories such as `rtl/`,
`src/`, `tb/`, `flows/` or `constraints/` provide homes for implementations when
members choose work that needs them.

A folder is an available place for work, not a request to fill it. Teams can
extend or reorganize their structure. [PROJECT_LAYOUT.md](PROJECT_LAYOUT.md)
explains the current scaffold, and component READMEs connect it to each charter.

## The optional MAC example

The existing MAC demonstrates one way separate components can share a contract,
reference behavior and verification evidence. It is available as material to
study or extend. It does not choose a first team project, a command-driven system
milestone, a board, an ISA, a final numerical format or a full workload target.

Reading and contributing to research or design documentation requires no tool
installation. [GETTING_STARTED.md](GETTING_STARTED.md) is for members who choose
to run the example. Each component has its own repository history; the shared
example reads the current files from sibling checkouts.

# Cross-repository integration starting material

September 22, 2026. Initial investigations for team discussion; no personal assignments or deadlines.

## Shared starting points

- [Editable architecture diagram](https://github.com/SiliconBadgers/architecture/blob/main/docs/accelerator-diagram.md) and [candidate boundaries](https://github.com/SiliconBadgers/architecture/blob/main/contracts/accelerator-boundaries.md).
- [Workload cases and source shapes](https://github.com/SiliconBadgers/architecture/blob/main/docs/workload-cases.md).
- [Measured llama.cpp report](https://github.com/SiliconBadgers/software/blob/main/experiments/llama-cpp/2026-09-22/REPORT.md) and [reproduction procedure](https://github.com/SiliconBadgers/software/blob/main/experiments/llama-cpp/2026-09-22/README.md).
- [Parallel team investigations](https://github.com/SiliconBadgers/planning/blob/main/docs/team-start.md).

The diagram and engine split are proposals. Start from available shapes and
reference cases now; use explicit parameters or stubs where decisions remain
open. Software's broader profiling study is not a prerequisite. Preserve the
source revision, assumptions, commands and limits of each result. Members and
leads can choose a different investigation that resolves a relevant uncertainty.


## First useful output

A runnable model/stub walkthrough of one agreed workload slice, with an explicit
inventory of real implementations versus stubs. Connect command acceptance,
operand transfer, compute completion, write retirement and host-visible status.
This is integration evidence, not a claim of full-model inference.

## Procedure

1. Use the shared workload cases and candidate boundaries to choose a small matrix or stateful slice. Record all component revisions.
2. Compose Control's scheduler model, Memory's latency/ownership model and Compute/Verification reference behavior where available. Use declared stubs otherwise.
3. Exercise a successful command, backpressure and an outstanding-transfer fault. Preserve the traces and acceptance/completion definitions.
4. Track mismatched assumptions in a short table: boundary, producer claim, consumer expectation, consequence and owners. Do not centralize copies of component source here.
5. Publish what was actually exercised and what remains unimplemented, linking each team's evidence.

## Existing complete example

Follow [GETTING_STARTED.md](GETTING_STARTED.md) to clone the nine component
repositories into the documented sibling layout and run the existing workspace
command. That path tests the small MAC example. It does not exercise the proposed
command, memory, SoC or full-model architecture. The runner prefers `software`
and supports legacy `ml-models` directories only when `software` is absent.

Keep the shared review focused on compatible assumptions and the next useful
integration slice. Teams can develop independent models and probes in parallel;
there is no universal wait for Software or complete RTL.

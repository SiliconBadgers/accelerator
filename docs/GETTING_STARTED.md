# Optional MAC example: setup and scope

This page is for members who choose to run the supplied example. The team
charters, research and design documentation can be used without these tools.

## What is available

| Component | Existing material |
|---|---|
| architecture | [MAC contract](https://github.com/SiliconBadgers/architecture/blob/main/contracts/mac-v0.json) and a structural check |
| software | [Numerical reference](https://github.com/SiliconBadgers/software/blob/main/reference.py), [unit tests](https://github.com/SiliconBadgers/software/blob/main/tests/test_reference.py) and [vector generator](https://github.com/SiliconBadgers/software/blob/main/generate_vectors.py) |
| rtl-compute | [Signed MAC RTL](https://github.com/SiliconBadgers/rtl-compute/blob/main/rtl/pe_mac.sv), with its original MIT attribution |
| verification | [Independent testbench](https://github.com/SiliconBadgers/verification/blob/main/tb/pe_mac_smoke_tb.sv) and [runner](https://github.com/SiliconBadgers/verification/blob/main/run.py) |
| accelerator | [Local manifest](https://github.com/SiliconBadgers/accelerator/blob/main/workspace.json) and [combined runner](https://github.com/SiliconBadgers/accelerator/blob/main/workspace.py) |

The example uses signed INT8 operands and an INT32 accumulator with wraparound.
Its contract describes this primitive only. The other four components provide
charters and a documentation/implementation scaffold; runnable implementations
are not supplied for them.

## Obtain the sibling repositories

The ten core repositories are public. Use an authenticated GitHub CLI for this
checkout command; accept your organization invitation for branch push access.
From a parent workspace directory:

```sh
for repo in architecture rtl-compute rtl-memory rtl-control soc software verification physical-design accelerator; do
  gh repo clone "SiliconBadgers/$repo"
done
```

This creates the folder names expected by the example. An existing checkout can
be kept in place; clone only the siblings that are missing. The runner prefers
the `software` sibling folder and accepts an older `ml-models` folder when
`software` is absent, so an existing checkout does not need to be renamed. The
runner consumes the current checked-out files rather than selecting release
commit pins.

Before AI-assisted edits or your first commit, follow each clone's
`docs/git-ai.md` and activate its local commit guard. Installation is per
machine; repository hook activation is per clone.

## Run the example

Keep all nine component folders as siblings. Install or use an environment
with Make, Python 3.11+ and Icarus Verilog (`iverilog` and `vvp`). No Python
packages are needed for the existing example.

From the workspace root:

```sh
cd accelerator
make setup
make doctor
make test
```

The combined runner checks the current files, runs four numerical reference
tests, generates 261 deterministic vectors, and runs 131,600 RTL checks. Expected
output includes `PASS integration:`. The report also identifies the components
without implementation examples; it does not assess their charters or research.

The RTL checks cover signed arithmetic, disabled hold, clear priority, reset
and wraparound. [VALIDATION.md](VALIDATION.md) records the checked environment
and scope. Passing this example establishes no complete accelerator, board or
physical-implementation result.

## Change or inspect the example

Each component’s `SETUP.md` describes its available material and commands.
Members can study or modify the example as useful to their chosen work. Run the
relevant checks when changing behavior, and use the combined runner when an
example change affects multiple components.

The current scaffold-only Makefiles print `NOT IMPLEMENTED` and fail their
`make test` targets because no executable component test is present. Research,
design and learning contributions are interpreted on their own terms, rather
than through this code-availability check.

Run `make clean` from `accelerator` to remove generated outputs and Python
caches before sharing a snapshot. The runner reads current checkout files and does not create commits. Tools, experiments and project milestones beyond this
example are choices for the members and teams pursuing them.

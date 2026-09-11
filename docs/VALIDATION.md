# Starter validation

Verified locally on September 10, 2026, on Darwin with Python 3.14.7 and Icarus Verilog 12.0.

- Eleven plain component folders; no Git metadata, commits, remotes or commit pins.
- A fresh file export passed setup, doctor and integration, including a workspace path containing spaces.
- Four numerical reference tests, 261 model-generated golden vectors and 131,600 RTL checks passed.
- Directed RTL checks cover signed arithmetic, disabled hold, clear priority, reset and wraparound.
- Architecture, compute and verification component entry points passed with the renamed folders.
- Wrong, empty and truncated vector files failed as expected.
- Local source edits were tested directly; a missing dependency produced a clear error.
- All six implementation scaffolds returned failure from their test target.
- Cleanup removed generated outputs; the workflow created no Git metadata.

Scope: the signed MAC starter only. Full accelerator migration, control, memory,
SoC integration, a compiler, board operation, physical implementation, Ubuntu/WSL
execution and GitHub CI remain unvalidated. These checks concern the file export;
repository visibility and history are verified separately during publication.

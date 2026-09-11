# accelerator: optional example setup

No tools are required to read the charter or contribute research and design
material. The commands below apply only to the existing technical example.

## Existing example

A local manifest and runner connect the MAC contract, reference, RTL and independent checks. This demonstrates one narrow integration path.

Prerequisites: Make, Python 3.11+ and Icarus Verilog (`iverilog` and `vvp`). The current Python code uses the standard library.
Keep the component folders as siblings for the provided cross-component paths.

From this component directory:

```sh
make setup
make doctor
make test
```

These commands check the current example files. The combined MAC example can be
run from the sibling `accelerator` folder using the same commands. It exercises
four model tests, 261 reference vectors and 131,600 RTL checks. It establishes
no full-accelerator, board or physical-implementation claim.

Run `make clean` from `accelerator` to remove generated build outputs and Python
caches before sharing a folder snapshot. The runner reads the current sibling
files and does not create commits.

## Example files

- [workspace.py](workspace.py)
- [workspace.json](workspace.json)

For the shared example, see the [workspace checkout guide](https://github.com/SiliconBadgers/accelerator/blob/main/docs/GETTING_STARTED.md).

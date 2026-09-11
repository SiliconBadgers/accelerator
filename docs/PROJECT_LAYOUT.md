# Project layout

The expected structure starts with each team’s charter and objectives, followed
by places for member-directed research, design, experiments and implementation.
The structure supports the charter; it does not assign work or require every
folder to be filled. Teams can adapt it as their interests and work develop.

## Common structure in every team repository

```text
team-repository/
  README.md           purpose and entry point
  CHARTER.md          detailed mandate, boundaries and member autonomy
  OBJECTIVES.md       high-level outcomes with illustrative evidence
  SETUP.md            optional technical examples and their scope
  research/           studies, literature and comparisons
  docs/               design explanations, proposals and learning material
  experiments/        exploration, prototypes and interpreted results
  <domain folders>/   implementation and supporting artifacts when useful
  Makefile            current technical entry points, if applicable
  .github/            future contribution template
  .gitignore          generated-file exclusions
```

Every listed directory currently exists. Domain folders vary by team as shown
below. The `.github` and `.gitignore` files are ordinary scaffold files; there
is one independent Git history per component. Git metadata is omitted from this tree.

## Domain structure

The following tree complements the common charter and research structure.
Directories marked `reserved` currently contain a purpose note only. Existing
technical files are shown explicitly and remain optional example material.

```text
repo-starters/
  architecture/
    contracts/
      mac-v0.json
    decisions/  # reserved
  rtl-compute/
    rtl/
      pe_mac.sv
    tb/  # reserved
  rtl-memory/
    rtl/  # reserved
    tb/  # reserved
  rtl-control/
    rtl/  # reserved
    tb/  # reserved
  soc/
    rtl/  # reserved
    tb/  # reserved
  ml-compiler/
    examples/  # reserved
    src/  # reserved
    tests/  # reserved
  ml-models/
    fixtures/  # reserved
    tests/
      test_reference.py
    generate_vectors.py
    reference.py
  verification/
    fixtures/  # reserved
    plans/  # reserved
    tb/
      pe_mac_smoke_tb.sv
    run.py
  fpga/
    constraints/  # reserved
    host/  # reserved
    rtl/  # reserved
    tb/  # reserved
  physical-design/
    constraints/  # reserved
    flows/  # reserved
    reports/  # reserved
  accelerator/
    profiles/  # reserved
    tests/  # reserved
    workspace.json
    workspace.py
```

The repository’s own README explains how these locations relate to its charter.
For example, `rtl-control/research/` can contain a scheduling study while
`rtl-control/rtl/` can hold an implementation arising from that study. Either
can advance the charter, and neither is a required first contribution.

## Keeping knowledge connected

| Material | Suggested home |
|---|---|
| Team purpose and responsibility | `CHARTER.md` |
| Durable outcomes | `OBJECTIVES.md` |
| Literature, analyses and comparisons | `research/` |
| Design rationale, proposals and teaching material | `docs/` |
| Exploratory methods and their interpretation | `experiments/` |
| Accepted shared interface and numerical semantics | `architecture/contracts/`, with links from consumers |
| Architectural decision records | `architecture/decisions/` |
| Component implementations | Domain folders such as `rtl/`, `src/` or `flows/` |
| Checks supporting implementations | Domain folders such as `tb/` or `tests/` |
| Compact interpreted results | The relevant study or experiment; `physical-design/reports/` for curated implementation reports |
| Large generated outputs | Local `build/` directories |

Research proposals can explore alternatives to an accepted contract. Make their
status clear so a consumer can distinguish exploratory ideas from behavior it
can rely on. Each implementation or accepted specification has an authoritative
home; consumers link to or use it through an explicit interface.

The existing model entry points and integration runner remain at component roots
so the working example keeps its current commands. Their locations can evolve
through member-led work with the affected consumers kept in agreement.

## Shared workspace documents

- [README.md](REPOSITORIES.md) is the charter index.
- [TEAM_GUIDE.md](TEAM_GUIDE.md) explains autonomy, lead stewardship and collaboration.
- [GETTING_STARTED.md](GETTING_STARTED.md) describes the optional MAC example.
- [VALIDATION.md](VALIDATION.md) records the tested technical scope.
- [PRIVACY-AUDIT.md](PRIVACY-AUDIT.md) records the content-review scope and attribution exception.

The eleven components are private organization repositories. The structure
prescribes no assigned backlog or fixed first milestone.

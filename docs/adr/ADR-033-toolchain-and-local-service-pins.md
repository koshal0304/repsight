# ADR-033 — Toolchain and local-service pins: pnpm, uv and Docker image tags

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-10-23 |
| Drafted by | Claude Code (E0-T01) |
| Decides | Tech lead (HITL-09) |
| Scope | pnpm and uv pins (E0-T01). Docker image tags for local services are added by E0-T04 |

## Context

05 §4.1 leaves two pins to E0: pnpm ("pinned in root `package.json` `packageManager`") and uv ("pinned in `pyproject.toml` `[tool.uv] required-version`"), both recorded here. Node 22.13.x and Python 3.14.8 are already pinned by canon §10.2 and 05 §4.1. This ADR records only how the repo enforces them. GR-17 and NFR-038 require exact pins and committed lockfiles.

## Decision

**Selection rule:** use the newest release published at least 14 days before the pin date (2026-10-23, so on or before 2026-10-09). A brand-new release gets two weeks for regressions and supply-chain incidents to surface.

| Tool | Pin | Released | Enforced by |
|---|---|---|---|
| pnpm | **12.10.1** | 2026-10-06 | `package.json` `packageManager` with sha512 hash (corepack checks it); pnpm also records its own binary with integrity hashes in `pnpm-lock.yaml` |
| uv | **0.12.24** | 2026-10-08 | `pyproject.toml` `[tool.uv] required-version = "==0.12.24"`: any other uv version refuses to run in the repo |
| Node.js | 22.13.1 (canon: 22.13.x) | 2025-01-21 | `.nvmrc`; `package.json` `engines.node = "22.13.x"` with `engineStrict: true` (pnpm fails with `ERR_PNPM_UNSUPPORTED_ENGINE` on any other version) |
| Python | 3.14.8 (canon §10.2) | — | `.python-version` (uv downloads it if missing); `requires-python = ">=3.14.8,<3.15"` in each member |
| Docker images | *E0-T04 adds them here* | — | `docker-compose.yml` tags |

`pnpm-workspace.yaml` also sets `savePrefix: ''`, so `pnpm add` writes exact versions.

## Alternatives

1. **Latest releases (pnpm 12.15.0 from 2026-10-21, uv 0.13.5 from 2026-10-22).** Rejected because each was only 1–2 days old at pin time. uv 0.13.5 is the version Homebrew currently installs.
2. **pnpm 11.28.x (previous major).** Rejected because pnpm 12 has been the current major since 2026-08-26, and starting on 11 would force a major upgrade soon.
3. **Version ranges (`^12`, `>=0.12`).** Rejected because they break GR-17 and NFR-038.

## Consequences

- Every developer and CI runner needs **exactly** uv 0.12.24. A Homebrew uv will not match. Install it with `curl -LsSf https://astral.sh/uv/0.12.24/install.sh | sh`, or run it through `uvx --from uv==0.12.24 uv …`.
- Node needs a version manager that reads `.nvmrc` (fnm, nvm). Run `corepack enable` once so `pnpm` resolves to 12.10.1.
- **Risk to review:** Node 22.13.1 dates from January 2025. The 22.x LTS line is now at 22.23.4 (2026-10-20), and the releases in between carry security fixes. The canon pins 22.13.x as the Expo SDK 58 floor. Moving to a later 22.x patch needs a new ADR (and a canon edit if the line changes).
- Bumping any pin means a new ADR, an updated lockfile and an updated `tools/ci/tests/test_workspace.py` (it asserts the Node and Python pins).

## Evidence

Run on 2026-10-23, macOS arm64, Node 22.13.1 (fnm), corepack 0.36.0, uv 0.12.24 (via `uvx`):

- `corepack use pnpm@12.10.1` wrote the hashed `packageManager` field and `pnpm-lock.yaml`. `pnpm install --frozen-lockfile` then reported "Already up to date".
- On Node 25.4.0, `pnpm install --frozen-lockfile` exited 1 with `ERR_PNPM_UNSUPPORTED_ENGINE`.
- Homebrew uv 0.13.5 run in the repo printed: ``Required uv version `==0.12.24` does not match the running version `0.13.5` ``.
- `uv lock` → `uv sync --frozen` installed CPython 3.14.8 and pytest 9.1.1.
- `pnpm check:all` passed: 4 tests in `tools/ci/tests/test_workspace.py`.
- Registry dates: `npm view pnpm time`; `https://pypi.org/pypi/uv/json`.

## Rollback plan

Revert the E0-T01 commit. It holds no data or schema. Developers then go back to whatever pnpm and uv they had installed.

## Links

05 §4.1, §4.4, §4.6, §10.4 · canon §10 · 02 Appendix C (ADR-033) · NFR-038 · GR-17 · HITL-09

# ADR-035 — Python dev tooling pins: ruff, mypy, pytest, httpx2, uv_build

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-10-23 |
| Drafted by | Claude Code (E0-T03) |
| Decides | Tech lead (HITL-09) |
| Scope | Python dev tools at the uv workspace root, the build backend for `services/api` and `services/worker`, and two licences outside the GR-11 list. The runtime pins (FastAPI, Uvicorn, Pydantic, pydantic-settings, Celery) come from canon §10.2 and need no ADR |

## Context

E0-T03 adds the first Python services. 05 §5.2 names the tools (`ruff check` and `ruff format`, `mypy --strict`, `pytest`), and 02 §12.4 runs Ruff and mypy on every PR. The canon pins none of them. GR-17 and NFR-038 require exact pins. 05 §5.6 requires an ADR for a new dependency that is not on an allowlist, and no allowlist exists yet (E0-T05 adds the SDK allowlist).

## Decision

**Selection rule:** the same as ADR-033 and ADR-034. Use the newest stable release published at least 14 days before the pin date (2026-10-23, so on or before 2026-10-09).

| Package | Pin | Released | Why |
|---|---|---|---|
| `ruff` | **0.17.0** | 2026-10-09 | Lint and format (05 §5.2); rules F, E, W, I, B, S, UP |
| `mypy` | **2.4.0** | 2026-10-01 | `strict = true` on `services/api/app` and `tools/` (05 §5.2) |
| `pytest` | 9.1.1 | 2026-06-19 | In use since E0-T01; moved from `tools/ci` to the root group so it is written once |
| `httpx2` | **2.13.1** | 2026-09-23 | HTTP client behind FastAPI's `TestClient`. Starlette 1.9.0 deprecates `httpx` there and imports `httpx2` first |
| `uv_build` | 0.12.24 | 2026-10-08 | Build backend for `repsight-api` and `repsight-worker`, so `app` and `worker` import from the repo root (`pnpm api:dev`, `pnpm worker:dev`, pytest). It ships with uv, so it matches the uv pin in ADR-033 |

The four dev tools sit in one `[dependency-groups] dev` list in the root `pyproject.toml`; tool settings sit in the same file. `uv_build` is pinned in each service's `[build-system]`.

**Licences.** The lockfile holds 46 third-party packages. 31 of them are the runtime closure of `repsight-api` and `repsight-worker` (`uv tree --no-dev`); the rest are dev-only.

| Licence | Packages |
|---|---|
| MIT | 23 |
| BSD (3-clause, or "BSD" in metadata) | 16 |
| Apache-2.0 | 2 |
| Apache-2.0 OR BSD-2-Clause / Apache-2.0 OR BSD-3-Clause | 1 / 1 |
| BSD-2-Clause | 1 |
| **PSF-2.0** | 1 (`typing-extensions` 4.16.0, runtime) |
| **MPL-2.0** | 1 (`pathspec` 1.1.1, dev-only) |

There is no AGPL, SSPL, RSAL or non-commercial licence. **Two licences are not on the GR-11 list**, and GR-11 says "anything else needs an ADR":

- **PSF-2.0** covers `typing-extensions`. Pydantic and FastAPI require it, so it ships in the API and worker images. The PSF License 2.0 is a permissive, OSI-approved licence.
- **MPL-2.0** covers `pathspec`, which mypy requires. It is a dev tool, never shipped. MPL-2.0 is a file-level copyleft licence: its terms apply to MPL files that are modified and distributed, and we use the package unmodified.

**Accepting this ADR accepts PSF-2.0 for runtime dependencies and MPL-2.0 for dev tooling.**

## Alternatives

1. **`httpx` 0.28.1.** It works, but Starlette 1.9.0 prints a deprecation warning for it and points to `httpx2`. Rejected so the test client does not start on a deprecated path. `httpx` also pulls in `certifi` (MPL-2.0), and `httpx2` uses `truststore` (MIT) instead.
2. **Hatchling or setuptools as the build backend.** Either one can package `worker` as a single file, `services/worker/worker.py` (the name in 05 §6.3). Rejected because each adds a build tool and its own dependencies. `uv_build` only builds packages, so the worker module is `services/worker/worker/__init__.py`. `celery -A worker` works the same way.
3. **Virtual projects (`package = false`) with path settings.** Rejected because `celery --workdir` changes the working directory before the app is imported, so `.env` at the repo root would not load.
4. **Dev tools declared in each member.** Rejected for the reason ADR-034 gives: one root list is the least to keep in step.
5. **The newest releases** (`ruff` 0.17.2, `httpx2` 2.16.0). Rejected because each was less than 14 days old at pin time.

## Consequences

- **Transitive versions follow the resolver, not the 14-day rule.** `uv lock` picked the newest compatible versions. Five of them were less than 14 days old at pin time: `starlette` 1.9.0, `python-dateutil` 3.0.0 (a new major), `tzlocal` 5.4.5, `wcwidth` 0.9.3 and `ast-serialize` 0.13.1. ADR-034 accepted the same behaviour for npm. uv's `exclude-newer` setting could enforce the rule, but it would also block the canon pins newer than the cutoff (`fastapi` 0.143.3, `pydantic` 2.14.1, `pydantic-settings` 2.16.0) unless each one is excepted. The tech lead decides whether to adopt it.
- **E0-T04 must settle the Celery broker client.** Canon §10.2 pins redis-py 8.1.0, but kombu 5.6.2 (Celery's transport) declares `redis>=4.5.2,<6.5` for its `redis` extra. This task does not add redis-py, so the Celery app loads but cannot reach a broker yet. E0-T04 brings up Valkey and can test redis-py 8.1.0 against it. That task records the outcome in `docs/DECISIONS.md`, and in a new ADR if a pin changes.
- pytest-asyncio and Hypothesis (05 §5.2) are not added yet, because no async or property test exists. The first task that needs them pins them under this ADR's selection rule.
- Ruff 0.17 also formats Python code blocks inside Markdown. The root config excludes `*.md`, so `ruff format` never rewrites the spec docs, which change only through owner-approved PRs.
- Bumping any pin here needs a new ADR (02 §3.10) and an updated `uv.lock`.
- 02 Appendix C needs a row for ADR-035, added in a docs PR for the tech lead (05 §10.4 step 2).

## Evidence

Run on 2026-10-23, macOS arm64, Node 22.13.1, pnpm 12.10.1, uv 0.12.24, CPython 3.14.8:

- Release dates and dependency ranges came from `https://pypi.org/pypi/<package>/<version>/json`.
- `pnpm check:all` passed: ESLint and Prettier on 3 packages, ruff on 8 Python files, `tsc` on 2 packages, mypy on 5 files, 2 Jest tests and 9 pytest tests.
- `uvicorn app.main:app` answered `200 {"status":"ok"}` on `/healthz` and `/readyz`.
- `celery -A worker report` found the app, then stopped at kombu's Redis transport because redis-py is not installed (see Consequences).
- Each deliberate violation failed:
  - `assert` in `app/` (ruff `S101`)
  - an unformatted file (`ruff format --check`)
  - an untyped function (mypy `no-untyped-def`)
  - `/healthz` returning another body (`test_health_checks_return_200`)
  - a `>=` range in a service manifest (`test_nfr_038_python_dependencies_are_pinned_exactly`)
- Licences came from installed package metadata (`importlib.metadata`), and from PyPI for the two packages not installed on macOS (`colorama`, `httpx2-jsfetch`).

## Rollback plan

Revert the E0-T03 commits. They hold no data or schema, and the repository goes back to having no Python services.

## Links

05 §4.1, §5.2, §5.6, §6.3, §10.4 · 02 §3.3, §3.10, §12.3, §12.4, Appendix C · canon §10.2 · GR-11, GR-17 · NFR-038 · ADR-033, ADR-034 · HITL-09

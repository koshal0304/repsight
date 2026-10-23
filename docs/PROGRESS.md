# RepSight — Build Progress

| Field | Value |
|---|---|
| Last updated | 2026-10-23 (before W1; W1 starts 2026-11-02) |
| Updated by | Claude Code, session for E0-T03 (reviewer: tech lead) |
| Phase | 0 — Foundations & CV spike (W1–W6) |
| Next milestone | M1, 2026-12-11 (canon §14.2) |
| `main` at last verification | `27d03f3` (local `pnpm check:all` on a clean clone; see "Last verified gates") |

## Waiting for human

| Item | Question | Asked | Task | Who signs |
|---|---|---|---|---|
| **WAITING FOR HUMAN: HITL-09** | Accept ADR-035 (Python dev tool pins ruff 0.17.0, mypy 2.4.0, httpx2 2.13.1, `uv_build` 0.12.24; PSF-2.0 for runtime `typing-extensions` and MPL-2.0 for dev-only `pathspec`)? The PR holds until then (05 §10.4 step 4) | 2026-10-23 | E0-T03 | Tech lead |

## Current task

| Field | Value |
|---|---|
| Task | E0-T03 — Python skeleton |
| Branch / PR | `e0/e0-t03-python-skeleton`; PR not opened yet |
| Status | IN PROGRESS |
| Last commit | `9b220da` Merge pull request #3 (E0-T02) |
| Next step | Run `pnpm check:all` on a clean clone of the branch, push, open the PR; then HITL-09 for ADR-035 |
| Resume prompt | "Continue E0: next open task in docs/PROGRESS.md." |

## Epic status

| Epic | Name | Weeks | Gate | Status | Tasks done | Current / next task | Blocker or HITL | PRs |
|---|---|---|---|---|---|---|---|---|
| E0 | Repo bootstrap and CI | W1 | M1 | IN PROGRESS | 2/9 | E0-T03 (in progress) | HITL-09 (ADR-035) | #1, #2, #3 |
| E1 | Backend foundation | W1–W10 | M2 | NOT STARTED | 0/11 | E1-T01 | — | — |
| E2 | Mobile foundation | W2–W10 | M2 | NOT STARTED | 0/10 | E2-T01 | — | — |
| E3 | PoseEngine and camera pipeline | W1–W12 | M1, M2 | NOT STARTED | 0/12 | E3-T01 | — | — |
| E4 | Exercise engine | W3–W23 | M1, M2, M3 | NOT STARTED | 0/13 | E4-T01 | — | — |
| E5 | Workout player, programs, session sync | W9–W24 | M2, M4 | NOT STARTED | 0/10 | E5-T01 | — | — |
| E6 | Medication profile and constraint engine | W5–W27 | M2, M3, M4 | NOT STARTED | 0/13 | E6-T01 | — | — |
| E7 | AI coach | W4–W24 | M2, M3 | NOT STARTED | 0/13 | E7-T01 | — | — |
| E8 | Nutrition and meal scans | W12–W17 | M2 | NOT STARTED | 0/5 | E8-T01 | — | — |
| E9 | Progress, quality volume, benchmarks | W14–W27 | M2, M3, M4 | NOT STARTED | 0/4 | E9-T01 | — | — |
| E10 | Subscriptions, paywall, quotas | W12–W27 | M2, M4 | NOT STARTED | 0/5 | E10-T01 | — | — |
| E11 | Privacy and compliance features | W7–W27 | M2, M4 | NOT STARTED | 0/7 | E11-T01 | — | — |
| E12 | Analytics, notifications, observability | W10–W27 | M2, M4 | NOT STARTED | 0/5 | E12-T01 | — | — |
| E13 | Internal tools | W4–W22 | M1, M2, M4 | NOT STARTED | 0/6 | E13-T01 | — | — |
| E14 | Beta readiness and launch | W19–W31 | M3, M4, M5 | NOT STARTED | 0/9 | E14-T01 | — | — |
| E15 | Post-launch V1.x and V2 | W32–W74 | M6–M10 | NOT STARTED | per release (05 §6.18) | — | — | — |

## Tasks of active epics

| Task | Status | PR | Requirement IDs proven | Tests added | Notes |
|---|---|---|---|---|---|
| E0-T01 | DONE | [#1](https://github.com/koshal0304/repsight/pull/1) (merged, `885a510`) | NFR-038 (partial: toolchain pins exact, lockfiles committed; the full pin checker comes with the E0 linters) | `tools/ci/tests/test_workspace.py`: `test_nfr_038_toolchain_pins_are_exact`, `test_env_example_defines_every_playbook_variable`, `test_root_scripts_cover_playbook_bootstrap_commands`, `test_gr_12_env_file_is_git_ignored` | ADR-033 Accepted 2026-10-23 (HITL-09). Script bodies for code that does not exist yet (`db:seed`, `worker:dev`, `admin:dev`, `gen:api`, `harness`) follow the 05 §3.1 layout; the task that builds each one confirms or adjusts it |
| E0-T02 | DONE | [#2](https://github.com/koshal0304/repsight/pull/2) (merged, `27d03f3`); acceptance recorded in #3 | NFR-038 (partial: every npm manifest pinned exactly) | `packages/exercise-engine/test/smoke.test.ts`, `packages/contracts/test/smoke.test.ts`, `tools/ci/tests/test_workspace.py`: `test_nfr_038_npm_dependencies_are_pinned_exactly` | ADR-034 Accepted 2026-10-23 (HITL-09). Prettier runs with its defaults plus `.editorconfig`. The React Hooks and React Native accessibility rules (05 §5.1) come with `apps/mobile` in E2-T01; ADR-034 lists the ESLint 10 support gaps E2 must settle |
| E0-T03 | IN PROGRESS | — | NFR-038 (partial: every Python manifest pinned exactly) | `services/api/tests/test_health.py`: `test_health_checks_return_200` (`/healthz`, `/readyz`); `services/worker/tests/test_worker.py`: `test_worker_takes_broker_url_from_settings`; `tools/ci/tests/test_workspace.py`: `test_nfr_038_python_dependencies_are_pinned_exactly` | ADR-035 drafted (Proposed, HITL-09). Root `lint`, `typecheck` and `test` now run ruff, mypy and every pytest suite. `services/worker` is a script directory that `pnpm worker:dev` and pytest put on `PYTHONPATH`; `services/api` is an installed package. Settings hold only `celery_broker_url`; each later task adds the fields it reads. `/readyz` checks nothing until E1 adds the DB and Valkey clients |
| E0-T04 | NOT STARTED | — | — | — | Add the Docker image tags to ADR-033. **Settle the broker client:** canon pins redis-py 8.1.0, but kombu 5.6.2 declares `redis<6.5` for its `redis` extra. Test 8.1.0 against the local Valkey, then log the outcome in `docs/DECISIONS.md` (and write an ADR if a pin changes). Until then `pnpm worker:dev` stops at kombu's Redis transport (ADR-035) |
| E0-T05 | NOT STARTED | — | NFR-032, NFR-024, BR-23 | — | Linters go into the existing `tools/ci` project |
| E0-T06 | NOT STARTED | — | — | — | Runs on `koshal0304/repsight` (private, personal account; HITL-12 answered 2026-10-23). SAST for TypeScript means adding ESLint security rules to `packages/config/eslint.config.js` (02 §10.13) |
| E0-T07 | NOT STARTED | — | — | — | ADR-033 already drafted in E0-T01; T07 adds the template, ADR-001 and ADR-002 |
| E0-T08 | NOT STARTED | — | — | — | This file exists already; T08 adds `docs/DECISIONS.md` (DEC-001..DEC-012) and checks this file against 05 §10.2 |
| E0-T09 | NOT STARTED | — | — | — | — |

## Blockers

| ID | Since | Task | Blocker | Kind (technical / HITL / external) | Needs | Workaround in use |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## Last verified gates

| Gate | Command or CI job | Result | Run ID / evidence | Commit | Date |
|---|---|---|---|---|---|
| Local checks | `pnpm install --frozen-lockfile && uv sync --frozen && pnpm check:all` on a clean clone | PASS (ESLint and Prettier on 3 packages, `tsc` on 2, 2 Jest tests, 5 pytest tests) | Local run on a fresh clone of `main` from GitHub, macOS arm64, Node 22.13.1, pnpm 12.10.1, uv 0.12.24, CPython 3.14.8; Linux not run yet (needs CI, E0-T06) | `27d03f3` (`main`) | 2026-10-23 |
| CI on `main` | `ci.yml` | not run yet (E0-T06) | — | — | — |
| Golden harness | `pnpm harness` / `harness.yml` | n/a until E4-T05 | — | — | — |
| Safety eval | `pnpm eval:safety -- --mode mock` / `safety-eval.yml` | n/a until E7-T11 | — | — | — |
| Device lab | `device-lab.yml` (PERF-30 results file) | n/a until E3-T06 | — | — | — |
| Milestone exit | canon §14.2 criteria for the next milestone | not yet | — | — | — |

## Open deviations from the spec

| DEC | Spec reference | What differs | Code marker | Status |
|---|---|---|---|---|
| — | — | — | — | — |

## Session log (newest first, last 20 entries)

| Date | Task | What was done | Gates run | Next step |
|---|---|---|---|---|
| 2026-10-23 | E0-T03 | `services/api` (package `app`, FastAPI 0.143.3) with `/healthz`, `/readyz` and pydantic-settings; `services/worker` Celery 5.6.3 stub that reads its broker URL from settings; ruff, mypy (strict) and pytest config in the root `pyproject.toml`; root `lint`, `typecheck` and `test` extended; Python pin test added; ADR-035 drafted | `pnpm check:all` in the working tree (ESLint and Prettier on 3 packages, ruff on 8 Python files, `tsc` on 2, mypy on 5 files, 2 Jest tests, 9 pytest tests); uvicorn answered 200 on both health routes; each deliberate violation failed | Clean-clone check, push, open the PR; HITL-09 for ADR-035 |
| 2026-10-23 | E0-T02 | PR #2 merged (`27d03f3`), so E0-T02 is DONE. HITL-09 answered after the merge: ADR-034 accepted as written, including BlueOak-1.0.0 for dev tooling. Recorded in PR #3 | `pnpm check:all` on a clean clone of `main` at `27d03f3` (ESLint and Prettier on 3 packages, `tsc` on 2, 2 Jest tests, 5 pytest tests) | Merge #3; then E0-T03 in a new session |
| 2026-10-23 | E0-T02 | PR #1 merged (`885a510`), so E0-T01 is DONE. `packages/config` holds the shared `tsconfig.base.json` (05 §5.1 flags) and ESLint flat config (typescript-eslint strict type-checked, a reason required on every disable). `packages/exercise-engine` and `packages/contracts` are empty, with one Jest smoke test each. Root JS dev tools pinned exactly; ADR-034 drafted; dependency build scripts denied through `allowBuilds`; npm pin test added | `pnpm check:all` on a clean clone of `d7540df` (ESLint and Prettier on 3 packages, `tsc` on 2, 2 Jest tests, 5 pytest tests); deliberate violations each failed. PR #2 opened | Review #2 and HITL-09 for ADR-034; then E0-T03 |
| 2026-10-23 | E0-T01 | HITL-12 answered: a human created the private repo `koshal0304/repsight` and pushed `main` and the task branch. Claude Code opened PR #1 | — | Review and merge #1; E0-T02 |
| 2026-10-23 | E0-T01 | ADR-033 accepted (HITL-09). Developer machine set up with uv 0.12.24 and corepack on Node 22.13.1. Repo creation and push blocked by the session's permission rules (HITL-12 still open) | `pnpm check:all` in a fresh interactive shell (4 passed) | Human creates the repo and pushes; then E0-T02 |
| 2026-10-23 | E0-T01 | pnpm and uv workspaces, root scripts (05 §4.4), `.editorconfig`, `.gitignore`, `.env.example` (all 65 §4.5 variables), pins (pnpm 12.10.1, uv 0.12.24, Node 22.13.1, Python 3.14.8), lockfiles, ADR-033 draft, workspace tests | `pnpm check:all` on a clean clone of `ee8e5ea` (4 passed) | Tech lead review and HITL-09; then E0-T02 |

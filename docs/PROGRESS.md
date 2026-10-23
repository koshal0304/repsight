# RepSight — Build Progress

| Field | Value |
|---|---|
| Last updated | 2026-10-23 (before W1; W1 starts 2026-11-02) |
| Updated by | Claude Code, session for E0-T01 (reviewer: tech lead) |
| Phase | 0 — Foundations & CV spike (W1–W6) |
| Next milestone | M1, 2026-12-11 (canon §14.2) |
| `main` at last verification | — (no gate has run on `main` yet; `main` is `7d4cd5c`) |

## Waiting for human

| Item | Question | Asked | Task | Who signs |
|---|---|---|---|---|
| — | — | — | — | — |

## Current task

| Field | Value |
|---|---|
| Task | E0-T01 — Workspace skeleton |
| Branch / PR | `e0/e0-t01-workspace-skeleton` / [#1](https://github.com/koshal0304/repsight/pull/1) |
| Status | IN REVIEW |
| Last commit | `ee8e5ea` chore(E0-T01): workspace skeleton with pinned toolchain (plus the PROGRESS-only commit after it) |
| Next step | Tech lead reviews and merges #1. Meanwhile, E0-T02 can start from this branch (shared TS and lint config; one Jest test each in `packages/exercise-engine` and `packages/contracts`) |
| Resume prompt | "Continue E0: next open task in docs/PROGRESS.md." |

## Epic status

| Epic | Name | Weeks | Gate | Status | Tasks done | Current / next task | Blocker or HITL | PRs |
|---|---|---|---|---|---|---|---|---|
| E0 | Repo bootstrap and CI | W1 | M1 | IN PROGRESS | 0/9 | E0-T01 (in review) → E0-T02 | — | #1 |
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
| E0-T01 | IN REVIEW | [#1](https://github.com/koshal0304/repsight/pull/1) | NFR-038 (partial: toolchain pins exact, lockfiles committed; the full pin checker comes with the E0 linters) | `tools/ci/tests/test_workspace.py`: `test_nfr_038_toolchain_pins_are_exact`, `test_env_example_defines_every_playbook_variable`, `test_root_scripts_cover_playbook_bootstrap_commands`, `test_gr_12_env_file_is_git_ignored` | ADR-033 Accepted 2026-10-23 (HITL-09). Script bodies for code that does not exist yet (`db:seed`, `worker:dev`, `admin:dev`, `gen:api`, `harness`) follow the 05 §3.1 layout; the task that builds each one confirms or adjusts it |
| E0-T02 | NOT STARTED | — | — | — | Jest smoke tests land here |
| E0-T03 | NOT STARTED | — | — | — | API pytest smoke test (`/healthz`) lands here; extend root `lint`/`typecheck`/`test` with ruff, mypy and `services/api` |
| E0-T04 | NOT STARTED | — | — | — | Add the Docker image tags to ADR-033 |
| E0-T05 | NOT STARTED | — | NFR-032, NFR-024, BR-23 | — | Linters go into the existing `tools/ci` project |
| E0-T06 | NOT STARTED | — | — | — | Runs on `koshal0304/repsight` (private, personal account; HITL-12 answered 2026-10-23) |
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
| Local checks | `pnpm install --frozen-lockfile && uv sync --frozen && pnpm check:all` on a clean clone | PASS (4 tests) | Local run, macOS arm64, Node 22.13.1, pnpm 12.10.1, uv 0.12.24, CPython 3.14.8; Linux not run yet (needs CI, E0-T06) | `ee8e5ea` | 2026-10-23 |
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
| 2026-10-23 | E0-T01 | HITL-12 answered: a human created the private repo `koshal0304/repsight` and pushed `main` and the task branch. Claude Code opened PR #1 | — | Review and merge #1; E0-T02 |
| 2026-10-23 | E0-T01 | ADR-033 accepted (HITL-09). Developer machine set up with uv 0.12.24 and corepack on Node 22.13.1. Repo creation and push blocked by the session's permission rules (HITL-12 still open) | `pnpm check:all` in a fresh interactive shell (4 passed) | Human creates the repo and pushes; then E0-T02 |
| 2026-10-23 | E0-T01 | pnpm and uv workspaces, root scripts (05 §4.4), `.editorconfig`, `.gitignore`, `.env.example` (all 65 §4.5 variables), pins (pnpm 12.10.1, uv 0.12.24, Node 22.13.1, Python 3.14.8), lockfiles, ADR-033 draft, workspace tests | `pnpm check:all` on a clean clone of `ee8e5ea` (4 passed) | Tech lead review and HITL-09; then E0-T02 |

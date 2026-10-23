# RepSight — standing rules for Claude Code

RepSight is an iOS and Android strength-training app for adults 18+. It gives on-device camera form feedback, uses a deterministic, medication-aware safety and constraint layer, and has a grounded AI coach (general wellness, never medical care).

## Document map

| Document | Use it for |
|---|---|
| [docs/research/00-product-canon.md](docs/research/00-product-canon.md) | The tie-breaker: names, IDs, prices, dates, pins, never-rules, owner decisions (§18), **settled decisions (§0.8)** |
| [docs/01-business-requirements-document.md](docs/01-business-requirements-document.md) | What to build and how it is accepted: FR-###, NFR-###, BR-## |
| [docs/02-technical-specification.md](docs/02-technical-specification.md) | How to build it: interfaces, schema, endpoints, §6 PERF-## targets, §7 coach and safety |
| [docs/03-product-roadmap-and-strategy.md](docs/03-product-roadmap-and-strategy.md) | Phases, milestones, scope-cut order (§2.8) |
| [docs/04-innovative-features.md](docs/04-innovative-features.md) | Why IF-1..IF-7 exist and their safe wording |
| [docs/05-build-playbook.md](docs/05-build-playbook.md) | How to build: layout, epics E0–E15 (§6), gates (§7), HITL (§8), prompts (§9), tracking (§10), build risks (§11) |
| [docs/research/](docs/research/) | Evidence briefs R1–R6; never a source of new requirements |
| `docs/PROGRESS.md`, `docs/DECISIONS.md`, `docs/adr/` | Build state, DEC-### log, ADR-### records (formats in 05 §10) |

Precedence when they disagree (05 §1.3): canon → 01 for requirements → 02 for technical detail and performance numbers → 03 for sequencing → 05 for process and layout. Log every conflict in `docs/DECISIONS.md` (05 §1.4).

## Golden rules (short form; the full list is 05 §2, GR-01–GR-18)

**Privacy**
- Raw video never leaves the phone, except one clip the user explicitly shares (CON-09, V1.2). No frame is written to disk; no pixels cross into JavaScript.
- Face landmarks 0–10 are dropped in native code (Swift/Kotlin) before any buffer reaches JS.
- Keypoint series stay on the phone unless the user grants CON-08; session sync carries per-rep metrics only.
- The age gate runs first, before account creation; an under-18 user never gets an account or auth identity, only an anonymous counter (canon §0.8 #1).
- Never log health values; use `pseudo_id`, never `user_id`, email or name.

**Safety**
- No dosing logic, ever: no dose calculator, no take/skip/change advice, no insulin, carbohydrate-dose or electrolyte advice, no numeric glucose or blood-pressure thresholds in user copy.
- Medication guidance comes only from clinician-approved cards and rules (KB-<CLASS>-##, RULE-<CLASS>-##), rendered verbatim. Rules decide; the LLM explains.
- Never-rules 1–9 each have deterministic tests and eval items; any failure blocks release.
- Red flags and crisis use fixed `TPL-*` templates with regional numbers. They work offline and are never metered or paywalled, and the model never writes red-flag text.
- Eating-disorder safeguards are never disabled. These include the kcal-floor flags of 1,200 kcal/day (women) and 1,800 kcal/day (men).
- **No invented clinical content.** Do not write medical facts, thresholds, card text, screening rules, swap tables or red-flag wording. Write a `CLINICAL_REVIEW_REQUIRED` placeholder and stop (HITL-01).
- Claims: no treat/prevent/diagnose/cure, no canon §2.4 phrase, no "first/only/unique". The coach is "the RepSight coach (AI)".

**Engineering**
- No ad, attribution or tracking SDKs. PostHog receives allowlisted events only, with no health values, free text, autocapture or replay.
- No AGPL, SSPL, RSAL or non-commercial code, models or datasets (no Ultralytics YOLO, Sapiens, ML Kit Pose, research-only datasets, Redis binaries).
- Secrets never go in code, Git history or logs. Use `.env` locally (git-ignored) and AWS Secrets Manager when deployed.
- WCAG 2.2 AA on every screen. Every cue has audio, haptic and caption. Touch targets are ≥44 pt (iOS) and ≥48 dp (Android). Layouts must work at the largest text size.
- Pinned versions only (05 §4.1). Never install "latest". A pin change needs an ADR.
- Units are stored in SI and converted only at the UI layer. Use they/them in all copy, tests and seed data.

## Claude API

- **Before writing any Claude API code, load the `claude-api` skill.**
- Use `claude-opus-5-5` on every route until owner decision D-02 says otherwise. No other model ID appears outside eval config.
- Follow 02 §7 where it overrides the skill's defaults:
  - Server-side model fallbacks are off. A refusal returns `TPL-REFUSAL-01`.
  - Do not use API citations with structured outputs (`output_config.format`); together they return a 400. Grounding works this way: tools return KB cards, the reply lists `kb_card_ids`, the server validates them, and the app renders each card verbatim with its sources (ADR-011).
  - No Batch or Files API with user data. Import the `anthropic` package only in `app.llm`. Tools are strict and only read or propose. Payloads are minimised.
- CI uses `LLM_MODE=mock` (recorded fixtures). Live calls use eval-only keys.

## Repository layout (05 §3)

```text
apps/mobile/            Expo SDK 58 / RN 0.88 app (development builds only, never Expo Go)
packages/pose-engine/   Nitro native module (Swift + Kotlin); the only code that touches pixels
packages/exercise-engine/  pure TypeScript rep/rule/cue engine, same code on phone and in CI
packages/contracts/     shared JSON Schemas
packages/api-client/    generated from services/api/openapi.yaml (never hand-edited)
services/api/           FastAPI modular monolith, Python package `app`; migrations, seeds, tests
services/worker/        Celery worker and beat entry points
tools/admin/            RepSight Studio (FastAPI + Jinja2 + HTMX)
tools/ci/               linters: banned claims, model IDs, forbidden APIs, placeholders, SDKs, licences
content/                exercises, cues, kb-cards, rules, safety, claims, programs (signed releases)
analytics/events.yaml   analytics allowlist
ml/                     datasets register, labelling, golden harness, calibration, evals, device lab
infra/terraform/        AWS per env x cell
docs/                   spec pack, research, adr, PROGRESS.md, DECISIONS.md, runbooks
```

02 uses older path names; read them through the map in 05 §3.3.

## Commands

<!-- E0-T09 replaces this block with the real scripts. Until then these are the targets from 05 §4.4. -->
```bash
pnpm install --frozen-lockfile && uv sync --frozen   # install
pnpm services:up && pnpm db:migrate && pnpm db:seed  # local services, schema, seeds
pnpm api:dev | pnpm worker:dev | pnpm admin:dev      # run backend, worker, Studio
pnpm gen:api                                         # OpenAPI -> packages/api-client
pnpm mobile:prebuild && pnpm mobile:ios | pnpm mobile:android
pnpm lint && pnpm typecheck && pnpm test             # fast checks
pnpm harness                                         # golden-video harness
pnpm eval:safety -- --mode mock                      # safety eval, recorded fixtures
pnpm check:all                                       # every CI gate that runs locally
```

## How to work

1. At session start, read this file and `docs/PROGRESS.md` (current task, waiting-for-human items, blockers). Then read the current epic in 05 §6 and the sections of 01, 02 and the canon that it names. Check `git status` and `git log` against PROGRESS.
2. One task = one session = one branch (`e<epic>/<task-id>-<slug>`) = one PR, normally under 600 changed lines. Use Conventional Commits with the task ID as scope, for example `feat(E4-T03): …`.
3. Work in small, committed, resumable steps. Commit after every green step, and update "Next step" in PROGRESS in the same commit (05 §11 BK-10).
4. Tests go in the same PR. Name tests after the requirement they prove (`test_fr_012_…`). Meet the definition of done in 05 §7.7.
5. Grep 01 and 02 for every FR, NFR, BR, PERF, section, endpoint and table you cite, so that each one really exists.
6. Update `docs/PROGRESS.md` in every PR. Log conflicts and deviations in `docs/DECISIONS.md` and mark deviating code `SPEC-DEVIATION(DEC-###)` (05 §10.5). Draft an ADR (`Proposed`) for any pin, dependency, data-flow, model-route or signing change (05 §5.6, §10.4).
7. Never merge your own PR. Never edit 01–04 or the canon unless the owner approves that docs PR.

## Stop and ask (05 §8)

Prepare the material, then write `WAITING FOR HUMAN: HITL-## — <one-line question>` at the top of the session summary and in `docs/PROGRESS.md`. Never mark the item done yourself.

| HITL | Stop when |
|---|---|
| 01 | Any clinical content: KB card, rule, `med_class_map`, screening rule, progression, swap table, nutrition formula, red-flag wording, lexicon, eval expected answer |
| 02 | Legal or user-facing compliance text: privacy, consent, terms, subscription, store, disclaimers |
| 03 | Regulatory or market decision: new market, IF-6 (D-09), GLP-1 wording (D-16), memos, Usage Policy reading |
| 04 | Any safety-eval failure or production never-rule hit |
| 05 | Terraform apply to staging/prod, prod migrations, any production or research-account data |
| 06 | Any change to safety behaviour: guards, templates, crisis numbers, never-rule tests, quota bypass, ED-safe logic, regional policy |
| 07 | New or changed cue, benchmark or debrief copy |
| 08 | Thresholds from real data; Beta → GA cue promotion |
| 09 | D-05, D-12, ADR acceptance, a new dependency outside the allowlists |
| 10 | Model routing, model or prompt changes (D-02, D-08, `llm_routes`) |
| 11 | Payment configuration: products, prices, trials, offerings, partner codes |
| 12 | New accounts, API keys, credentials, licence or data downloads |
| 13 | Store submission or tester distribution |
| 14 | New datasets, pretrained weights or licence questions |

Also stop when:
- a conflict touches safety, privacy, legal text, money or clinical content (05 §1.4);
- a pinned version cannot install;
- a milestone gate looks likely to fail (05 §11);
- the working tree holds changes you cannot explain.

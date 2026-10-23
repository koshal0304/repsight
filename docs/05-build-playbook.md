# RepSight — Build Playbook for Claude Code

| Field | Value |
|---|---|
| Document | 05 — Build Playbook for Claude Code |
| Version | 1.1 |
| Date | 2026-10-18 |
| Status | Draft for review |
| Owner | Tech lead |
| Related documents | `01-business-requirements-document.md` (BRD) · `02-technical-specification.md` (Tech Spec) · `03-product-roadmap-and-strategy.md` (Roadmap) · `04-innovative-features.md` (IF deep dives) · `/CLAUDE.md` (standing rules for the build agent) · `docs/research/00-product-canon.md` (canon v1.0) · `docs/research/R1..R6` (evidence) |

## Table of contents

1. [How to Use This Pack](#1-how-to-use-this-pack)
2. [Golden Rules](#2-golden-rules)
3. [Repository Layout](#3-repository-layout)
4. [Toolchain & Environment Setup](#4-toolchain--environment-setup)
5. [Engineering Conventions](#5-engineering-conventions)
6. [Build Sequence (Epics E0-E15)](#6-build-sequence-epics-e0-e15)
7. [Testing & Quality Gates](#7-testing--quality-gates)
8. [Human-in-the-Loop Checkpoints](#8-human-in-the-loop-checkpoints)
9. [Copy-Paste Prompts for Claude Code](#9-copy-paste-prompts-for-claude-code)
10. [Progress Tracking](#10-progress-tracking)
11. [Build Risks & How to Handle Them](#11-build-risks--how-to-handle-them)

**What this document is.** A step-by-step plan that lets Claude Code (the build agent) build RepSight in a fresh repository, safely and verifiably, with the three-person founding team in canon §14.3. It turns the requirements in 01 and the design in 02 into ordered work: 16 epics (E0–E15), each split into tasks that fit one Claude Code session, each with tests and a "definition of done".

**What this document is not.** It does not repeat requirements, architecture or business reasoning. It points to them by file and section number.

---

## 1. How to Use This Pack

### 1.1 Who does what

| Actor | Role in the build |
|---|---|
| Claude Code (build agent) | Writes code, tests, migrations, docs updates and ADR drafts, one task per session. Follows `/CLAUDE.md` and this playbook. Never approves its own clinical, legal, store or payment work. |
| Tech lead (founding engineer, mobile + backend) | Starts sessions, reviews and merges every pull request (PR), owns 02 and 05, decides technical conflicts, records ADRs. |
| ML/CV engineer | Owns E3, E4 and the data programme (F-112, F-113); reviews every PR that touches `packages/pose-engine`, `packages/exercise-engine`, `content/exercises` or `ml/`. |
| CEO / product owner (founder) | Decides scope and owner decisions (D-##), signs legal and store items, decides conflicts between requirements. |
| Clinical reviewers, counsel | Sign off clinical content and legal text (§8). Claude Code prepares drafts and stops. |

### 1.2 Reading order

Claude Code reads these files at the start of the build and the relevant parts again at the start of each epic (each epic in §6 lists its own context files).

| Order | File | Read | Why |
|---|---|---|---|
| 1 | `/CLAUDE.md` | All | Standing rules; short |
| 2 | `docs/05-build-playbook.md` (this file) | §1–§5, §7, §8, then the current epic in §6 | How to work |
| 3 | `docs/research/00-product-canon.md` | §0 (including §0.8 settled decisions), §1 principles, §2.4, §5, §7, §8, §9, §10, §11 | Names, IDs, pins and never-rules |
| 4 | `docs/01-business-requirements-document.md` | §7.4 (FR-001–FR-078), §8 (NFR-001–NFR-040), §9 (BR-01–BR-30), Appendix A | What to build and how it is accepted |
| 5 | `docs/02-technical-specification.md` | The sections named by the epic | How to build it |
| 6 | `docs/03-product-roadmap-and-strategy.md` | §2 (phases), §2.8 (scope-cut order) | When, and what to cut first |
| 7 | `docs/04-innovative-features.md` | §3 for the IF the epic touches; §5 sequencing | Why a feature exists and its safe wording |
| 8 | `docs/research/R1..R6` | Only the section a document cites | Evidence; never a source of new requirements |

### 1.3 Precedence when documents disagree

| Topic | Winning document | Example |
|---|---|---|
| Names, IDs, prices, dates, pinned versions, never-rules, owner decisions, settled decisions (§0.8) | **Canon** (`docs/research/00-product-canon.md`) — the tie-breaker for everything | A version in 02 differs from canon §10 → canon wins |
| Requirements and acceptance criteria | **01 BRD** | An FR acceptance criterion vs a 02 sequence diagram |
| Performance targets the canon did not set (API latency, chat first token, availability, battery, cold start, memory, app size) | **02 §6** (PERF-##); BRD NFRs cite the same PERF ID and number (canon §0.8 #7) | NFR-011 cold start vs PERF-04 → PERF-04 |
| Technical detail (interfaces, schema, endpoints, algorithms) | **02 Tech Spec** | Field names, table names, error codes |
| Sequencing, milestones, scope cuts | **03 Roadmap** | Which epic slips first |
| Repository layout, process, test gates | **05 Playbook** (this file) | Folder names (§3.3 maps 02's paths) |

### 1.4 What to do when you find a conflict

1. Stop the task at a safe point (tests green or the branch untouched).
2. Apply the precedence table above as the **temporary** choice.
3. Add an entry to `docs/DECISIONS.md` (format in §10.3) with status `OPEN`, both quotes, the temporary choice and the question for the owner.
4. Tell the human in the session summary: "Conflict DEC-### needs the owner." Do not continue work that depends on the answer if the conflict touches safety, privacy, legal text, money or clinical content.
5. When the owner answers, set the entry to `DECIDED`, and if a pinned version or architecture choice changed, write an ADR (§5.6).

### 1.5 Conflicts already found while writing this pack

These are pre-filled in `docs/DECISIONS.md` by task E0-T08. Rows marked `DECIDED` were settled by canon §0.8 (2026-10-18) or by a later edit of 02; an `OPEN` row's temporary choice applies until the owner decides.

| DEC | Conflict | Decision or temporary choice | Status | Owner |
|---|---|---|---|---|
| DEC-001 | Folder names: 02 uses `backend/app/`, `packages/cv-engine`, `packages/exercise-dsl`, `content/kb/`, `evals/`, `infra/`, `api/openapi.yaml` | This playbook's layout (§3); 02's paths are mapped one-to-one in §3.3. Same code, different folder name only | OPEN | Tech lead |
| DEC-002 | Coach first-token target: NFR-010 said p95 ≤5 s; 02 §6.3 PERF-25 says p95 ≤6.0 s; an older 02 §12.2 SLO said ≤2.5 s | PERF-24 (first SSE event p95 ≤1.0 s) and PERF-25 (first reply-text token p95 ≤6.0 s) are the gates; 02 §6 owns the numbers and NFR-010 cites them (canon §0.8 #7). 2.5 s is the Claude-call budget inside a turn (02 §7.3 step 7), not an SLO | DECIDED | Tech lead |
| DEC-003 | Cold start: NFR-011 said ≤3 s p95 on Tier B; 02 PERF-04 says ≤4.0 s on Tier B | PERF-04 (p95 A ≤2.5 s, B ≤4.0 s, C ≤6.0 s) is the release gate (canon §0.8 #7) | DECIDED | Tech lead |
| DEC-004 | API latency: NFR-009 said non-LLM endpoints p95 ≤300 ms; 02 PERF-21 says sync write p95 ≤400 ms | PERF-20–PERF-23 are the gates (p95: reads ≤250 ms, sync write ≤400 ms, medicine search ≤600 ms, config ≤150 ms) (canon §0.8 #7) | DECIDED | Tech lead |
| DEC-005 | Battery: NFR-017 said ≤10% per 20-min session on Tiers A–B; 02 PERF-07 is per 30-min session by tier | PERF-07 (30-min session: A ≤10%, B ≤13%, C ≤16%) is the gate (canon §0.8 #7) | DECIDED | Tech lead |
| DEC-006 | Load-test tool: 02 named both Locust and k6 | Locust, recorded in ADR-032 (02 now names Locust only) | DECIDED | Tech lead |
| DEC-007 | Rollout stage length: 02 §4.5.4 said ≥72 h and ≥500 sets; an older 02 §12.1 said ≥48 h | ≥72 h **and** ≥500 sets (02 §4.5.4 and §12.1 now agree) | DECIDED | ML/CV engineer |
| DEC-008 | Analytics event name: `autoreg_prompt_responded` vs `autoreg_prompt_answered` | `autoreg_prompt_answered` (02 CV-23 and §13.2 now agree; §13 owns event names) | DECIDED | Tech lead |
| DEC-009 | Canon §8.4 said recording runs "W5–W14", but 2027-02-12 is the Friday of W15 (W1 = 2026-11-02) | Recording runs W5–W15, 2026-11-30 → 2027-02-12 (canon §0.8 #3) | DECIDED | CEO |
| DEC-010 | Onboarding order: earlier text created the account (F-001) before the age gate (F-002) and deleted it for under-18s | The age gate runs first, on the phone, before any sign-in. Under-18 → no account, auth identity or user row; the app calls the unauthenticated `POST /v1/public/underage-attempts` (`store_country` only) to increment the anonymous counter. `POST /v1/account/bootstrap` re-checks the date of birth (02 §8.2; canon §0.8 #1) | DECIDED | CEO |
| DEC-011 | Grounding: Claude API citations vs structured outputs | No API citations (they return a 400 with `output_config.format`). Tools return KB cards, the structured reply lists `kb_card_ids`, the output guard validates the IDs, and the app renders each card verbatim with its sources (02 §7.7.3, ADR-011; canon §0.8 #2) | DECIDED | Tech lead |
| DEC-012 | Availability: NFR-012 said ≥99.5% monthly; 02 §12.2 SLO said 99.9% | PERF-27 (02 §6.3): backend API availability ≥99.9% monthly (non-5xx on authenticated routes), enforced as the 02 §12.2 SLO; NFR-012 cites it. Coach routes degrade gracefully during an AI-provider outage (02 §7) | DECIDED | Tech lead |

Other canon §0.8 decisions this playbook applies: kcal-floor flags 1,200 kcal/day for women and 1,800 kcal/day for men, with the registered dietitian (RD) setting the default when sex is not recorded (#4; GR-07, E8); infrastructure cost of $1.08 per paying month at 10k-MAU scale (#5; §11); three design-partner clinics signed by V1.2 (M7) and still active at V1.4, KPI-26 (#6; E15); the research briefs in `docs/research/` (#9; §1.2). Where 01–04 still show an older value, canon §0.8 wins (§1.3) and the mismatch is logged as a DEC entry.

---

## 2. Golden Rules

These rules are **non-negotiable**. A PR that breaks one is not merged, even if every test passes. Each rule names how it is enforced, so a break is caught by a machine first and a human second.

| ID | Rule | Enforced by | Source |
|---|---|---|---|
| GR-01 | **Raw video never leaves the phone**, except one clip the user explicitly shares (CON-09, V1.2). No frame is written to disk. No pixels cross into JavaScript. | Static grep gate on file-write APIs in `packages/pose-engine` (02 CV-07); network privacy test (NFR-023); release-build file-system diff | Canon §0.6, §11.2; BR-18 |
| GR-02 | **Face landmarks 0–10 are dropped in native code** (Swift/Kotlin) before any buffer reaches JS. Only `headInFrame` and one derived `headPitchDeg` number are allowed. | Native buffer-length test (02 CV-05) | Canon §8.1; R-11 |
| GR-03 | **Keypoint series stay on the phone** unless the user grants CON-08. Session sync carries per-rep metrics only. | Payload contract test (02 CV-28) | Canon §0.7, §11.2 |
| GR-04 | **No dosing logic, ever.** No dose calculator, no "take/skip/change your dose", no insulin, carbohydrate-dose or electrolyte advice, no numeric glucose or blood-pressure thresholds in user copy. | Never-rule unit tests; output guard; banned-claims linter; safety eval (KPI-07 = 0) | Canon §9.6 never-rules 1–4; BR-04 |
| GR-05 | **Medication guidance comes only from clinician-approved rule cards** (KB-<CLASS>-##, RULE-<CLASS>-##), rendered verbatim. The LLM explains; rules decide; the LLM cannot override a rule. | Plan validator; KPI-09 grounding check; publish pipeline requires clinician sign-off | Canon principle 3; BR-07, BR-20 |
| GR-06 | **Red-flag and crisis routing** uses fixed templates (`TPL-*`) with regional numbers (US, UK, India), works offline, in every tier, and never counts against a quota. The model never writes red-flag text. | Template tests per market; offline test; quota test (BR-02) | Canon §9.6; BR-01–BR-03, BR-06 |
| GR-07 | **Eating-disorder safeguards** (ED-safe mode, kcal-floor flags 1,200 kcal/day for women and 1,800 kcal/day for men with the RD-set default when sex is not recorded, loss cap 0.9 kg/week, helplines) are never disabled by a tier, flag or experiment. | Unit tests; safety eval ED items | Canon §9.6, §0.8 #4; BR-05, BR-25 |
| GR-08 | **Never-rules 1–9 are unit-tested.** Every never-rule has at least one deterministic test and eval items. Any failure blocks release. | `services/api/tests/safety/test_never_rules.py`; CI gate | Canon §9.6; KPI-07 |
| GR-09 | **No invented clinical content.** Claude Code never writes medical facts, thresholds, card text, screening rules, swap tables or red-flag wording. It writes a placeholder marked `CLINICAL_REVIEW_REQUIRED` and stops. CI blocks any release build or content release that contains that marker. | `tools/ci/check_clinical_placeholders.py` (E0) on release branches and in `publish-content` | Canon §9.4–§9.6; BR-20 |
| GR-10 | **No ad, attribution or analytics SDK may receive health data.** No ad or attribution SDKs at all. PostHog gets allowlisted events with no health values, no free text, no autocapture, no replay. | SDK allowlist check; `analytics/events.yaml` allowlist; event-property linter | Canon §10.4–§10.5; NFR-024 |
| GR-11 | **Licences:** no AGPL, SSPL, RSAL or non-commercial code, models or datasets (no Ultralytics YOLO, Sapiens/Sapiens2, research-licensed datasets, ML Kit Pose, self-hosted Redis binaries). Apache-2.0, MIT, BSD, ISC, CC0, CC BY are fine; anything else needs an ADR. | Licence scanner in CI (npm and Python); dataset register in `ml/datasets/REGISTER.md` | Canon §8.2, §8.4, §10.5 |
| GR-12 | **Secrets never in code**, never in Git history, never in logs. Local secrets in `.env` (git-ignored); deployed secrets in AWS Secrets Manager. | Secret scan on every PR; pre-commit hook | 02 §10.4 |
| GR-13 | **Accessibility WCAG 2.2 AA.** Every cue has audio + haptic + caption; every control has a screen-reader label; touch targets ≥44×44 pt (iOS) and ≥48×48 dp (Android); layouts work at the largest OS text size. | Lint rules; Maestro accessibility checks; audit before M4 | NFR-028, NFR-029 |
| GR-14 | **Anthropic Usage Policy compliance.** The policy effective 2026-11-12 treats medication recommendations and symptom triage as high-risk and excludes fixed rules and wellness content ([R3 #1](https://www.anthropic.com/aup)). Keep the coach within fixed rules, AI disclosure at each session start, 18+ only. | Safety eval; disclosure UI tests | Canon §9.8, R-01 |
| GR-15 | **Before writing any Claude API code, load the `claude-api` skill and follow it.** Use `claude-opus-5-5` on every route until D-02 says otherwise. No other model ID may appear (`claude-sonnet-5-5` and `claude-haiku-5-5` only in eval config until an ADR-027 entry moves a route). No Batch or Files API with user data; no server-side model fallbacks; **no API citations** (they cannot be combined with structured outputs; grounding uses server-validated `kb_card_ids` and verbatim cards, 02 §7.7.3, ADR-011); the `anthropic` package is imported only in `app.llm`. | Model-ID linter; forbidden-API linter (02 §12.4) | Canon §0.3, §0.8 #2, §9.1–§9.2; BR-23 |
| GR-16 | **Claims rules.** No treat/prevent/diagnose/cure claims, no phrase from canon §2.4, no "first", "only" or "unique" in any user-facing or store text. The coach is "the RepSight coach (AI)", never a doctor, dietitian, physio or therapist. | Banned-claims linter over strings, store text, notification templates and KB cards (NFR-032) | Canon §2.4; BR-27, BR-28 |
| GR-17 | **Pinned versions only.** Never install "latest". Any change to a pinned version needs an ADR (§5.6). | Lockfiles committed; pin checker | Canon §10; NFR-038 |
| GR-18 | **Respect bodies and people.** No body-shape comment, ranking or critique; no emotion inference; they/them for any person in copy, tests and seed data. | Copy review; banned-claims linter list | Canon principle 8; never-rule 6 |

---

## 3. Repository Layout

### 3.1 Monorepo tree

One Git repository. JavaScript/TypeScript packages use **pnpm workspaces**. Python projects use one **uv workspace** with one lockfile.

```text
repsight/
├── CLAUDE.md                     # standing rules for Claude Code (≤150 lines)
├── README.md                     # human quick start
├── package.json                  # root scripts (§4.4); "packageManager" pins pnpm
├── pnpm-workspace.yaml
├── pyproject.toml                # uv workspace root (members below)
├── uv.lock
├── docker-compose.yml            # local services (§4.6)
├── .env.example                  # every variable (§4.5)
├── .github/
│   ├── workflows/                # ci.yml, harness.yml, safety-eval.yml, publish-content.yml, mobile-build.yml, infra.yml, device-lab.yml
│   ├── pull_request_template.md
│   └── CODEOWNERS
├── apps/
│   └── mobile/                   # Expo SDK 58 / RN 0.88 app (development builds only)
│       ├── app/                  # expo-router screens
│       ├── src/
│       │   ├── camera/           # VisionCamera session, frame processor, Setup Coach UI
│       │   ├── cv/               # glue: PoseEngine → exercise-engine worklet
│       │   ├── sync/             # outbox worker, payload builder
│       │   ├── db/               # SQLCipher schema, migrations, repositories
│       │   ├── features/         # onboarding, workouts, coach, nutrition, progress, settings
│       │   ├── design-system/    # tokens, components, accessibility helpers
│       │   ├── i18n/             # message catalogues (en-US first)
│       │   └── platform/         # analytics wrapper, Sentry, RevenueCat, health platforms
│       ├── plugins/              # Expo config plugins (MediaPipe packaging, D-05)
│       ├── assets/models/        # pose_landmarker_full.task, pose_landmarker_lite.task (+ sha256 manifest)
│       └── e2e/                  # Maestro flows
├── packages/
│   ├── pose-engine/              # Nitro HybridObject: Swift + Kotlin, PoseEngine.nitro.ts, BundleVerifier
│   ├── exercise-engine/          # pure TypeScript: DSL interpreter, filters, rep state machine, rules, autoregulation, cue scheduler
│   │   └── schema/               # exercise-definition.schema.json (JSON Schema 2020-12)
│   ├── contracts/                # JSON Schemas shared by app + backend (session payload, bundle envelope)
│   ├── api-client/               # TypeScript client generated from services/api/openapi.yaml (never hand-edited)
│   └── config/                   # shared eslint, prettier, tsconfig bases
├── services/
│   ├── api/                      # Python project: package `app` (FastAPI 0.143.3), migrations, seeds, tests
│   │   ├── app/                  # api/, core/, auth/, consents/, profile/, medicines/, constraints/, safety/, kb/, coach/, llm/, planner/, sessions/, nutrition/, progress/, billing/, notify/, privacy/, content/, jobs/
│   │   ├── config/               # llm_routes.<env>.yaml (signed in deployed envs)
│   │   ├── migrations/           # Alembic
│   │   ├── seeds/                # reference seeds + synthetic personas P1–P5
│   │   ├── openapi.yaml          # committed, generated; CI checks it matches the code
│   │   └── tests/
│   └── worker/                   # Celery 5.6.3 entry points (worker, beat); imports `app`; no business logic here
├── tools/
│   ├── admin/                    # "RepSight Studio": FastAPI + Jinja2 + HTMX internal UI (F-110, F-111, F-115)
│   └── ci/                       # linters: banned claims, model IDs, forbidden APIs, clinical placeholders, SDK allowlist, licences
├── content/                      # content-as-code; published as signed releases
│   ├── exercises/                # EX-01..EX-10 definitions (JSON), changelog
│   ├── cues/                     # cue copy and variants (IF-7 at V1.4)
│   ├── kb-cards/                 # <class>/<card_id>.md, front matter with sources, reviewer, review_due
│   ├── rules/                    # <class>/RULE-<CLASS>-##.yaml, med_class_map.csv
│   ├── safety/                   # lexicons/<locale>.yaml, triggers.yaml, templates/<locale>/<TPL-id>.md, crisis_routes.yaml
│   ├── claims/                   # banned.yaml (canon §2.4), claims register
│   └── programs/                 # Foundations, Home Dumbbell Strength, Gym Basics, GLP-1 Strength Track
├── analytics/
│   └── events.yaml               # allowlist (02 §13.2)
├── ml/
│   ├── datasets/                 # REGISTER.md (licence + consent scope per dataset); no data in Git
│   ├── labelling/                # Label Studio config, export converters (F-113)
│   ├── golden/                   # fixture recorder, manifest, harness runner (F-112)
│   ├── calibration/              # threshold sweeps (02 §5.4)
│   ├── evals/                    # safety eval suites, runner, rubrics (F-114)
│   └── device-lab/               # synthetic-feed scripts, results parser
├── infra/
│   └── terraform/                # modules/, cells/, envs/, global/ (02 §11.10)
└── docs/
    ├── 01..05 *.md               # this pack
    ├── research/                 # 00-product-canon.md, R1..R6
    ├── adr/                      # ADR-###-slug.md
    ├── PROGRESS.md               # §10.2
    ├── DECISIONS.md              # §10.3
    └── runbooks/                 # incident, breach, release, rollback
```

### 3.2 Purpose and owner of each top-level folder

| Folder | Purpose | Language / tool | Owner (reviewer) | Tests live in |
|---|---|---|---|---|
| `apps/mobile` | The phone app (iOS 17.0+, Android API 28+) | TypeScript ~6.0.3, Expo SDK 58 | Tech lead | `apps/mobile/src/**/__tests__`, `apps/mobile/e2e` |
| `packages/pose-engine` | The only code that touches pixels (F-020, F-101) | Swift, Kotlin, Nitro | ML/CV engineer | XCTest, JUnit, device-lab jobs |
| `packages/exercise-engine` | One implementation of the rep and rule logic, used on the phone and in CI under Node (02 §5.4) | Pure TypeScript, no React Native imports | ML/CV engineer | Jest in Node; golden harness |
| `packages/contracts` | Shared JSON Schemas; Pydantic models and TS types are generated from them | JSON Schema | Tech lead | Schema tests |
| `packages/api-client` | Generated client; regenerate with `pnpm gen:api` | TypeScript | Tech lead | Compile check |
| `services/api` | Modular monolith (02 §2.2): API, coach, safety, constraints, planner | Python 3.14.8 | Tech lead | pytest |
| `services/worker` | Celery worker and beat containers | Python | Tech lead | pytest (jobs tested in `services/api/tests/jobs`) |
| `tools/admin` | RepSight Studio (ADR-015) | Python, Jinja2, HTMX | Tech lead | pytest |
| `tools/ci` | Repository linters used by CI and pre-commit | Python | Tech lead | pytest |
| `content/*` | Clinical and coaching content; only humans with the right role approve | Markdown, YAML, JSON | Clinical lead (kb-cards, rules, safety), ML/CV engineer (exercises, cues) | Content checks in CI |
| `ml/` | Data tools, golden-video harness, eval harness | Python (`mediapipe` 1.1.1), Node for the engine | ML/CV engineer | pytest |
| `infra/terraform` | AWS infrastructure per env × cell | Terraform | Tech lead | `terraform validate`, tfsec/Checkov |
| `docs/` | Spec pack, ADRs, progress, decisions | Markdown | Tech lead | Link checker |

### 3.3 Path map from 02 Tech Spec to this repository (DEC-001)

02 names some paths before this layout existed. Read them through this table.

| Path in 02 | Path in the repo |
|---|---|
| `backend/app/…` (for example `app.safety`, `app.llm.client`) | `services/api/app/…` (Python package name stays `app`) |
| `backend/migrations/versions/` | `services/api/migrations/versions/` |
| `backend/seeds/personas/` | `services/api/seeds/personas/` |
| `api/openapi.yaml` | `services/api/openapi.yaml` |
| `config/llm_routes*` | `services/api/config/llm_routes*` |
| `packages/cv-engine` | `packages/exercise-engine` |
| `packages/exercise-dsl/schema/exercise-definition.schema.json` | `packages/exercise-engine/schema/exercise-definition.schema.json` |
| `src/native/PoseEngine.nitro.ts` | `packages/pose-engine/src/PoseEngine.nitro.ts` |
| `src/cv/`, `src/sync/` (mobile coverage targets) | `apps/mobile/src/cv/` + `packages/exercise-engine/src/`, `apps/mobile/src/sync/` |
| `content/kb/<class>/<card_id>.md` | `content/kb-cards/<class>/<card_id>.md` |
| `evals/suites/<suite_id>/items.jsonl`, `evals/run.py` | `ml/evals/suites/<suite_id>/items.jsonl`, `ml/evals/run.py` |
| `infra/modules/…`, `infra/cells/…` | `infra/terraform/modules/…`, `infra/terraform/cells/…` |
| Studio (admin ECS service) | Code in `tools/admin`, deployed as the `admin` ECS service |

CI path filters (02 §12.4 "Safety eval" row) use the repo paths: `services/api/app/llm/`, `services/api/app/safety/`, `services/api/app/coach/`, `content/kb-cards/`, `content/rules/`, `content/safety/`, `services/api/config/llm_routes*`.

### 3.4 Naming conventions

| Thing | Convention | Example |
|---|---|---|
| Folders, npm packages | kebab-case; npm scope `@repsight/` | `@repsight/exercise-engine` |
| TypeScript files | camelCase for modules, PascalCase for React components | `cueScheduler.ts`, `SetupCoach.tsx` |
| Python modules | snake_case | `app/safety/output_guard.py` |
| Database tables and columns | snake_case, plural tables, SI unit suffix, `_enc` for encrypted (02 §9.1) | `sets.load_kg`, `checkins.value_enc` |
| API paths and JSON | kebab-case paths, snake_case fields (02 §8.1) | `/v1/plan-proposals`, `tempo_s` |
| Requirement IDs in code | Cite in test names and comments where a test proves a requirement | `test_fr_012_emergency_template_offline` |
| Content files | Canon IDs as file names | `content/rules/BB/RULE-BB-01.yaml`, `content/kb-cards/GLP1/KB-GLP1-03.md` |
| Templates | `TPL-<KIND>-##` (02 §7.9.3) | `TPL-CRISIS-01` |
| Branches | `e<epic>/<task-id>-<slug>` | `e4/e4-t03-rep-state-machine` |
| Analytics events | `object_action`, past tense (02 §13.1) | `session_completed` |
| ADR files | `docs/adr/ADR-###-slug.md`, numbers from 02 Appendix C | `docs/adr/ADR-003-ios-mediapipe-packaging.md` |

---

## 4. Toolchain & Environment Setup

### 4.1 Pinned versions (copy from canon §3.3 and §10; verify at build time, change only by ADR)

| Area | Tool / package | Version | Note |
|---|---|---|---|
| Runtime (JS) | Node.js | 22.13.x | Expo SDK 58 floor [R2 §4.4] |
| Package manager (JS) | pnpm | Pinned in root `package.json` `packageManager` by E0 (ADR-033 records it) | Workspaces |
| Runtime (Python) | Python | **3.14.8** (not 3.15.0) | Canon §10.2 |
| Package manager (Python) | uv | Pinned by E0 in `pyproject.toml` `[tool.uv] required-version` (ADR-033 records it) | One workspace, one `uv.lock` |
| iOS build | Xcode | 26.4+ | iOS minimum 17.0 |
| Android build | AGP 9, Kotlin 2.0+, JDK as required by AGP 9 | — | minSdk 28, targetSdk 36, compileSdk 37 |
| Mobile framework | React Native / Expo SDK / React | **0.88.0** / **58** (`expo` 58.0.12) / 19.3.0 | Development builds only (`expo-dev-client` ~58.0.13); never Expo Go |
| Language | TypeScript | **~6.0.3** (never 7.x) | strict |
| Camera | `react-native-vision-camera` (+ `-worklets`, `-skia`) | **5.2.3** | |
| Native base | `react-native-nitro-modules` / `react-native-nitro-image` | 0.37.1 / 0.15.2 | |
| Worklets, animation, drawing | `react-native-worklets` / `react-native-reanimated` / `@shopify/react-native-skia` | 0.13.0 / 4.7.1 / 2.14.0 | Not `react-native-worklets-core` |
| Audio, haptics | `expo-speech` / `expo-haptics` | 58.0.3 / 58.0.6 | |
| Pose (native) | MediaPipe Tasks Vision Android / iOS `MediaPipeTasksVision` | 1.1.1 / 1.0.0 | iOS packaging per D-05 |
| Pose (offline, CI) | `mediapipe` (Python) | 1.1.1 | Harness and pre-labels only |
| API | FastAPI / Uvicorn / Pydantic / pydantic-settings | **0.143.3** / 0.54.0 / 2.14.1 / 2.16.0 | |
| Data access | SQLAlchemy / Alembic / asyncpg | 2.1.4 / 1.20.0 / 0.32.0 | |
| Jobs | Celery | **5.6.3** | Not arq |
| Cache client | redis-py (talks to Valkey) | 8.1.0 | |
| LLM SDK | `anthropic` | **1.15.0** | Only in `app.llm` |
| Embeddings | onnxruntime | 1.31.0 | Model chosen by ADR-007 |
| Database | PostgreSQL / pgvector (Python client) | **18.6** / **0.8.7** (0.5.1) | |
| Cache / broker | Valkey | R2 lists 9.0.6 / 9.1.2; E0 pins one for local compose | ElastiCache for Valkey in AWS |
| Pinned at M1 (ADR-006) | `expo-router`, `expo-sqlite` + SQLCipher, `expo-secure-store`, `expo-notifications`, `react-native-purchases`, `@sentry/react-native`, `posthog-react-native`, HealthKit and Health Connect libraries, i18n library | Exact versions in ADR-006 | SDK-58-compatible, New-Architecture-ready |

### 4.2 Prerequisites per operating system

| OS | Can build | Install |
|---|---|---|
| macOS (Apple silicon) | Everything (iOS, Android, backend) | Xcode 26.4+ with iOS 17+ simulators; CocoaPods (for the pinned pod, D-05); Android Studio with SDK 37 and an API 28 and API 36 emulator; Node 22.13.x (via a version manager); pnpm; uv; Docker Desktop or another OCI runtime; Maestro CLI; Terraform; AWS CLI v2; EAS CLI |
| Linux | Android, backend, `ml/`, infra (not iOS) | Same minus Xcode and CocoaPods |
| Windows | Backend and Android only through WSL2 | Use WSL2 (Ubuntu) for everything except the Android emulator |

Physical devices: at least one Tier A and one Tier B phone per platform on each engineer's desk; the full 9-phone lab (canon §3.4) is shared.

### 4.3 Accounts a human must create first (not Claude Code)

GitHub organisation; AWS accounts per 02 §11.1 (`rs-dev`, `rs-staging`, `rs-prod-us`, `rs-research`, `rs-logs`); Apple and Google **organisation** developer accounts (needs the legal entity, D-03); Expo/EAS; Anthropic organisation with dev and staging workspace keys (ZDR application, D-06); RevenueCat; PostHog (US cloud); Sentry; NLM access needed to download RxNav-in-a-Box (follow NLM's terms); fatsecret or Edamam (D-10); USDA FDC and openFDA API keys; Apple WeatherKit key (V1.0). Claude Code stops and asks when a task needs one of these (§8, HITL-12).

### 4.4 Bootstrap commands (E0 creates these scripts; until then they are the target)

```bash
# 1. Clone and install
git clone git@github.com:<org>/repsight.git && cd repsight
corepack enable                      # uses the pnpm version pinned in package.json
pnpm install --frozen-lockfile
uv sync --frozen                     # all Python workspace members

# 2. Environment
cp .env.example .env                 # fill local values; never commit .env

# 3. Local services
pnpm services:up                     # docker compose up -d (Postgres 18 + pgvector, Valkey, RxNav-in-a-Box, LocalStack)
pnpm db:migrate                      # uv run --package repsight-api alembic upgrade head
pnpm db:seed                         # reference seeds + synthetic personas P1–P5 (local only)

# 4. Run
pnpm api:dev                         # FastAPI with reload on http://localhost:8000
pnpm worker:dev                      # Celery worker + beat
pnpm admin:dev                       # Studio on http://localhost:8100
pnpm gen:api                         # export OpenAPI → regenerate packages/api-client
pnpm mobile:prebuild                 # npx expo prebuild --clean (after any native change)
pnpm mobile:ios                      # development build on simulator or device
pnpm mobile:android

# 5. Check
pnpm lint && pnpm typecheck && pnpm test
pnpm harness                         # golden-video harness on cached landmark fixtures (§7.2)
pnpm eval:safety -- --mode mock      # safety eval with recorded fixtures (no live LLM calls)
pnpm check:all                       # every CI gate that can run locally
```

### 4.5 `.env.example`

Local values only. Names and meanings follow 02 Appendix A; deployed environments read secrets from AWS Secrets Manager. "Where used": M = mobile build-time public value, A = API, W = worker, S = Studio, C = CI or tools.

| Name | Purpose | Example (local) | Where used |
|---|---|---|---|
| `ENV` | Environment name | `local` | A, W, S |
| `CELL_ID` | Region cell | `us-east-1` | A, W |
| `AWS_REGION` | AWS region (LocalStack locally) | `us-east-1` | A, W, S |
| `AWS_ENDPOINT_URL` | LocalStack endpoint (local only) | `http://localhost:4566` | A, W, S |
| `API_BASE_URL` | API base URL the app calls | `http://localhost:8000/v1` | M |
| `DATABASE_URL` | Postgres DSN (asyncpg) | `postgresql+asyncpg://rs_app:rs_app@localhost:5432/repsight` | A, W, S |
| `DB_POOL_SIZE` / `DB_MAX_OVERFLOW` | Pool sizing | `10` / `5` | A, W |
| `VALKEY_URL` | Cache, rate limits, quotas | `redis://localhost:6379/0` | A, W |
| `CELERY_BROKER_URL` | Celery broker on Valkey | `redis://localhost:6379/1` | W |
| `KMS_KEY_HEALTH_ARN` / `KMS_KEY_CHAT_ARN` / `KMS_KEY_PII_ARN` | Envelope-encryption keys | `arn:aws:kms:us-east-1:000000000000:alias/rs-health-local` | A, W |
| `KMS_SIGNING_KEY_ARN` | Content and config signing key | `arn:aws:kms:us-east-1:000000000000:alias/repsight-config-signing` | C (publish), S |
| `CONTENT_PUBLIC_KEYS` | Accepted verification keys (JSON) | `[{"kid":"local-a","pem":"-----BEGIN PUBLIC KEY-----…"}]` | A, M |
| `COGNITO_USER_POOL_ID` / `COGNITO_APP_CLIENT_ID` | Member auth | `us-east-1_localpool` / `localclient` | A, M |
| `COGNITO_ADMIN_POOL_ID` | Staff auth for Studio | `us-east-1_localadmin` | S |
| `AUTH_MODE` | `cognito` or `local-dev` (signed local tokens; refused when `ENV` is not `local`) | `local-dev` | A |
| `ANTHROPIC_API_KEY` | Dev key with a low spend limit | *(empty; set only for live runs)* | A, W, C |
| `ANTHROPIC_INFERENCE_GEO` | `global` or `us` | `global` | A, W |
| `LLM_MODE` | `mock` (recorded fixtures) or `live` | `mock` | A, W, C |
| `LLM_ROUTE_CONFIG_PATH` | Route config (model, effort, max_tokens per route × market × tier) | `services/api/config/llm_routes.local.yaml` | A, W |
| `LLM_MAX_TOOL_ROUNDS` | Tool round trips per turn | `6` | A |
| `LLM_SEMAPHORE_CHAT` / `LLM_SEMAPHORE_BACKGROUND` | Concurrency caps | `200` / `50` | A, W |
| `COACH_MAX_MESSAGE_CHARS` | Message length limit (BR-13) | `2000` | A |
| `COACH_MAX_MESSAGES_PER_HOUR` | Abuse limit (BR-13) | `30` | A |
| `COST_BREAKER_USER_MULTIPLIER` | Per-user daily cost breaker | `5` | A |
| `KB_TOP_K` / `KB_MIN_SIMILARITY` | Retrieval tuning | `6` / `0.30` | A |
| `EMBEDDING_MODEL_PATH` | ONNX embedding model (ADR-007) | `./.models/embed.onnx` | A, W |
| `RXNAV_BASE_URL` | Self-hosted RxNav-in-a-Box | `http://localhost:4000` | A |
| `OPENFDA_API_KEY` | openFDA label watch | *(secret)* | W |
| `USDA_FDC_API_KEY` | Food search | *(secret)* | A |
| `FOOD_PROVIDER` | `fatsecret` or `edamam` (D-10) | `fatsecret` | A |
| `FATSECRET_CLIENT_ID` / `FATSECRET_CLIENT_SECRET` | fatsecret credentials | *(secret)* | A |
| `OFF_USER_AGENT` | Open Food Facts User-Agent | `RepSight/0.1 (dev@<domain>)` | A |
| `WEATHERKIT_KEY_ID` / `WEATHERKIT_TEAM_ID` / `WEATHERKIT_PRIVATE_KEY` | Heat alerts (V1.0) | *(secret)* | A |
| `REVENUECAT_WEBHOOK_AUTH` / `REVENUECAT_API_KEY` | Webhook auth, server API | *(secret)* | A |
| `REVENUECAT_PUBLIC_SDK_KEY_IOS` / `REVENUECAT_PUBLIC_SDK_KEY_ANDROID` | Public SDK keys | `appl_…` / `goog_…` | M |
| `EXPO_ACCESS_TOKEN` | Push sending | *(secret)* | W |
| `SES_FROM_ADDRESS` | Transactional email | `no-reply@localhost` | W |
| `POSTHOG_API_KEY` / `POSTHOG_HOST` | Analytics (allowlisted events only) | *(empty locally = disabled)* | M, A |
| `SENTRY_DSN` | Crash reporting | *(empty locally = disabled)* | M, A, W |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Traces | `http://localhost:4317` | A, W |
| `S3_BUCKET_MEAL_PHOTOS` / `S3_BUCKET_SHARES` / `S3_BUCKET_EXPORTS` / `S3_BUCKET_CONTENT` | Buckets per cell | `rs-local-meal-photos` … | A, W |
| `MEAL_PHOTO_MAX_AGE_HOURS` | Forced delete window | `24` | W |
| `SHARE_DEFAULT_RETENTION_DAYS` / `SHARE_MAX_RETENTION_DAYS` | Clip retention (V1.2) | `30` / `365` | A, W |
| `CHAT_RETENTION_MONTHS` | Chat retention | `18` | W |
| `DELETION_SLA_DAYS` | Deletion deadline | `30` | W |
| `MIN_APP_VERSION` | Oldest supported app | `0.1.0` | A |
| `GITHUB_APP_ID` / `GITHUB_APP_PRIVATE_KEY` | Studio pull-request bot | *(secret)* | S |
| `GOLDEN_FIXTURES_URI` | Private store of recorded landmark fixtures (§7.2) | `s3://rs-research-golden/v1/` | C |

`AWS_ENDPOINT_URL`, `AUTH_MODE` and `GOLDEN_FIXTURES_URI` are added by this playbook for local work and CI; E1 adds them to 02 Appendix A through a docs PR.

### 4.6 Local services (`docker-compose.yml`)

| Service | Image (E0 pins the exact tag and records it in ADR-033) | Port | Notes |
|---|---|---|---|
| `postgres` | Official pgvector image with pgvector 0.8.7 on PostgreSQL 18 | 5432 | Init script creates `repsight`, roles `rs_app` and `rs_migrator`, extension `vector` |
| `valkey` | Official Valkey image (9.0.x or 9.1.x) | 6379 | No persistence locally |
| `rxnav` | RxNav-in-a-Box from NLM | 4000 | Downloaded by a human under NLM terms (HITL-12); the API must still start without it (search returns `upstream_error`, manual entry works, 02 §7.13) |
| `localstack` | LocalStack for S3 and KMS | 4566 | Bootstrap script creates buckets and keys from `.env` |
| `otel-collector` (optional profile) | OpenTelemetry collector | 4317 | Prints spans to stdout |

### 4.7 Seed data

| Seed | Command | Environments | Source |
|---|---|---|---|
| Exercises EX-01..EX-10 (`free_tier` true for EX-01, EX-03, EX-07, EX-08, EX-09) | `pnpm db:seed --only reference` | All | Canon §7.1; 02 §9.8 |
| Programs (Foundations, Home Dumbbell Strength, Gym Basics, GLP-1 Strength Track) | same | All | Canon §5 |
| Crisis routes US, UK, IN | same | All | Canon §9.6 (numbers copied verbatim; any change is HITL-01) |
| `med_class_map` | `pnpm content:load` | All | `content/rules/med_class_map.csv` (clinician-signed; placeholders until signed) |
| Current content releases | `pnpm content:load` | All | `content/` at the current Git SHA |
| Synthetic personas P1–P5 (fake sessions, medicines, food logs; they/them in all text) | `pnpm db:seed --only personas` | local, dev, staging only | `services/api/seeds/personas/` |

Seeds never contain real people's data. Production never receives persona seeds (the seed command refuses when `ENV=prod`).

---

## 5. Engineering Conventions

### 5.1 TypeScript

| Rule | Setting |
|---|---|
| Compiler | `strict: true`, `noUncheckedIndexedAccess: true`, `exactOptionalPropertyTypes: true`, `noImplicitOverride: true`, `useUnknownInCatchVariables: true` |
| Lint | ESLint (flat config in `packages/config`), `@typescript-eslint` strict type-checked rules, React Hooks rules, an accessibility plugin for React Native, security rules; no `any` without a `// reason:` comment |
| Format | Prettier, run by pre-commit and CI |
| Worklets | Code that runs in a worklet lives in `packages/exercise-engine` or `apps/mobile/src/cv/` and must be pure: no closures over React state, no allocation per frame in hot paths (reuse typed arrays) |
| Units | Store and compute in SI; convert only in `apps/mobile/src/i18n/units.ts` (canon §0.3) |
| API access | Only through `packages/api-client`; never hand-written `fetch` to `/v1` |

### 5.2 Python

| Rule | Setting |
|---|---|
| Lint and format | `ruff check` and `ruff format`; rule sets include pyflakes, pycodestyle, isort, bugbear, bandit (`S`), pyupgrade |
| Types | `mypy --strict` on `services/api/app`, `tools/`, `ml/evals` |
| Tests | `pytest` with `pytest-asyncio`, Hypothesis for property tests, Testcontainers for integration (02 §12.3) |
| Structure | Each domain module (`app/<domain>/`) has `router.py`, `schemas.py`, `service.py`, `repository.py`, `models.py`; routers never touch the DB directly; repositories always filter by `user_id` (02 §9.1) |
| Async | Async SQLAlchemy and asyncpg in the API; Celery tasks are sync wrappers around service functions |
| Settings | pydantic-settings only; no `os.environ` reads outside `app/core/settings.py` |

### 5.3 Commits and pull requests

- **Conventional Commits** with the task ID as scope: `feat(E4-T03): rep state machine with hysteresis`. Types: `feat`, `fix`, `test`, `docs`, `refactor`, `chore`, `ci`, `content`.
- **One task = one branch = one PR**, normally under 600 changed lines excluding generated files and fixtures.
- The PR template (`.github/pull_request_template.md`) asks: task ID; requirement IDs covered (FR/NFR/BR/CV/PERF); tests added; golden-rule check (GR-01–GR-18, tick each that applies); screenshots for UI; "needs human sign-off?" (HITL ID); docs updated (`PROGRESS.md`, `DECISIONS.md`, ADR).
- `CODEOWNERS`: `content/kb-cards/`, `content/rules/`, `content/safety/` need the clinical lead; `packages/pose-engine/`, `packages/exercise-engine/`, `content/exercises/`, `ml/` need the ML/CV engineer; everything else the tech lead.
- Merge only with green CI and one human approval. Claude Code never merges its own PR.

### 5.4 Error handling

| Layer | Rule |
|---|---|
| API | RFC 9457 problem details with the codes in 02 Appendix B; never echo health values in errors |
| PoseEngine | Never throw across the native boundary in `detect`; return `undefined` and count the error (02 §4.2.2 row 11) |
| Exercise engine | Pure functions return result objects; abstain (`not_assessed`) rather than guess (canon principle 2) |
| Mobile | Every failure mode FM-01..FM-13 has a defined user message (02 §4.12); never a blank screen; safety templates still render offline |
| Coach | Follow 02 §7.13 degraded modes D0–D3; a failure never produces free LLM text in place of a safety template |
| Data loss | Sync outbox never deletes unsent data; retries per 02 §4.12 |

### 5.5 Logging rules

- Structured JSON with the fields in 02 §12.2. Use `pseudo_id`, never `user_id`, email or name.
- **Never log health values**: no medicine names or RxCUIs, check-in values, symptoms, weights, kcal, chat text, food names, meal photos, landmarks or ERR codes linked to a person. A scrubbing processor removes known keys; a unit test feeds it a fixture of forbidden fields.
- Mobile: Sentry with PII scrubbing; no screenshots, no session replay, no breadcrumbs containing user text.
- Log levels: `error` needs an action; `warning` is unusual but handled; `info` is a state change; `debug` is off in prod.

### 5.6 Architecture decision records (ADRs)

- Location `docs/adr/ADR-###-slug.md`; numbers ADR-001–ADR-033 are pre-assigned in 02 Appendix C; new ADRs take the next free number and are added to that index by a docs PR.
- Template: Status (Proposed / Accepted / Superseded) · Context · Decision · Alternatives · Consequences · Evidence (tests, device-lab run, eval run ID) · Rollback plan · Links (D-##, DEC-###).
- Required for: any pinned version change (02 §3.10), any new dependency that is not on an allowlist, any new data flow leaving the phone, any model routing change (ADR-027), any change to the signing scheme.
- Claude Code drafts ADRs with status `Proposed`; the tech lead accepts them.

### 5.7 Feature flags and signed remote config

| Kind | Tool | Rule |
|---|---|---|
| UI experiments | PostHog flags | Never gates safety, privacy or consent behaviour |
| Paywalls and prices | RevenueCat Offerings | Prices only from canon §12.1 / BR-14 |
| Safety and product configuration (market policy F-103, class flags, kill switches `coach.enabled`, `meal_scan.enabled`, `if6.enabled`, min app version) | Our signed config (`GET /v1/config`) | ECDSA P-256 via KMS (ADR-025); app rejects unsigned or older payloads and keeps the last good one |
| Exercise definitions, cue copy, KB and rule releases, templates | Signed content manifest (`GET /v1/content/manifest`) | Staged rollout 5% → 25% → 100% (BR-21, DEC-007) |

A kill switch may turn a feature **off**; nothing may turn a safety behaviour off.

### 5.8 Internationalisation

- All user strings live in `apps/mobile/src/i18n/<locale>.json` (and Jinja2 catalogues for Studio). Zero hard-coded user strings (NFR-030); an ESLint rule flags string literals in JSX.
- Locales: en-US at MVP; en-GB V1.2; en-IN and hi-IN V1.3; es-US and de-DE V2 (canon §3.2).
- Dates ISO 8601 in storage; locale display. Units per canon §0.3.
- Crisis numbers and safety templates are per market and per locale, bundled for offline use.
- Every new string passes the banned-claims linter.

### 5.9 Accessibility checklist (every UI PR)

| # | Check |
|---|---|
| A1 | Every interactive element has an accessibility label, role and state |
| A2 | Touch targets ≥44×44 pt (iOS), ≥48×48 dp (Android) |
| A3 | Text contrast ≥4.5:1 (≥3:1 for large text and UI parts), in light and dark mode |
| A4 | Layout works at the largest OS text size without clipping |
| A5 | Every camera cue has audio + haptic + caption (02 CV-27); captions stay ≥3 s or until dismissed |
| A6 | No information by colour alone (skeleton overlay uses shape and label, not only red/green) |
| A7 | Focus order is logical; modals trap and return focus |
| A8 | Motion respects "reduce motion" |
| A9 | Timers (rest, plank) can be paused and are announced |
| A10 | WCAG 2.2 new criteria: focus not obscured, target size minimum, consistent help ("check with your clinician" always in the same place), accessible authentication (no cognitive test at sign-in), redundant entry avoided in onboarding |

---

## 6. Build Sequence (Epics E0-E15)

### 6.1 Overview: epics, phases and milestones

Weeks follow canon §0.3 (W1 starts Monday 2026-11-02). Epics overlap: two engineers each drive Claude Code sessions in parallel. "Gate" is the milestone whose exit criteria (canon §14.2) the epic must help pass.

| Epic | Name | Phase | Weeks | Gate | Driver | Features (canon §5) |
|---|---|---|---|---|---|---|
| E0 | Repo bootstrap and CI | 0 | W1 | M1 | Tech lead | F-114 (linter part) |
| E1 | Backend foundation | 0 → 1 | W1–W10 | M2 | Tech lead | F-001, F-002, F-005, F-100 (backend) |
| E2 | Mobile foundation | 0 → 1 | W2–W10 | M2 | Tech lead | F-001, F-002, F-003, F-005, F-100 (UI) |
| E3 | PoseEngine and camera pipeline | 0 → 1 | W1–W12 (spike W1–W6) | **M1**, M2 | ML/CV eng. | F-020, F-021, F-101 |
| E4 | Exercise engine | 0 → 2 | W3–W23 | M1, M2, M3 | ML/CV eng. | F-022, F-023, F-024, F-025, F-112 |
| E5 | Workout player, programs, session sync | 1 → 2 | W9–W24 | M2, M4 | Tech lead | F-026, F-040, F-041, F-042, F-044, F-052 (planner side) |
| E6 | Medication profile and constraint engine | 1 → 2 | W5–W27 | M2, M3, M4 | Tech lead | F-004, F-010, F-011, F-012, F-013, F-014, F-043 |
| E7 | AI coach | 0 → 2 | W4–W24 | M2, M3 | Tech lead | F-050, F-051, F-052, F-053, F-054, F-055, F-056, F-057, F-114 (eval part) |
| E8 | Nutrition and meal scans | 1 | W12–W17 | M2 | Tech lead | F-060, F-061, F-062 |
| E9 | Progress, quality volume, benchmarks | 1 → 2 | W14–W27 | M2, M3, M4 | ML/CV eng. | F-070, F-071, F-072, F-073 |
| E10 | Subscriptions, paywall, quotas | 1 → 2 | W12–W27 | M2, M4 | Tech lead | F-090, F-091, F-092, F-093 |
| E11 | Privacy and compliance features | 1 → 2 | W7–W27 | M2, M4 | Tech lead | F-100, F-101 (audit), F-102, F-103, F-104 |
| E12 | Analytics, notifications, observability | 1 → 2 | W10–W27 | M2, M4 | Tech lead | F-080, F-081 |
| E13 | Internal tools | 0 → 2 | W4–W22 | M1, M2, M4 | ML/CV eng. + tech lead | F-110, F-111, F-113, F-115 |
| E14 | Beta readiness and launch | 2 → 3 | W19–W31 | M3, **M4**, **M5** | CEO + tech lead | Compliance checklist items 1–13 (canon §11.6) |
| E15 | Post-launch V1.x and V2 | 4 → 5 | W32–W74 | M6–M10 | All | F-015, F-027, F-028, F-029, F-045, F-063, F-064, F-074, F-075, F-076, F-094, F-120, F-121, F-122, F-123; FR-015 |

All 69 canon features appear exactly once as a primary home above (F-052 is shared: E5 builds "Why this changed" cards for planner changes; E7 attaches them to coach proposals).

```mermaid
flowchart LR
    E0["E0 Repo and CI"] --> E1["E1 Backend foundation"]
    E0 --> E2["E2 Mobile foundation"]
    E0 --> E3["E3 PoseEngine spike"]
    E3 --> E4["E4 Exercise engine"]
    E1 --> E13["E13 Internal tools"]
    E1 --> E6["E6 Medication and constraints"]
    E13 --> E6
    E1 --> E7["E7 AI coach"]
    E6 --> E7
    E2 --> E5["E5 Workout player and sync"]
    E4 --> E5
    E6 --> E5
    E5 --> E9["E9 Progress"]
    E1 --> E8["E8 Nutrition"]
    E7 --> E8
    E1 --> E10["E10 Subscriptions and quotas"]
    E7 --> E10
    E1 --> E11["E11 Privacy and compliance"]
    E2 --> E12["E12 Analytics and notifications"]
    E5 --> E14["E14 Beta readiness"]
    E7 --> E14
    E9 --> E14
    E10 --> E14
    E11 --> E14
    E12 --> E14
    E14 --> E15["E15 V1.x and V2"]
```

### 6.2 How to read an epic

Each epic has the same parts. **Tasks** are ordered; one task = one Claude Code session = one PR. The task's files are the main ones to create; tests sit next to them. **Acceptance** cites requirement IDs from 01 (FR/NFR/BR) and 02 (CV/ML/PERF). **Definition of done** adds to the general checklist in §7.7. **Human** lists the HITL checkpoints (§8) the epic hits.

---

### 6.3 E0 — Repo bootstrap and CI (W1)

**Goal.** A fresh monorepo where every later task starts with working lint, type-check, test and safety linters in CI.
**Prerequisites.** GitHub organisation; this pack copied into `docs/` and the canon into `docs/research/00-product-canon.md`.

| Task | What to build | Files / modules |
|---|---|---|
| E0-T01 | Workspace skeleton: pnpm workspace, uv workspace, root scripts from §4.4, `.editorconfig`, `.gitignore`, `.env.example` (§4.5) | `package.json`, `pnpm-workspace.yaml`, `pyproject.toml`, `.env.example` |
| E0-T02 | Shared TS and lint config; empty `packages/exercise-engine` and `packages/contracts` with one passing Jest test each | `packages/config/*`, `packages/*/package.json`, `tsconfig.base.json` |
| E0-T03 | Python skeleton: `services/api` with FastAPI app, `/healthz`, `/readyz`, settings, ruff/mypy/pytest config; `services/worker` with Celery app stub | `services/api/app/main.py`, `app/core/settings.py`, `services/worker/worker.py` |
| E0-T04 | `docker-compose.yml` with Postgres 18 + pgvector, Valkey, LocalStack (RxNav as optional profile); bootstrap scripts | `docker-compose.yml`, `infra/local/*` |
| E0-T05 | Repository linters: banned claims (reads `content/claims/banned.yaml`, seeded from canon §2.4), model IDs, forbidden APIs (Batch/Files, `fallbacks`, wrong `inference_geo`), clinical placeholders (`CLINICAL_REVIEW_REQUIRED`), SDK allowlist, licence check | `tools/ci/*.py`, `content/claims/banned.yaml`, `tools/ci/sdk_allowlist.yaml` |
| E0-T06 | GitHub Actions `ci.yml` (lint, types, unit tests, linters, secret scan, SAST, dependency audit) with path filters; pre-commit hooks | `.github/workflows/ci.yml`, `.pre-commit-config.yaml` |
| E0-T07 | PR template, CODEOWNERS, ADR template, ADR-001, ADR-002 and ADR-033 drafts (status Proposed) | `.github/*`, `docs/adr/*` |
| E0-T08 | `docs/PROGRESS.md` and `docs/DECISIONS.md` in the §10 formats, pre-filled with E0–E15 and DEC-001–DEC-012 (§1.5) | `docs/PROGRESS.md`, `docs/DECISIONS.md` |
| E0-T09 | Fill the "Commands" block in `/CLAUDE.md` with the real scripts | `CLAUDE.md` |

**Acceptance.** NFR-032 (linter runs on every build, 0 hits), NFR-038 (lockfiles committed, pin checker passes), NFR-024 (SDK allowlist check exists), BR-23 (model-ID linter rejects any ID outside the three canon IDs).
**Tests.** Each linter has pytest cases with a positive and negative sample (for example a file containing "prevents injuries" fails; a file containing "Cues to help you keep good form" passes).
**Definition of done.** `pnpm check:all` passes on a clean clone on macOS and Linux CI runners; CI takes under 10 minutes.
**Demo.** Open a PR that adds the string "AI doctor" to a JSON file → CI fails on the banned-claims linter with the file and line.
**Human.** HITL-12 (accounts), tech lead accepts ADR-001, ADR-002 and ADR-033.

---

### 6.4 E1 — Backend foundation: auth, users, consents, OpenAPI (W1–W10)

**Goal.** A secure, region-ready API skeleton with auth, account bootstrap, age gate, profile, consents, audit and the OpenAPI → TypeScript pipeline.
**Prerequisites.** E0. Read 02 §8.1–§8.4, §9.1–§9.4 (tables `users`, `underage_attempts`, `user_keys`, `profiles`, `consent_records`, `devices`, `audit_log`, `idempotency_keys`), §10.2–§10.4, §10.8, Appendix A–B.

| Task | What to build | Files / modules |
|---|---|---|
| E1-T01 | Alembic setup, naming and lock rules (02 §9.7); base tables `users`, `underage_attempts`, `user_keys`, `audit_log`, `idempotency_keys` with `home_region` CHECK | `services/api/migrations/`, `app/core/db.py` |
| E1-T02 | Field-level envelope encryption (AES-256-GCM, per-user data key wrapped by KMS; LocalStack locally) and crypto-shredding helper (ADR-017) | `app/core/crypto.py` |
| E1-T03 | Auth: Cognito JWT verification, `AUTH_MODE=local-dev` signer for local only, `require_role`, row-ownership repository base class | `app/auth/*`, `app/core/repository.py` |
| E1-T04 | Problem-details errors (02 Appendix B), request IDs, structured logging with scrubber, rate limits on Valkey (RL-* classes) | `app/core/errors.py`, `app/core/logging.py`, `app/core/ratelimit.py` |
| E1-T05 | Unauthenticated, rate-limited `POST /v1/public/underage-attempts` (`store_country` only; stores no IP, device ID or date of birth; increments `underage_attempts`); `POST /v1/account/bootstrap` after the first sign-in (re-checks the date of birth: a tampered under-18 value → `403 age_gate_blocked`, Cognito user deleted, no user row, counter +1; store country → market and `home_region`); `GET/PATCH /v1/me`; `POST /v1/auth/sign-out-all` (02 §8.2, DEC-010) | `app/account/*` |
| E1-T06 | `GET/PUT /v1/profile` (goals, equipment with `weights_kg[]`, schedule) | `app/profile/*` |
| E1-T07 | Consents: `GET /v1/consents`, `PUT /v1/consents/{consent_id}`, `GET /v1/consents/history`; records with version, timestamp, locale, text hash; `require_consent("CON-xx")` dependency | `app/consents/*` |
| E1-T08 | Idempotency middleware for `POST` (02 §8.1) and ETag/`If-Match` helpers | `app/core/idempotency.py` |
| E1-T09 | OpenAPI export, committed `services/api/openapi.yaml`, CI diff check, generated `packages/api-client`, Schemathesis contract job | `tools/ci/openapi_check.py`, `packages/api-client/*` |
| E1-T10 | `GET /v1/config` signed with the local KMS key (ADR-025) and `POST /v1/devices` | `app/content/config_service.py`, `app/notify/devices.py` |
| E1-T11 | Terraform modules for dev: network, rds-postgres, valkey, s3-buckets, kms, cognito, ecs-service, github-oidc (plan only until the human applies) | `infra/terraform/modules/*`, `infra/terraform/envs/dev` |

**Acceptance.** FR-001 AC-1 (backend part), FR-002 AC-2 (under-18 → no account or auth identity is ever created; only the anonymous counter is kept), FR-003 AC-1/AC-2, FR-064 (backend records), BR-10, NFR-009 / PERF-20 (read endpoints p95 ≤250 ms on the local load smoke; DEC-004), NFR-020 (field encryption on `_enc` columns), NFR-033 (consent record fields), NFR-037 (`home_region` on every user-scoped row).
**Tests.** Row-ownership test that calls every member endpoint with a second user's IDs and expects `404`; age-gate boundary tests (17 years 364 days, 18 years 0 days, leap-day birthdays); the underage-attempts endpoint accepts only `store_country` and writes nothing but the (day, market) count; consent version/hash tests; encryption round-trip and crypto-shred tests; idempotency replay (same key + body → same response; same key + other body → `409 idempotency_key_reused`).
**Definition of done.** OpenAPI committed and client regenerated; migrations pass upgrade and downgrade on an empty DB; no secrets in code.
**Demo.** `curl` `POST /v1/public/underage-attempts` with no token → `underage_attempts` count +1, no user row, no Cognito user; then `curl` bootstrap with a tampered under-18 date of birth → `403 age_gate_blocked`, the test Cognito user deleted and no user row.
**Human.** HITL-05 (production data: none yet, but Terraform apply to any AWS account needs the tech lead), HITL-12.

---

### 6.5 E2 — Mobile foundation: navigation, auth, onboarding, design system, age gate (W2–W10)

**Goal.** An Expo SDK 58 development build that runs the age gate first, then signs in (no sign-in is offered before the gate passes, DEC-010), records consents, collects goals and equipment, stores data in an encrypted local DB and syncs through an outbox.
**Prerequisites.** E0, E1-T05..T07. ADR-006 (M1 library pins) drafted. Read 02 §2.5 (threading), §3.1, §4.12 (offline), §8.2 (age gate before sign-in), BRD FR-001–FR-006, FR-064 and BR-10.

| Task | What to build | Files / modules |
|---|---|---|
| E2-T01 | Expo app from the SDK 58 template, development build profiles (`development`, `preview`, `production`) in `eas.json`, iOS 17.0 / Android API 28 floors, targetSdk 36, compileSdk 37 | `apps/mobile/app.config.ts`, `eas.json` |
| E2-T02 | Design system: tokens (light/dark), typography with dynamic type, buttons, inputs, cards, caption component, accessibility helpers | `src/design-system/*` |
| E2-T03 | Navigation with `expo-router`: welcome → age gate → auth → onboarding stack, main tabs (Today, Workouts, Coach, Food, Progress, Settings) | `app/*` |
| E2-T04 | Age gate as the first onboarding step, before any sign-in: neutral date-of-birth screen with no hint of the cut-off; under-18 → resources screen, no auth call, only `POST /v1/public/underage-attempts`; the date of birth is held in memory until bootstrap and never written to disk; "not available in your region yet" screen (no account) | `src/features/onboarding/AgeGate.tsx` |
| E2-T05 | Auth, reachable only after the age gate passes: Sign in with Apple, Google, email one-time code via Cognito; `POST /v1/account/bootstrap`; refresh token in `expo-secure-store`; local-dev auth for simulator | `src/features/auth/*` |
| E2-T06 | Onboarding: goals, experience, schedule, home/gym, dumbbell weights; units and locale (lb/kg display, SI storage) | `src/features/onboarding/*`, `src/i18n/units.ts` |
| E2-T07 | Consent screens for CON-01, CON-02, CON-03 explainer (consent center UI completed in E11) | `src/features/consent/*` |
| E2-T08 | Encrypted local DB (SQLite + SQLCipher; key in `expo-secure-store`), migrations, excluded from iCloud backup | `src/db/*` |
| E2-T09 | Sync outbox worker with idempotency keys and backoff (1 min doubling to 1 h; give up after 30 days with a support flag, never delete) | `src/sync/outbox.ts` |
| E2-T10 | i18n setup (en-US catalogue), ESLint rule against literal strings, signed-config client (`/v1/config`) with last-good fallback | `src/i18n/*`, `src/platform/config.ts` |

**Acceptance.** FR-001 AC-1, FR-002 AC-1/AC-2, FR-003 AC-2, FR-004 AC-1, FR-006 AC-1/AC-2, NFR-011 / PERF-04 (cold start p95 ≤4.0 s on Tier B; DEC-003), NFR-018 (outbox: offline data synced within 60 s of reconnect), NFR-028/NFR-029, NFR-030, NFR-031.
**Tests.** Jest for unit conversion (round trips lb↔kg, ft/in↔cm), outbox retry and idempotency; Maestro flows: age gate pass → sign-in; age gate fail → resources screen with no sign-in option and no auth request (network log shows only the anonymous counter call); onboarding complete; airplane mode → data kept → reconnect → synced.
**Definition of done.** Builds on both platforms with `npx expo prebuild --clean`; screen-reader walkthrough of onboarding recorded in the PR.
**Demo.** Fresh install on a Tier B Android phone → age gate → sign in with email code → onboarding → home screen; turn on the largest text size and repeat with no clipping.
**Human.** Designer reviews screens; HITL-02 for the wording of consent and age-gate screens (counsel).

---

### 6.6 E3 — PoseEngine native module and camera pipeline (spike W1–W6, hardening W7–W12)

**Goal.** Prove at **M1 (2026-12-11)** that MediaPipe Pose Landmarker runs fast enough on real phones inside a VisionCamera 5 frame processor, with face landmarks dropped natively and no pixels in JS; then harden it into F-020, F-021 and F-101.
**Prerequisites.** E0. Read 02 §4.1–§4.4, §4.11, §4.12, §6.1–§6.4, canon §8.1–§8.3. D-05 default: pin the `MediaPipeTasksVision` 1.0.0 pod.

**M1 spike first (W1–W6).** Do tasks T01–T07 before anything else in this epic. The spike answers the go/no-go question for the whole product (D-12: evaluate QuickPose only if M1 gates fail).

| Task | What to build | Files / modules |
|---|---|---|
| E3-T01 | Nitro module scaffold: `PoseEngine.nitro.ts` exactly as 02 §4.2.1; Nitrogen codegen; empty Swift and Kotlin implementations | `packages/pose-engine/src/PoseEngine.nitro.ts`, `ios/`, `android/` |
| E3-T02 | Android: MediaPipe Tasks Vision 1.1.1, VIDEO mode, `num_poses = 1`, GPU delegate with CPU fallback, monotonic timestamps, reused Float32 buffers (22×5 and 22×3), face points 0–10 never copied | `android/src/main/java/.../HybridPoseEngine.kt` |
| E3-T03 | iOS: `MediaPipeTasksVision` 1.0.0 pod through an Expo config plugin; same contract; prove it in a **release** build (D-05); if the pod fails, vendor the xcframework through the plugin and record ADR-003 | `ios/HybridPoseEngine.swift`, `apps/mobile/plugins/withMediaPipe.ts` |
| E3-T04 | Camera session: format ≤1920×1080, 16:9, 30 fps target, no recording output; `useAsyncRunner` frame processor that drops when busy and disposes every frame in `try/finally` | `apps/mobile/src/camera/*` |
| E3-T05 | Skia skeleton overlay from shared values; frame → overlay latency instrumentation | `apps/mobile/src/camera/Overlay.tsx` |
| E3-T06 | Synthetic-feed debug build (AVAssetReader / MediaCodec reads a bundled golden clip instead of the camera) and the device-lab runner that logs `getStats()` and thermal state every 10 s for 20 min | `packages/pose-engine/*/SyntheticFeed*`, `ml/device-lab/run_synthetic.py` |
| E3-T07 | Spike report: FPS, p95 latency, thermal per device; ADR-003, ADR-029 (VIDEO running mode), ADR-030 (camera pixel format) drafts | `docs/adr/*`, `docs/PROGRESS.md` |
| E3-T08 | Thermal governor L0–L3 (Full → Lite → lower FPS → counting-only), polled ≤ once per 10 s, applied between sets | `packages/pose-engine/*/ThermalGovernor*` |
| E3-T09 | Apple Vision 2D fallback on iOS (19 → 22 joint map; dependent rules disabled) and optional `bodyHeight` (iOS 17+) | `ios/AppleVisionBackend.swift` |
| E3-T10 | Device tilt (gravity vector), model SHA-256 check at load, `BundleVerifier` (ECDSA P-256, two pinned keys) | `ios/*`, `android/*` |
| E3-T11 | Setup Coach checks S1–S5 (distance 2–4 m, required view, full-body framing, lighting via `meanLuma`, tilt) and the three-rep personal baseline (median of three assessed reps) | `apps/mobile/src/camera/SetupCoach/*`, `packages/exercise-engine/src/baseline.ts` |
| E3-T12 | Failure modes FM-01..FM-13 wired to the user messages in 02 §4.12 | `apps/mobile/src/camera/failureModes.ts` |

**Acceptance.** M1 exit criteria (canon §14.2): Full model ≥30 FPS on Tier A and ≥20 FPS on Tier B over 20 min; p95 frame-to-overlay ≤150 ms on Tier B; iOS packaging proven in a release build. Then FR-016, FR-017, FR-018, FR-019, FR-065; NFR-001, NFR-002, NFR-016, NFR-017 (PERF-07, DEC-005); 02 CV-01–CV-07, CV-10–CV-12, CV-30, CV-31; BR-18.
**Tests.** Native: CV-04 (300-frame synthetic feed, 0 timestamp errors), CV-05 (buffer byte lengths 22×5×4 and 22×3×4; face-only images return no face coordinates), CV-06 (corrupted model hash → Apple Vision within 2 s), CV-07 (release-build file-system diff and static grep on write APIs); governor tests with mocked thermal states; one test per FM row (§7.4).
**Definition of done.** Device-lab results file per build (PERF-30); no `console.log` of landmarks; the module exposes no API that returns pixels.
**Demo.** On a Tier B phone, start a squat session: skeleton overlay follows the body, the debug HUD shows FPS ≥20 after 20 minutes, and a file-system diff after the session shows no new image or video files.
**Human.** HITL-09 (D-05 decision recorded by the tech lead at M1), HITL-08 if thresholds are tuned on real data; ML/CV engineer reviews every PR.

---

### 6.7 E4 — Exercise engine: DSL, rep counter, rules, cue scheduler, golden fixtures (W3–W23)

**Goal.** One pure-TypeScript engine that turns landmark streams into reps, per-rep metrics, form-rule results, autoregulation prompts and cues, identical on the phone and in CI.
**Prerequisites.** E0; E3-T01 types. Read 02 §4.3, §4.5–§4.10, §5.2–§5.5; canon §7 (EX-01–EX-10, the 26 ERR codes) and §8.3.
**Order.** EX-01 squat and EX-03 push-up first (T01–T06 by W6, for ML-07 at M1); then the other eight exercises by W16; calibration v1 at M2 (rules marked "M2" in canon §7.2); full calibration at M3.

| Task | What to build | Files / modules |
|---|---|---|
| E4-T01 | JSON Schema for `ExerciseDefinition` (02 §4.5.2) and the bundle envelope; schema tests | `packages/exercise-engine/schema/exercise-definition.schema.json`, `packages/contracts/bundle-envelope.schema.json` |
| E4-T02 | Post-processing: visibility gate, One Euro filter, hip-centred torso-scaled normalisation, joint angles (02 §4.3) | `src/filters/oneEuro.ts`, `src/geometry/*` |
| E4-T03 | Rep state machine with hysteresis and per-phase timing; `RepEvent` | `src/reps/stateMachine.ts` |
| E4-T04 | Rule types and per-rep confidence/abstention (≥80% of the rep's frames above the visibility threshold, start 0.5) | `src/rules/*` |
| E4-T05 | Golden-video harness runner in Node + Python landmark extraction (§7.2), CI job `harness.yml` | `ml/golden/*`, `.github/workflows/harness.yml` |
| E4-T06 | EX-01 and EX-03 definitions with start thresholds from canon §7.2; run ML-07 (≥90% of 50 golden sets exact) | `content/exercises/EX-01.json`, `EX-03.json` |
| E4-T07 | Per-rep metrics: ROM, tempo, velocity estimate (landmark displacement ÷ time, scaled by body height), confidence (02 §4.10.1) | `src/metrics/*` |
| E4-T08 | Autoregulation: velocity loss vs best of reps 1–2 (default 30%, user range 10–40%), form drift (new GA error on 2 consecutive reps, or ROM >15% below rep 1), next-set suggestion clamped by the constraint set; at most one prompt per set | `src/autoreg/*` |
| E4-T09 | Cue scheduler: ≤1 corrective cue per rep at rep boundaries, cooldowns, periodic positive cue, GA vs "Beta tip" copy, audio + haptic + caption payload | `src/cues/scheduler.ts` |
| E4-T10 | EX-02, EX-04, EX-05, EX-06 definitions | `content/exercises/*.json` |
| E4-T11 | EX-07, EX-08 (incl. 30-s benchmark count, full stands only), EX-09 ("quality seconds" timer), EX-10 | `content/exercises/*.json` |
| E4-T12 | Mobile glue: worklet adapter from `PoseResult` to the engine; cue output to `expo-speech`/`expo-haptics`; captions | `apps/mobile/src/cv/*` |
| E4-T13 | Calibration tooling (threshold sweep, precision ≥0.92 on calibration split) and bundle changelog | `ml/calibration/*`, `content/exercises/CHANGELOG.md` |

**Acceptance.** FR-020–FR-025, FR-071; NFR-003–NFR-008, NFR-040; BR-21, BR-22, BR-26; 02 CV-08, CV-13–CV-27, ML-01, ML-02, ML-06, ML-07. M2: KPI-01 on Tier A golden sets for all 10 exercises. M3: every GA cue meets KPI-02 on the held-out set.
**Tests.** CV-16 synthetic pause streams (0 phantom reps); CV-20 (20 scripted rep sequences per trigger); CV-22 property test (10,000 random suggestions × constraint sets → 0 violations); CV-24 (30 scripted scheduler sequences); CV-26 (every Beta rule's copy starts with "Beta tip"); CV-13 (8 tampered bundles rejected); golden harness regression rules (§7.2).
**Definition of done.** No React Native import in `packages/exercise-engine` (lint rule); coverage ≥90% lines on `packages/exercise-engine/src` (playbook target, stricter than NFR-039's 80%); every threshold carries "calibrate in M2/M3" until calibrated.
**Demo.** Run `pnpm harness --ex EX-01` → table of exact-rep rate and per-cue precision/recall vs labels and vs the current bundle; then do 8 slow squats on a phone and hear one cue at most per rep.
**Human.** HITL-08 (threshold calibration with real data, ML/CV engineer signs), HITL-07 (cue copy reviewed by coaches; no clinical claims).

---

### 6.8 E5 — Workout player, programs and session sync (W9–W24)

**Goal.** Users follow a plan, run camera and manual sets, and every finished session syncs as per-rep metrics.
**Prerequisites.** E2, E4-T12, E6-T03 (constraint set read API). Read 02 §2.4.1–§2.4.2, §4.10.2, §8.5.1 (programs, plan proposals, sessions), §8.5.2, §9.4 (`programs`, `program_enrolments`, `plan_weeks`, `plan_proposals`, `sessions`, `sets`, `reps`, `form_events`).

| Task | What to build | Files / modules |
|---|---|---|
| E5-T01 | Tables and migrations for programs, enrolments, plan weeks, proposals, sessions, sets, reps, form events (monthly partitions for `reps`, `form_events`, ADR-018) | `services/api/migrations/*`, `app/sessions/models.py`, `app/planner/models.py` |
| E5-T02 | `POST /v1/sessions/sync` (idempotent batch upsert, ≤5 MB, `payload_version`), `GET /v1/sessions`, `GET /v1/sessions/{session_id}` | `app/sessions/*` |
| E5-T03 | Mobile payload builder from the engine's SessionLog (no keypoints, no pixels) | `apps/mobile/src/sync/payload.ts` |
| E5-T04 | Deterministic planner and plan validator: equipment, schedule, constraint set; every change is a proposal | `app/planner/service.py`, `app/planner/validator.py` |
| E5-T05 | Plan proposals API (`/v1/plan-proposals`, confirm, decline) and "Why this changed" card model citing data or a rule ID | `app/planner/router.py`, `app/planner/why_cards.py` |
| E5-T06 | Program content for Foundations, Home Dumbbell Strength, Gym Basics, GLP-1 Strength Track (structure only; any clinical progression rule is a `CLINICAL_REVIEW_REQUIRED` placeholder) | `content/programs/*` |
| E5-T07 | Workout player: today's session, timers, rest, manual logging for non-camera moves, equipment-busy swaps from the reviewed swap table | `apps/mobile/src/features/workouts/*` |
| E5-T08 | Camera set flow: Setup Coach → set → autoregulation prompt → set-end summary with "was this cue right?" (≤1 set per session) | `apps/mobile/src/features/workouts/CameraSet/*` |
| E5-T09 | Offline: 14-day plan cache with constraint-set version; FM-10, FM-11 handling | `apps/mobile/src/db/planCache.ts` |
| E5-T10 | (Beta) Voice logging: on-device speech-to-text for RPE, reps in reserve, discomfort; audio never stored | `apps/mobile/src/features/workouts/voice/*` |

**Acceptance.** FR-030, FR-031, FR-032 (structure), FR-034, FR-038 (planner side), FR-026 (Beta), FR-004 AC-2; NFR-015, NFR-018; BR-11 (Free gets Foundations and the five free exercises), BR-24; 02 CV-28, CV-29.
**Tests.** CV-29 (same payload 5× → one session); CV-28 privacy scan of 1,000 generated payloads; validator property tests (no proposal applied that violates a rule); Maestro: full camera session on simulator with injected test video → sync → history.
**Definition of done.** Sync endpoint meets PERF-21 (p95 ≤400 ms) locally under the load smoke (NFR-009, DEC-004); no plan change without a why-card (KPI-25 counter = 100%).
**Demo.** Airplane mode → complete a push-up session → reconnect → session appears in history with per-rep ROM and tempo, and the server DB has no coordinate arrays.
**Human.** HITL-01 (program progression and swap table need clinical/coach sign-off); designer review of the player.

---

### 6.9 E6 — Medication profile and constraint engine (W5–W27)

**Goal.** Users list medicines; the deterministic engine maps RxCUI → class → clinician-owned rules → constraint set that changes the plan, never the medicine. Red-flag check-ins and gates route to fixed templates.
**Prerequisites.** E1, E13-T01..T03 (content-as-code pipeline). Read 02 §2.4.4, §7.8, §7.9.2–§7.9.3, §8.5.4, §9.4 (`health_profiles`, `health_gates`, `med_class_map`, `user_medicines`, `dose_schedules`, `dose_events`, `checkins`, `rules`, `rule_versions`, `constraint_sets`); canon §9.5–§9.6.
**Scope by release.** MVP: GLP1, BB, INS, SGLT2, ACAP, STAT. V1.0 (by M4): AHT, DIU, FQ, CS, STIM, AD, ACH, THY, SUP (caffeine counter), heat alerts (F-014). Beta: dose-cycle scheduling (F-043, live by M3).

| Task | What to build | Files / modules |
|---|---|---|
| E6-T01 | Rule schema and loader for `content/rules/<class>/RULE-<CLASS>-##.yaml`; signed rule releases (`rules-YYYY.MM.DD.N`) | `app/constraints/schema.py`, `app/constraints/loader.py` |
| E6-T02 | RxNav client (no user identifiers forwarded; 24 h Valkey cache), `GET /v1/medicines/search`, NLM attribution string in the response | `app/medicines/rxnav.py` |
| E6-T03 | Constraint engine: RxCUI → RxClass → class codes via `med_class_map` → rule evaluation order (02 §7.8.5) → constraint set with KB card IDs; uncovered-medicine card | `app/constraints/engine.py` |
| E6-T04 | Medicines API (`/v1/medicines`, schedule, `/v1/dose-events`, `/v1/constraints`) with field encryption | `app/medicines/*` |
| E6-T05 | Rule files for the 6 MVP classes as **structures with `CLINICAL_REVIEW_REQUIRED` placeholders**; the clinical lead fills and signs them | `content/rules/{GLP1,BB,INS,SGLT2,ACAP,STAT}/*` |
| E6-T06 | Pre-participation screening flow and clearance gate (question set versioned; clearance rules from the clinician) | `app/health_profile/*`, `apps/mobile/src/features/health/Screening/*` |
| E6-T07 | Safety gates (pregnancy, new diagnosis, new medicine) and red-flag check-ins → `TPL-EMERGENCY-01`, `TPL-URGENT-*`, `TPL-CRISIS-01`, `TPL-GATE-*`; templates bundled offline per market | `app/safety/checkin_rules.py`, `content/safety/templates/en-US/*` |
| E6-T08 | Mobile: medication list (search + manual), dose schedule, side-effect and energy check-ins, user-configured reminders (generic payload text) | `apps/mobile/src/features/health/*` |
| E6-T09 | Planner integration: RPE/talk-test mode for BB, template blocks for SGLT2, drill exclusions for ACAP, check-in prompts for INS/STAT | `app/planner/constraints_adapter.py` |
| E6-T10 | (Beta) Dose-cycle scheduling `POST /v1/schedule-suggestions/dose-cycle` | `app/planner/dose_cycle.py` |
| E6-T11 | (V1.0) Rule structures for the 9 further classes; caffeine counter `GET /v1/caffeine/today` | `content/rules/*`, `app/medicines/caffeine.py` |
| E6-T12 | (V1.0) Heat-risk alerts via WeatherKit REST (CON-10; city-level coordinates rounded to 1 decimal; not stored) `GET /v1/heat-risk` | `app/heat/*` |
| E6-T13 | Label-change watcher: DailyMed/openFDA → `label_change_tickets`; `review_due` checks | `app/jobs/label_watch.py` |

**Acceptance.** FR-005, FR-007, FR-008, FR-009, FR-010, FR-011, FR-012, FR-013 (V1.0), FR-033 (Beta); BR-01, BR-03, BR-06, BR-07, BR-08, BR-20; NFR-026, NFR-039 (≥80% lines; 02 §12.3 asks ≥85% on `app.constraints`, use 85%).
**Tests.** One fixture test per RULE ID (input medicine list → expected effects); "uncovered medicine" test; combination tests (BB + INS → hypoglycaemia education; ACAP + AD → SSRI co-listing flag; FQ + CS → tendon-protect); template tests per market (US/UK/IN numbers verbatim from canon §9.6); offline template test; gate pause test; property test: no constraint set ever changes a dose field (there is none) and no output text contains a number next to "mg/dL" or "mmHg".
**Definition of done.** No rule file contains a clinical value written by Claude Code; CI placeholder check passes only on non-release branches until the clinical lead signs.
**Demo.** Add "metoprolol" → plan switches to RPE mode with KB card "last reviewed" date; add "empagliflozin" → keto template disappears with a why-card; log "chest pain" in a check-in → session stops and `TPL-EMERGENCY-01` shows 911.
**Human.** HITL-01 (every rule, card, screening rule and template), HITL-03 (counsel on gate copy), HITL-06 (any safety rule change).

---

### 6.10 E7 — AI coach: chat API, Claude integration, tools, safety guard, KB, evals (W4–W24)

**Goal.** A grounded coach that reads structured data through strict tools, proposes (never applies) changes, renders clinician cards verbatim, and is wrapped by deterministic guards before and after the model.
**Prerequisites.** **Load the `claude-api` skill before writing any code in this epic (GR-15).** E1, E6-T03, E13-T01..T03. Read 02 §7 (all), §8.5.3, §8.7, §9.4 (`coach_threads`, `coach_messages`, `coach_memory`, `llm_calls`, `kb_cards`, `kb_card_versions`, `kb_chunks`, `safety_events`, `eval_runs`); canon §9.
**Phase 0 skeleton (W4–W6).** T01–T03 only, with `LLM_MODE=mock`.

| Task | What to build | Files / modules |
|---|---|---|
| E7-T01 | LLM gateway: the only module importing `anthropic` 1.15.0; route config (`chat`, `classifier`, `debrief`, `narration`, `meal_parse`) all on `claude-opus-5-5`; effort `medium`/`low` per canon §9.1; structured outputs; strict tools; no fallbacks; audit fields to `llm_calls`; recorded-fixture mock mode | `app/llm/client.py`, `services/api/config/llm_routes.*.yaml` |
| E7-T02 | Input guard: lexicons and patterns per locale, structured-signal rules, minor and ED signals, classifier call; `safety_events` | `app/safety/input_guard.py`, `content/safety/lexicons/en-US.yaml` |
| E7-T03 | Output guard and template renderer: never-rule checks, numeric checks, `kb_card_ids` validation (only IDs retrieved or mandatory in this turn; DEC-011); `TPL-REFUSAL-01`, `TPL-FALLBACK-01`, `TPL-REFERRAL-01`, `TPL-AI-NOTICE-01`, `TPL-MINOR-01` | `app/safety/output_guard.py`, `app/safety/templates.py` |
| E7-T04 | KB: card format with front matter, loader, `kb_chunks` with pgvector, retrieval (mandatory cards + vector search) returned to the model as tool results, verbatim rendering of each validated card with its sources; API citations never enabled (ADR-011) | `app/kb/*`, `content/kb-cards/*` |
| E7-T05 | Tools: the 14 strict tools of canon §9.3 with scope checks; `get_med_context` only with CON-05; `save_memory` only on user turns | `app/coach/tools.py` |
| E7-T06 | Orchestrator (one turn = one run, 02 §7.3), prompt-cache layout (4 breakpoints), mid-conversation constraint injection, streaming policy (ADR-014) | `app/coach/orchestrator.py` |
| E7-T07 | Chat API with SSE (`/v1/coach/threads`, `/turns`, `/messages`, `/report`, delete) and AI notice at thread start | `app/coach/router.py` |
| E7-T08 | Mobile chat: persistent "AI coach" label, session-start notice, report button, proposal cards with confirm/decline, offline state, draft kept locally | `apps/mobile/src/features/coach/*` |
| E7-T09 | Debrief and weekly narration (LLM for paid tiers, templates for Free) | `app/coach/debrief.py`, `app/coach/narration.py` |
| E7-T10 | ED-safe mode: hides calories, weight, BMI, deficits everywhere (API filters + UI) | `app/safety/ed_safe.py`, `apps/mobile/src/features/settings/EdSafe*` |
| E7-T11 | Eval harness: suites in `ml/evals/suites/`, runner, deterministic checks first, Opus judge with rubrics, gates (§7.5), CI workflow `safety-eval.yml` with path filters | `ml/evals/*`, `.github/workflows/safety-eval.yml` |
| E7-T12 | Degraded modes D0–D3 and the Valkey circuit breaker (02 §7.13) | `app/coach/degraded.py` |
| E7-T13 | (Beta) Coach memory: list, edit, delete, delete-all; health memories need CON-06 | `app/coach/memory.py`, `apps/mobile/src/features/coach/Memory*` |

**Acceptance.** FR-036–FR-044, FR-073 (eval part); FR-002 AC-3 (minor signal locks coach); NFR-010 / PERF-24, PERF-25 (DEC-002), NFR-019, NFR-022, NFR-025, NFR-026, NFR-027; BR-02, BR-03, BR-04, BR-05, BR-08, BR-19, BR-23, BR-28; KPI-07 = 0, KPI-08 ≥0.98, KPI-09 = 100%.
**Tests.** LLM contract tests with recorded responses (refusal, `max_tokens`, invalid structured output, tool loops); request-builder test that no request enables citations when `output_config.format` is set; an unknown or unretrieved `kb_card_ids` entry is rejected; payload-minimisation contract test (no name, email, keypoints, clips in any request body); never-rule unit tests (§7.5); India regional test (no medication counselling in chat, cards only) behind the F-103 flag; quota bypass test for safety templates.
**Definition of done.** Eval suite v1 green in CI with zero never-rule failures (M2); every `llm_calls` row has model ID, prompt version, KB version, rule IDs and eval-run ID.
**Demo.** Ask "Can I skip my dose before leg day?" → no dose advice; card + "ask your prescriber or pharmacist" referral. Ask "Why is my next squat session lighter?" → reply cites "velocity fell 34% by rep 7" from tool data with a why-card. Type a self-harm phrase → `TPL-CRISIS-01` with 988.
**Human.** HITL-01 (KB cards, lexicons, templates), HITL-04 (eval failures reviewed by clinicians), HITL-10 (D-02 routing), HITL-06.

---

### 6.11 E8 — Nutrition and meal scans (W12–W17)

**Goal.** Food logging by search, barcode, manual entry and meal photo, with clinician-formula protein and fibre targets and intake-floor flags.
**Prerequisites.** E1, E7-T01 (gateway), D-10 decided. Read 02 §8.5.1 (meal scans, nutrition), §8.5.6, §9.4 (`foods_cache`, `nutrition_entries`, `meal_scans`).

| Task | What to build | Files / modules |
|---|---|---|
| E8-T01 | Food search adapters: USDA FDC, fatsecret or Edamam (D-10), Open Food Facts barcode cache with attribution and share-alike notes | `app/nutrition/providers/*` |
| E8-T02 | Nutrition entries API and day view (`/v1/nutrition/entries`, `/v1/nutrition/days/{date}`) with ED-safe filtering | `app/nutrition/*` |
| E8-T03 | Targets: protein and fibre from the clinician formula as a **placeholder-driven** rule (`CLINICAL_REVIEW_REQUIRED` until the RD signs); kcal-floor flags 1,200 kcal/day (women) and 1,800 kcal/day (men), default for users without a recorded sex is a `CLINICAL_REVIEW_REQUIRED` setting the RD fills; loss-rate cap 0.9 kg/week; no protein target for users reporting kidney disease | `app/nutrition/targets.py`, `content/rules/NUTRITION/*` |
| E8-T04 | Meal scan: multipart upload (≤8 MB) → `meal_parse` route on `claude-opus-5-5` → structured estimate → user confirms; photo deleted after parsing, forced delete ≤24 h | `app/nutrition/meal_scan.py`, `app/jobs/meal_photo_cleanup.py` |
| E8-T05 | Mobile food log, barcode scanner, meal-photo flow with editable estimate | `apps/mobile/src/features/food/*` |

**Acceptance.** FR-045, FR-046, FR-047; BR-05, BR-25; NFR-025 (meal photo is the only image sent to Anthropic; consent CON-04 checked).
**Tests.** Retention job test (photo object gone after parse; forced delete at 24 h); `meal_not_food` path; floor flag tests at boundaries; ED-safe mode hides kcal in every response; 200 dietitian-labelled photos run in the eval suite (§7.5).
**Definition of done.** No food names or kcal in analytics or logs.
**Demo.** Scan a photo of a meal → editable items appear → confirm → day view updates protein; S3 shows no photo object afterwards.
**Human.** HITL-01 (RD signs protein formula and floors), HITL-12 (food API accounts).

---

### 6.12 E9 — Progress, quality volume and benchmarks (W14–W27)

**Goal.** Honest progress: history, weekly insights, total vs quality volume, monthly camera benchmarks, health-platform sync.
**Prerequisites.** E5. Read 02 §8.5.1 (progress, benchmarks, health sync), §9.4 (`benchmarks`, `wearable_daily_summaries`).

| Task | What to build | Files / modules |
|---|---|---|
| E9-T01 | History and weekly insights (deterministic charts; LLM narration for paid tiers via E7-T09) | `app/progress/weekly.py`, `apps/mobile/src/features/progress/*` |
| E9-T02 | (Beta) Quality-volume ledger: quality volume counts assessed reps with no GA error; PRs on quality reps only; no rep silently dropped | `app/progress/quality_volume.py` |
| E9-T03 | (Beta) HealthKit / Health Connect daily summaries per data type (CON-07) | `apps/mobile/src/platform/health/*`, `app/health_sync/*` |
| E9-T04 | (V1.0) Monthly benchmarks: 30-s chair stand (EX-08, full stands only), max quality push-ups (EX-03), quality plank hold (EX-09), squat-depth check-in (EX-01), shown as estimates with bands | `app/progress/benchmarks.py`, `apps/mobile/src/features/progress/Benchmarks/*` |

**Acceptance.** FR-050, FR-051 (Beta), FR-052 (V1.0), FR-053 (Beta); BR-26; KPI-19 instrumentation.
**Tests.** Quality-volume arithmetic property tests; benchmark wording passes the banned-claims linter ("strength benchmarks", never fall-risk); HealthKit read only for granted types.
**Definition of done.** Every camera number on screen carries "estimate" and an error band.
**Demo.** Persona P1 seed → Progress tab shows total vs quality volume and a "strength kept" benchmark trend.
**Human.** HITL-07 (benchmark copy review), HITL-02 (HealthKit/Health Connect declarations).

---

### 6.13 E10 — Subscriptions, paywall and quotas (W12–W27)

**Goal.** Free, Premium and Premium+ entitlements, quotas that never meter safety, the onboarding soft paywall and subscription-law compliance.
**Prerequisites.** E1, E7-T01. Read 02 §2.4.5, §7.11, §8.5.1 (entitlements), §8.6, §9.4 (`entitlements`, `billing_events`, `quota_counters`, `partner_codes`).

| Task | What to build | Files / modules |
|---|---|---|
| E10-T01 | RevenueCat SDK, entitlements Free/Premium/Premium+; `/webhooks/revenuecat`; `GET /v1/entitlements` | `app/billing/*`, `apps/mobile/src/platform/purchases.ts` |
| E10-T02 | Quotas per tier and market (canon §9.7), abuse limits (30/hour, 2,000 characters), per-user cost breaker; `GET /v1/quotas`; safety flows bypass all counters | `app/billing/quota.py` |
| E10-T03 | Tier gating: Free exercises (EX-01, EX-03, EX-07, EX-08, EX-09), programs, LLM vs template debriefs | `app/billing/gates.py` |
| E10-T04 | (Beta) Onboarding soft paywall, annual-led, 7-day trial on annual plans only, second prompt Days 4–7, RevenueCat Offerings | `apps/mobile/src/features/paywall/*` |
| E10-T05 | (V1.0) Subscription compliance: affirmative-consent records, annual renewal reminder, cancellation guidance; never block store refunds | `app/billing/compliance.py` |

**Acceptance.** FR-059, FR-060 (Beta), FR-061, FR-062 (V1.0); BR-01, BR-02, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16.
**Tests.** Quota table test generated from canon §9.7 (every tier × market); safety-template bypass test; webhook signature test; trial only on annual products; price display reads storefront prices (no hard-coded prices).
**Definition of done.** Prices in the app come only from RevenueCat; the PR shows sandbox screenshots.
**Demo.** Free user sends the 11th coach message in a month → `quota_exhausted` with reset date; then sends a red-flag phrase → template shows (not metered).
**Human.** HITL-11 (payment configuration in App Store Connect, Play Console and RevenueCat), HITL-02 (paywall and renewal copy).

---

### 6.14 E11 — Privacy and compliance features (W7–W27)

**Goal.** Consent center, export, deletion, AI disclosure, regional policy engine and opt-in training-data contribution.
**Prerequisites.** E1, E2. Read 02 §10 (all), §8.5.1 (export and deletion, consents), §9.6; canon §11.

| Task | What to build | Files / modules |
|---|---|---|
| E11-T01 | Consent center UI for CON-01..CON-12 with one-tap withdrawal and the effects of each withdrawal (02 §10.8) | `apps/mobile/src/features/consent/Center*` |
| E11-T02 | Export: `POST /v1/data-requests` (export) → machine-readable ZIP → short-lived download | `app/privacy/export.py` |
| E11-T03 | Deletion: in-app and web (`/v1/public/deletion-requests` + verify), crypto-shredding, Sign in with Apple token revoke, vendor deletions; completes within 30 days | `app/privacy/deletion.py` |
| E11-T04 | AI disclosure everywhere the coach appears; AI-processing consent (CON-04) before first chat or meal scan | `apps/mobile/src/features/coach/Disclosure*` |
| E11-T05 | (V1.0) Regional policy engine F-103 in signed config: India no medication counselling in chat; UK/EU medication features only after memo; IF-6 US-only | `app/content/market_policy.py` |
| E11-T06 | Network privacy test: run a full session with a proxy and assert no frames, keypoints or clips leave without the matching consent | `apps/mobile/e2e/privacy/*`, `tools/ci/network_privacy.py` |
| E11-T07 | (Beta) Training-data contribution (CON-08): keypoints without face points to the research account; revocation removes the person from future sets (ADR-026) | `app/research/*` |

**Acceptance.** FR-064, FR-065, FR-066, FR-067 (V1.0), FR-068 (Beta); BR-09, BR-17, BR-18, BR-19, BR-28; NFR-023, NFR-024, NFR-033, NFR-037; KPI-23 = 0.
**Tests.** Deletion integration test (all tables, S3 objects, Valkey keys, vendors queued); export completeness test against the DC-01..DC-15 inventory; consent withdrawal test for each CON; regional flag tests per market.
**Definition of done.** Retention table in code matches canon §11.1 (test compares them).
**Demo.** Withdraw CON-05 → coach answers about medicines show class-level card IDs only; delete the account → user cannot sign in, Cognito identity gone.
**Human.** HITL-02 (privacy policy, Consumer Health Data Policy, consent texts), HITL-05.

---

### 6.15 E12 — Analytics, notifications and observability (W10–W27)

**Goal.** Allowlisted analytics, reminders and lifecycle notifications without health words, and production observability.
**Prerequisites.** E1, E2. Read 02 §12.2, §13; §8.5.1 (notifications).

| Task | What to build | Files / modules |
|---|---|---|
| E12-T01 | `analytics/events.yaml` from 02 §13.2; typed client wrapper that drops non-allowlisted events and properties; CI check; consent gating by market (CON-11) | `apps/mobile/src/platform/analytics.ts`, `tools/ci/analytics_check.py` |
| E12-T02 | Sentry (mobile, API, worker) with PII scrubbing; OpenTelemetry in API and workers; custom metrics of 02 §12.2 | `app/core/telemetry.py` |
| E12-T03 | Reminders and preferences (`/v1/reminders`, `/v1/notification-preferences`, quiet hours); Expo push with generic text | `app/notify/*`, `apps/mobile/src/features/settings/Notifications*` |
| E12-T04 | (Beta) Lifecycle: Day 4–7 progress prompt, missed-session nudge, dose-day check-in, weekly review | `app/notify/lifecycle.py` |
| E12-T05 | Dashboards and alerts (02 §12.2 table), per-tier FPS/cue latency/assessed-rep panels | `infra/terraform/modules/observability/*` |

**Acceptance.** FR-057, FR-058 (Beta); BR-29; NFR-024, NFR-034, NFR-035, NFR-014.
**Tests.** Push payload linter (no medicine or health words); analytics property test (no free text, no health values); alert rules unit-tested where possible.
**Demo.** Set a dose reminder → push shows "Your reminder" with no medicine name.
**Human.** HITL-02 (notification wording).

---

### 6.16 E13 — Internal tools: CMS, exercise editor, ops console, labelling pipeline (W4–W22)

**Goal.** RepSight Studio (ADR-015) so clinicians and coaches review content without Git, a signed publish pipeline, staged rollouts and an ops console; plus the labelling pipeline for the data programme.
**Prerequisites.** E1. Read 02 §12.1, §4.5.4, §5.3.4, §7.7.4, §8.5.1 (admin endpoints).

| Task | What to build | Files / modules |
|---|---|---|
| E13-T01 | Content-as-code loaders and CI content checks (schema, links, never-rule patterns, placeholders) | `tools/ci/content_check.py` |
| E13-T02 | `publish-content` workflow: build release, sign with KMS (ECDSA P-256), upload to S3/CloudFront, register in `content_releases`, manifest endpoint `GET /v1/content/manifest` | `.github/workflows/publish-content.yml`, `app/content/*` |
| E13-T03 | Studio shell: Cognito admin pool, roles (`content-reviewer`, `clinician-reviewer`, `admin`), review queue and decision endpoints, two-person rule | `tools/admin/*` |
| E13-T04 | Labelling pipeline (F-113): Label Studio config, BlazePose Heavy pre-labels (`mediapipe` 1.1.1), two labellers + adjudicator, inter-rater agreement per ERR code | `ml/labelling/*` |
| E13-T05 | Exercise-definition editor (F-111): threshold and cue-copy edits as PRs, harness run on candidate, staged rollout 5% → 25% → 100% with guard metrics | `tools/admin/exercises/*` |
| E13-T06 | (Beta) Ops console (F-115): AI cost per user/route/tier/day, safety-event queue, weekly production sample, support lookup (email reveal audited) | `tools/admin/ops/*` |

**Acceptance.** FR-069, FR-070, FR-072, FR-074 (Beta); BR-20, BR-21; NFR-035, NFR-040; 02 CV-14.
**Tests.** Signature and manifest tests; rollout bucket stability across 10,000 synthetic users; guard breach halts rollout; role tests (a content-reviewer cannot approve a medication card).
**Demo.** Coach edits a cue's copy in Studio → PR opens → harness passes → admin publishes at 5% → manifest shows the new version for 5% of synthetic users.
**Human.** HITL-01 (approvals happen here), HITL-08.

---

### 6.17 E14 — Beta readiness and launch (W19–W31)

**Goal.** Pass M3 (2027-04-09), M4 (2027-05-14) and launch V1.0 on 2027-06-01 (M5).
**Prerequisites.** All MVP and Beta epics. Read canon §11.6 and §14.2; 02 §10.13, §12.6; 03 §2.4–§2.5.

| Task | What to build or run | Output |
|---|---|---|
| E14-T01 | Validation study tooling (W20–W26): rep exact/±1, per-cue precision/recall, Kinovea angle MAE on 30 participants, velocity loss vs linear position transducer on 20, stratified reports | `ml/validation/*`, validation report draft |
| E14-T02 | Methodology page content draft (how form scores work, and their limits), from study results only | `docs/methodology/` draft for counsel |
| E14-T03 | D-02 eval run on `claude-sonnet-5-5` and `claude-haiku-5-5` per route (no traffic moves) | Eval report for the owner by 2027-04-23 |
| E14-T04 | Performance gates on the 9-phone lab: KPI-03/KPI-04 on Tiers A and B (M3), all PERF release gates (M4) | Device-lab report |
| E14-T05 | Security: MASVS L1 self-assessment, ZAP baseline, threat-model review, fix all high/critical pen-test findings | Security report |
| E14-T06 | Load test at 2× projected peak (NFR-036) | Load-test report |
| E14-T07 | Store kits: privacy manifest and labels, usage strings, reviewer notes, Google Health apps / Data safety / Health Connect declarations, web deletion URL, target API 36 | `docs/store/*` drafts |
| E14-T08 | WCAG 2.2 AA fixes from the audit; accessibility statement draft | Audit fix PRs |
| E14-T09 | Release candidate freeze, runbooks (incident, breach with HBNR 60 days, rollback), on-call rota | `docs/runbooks/*` |

**Acceptance.** M3 and M4 exit criteria (canon §14.2); compliance checklist items 1–13 (canon §11.6); NFR-001–NFR-008, NFR-021, NFR-028, NFR-036; KPI targets at Beta exit (canon §15).
**Definition of done.** Release checklist 02 §12.6 complete with eval run ID in the release notes.
**Demo.** The M4 review: one page per gate with evidence links.
**Human.** HITL-02, HITL-03, HITL-04, HITL-05, HITL-10, HITL-13 (store submission on 2027-05-17).

---

### 6.18 E15 — Post-launch V1.x and V2, by release

Each release below becomes its own set of tasks in `docs/PROGRESS.md` at the start of its phase, using the same epic format. Full acceptance criteria for V1.x and V2 FRs are written in 01 when scheduled (01 §7.4 "Format").

| Release (date, milestone) | Scope | Key requirements | Gate and human steps |
|---|---|---|---|
| V1.1 Android US (2027-07-13, M6) | Android release from the same codebase; Android device-matrix calibration | KPI-01–KPI-04 on Android | Play Health apps and Health Connect declarations (HITL-13) |
| V1.2 UK + sharing (2027-08-24, M7) | en-GB; UK crisis routes; F-027 replay and shareable clip (on-device face blur, CON-09, 30-day default, ≤365 days); F-074 clinician report; F-094 US web checkout (D-13); F-120 clinic pilot (three design-partner clinics signed by M7 and still active at V1.4, KPI-26) | FR-027, FR-054, FR-063, FR-075 | UK memo and DPIA (HITL-03); counsel on web checkout (HITL-11) |
| V1.3 India (2027-10-05, M8) | en-IN, hi-IN; F-063 IFCT 2017 food data (NIN permission); F-123 partner codes; India quotas; DPDP flows; plan cards only for medication | FR-048, FR-078; Hindi safety eval (KPI-07, KPI-08) | D-08 (HITL-10); Hindi lexicons TD-08 (HITL-01) |
| V1.4 (2027-11-16, M9) | F-015 supplement check; F-028 barbell recorded-set analysis; F-045 comfort-range training (US only, D-09); F-064 fuelling summary; F-075 movement–discomfort journal; F-076 cue learning (Thompson sampling, ≤1 cue per rep); HealthKit Medications import (FR-015) | FR-014, FR-015, FR-028, FR-035, FR-049, FR-055, FR-056 | D-09 counsel memo (HITL-03); scope-cut order IF-7 → IF-6 → F-028 → F-064 if late (03 §2.8) |
| V2.0 (2028-03-28, M10) | F-029 learned CV models on LiteRT 2.3.0 (only our data); F-121 clinician portal and F-122 guardrails in a separate HIPAA-ready tenant (ADR-028); EU entry (D-15) with eu-central-1 cell; es-US, de-DE | FR-029, FR-076, FR-077 | BAA and Anthropic HIPAA organisation (HITL-02, HITL-05); EU memo, Art. 50 notices |

---

## 7. Testing & Quality Gates

### 7.1 Test pyramid

The layers follow 02 §12.3; this table adds where each lives in the repo and when it runs.

| Layer | Tool | Lives in | Runs | Blocks merge? |
|---|---|---|---|---|
| Unit (exercise engine) | Jest in Node | `packages/exercise-engine/test` | Every PR | Yes |
| Unit (mobile) | Jest | `apps/mobile/src/**/__tests__` | Every PR | Yes |
| Unit (backend, rules, never-rules) | pytest + Hypothesis | `services/api/tests/unit` | Every PR | Yes |
| Native (PoseEngine) | XCTest, JUnit | `packages/pose-engine/ios/Tests`, `android/src/test` | PRs touching the module | Yes |
| Contract | Schemathesis on `services/api/openapi.yaml`; generated client compiles | `services/api/tests/contract` | Every PR | Yes |
| Integration | pytest + Testcontainers (Postgres 18 + pgvector, Valkey, RxNav image, LocalStack) | `services/api/tests/integration` | Every PR (backend paths) | Yes |
| LLM contract | Recorded Anthropic fixtures per route (`LLM_MODE=mock`) | `services/api/tests/llm` | Every PR | Yes |
| CV regression | Golden-video harness (§7.2) | `ml/golden` | PRs touching `packages/exercise-engine`, `content/exercises`, `content/cues` | Yes |
| LLM safety eval | §7.5 | `ml/evals` | Path filters (§3.3), nightly on `main`, weekly production sample | Yes |
| Mobile end-to-end | Maestro (simulator/emulator; nightly cloud device farm) | `apps/mobile/e2e` | Nightly; release branches | Release only |
| Performance | Synthetic-feed device-lab runs; Locust (ADR-032) | `ml/device-lab`, `services/api/tests/load` | Nightly; release branches | Release only |
| Security | SAST, dependency audit, secret scan every PR; ZAP weekly | CI | Per 02 §10.13 | Yes (high findings) |
| Accessibility | Lint rules every PR; manual audit before M4 | CI + audit | — | Yes (AA blockers) |

### 7.2 Golden fixtures: format, recording and regression rules

**Principle.** A golden fixture is a **landmark sequence as JSON, never raw video**. Video from paid recording sessions stays in the research account (DC-11, faces blurred). Only landmark streams and labels leave that account, and only into the private fixture store (`GOLDEN_FIXTURES_URI`). Git holds only **synthetic** fixtures (generated by code) for unit tests.

**Files.** Two JSON files per clip, plus a manifest.

```text
<GOLDEN_FIXTURES_URI>/v1/
  manifest.json                         # clip_id → sha256, split, ex_id, view, tier, model version
  EX-01/side/gc_000123.landmarks.json
  EX-01/side/gc_000123.labels.json
packages/exercise-engine/test/fixtures/synthetic/   # generated, committed
```

`*.landmarks.json` (schema `packages/contracts/golden-landmarks.v1.schema.json`):

```json
{
  "schema": "repsight.golden.landmarks.v1",
  "clip_id": "gc_000123",
  "ex_id": "EX-01",
  "view": "side",
  "conditions": { "distance_m": 3, "lighting": "bright", "clothing": "tights", "device_tier": "B" },
  "source": { "kind": "paid_session", "release_ref": "REL-0042", "split": "dev" },
  "pose": { "backend": "mediapipe", "variant": "full", "runtime": "mediapipe-python 1.1.1", "running_mode": "VIDEO", "model_sha256": "<sha256>" },
  "fps": 30,
  "layout": "mp33_body_22",
  "frames": [
    { "t_ms": 0, "lm": [0.512, 0.301, -0.12, 0.98, 0.99], "world": [0.01, -0.42, 0.03] }
  ],
  "sha256": "<sha256 of frames>"
}
```

Each `lm` array holds 22 landmarks × `[x, y, z, visibility, presence]` = 110 numbers (the example shows the first 5); each `world` array holds 22 × `[x, y, z]` = 66 numbers. Points 0–10 (face) are never present. No participant name, face data or free text is allowed.

`*.labels.json` (schema `packages/contracts/golden-labels.v1.schema.json`):

```json
{
  "schema": "repsight.golden.labels.v1",
  "clip_id": "gc_000123",
  "labellers": ["coach_07", "coach_12"],
  "adjudicated": true,
  "reps": [
    { "index": 1, "start_ms": 1200, "end_ms": 3400, "phases": [{ "name": "descent", "start_ms": 1200 }],
      "errors": [{ "code": "ERR-EX01-01", "severity": 1 }], "quality": [] }
  ],
  "set": { "expected_reps": 8, "out_of_frame": false, "occlusion": false }
}
```

**How to record fixtures.**

| Step | Who | Command / action |
|---|---|---|
| 1 | Session coach | Record a paid session under a written release that names model training (canon §8.4); upload to the research account |
| 2 | Pipeline (E13-T04) | `uv run ml/golden/extract.py --clip <id>`: Pose Landmarker Full, VIDEO mode, `mediapipe` 1.1.1 → drop points 0–10 → write `landmarks.json` with model SHA-256 |
| 3 | Two coaches + adjudicator | Label in Label Studio on the skeleton replay; export with `ml/labelling/export.py` → `labels.json` |
| 4 | ML/CV engineer | `uv run ml/golden/register.py --split dev|calib|test` assigns the split **by subject**; held-out test participants are never used for calibration |
| 5 | CI | `pnpm harness` downloads by manifest, checks SHA-256, runs the engine, compares with labels and with the production bundle |

Team-only on-device recording: the development build has a "fixture recorder" (compile flag, absent from release builds) that writes `PoseResult` streams, never pixels, for team members who signed the release.

**Regression rules** (02 §5.4): CI fails if the exact-rep rate drops >1 point; any GA cue's precision drops >0.02; any set moves from exact to off by ≥2; or any GA cue falls below KPI-02 on the development split. The held-out test split runs only at milestones (M2, M3, M4) and for Beta → GA promotion (BR-22).

### 7.3 Gates by stage

| Stage | Gate |
|---|---|
| Every PR | Lint, types, unit, contract, integration, linters (claims, model IDs, forbidden APIs, SDK allowlist, licences, analytics allowlist), secret scan, OpenAPI diff, migration up/down, path-filtered harness and safety eval |
| Merge to `main` | All of the above + nightly safety eval and Maestro |
| Content release | Content checks, placeholder check (no `CLINICAL_REVIEW_REQUIRED`), clinician co-sign, safety eval or harness, signature |
| Release branch | Device-lab run on 9 phones, golden regression, held-out run at milestones, safety eval on the exact prompt/model/KB/rule tuple, store copy linter, 02 §12.6 checklist |
| Milestone | Canon §14.2 exit criteria with evidence links in `docs/PROGRESS.md` |

### 7.4 Failure-mode test matrix (02 CV-32)

| FM | Test level | Test name |
|---|---|---|
| FM-01 | Native + UI | `fm01_mediapipe_load_fail_manual_logging` |
| FM-02 | Native (iOS) | `fm02_ios_fallback_apple_vision` |
| FM-03 | UI (Maestro) | `fm03_camera_permission_denied` |
| FM-04 | Engine | `fm04_tracking_lost_pauses_reps` |
| FM-05 | Engine | `fm05_wrong_view_counts_only_view_independent_rules` |
| FM-06 | Engine | `fm06_low_light_rules_abstain` |
| FM-07 | Native | `fm07_thermal_ladder_l1_to_l3` |
| FM-08 | Native + unit | `fm08_bundle_signature_fail_keeps_last_good` |
| FM-09 | Engine | `fm09_baseline_invalid_population_default_beta` |
| FM-10 | Mobile unit | `fm10_local_db_write_retry` |
| FM-11 | UI | `fm11_app_killed_recovers_completed_sets` |
| FM-12 | Engine | `fm12_second_person_resets_tracking` |
| FM-13 | Engine + native | `fm13_phone_moved_pauses_rules` |

### 7.5 LLM safety-eval gates and never-rule tests

| Item | Rule |
|---|---|
| Suite | 02 §7.12: ≥1,050 red-team items (15 classes × benign, edge, red-flag, jailbreak, eating-disorder risk, minor, crisis), HealthBench consensus subset, 200 dietitian-labelled meal photos, OWASP LLM/Agentic prompt-injection cases. Items are written **with clinicians**; Claude Code may draft structure and jailbreak/injection patterns, never clinical expected answers |
| Deterministic first | Template-ID equality, never-rule patterns, KB card IDs, numeric checks; then the Opus judge (`claude-opus-5-5`) with rubrics |
| Gates | Never-rule or crisis-routing failures = 0 (KPI-07); red-flag recall ≥0.98 (KPI-08); medication-answer grounding 100% (KPI-09); clinician rubric not lower than production by >3% |
| Never-rule unit tests | `services/api/tests/safety/test_never_rules.py` has at least one deterministic test per never-rule 1–9 (canon §9.6) against the output guard, plus planner tests for never-rule 5 (kcal floors, 0.9 kg/week cap) |
| Mock vs live | PR runs use recorded fixtures; nightly and release runs call the API live with eval-only keys (no user data, so the Batch API is allowed here only, canon §0.7) |
| Records | Each run writes an `eval_runs` row; the run ID goes into release notes and `llm_calls` |
| Failure handling | Any failure blocks merge; clinicians review every failure (HITL-04); Claude Code may not edit an expected answer to make a test pass |

### 7.6 Performance budgets and coverage targets in CI

| Budget | Gate | Where |
|---|---|---|
| Pose FPS (PERF-01, NFR-001) | A ≥30, B ≥20, C ≥15 (Lite) over 20 min | Nightly synthetic feed; weekly live rig |
| Frame → overlay p95 (PERF-02, NFR-002) | A ≤100 ms, B ≤150 ms, C ≤200 ms | Device lab |
| Rep end → cue p95 (PERF-03, NFR-003) | ≤500 ms A–B, ≤700 ms C | Device lab + production telemetry |
| Thermal (PERF-08, NFR-016) | No `serious` state within 20 min on A–B | Device lab |
| Cold start (PERF-04, NFR-011) | p95 A ≤2.5 s, B ≤4.0 s, C ≤6.0 s (DEC-003) | Device lab, 20 launches |
| Peak memory (PERF-06) | A ≤450 MB, B ≤350 MB, C ≤300 MB | Device lab, per milestone |
| Battery (PERF-07, NFR-017) | 30-min session: A ≤10%, B ≤13%, C ≤16% (DEC-005) | Device lab, per milestone, median of 3 runs |
| App download size (PERF-11) | ≤80 MB iOS per device | EAS build artefact check |
| Non-LLM API p95 (PERF-20–PERF-23, NFR-009) | Reads ≤250 ms, sync write ≤400 ms, medicine search ≤600 ms, config ≤150 ms (DEC-004) | Locust on staging nightly; regression >20% blocks deploy |
| Coach first SSE event / first reply token p95 (PERF-24, PERF-25, NFR-010) | ≤1.0 s / ≤6.0 s (DEC-002) | Staging with live eval keys, nightly |

| Coverage target | Value | Source |
|---|---|---|
| `packages/exercise-engine/src` | ≥90% lines | Playbook target |
| `services/api/app/constraints`, `app/safety`, `app/planner` | ≥85% lines; 100% of rule IDs and never-rules have tests | 02 §12.3; NFR-039 |
| `apps/mobile/src/cv`, `apps/mobile/src/sync` | ≥80% lines | 02 §12.3 |
| Other backend modules | ≥75% lines | Playbook target |
| Content | 100% of RULE IDs have a fixture; 100% of templates render in every live locale | Playbook target |

### 7.7 Definition of Done (every task)

- [ ] Code, tests and docs in one PR; CI green.
- [ ] Acceptance criteria of the cited FR/NFR/BR/CV IDs proven by named tests.
- [ ] No golden rule broken (PR template GR checklist ticked).
- [ ] No health values in logs, analytics or error bodies.
- [ ] Every new user string externalised, linted for banned claims, and accessible (§5.9).
- [ ] No `CLINICAL_REVIEW_REQUIRED` marker reached a release branch or content release.
- [ ] OpenAPI and generated client updated if the API changed; migration up/down tested if the schema changed.
- [ ] ADR written if a pin, dependency, data flow or model route changed.
- [ ] `docs/PROGRESS.md` updated; any conflict logged in `docs/DECISIONS.md`.
- [ ] Demo steps written in the PR description.

---

## 8. Human-in-the-Loop Checkpoints

Claude Code **stops and asks** at each checkpoint below. It prepares the material (draft, diff, evidence, question) and writes "WAITING FOR HUMAN: HITL-## — <one-line question>" at the top of the session summary and in `docs/PROGRESS.md`. It never marks the item done itself.

| ID | Checkpoint | Trigger | Who signs | Claude Code prepares |
|---|---|---|---|---|
| HITL-01 | Clinical content sign-off | Any KB card, constraint rule, `med_class_map`, screening rule, program progression, swap table, nutrition formula, red-flag wording, safety lexicon or eval expected answer | Clinical lead (PharmD) or the reviewer for the discipline (RD, DPT, sports-medicine physician) | Structure with `CLINICAL_REVIEW_REQUIRED` placeholders, source links from canon §9.4, tests that will pass once values exist |
| HITL-02 | Legal and user-facing compliance text | Privacy policy, Consumer Health Data Policy, consent texts, terms, subscription and renewal copy, store descriptions, disclaimers, DPDP notice | Counsel (CEO accountable) | Draft from canon wording (§11.5 statement verbatim), list of claims checked |
| HITL-03 | Regulatory or market decision | New market, IF-6 (D-09), GLP-1 wording (D-16), qualification memos | Counsel + CEO | Feature-flag plan, affected strings |
| HITL-04 | Safety eval failure review | Any eval failure or production never-rule hit | Clinical lead | Failure list with transcripts (eval items only) |
| HITL-05 | Production data and infrastructure | Terraform apply to staging/prod, prod migrations, any access to production data, research-account data | Tech lead | Plan output, rollback steps |
| HITL-06 | Any change to safety behaviour | Guards, templates, crisis numbers, never-rule tests, quota bypass, ED-safe logic, regional policy | Tech lead + clinical lead | Diff, eval run ID, reasons |
| HITL-07 | Coaching and cue copy | New or changed cue copy, benchmark copy, debrief templates | Certified coach reviewer + banned-claims linter | Copy table with GA/Beta labels |
| HITL-08 | Threshold calibration with real data | Any threshold or filter value derived from recorded data; Beta → GA promotion | ML/CV engineer | Harness and held-out reports, stratified results |
| HITL-09 | Technical owner decisions | D-05, D-12, ADR acceptance, new dependency outside allowlists | Tech lead (CEO for D-12) | ADR draft with evidence |
| HITL-10 | Model routing and model/prompt changes | D-02, D-08, any `llm_routes` change in staging/prod, any production prompt version change | CEO (accountable) + tech lead + clinical lead | Eval comparison on all four D-02 criteria; ADR-027 entry |
| HITL-11 | Payment configuration | Products, prices, trials, offerings, web checkout, partner codes | CEO | Product ID table from canon §12.1 |
| HITL-12 | Accounts, credentials, contracts | Any new vendor account, API key, licence download (RxNav-in-a-Box), data licence (IFCT 2017) | CEO / tech lead | List of what is needed and why |
| HITL-13 | Store submission | TestFlight external testing, Play closed testing, production submission (2027-05-17 for V1.0) | CEO | Store kit checklist (02 §12.6 rows 8–9) |
| HITL-14 | Datasets and model weights | Any new dataset, pretrained weights or licence question (canon §8.4, §10.5) | ML/CV engineer + counsel | Licence text and `ml/datasets/REGISTER.md` entry |

---

## 9. Copy-Paste Prompts for Claude Code

Paste one prompt to start each epic. Each prompt is self-contained. For later sessions in the same epic, say: "Continue <epic>: next open task in docs/PROGRESS.md."

### 9.1 E0 — Repo bootstrap and CI

```text
You are building RepSight. Read CLAUDE.md, docs/05-build-playbook.md §1–§5 and §6.3, and docs/research/00-product-canon.md §0, §2.4, §10.
Goal: complete epic E0 (tasks E0-T01..E0-T09) one task per PR.
Constraints: pinned versions only (playbook §4.1; pnpm and uv pins recorded in ADR-033); no ad/attribution SDKs; banned-claims list copied verbatim from canon §2.4 into content/claims/banned.yaml; model-ID linter allows only claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5.
Outputs: workspace, docker-compose.yml, tools/ci linters, .github/workflows/ci.yml, PR template, CODEOWNERS, ADR-001/002/033 drafts, docs/PROGRESS.md and docs/DECISIONS.md (DEC-001..DEC-012 from playbook §1.5), CLAUDE.md commands.
Tests: pytest positive/negative cases for every linter; one Jest and one pytest smoke test.
Stop and ask if: an account or secret is needed (HITL-12), a pinned version cannot install, or a licence is unclear.
```

### 9.2 E1 — Backend foundation

```text
You are building RepSight. Read CLAUDE.md, playbook §6.4 and §7, 02-technical-specification.md §8.1–§8.4, §9.1–§9.4, §9.7, §10.2–§10.4, §10.8, Appendix A–B, and BRD FR-001–FR-003, FR-064, BR-10.
Goal: epic E1 tasks E1-T01..E1-T11, one per PR, in services/api (package `app`) and infra/terraform.
Constraints: the age gate runs on the phone before sign-in (DEC-010): POST /v1/public/underage-attempts is unauthenticated, takes store_country only and stores no IP, device ID or date of birth; bootstrap re-checks the date of birth and never keeps an under-18 user; home_region on every user-scoped row; `_enc` columns use envelope encryption; RFC 9457 errors; idempotency keys on POST; logs use pseudo_id and never health values; AUTH_MODE=local-dev refused outside ENV=local; Terraform plan only.
Outputs: migrations, account/profile/consent endpoints, signed /v1/config, committed openapi.yaml, generated packages/api-client.
Tests: row-ownership test for every member endpoint, age-gate boundaries, consent records, encryption round trip and crypto-shred, idempotency replay, Schemathesis.
Stop and ask if: you need to apply Terraform (HITL-05), consent or age-gate wording is needed (HITL-02), or 02 conflicts with the BRD (log in DECISIONS.md).
```

### 9.3 E2 — Mobile foundation

```text
You are building RepSight. Read CLAUDE.md, playbook §5.1, §5.8, §5.9 and §6.5, 02 §2.5, §3.1, §4.12, §8.2, and BRD FR-001–FR-006, FR-064, BR-10, NFR-011, NFR-018, NFR-028–NFR-031.
Goal: epic E2 tasks E2-T01..E2-T10 in apps/mobile (Expo SDK 58, RN 0.88.0, TypeScript ~6.0.3, development builds only, never Expo Go).
Constraints: iOS 17.0 / Android API 28 floors, targetSdk 36, compileSdk 37; SI storage, locale display; all strings in i18n catalogues; SQLCipher DB excluded from iCloud backup; API only via packages/api-client; WCAG 2.2 AA checklist on every screen; M1 library versions only from ADR-006.
Outputs: design system, navigation, neutral age gate as the first step (before any sign-in, DEC-010), auth, onboarding, consent screens, encrypted DB, sync outbox.
Tests: Jest (units, outbox), Maestro flows (age gate pass → sign-in, age gate fail → no auth call, onboarding, offline → reconnect).
Stop and ask if: ADR-006 versions are not yet accepted (HITL-09), legal wording is needed (HITL-02), or a library is not New-Architecture-ready.
```

### 9.4 E3 — PoseEngine and camera pipeline

```text
You are building RepSight. Read CLAUDE.md (golden rules GR-01, GR-02), playbook §6.6 and §7.4, 02 §4.1–§4.4, §4.11, §4.12, §6, and canon §8.1–§8.3.
Goal: first the M1 spike (E3-T01..E3-T07) proving Full model ≥30 FPS on Tier A and ≥20 FPS on Tier B over 20 min, p95 frame-to-overlay ≤150 ms on Tier B, and iOS packaging in a release build; then E3-T08..E3-T12.
Constraints: PoseEngine.nitro.ts exactly as 02 §4.2.1; MediaPipe Android 1.1.1 and iOS MediaPipeTasksVision 1.0.0 (D-05 default); VIDEO mode, num_poses = 1; face points 0–10 never copied to any output; no pixel persistence; no pixels to JS; dispose every frame in try/finally.
Outputs: native module (Swift + Kotlin), camera session, Skia overlay, synthetic-feed build, device-lab runner, thermal governor, Apple Vision fallback, Setup Coach, FM-01..FM-13 handling, ADR drafts (ADR-003, ADR-004, ADR-029, ADR-030).
Tests: CV-04, CV-05, CV-06, CV-07, governor tests, one test per FM row.
Stop and ask if: the pod fails in a release build (D-05, HITL-09), M1 gates look likely to fail (D-12), or any threshold needs real-data tuning (HITL-08).
```

### 9.5 E4 — Exercise engine

```text
You are building RepSight. Read CLAUDE.md, playbook §6.7 and §7.2, 02 §4.3, §4.5–§4.10, §5.2–§5.5, and canon §7 (EX-01..EX-10, 26 ERR codes) and §8.3.
Goal: epic E4 in packages/exercise-engine (pure TypeScript, no React Native imports) plus content/exercises and ml/golden. Do EX-01 and EX-03 first (ML-07 at M1), then the other eight.
Constraints: thresholds relative to the user's baseline; start values from canon §7.2 marked "calibrate in M2/M3"; cue only if every joint passes the visibility gate in ≥80% of the rep's frames, else "form not assessed"; ≤1 corrective cue per rep; frontal-plane cues stay Beta; no spinal-rounding cue; LLMs never produce live cues; golden fixtures are landmark JSON, never video.
Outputs: schema, filters, state machine, rules, metrics, autoregulation, cue scheduler, harness runner and CI job, mobile worklet glue, calibration tools.
Tests: CV-13, CV-16, CV-20, CV-22, CV-24, CV-26, harness regression rules; ≥90% line coverage.
Stop and ask if: a threshold must be set from recorded data (HITL-08), cue copy is new (HITL-07), or a dataset licence is unclear (HITL-14).
```

### 9.6 E5 — Workout player, programs, session sync

```text
You are building RepSight. Read CLAUDE.md, playbook §6.8, 02 §2.4.1–§2.4.2, §4.10.2, §8.5.1–§8.5.2, §9.4 (programs … form_events), BRD FR-026, FR-030–FR-034, FR-038, BR-11, BR-24.
Goal: epic E5 tasks E5-T01..E5-T10.
Constraints: sync payload has per-rep metrics only (no keypoints, pixels or face data); POST /v1/sessions/sync is idempotent; every plan change is a validated proposal the user confirms, with a "Why this changed" card citing data or a rule ID; program progressions and the swap table are CLINICAL_REVIEW_REQUIRED placeholders until signed; voice audio never stored.
Outputs: migrations, sync API, payload builder, planner and validator, proposals API, program structures, workout player, camera set flow, plan cache, voice logging (Beta).
Tests: CV-28, CV-29, validator property tests, Maestro camera session with injected video → sync → history.
Stop and ask if: clinical progression values or swaps are needed (HITL-01), or the payload must carry anything new (privacy review, HITL-06).
```

### 9.7 E6 — Medication profile and constraint engine

```text
You are building RepSight. Read CLAUDE.md (GR-04, GR-05, GR-06, GR-09), playbook §6.9 and §8, 02 §2.4.4, §7.8, §7.9.2–§7.9.3, §8.5.4, and canon §9.4–§9.6.
Goal: epic E6: rule schema and loader, RxNav client, deterministic constraint engine, medicines API, screening and gates, red-flag check-ins with fixed templates, mobile health screens, planner integration; Beta dose-cycle suggestions; V1.0 classes, caffeine counter and heat alerts.
Constraints: the engine changes the plan, never the medicine; no dosing logic; no numeric glucose or BP thresholds in copy; NO clinical values written by you — every rule effect, card text, screening rule and template is a CLINICAL_REVIEW_REQUIRED placeholder; crisis numbers copied verbatim from canon §9.6; templates work offline and are never metered.
Outputs: app/constraints, app/medicines, app/health_profile, app/safety/checkin_rules.py, content/rules structures, apps/mobile/src/features/health.
Tests: one fixture per RULE ID, class combinations, uncovered-medicine card, templates per market, offline templates, gate pause; ≥85% coverage on app.constraints.
Stop and ask if: any clinical content is needed (HITL-01), any safety behaviour changes (HITL-06), or RxNav access is missing (HITL-12).
```

### 9.8 E7 — AI coach

```text
You are building RepSight. FIRST load the claude-api skill and follow it. Then read CLAUDE.md, playbook §6.10 and §7.5, 02 §7 (all), §8.5.3, §8.7, and canon §9.
Goal: epic E7: LLM gateway (only module importing anthropic 1.15.0), input and output guards, templates, KB retrieval, 14 strict tools, orchestrator with prompt caching, SSE chat API, mobile chat, debrief and narration, ED-safe mode, eval harness and CI gate, degraded modes; Beta coach memory.
Constraints: claude-opus-5-5 on every route until D-02 says otherwise; structured outputs; no API citations (a 400 with output_config.format): tools return KB cards, the reply lists kb_card_ids, the server validates them and the app renders each card verbatim with its sources (02 §7.7.3, ADR-011); strict tools that only read or propose; no Batch/Files API with user data; no server-side fallbacks; refusal → TPL-REFUSAL-01; the model never writes red-flag text; minimised payloads (pseudonymous key, no name, email, keypoints or clips); AI notice at session start and a persistent "AI coach" label; LLM_MODE=mock in CI.
Outputs: app/llm, app/safety, app/kb, app/coach, ml/evals, apps/mobile/src/features/coach.
Tests: LLM contract fixtures (refusal, max_tokens, invalid output), payload-minimisation test, never-rule tests 1–9, quota bypass for safety, India no-counselling flag test, eval gates KPI-07/08/09.
Stop and ask if: KB cards, lexicons or eval expected answers need clinical text (HITL-01), any eval fails (HITL-04), or a route/model/prompt change is proposed (HITL-10).
```

### 9.9 E8 — Nutrition and meal scans

```text
You are building RepSight. Read CLAUDE.md, playbook §6.11, 02 §8.5.1 (meal scans, nutrition), §8.5.6, §9.4 (foods_cache, nutrition_entries, meal_scans), BRD FR-045–FR-047, BR-05, BR-25. Load the claude-api skill before touching the meal_parse route.
Goal: epic E8 tasks E8-T01..E8-T05.
Constraints: provider per D-10 with attribution; meal photo deleted after parsing, forced delete ≤24 h; CON-04 required; the protein/fibre formula and the floor default for users without a recorded sex are CLINICAL_REVIEW_REQUIRED until the RD signs; kcal-floor flags 1,200 kcal/day (women) and 1,800 kcal/day (men) and the 0.9 kg/week cap come from canon §0.8 #4 and §9.6; ED-safe mode hides kcal, weight, BMI and deficits; no food names or kcal in logs or analytics.
Outputs: app/nutrition, retention job, apps/mobile/src/features/food.
Tests: retention, meal_not_food, floor boundaries, ED-safe filtering, meal-photo eval items.
Stop and ask if: D-10 is undecided or an account is missing (HITL-12), or nutrition values are needed (HITL-01).
```

### 9.10 E9 — Progress, quality volume, benchmarks

```text
You are building RepSight. Read CLAUDE.md, playbook §6.12, 02 §8.5.1 (progress, benchmarks, health sync), §9.4 (benchmarks, wearable_daily_summaries), BRD FR-050–FR-053, BR-26, canon IF-2 and IF-3.
Goal: epic E9: history and weekly insights (MVP), quality-volume ledger and health-platform sync (Beta), monthly camera benchmarks (V1.0).
Constraints: quality volume counts only assessed reps with no GA error; PRs on quality reps; never drop a rep silently; camera numbers are labelled estimates with error bands; benchmarks are "strength benchmarks", never fall-risk tests; health sync reads daily summaries only per granted type (CON-07).
Outputs: app/progress, app/health_sync, apps/mobile/src/features/progress, platform health adapters.
Tests: ledger property tests, benchmark rules (EX-08 full stands only, EX-09 quality seconds), banned-claims lint on copy, per-type permission tests.
Stop and ask if: benchmark copy is new (HITL-07) or health-platform declarations are needed (HITL-02).
```

### 9.11 E10 — Subscriptions, paywall, quotas

```text
You are building RepSight. Read CLAUDE.md, playbook §6.13, 02 §2.4.5, §7.11, §8.5.1 (entitlements), §8.6, canon §9.7 and §12.1, BRD FR-059–FR-062, BR-01, BR-02, BR-11–BR-16.
Goal: epic E10: RevenueCat entitlements and webhook, quotas and abuse limits, tier gating, Beta soft paywall, V1.0 subscription compliance.
Constraints: safety templates, red-flag flows and crisis routing never count against quotas and are never paywalled; quotas exactly as canon §9.7 per tier and market; 7-day trial on annual plans only; prices only from store/RevenueCat (canon §12.1 values); never block store refunds; no health data to RevenueCat.
Outputs: app/billing, apps/mobile/src/features/paywall, platform purchases module.
Tests: quota table generated from canon §9.7, safety bypass, webhook auth, trial rules, cost breaker.
Stop and ask if: products, prices or offerings must be created in App Store Connect, Play Console or RevenueCat (HITL-11), or paywall/renewal copy is needed (HITL-02).
```

### 9.12 E11 — Privacy and compliance features

```text
You are building RepSight. Read CLAUDE.md (GR-01–GR-03, GR-10), playbook §6.14, 02 §10 and §9.6, canon §11, BRD FR-064–FR-068, BR-09, BR-17–BR-19, NFR-023, NFR-024, NFR-033, NFR-037.
Goal: epic E11: consent center (CON-01..CON-12), export, in-app and web deletion with crypto-shredding, AI disclosure, V1.0 regional policy engine, network privacy test, Beta keypoint contribution (CON-08).
Constraints: withdrawal as easy as granting; deletion within 30 days, backups roll off within 35; revoke Sign in with Apple tokens; retention exactly as canon §11.1; regional rules live only in signed config; keypoint contributions exclude face points and go to the research account.
Outputs: app/privacy, app/content/market_policy.py, app/research, consent center UI, privacy e2e tests.
Tests: deletion across all tables/S3/Valkey/vendors, export completeness vs DC-01..DC-15, per-consent withdrawal effects, per-market flags, network proxy test.
Stop and ask if: legal or consent text is needed (HITL-02), production data is involved (HITL-05), or a new data flow appears (ADR + HITL-06).
```

### 9.13 E12 — Analytics, notifications, observability

```text
You are building RepSight. Read CLAUDE.md (GR-10), playbook §6.15, 02 §12.2 and §13, BRD FR-057, FR-058, BR-29, NFR-024, NFR-034, NFR-035.
Goal: epic E12: analytics allowlist and typed wrapper, Sentry and OpenTelemetry, reminders and preferences, Beta lifecycle notifications, dashboards and alerts.
Constraints: PostHog gets only events and properties in analytics/events.yaml; no health values, free text, autocapture, replay or IP; consent by market (CON-11); push payloads never contain medicine or health words; logs use pseudo_id; KPI sources for safety and cost come from our DB, not PostHog.
Outputs: analytics/events.yaml, platform analytics module, app/core/telemetry.py, app/notify, observability Terraform module.
Tests: allowlist checker, property tests on event payloads, push-payload linter, scrubber test.
Stop and ask if: notification wording is new (HITL-02) or an alert needs an on-call tool account (HITL-12).
```

### 9.14 E13 — Internal tools

```text
You are building RepSight. Read CLAUDE.md, playbook §6.16, 02 §12.1, §4.5.4, §5.3.4, §7.7.4, §8.3, §8.5.1 (admin endpoints).
Goal: epic E13: content checks, signed publish-content workflow and manifest, RepSight Studio (FastAPI + Jinja2 + HTMX in tools/admin) with roles and two-person review, labelling pipeline (Label Studio, BlazePose Heavy pre-labels, two coaches + adjudicator), exercise-definition editor with staged rollout, Beta ops console.
Constraints: content-as-code in Git; approvals recorded with name, role and time; a content-reviewer cannot approve medication content; publishing requires clinician co-sign and a passing eval or harness; rollout 5% → 25% → 100%, ≥72 h and ≥500 sets per stage (DEC-007); HTMX served from our static files; support tools show no health values and audit email reveal.
Outputs: tools/admin, .github/workflows/publish-content.yml, app/content, ml/labelling.
Tests: signature/manifest tests, bucket stability for 10,000 synthetic users, guard breach halt, role tests.
Stop and ask if: KMS keys or the GitHub App must be created (HITL-12), or a release would publish clinical content (HITL-01).
```

### 9.15 E14 — Beta readiness and launch

```text
You are building RepSight. Read CLAUDE.md, playbook §6.17 and §8, canon §11.6, §14.2, §15, 02 §10.13, §12.6, and 03 §2.4–§2.5.
Goal: prepare M3 (2027-04-09), M4 (2027-05-14) and launch (2027-06-01): validation-study tooling and stratified reports, methodology-page draft from results only, D-02 eval comparison (no traffic moves), device-lab and load-test reports, security fixes, store-kit drafts, WCAG fixes, runbooks and release-candidate checklist.
Constraints: report measured results only, never invent numbers; every stratum >5 points below the overall rep accuracy blocks GA for that exercise; store and methodology text must pass the banned-claims linter and canon §2.4; do not submit to stores or change model routing.
Outputs: ml/validation, docs/store drafts, docs/runbooks, reports linked in docs/PROGRESS.md.
Tests: report generators unit-tested on synthetic data; release checklist automation.
Stop and ask if: any gate fails (CEO decides per 03 §2.8), legal/store text needs sign-off (HITL-02, HITL-13), or D-02 results are ready (HITL-10).
```

---

## 10. Progress Tracking

Build state lives in the repository, not in anyone's memory or chat history, so that any session (Claude Code or human) can stop at any point and the next one can resume cold. Three places hold it.

### 10.1 The three records

| Record | Holds | Who writes | Who approves | Read when |
|---|---|---|---|---|
| `docs/PROGRESS.md` | Where the build is now: current task, epic and task status, blockers, waiting-for-human items, last verified gates, open deviations, short session log | Claude Code, in the same PR as the work | Tech lead (through PR review) | First thing in every session |
| `docs/DECISIONS.md` | Why something is the way it is: conflicts between documents, deviations from the spec, clarifications, records of owner decisions (D-##), each as a DEC-### entry | Claude Code drafts; the owner decides | The DEC entry's owner (§1.5 column) | At the start of each epic (open entries touching it) and whenever a conflict appears |
| `docs/adr/ADR-###-slug.md` | Architecture decisions with evidence: pinned versions, dependencies, data flows, model routing, signing | Claude Code drafts with status `Proposed` | Tech lead accepts (HITL-09); model routing also HITL-10 | When a task touches the area the ADR covers |

Rule of thumb: **DEC = "the documents disagree, or the build differs from them"; ADR = "we chose an architecture or a pinned version, here is the evidence".** A DEC entry can lead to an ADR (§1.4 step 5); both then link to each other.

### 10.2 `docs/PROGRESS.md` format

**Rules.**

1. One file, fixed section order (template below). The newest state is always at the top; the session log is the only part that grows, and it keeps the last 20 entries (Git history keeps the rest).
2. Status values, exactly: `NOT STARTED`, `IN PROGRESS`, `IN REVIEW` (PR open), `BLOCKED`, `WAITING FOR HUMAN`, `DONE`. A task is `DONE` only when its PR is merged to `main` and its definition of done (§7.7 plus the epic's own) is met. An epic is `DONE` only when every task is `DONE` and its acceptance IDs are proven by named tests.
3. Every "Waiting for human" row uses the §8 wording: `WAITING FOR HUMAN: HITL-## — <one-line question>`. Claude Code never removes a row itself; the human answers in the PR or the session and Claude Code then records the answer (and the DEC entry, if one exists).
4. "Last verified gates" records only results Claude Code saw: the command or CI job, the run ID, the commit SHA and the date. Never write `PASS` for a gate that was not run on that commit.
5. Dates are ISO 8601; weeks are canon W numbers (W1 = 2026-11-02). Never put health data, user data, secrets or real people's names (other than the team's) in this file.

**Template** (E0-T08 creates the file from this, pre-filled with the 16 epics):

```markdown
# RepSight — Build Progress

| Field | Value |
|---|---|
| Last updated | 2026-11-02 (W1) |
| Updated by | Claude Code, session for E0-T01 (reviewer: <tech lead>) |
| Phase | 0 — Foundations & CV spike (W1–W6) |
| Next milestone | M1, 2026-12-11 (canon §14.2) |
| `main` at last verification | `<sha>` |

## Waiting for human

| Item | Question | Asked | Task | Who signs |
|---|---|---|---|---|
| WAITING FOR HUMAN: HITL-12 | <one-line question, e.g. "Create the GitHub organisation and grant the bot access?"> | 2026-11-02 | E0-T01 | CEO / tech lead |

## Current task

| Field | Value |
|---|---|
| Task | E0-T01 — Workspace skeleton |
| Branch / PR | `e0/e0-t01-workspace-skeleton` / #<n> |
| Status | IN PROGRESS |
| Last commit | `<sha>` <conventional commit subject> |
| Next step | <the very next small step, so a cut-off session can resume> |
| Resume prompt | "Continue E0: next open task in docs/PROGRESS.md." |

## Epic status

| Epic | Name | Weeks | Gate | Status | Tasks done | Current / next task | Blocker or HITL | PRs |
|---|---|---|---|---|---|---|---|---|
| E0 | Repo bootstrap and CI | W1 | M1 | IN PROGRESS | 0/9 | E0-T01 | — | — |
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
| E15 | Post-launch V1.x and V2 | W32–W74 | M6–M10 | NOT STARTED | per release (§6.18) | — | — | — |

## Tasks of active epics

| Task | Status | PR | Requirement IDs proven | Tests added | Notes |
|---|---|---|---|---|---|
| E0-T01 | IN PROGRESS | — | NFR-038 | — | — |

## Blockers

| ID | Since | Task | Blocker | Kind (technical / HITL / external) | Needs | Workaround in use |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## Last verified gates

| Gate | Command or CI job | Result | Run ID / evidence | Commit | Date |
|---|---|---|---|---|---|
| Local checks | `pnpm check:all` | not run yet | — | — | — |
| CI on `main` | `ci.yml` | not run yet | — | — | — |
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
| 2026-11-02 | E0-T01 | <one line> | <commands> | <one line> |
```

Blocker IDs use `BLK-###` (sequential, never reused). A blocker that needs a human is also a "Waiting for human" row.

### 10.3 `docs/DECISIONS.md` format

**Rules.**

1. Append-only log. IDs are `DEC-###`, sequential, never reused. DEC-001–DEC-012 come from §1.5.
2. Status: `OPEN` → `DECIDED` → (optionally) `SUPERSEDED by DEC-###`. A `DECIDED` entry is never rewritten; a changed decision is a new entry that supersedes it.
3. Type: `Conflict` (two documents disagree), `Deviation` (the build differs from the spec, §10.5), `Clarification` (the spec is silent or ambiguous and a choice was needed), `Owner decision` (records the outcome of a D-## or a settled canon §0.8 item).
4. Every entry has: context (with exact quotes and file/section of each source), decision (or, while `OPEN`, the temporary choice from §1.3 and the question for the owner), alternatives considered, owner, date raised and date decided, links (PRs, ADR-###, D-##, HITL-##, canon §, spec sections, FR/NFR/BR IDs).
5. While an entry is `OPEN` and touches safety, privacy, legal text, money or clinical content, dependent work stops (§1.4 step 4) and the entry also appears under "Waiting for human" in `docs/PROGRESS.md`.

**Template:**

```markdown
# RepSight — Decisions Log

Append-only. Status: OPEN, DECIDED, SUPERSEDED. Types: Conflict, Deviation, Clarification, Owner decision.
Precedence for temporary choices: playbook §1.3.

## Index

| DEC | Title | Type | Status | Owner | Raised | Decided |
|---|---|---|---|---|---|---|
| DEC-001 | Folder names differ between 02 and the playbook | Conflict | OPEN | Tech lead | 2026-11-02 | — |

---

## DEC-001 — Folder names differ between 02 and the playbook

| Field | Value |
|---|---|
| Status | OPEN |
| Type | Conflict |
| Owner | Tech lead |
| Raised | 2026-11-02 by Claude Code (E0-T08) |
| Decided | — |
| Blocks | Nothing (temporary choice in use) |

**Context.** 02 names paths such as `backend/app/` and `packages/cv-engine`; the playbook layout (05 §3.1) uses `services/api/app/` and `packages/exercise-engine`.
> 02 §7.2: "Each box is a Python package under `backend/app/` (layout in `05-build-playbook.md` §3)."
> 02 §5.4: "the TypeScript package `packages/cv-engine` (pure TS, no React Native imports) runs on the phone inside the worklet and in CI under Node."

**Decision.** OPEN — temporary choice: the playbook layout, with 02's paths mapped one-to-one in 05 §3.3.
Question for the owner: "Keep the playbook layout and update 02's paths in a docs PR?"

**Alternatives considered.**
1. Rename the repository folders to match 02 — more churn in CI path filters and CODEOWNERS.
2. Keep both names with symlinks — confusing; breaks tooling on Windows/WSL.

**Consequences and follow-ups.** Docs PR to 02 after the decision; CI path filters already use repo paths (05 §3.3).

**Links.** 05 §1.5, §3.3; 02 §5.4, §7.2.
```

### 10.4 ADR process (`docs/adr/`)

The ADR template and the list of changes that need an ADR are in §5.6. The process:

| Step | What happens | Who |
|---|---|---|
| 1. Detect | The task changes a pinned version, adds a dependency outside an allowlist, adds a data flow leaving the phone, changes a model route, or changes signing (§5.6) — or a DEC decision changes architecture (§1.4 step 5) | Claude Code |
| 2. Number | Use the number pre-assigned in 02 Appendix C (ADR-001–ADR-033) when the topic is listed there; otherwise the next free number (ADR-034 onward), and draft the docs PR that adds the row to 02 Appendix C (the tech lead owns 02) | Claude Code |
| 3. Draft | `docs/adr/ADR-###-slug.md` with status `Proposed`, in the same PR as the change or in an earlier PR. Evidence is mandatory: test output, device-lab results file (PERF-30), eval run ID or licence text | Claude Code |
| 4. Hold | Code that depends on the decision (for example a new pin in a lockfile) does not merge until the ADR is `Accepted` | Tech lead |
| 5. Decide | The tech lead sets `Accepted` (HITL-09) or rejects it with a reason; model routing (ADR-027 entries) also needs HITL-10; D-## items need their owner | Tech lead (+ owner) |
| 6. Supersede | A changed decision is a new ADR; the old one becomes `Superseded by ADR-###`. ADRs are never deleted or rewritten after acceptance | Claude Code drafts, tech lead accepts |
| 7. Record | `docs/PROGRESS.md` notes the ADR in the task row; any linked DEC entry links back | Claude Code |

### 10.5 Recording deviations from the spec

A **deviation** is anything built differently from 01, 02, the canon or this playbook: a different name, path, field, number, behaviour, sequence or library, including a temporary stub that will ship. It is not a deviation to use `LLM_MODE=mock`, synthetic fixtures, or `CLINICAL_REVIEW_REQUIRED` placeholders (GR-09); those are the planned way of working.

1. **Never deviate silently.** If the deviation touches safety, privacy, legal text, money or clinical content, stop first and ask (§1.4); do not build it until the owner decides.
2. **Write a DEC entry** of type `Deviation`: the spec reference with an exact quote, what the code does instead, why, the risk, and how to revert.
3. **Mark the code** with a one-line comment at the place of the deviation: `SPEC-DEVIATION(DEC-###): <short reason>`. `git grep -n "SPEC-DEVIATION"` must list exactly the open deviation entries; the tech lead checks this at each milestone.
4. **List it** in "Open deviations from the spec" in `docs/PROGRESS.md` and in the PR description ("Deviations: DEC-###").
5. **Close it** one of two ways: the document owner updates the spec in a docs PR (01 and the canon: CEO; 02 and 05: tech lead; Claude Code may draft that PR but never edits 01–04 or the canon to match its own code without the owner's approval in that PR), or the code is changed back. Then remove the marker, set the DEC entry to `DECIDED`, and remove the PROGRESS row.

### 10.6 When to update each file

| Event | `docs/PROGRESS.md` | `docs/DECISIONS.md` | `docs/adr/` | `/CLAUDE.md` |
|---|---|---|---|---|
| Session start | Read: current task, waiting-for-human, blockers. Compare with `git status` and `git log`; if they disagree, stop and ask | Read open entries for the epic | Read ADRs the task touches | Read |
| Task start | Set current task and `IN PROGRESS`; branch name | — | — | — |
| Each green step (tests pass, commit made) | Update "Next step" and "Last commit" in the same commit | — | — | — |
| Conflict found | Blocker row if work depends on it | New `OPEN` entry (Conflict) | — | — |
| Deviation needed | "Open deviations" row | New entry (Deviation), §10.5 | ADR too if architectural | — |
| HITL checkpoint reached | "Waiting for human" row; status `WAITING FOR HUMAN` | Entry if a choice is needed | — | — |
| Owner answers | Remove the waiting row; unblock | Set `DECIDED` with date and answer | Write or update the ADR if a pin or architecture changed | Update if a standing rule changed |
| Pin, dependency, data flow, model route or signing change | Note in task row | — | `Proposed` ADR in the same PR (§10.4) | Update pins only if CLAUDE.md lists them |
| PR opened | `IN REVIEW`, PR link, requirement IDs, tests | — | — | — |
| PR merged (next session checks `main`) | `DONE`; next task becomes current | — | — | — |
| Gate run (CI on `main`, harness, safety eval, device lab, load test) | "Last verified gates" with run ID and commit | — | Evidence link in the related ADR | — |
| Commands or scripts change | — | — | — | "Commands" block (first filled by E0-T09) |
| Milestone review | Exit criteria with evidence links (§7.3); epic statuses | Close or re-date open entries | Accept pending ADRs with gate dates | — |
| Session end, or before any long-running step | Session-log row and "Next step"; commit and push the branch | — | — | — |

---

## 11. Build Risks & How to Handle Them

Canon §17 lists the business risks (R-01–R-18). This section lists the **build-execution** risks: what tends to go wrong while Claude Code builds RepSight, how to notice it early, what Claude Code does on its own, and where it must stop. IDs are `BK-##`. The general rule from 03 §2.8 holds throughout: **we cut features, never gates.** Claude Code never cuts scope, lowers a gate, or edits a label, expected answer or held-out split to make a test pass.

| ID | Risk (canon R-##) | Early signal | What Claude Code does | When to stop and ask |
|---|---|---|---|---|
| BK-01 | **Frame-processor performance** misses the tier gates (R-02) | Nightly device-lab file (PERF-30) shows PERF-01 FPS below the tier gate, PERF-02 p95 rising, PERF-09 dropped frames above 10% (A) or 35% (B), thermal `serious` before 20 min (PERF-08); profiler shows per-frame allocations or work on the JS thread | Profile before optimising; keep pixels and inference native (GR-01, GR-02); reuse buffers; confirm the async runner drops frames when busy and every frame is disposed; check GPU delegate → CPU fallback; use the thermal governor ladder and Lite on Tier C as 02 §4.11 specifies; record each experiment and result in PROGRESS and the ADR-029 draft | M1 gates (Full ≥30 FPS Tier A, ≥20 FPS Tier B over 20 min, p95 frame-to-overlay ≤150 ms Tier B) look unreachable → D-12 (QuickPose evaluation, CEO; HITL-09). Any change that lowers a PERF gate, changes the model variant per tier or adds a native dependency |
| BK-02 | **iOS MediaPipe packaging** fails (D-05, R-08) | CocoaPods trunk is read-only from **2026-12-02**: no new pods or versions can be published, existing ones (`MediaPipeTasksVision` 1.0.0) keep resolving; 1.1.x is not on CocoaPods; RN SwiftPM support is experimental. Watch for `pod install` resolving another version, a crash or missing symbols in a **release** build, `Podfile.lock` drift after `expo prebuild` | Pin `MediaPipeTasksVision` exactly at 1.0.0 in the config plugin and commit `Podfile.lock`; prove it in a release build in E3-T03, well before 2026-12-02; ask for the pod's xcframework and podspec to be archived with SHA-256 in a team artefact store before that date; if the pod fails, vendor the xcframework through the config plugin (D-05 fallback) and draft ADR-003; do not move to SwiftPM | The pod fails in a release build, or the archive needs a store or account (HITL-09 for D-05 by 2026-12-11; HITL-12 for the store); any licence question about vendored binaries (HITL-14) |
| BK-03 | **Accuracy shortfalls** on rep counting or GA cues (R-02, R-03) | Harness exact-rep rate on the development split trending below the KPI-01 path; any GA cue below KPI-02 (precision 0.90 / recall 0.70); assessed-rep rate falling (KPI-05); a stratum >5 points below overall (NFR-008); low inter-rater agreement for an ERR code | Report stratified harness results per exercise, cue and tier; keep a weak cue as Beta tip or "form not assessed" rather than forcing it (abstain, canon principle 2); never tune on the held-out test split; list which exercises are on track for GA. **Scope-cut order (03 §2.8, R-16):** IF-7 (F-076) → IF-6 (F-045, F-075) → F-028 → F-064 → MVP reduced to 6 GA exercises (M2 at risk) → Beta "Should" features F-026, F-056, F-073, F-104 → launch date moves. Claude Code prepares the evidence; it never applies a cut | A GA cue fails KPI-02 at a milestone; M2 or M4 is at risk (CEO decides the cut, 03 §2.8); any threshold set from recorded data (HITL-08); Beta → GA promotion (HITL-08) |
| BK-04 | **App Review or Play rejection** (R-09) | TestFlight external review or Play pre-review feedback on guideline 1.4.1 (health claims), 5.1.2(i) (AI data sharing consent), 5.1.1(v) (account deletion), privacy manifest or labels, Play Health apps / Data safety / Health Connect declarations | Keep the store kit (E14-T07) passing 02 §12.6 rows 7–9 and the banned-claims linter; reviewer notes explain on-device processing and the AI-consent screen; fix technical causes (missing usage string, privacy manifest entry, deletion path) in a PR; draft the reply to the reviewer | Always before any reply or resubmission (HITL-13); any copy change (HITL-02); never remove or weaken a safety behaviour to satisfy review (HITL-06); feature removal is the CEO's call |
| BK-05 | **AI cost overrun** (R-05) | Ops console (F-115) shows AI cost per user, route or tier above the canon §13.2 token math; AI share of net revenue trending above 30% (NFR-035); thinking tokens per turn above plan; prompt-cache hit rate low; cost breaker trips; dev-key spend limit reached. Infrastructure should stay near $1.08 per paying month at 10k-MAU scale (canon §16.2) | Check the cache layout (02 §7.4.3) and cache hits; check tool round trips (≤6), retrieval size (`KB_TOP_K`) and runaway loops; keep CI on `LLM_MODE=mock`; produce a cost report by route with the cause; draft options | Any change to model, effort, `max_tokens` or route (D-02, HITL-10, ADR-027); any change to quotas or prices (canon §9.7, §12.1; CEO, HITL-11) |
| BK-06 | **Anthropic usage-policy change** (R-01, R-13) | The new Usage Policy takes effect **2026-11-12** (medication recommendations and symptom triage are high-risk; fixed rules and wellness content are excluded); any later policy, pricing or model-deprecation notice; refusal stop-reason rate or safety-eval drift rising | Map affected features to GR-14 and the never-rules; keep refusals on `TPL-REFUSAL-01`; confirm AI disclosure at session start and the 18+ gate; make sure the `coach.enabled` kill switch works; summarise the change for the owner without interpreting law | Always: the CEO and counsel confirm the reading of the policy before 2026-11-12 (HITL-03); any change to coach scope or safety behaviour (HITL-06); any model change (HITL-10) |
| BK-07 | **Clinical-review bottleneck** (R-12) | `CLINICAL_REVIEW_REQUIRED` count not falling week on week; Studio review queue ageing; content releases blocked; M2 needs the 6 MVP classes and about 20 KB cards signed | Never fill clinical content (GR-09); send complete review packets (structure, sources from canon §9.4, tests that pass once values exist); track the placeholder count per milestone in PROGRESS; continue non-clinical tasks; order packets by milestone need | A milestone path depends on unsigned content (HITL-01); reviewer capacity needs the CEO (D-07) |
| BK-08 | **Data-collection delay** (R-03) | Recording sessions (W5–W15, 2026-11-30 → 2027-02-12; 60 US + 60 India participants, D-11) behind plan; labelled clips per ERR code below the coverage matrix (02 §5.3.3); releases or consent forms unsigned; labelling throughput below plan (≈600 h) | Keep building on synthetic fixtures and team-only recordings; prioritise EX-01 and EX-03; make the harness report coverage gaps per ERR code; never use unlicensed, scraped or research-only data (GR-11) | Any dataset or weights licence question (HITL-14); any access to research-account data (HITL-05); M2 calibration at risk (CEO, 03 §2.8 order 5) |
| BK-09 | **Dependency or version drift** (R-13) | Lockfile changes outside the task's scope; `pnpm install --frozen-lockfile` or `uv sync --frozen` fails; Expo SDK 58 compatibility warnings; deprecation notices; a high or critical CVE; a pinned version yanked | Frozen lockfiles only; never install "latest" (GR-17); no incidental upgrades inside feature PRs; keep SDK-aligned packages in lockstep; run the pin checker; for a needed bump, a separate PR with an ADR (§10.4) | A pinned version cannot install or has a high/critical CVE; any pin change (ADR, HITL-09); any new dependency outside the allowlists (HITL-09, GR-11) |
| BK-10 | **Usage limits or network outages during long agentic sessions** | Rate-limit or usage-limit messages, timeouts, a session cut off mid-task, a very long context | **Work in small, committed, resumable steps:** one task per session; commit after every green step with a Conventional Commit; update "Next step" in PROGRESS in the same commit; push the branch; write long files in parts and re-read each part; keep scripts and migrations idempotent; stop at a safe point rather than leaving files half-edited. On resume: `git status`, `git log -5`, read PROGRESS, re-run the task's tests, then continue from "Next step". Never regenerate a whole file from memory over existing work | The working tree has changes the session cannot explain; PROGRESS and Git disagree; a push would need force |
| BK-11 | **Spec documents change under the build** | 01–04 or the canon changed since the epic started (`git log` on `docs/`); a cited FR, NFR, BR, PERF, section, endpoint or table no longer exists | Re-read the cited sections at the start of each epic; grep every cited ID before relying on it; log mismatches as DEC entries (§10.3); follow the precedence table (§1.3) meanwhile | The change touches safety, privacy, legal text, money or clinical content (§1.4 step 4) |

*End of playbook.*

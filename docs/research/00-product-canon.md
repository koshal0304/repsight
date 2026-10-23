# RepSight Product Canon (v1.0, 2026-10-17)

**Status:** Decision record (v1.1, 2026-10-18). The five documents in `docs/` were written from this file and are now the working specification. When two documents disagree, this file is the tie-breaker (see 05 §1.3). Section 0.8 lists the decisions settled after the documents were written. Where something is still open, it appears in Section 18 as an owner decision (D-##) with a recommended default; writers use the default until the owner decides.

**Evidence base:** six research briefs, cited as [R1]–[R6]. A citation such as `[R1 S17]` means "brief R1, source S17"; `[R2 #2]` means "brief R2, source 2". Key facts keep their original URL inline.

| Brief | Topic |
|---|---|
| R1 | Competitive landscape (camera form feedback, AI coaches, GLP-1/medication-aware apps) |
| R2 | On-device pose models, datasets, mobile and backend stack versions |
| R3 | AI coach knowledge base, medication-exercise safety, Anthropic platform facts |
| R4 | Regulatory, privacy and app-store compliance (US, EU/UK, India) |
| R5 | Market, pricing, subscription and acquisition benchmarks, unit economics |
| R6 | Novelty check of candidate "unique" features |

---

## 0. Conventions

### 0.1 Document map

| Path (repo) | Document | Owner | Must copy from canon |
|---|---|---|---|
| `docs/01-business-requirements-document.md` | BRD: scope, personas, FR-###/NFR-###, claims rules, compliance | CEO / product owner | §1–5, §7, §9 (safety policy), §11, §12, §15, §17 |
| `docs/02-technical-specification.md` | Architecture, interfaces, data model, ADR-### | Tech lead | §7–11, §13 (token math), §14 (gates) |
| `docs/03-product-roadmap-and-strategy.md` | Phases, milestones, GTM, pricing, KPIs, budget | CEO | §2, §3, §12–18 |
| `docs/04-innovative-features.md` | IF-1..IF-7 deep dives, honest "exists elsewhere" lines | CPO | §2, §5, §6 |
| `docs/05-build-playbook.md` | Step-by-step build plan for Claude Code, test gates, definition of done | Tech lead | §5, §7–11, §14, §15 |
| `CLAUDE.md` (repo root) | Standing instructions for the Claude Code build agent: stack pins, never-rules, privacy boundary, test commands | Tech lead | §8–11, §9.6 never-rules |

### 0.2 ID schemes

| Prefix | Meaning | Format and rule | Range used here |
|---|---|---|---|
| P# | Persona | P1..P5 | P1–P5 |
| F-### | Product feature | Three digits, grouped by module (001–009 onboarding, 010–019 health, 020–039 camera, 040–049 workouts, 050–059 coach, 060–069 nutrition, 070–079 progress, 080–089 notifications, 090–099 subscription, 100–109 privacy, 110–119 admin, 120–129 B2B). IDs are never reused. | F-001–F-123 |
| IF-# | Innovative feature bundle | IF-1..IF-7; each lists its F-### members | IF-1–IF-7 |
| EX-## | Exercise in the camera library | Two digits | EX-01–EX-10 at MVP |
| ERR-EX##-## | Form error for an exercise | Exercise number + two-digit error number | e.g., ERR-EX01-02 |
| FR-### / NFR-### | Functional / non-functional requirement (BRD, Tech Spec) | Each FR cites at least one F-###; each NFR cites a KPI-## or a §8 target | defined by the BRD |
| M# | Milestone | M1..M10 (§14) | M1–M10 |
| R-## | Risk | §17 | R-01–R-18 |
| KPI-## | Key performance indicator | §15 | KPI-01–KPI-28 |
| D-## | Open owner decision | §18 | D-01–D-17 |
| KB-<CLASS>-## | Knowledge-base card (clinician-approved text) | Class codes from §9.5, e.g., KB-BB-01 | ~20 at MVP, ~45 at V1.0 |
| RULE-<CLASS>-## | Constraint-engine rule | Same class codes, e.g., RULE-SGLT2-02 | defined by Tech Spec |
| ADR-### | Architecture decision record | Any change to a pinned version in §10 needs an ADR | defined by Tech Spec |
| CON-## / DC-## | Consent purpose / data class | §11.3 consents CON-01..CON-12; §11.1 data classes DC-01..DC-15 | CON-01–CON-12, DC-01–DC-15 |

### 0.3 Units, dates, currencies, language

- **Storage and computation are always metric/SI:** kg, cm, m, s, m/s, degrees for joint angles, kcal, g, °C. **Display** follows locale, user-overridable: US = lb, ft/in, °F; UK = kg (body weight optionally st/lb), °C; India = kg, cm, °C. Convert only at the UI layer.
- **Dates:** ISO 8601 (YYYY-MM-DD). **Week numbering:** W1 is the week starting Monday 2026-11-02 (kickoff). Release dates are Tuesdays.
- **Currency:** USD is primary for every business figure (costs, budgets, unit economics). Local list prices: USD (US), GBP incl. 20% VAT (UK), INR incl. 18% GST (India); EUR is set at D-15. FX assumption: ₹94 = $1 [R5]. GBP figures are never converted.
- **Kickoff:** Monday **2026-11-02**. Today (canon date): 2026-10-17.
- **Pronouns:** use they/them for every persona and for "the user" in all documents. Never describe users' bodies in evaluative terms.
- **Names:** product working name "RepSight" (D-01). Tiers: Free, Premium, Premium+. Program: "GLP-1 Strength Track". The coach is "the RepSight coach (AI)", never a person, doctor, dietitian, physio or therapist.
- **Model IDs:** `claude-opus-5-5` (default), `claude-sonnet-5-5`, `claude-haiku-5-5`. No other model ID appears in code or docs.

### 0.4 Release vocabulary (used in every table)

| Release | Meaning | Date |
|---|---|---|
| MVP | Feature set of the internal/closed alpha (team + 30 testers) | Code-complete at M2, 2027-03-05 |
| Beta | Features added during the closed beta (500 US testers) | 2027-03-08 → M4 2027-05-14 |
| V1.0 | Public launch, US, iOS | 2027-06-01 |
| V1.x | V1.1 Android US (2027-07-13), V1.2 UK (2027-08-24), V1.3 India (2027-10-05), V1.4 (2027-11-16) | see §14 |
| V2 | V2.0 B2B clinician platform, learned CV models, EU entry | 2028-03-28 |

### 0.5 Confidence and citation rules for writers

1. Every competitor or market fact carries an `[R#]` citation; key facts keep the URL.
2. "Novel" means "not found in the R6/R1 searches as of 2026-10-16", never "first in the world" (§2.4).
3. All proposed accuracy targets in §8 are release gates to validate, not measured results.

### 0.6 Fixed product boundaries (apply to every document)

- General-wellness product for healthy adults 18+ [R4 #2](https://www.fda.gov/media/90652/download). No dosing, no disease thresholds in user copy, no treat/prevent/diagnose/cure claims.
- Raw camera video never leaves the phone unless the user shares one specific clip (§11.2).
- A deterministic, versioned safety-rules engine runs before and after the LLM; the LLM can never override it (§9).

### 0.7 Where the evidence changed the starting guidance

| Starting guidance | What the briefs show | Canon decision |
|---|---|---|
| "Keypoints and metrics sync" | Stored movement series can be gait/biometric data (WA MHMDA, COPPA); R4 says store per-rep summaries; R2 says keypoint telemetry should be opt-in [R4 #31](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010), [R2 #2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) | Per-rep and per-set **metrics** sync by default. **Keypoint time series** stay on the phone and upload only with the separate "Help improve form models" consent, with face landmarks 0–10 removed. |
| Redis | Redis 8.x is RSALv2/SSPLv1/AGPLv3 tri-licensed; Valkey is BSD-3 [R2 #116](https://raw.githubusercontent.com/redis/redis/unstable/LICENSE.txt), [R2 #118](https://github.com/valkey-io/valkey/releases) | Managed **Valkey** (Redis-protocol compatible) on Amazon ElastiCache. |
| Message Batches API (50% off) as a cost lever | Batch and Files are not ZDR- or HIPAA-eligible; Batch keeps data 29 days [R3 #3](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) | **No Batch or Files API for any request containing user data.** Batch only for non-personal jobs (eval runs, KB drafting). |
| Four R6 bundles as headline features | R4: "rehab or pain programmes for a condition" are devices/MDSW in US/EU/India [R4 #14](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) | Bundle (c) is reframed as **Comfort-Range Training (IF-6)**, US-only, V1.4, gated by counsel (D-09). |
| Show ADA guidance verbatim (glucose <90 mg/dL) [R3 #11] | FDA GW excludes diagnostic thresholds in UI; R6 safer phrasing avoids numbers [R6 #21](https://www.fda.gov/media/90652/download) | **No numeric glucose or BP thresholds in user copy.** Users follow their own care team's plan. |
| Evaluate Apple Vision on iOS | Apple 2D has 19 joints and scored below BlazePose in Google's (pre-revision2) test [R2 #3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md) | MediaPipe is primary on both platforms; Apple Vision 2D is the iOS fallback and cross-check; Apple 3D `bodyHeight` is optional calibration. |
| India region strategy | Anthropic `inference_geo` is `global` or `us` only; no India or EU inference residency [R3 #4](https://platform.claude.com/docs/en/manage-claude/data-residency) | India runs from us-east-1 at V1.3 under a disclosed transfer; an ap-south-1 data cell is built "region-ready" and deployed only on a trigger (§10.3). |
| Refusal with optional server-side fallbacks | A fallback that switches models would be an automatic downgrade | Server-side model fallbacks **off**; a `refusal` stop reason returns a fixed template plus resources. |

### 0.8 Decisions settled after the documents were written (2026-10-18)

| # | Decision | Reason |
|---|---|---|
| 1 | The age gate (F-002) runs before account creation (F-001); no account or auth identity is ever created for an under-18 user | Privacy-protective and simpler than deleting a just-created account (BRD review) |
| 2 | API citations are not used; grounding uses server-validated `kb_card_ids` and verbatim card rendering | The citations feature returns a 400 when combined with structured outputs (02 §7) |
| 3 | Recording sessions run W5–W15 (2026-11-30 → 2027-02-12) | 2027-02-12 falls in W15 |
| 4 | kcal-floor flags: 1,200 kcal/day for women, 1,800 for men; RD sets the default when sex is not recorded | R3 §2, from the 2025 ACLM/ASN/OMA/TOS advisory |
| 5 | Infrastructure per paying month at 10k-MAU scale is $1.08 everywhere | Matches §16.2 |
| 6 | Three design-partner clinics are signed by V1.2 (M7) and still active at V1.4 (KPI-26) | Aligns M7 with KPI-26 |
| 7 | Backend and device targets that the canon did not set (API latency, chat first token, availability, battery, cold start, memory) are owned by 02 §6; the BRD NFRs cite the same values | One source for performance numbers |
| 8 | US-based budget variants multiply every people line by 3.2 ($16,000 ÷ $5,000) and leave other lines unchanged, before and after launch | Reproduces §16.1; used in 03 §8 |
| 9 | The research briefs live in `docs/research/` (R1–R6) next to this file | The documents cite them there |
| 10 | Backend API availability target is PERF-27: ≥99.9% monthly (02 §6.3, §12.2); BRD NFR-012 cites it | One availability number across the pack |

---

## 1. Identity

| Item | Decision |
|---|---|
| Working name | **RepSight** (trademark and app-store availability to be checked; D-01). Fallbacks if blocked: "FormSight", "SteadyRep". |
| Tagline | **"Every rep seen. Every plan in context."** |
| Category | Phone-only AI strength coach (general wellness), adults 18+ |
| Launch segment | Adults on GLP-1 medicines who want to keep their strength while losing weight, and adults on everyday medicines that change how exercise feels |

**Positioning statement.** For adults who want to build or keep strength, especially while losing weight on a GLP-1 medicine or while taking everyday medicines that change how exercise feels, RepSight is a phone-only strength coach that sees every rep through the camera, adapts each session to what it saw, and plans within medication-aware safety rules reviewed by clinicians. Unlike camera form apps such as Zing (no nutrition logging) and Coach.AI, neither of which is medication-aware [R1 S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792), and AI health coaches such as Google Health Coach, MyFitnessPal and Oura, which never see how a workout was performed [R1 §2], RepSight closes the loop: **see, reason, adapt, prove** [R1 §6].

**Vision.** Anyone, on any medication and at any fitness level, can build and keep strength safely with a coach that sees how they move and respects their health context.

**Mission.** Turn a phone camera into a trustworthy strength coach that measures every rep, adapts each session within clinician-reviewed safety rules, and proves progress the user can share with their care team.

**Product principles** (every FR and design review is checked against these):

| # | Principle | What it means in practice |
|---|---|---|
| 1 | **Safety is never paywalled** | Medication constraints, red-flag routing, crisis resources, eating-disorder safeguards and intake floors work in every tier and never count against quotas. |
| 2 | **Say nothing rather than something wrong** | Cues fire only above confidence gates; low-confidence reps are counted and marked "form not assessed"; beta cues are labelled [R2 §2.4]. |
| 3 | **Rules decide, the LLM explains** | Deterministic engines own safety and plan validity; the LLM only proposes, explains and narrates structured data; it cannot override a rule [R3 §5]. |
| 4 | **Video stays on the phone** | Only metrics leave the phone by default; a clip leaves only when the user shares that clip (§11.2). |
| 5 | **Context, not medical advice** | No dosing, diagnosis, treatment or symptom interpretation; clinical values come from clinician-approved rules or the user's own clinician; "check with your clinician" is always one tap away [R4 §9]. |
| 6 | **Every change shows its "why"** | Each plan change carries a "Why this changed" card citing measured data or a named rule; the user confirms changes. |
| 7 | **Quality over volume, estimates over false precision** | Progress counts quality reps; camera numbers are labelled estimates with error bands [R6 C16, R6 #33]. |
| 8 | **Respect bodies** | No body-shape comments, ranking or critique (including from the camera), no "burn it off" framing, eating-disorder-safe mode available [R3 #1](https://www.anthropic.com/aup). |

---

## 2. Honest uniqueness statement

### 2.1 What already exists (we do not claim these)

| Capability | Who already ships it (evidence) |
|---|---|
| Real-time camera form cues and rep counting on hardware | Peloton IQ on Bike+/Tread+/Row+ (Oct 2025) and Tread Vision (Sept 2026) [R1 S2](https://www.onepeloton.com/blog/what-is-peloton-iq); Tonal 2 "Smart View" [R1 S9](https://www.tonal.com/products/tonal-2) |
| Real-time phone-camera form feedback plus AI chat | Zing AI ("Zing Vision", 4.8★ from ~31K ratings) [R1 S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792); Coach.AI (camera, nutrition plans, chat, on-device) [R1 S18](https://apps.apple.com/us/app/coach-ai/id6504732473) |
| Upload-a-video form checks | At least nine indie apps (Form Fix, Formax, GymSpotter, SquatEye, …) [R1 §1.3] |
| Clinical camera exercise programs (B2B) | Hinge Health TrueMotion [R1 S33](https://ir.hingehealth.com/news/news-details/2025/Hinge-Health-unveils-new-AI-powered-care-tools/default.aspx); Sword (bought Kaia, $285M) [R1 S34](https://swordhealth.com/newsroom/sword-acquires-kaia-health); Kemtai [R1 S42](https://kemtai.com/) |
| Pose SDKs sold off the shelf | QuickPose, Sency, Kemtai [R1 S44](https://quickpose.ai/) |
| LLM health coaches over wearable and food data | Google Health Coach (Gemini; $9.99/mo, ₹99/mo) [R1 S53](https://techcrunch.com/?p=3120136), [R1 S55](https://www.tech2.com/gadgets/google-replaces-fitbit-app-with-google-health-brings-health-coach-to-india-text-ws-l-10080257.html); WHOOP Coach with EHR medications [R1 S58](https://hlth.com/insights/news/whoop-expands-digital-health-offering-with-healthex-integration-and-clinician-video-visits); Oura Advisor [R1 S61](https://ouraring.com/blog/oura-advisor/); MyFitnessPal AI Coach [R1 S77](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718); Samsung Health Assistant (US beta) [R1 S65]; ChatGPT Health and Claude connectors [R1 S100, S102] |
| GLP-1 companions (dose/side-effect logs, protein, "muscle" content) | MyFitnessPal GLP-1 Support (free) [R1 S78](https://www.bakersfield.com/ap/news/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build/article_594b029e-ed9b-5c1a-ac3b-a4ea46e70908.html); Oura GLP-1 Insights [R1 S63](https://ouraring.com/blog/glp-1-insights/); Noom "Muscle Defense" [R1 S88](https://apps.apple.com/us/app/noom-weight-loss-glp-1-care/id634598719); WeightWatchers GLP-1 Success [R1 S89](https://www.weightwatchers.com/us/how-it-works/glp-1-program); Sword Pulse (employer) [R1 S37] |
| Camera velocity-based training | Metric (velocity-loss alerts 5–45%) [R6 #32](https://www.metric.coach/articles/introducing-real-time-feedback); SetSync; RepSpeed [R6 #34, #35] |
| Medication tracking and interaction warnings | Apple HealthKit Medications API [R6 #18](https://developer.apple.com/videos/play/wwdc2025/321/); Samsung Health interaction warnings [R6 #17](https://www.androidcentral.com/apps-software/samsung-health-medications); Apple VO2 max medication input [R1 S71](https://support.apple.com/en-us/HT211856) |
| "Video never leaves your phone" | Common claim (REPcount, RepChamp, Sency, Peloton "not recorded or stored") [R6 C15] — a trust requirement, not a differentiator |

### 2.2 What is unique about RepSight (combination, Medium confidence)

1. **Medication-aware training changes.** No shipping product was found that changes exercise choice, intensity measure (HR vs RPE), timing, fuelling or safety prompts from a medication list (R6 C1: NOVEL, Medium) [R6 §3 C1]; no consumer fitness app adapts training to beta-blockers, insulin/sulfonylureas, statins or anticoagulants [R1 §3.3].
2. **Camera-verified strength for GLP-1 users.** GLP-1 programs deliver muscle preservation as content or human PTs; none was found that verifies training quality or volume by camera (R1 W2) [R1 §5].
3. **One phone product that combines velocity loss, form drift and an automatic next-set suggestion** (R6 C2: no exact spec found) and counts only quality reps toward progress (R6 C16).
4. **A coach that knows what the camera saw.** No AI coach receives rep-by-rep form or range-of-motion data (R1 W1, Medium-High) [R1 §2 observations].
5. **Camera-enforced comfort-range caps with a shareable movement-discomfort journal** — not found in consumer apps (R6 C6/W1), shipped only within wellness framing (IF-6).

### 2.3 One-sentence differentiator (internal)

> RepSight closes the loop that no consumer app we found closes: it sees every rep, reasons over your nutrition and medication context within clinician-reviewed rules, adapts your next session, and proves strength progress you can share.

External copy must not use "only", "first" or "unique" until the claims register entry has legal and evidence sign-off [R6 recommendations].

### 2.4 Claims we must NOT make (enforced by the CI banned-claims linter, F-114)

| Never say | Why | Say instead |
|---|---|---|
| "First/only app with camera form correction" or "first fitness, diet and medication chatbot" | False [R1 §6] | "A strength coach that sees every rep" |
| "Prevents injuries", "injury-proof", "detects injuries", "diagnoses posture problems" | Device/substantiation [R4 §9] | "Cues to help you keep good form; stop if you feel pain" |
| "Physical therapy", "rehab", "relieves/treats pain" | Rehab for a condition is MDSW/device [R4 #14] | "Train around discomfort; tell your physio if it persists" |
| "Prevents GLP-1 muscle loss", "treats muscle atrophy", "protects your muscle" | Non-wellness claim in FDA GW [R6 #21](https://www.fda.gov/media/90652/download) | "Helps you keep strength while losing weight" |
| "Treats obesity", "reverses diabetes", "lowers your blood pressure", "for eating disorders" | GW exclusions [R4 #2](https://www.fda.gov/media/90652/download) | "Supports your weight-management goals"; "regular activity may help reduce the risk of high blood pressure" |
| "Tells you what dose to take", "adjusts your GLP-1 dose", "safe to stop/start/combine" | Dosing = device; India bars AI counselling [R4 #22](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc) | "Log your medicines and set your own reminders; check with your clinician" |
| "Clinically proven", "medical-grade", "as accurate as a physio/trainer" | GW exclusion 4; Apple 1.4.1; FTC substantiation [R4 #85](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance) | "How our form scores work, and their limits" (methodology page) |
| "AI doctor/dietitian/physio/nurse", "prescribe", "therapy", "your AI companion" | CA AB 489; IL WOPR; SB 243 [R3 #88](https://psychology.ca.gov/laws_regs/ab489_advisory.pdf), [R4 #69] | "AI coach — not a doctor, dietitian or therapist" |
| "Your result is abnormal", "you may have X" | GW notification limits [R4 §1.1] | "You may want to talk to a health professional" |
| "Lose 5 kg in 2 weeks", "burn belly fat", spot reduction | CAP 13; FTC [R4 #86](https://www.asa.org.uk/type/non_broadcast/code_section/13.html) | "Build habits that support your goals" |
| "HIPAA-compliant", "100% anonymous" | GoodRx precedent; Apple consent rules [R4 #28](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising) | "Video is processed on your phone" (true in every mode) |
| Camera heart rate, BP, SpO2 or "readiness" scores | Apple 1.4.1; unvalidated [R4 §1.1] | Nothing in V1 |

---

## 3. Markets & platforms

### 3.1 Launch sequence

| Release | Date | Market | Platforms | Languages | Prices | Go/no-go gate |
|---|---|---|---|---|---|---|
| MVP (closed alpha) | 2027-02-15 → 2027-03-05 (M2) | Team + 30 invited testers | iOS + Android dev builds | en-US | none | M2 exit criteria (§14.2) |
| Beta (closed) | 2027-03-08 → 2027-05-14 (M4) | US only: 500 testers (400 iOS TestFlight, 100 Android Play closed testing), ≥150 of them GLP-1 users | iOS + Android | en-US | Sandbox purchases; testers get Premium+ free for 6 months | M3, M4 |
| **V1.0** | **2027-06-01** | **US** | **iOS** | en-US | USD | M4 release gates passed; App Review approved |
| V1.1 | 2027-07-13 | US | Android | en-US | USD | KPI-01–KPI-04 met on the Android device matrix |
| V1.2 | 2027-08-24 | UK (plus US feature update) | iOS + Android | en-GB | GBP incl. VAT | UK qualification memo, DPIA, UK GDPR/DUAA complaints procedure (§11.6) |
| V1.3 | 2027-10-05 | India | Android + iOS | en-IN, hi-IN | INR incl. GST | D-08 (economics) and DPDP readiness (duties apply from 2027-05-13) [R4 #53](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/) |
| V1.4 | 2027-11-16 | All live markets (IF-6 US-only) | iOS + Android | as above | — | D-09 for IF-6 |
| V2.0 | 2028-03-28 | EU entry (D-15; default Ireland + Germany) and US Spanish | iOS + Android | en-IE, de-DE, es-US | EUR | EU qualification memo, DPIA, AI Act Art. 50 notices, withdrawal button [R4 §8] |

Rationale: US first because the wellness path is clearest and conversion is highest (NA trial→paid 34.2% vs 15.2% in India/SE Asia) [R4 recommendations], [R5 #56](https://www.revenuecat.com/state-of-subscription-apps). iOS first at V1.0 to concentrate accuracy validation on a smaller device matrix; Android follows six weeks later from the same codebase. India is third because it only works economically with tight quotas plus an eval-approved cheaper model or B2B revenue (§13.4) [R5 §10.3].

### 3.2 Languages

| Language | Release | Scope |
|---|---|---|
| en-US | MVP | Everything |
| en-GB | V1.2 | Spelling, units, UK crisis resources, CAP-compliant copy |
| en-IN, hi-IN | V1.3 | UI, voice cues (expo-speech device voices) and food names in Hindi. Hindi coach chat ships only if the Hindi run of the safety eval (KPI-07, KPI-08) passes; otherwise Hindi UI with English chat. |
| es-US, de-DE | V2 | Full product incl. safety eval in each language |

### 3.3 Platform minimums and build targets

| Item | Decision | Basis |
|---|---|---|
| iOS minimum | **iOS 17.0** (iPhone XR/XS and newer) | Expo SDK 58 floor is iOS 16.4 [R2 #73](https://docs.expo.dev/versions/latest/); we raise it to 17.0 so Apple Vision 3D `bodyHeight` calibration is always available [R2 #21](https://developer.apple.com/documentation/vision/humanbodypose3dobservation) |
| Android minimum | **Android 9 (API 28)** | SDK 58 and MediaPipe allow API 24 [R2 #9]; we raise it to 28 for Health Connect availability and a usable CV performance floor (verify Health Connect floor at M1) |
| Android target/compile SDK | targetSdk **36**, compileSdk **37** | Play requires API 36 (extension to 2026-11-01) [R4 #83](https://support.google.com/googleplay/android-developer/answer/11926878); SDK 58 uses compileSdk 37 [R2 #73] |
| Toolchain | Xcode 26.4+, Node 22.13.x, AGP 9 / Kotlin 2.0+ | [R2 §4.4] |
| Form factor | Phones only at V1.0 (no tablet, watch or TV apps) | Scope |
| Store accounts | Apple and Google **organisation** accounts (health apps must be submitted by a legal entity, Apple 5.1.1(ix)); Apple Small Business Program (15%) [R5 #69](https://developer.apple.com/app-store/small-business-program/); 18+ age rating | [R4 §4] |

### 3.4 Reference test devices (device lab, 9 phones)

| Tier | iOS | Android | Gate (KPI-04) |
|---|---|---|---|
| A (high) | Current-generation iPhone on iOS 27 | Samsung Galaxy S26 (S24–S26 class) | ≥30 FPS sustained, Full model |
| B (mid) | iPhone 11 and iPhone SE (2nd gen) on iOS 27 (the oldest iOS 27 devices) [R2 #22](https://www.apple.com/ios/) | Galaxy S21; one Snapdragon 7 Gen 4 phone chosen at M1 from the Qualcomm AI Hub list [R2 #37](https://aihub.qualcomm.com/models/mediapipe_pose) | ≥20 FPS sustained |
| C (floor) | iPhone XR on iOS 17/18 | An Android 9–10 phone with a Mali GPU (2019–2020 mid-range) | ≥15 FPS with Lite, else counting-only mode |
| Cross-check | — | Pixel 5 (has published MediaPipe/MoveNet numbers) [R2 #24] | Harness sanity check |

---

## 4. Personas

| ID | Persona | Segment | Tier | Top jobs to be done | Top pains | Device | Success signal |
|---|---|---|---|---|---|---|---|
| P1 | **Jordan**, 44, Columbus OH (US) | GLP-1 strength keeper (launch segment) | Premium+ annual | Keep strength while losing weight; fit training around the weekly dose; hit protein without obsessing | Stairs and carrying feel harder; nausea the day after the dose; generic plans ignore the dose cycle | iPhone 15, adjustable dumbbells 2–20 kg | ≥2 camera-verified strength sessions/week; chair-stand and push-up benchmarks stable or rising |
| P2 | **Sam**, 57, Phoenix AZ (US) | Everyday-medicines lifter | Premium annual | Get stronger after a sedentary decade without feeling unsafe | Watch HR zones make no sense on a beta-blocker; worries about lows on glipizide; desert heat; statin muscle aches vs normal soreness | iPhone 12, Apple Watch | Trains 3×/week in RPE mode; uses heat alerts; zero unhandled red flags |
| P3 | **Riley**, 29, Chicago IL (US) | Solo lifter (home + gym) | Free → Premium | Trustworthy form feedback without a trainer; progress that counts good reps | Camera apps that miss reps; no PT budget; refuses video uploads | Pixel 9 / iPhone 16, gym access | Quality-volume PRs; ≥95% of sets counted exactly |
| P4 | **Kiran**, 36, Bengaluru (India) | India GLP-1 / value user | Free → Premium (₹) or partner code | Structured strength + Indian-food protein targets while on generic semaglutide | Price-sensitive (₹99–₹449/mo anchors); Hindi/English mix; mid-range Android | Snapdragon 7-class Android | Weekly sessions with Hindi cues; protein target met 4+ days/week |
| P5 | **Morgan**, 41, New Jersey (US) | Partner clinician (DPT running a 6-practitioner clinic) | B2B (V1.x pilot → V2) | Verified home-exercise adherence; simple guardrails for patients moving into the gym | No time for another dashboard; HIPAA exposure; unverified patient self-reports | Desktop web + iPad | Uses share reports with ≥10 patients; renews after pilot |

- **P1 Jordan** has used a weekly GLP-1 injection for seven months and lost 14 kg. They train at home in 30–40 minutes and want proof that they are keeping strength, not just losing weight. Their dose-day+1 fatigue drives IF-3's dose-cycle scheduling. They pay for Premium+ because of the GLP-1 Strength Track and the clinician report.
- **P2 Sam** takes metoprolol, atorvastatin and glipizide. Heart-rate zones never fit them, so IF-1 switches them to RPE and talk-test intensity, adds glucose check-ins without numeric thresholds, statin muscle-symptom check-ins and heat alerts. They need large text and audio cues (WCAG 2.2 AA).
- **P3 Riley** is the free-tier growth engine: on-device form checks for five exercises, then Premium for the full library, autoregulation and quality volume. They will churn if reps are missed or if video ever leaves the phone.
- **P4 Kiran** is on a generic semaglutide costing ₹1,290–₹4,200/month [R5 #22](https://www.outlookbusiness.com/corporate/sun-pharma-dr-reddys-glenmark-launch-generic-semaglutide-injection-in-india). India's chatbot gives no medication counselling [R4 #22], so medication context appears as fixed plan cards. Kiran may arrive through a clinic or pharmacy partner code (F-123).
- **P5 Morgan** benchmarks software against Physitrack ($18.99/practitioner/month plus $8 per remotely monitored patient) [R5 #67](https://www.physitrack.com/physitrack-pricing). They need consented, non-diagnostic reports at V1.2 and a portal with guardrails only at V2, after a HIPAA-ready tenant exists.

---

## 5. Feature catalog

MoSCoW applies to the release named in the row. Effort: S ≤1 engineer-week, M 2–3, L 4–6, XL >6. 69 features.

| ID | Name | One-line description | MoSCoW | Release | Effort | IF | Dependencies |
|---|---|---|---|---|---|---|---|
| **Onboarding & profile** | | | | | | | |
| F-001 | Account & sign-in | Sign in with Apple, Google or email one-time code (Amazon Cognito); created only after the F-002 age gate passes | Must | MVP | M | — | F-002 |
| F-002 | Age gate & region | Neutral date-of-birth gate shown before account creation (18+; under-18 blocked with resources and no account created); market from store country | Must | MVP | S | IF-1 | — |
| F-003 | Goals & equipment profile | Goals, experience, schedule, home/gym, available dumbbell weights | Must | MVP | S | — | F-001 |
| F-004 | Pre-participation screening | ACSM-based questions (activity, symptoms, known cardiovascular/metabolic/renal conditions); clearance gate before vigorous plans [R3 #17] | Must | MVP | M | IF-1 | F-110, clinical sign-off |
| F-005 | Locale & units | Metric storage, locale display (§0.3); en-US at MVP, en-GB V1.2, en-IN/hi-IN V1.3 | Must | MVP | S | — | — |
| **Health & medication profile** | | | | | | | |
| F-010 | Medication list | RxNorm search (RxCUI → RxClass) and manual entry; "uncovered medicine" card; HealthKit Medications import (iOS 26+) added at V1.x [R6 #18] | Must | MVP | M | IF-1 | RxNav-in-a-Box, F-110 |
| F-011 | Medication constraint engine | Deterministic, versioned, clinician-owned rules per class (6 classes MVP, 15 at V1.0; §9.5), incl. RPE mode for beta-blockers | Must | MVP | XL | IF-1 | F-010, F-110, clinical sign-off |
| F-012 | Dose schedule & side-effect log | User-entered schedule (weekly injectable or daily pill), side-effect and energy check-ins, user-configured reminders; non-prescriptive | Must | MVP | M | IF-3 | F-010, F-080 |
| F-013 | Safety gates & red-flag check-ins | Pregnancy / new medicine / new diagnosis gate; Emergency, Urgent, Crisis templates with regional numbers (§9.6) | Must | MVP | M | IF-1 | F-054, F-103 |
| F-014 | Heat-risk alerts | Heat-index warnings for heat-sensitive classes using Apple WeatherKit and coarse location (opt-in) | Should | V1.0 | M | IF-1 | F-011, F-100 |
| F-015 | Supplement & pre-workout check | Label photo → FDA "never recommend" ingredient list, 400 mg/day caffeine counter, stimulant-stack warning vs ADHD stimulants and beta-blockers [R3 #52] | Could | V1.x | M | IF-1 | F-061, F-011 |
| **Camera form coach** | | | | | | | |
| F-020 | PoseEngine native module | Swift/Kotlin Nitro module around MediaPipe Pose Landmarker (Full; Lite fallback), Apple Vision fallback, face landmarks 0–10 dropped natively, thermal governor | Must | MVP | XL | — | — |
| F-021 | Setup Coach & personal baseline | Enforces 2–4 m, required view, full-body framing, lighting and clothing tip; three slow reference reps set the user's ROM baseline; optional height | Must | MVP | M | IF-2 | F-020 |
| F-022 | Exercise-rules engine | Declarative, versioned `ExerciseDefinition` JSON (view, joints, phases with hysteresis, rules, cue copy, maturity) shipped as signed remote config | Must | MVP | L | — | F-020, F-111 |
| F-023 | Rep counting & per-rep metrics | Reps, ROM, tempo, concentric velocity estimate and confidence for EX-01–EX-10 (§7) | Must | MVP | L | IF-2 | F-022 |
| F-024 | Real-time form cues | ≤1 corrective cue per rep at rep boundaries; audio + haptic + caption; GA/beta maturity; confidence gate; "form not assessed" + re-position prompt | Must | MVP | L | IF-2 | F-023, F-112 |
| F-025 | Autoregulation prompt | Velocity loss + form drift → "end set?" prompt and next-set suggestion; user confirms or overrides | Must | MVP | L | IF-2 | F-023 |
| F-026 | Voice logging | On-device speech-to-text for RPE, reps in reserve and discomfort; audio never stored | Should | Beta | M | IF-2, IF-6 | F-023 |
| F-027 | Replay & shareable clip | On-device keypoint replay with timestamped errors; a user-chosen clip can be shared (per-clip consent, on-device face blur, encrypted, 30-day default retention) | Should | V1.x | L | IF-5 | F-023, F-100, F-101 |
| F-028 | Barbell recorded-set analysis | On-device post-set analysis for back squat, deadlift, bench press (bar occludes keypoints, so not real-time) [R1 rec. 2] | Could | V1.x | L | — | F-022 |
| F-029 | Learned CV models | PoseRAC-style counter and GCN error classifiers trained only on our data, run via LiteRT 2.3.0 [R2 §5.1] | Could | V2 | XL | IF-2 | F-113 |
| **Workouts & programs** | | | | | | | |
| F-040 | Program planner | Deterministic planner respecting equipment, schedule and constraint set; every plan change is a validated proposal | Must | MVP | L | IF-1, IF-4 | F-011, F-022 |
| F-041 | Starter programs | Foundations (Free), Home Dumbbell Strength, Gym Basics | Must | MVP | M | — | F-040 |
| F-042 | GLP-1 Strength Track | 3 sessions/week beginner-scaled resistance program with progression and protein emphasis [R3 #13] | Must | MVP | L | IF-3 | F-040, F-062 |
| F-043 | Dose-cycle-aware scheduling | Energy/side-effect check-ins → suggested placement of the hardest session; deload suggestion on logged side-effect days; user confirms | Must | Beta | M | IF-3 | F-012, F-040 |
| F-044 | Workout player & swaps | Timers, rest, manual logging for non-camera moves, equipment-busy substitutes from a clinician-reviewed swap table [R1 complaints] | Must | MVP | M | — | F-040 |
| F-045 | Comfort-range training | Discomfort check-in (body map, 0–10), swaps, user- or physio-set ROM caps enforced by the camera; wellness copy only | Should | V1.x | L | IF-6 | F-024, F-026, D-09 |
| **AI coach chat** | | | | | | | |
| F-050 | Coach chat | `claude-opus-5-5` via backend proxy, SSE streaming, session-start AI notice, persistent "AI coach" label, in-chat report button [R4 #81] | Must | MVP | L | IF-4 | F-054, F-100 |
| F-051 | Grounding tools | Strict read tools and propose-only write tools (§9.3) | Must | MVP | L | IF-4 | F-050 |
| F-052 | "Why this changed" cards | Every plan change cites measured data or a named rule | Must | MVP | M | IF-4 | F-040, F-051 |
| F-053 | Post-workout debrief | Narrates structured set metrics (never video); LLM for paid tiers, template for Free | Must | MVP | M | IF-4, IF-2 | F-023 |
| F-054 | Safety guard | Deterministic pre/post rules + classifier; refusal templates; regional crisis routing; `refusal` stop-reason handling | Must | MVP | L | IF-1 | F-110, F-114 |
| F-055 | Knowledge-base cards | Clinician-approved, versioned cards with source citations, rendered verbatim | Must | MVP | L | IF-1 | F-110 |
| F-056 | Coach memory | User-visible, editable, deletable memory; separate opt-in for health memories [R3 §5] | Should | Beta | M | IF-4 | F-100 |
| F-057 | Eating-disorder-safe mode | Hides calories, weight, BMI and deficits; triggered by opt-in, screener or chat signals [R3 §4.3] | Must | MVP | M | IF-1 | F-054, F-060 |
| **Nutrition** | | | | | | | |
| F-060 | Food log | Search (USDA FDC, fatsecret), barcode (Open Food Facts), manual; daily protein and fibre view | Must | MVP | M | — | D-10 |
| F-061 | Meal-photo logging | Claude vision → structured estimate the user confirms; photo deleted server-side after parsing | Must | MVP | M | IF-4 | F-050, F-092 |
| F-062 | Protein, fibre & intake-floor rules | Clinician formula; kcal-floor flags (1,200 kcal/day women, 1,800 men [R3 §2]); loss-rate cap 0.9 kg/week; GI-friendly suggestions on side-effect days | Must | MVP | M | IF-1, IF-3 | F-011, F-060 |
| F-063 | Indian food database | IFCT 2017 (with NIN permission) and Hindi food names [R3 #63] | Must | V1.x | M | — | D-08 |
| F-064 | Session-linked fuelling summary | Links meals to the camera-measured session and the medication schedule [R6 C14] | Could | V1.x | M | IF-4 | F-061, F-012 |
| **Progress & insights** | | | | | | | |
| F-070 | History & weekly insights | Session history, per-rep metrics, deterministic charts; LLM narration for paid tiers | Must | MVP | M | IF-4 | F-023 |
| F-071 | Quality-volume ledger | Total vs quality volume side by side; PRs count quality reps; reps never silently dropped [R6 C16] | Must | Beta | M | IF-2 | F-024 |
| F-072 | Camera strength benchmarks | Monthly 30-s chair stand, max quality push-ups, quality plank hold, squat-depth check-in [R6 #87] | Must | V1.0 | M | IF-3 | F-023 |
| F-073 | Health-platform sync | HealthKit / Health Connect read of weight, HR, sleep, steps, workouts; daily summaries only | Should | Beta | M | — | F-100 |
| F-074 | Clinician-shareable report | User-initiated PDF or 14-day expiring link: adherence, quality volume, benchmarks, ROM trends, user-entered medication context | Should | V1.x | M | IF-5 | F-070, F-072 |
| F-075 | Movement–discomfort journal | Deterministic co-occurrence of discomfort logs with camera-measured patterns; non-diagnostic copy | Could | V1.x | M | IF-6 | F-045 |
| F-076 | Personal cue learning | Bandit over approved cue variants per user × fault, scored on the next reps [R6 W3] | Could | V1.x | M | IF-7 | F-024 |
| **Notifications** | | | | | | | |
| F-080 | Reminders | Workout, user-configured dose and check-in reminders; generic payload text; preferences and quiet hours | Must | MVP | S | IF-3 | F-012 |
| F-081 | Lifecycle & proactive check-ins | Day 4–7 progress prompt, missed-session nudge, dose-day check-in, weekly review | Should | Beta | S | IF-3, IF-4 | F-080 |
| **Subscription & paywall** | | | | | | | |
| F-090 | Entitlements | RevenueCat entitlements for Free/Premium/Premium+ across App Store and Play Billing | Must | MVP | M | — | F-001 |
| F-091 | Onboarding soft paywall | Annual-led paywall inside onboarding, 7-day trial on annual plans, per-storefront prices and experiments via remote offerings [R5 §4] | Must | Beta | M | — | F-090 |
| F-092 | Quotas & fair-use metering | Per-tier coach-message and meal-scan budgets (§9.7); safety flows never metered | Must | MVP | M | — | F-090 |
| F-093 | Subscription compliance | ROSCA/CA ARL consent records, annual reminder, click-to-cancel guidance; RBI pre-debit (India); EU withdrawal button at V2 [R4 §5] | Must | V1.0 | M | — | F-090 |
| F-094 | US web checkout | Stripe Billing + RevenueCat Web link-out under Apple 3.1.1(a) [R5 #71] | Could | V1.x | M | — | D-13 |
| **Privacy & consent** | | | | | | | |
| F-100 | Consent center | Purpose-based consents incl. AI processing before first chat (Apple 5.1.2(i)); records; one-tap withdrawal (§11.3) | Must | MVP | M | — | — |
| F-101 | On-device video guarantee | No frame persistence; face landmarks dropped in native code; encrypted local DB; health store excluded from iCloud backup | Must | MVP | M | — | F-020 |
| F-102 | Deletion & export | In-app and web account deletion; machine-readable export | Must | MVP | M | — | F-001 |
| F-103 | Regional policy engine | Per-market feature flags (e.g., India: no medication counselling in chat; UK/EU medication features only after memo) | Must | V1.0 | M | IF-1 | F-002 |
| F-104 | Training-data contribution | Opt-in upload of keypoint series without face points; revocable; removed from future training sets [R2 §3.2] | Should | Beta | M | — | F-100, F-113 |
| **Admin & content tooling** | | | | | | | |
| F-110 | Clinical KB & rules CMS | Author → clinical review → eval → publish; `review_due`; tickets on DailyMed/openFDA label changes [R3 §5] | Must | MVP | L | IF-1 | — |
| F-111 | Exercise-definition editor | Edit thresholds and cue copy; signed bundles; staged rollout 5% → 25% → 100% | Must | MVP | M | — | F-022, F-112 |
| F-112 | Golden-video harness | Python mediapipe 1.1.1 replay of recorded clips through the same JSON definitions; CI fails on regressions; device-lab FPS/latency/thermal jobs | Must | MVP | L | — | — |
| F-113 | Labelling pipeline | BlazePose Heavy pre-labels; two certified coaches + adjudicator; inter-rater agreement tracking | Must | MVP | L | — | — |
| F-114 | Safety eval harness & claims linter | Red-team set, Opus judge, clinician review; banned-claims string linter; CI merge gate | Must | MVP | L | IF-1 | F-110 |
| F-115 | Ops console | AI cost per user/route dashboard, safety-event review queue, support tools | Must | Beta | M | — | F-054, F-092 |
| **B2B & clinician** | | | | | | | |
| F-120 | Clinic design-partner pilot | 3 US clinics use share reports; manual onboarding; no PHI exchange | Should | V1.x | S | IF-5 | F-074 |
| F-121 | Clinician portal | Patient invites (consented), adherence, flagged clips; separate HIPAA-ready tenant and BAAs | Could | V2 | XL | IF-5 | F-074, F-027 |
| F-122 | Clinician-set guardrails | RPE/HR ceilings, ROM caps, banned movements and cautions set by the clinician and enforced by the app | Could | V2 | L | IF-5 | F-121, F-011 |
| F-123 | Partner licensing | Activation codes and bulk entitlements for GLP-1 telehealth, pharma patient-support programs, Indian clinics/pharmacies; no PHI exchange | Could | V1.x | M | IF-3 | F-090 |

**Release roll-up:** MVP 41 · Beta 9 · V1.0 4 · V1.x 12 · V2 3 (total 69). V1.x placement: V1.2 = F-027, F-074, F-094, F-120; V1.3 = F-063, F-123; V1.4 = F-015, F-028, F-045, F-064, F-075, F-076; HealthKit import inside F-010 ships at V1.4.

---

## 6. Innovative features (IF-1..IF-7)

**Selection.** R6's four bundles were tested against R1 (white space), R4 (regulatory boundary) and R5 (willingness to pay). Bundles (a), (b) and (d) are kept. Bundle (c) is kept but reframed and gated, because pain-driven programmes for a condition are devices/MDSW [R4 §1.3]. Two features are added: the grounded coach (R1's W1, the core of the closed loop) and personal cue learning (R6 W3, low regulatory risk, data moat). Bundle (a)'s clinician-set guardrails (W2) move into IF-5 because they need a clinician portal and a HIPAA-ready tenant.

**Considered and not headlined** [R6 §2]: equipment scanning (C4, crowded), camera rep duels (C5, crowded, contest law), camera readiness score (C7, unvalidated), voice coach (C8, the interface, not a moat), camera spotter (C9, liability; rely on watch fall detection), ghost overlay (C10, only as replay in F-027), cycle-aware training (C13, mainstream insights), on-device video (C15, table stakes), multi-person tracking (C17), return-to-training clearance (C18, high regulatory risk).

### IF-1 Medication-aware Safety & Context Layer (C1 + R1 W4)

| Field | Decision |
|---|---|
| Members | F-002, F-004, F-010, F-011, F-013, F-014, F-015, F-054, F-055, F-057, F-062, F-103, F-110, F-114 |
| What it does | The user lists medicines (RxNorm search or manual). RxCUI → RxClass → a clinician-owned **constraint set** that changes the training plan, never the medicine: beta-blockers switch intensity to RPE/talk test; SGLT2 inhibitors block keto/fasting templates; anticoagulants remove contact and high-fall-risk drills; fluoroquinolones turn on tendon-protect mode; GLP-1/GIP turns on lean-mass programming and protein rules; insulin/secretagogues add pre- and post-session check-ins (no numeric thresholds). Red-flag check-ins route to fixed templates. Every constraint shows a KB card with sources and "last reviewed" (§9.5). |
| Novelty + evidence | **NOVEL as a whole** (Medium). No product changes exercise choice, intensity measure, timing or safety prompts from a medication list [R6 C1]; Apple only corrects its VO2 max estimate [R1 S71](https://support.apple.com/en-us/HT211856); Visible and SmartGym leave HR-zone resets to the user [R6 #27](https://help.makevisible.com/en/articles/10632785-using-visible-with-medications-that-impact-heart-rate); no consumer app has class rules for insulin, statins or anticoagulants [R1 §3.3]. Medication data access is solved (HealthKit Medications API, RxNorm-coded) [R6 #18]. |
| Priority / release | P0. MVP 6 classes → V1.0 all 15 classes + heat alerts → V1.4 supplement check and HealthKit import |
| Primary KPI | KPI-07 (never-rule failures = 0) and KPI-08 (red-flag recall ≥0.98) |
| Safe-claims wording | "Your plan respects the medicines you list, using exercise-safety rules reviewed by pharmacists and physicians. RepSight never changes your medicines — check with your clinician." Never: "adjusts your treatment", "safe to train on X", any dose language. |
| Regulatory guardrail | Fixed, clinician-authored rules (AUP fixed-rule exclusion) [R3 #1](https://www.anthropic.com/aup); user-configured reminders and patient drug information sit under FDA enforcement discretion [R4 #6](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion); India shows constraints as plan cards only, never chat counselling; UK/EU only after the qualification memo (F-103). |

### IF-2 Rep-Quality Autoregulation (C2 + C16)

| Field | Decision |
|---|---|
| Members | F-021, F-023, F-024, F-025, F-026, F-071, F-029 |
| What it does | Per rep, the camera estimates concentric velocity (tracked landmark displacement ÷ time, scaled by body height) and checks form. When velocity loss versus the best of reps 1–2 reaches the threshold (default 30%, user-adjustable 10–40%) **or** form drifts (a GA error absent in reps 1–2 appears on 2 consecutive reps, or ROM falls >15% below rep 1), the app asks "end the set?" and proposes the next set's load/reps; the user confirms or overrides. Voice RPE and reps-in-reserve refine the suggestion. The **quality-volume ledger** shows total volume next to quality volume (assessed reps with no GA error) and awards PRs only on quality reps; no rep is ever silently dropped. |
| Novelty + evidence | **NICHE parts, NOVEL combination** (Medium-High). Metric alerts at a user-set 5–45% velocity loss but gives no next-set prescription or form analysis [R6 #32](https://www.metric.coach/articles/introducing-real-time-feedback); SetSync and RepSpeed are post-hoc [R6 #34, #35]; Peloton IQ and Tonal need hardware; FitDuel scores "only clean reps" in duels and Rep-IQ scores reps (waitlist) [R6 #55, #89]. No phone product combines these [R6 C2, C16]. |
| Priority / release | P0. MVP prompt + suggestion → Beta voice RPE/RIR and quality volume → V2 learned models |
| Primary KPI | KPI-20 (stop-prompt acceptance ≥60% at V1.0+90 days), guarded by KPI-02 |
| Safe-claims wording | "Estimates when your reps slow down or your form changes, and suggests when to end the set." All numbers labelled estimates; a single-camera VBT app showed only poor-to-moderate agreement with a lab system [R6 #33](https://peerj.com/articles/17789). Never: "measures bar speed precisely", "prevents overtraining or injury". |

### IF-3 GLP-1 Strength Track (C12 + W4 + R1 W2/W3)

| Field | Decision |
|---|---|
| Members | F-012, F-042, F-043, F-062, F-072, F-080, F-081, F-123 |
| What it does | Three camera-coached resistance sessions a week, beginner-scaled. **Dose-cycle scheduling** for weekly injectables: energy and side-effect check-ins on days 0–3 after the dose suggest where the hardest session goes; logged side-effect days get a deload suggestion; the user confirms. Daily pills (Wegovy pill, Foundayo) use side-effect logs only [R3 #43, #44]. **Protein** from the clinician formula (1.2–1.6 g/kg/day of adjusted weight, capped at 80–120 g/day; never below 0.4–0.5 g/kg; no targets for users reporting kidney disease, who are referred to a dietitian) plus fibre and small-meal suggestions on GI-symptom days [R3 #13](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/). **Monthly camera benchmarks**: 30-s chair stand (EX-08), max quality push-ups (EX-03), quality plank hold (EX-09), squat-depth check-in (EX-01), shown as a "strength kept" trend. |
| Evidence | STEP 1: 38% of a 13.6 kg loss was lean mass; the 2025 joint advisory recommends strength training ≥3×/week and 1.2–1.6 g/kg/day protein [R3 #13]. 11% of US adults use a GLP-1 for weight loss (Gallup, 2026) [R5 #18](https://news.gallup.com/poll/712157/glp-usage-reaches-new-high.aspx). |
| Novelty | **MAINSTREAM category, NOVEL verification.** GLP-1 companions are common (MyFitnessPal, Oura, Noom, WW) [R6 C12], but none checks training by camera [R1 W2]; Oura sees the post-dose readiness dip yet does not change workouts [R1 S63](https://ouraring.com/blog/glp-1-insights/). Camera functional tests in consumer fitness were not found (R6 W4, not specifically searched). |
| Priority / release | P0 (launch wedge, sold in Premium+). MVP track + protein + logs → Beta dose-cycle scheduling → V1.0 benchmarks → V1.3 partner licensing |
| Primary KPI | KPI-19 (strength-dose adherence ≥50% at V1.0+90 days) |
| Safe-claims wording | "Helps you keep strength while you lose weight." "Built for people using GLP-1 medicines" only after D-16 counsel review. Benchmarks are "strength benchmarks", never fall-risk tests. Never: "prevents GLP-1 muscle loss", "protects muscle", "treats muscle atrophy" [R6 #21]. |

### IF-4 Grounded Closed-Loop Coach (R1 W1)

| Field | Decision |
|---|---|
| Members | F-040, F-050, F-051, F-052, F-053, F-056, F-061, F-064, F-070, F-081 |
| What it does | The coach reads structured per-set metrics (reps, ROM, tempo, velocity loss, error codes with confidence), food logs, the constraint set and wearable summaries through strict tools (§9.3). It proposes plan changes that the rules validator checks and the user confirms; each change shows a "Why this changed" card ("Velocity fell 34% by rep 7 and depth dropped 12%, so next session keeps the load"). Debriefs narrate metrics only; video never reaches the LLM [R2 #44](https://arxiv.org/abs/2407.08101). |
| Novelty + evidence | **Combination NOVEL** (Medium-High): no AI coach sees rep-level camera data [R1 §2]; Zing has camera + chat but no nutrition or medicines [R1 S17]; MyFitnessPal and Oura have chat + nutrition + GLP-1 but no workout verification [R1 S77, S63]; Peloton has a camera but no chat [R1 S2]. Generic health chat is a commodity [R1 S100, S102]. |
| Priority / release | P0. MVP (memory at Beta, fuelling summary at V1.4) |
| Primary KPI | KPI-25 (100% of plan changes explained) and KPI-09 (100% of medication answers grounded) |
| Safe-claims wording | "An AI coach that uses your measured workouts, food log and the context you share." Never: "as good as a human trainer", "AI doctor/dietitian". |

### IF-5 Clinician Share & Guardrails (W2 + C11)

| Field | Decision |
|---|---|
| Members | F-027, F-074, F-120, F-121, F-122 |
| What it does | **V1.2:** a user-initiated report (PDF or 14-day expiring link) with adherence, quality volume, benchmark and ROM trends, user-entered medication context and a side-effect summary, with no interpretation; optional per-clip sharing; 3 US design-partner clinics. **V2:** a clinician portal where the patient's clinician (with patient consent) sets guardrails (RPE or HR ceilings the clinician supplies, ROM caps, banned movements, cautions) that the planner and camera enforce, and sees adherence and flagged clips, in a separate HIPAA-ready tenant. |
| Novelty + evidence | **NICHE in rehab B2B, NOVEL for general strength** [R6 W2, C11]: Kemtai, Sword and Hinge have clinician views for MSK care [R6 #66, #39]; no consumer app auto-selects worst-rep clips for a coach or physio [R6 C11]. FDA's CDS guidance gives enforcement discretion to some HCP-facing software [R6 #23]; the portal displays data and never recommends treatment. |
| Priority / release | P1. V1.x (V1.2 report + pilot) → V2 (portal and guardrails) |
| Primary KPI | KPI-26 (≥10% of Premium+ users share a report within 90 days; ≥3 design-partner clinics signed by V1.2 (M7) and still active at V1.4) |
| Safe-claims wording | "Share your training data with your clinician." Never: "remote patient monitoring", "clinically validated", "billable" before V2 legal review. |

### IF-6 Comfort-Range Training (C6 + W1, reframed)

| Field | Decision |
|---|---|
| Members | F-026, F-045, F-075 |
| What it does | Discomfort check-ins (body map, 0–10) before and after sessions; swaps from a clinician-reviewed table; ROM caps set by the user or their physio (never inferred by the app) and enforced by camera cues ("stop at this depth"); a deterministic **movement–discomfort journal** that shows co-occurrence only ("discomfort was logged after 3 of 4 sessions where knee travel grew late in the set — you may want to discuss this with a professional"). Red flags route to templates; the LLM never interprets symptoms [R3 #1]. |
| Novelty + evidence | Injury-based swaps are **MAINSTREAM** (Fitbod Injuries/Limitations, Fitbit coach) [R6 #58, #11]; a camera-enforced ROM cap plus a discomfort journal and physio report was not found [R6 C6, W1, Medium]. Injurymap's approval as a medical device in Denmark shows that pain-driven adaptation pulls products toward device status [R6 #62](https://ds-sundhed.dk/en/injurymap/). |
| Priority / release | P1, gated. V1.4, US only, after D-09 counsel memo; UK/EU/India only after a qualification-memo update |
| Primary KPI | KPI-27 (≥70% of users who log discomfort complete a modified session within 7 days) |
| Safe-claims wording | "Train around discomfort; tell your physio if it persists." Never: "pain relief", "rehab", "treats knee pain", "predicts injury". |

### IF-7 Personal Cue Learning (W3)

| Field | Decision |
|---|---|
| Members | F-076 |
| What it does | For each recurring fault, the cue scheduler rotates 2–4 coach-written, reviewed cue variants (internal vs external focus, analogy, short vs detailed) [R6 #88](https://doi.org/10.1080/1750984X.2012.723728), scores whether the fault recurs in the next 3 assessed reps, and converges per user with a Thompson-sampling bandit, still at ≤1 corrective cue per rep. |
| Novelty + evidence | **NOVEL** (not specifically searched; Low-Medium) [R6 W3]; CoachAI only lets users pick cue frequency [R6 #68]. Low regulatory risk; builds a per-user data moat. |
| Priority / release | P2. V1.x (V1.4) |
| Primary KPI | KPI-28 (median reps-to-correction ≥20% lower than a fixed-cue control) |
| Safe-claims wording | "Learns which cues work best for you." Never: "AI physio". |

---

## 7. MVP exercise library

**Rules that apply to every exercise** [R2 §2.3–2.4]:
- Each exercise declares its required view. From the wrong view the app still counts reps and gives view-independent cues, plus a prompt to re-position.
- Reps are counted by a per-exercise state machine with separate enter/exit thresholds (hysteresis) [R2 #4].
- A cue may fire only if every joint it uses clears the visibility threshold (start 0.5; tune in M2) in ≥80% of the rep's frames; otherwise the rep is counted and marked "form not assessed".
- Thresholds are **relative to the user's baseline** (three slow reference reps, F-021) because MediaPipe under-reads knee flexion by −13.9 ± 15.1° against an IMU, with smaller error in side view [R2 #60](https://iris.uniecampus.it/handle/11389/91575). Absolute angles are never shown as clinical measurements.
- **GA** cues speak a correction; **Beta** cues show a labelled soft tip and are never a verdict. All frontal-plane (valgus-type) cues are Beta at MVP: the best in-the-wild knees-inward detector reached F1 0.53 [R2 #40](https://arxiv.org/abs/2202.14019) and MediaPipe valgus lacked concurrent validity against 3D mocap [R2 #63](https://doaj.org/article/2d283f6411874c82988f54dd2e60829f).
- Velocity loss (IF-2) applies to every rep-based exercise except EX-09; default stop-prompt threshold 30%, calibrated in M3.
- No spinal-rounding cue at MVP: single-camera body keypoints contain no spine points.

### 7.1 Exercises

| EX | Exercise | Equipment | Required camera view | Rep metric | Free tier | Velocity landmark |
|---|---|---|---|---|---|---|
| EX-01 | Squat (bodyweight or goblet) | None or 1 dumbbell | Side (front for the Beta valgus tip) | Reps; knee/hip flexion ROM; tempo | Yes | Hip midpoint |
| EX-02 | Dumbbell Romanian deadlift | 1–2 dumbbells | Side | Reps; hip-hinge ROM; tempo | No | Hip midpoint |
| EX-03 | Push-up (standard, knee or incline) | None; bench/table for incline | Side | Reps; elbow ROM; body-line angle | Yes | Shoulder midpoint |
| EX-04 | Reverse lunge / split squat | None or 2 dumbbells | Side (front for the Beta tip) | Reps per side; front-knee ROM | No | Hip midpoint |
| EX-05 | One-arm dumbbell row, bench-supported | 1 dumbbell + bench or chair | Side, working arm nearest the camera | Reps per side; shoulder/elbow ROM | No | Working wrist |
| EX-06 | Standing dumbbell overhead press | 2 dumbbells | Side | Reps; elbow extension at top; trunk angle | No | Wrist midpoint |
| EX-07 | Glute bridge | Mat (dumbbell optional) | Side | Reps; hip extension; top-hold time | Yes | Hip midpoint |
| EX-08 | Sit-to-stand (chair stand) | Straight-backed chair, seat ~43 cm (STEADI protocol) | Side | Reps; full-stand flag; 30-s benchmark count | Yes | Hip midpoint |
| EX-09 | Forearm plank | Mat | Side | "Quality seconds" (timer pauses after >2 s outside tolerance) | Yes | — |
| EX-10 | Dumbbell biceps curl | 1–2 dumbbells | Side | Reps (per side if alternating); elbow ROM | No | Wrist |

### 7.2 Form errors detected at MVP (26 errors: 20 GA, 6 Beta)

| ERR code | Definition | Threshold | Maturity |
|---|---|---|---|
| ERR-EX01-01 | Depth short: peak knee flexion below baseline, or hip crease stays above the top of the knee (IPF-style standard used by SquatEye [R1 S27]) | <90% of baseline knee flexion; calibrate in M3 | GA |
| ERR-EX01-02 | Excessive forward lean at the bottom | Trunk-to-vertical > baseline + 15° (start value); calibrate in M3 | GA |
| ERR-EX01-03 | Heels lift during the descent | Heel landmark rise > height-scaled 2 cm (start value); calibrate in M3 | Beta |
| ERR-EX01-04 | Knees cave (valgus), front view | Frontal-plane projection angle trending above the user's own baseline across the set; never a verdict; calibrate in M3 | Beta |
| ERR-EX02-01 | Insufficient hinge | Peak hip flexion <85% of baseline; calibrate in M3 | GA |
| ERR-EX02-02 | Squatting the hinge (too much knee bend) | Knee flexion at bottom > baseline + 20°; calibrate in M3 | GA |
| ERR-EX02-03 | Dumbbells drift away from the legs | Wrist-to-knee/ankle line distance > 25% of thigh length at bottom; calibrate in M3 | Beta |
| ERR-EX03-01 | Hip sag | Shoulder–hip–ankle line deviates downward >10° (start value); calibrate in M3 | GA |
| ERR-EX03-02 | Hip pike | Upward deviation >15° (start value); calibrate in M3 | GA |
| ERR-EX03-03 | Partial range | Bottom elbow flexion <90% of baseline; calibrate in M2 | GA |
| ERR-EX04-01 | Short lunge depth | Front-knee flexion <90% of baseline; calibrate in M3 | GA |
| ERR-EX04-02 | Torso pitches forward | Trunk angle > baseline + 15°; calibrate in M3 | GA |
| ERR-EX04-03 | Front knee caves, front view | Same trend method as ERR-EX01-04; calibrate in M3 | Beta |
| ERR-EX05-01 | Partial pull | Shoulder extension at top <85% of baseline; calibrate in M3 | GA |
| ERR-EX05-02 | Torso heave / rotation | Trunk angle changes >15° within the rep; calibrate in M3 | GA |
| ERR-EX06-01 | Incomplete lockout | Elbow extension at top < baseline − 10°; calibrate in M3 | GA |
| ERR-EX06-02 | Excessive lean-back | Trunk extension > baseline + 10° during the press (sagittal inference only [R2 §2.3]); calibrate in M3 | Beta |
| ERR-EX07-01 | Incomplete hip extension | Shoulder–hip–knee angle at top < baseline − 10°; calibrate in M3 | GA |
| ERR-EX07-02 | No pause at the top | Hold shorter than the programmed pause (default 1 s; program-defined) | GA |
| ERR-EX08-01 | Incomplete stand (does not count toward the benchmark) | Knee angle at top <160° (start value); calibrate in M2; STEADI counts full stands only [R6 #87](https://www.cdc.gov/steadi/hcp/clinical-resources/index.html) | GA |
| ERR-EX08-02 | Arms used to push off | Wrists leave the crossed-arm position by >15% of torso length; calibrate in M2 | GA |
| ERR-EX09-01 | Hips sag | Body line >10° below straight for >2 s; calibrate in M3 | GA |
| ERR-EX09-02 | Hips pike | Body line >15° above straight for >2 s; calibrate in M3 | GA |
| ERR-EX10-01 | Torso swing | Trunk angle change >10° during the curl; calibrate in M3 | GA |
| ERR-EX10-02 | Partial range | Top elbow flexion <90% of baseline, or bottom extension < baseline − 15°; calibrate in M3 | GA |
| ERR-EX10-03 | Elbow drifts forward | Upper arm >25° from vertical at the top; calibrate in M3 | Beta |

A Beta cue is promoted to GA only when it meets KPI-02 (precision ≥0.90, recall ≥0.70) on the frozen held-out set [R2 §5.2].

---

## 8. Form-correction engine headlines

### 8.1 Pipeline (on-device, MVP) [R2 §5.1]

```
VisionCamera 5.2.3 frame output (~HD 16:9, 30 fps)
 └─ useAsyncRunner worklet: drop the frame if busy; always dispose() in try/finally
     └─ PoseEngine (custom Nitro HybridObject, Swift + Kotlin)
         MediaPipe Pose Landmarker, VIDEO mode, num_poses = 1, Full model (Lite on Tier C or thermal stress)
         → drop face landmarks 0–10 in native code (keep at most one derived head-angle number)
         → 22 body landmarks × (x, y, z, visibility, presence) + world points as typed arrays; no pixels cross into JS
 └─ Worklet: visibility gate → One Euro filter (mincutoff ≈ 1 Hz, beta from 0.001, tuned per exercise) → hip-centred, torso-scaled normalisation → joint angles
 └─ Exercise state machine (phases + hysteresis) → RepEvent + per-rep metrics (ROM, tempo, velocity estimate, confidence)
 └─ View-aware rule engine (abstains on low confidence) → cue scheduler (rep boundaries, ≤1 corrective cue per rep, periodic positive cue)
 └─ Outputs: Skia skeleton overlay + captions; expo-speech audio + expo-haptics; SessionLog (metrics only, never pixels)
 └─ Thermal governor (iOS ThermalState / Android thermal status, polled ≤ once per 10 s): Full → Lite → lower FPS → counting-only
```

Fallback: if MediaPipe fails to initialise on iOS, Apple Vision 2D runs instead (fewer joints, so view-specific cues that need missing joints are disabled). Rules, thresholds and cue copy ship as signed, versioned remote config (F-022, F-111), so tuning needs no app release. LLMs and VLMs never produce live cues: zero-shot VLMs scored 1.29–2.27/5 on QEVD [R2 #44](https://arxiv.org/abs/2407.08101).

### 8.2 Models per platform (versions and licences; verify latest stable at build time)

| Platform | Role | Model / runtime | Version | Licence |
|---|---|---|---|---|
| Android | Primary | MediaPipe Pose Landmarker (BlazePose GHUM 3D) Full, via `com.google.mediapipe:tasks-vision` | 1.1.1 (minSdk 24) [R2 #7](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/maven-metadata.xml) | Apache-2.0 (SDK and model card) [R2 #2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) |
| Android | Degrade | Pose Landmarker Lite | 1.1.1 | Apache-2.0 |
| iOS | Primary | `MediaPipeTasksVision` (CocoaPods, iOS 15+; packaging per D-05) | 1.0.0 [R2 #10](https://cdn.cocoapods.org/Specs/9/9/0/MediaPipeTasksVision/1.0.0/MediaPipeTasksVision.podspec.json) | Apache-2.0 |
| iOS | Fallback / cross-check | Apple Vision `VNDetectHumanBodyPoseRequest` (2D, 19 joints) | OS framework [R2 #18](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest) | Apple OS |
| iOS | Optional calibration | Apple Vision 3D `HumanBodyPose3DObservation.bodyHeight` | iOS 17+ [R2 #21] | Apple OS |
| Offline / CI | Pre-labelling (Heavy), golden-video replay (Full) | `mediapipe` (Python) | 1.1.1 [R2 #110](https://pypi.org/project/mediapipe/) | Apache-2.0 |
| V2 | Learned temporal models | LiteRT (Android) and LiteRT/Core ML (iOS) inside PoseEngine | LiteRT 2.3.0 [R2 #119] | Apache-2.0 |
| Watch-list only | RTMPose (code Apache-2.0, weights' commercial status unverified), RF-DETR Keypoint (preview), MoveNet (Apache-2 per NGC) | — | — | Legal review before any use |
| **Excluded** | YOLO26-pose (AGPL-3.0 or paid Enterprise) [R2 #29](https://www.ultralytics.com/license); Sapiens (CC BY-NC) and Sapiens2 (bars biometric processing) [R2 #33, #34]; ML Kit Pose (beta, no release since Aug 2024) [R2 #14] | — | — | — |

Model limits that shape copy: single person, ≤4 m, head visible, "not intended for human life-critical decisions" [R2 #2]. Copy says "form guidance", never injury prevention.

### 8.3 Targets (release gates; proposed in R2 §5.2, to be confirmed at M1/M3)

| Metric | Tier A | Tier B | Tier C | KPI |
|---|---|---|---|---|
| Sustained pose FPS over a 20-min session | ≥30 | ≥20 | ≥15 (Lite), else counting-only | KPI-04 |
| Frame-to-overlay latency, p95 | ≤100 ms | ≤150 ms | ≤200 ms | NFR |
| Rep end → audio cue, p95 | ≤500 ms | ≤500 ms | ≤700 ms | KPI-03 |
| Rep count, guided setup | Exact on ≥95% of sets; within ±1 on ≥99% | same | Tier C ≥90% exact by V1.0+90 days | KPI-01 |
| Form-cue precision / recall per GA cue (held-out set) | ≥0.90 / ≥0.70 | same | cues off | KPI-02 |
| Sagittal angle MAE vs lab reference, side view | ≤10° | ≤10° | n/a | NFR |
| Velocity-loss agreement vs linear position transducer | Within ±10 percentage points on ≥80% of sets | same | n/a | NFR (M4 study) |
| Assessed-rep rate (not abstained) | ≥85% (Beta) → ≥90% (V1.0+90 days) | same | n/a | KPI-05 |
| Thermal | No "serious" state within 20 min | same | degrade gracefully | NFR |

Context: in-the-wild rep counting state of the art is only OBO 0.56 (PoseRAC) [R2 #51](https://github.com/MiracleDance/PoseRAC), which is why the guided setup is mandatory; OpenCap with two iPhones reached 4.5° MAE [R2 #59].

### 8.4 Data strategy

| Topic | Decision |
|---|---|
| Rule | **No research-licensed dataset is used for training, benchmarking or demos** (Fitness-AQA, Fit3D, QEVD, EgoExo-Fitness, MyoMechanix, RepCount, Countix, EC3D; SMPL/SMPL-X without a commercial licence) [R2 §3.1](https://github.com/iSEE-Laboratory/EgoExo-Fitness). Only the MM-Fit CC BY 4.0 video subset may be used, with attribution, after a consent-scope check [R2 #48](https://zenodo.org/records/7672767). |
| Collection | (1) Paid recording sessions with written releases naming model training (W5–W15, 2026-11-30 → 2027-02-12); (2) coach-directed error sets mixing natural errors under load with coached ones (faked unloaded errors are exaggerated [R2 #40]); (3) in-app opt-in keypoint contributions from Beta (F-104); video only in paid sessions. |
| Volume (to V1.0) | **120 participants** (60 US + 60 India, D-11), each doing all 10 exercises: 2 normal sets + 1 error-directed set, filmed from the required view and a 45° view → **≈7,200 labelled set clips, ≈57,600 rep-views**, far above "a few hundred samples per terminal state" [R2 #4]. Plus **30 held-out validation participants** (never in training or calibration) in W20–W26. Collection continues per cue until it meets KPI-02. |
| Coverage matrix | Views front/45°/side; distance 2/3/4 m; light bright/dim/backlit; clothing shorts/tights/loose; equipment occlusion; ≥40% women, ≥30% aged 45+, ≥30% BMI ≥30, skin tone spread across Monk Skin Tone scale groups; ≥3 phone models per tier [R2 §3.2]. |
| Labels | Rep start/end and phase; per-rep error tags with severity 0–2; view tag; quality flags (occlusion, out of frame). Two certified coaches label every clip, an adjudicator resolves disagreements; inter-rater agreement tracked per error code. Keypoints pre-labelled offline with BlazePose Heavy (F-113). ≈830 labelling hours. |
| Consent & privacy | Written release for video; faces blurred on stored clips; keypoints stored by default for research data; consent revocation removes a person from future training sets; retention schedule in §11.3 [R2 §3.2, R4 #43]. |
| Splits | By subject (nobody in both train and test); test sets frozen per exercise × view and per device tier. |
| Validation protocol (M4) | Rep exact/±1 rates and per-cue precision/recall against adjudicated labels; angle MAE against Kinovea video goniometry on 30 participants; velocity loss against a linear position transducer on 20 participants [R6 recommendations]; results **stratified** by sex, age band (18–34/35–54/55+), BMI band, skin-tone group, clothing, lighting and device tier. Any stratum more than 5 points below the overall rep-accuracy figure blocks GA for that exercise. Results feed the public methodology page (Apple 1.4.1) [R4 #75]. |

---

## 9. AI coach headlines

### 9.1 Model and platform configuration

| Setting | Decision |
|---|---|
| Default model | `claude-opus-5-5` on **every** route at V1.0 (chat, safety classifier, debrief, plan narration, meal-photo parsing). Adaptive thinking is always on; depth via `output_config.effort`: `medium` for chat and plan narration, `low` for the classifier, meal parsing and debriefs. |
| SDK | Official Python SDK `anthropic` 1.15.0 [R2 #108](https://pypi.org/project/anthropic/), called only from our backend (no device-to-Anthropic calls). |
| Output | Final replies via structured outputs (`output_config.format`) → `{reply_text, kb_card_ids[], plan_change_proposal?, red_flag?}`; no assistant prefill. |
| Tools | `tool_choice: auto` with `strict: true` JSON-schema tools (forced `any`/`tool` is not supported). Tools only read or **propose**. No PHI in schemas [R3 #3]. |
| Streaming | SSE for chat. |
| Prompt caching | Prefix order, max 4 breakpoints: (1) policy + persona, (2) tool definitions + KB index, (3) user profile + constraint summary, (4) conversation so far. 5-minute cache. |
| Context | Mid-conversation system messages inject constraint changes; server-side compaction (beta) only for threads >100K tokens in the consumer org (ZDR-eligible, not HIPAA-eligible) [R3 #3]. |
| Citations | Not the API citations feature (it cannot be combined with `output_config.format`). Tools return KB cards; the reply lists `kb_card_ids`, the server validates them, and the app renders each card verbatim with its sources (02 §7). |
| Refusals | `refusal` stop reason → fixed fallback + resources. Server-side model fallbacks off. |
| Data terms | Apply for ZDR (D-06); no Batch or Files API with user data; `inference_geo: global` (US-only `us` costs 1.1× and is used only if a contract requires it) [R3 #4](https://platform.claude.com/docs/en/manage-claude/data-residency). Avoid "Covered Models" that need 30-day retention [R3 §6]. |
| Audit | Every message logs model ID, prompt version, KB version, rule IDs fired and eval-run ID. |

### 9.2 Cost table and the routing decision (D-02)

Prices per 1M tokens (as of 2026-10-06; cache-write prices from the official page via R5 [R5 #76](https://platform.claude.com/docs/en/about-claude/pricing)):

| Model | Input | Output | Cache read | Cache write (5 min) | Context | Notes |
|---|---|---|---|---|---|---|
| Claude Opus 5.5 `claude-opus-5-5` | $4.00 | $20.00 | $0.20 | $5.00 | 1M; 128K max output | Default; thinking billed as output |
| Claude Sonnet 5.5 `claude-sonnet-5-5` | $2.00 | $10.00 | $0.20 (official page shows $0.10; we model $0.20) | $2.50 | 1M | Eval-gated alternative |
| Claude Haiku 5.5 `claude-haiku-5-5` | $0.10 ($0.50 >100K prompt) | $0.50 ($2.50 >100K) | $0.01 (R5) | $0.125 (assumed 1.25×; verify) | 1M | Eval-gated alternative |

| Unit (token math in §13.2) | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|
| One coach turn (5K cached + 1K fresh in + 800 out) | $0.0210 | $0.0110 | $0.00055 |
| Active Premium user-month (base usage) | **$2.42** | $1.23 | $0.06 |
| Active Premium+ user-month (1.8× usage) | $4.36 | $2.21 | $0.11 |
| Free monthly active user | $0.12 | $0.062 | $0.003 |

**D-02 (owner decision): model routing per route.** Default: Opus 5.5 on all routes at V1.0. At M3 (2027-04-09) the same eval suite runs on Sonnet 5.5 and Haiku 5.5 per route. A route may move only if the cheaper model shows (1) zero never-rule failures, (2) red-flag recall at least equal to Opus, (3) clinician-rated rubric score within 3% of Opus, and (4) for India routes, parity in English and Hindi. Recommended order of candidates if they pass: meal-photo parsing → free-tier chat → India routes; paid-tier chat, plan narration and the safety classifier stay on Opus. Deadline: 2027-04-23 for V1.0 config; 2027-08-13 for India. Re-run on every model or prompt change. Moving traffic is never automatic.

### 9.3 Tool list (strict)

| Tool | Type | Returns / does |
|---|---|---|
| `get_profile_summary` | read | Goals, experience, equipment, units (no name, email or exact location) |
| `get_constraints` | read | Active constraint set: rule IDs, effects, KB card IDs, gates |
| `get_recent_sessions(days≤28)` | read | Sessions with per-set metrics: reps, ROM, tempo, velocity loss, ERR codes, confidence |
| `get_session_detail(session_id)` | read | One session's per-rep metrics |
| `get_program(week)` | read | Current plan and adherence |
| `get_food_log(days≤14)` | read | Daily totals, protein, fibre, floor flags (hidden in ED-safe mode) |
| `get_med_context(days≤28)` | read | Medicine names/classes, dose events, side-effect check-ins (only with consent CON-05, §11.3) |
| `get_wearable_summary(days≤28)` | read | Daily HR, sleep, steps, weight trend (summaries only) |
| `search_kb(query, class?)` | read | KB cards as citable search results |
| `propose_plan_change(changes, reason_codes)` | propose | Validated by the rules engine; shown with a "Why this changed" card; user confirms |
| `propose_session_adjustment(session_id, kind = swap / load / volume)` | propose | Same validation and confirmation |
| `log_checkin(type = rpe / discomfort / side_effect / energy, value)` | propose | Saved only after user confirmation |
| `save_memory(text, category)` | write (user turns only) | Visible, editable, deletable; health memories need consent CON-06 |
| `flag_safety_concern(tier, template_id)` | route | Hands over to the deterministic template; the model never writes the red-flag text |

No web browsing, code execution, outbound messaging, payment or medication-changing tools.

### 9.4 Knowledge-base sources (cards cite these; review at least every 12 months and on any label change)

FDA labels via DailyMed (SPL set ID, `effective_time`) and openFDA [R3 #57](https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm); RxNorm/RxClass via RxNav-in-a-Box (NLM attribution required; the NLM interaction API was discontinued in 2024) [R3 #53, #54]; ADA Standards of Care 2026 §5 [R3 #11](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690188); 2025 ACLM/ASN/OMA/TOS GLP-1 nutrition advisory [R3 #13]; ACSM 2026 resistance-training position stand and ACSM pre-participation screening [R3 #16, #17]; CDC heat and medications guidance (2025-09-18) [R3 #24](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html); AHA beta-blocker exercise page [R3 #19]; NHS apixaban/rivaroxaban pages [R3 #47]; FDA caffeine guidance and supplement-ingredient directory (2026-05-01) [R3 #49, #52]; ISSN caffeine (2021) and creatine (2017) stands; CDC STEADI [R6 #87]; USDA FDC, Open Food Facts, IFCT 2017 (India, with permission). Interaction databases (DrugBank, FDB) are **not** used before an FDA CDS review [R3 §3].

### 9.5 Medication classes (constraint engine)

| Code | Class (examples) | Release | Constraint applied to the plan | Red flag → template tier |
|---|---|---|---|---|
| GLP1 | GLP-1 RA and GIP/GLP-1 (semaglutide injection and pill, tirzepatide, orforglipron) | **MVP** | Lean-mass programme on; protein rule; kcal-floor flag; GI-friendly meals; dose-cycle scheduling (Beta) | Persistent vomiting/diarrhoea with dizziness or low urine → Urgent; suicidal language → Crisis [R3 #31] |
| BB | Beta-blockers (metoprolol, atenolol, propranolol) | **MVP** | Intensity = RPE/talk test; HR zones off unless the clinician supplied targets; hypoglycaemia education if a glucose-lowering drug is also listed | Chest pain or fainting → Emergency |
| INS | Insulin and secretagogues (insulin glargine, glipizide) | **MVP** | Pre- and post-session check-in prompts; "carry fast-acting carbs" checklist; follow your own diabetes plan; no numbers | Reported lows or symptoms → Urgent (clinical lead sets wording) |
| SGLT2 | SGLT2 inhibitors (empagliflozin, dapagliflozin) | **MVP** | Block keto/very-low-carb templates, prolonged fasts, aggressive deficits; hydration emphasis [R3 #30] | Nausea, vomiting, abdominal pain, malaise, shortness of breath → Urgent |
| ACAP | Anticoagulants and antiplatelets (apixaban, rivaroxaban, warfarin; aspirin, clopidogrel) | **MVP** | Exclude contact, combat and high-fall-risk drills; protective-gear prompts; flag SSRI co-listing [R3 #35] | Head impact, a fall, bleeding that won't stop, blood in vomit/cough, severe headache → Emergency |
| STAT | Statins (atorvastatin) | **MVP** | Muscle-symptom check-ins separating normal soreness from red flags; conservative ramp after start or dose change (clinician to confirm) [R3 #34] | Dark urine, unexplained muscle pain or weakness, fever → Urgent |
| AHT | Other antihypertensives (amlodipine, lisinopril, losartan, nitrates, alpha-blockers) | V1.0 | Graded cool-down ≥5–10 min; rise-slowly prompts; heat hydration | Dizziness or fainting → stop + template |
| DIU | Diuretics (furosemide, HCTZ) | V1.0 | Hydration plan, heat alerts, cramp check-ins; no electrolyte supplement advice | Cramps with weakness or palpitations → Urgent |
| FQ | Fluoroquinolones (levofloxacin, ciprofloxacin) | V1.0 | Tendon-protect mode during the course and a post-course window set by the clinical lead: no plyometrics, sprints or heavy eccentric lower-limb work [R3 #36] | Tendon pain/swelling → stop; contact prescriber |
| CS | Systemic corticosteroids (prednisone) | V1.0 | Encourage weight-bearing and resistance training; glucose check-ins if a diabetes medicine is listed; with FQ → tendon-protect | New weakness → clinician |
| STIM | ADHD stimulants (amphetamine, methylphenidate) | V1.0 | Heat/hydration alerts; caffeine and pre-workout stacking warning; HR-zone recalibration flag | Chest pain, fainting, palpitations → Emergency |
| AD | Antidepressants (SSRIs/SNRIs, TCAs) | V1.0 | Heat alerts; never suggest NSAIDs; hyponatraemia symptom check on long endurance sessions | Confusion or unsteadiness → Urgent; self-harm language → Crisis |
| ACH | Anticholinergic and heat-impairing drugs (diphenhydramine, oxybutynin; antipsychotics, lithium, topiramate) | V1.0 | Heat-index warnings; suggest indoor or cooler slots | Heat-illness signs → Emergency |
| THY | Thyroid hormone (levothyroxine) | V1.0 | Refuse "thyroid for weight loss" (boxed warning) [R3 #42]; otherwise train normally | Palpitations or chest pain → template |
| SUP | Supplements (caffeine, creatine, pre-workouts) | V1.0 (caffeine counter); V1.4 label scan (F-015) | 400 mg/day caffeine cap incl. pre-workouts; never recommend pure/powdered caffeine; FDA "never recommend" list; creatine as education only | Unlawful ingredient → warning card |

KB cards: ~20 for the 6 MVP classes, ~45 for all 15 by V1.0 [R3 rec. 8]. A medicine outside the covered classes gets the generic "check with your clinician or pharmacist about exercise" card and no class-specific claims.

### 9.6 Safety policy (deterministic; enforced before and after the LLM)

**Red-flag tiers** (deterministic rules + classifier; fixed clinician-approved templates, never free text) [R3 §4.1]:

| Tier | Triggers (examples) | Response |
|---|---|---|
| Emergency | Chest pain or fainting during exercise; head injury on an anticoagulant; heat illness; suicidal intent | Stop the session; show the local emergency number |
| Urgent | Rhabdomyolysis signs on a statin; DKA signs on an SGLT2 inhibitor; tendon pain on a fluoroquinolone; persistent vomiting on a GLP-1; recurrent lows | "See a clinician today" template |
| Crisis | Self-harm; eating-disorder behaviours | Crisis line plus a human service; ED-safe mode on |
| Gate | Pregnancy; new diagnosis; new medicine | Pause affected features until the user confirms clinician clearance; pregnancy stop signs shown [R3 #94] |

**Crisis and emergency routing** (built by us; Claude's ThroughLine banner is not available via the API [R3 #10]):

| Market | Emergency | Crisis | Eating-disorder support |
|---|---|---|---|
| US | 911 | 988 call/text/chat [R3 #69](https://988lifeline.org/) | ANAD (888) 375-7767 [R3 #74](https://anad.org/get-help/) |
| UK | 999 / A&E | NHS 111 mental-health option; Samaritans 116 123 [R3 #70] | Beat (England 0808 801 0677; Scotland 0808 801 0432; Wales 0808 801 0433; NI 0808 801 0434) [R3 #73] |
| India | 112 | Tele-MANAS 14416 or 1-800-891-4416 [R3 #71](https://telemanas.mohfw.gov.in/) | None verified; Tele-MANAS |

**Never-rules (unit-tested; any failure blocks release, KPI-07):**
1. Never tell a user to start, stop, skip, re-time or change the dose of any medicine; never encourage stopping a beta-blocker or anticoagulant.
2. No dose calculators, insulin or carbohydrate-dose advice, or electrolyte/potassium advice [R3 #83].
3. No diagnosis, symptom interpretation, lab interpretation or treatment plans; no "abnormal" results; no disease thresholds in copy.
4. No interaction checking beyond the fixed class rules; out-of-scope medication questions get "ask your prescriber or pharmacist" plus an export option.
5. No plan below the kcal floors (flag at 1,200 kcal/day for women and 1,800 for men [R3 §2]; the RD sets the default for users who do not record sex) or targeting loss above 0.9 kg (2 lb)/week [R4 #86]; no "burn it off" or compensatory-exercise framing; never refuse a user's choice to eat more.
6. No body-shape comment, ranking or critique, including from camera data; no emotion inference from face or voice [R4 #63](https://artificialintelligenceact.eu/recital/18/).
7. No professional titles ("Dr", "RD", "PT", "nurse", "therapist", "prescribe"); AI disclosure at each session start plus a persistent label [R3 #88].
8. No thyroid hormone for weight loss; no recommendation of FDA-listed unlawful supplement ingredients.
9. **India:** the chatbot gives no medication counselling; medication context appears only as fixed plan cards [R4 #22].

**Eating-disorder safeguards** (lessons from NEDA's Tessa, disabled 2023-05-30 after a generative "upgrade" gave dieting advice [R3 #68](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea)): ED-safe mode (F-057) triggered by opt-in, a clinician-chosen screener or chat signals; numeric floors; human helplines always offered; any model, prompt, KB or vendor change re-runs the safety eval and needs clinical sign-off; model IDs pinned.

**Age:** 18+ only (Anthropic consumer services are 18+ [R3 #9]); a user signalling they are under 18 → coach locked and resources shown.

### 9.7 Message limits per tier (enforced by F-092; safety templates and crisis routing never count)

| Tier | Coach messages / month | Meal-photo scans / month | Post-workout debrief | Weekly plan narration |
|---|---|---|---|---|
| Free (US, UK) | 10 | 3 | Template (no LLM) | Template |
| Free (India) | 4 | 1 | Template | Template |
| Trial (7 days, annual plans) | Premium limits | Premium limits | LLM | LLM |
| Premium (US, UK) | 150 | 90 | LLM, one per session | LLM, weekly |
| Premium (India) | 60 | 36 | LLM | LLM |
| Premium+ (US, UK) | 270 | 160 | LLM | LLM + monthly benchmark summary |
| Premium+ (India) | 108 | 64 | LLM | LLM |

Abuse limits for all tiers: ≤30 coach messages per hour, ≤2,000 characters per message (OWASP LLM10) [R3 #78](https://genai.owasp.org/llm-top-10/). Premium+ = 1.8× Premium; India = 40% of US.

### 9.8 Evaluation and change control

- **Suite:** R3 red-team set (15 classes × benign, edge, red-flag, jailbreak, eating-disorder risk, minor, crisis; ≥10 items each → ≥1,050 items, written with clinicians), the HealthBench consensus subset [R3 #75](https://arxiv.org/abs/2505.08775), 200 dietitian-labelled meal photos, prompt-injection cases from OWASP LLM/Agentic Top 10 [R3 #78, #79].
- **Judge:** Opus 5.5 with per-item rubrics; clinicians double-review a stratified sample and every failure (LLM juries reached ICC 0.47 vs 0.43 between clinicians in MedHELM [R3 #77]).
- **Gates:** zero never-rule or crisis-routing failures (KPI-07), red-flag recall ≥0.98 (KPI-08). Runs in CI on every prompt, model, KB or rule change (F-114) and on a weekly production sample.
- **AUP:** Anthropic's Usage Policy effective 2026-11-12 treats medication recommendations and symptom triage as high-risk and excludes wellness content and fixed rules [R3 #1]; our reading that clinician-approved cards plus fixed routing satisfy it must be confirmed with Anthropic before 2026-11-12 (§11.6, R-01).

---

## 10. Tech stack & services

Versions are the R2 registry snapshot of 2026-10-16 [R2 §4]. **Verify latest stable at build time**; any change to a pinned version needs an ADR. Move SDK-aligned packages in lockstep (Expo's bundled module list), never "latest" [R2 §4.4].

### 10.1 Mobile app

| Component | Pinned version | Notes |
|---|---|---|
| React Native | **0.88.0** [R2 #69](https://www.npmjs.com/package/react-native) | New Architecture only (RN ≥0.82); Hermes V1 |
| Expo SDK | **58** (`expo` 58.0.12; template `expo-template-default` 58.0.21) [R2 #72, #75] | Development builds only (`expo-dev-client` ~58.0.13); never Expo Go; `npx expo prebuild --clean` after native changes |
| React | 19.3.0 | Bundled with SDK 58 |
| TypeScript | **~6.0.3** (do not use 7.0.2, which ships without a programmatic API) [R2 #96](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) | strict mode |
| Camera | `react-native-vision-camera` **5.2.3** + `react-native-vision-camera-worklets` 5.2.3 + `react-native-vision-camera-skia` 5.2.3 [R2 #76](https://www.npmjs.com/package/react-native-vision-camera) | Frame processors need `react-native-worklets`, not `worklets-core` [R2 #78] |
| Native module base | `react-native-nitro-modules` 0.37.1, `react-native-nitro-image` 0.15.2 | Our `PoseEngine` HybridObject (Swift + Kotlin) |
| Worklets / animation / drawing | `react-native-worklets` 0.13.0, `react-native-reanimated` 4.7.1, `@shopify/react-native-skia` 2.14.0 | Lockstep with RN 0.86–0.88 |
| Pose (native) | MediaPipe Tasks Vision Android 1.1.1; iOS `MediaPipeTasksVision` 1.0.0 | D-05 packaging (CocoaPods trunk goes read-only 2026-12-02) [R2 #13](https://blog.cocoapods.org/CocoaPods-Specs-Repo/) |
| Audio / haptics | `expo-speech` 58.0.3, `expo-haptics` 58.0.6 | TTS cues; on-device speech recognition via the OS (iOS Speech on-device mode, Android on-device recognizer) |
| V2 runtime | LiteRT 2.3.0 inside PoseEngine; `react-native-fast-tflite` 3.0.1 only as a standalone option (its VisionCamera v5 glue is private) [R2 #85] | Not in MVP |
| Pinned at M1 by ADR (not in R2) | `expo-router`, `expo-sqlite` with SQLCipher + `expo-secure-store`, `expo-notifications`, `react-native-purchases` (RevenueCat), `@sentry/react-native`, `posthog-react-native`, HealthKit and Health Connect libraries | Must be SDK-58-compatible and New-Architecture-ready |

### 10.2 Backend

| Component | Pinned version | Notes |
|---|---|---|
| Python | **3.14.8** (not 3.15.0, released 2026-10-09) [R2 #98](https://www.python.org/downloads/) | |
| API | FastAPI **0.143.3**, Uvicorn 0.54.0, Pydantic 2.14.1, pydantic-settings 2.16.0 [R2 #99](https://pypi.org/project/fastapi/) | OpenAPI → generated TypeScript client |
| ORM / migrations | SQLAlchemy 2.1.4, Alembic 1.20.0, asyncpg 0.32.0 | |
| Database | **PostgreSQL 18.6** (supported to 2030-11-14) + **pgvector 0.8.7** (Python client 0.5.1) [R2 #114, #115] | pgvector serves KB-card and memory retrieval; embeddings from a self-hosted open-weights model run with onnxruntime 1.31.0 (model chosen by ADR at M1; Apache-2.0/MIT only), so no extra data processor |
| Cache / broker | **Amazon ElastiCache for Valkey** (BSD-3; R2 lists 9.0.6/9.1.2) with redis-py 8.1.0 | Replaces Redis for licence reasons (§0.7) |
| Jobs | Celery **5.6.3** [R2 #105] | Not arq (maintenance-only) [R2 #106] |
| LLM SDK | `anthropic` **1.15.0** | §9.1 |
| Offline CV tooling | `mediapipe` 1.1.1 (golden-video replay, pre-labelling) | CI and labelling only |

### 10.3 Hosting and regions

| Item | Decision |
|---|---|
| Cloud | AWS. Primary region **us-east-1**, multi-AZ: ECS Fargate (API + Celery workers), RDS for PostgreSQL 18 (Multi-AZ, point-in-time recovery 35 days), ElastiCache for Valkey, S3 + KMS, CloudFront, WAF, Secrets Manager, CloudWatch + OpenTelemetry, SES, Cognito |
| Disaster recovery | Nightly snapshot copy and S3 replication to us-west-2; RPO ≤15 min in-region, 24 h cross-region; RTO 4 h |
| UK (V1.2) | Served from us-east-1 under the UK extension to the EU-US Data Privacy Framework, IDTA as fallback [R4 #51] |
| **India (V1.3)** | Served from us-east-1 with a DPDP-compliant notice of transfer. The schema is **region-ready** from day 1 (`home_region` on every user-scoped row; region-scoped S3 buckets and KMS keys). An **ap-south-1 (Mumbai) cell** is deployed when a trigger fires: a partner contract requiring India storage, a MeitY transfer restriction that affects us, or India MAU >50,000. LLM inference stays outside India in every case (no India `inference_geo`) [R3 #4]. |
| EU (V2) | eu-central-1 cell + DPF/SCCs |
| B2B HIPAA (V2) | Separate AWS account and a separate Anthropic organisation with a BAA (BAAs are organisation-level and permanent; Batch, Files and compaction are blocked there) [R3 #3] |

### 10.4 Third-party services

| Need | Service | What it may receive | Rule |
|---|---|---|---|
| Auth | Amazon Cognito (Sign in with Apple, Google, email one-time code) | Email, auth IDs | Revoke Sign in with Apple tokens on deletion [R4 §4] |
| Payments | RevenueCat + App Store / Play Billing; Stripe Billing + RevenueCat Web for US web checkout at V1.2 (D-13) | Receipts, pseudonymous app-user ID | No health data |
| LLM | Anthropic API (ZDR requested) | Minimised prompts (§11.2) | Backend proxy only |
| Product analytics | PostHog Cloud (US) | Allowlisted events, pseudonymous ID | No health values, no free text, no autocapture, no session replay |
| Crash reporting | Sentry | Stack traces, device model | PII scrubbing; no screenshots or replay |
| Push | Expo Push Service → APNs/FCM | Device token, generic text | Never medicine or health words in payloads |
| Email | Amazon SES | Email address, transactional text | No tracking pixels on health-related emails |
| Feature flags / remote config | PostHog flags (UI experiments only); our own signed remote-config service for exercise rules, constraint rules and cue copy; RevenueCat Offerings for paywalls | — | Safety configuration never lives in a third-party flag tool |
| Weather (heat alerts) | Apple WeatherKit REST (server-side) | Coarse, city-level location | Only with consent CON-10 |
| Drug data | RxNav-in-a-Box (self-hosted), openFDA, DailyMed | No user identifiers | NLM attribution string required [R3 #53] |
| Nutrition data | USDA FDC (CC0), Open Food Facts (ODbL, cached), fatsecret Premier Free or Edamam (D-10); IFCT 2017 for India with NIN permission | Food search strings | Attribution; share-alike for OFF-derived databases [R3 #61] |
| Build / CI | EAS Build & Submit, GitHub Actions, device lab + cloud device farm | Code and builds | — |

### 10.5 Explicitly NOT used

- **Ad, attribution or tracking SDKs** of any kind (Meta, Google Ads, AppsFlyer, etc.), pixels or IDFA/AAID; no App Tracking Transparency prompt because nothing tracks [R4 #28].
- AGPL or non-commercial models and data: Ultralytics YOLO, Sapiens/Sapiens2, research-licensed datasets (§8.4); RTMPose/ViTPose weights until legal review.
- ML Kit Pose; community MediaPipe RN plugins; `react-native-worklets-core`; Flutter; Expo Go; TypeScript 7 for tooling; arq; Redis-licensed binaries we host ourselves.
- LLMs or VLMs for live cues; Anthropic Batch or Files API with user data; "Covered Models" with 30-day retention; server-side model fallbacks.
- Drug-interaction databases (DrugBank, FDB, Medi-Span) and dose calculators; Nutritionix (partner-only) [R3 #65].
- Camera vital signs (heart rate, BP, SpO2), face recognition, face embeddings, segmentation masks, emotion inference.
- Session replay, autocapture analytics, iCloud backup of the health store, Google Fit APIs (deprecated) [R4 #84].

---

## 11. Data, privacy & compliance stance

### 11.1 Data inventory

| Class | Contents | Where processed | Leaves the phone? | Stored | Retention |
|---|---|---|---|---|---|
| DC-01 Account | Email, auth IDs, home region, birth year, age-gate result | Cloud | Yes | Postgres | Account life + 30 days |
| DC-02 Camera frames / video | Raw pixels | **Device only** | **Never** (except DC-10) | Not stored; each frame discarded after inference | 0 |
| DC-03 Keypoint series | Body landmarks over time (face points 0–10 already removed) | Device | **No by default**; only via DC-11 opt-in | On-device replay buffer | ≤30 days on device |
| DC-04 Training metrics | Per-rep/per-set reps, ROM, tempo, velocity estimate, ERR codes, confidence, session summaries | Derived on device | Yes | Postgres | Account life |
| DC-05 Health & medication profile | Screening answers, medicines (RxCUI/class), schedules, side-effect/energy/discomfort check-ins, gates | Device + cloud | Yes (consent CON-02) | Postgres, field-level KMS encryption | Account life; items deletable any time |
| DC-06 Nutrition | Food entries, targets, floors | Cloud | Yes | Postgres | Account life |
| DC-07 Meal photos | Image for analysis | Cloud (transient) + Anthropic | Yes, transiently (consent CON-04) | Deleted after parsing (≤24 h on retry failure); device copy optional | 0–24 h server-side |
| DC-08 Coach chats & memory | Messages, memory items | Cloud + Anthropic | Yes (CON-04; health memories CON-06) | Postgres, encrypted | Chats 18 months rolling; memory until deleted |
| DC-09 Health-platform data | HealthKit/Health Connect weight, HR, sleep, steps, workouts | Read on device | Daily summaries only (CON-07) | Postgres | Account life; never used for ads or marketing |
| DC-10 Shared clips | One user-chosen clip, face-blurred on device | Device → S3 | Yes, per clip (CON-09) | S3 + KMS | 30 days default, user max 365 days (Texas CUBI one-year limit) [R4 #43] |
| DC-11 Training contributions | Keypoint series (opt-in CON-08); paid-session video under written release, faces blurred | Research store | Yes (opt-in / release) | Separate de-identified bucket | Until consent withdrawn; session video ≤3 years |
| DC-12 Location | City-level location for heat alerts | Backend → WeatherKit | Yes (CON-10) | Not stored | ≤24 h |
| DC-13 Billing | Store receipts, entitlements | RevenueCat | Yes | RevenueCat + Postgres | 7 years (tax) |
| DC-14 Diagnostics | Allowlisted analytics events, crash reports | PostHog, Sentry | Yes (CON-11 where opt-in) | Vendors | Analytics 13 months; crashes 90 days |
| DC-15 Safety, consent & audit logs | Model/prompt/KB/rule versions, red-flag tier, consent records | Cloud | Yes | Postgres/S3 | 24 months (India needs ≥1 year) [R4 §2.5]; subscription consent proof 3 years or 1 year after the contract ends, whichever is longer [R4 #92] |

### 11.2 Exactly what leaves the phone

- **By default (with consents CON-01, CON-02):** DC-01, DC-04, DC-05, DC-06, DC-09 daily summaries, DC-13–DC-15.
- **Transient:** meal photos (DC-07) and city-level location (DC-12).
- **Only on explicit opt-in:** keypoint series (DC-11 via CON-08) and a specific clip the user shares (DC-10 via CON-09).
- **Never:** raw frames or video (except a shared clip), face landmarks, voice audio (transcribed on device, then discarded), segmentation masks, precise location, contacts, advertising IDs.
- **To Anthropic, per call, only:** a pseudonymous user key (never name or email), the profile summary, the constraint set, the metrics or logs a tool returned, the user's message, and the meal photo for a scan. Never keypoints or clips. Anthropic may keep API data up to 30 days unless ZDR is approved, and flagged content up to 2 years; the privacy policy says so [R3 #6](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).
- **Deletion:** in-app and web deletion completes within 30 days (backups roll off within 35 days). India: 48-hour notice before purpose-completion erasure; grievances answered within 90 days [R4 §2.5].

### 11.3 Consent model (purpose-based, recorded with version, timestamp, locale and text hash; withdrawal as easy as granting)

| ID | Consent | Default | Required for |
|---|---|---|---|
| CON-01 | Terms and privacy notice | Required | Any use |
| CON-02 | Explicit consent to process health data for the service (GDPR Art. 9(2)(a); WA MHMDA) | Required for training features | Camera coaching, programs, medication layer |
| CON-03 | OS camera permission, with an on-device explainer | Asked at first camera session | Camera coaching |
| CON-04 | AI processing by a third-party AI provider (Apple 5.1.2(i)) [R4 #75] | Asked before first chat or meal scan | Coach, meal scans, LLM debriefs |
| CON-05 | "Let the coach use my medicine list and logs" | Off until granted | Coach sees medicine names and dose/side-effect logs (otherwise class-level rule IDs only) |
| CON-06 | Health memories | Off | Coach remembers health facts |
| CON-07 | HealthKit / Health Connect, per data type | Off | Wearable sync |
| CON-08 | Help improve form models (keypoint contribution) | Off | DC-11 |
| CON-09 | Share this clip / this report | Asked each time | DC-10, F-074 |
| CON-10 | City-level location for heat alerts | Off | F-014 |
| CON-11 | Product analytics | US and UK: on with opt-out; India and EU: opt-in | DC-14 |
| CON-12 | Marketing messages | Off; never segmented by health data | Marketing |

Chats are never used to train models; there is no opt-in path at V1 (Anthropic API data is not used for training by default [R3 #7]).

### 11.4 Age gate

Neutral date-of-birth screen at the start of onboarding, before any account is created (no hint of the cut-off); under 18 → blocked with resources and only an anonymous "underage attempt" counter kept. 18+ store ratings. A chat signal that the user is a minor locks the coach and shows resources. No weight-control marketing to under-18s or to people with BMI below 18.5 [R4 #86]. Rationale: COPPA (compliance since 2026-04-22), DPDP parental consent for all under-18s, Anthropic 18+ rule [R4 §2.5, R3 §4.5].

### 11.5 Regulatory positioning

**Store and onboarding statement** (Google's required wording plus Apple's doctor reminder) [R4 §9](https://support.google.com/googleplay/android-developer/answer/16679511): "RepSight is a fitness and nutrition coaching app for healthy adults, with camera-based technique feedback and an AI coach. It is not a medical device and does not diagnose, treat, cure, or prevent any medical condition. Consult a healthcare professional for medical advice."

| Market | Positioning |
|---|---|
| US | General wellness under FDA's guidance of 2026-01-06; medication log, user-set reminders and label-sourced information sit under enforcement discretion [R4 #2, #6]. Not a HIPAA entity for the consumer app; the FTC Health Breach Notification Rule applies (60-day notices, up to $53,088 per violation) [R4 #25](https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0); WA MHMDA, Nevada SB 370 and Connecticut apply. Companion/therapy chatbot laws (CA SB 243, UT HB 452, IL WOPR, NY): build to the strictest version — AI disclosure, crisis protocol, no therapy or companion positioning [R4 §3]. |
| UK | MHRA intended-purpose test; qualification memo before V1.2; UK GDPR + Data (Use and Access) Act (complaints procedure); CAP Code s.13 [R4 §1.2, §2.4] |
| India | Not a device under CDSCO's intended-use draft; AI may not counsel patients or prescribe (Telemedicine Guidelines) → no medication counselling in chat; DPDP duties from 2027-05-13; Dark Patterns Guidelines; RBI e-mandate rules for direct billing [R4 §1.2, §2.5, §5] |
| EU (V2) | Not MDSW under MDCG 2019-11 rev.1; GDPR Art. 9 explicit consent + DPIA; AI Act Art. 50 disclosure (in force since 2026-08-02) and 50(2) machine-readable marking; two-step withdrawal button [R4 #59](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) |

### 11.6 Pre-launch compliance checklist (headline; the full matrix is R4 §8)

| # | Item | Due |
|---|---|---|
| 1 | Confirm the AUP reading with Anthropic (before 2026-11-12); apply for ZDR | Phase 0 |
| 2 | Intended-use statement, US qualification memo, claims register, banned-claims linter in CI | MVP |
| 3 | Consent center with records; AI-processing consent before first chat; 18+ age gate policy | MVP |
| 4 | On-device video architecture; face landmarks dropped; written biometric retention and destruction schedule (BIPA/CUBI) | MVP |
| 5 | SDK inventory with zero ad/attribution SDKs; Apple privacy labels and manifest; Google Data safety form | Beta |
| 6 | Privacy policy + Consumer Health Data Policy (WA/NV/CT); itemised DPDP notice for India | Beta (India by V1.3) |
| 7 | Breach runbook (HBNR 60 days, DPDP 72-hour report, state laws) and a tabletop exercise | Beta |
| 8 | Security programme: encryption, access control, ≥1-year logs, penetration test | M4 |
| 9 | Chatbot safety case: scope policy, refusal list, red-team results, published self-harm protocol, model/prompt change log | M4 |
| 10 | Form-scoring validation report and public methodology page (Apple 1.4.1) | M4 |
| 11 | Store kits: Apple organisation account, usage strings, reviewer notes; Google Health apps declaration, Health Connect declaration, web deletion URL, in-chat AI report button, target API 36 | Beta → M4 |
| 12 | Subscription compliance: affirmative-consent records, annual reminder, easy cancellation (ROSCA, CA ARL) | M4 |
| 13 | WCAG 2.2 AA audit and accessibility statement; audio + haptic + caption for every cue | M4 |
| 14 | UK: qualification memo, DPIA, complaints procedure | V1.2 |
| 15 | India: DPDP flows (notice, consent, erasure, grievance officer), dark-patterns self-audit, Hindi copy review, ASCI AI-ad labelling | V1.3 |
| 16 | EU: qualification memo, DPIA, Art. 50 notices and marking, withdrawal button, DPF/SCCs | V2 |
| 17 | B2B: BAA template, HIPAA-ready tenant, security questionnaire, Colorado AI law review | V2 |

---

## 12. Business model

### 12.1 Consumer tiers and prices

| Tier | US | UK (incl. 20% VAT) | India (incl. 18% GST) | What is included |
|---|---|---|---|---|
| **Free** | $0 | £0 | ₹0 | Camera coaching with full cues for 5 exercises (EX-01, EX-03, EX-07, EX-08, EX-09); Foundations program; food log (search, barcode, manual); medication list, dose schedule, side-effect log and reminders; the **full Safety & Context Layer** (all constraints, red flags, crisis routing, ED-safe mode); 10 coach messages + 3 meal scans/month (India 4 + 1); template debriefs; session history |
| **Premium** | **$14.99/month · $99.99/year** | £12.99 · £89.99 | ₹349 · ₹2,499 | All 10 exercises and future library; autoregulation and quality volume (IF-2); all starter programs; adaptive planner with "Why this changed"; 150 coach messages + 90 meal scans/month (India 60 + 36); LLM debriefs and weekly narration; health-platform sync; coach memory |
| **Premium+** | **$29.99/month · $179.99/year** | £24.99 · £149.99 | ₹699 · ₹4,999 | Everything in Premium + GLP-1 Strength Track (dose-cycle scheduling, protein/fibre rules, monthly camera benchmarks); clinician-shareable report (V1.2); 1.8× AI quota (270 + 160; India 108 + 64) |

Rules:
- **Trial:** 7-day free trial on annual plans only, all markets; no trial on monthly plans [R5 §9]. Post-launch experiment: 7 vs 14 days.
- **Annual discount:** Premium 44% off 12× monthly; Premium+ 50% off.
- **Price test (D-04):** $99.99 vs $119.99/year (with $19.99/month) in the first 8 weeks after launch.
- **Paywall:** soft, annual-led, inside onboarding (82–86% of H&F trials start on Day 0) with a second prompt on Days 4–7 [R5 §4]. Paywall copy is matched to search intent (+41.5% install→trial measured by Adapty) [R5 #60].
- **Fees and taxes:** Apple Small Business Program 15% [R5 #69]; Google Play 15% (10% service + 5% billing fee in US/UK/EEA from 2026-06-30) [R5 #72]. UK: £89.99 → £74.99 before VAT → £63.74 after a 15% fee. US web checkout (Stripe Billing 0.7% + card fees) from V1.2 under D-13 [R5 #73].
- **Anchors:** Fitbod $15.99/$95.99, Zing ~$19.99/$59.99, Ladder $29.99/$179.99, Google Health Premium $9.99/mo, MyFitnessPal $79.99/yr; India: cult.fit LIVE ₹449/₹1,999, Fitbod ₹399/₹1,999, Google Health Coach ₹99/mo [R5 §3], [R1 S55].

### 12.2 B2B offers (pilot hypotheses, to validate)

| Offer | Buyer | Price | Release | Conditions |
|---|---|---|---|---|
| Clinic design-partner pilot | 3 US physio, sports-medicine or obesity clinics | Free for 6 months | V1.2 | Patients share reports themselves; no PHI exchange, so no BAA needed yet |
| Partner licence | GLP-1 telehealth providers, pharma patient-support programs, Indian clinics and pharmacies | **$12** (US) or **₹149** (India) per activated member per month for a Premium+ entitlement; minimum 200 activated members; first 3 months at 50% | V1.3 | Activation codes only; partners see no user data unless the user shares a report. Healthify's Novo Nordisk India program shows the channel exists [R1 S84] |
| RepSight Clinic | Clinics (portal) | **$29 per practitioner/month + $8 per active patient/month** (Physitrack anchor: $18.99 + $8) [R5 #67](https://www.physitrack.com/physitrack-pricing) | V2 | HIPAA-ready tenant and BAA |
| Employers and insurers | Wellness programs (43% of US firms with 5,000+ workers cover GLP-1s for weight loss) [R5 #21] | No list price; outcome-linked pilots | After V2 | Colorado AI law and wellness-incentive review first |
| Trainers / gyms (white-label) | — | Not planned before 2028 (anchors $19/coach, $299/location [R5 §9]) | Backlog | — |

---

## 13. Unit economics

Model: 36-month cohort per acquired paying subscriber, US list prices, Opus 5.5 on all routes. Contribution = net revenue − AI − infrastructure − free-user AI serving cost. Script: `scratchpad/scripts/canon_calc.py` (self-check: it reproduces R5's base case within 0.03 of LTV/CAC).

### 13.1 Assumptions

| Input | Pessimistic | Base | Optimistic | Source |
|---|---|---|---|---|
| Install → paid (all channels) | 1.8% | 3.0% | 6.0% | H&F median 2.9%, upper quartile 6.2% [R5 #56] |
| Share of installs that are paid | 75% | 60% | 40% | Assumption |
| Paid cost per install | $4.50 | $3.00 | $2.50 | Apple Ads H&F $1.89–$3.97 per download [R5 #59](https://adapty.io/blog/apple-ads-benchmarks-2026/) |
| **CAC per payer** (CPI × paid share ÷ conversion) | **$187.50** | **$60.00** | **$16.67** | Arithmetic |
| Annual-plan share of payers | 50% | 65% | 72% | [R5 #56, #58] |
| Premium+ share of payers | 5% | 10% | 15% | Assumption |
| Monthly renewals (1st / 2nd / 3rd / each later month) | 45/65/75/82% | 55/70/78/85% | 60/75/82/88% | [R5 #56] |
| Annual renewals (1st / 2nd) | 25/45% | 33/55% | 45/65% | [R5 #56] |
| Refunds | 6% | 4% | 3% | [R5 #56, #57] |
| Store fee, year 1 / later | 30% / 15% | 15% / 15% | 12% / 12% (web blend) | [R5 #69, #70, #72] |
| AI per active Premium month | $4.84 (tokens 2×) | **$2.42** | $1.45 (tokens 0.6×) | §13.2 |
| Premium+ AI | 1.8× Premium | 1.8× | 1.8× | §9.7 |
| Share of months active (annual / monthly payers) | 75% / 100% | 60% / 100% | 50% / 100% | [R5 §10] |
| Infrastructure per paying month | $1.08 (10k-MAU scale) | $0.35 (100k-MAU scale) | $0.20 | §16.2 |
| Free + trial AI per install (first 30 days) | $0.40 | $0.20 | $0.10 | §13.2 |

### 13.2 AI cost per active user (explicit token math, Opus 5.5 prices from §9.2)

| Task | Calls per active Premium month | Tokens per call | Opus cost per call (tokens × $/1M) | Opus / month | Sonnet / month | Haiku / month |
|---|---|---|---|---|---|---|
| Coach chat turn | 30 | 5,000 cache read + 1,000 in + 800 out | 5,000×0.20 + 1,000×4 + 800×20 = $0.0010 + $0.0040 + $0.0160 = **$0.0210** | $0.630 | $0.330 | $0.017 |
| Safety classifier (every turn + 20% post-check) | 36 | 1,000 cache read + 500 in + 150 out | $0.0002 + $0.0020 + $0.0030 = **$0.0052** | $0.187 | $0.097 | $0.005 |
| Prompt-cache writes (new chat sessions) | 10 | 5,000 written | 5,000×5.00 = **$0.0250** | $0.250 | $0.125 | $0.006 |
| Post-workout debrief | 12 | 3,000 in + 600 out | $0.0120 + $0.0120 = **$0.0240** | $0.288 | $0.144 | $0.007 |
| Weekly plan narration | 4 | 8,000 in + 2,500 out | $0.0320 + $0.0500 = **$0.0820** | $0.328 | $0.164 | $0.008 |
| Meal-photo analysis | 45 | 2,600 in (image incl.) + 300 out | $0.0104 + $0.0060 = **$0.0164** | $0.738 | $0.369 | $0.019 |
| **Active Premium user-month** | | | | **$2.42** | **$1.23** | **$0.06** |
| Active Premium+ user-month (×1.8) | | | | $4.36 | $2.21 | $0.11 |
| Free monthly active user (3 turns + 3 classifier calls + 1 cache write + 1 meal scan) | | | | $0.12 | $0.062 | $0.003 |
| Per install, first 30 days (4 turns + 4 classifier + 1.5 cache writes + 1 scan = $0.159, plus 7% of installs × 7-day trial at Premium usage = $0.040) | | | | **$0.20** | — | — |

Output tokens include adaptive thinking; measure real usage in beta (R3 notes thinking-token billing must be measured). India usage = 40% of US: $0.97 per active Premium month on Opus, $0.02 on Haiku.

### 13.3 Results (US)

| Scenario | CAC | Free-user AI per payer | Net revenue 12 / 36 months | Contribution 12 / 36 months | **LTV36/CAC** | Payback month |
|---|---|---|---|---|---|---|
| Pessimistic | $187.50 | $22.22 | $48.49 / $64.82 | −$11.44 / −$6.33 | **<0** | Never |
| **Base** | **$60.00** | **$6.67** | **$73.64 / $105.07** | **$48.40 / $71.72** | **1.20** | **13** |
| Optimistic | $16.67 | $1.67 | $85.94 / $140.86 | $73.40 / $121.37 | **7.28** | 1 (annual paid upfront) |

**What moves the base case** (one change at a time, LTV36/CAC): Sonnet 5.5 on all routes 1.43 · Haiku 5.5 on all routes 1.66 (both only if D-02 evals pass) · $119.99/yr and $19.99/mo Premium 1.52 · R5's draft $89.99/yr 1.08 · 60% organic installs 1.79 · top-quartile conversion (6.2%) 2.59 · tokens 2× 0.83 · Apple's standard 30% first-year fee 0.98.

**AI as a share of net revenue (Opus, base):** an annual Premium payer nets $81.59 in year 1 ($99.99 × 0.96 × 0.85) and costs $17.42 of AI (21%; Sonnet 11%). A monthly Premium payer nets $12.23/month and costs $2.42 when active (20%; Sonnet 10%). Including free users, AI is 30% of net revenue at both 10k and 100k MAU (§16.2).

**Readout:** the US base case is positive but below the 1.5 gate (KPI-17). Paid acquisition therefore stays in test mode (the launch-window Apple Ads test in §16.3) until LTV36/CAC ≥1.5 holds for two consecutive months. The levers, in order: organic and creator share, the D-04 price test, conversion work on paywall and onboarding, then D-02 routing.

### 13.4 India (₹2,499/year, ₹349/month; prices incl. 18% GST; 15% store fee; ₹94/$)

Assumptions: AI usage 40% of US; install → paid 1.2%; CPI $0.30; 50% organic; annual first renewal 22% (IN/SEA median) and second 45%; monthly renewals 46/65/75/82%; refunds 7.7% [R5 #56, #61]; free + trial AI per install $0.08 (Opus).

| Scenario | CAC | Net revenue 36 months | Contribution 36 months | LTV36/CAC |
|---|---|---|---|---|
| Base, Opus | $12.50 | $19.53 | $1.34 | **0.11** |
| Base, Haiku 5.5 (only if D-02 English + Hindi evals pass) | $12.50 | $19.53 | $15.04 | **1.20** (payback month 1) |
| Pessimistic, Opus (0.6% conversion, $0.50 CPI) | $41.67 | $19.53 | −$5.33 | <0 |
| Optimistic, Opus (2.0% conversion, $0.20 CPI) | $5.00 | $19.53 | $4.00 | 0.80 |

India therefore launches (D-08) only with an eval-approved cheaper model for India routes or a signed partner licence (§12.2); otherwise as Free + partner codes.

---

## 14. Timeline & milestones

### 14.1 Phases

| Phase | Weeks | Dates | Goal | Main outputs |
|---|---|---|---|---|
| 0. Foundations & CV spike | W1–W6 | 2026-11-02 → 2026-12-11 | Prove the camera pipeline; set up foundations | Repo, CI, Expo dev builds; PoseEngine prototype (iOS + Android); device-lab benchmarks; D-05; golden-video harness; backend skeleton; Claude client + guard skeleton; clinical lead and counsel engaged; consent forms and data protocol; recording sessions start W5 |
| 1. MVP build | W7–W18 | 2026-12-14 → 2027-03-05 (W8–W9 at half capacity) | Build the 41 MVP features; alpha from 2027-02-15 | 10 exercises, 6 medication classes and ~20 KB cards; recording sessions to W15 (2027-02-12); labelling ≈600 h; thresholds v1 |
| 2. Closed beta | W19–W28 | 2027-03-08 → 2027-05-14 | Calibrate, validate, build the 9 Beta and 4 V1.0 features, finish compliance | 15 classes and ~45 cards; validation study W20–W26; D-02 evals; paywall; compliance pack; release candidate |
| 3. Launch | W29–W31 | 2027-05-17 → 2027-06-04 | Store review and US iOS launch | Submission 2027-05-17; **launch Tuesday 2027-06-01** |
| 4. V1.x expansion | W32–W55 | 2027-06-07 → 2027-11-19 | Android, UK, India, V1.4 features | V1.1–V1.4 |
| 5. V2 build | W56–W74 | 2027-11-22 → 2028-03-31 | B2B platform, learned CV models, EU | V2.0 on 2028-03-28 |

### 14.2 Milestones and exit criteria

| M | Date (week) | Milestone | Exit criteria |
|---|---|---|---|
| M1 | 2026-12-11 (W6) | CV spike gate | Full model ≥30 FPS on Tier A and ≥20 FPS on Tier B over 20 min; p95 frame-to-overlay ≤150 ms on Tier B; iOS packaging proven in a release build (D-05); golden-video harness in CI; squat and push-up counted exactly on ≥90% of 50 golden sets; clinical lead and counsel contracted; recording protocol and releases approved; D-01, D-03, D-06, D-07, D-10, D-11, D-12, D-17 decided |
| M2 | 2027-03-05 (W18) | MVP complete, alpha exit | All 41 MVP features done; KPI-01 met on Tier A golden sets for all 10 exercises; zero never-rule failures on eval suite v1; 6 classes and ~20 KB cards clinician-signed; ≈7,200 set clips labelled; crash-free ≥99%; alpha feedback triaged |
| M3 | 2027-04-09 (W23) | Beta quality gate | Every GA cue meets KPI-02 on the held-out set; KPI-03/KPI-04 met on Tiers A and B; red-flag recall ≥0.98; D-02 route evals complete (decision by 2027-04-23); dose-cycle scheduling and quality volume live; 9 V1.0 classes drafted |
| M4 | 2027-05-14 (W28) | Launch readiness | All Beta-exit KPI targets (§15) met; validation report and methodology page published; 15 classes and ~45 cards signed; compliance checklist items 1–13 done (§11.6); penetration-test findings fixed; paywall and subscription compliance live; store kits complete; release candidate frozen |
| M5 | 2027-06-01 (W31) | **V1.0 public launch** (US, iOS) | App Review approved; on-call and support rota live; launch Apple Ads test running |
| M6 | 2027-07-13 (W37) | V1.1 Android (US) | KPI-01–KPI-04 met on the Android matrix; Play Health apps and Health Connect declarations approved |
| M7 | 2027-08-24 (W43) | V1.2 UK + sharing | UK checklist item 14 done; F-027, F-074, F-094, F-120 live; 3 design-partner clinics signed |
| M8 | 2027-10-05 (W49) | V1.3 India | D-08 passed; Hindi UI and cues; F-063 and F-123 live; India quotas; DPDP flows and checklist item 15 done |
| M9 | 2027-11-16 (W55) | V1.4 | IF-6 (US only, D-09), IF-7, F-015, F-028, F-064, F-075 and HealthKit import live |
| M10 | 2028-03-28 (W74) | V2.0 | F-029, F-121, F-122 live; HIPAA-ready tenant; EU entry (D-15) and es-US; checklist items 16–17 done |

### 14.3 Team plan by phase (FTE unless noted)

| Role | Phase 0 | Phase 1 | Phase 2 | Phases 3–4 (V1.x) | Phase 5 (V2) |
|---|---|---|---|---|---|
| CEO / product owner (founder) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Founding engineer, mobile + backend (works with Claude Code) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Founding ML/CV engineer (PoseEngine, rules engine, data) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Product designer (contract) | 0.5 | 0.5 | 0.5 | 0.3 | 0.3 |
| QA / device-lab tester (contract) | — | 0.5 (from W15) | 0.5 | 0.5 | 0.5 |
| Growth & community lead | — | — | 0.5 | 1.0 | 1.0 |
| Second engineer (mobile/backend) | — | — | — | 1.0 from V1.1, if funded | 1.0 |
| Support | — | — | — | 0.5 from launch | 0.5 |
| Clinical reviewers: PharmD clinical lead, sports-medicine physician, registered dietitian, physiotherapist (contract hours) | ~20 h | ~140 h | ~110 h | ~20 h/month | ~20 h/month |
| ML data labellers (certified coaches, contract hours) | Session coaches | ≈600 h | ≈230 h | As needed | As needed |
| Privacy / regulatory counsel (fixed fee) | US package | — | Launch review | UK (V1.2), India (V1.3) | EU, HIPAA/B2B |

---

## 15. KPIs

Targets by phase: **Beta exit** = M4 (2027-05-14); **V1.0+90 d** = 2027-08-30; **By V2.0** = 2028-03-28. "—" = not measurable in that phase.

| KPI | Name | Definition | Beta exit | V1.0+90 d | By V2.0 |
|---|---|---|---|---|---|
| KPI-01 | Rep-count accuracy | Sets counted exactly / within ±1 vs adjudicated labels, guided setup, frozen test set | ≥95% / ≥99% on Tiers A–B (iOS) | Same on iOS + Android; Tier C ≥90% exact | ≥97% exact, all tiers |
| KPI-02 | Cue precision / recall | Per GA cue on the held-out set (production labelled sample after launch) | ≥0.90 / ≥0.70 | ≥0.90 / ≥0.70 | ≥0.92 / ≥0.75 |
| KPI-03 | Cue latency | p95 rep end → audio cue | ≤500 ms (A–B), ≤700 ms (C) | Same | Same |
| KPI-04 | Pose FPS | Sustained over 20 min | A ≥30, B ≥20, C ≥15 (Lite) | Same incl. Android | Same |
| KPI-05 | Assessed-rep rate | Counted reps whose form was assessed (not abstained) | ≥85% | ≥90% | ≥92% |
| KPI-06 | Camera session completion | Camera sessions started that log ≥1 counted set | ≥80% | ≥85% | ≥88% |
| KPI-07 | Never-rule failures | Failures in the safety eval suite and weekly production sample | 0 | 0 | 0 |
| KPI-08 | Red-flag recall | On the clinician-labelled red-flag set (Emergency, Urgent, Crisis) | ≥0.98 | ≥0.98 | ≥0.99 |
| KPI-09 | Medication-answer grounding | Coach answers touching medicines that render a cited KB card or the fixed referral template | 100% | 100% | 100% |
| KPI-10 | Download → trial (D30, US) | Trials started ÷ downloads within 30 days | — | ≥9% | ≥12% |
| KPI-11 | Trial → paid (US) | Trials converting to paid | — | ≥38% | ≥42% |
| KPI-12 | Download → paid (D35, US) | Payers ÷ downloads within 35 days | — | ≥3.0% | ≥4.5% |
| KPI-13 | Refund rate | Refunded ÷ gross transactions | — | ≤4% (US) | ≤4% US, ≤8% India |
| KPI-14 | First annual renewal | Annual subscribers renewing at month 12 | — | — | First cohort renews from 2028-06-01; target ≥33% |
| KPI-15 | AI cost share | LLM spend ÷ net revenue | — | ≤30% | ≤15% (after D-02 and quota tuning) |
| KPI-16 | AI cost per install | Free + trial AI in the first 30 days | ≤$0.25 (measured on beta) | ≤$0.20 | ≤$0.12 |
| KPI-17 | LTV36/CAC | §13 model re-run monthly on live cohort data | — | ≥1.2 | ≥1.5 before paid scaling |
| KPI-18 | Strength-session frequency | Median camera-verified strength sessions per active payer per week | ≥2.0 | ≥2.0 | ≥2.5 |
| KPI-19 | GLP-1 strength-dose adherence | Active GLP-1 Track users with ≥2 camera-verified sessions/week in ≥3 of 4 weeks | ≥45% | ≥50% | ≥60% |
| KPI-20 | Autoregulation acceptance | Stop-set prompts accepted | ≥50% | ≥60% | ≥65% |
| KPI-21 | Week-4 retention | New users active in week 4 (assumption-based target; no verified benchmark) | ≥25% | ≥30% | ≥35% |
| KPI-22 | Crash-free sessions | Sentry crash-free session rate | ≥99.5% | ≥99.7% | ≥99.8% |
| KPI-23 | Privacy integrity | Unauthorised disclosures, or clips/keypoints uploaded without the matching consent | 0 | 0 | 0 |
| KPI-24 | Store rating | Average App Store / Play rating | — | ≥4.5 | ≥4.6 |
| KPI-25 | Explained plan changes | Plan changes showing a "Why this changed" card with data or rule citation | 100% | 100% | 100% |
| KPI-26 | Report sharing | Premium+ users sharing ≥1 clinician report within 90 days (from V1.2); design-partner clinics | — | — | ≥10%; ≥3 design-partner clinics signed by V1.2 (M7) and still active at V1.4 |
| KPI-27 | Discomfort continuity | Users logging discomfort who complete a modified session within 7 days (from V1.4) | — | — | ≥70% |
| KPI-28 | Cue-learning effect | Median reps-to-correction vs fixed-cue control (from V1.4) | — | — | ≥20% lower |

---

## 16. Budget

### 16.1 Phase 0 → V1.0 build budget (2026-11-02 → 2027-05-31, 7 months, USD)

Assumption: India-based core team at $5,000 per loaded FTE-month (D-03, D-17). Pre-launch marketing ($22,000) sits in §16.3, not here.

| Line item | Lean AI-assisted | Standard team |
|---|---|---|
| Core team | 3 founders × 7 months × $5,000 = $105,000 | 9 FTE (PM, designer, 2 mobile, native CV, backend, ML/data, QA, engineering lead) × 7 × $5,000 = $315,000 |
| Product designer, contract 0.5 FTE × 7 × $3,500 | $12,250 | In core team |
| QA / device tester, contract 0.5 FTE × 4 × $2,000 | $4,000 | In core team |
| Growth & community lead | 0.5 FTE × 3 × $3,000 = $4,500 | 1.0 FTE × 3 × $3,000 = $9,000 |
| Clinical reviewers, 270 h × $150 (PharmD 100 h, sports-medicine MD 50 h, RD 60 h, DPT 60 h) | $40,500 | $40,500 |
| Privacy / regulatory counsel (US package) | $25,000 | $25,000 |
| ML data program (120 participants, session coaches, ≈830 h labelling) | $35,000 | $35,000 |
| Validation study (Kinovea, linear position transducer, 30 participants) | $6,000 | $6,000 |
| Claude API for development and evals ($1,000/month) | $7,000 | $7,000 |
| Claude Code seats (3 × $200/month) | $4,200 | — |
| Cloud before launch ($800/month; standard + $4,000 more environments) | $5,600 | $9,600 |
| SaaS tools before launch ($600/month) | $4,200 | $4,200 |
| Device lab (9 phones, several bought used) | $6,000 | $6,000 |
| Entity, trademark searches and filings (US + India) | $5,000 | $5,000 |
| Penetration test | $8,000 | $8,000 |
| WCAG 2.2 AA audit | $4,000 | $4,000 |
| **Subtotal** | **$276,250** | **$474,300** |
| Contingency 15% | $41,438 | $71,145 |
| **Total to V1.0** | **$317,688** | **$545,445** |
| Same plan if people are US-based ($16,000 per loaded FTE-month; every people line × 3.2, other lines unchanged) | $635,835 | $1,365,165 |

### 16.2 Monthly run-rate after launch (infrastructure + AI + tools; people and marketing excluded)

Assumptions: paying subscribers = 12% of MAU; 75% of payers active in a month; Premium+ = 10% of payers; blended net revenue $9.48 per paying subscriber-month (65% annual; after 15% store fee and 4% refunds); AI per §13.2.

| Line | 10k MAU | 100k MAU |
|---|---|---|
| Paying subscribers / active payers / free MAU | 1,200 / 900 / 9,100 | 12,000 / 9,000 / 91,000 |
| Infrastructure (AWS): ECS Fargate, RDS PostgreSQL Multi-AZ, ElastiCache Valkey, ALB/NAT, S3/CloudFront, CloudWatch, WAF/KMS/Secrets, RxNav host, backups/DR, staging | $1,300 | $4,200 |
| AI, Opus 5.5 on all routes (default) | $3,444 | $34,442 |
| Tools: RevenueCat (1% of revenue above $2.5k), PostHog, Sentry, EAS, Claude Code seats, GitHub/Figma/Workspace, device cloud, SES/support desk; at 100k add Cognito (~$500) and a paid nutrition API (~$300) | $1,700 | $5,100 |
| **Total run-rate** | **$6,444** | **$43,742** |
| Net revenue (reference) | $11,379 | $113,792 |
| AI as % of net revenue (KPI-15) | 30% | 30% |
| AI if D-02 moved every route to Sonnet 5.5 / Haiku 5.5 | $1,758 / $86 | $17,579 / $864 |
| Infrastructure per paying subscriber-month (feeds §13.1) | $1.08 | $0.35 |

AWS figures are estimates to confirm with the AWS pricing calculator at M1.

### 16.3 Marketing budget by phase

| Phase | Dates | Budget | Use |
|---|---|---|---|
| Phases 0–1 | 2026-11-02 → 2027-03-05 | $6,000 | Landing page and waitlist $1k; content and SEO $2k; GLP-1 community outreach and alpha recruitment $3k |
| Phase 2 (beta) | 2027-03-08 → 2027-05-14 | $16,000 | Beta recruitment ads $6k; tester incentives $6k; nano-creator seeding $4k |
| Launch window | 2027-05-17 → 2027-08-27 | $66,000 | Apple Ads CAC test $30k (~9,400–12,000 downloads at $2.51–$3.20 each [R5 #59]); micro-creators $24k [R5 #63]; launch PR and assets $6k; Custom Product Pages and ASO $2k; Android launch $4k |
| V1.x growth | 2027-09-01 → 2028-02-29 | $84,000 base ($14k/month: US $8k organic, creator and referral; UK $3k; India $3k incl. partner development) | Paid scaling up to $26k/month ($156,000 total) only after KPI-17 ≥1.5 for two consecutive months |
| **Total to V2 start** | | **$172,000** ($244,000 if the gate is met) | |

---

## 17. Risks

| R | Category | Description | P | I | Mitigation | Owner |
|---|---|---|---|---|---|---|
| R-01 | Regulatory | Medication features or chat answers drift into device/CDS territory (dosing, thresholds, treatment); our AUP reading proves wrong [R4 §1, R3 #1] | M | H | Fixed clinician rules; never-rules + eval gate; banned-claims linter; counsel memo per market; confirm AUP reading with Anthropic before 2026-11-12; regional flags (F-103) | CEO + counsel |
| R-02 | CV accuracy | Missed reps or wrong cues on mid/low-tier phones or messy rooms destroy trust, as Metric and Tempo reviews show [R1 S31, S14] | M | H | Guided setup, confidence gating, Beta labels, golden-video CI, device lab, Lite fallback; QuickPose fallback (D-12) | ML/CV engineer |
| R-03 | Data | Collection or labelling slower or costlier than planned; no commercial datasets exist [R2 §3.1] | M | H | Recording from W5; US/India split; BlazePose Heavy pre-labels; cut MVP to 6 GA exercises if M2 is at risk | ML/CV engineer |
| R-04 | AI safety | Unsafe advice, eating-disorder harm (Tessa) or a missed red flag [R3 #68] | L | H | Deterministic guards, verbatim cards, ED-safe mode, change control, helplines, weekly production sampling | CEO + clinical lead |
| R-05 | AI cost | Thinking tokens or usage above the model push AI above 30% of revenue | M | M | Quotas, caching, low effort on non-chat routes, cost dashboard (F-115), D-02 evals | Tech lead |
| R-06 | Competition | Google, Peloton, MyFitnessPal, Sword or Oura/WHOOP copy the combination [R1 §7] | H | M | Speed; clinician-reviewed rule library; labelled dataset; partner channels; medication-aware positioning | CEO |
| R-07 | Unit economics | LTV36/CAC stays below 1.5 (base 1.20) or turns negative (pessimistic) | M | H | KPI-17 gate on paid scaling; organic, creator and B2B channels; price test; paywall conversion work | CEO + growth |
| R-08 | Technical dependency | iOS MediaPipe packaging: CocoaPods trunk read-only from 2026-12-02, 1.1.x not on CocoaPods, RN SwiftPM experimental [R2 §4.4] | M | M | D-05 at M1; vendored xcframework fallback | ML/CV engineer |
| R-09 | App stores | Rejection over health claims (1.4.1), AI consent (5.1.2(i)) or Play health declaration | M | M | Checklist items 5, 10, 11; reviewer notes; methodology page | CEO |
| R-10 | Privacy / security | Breach or unauthorised disclosure (HBNR, MHMDA, DPDP) | L | H | No ad SDKs; encryption; least privilege; pen test; runbook and tabletop; minimised LLM payloads | Tech lead |
| R-11 | Biometric law | Face points or stored movement series treated as biometric or gait data (BIPA, CUBI, WA, COPPA) [R4 §2.3] | L | H | Landmarks 0–10 dropped natively; keypoint series off by default; written retention schedule | Tech lead + counsel |
| R-12 | Clinical operations | Reviewer availability; KB goes stale after label changes | M | M | Retainers; DailyMed/openFDA change tickets; `review_due`; 12-month re-review | Clinical lead |
| R-13 | Third parties | NLM RxNav funding lapse; 2021-era pose model; Anthropic policy or pricing changes | M | M | Self-hosted RxNav-in-a-Box; Apple Vision fallback; pinned model IDs with eval gates; quarterly vendor review | Tech lead |
| R-14 | Liability | A user is injured following a program or cue | L | H | ACSM screening; conservative progression; "stop if you feel pain"; no injury-prevention claims; product-liability and E&O insurance before Beta | CEO |
| R-15 | India | Low conversion and Opus costs make India negative; DPDP and AI-counselling rules [R5 §10.3] | H | M | D-08 gate; India quotas; partner licences; Hindi evals | CEO |
| R-16 | Team capacity | Three-person core; key-person risk; schedule slip | M | H | Claude Code with CLAUDE.md; contractors; scope-cut order IF-7 → IF-6 → F-028 → F-064; second engineer from V1.1 | CEO |
| R-17 | Consumer law | Subscription rules (ROSCA, CA ARL, EU withdrawal, India dark patterns) | L | M | F-093; consent records; annual reminder; easy cancellation | CEO + counsel |
| R-18 | Chatbot laws | SB 243-style duties applied to us (reporting from 2027-07-01, private right of action) [R4 #67] | M | M | Build to the strictest version; D-14 | Counsel |

---

## 18. Owner decisions still open

Writers use the recommended default until the owner decides.

| D | Decision | Recommended default | Deadline |
|---|---|---|---|
| D-01 | Product name and trademark | "RepSight", after knockout searches (USPTO, UKIPO, India TMR) and App Store/Play name checks; fallbacks "FormSight", "SteadyRep" | 2026-11-20 |
| D-02 | Model routing per route | Opus 5.5 on every route at V1.0; run the §9.2 evals at M3; move a route only if all four criteria pass, in the order meal parsing → free-tier chat → India routes; paid chat, plan narration and the safety classifier stay on Opus | 2027-04-23 (V1.0); 2027-08-13 (India) |
| D-03 | Legal entity and team location | US Delaware C-corp (Apple/Google organisation accounts, US contracts, Small Business Program) with an Indian subsidiary if the team is India-based (the budget assumes it is) | 2026-11-13 |
| D-04 | Launch price | $14.99/month and $99.99/year Premium; test $119.99/year with $19.99/month for the first 8 weeks after launch; readout 2027-07-30 | 2027-05-07 |
| D-05 | iOS MediaPipe packaging | Pin the `MediaPipeTasksVision` 1.0.0 pod (existing pods keep resolving after trunk goes read-only); vendor the xcframework via a config plugin if the pod fails in a release build; revisit SwiftPM when RN support is stable | 2026-12-11 (M1) |
| D-06 | Anthropic data terms | Apply for ZDR now; consumer organisation without a BAA; a separate HIPAA-ready organisation only for B2B at V2 | 2026-11-27 |
| D-07 | Clinical lead | US-licensed PharmD as clinical lead for medication rules; sports-medicine physician as medical advisor; RD and DPT reviewers | 2026-11-13 |
| D-08 | India go/no-go | Launch 2027-10-05 only if D-02 approves a cheaper model for India routes (English + Hindi) or ≥1 partner licence is signed; otherwise Free + partner codes only | 2027-08-13 |
| D-09 | IF-6 Comfort-Range Training | Ship US-only in V1.4 after a counsel memo confirms the wellness framing; other markets only after a qualification-memo update | 2027-09-15 |
| D-10 | Nutrition database | fatsecret Premier Free (if eligible: under US$1M revenue and under US$1M raised) + USDA FDC + Open Food Facts; fallback Edamam ($69/month tier) [R3 #67] | 2026-12-04 |
| D-11 | Data-collection location | 60 US + 60 India participants | 2026-11-20 |
| D-12 | CV fallback (build vs buy) | Build PoseEngine; evaluate the QuickPose SDK only if M1 gates fail | 2026-12-11 |
| D-13 | US web checkout | Stripe Billing + RevenueCat Web at V1.2, US only, after counsel reviews the ROSCA/CA ARL flows; no India web billing before 2028 | 2027-07-01 |
| D-14 | Companion-chatbot law posture | Treat SB 243-style duties as applicable: AI disclosure, crisis protocol, annual-report readiness | 2027-05-14 |
| D-15 | EU entry | V2.0 in Ireland (en-IE) and Germany (de-DE) with an eu-central-1 cell; Premium €14.99/month and €99.99/year, Premium+ €29.99 and €179.99 (incl. VAT) | 2027-12-01 |
| D-16 | GLP-1 wording in marketing | Tier stays "Premium+", program "GLP-1 Strength Track"; "built for people using GLP-1 medicines" only after counsel review; never in the app name | 2027-03-26 |
| D-17 | Budget scenario and funding | Lean scenario ($317,688 to V1.0) with an India-based team; raise enough for 18 months of runway including launch marketing | 2026-11-06 |

---

## 19. Glossary

| Term | Meaning |
|---|---|
| 1RM | One-repetition maximum |
| ACSM | American College of Sports Medicine |
| Assessed rep | A counted rep whose required joints passed the visibility gate, so its form was evaluated |
| AUP | Anthropic Usage Policy (new version effective 2026-11-12) |
| BAA | Business associate agreement under HIPAA |
| BlazePose GHUM | Google's pose model behind MediaPipe Pose Landmarker (Lite, Full, Heavy) |
| CAC | Customer acquisition cost per paying subscriber |
| CDS | Clinical decision support (FDA guidance, 2026-01-06) |
| Constraint set | The class-level rule effects the engine applies to a user's plan (e.g., RPE mode, tendon-protect) |
| DPDP | India's Digital Personal Data Protection Act 2023 and Rules 2025 |
| DPIA | Data protection impact assessment |
| ED-safe mode | Eating-disorder-safe mode: hides calories, weight, BMI and deficits |
| Form drift | A new GA error or a ROM drop that appears during a set |
| GA / Beta cue | GA cues speak a correction; Beta cues show a labelled soft tip and never a verdict |
| GLP-1 RA / GIP | Glucagon-like peptide-1 receptor agonist / glucose-dependent insulinotropic polypeptide |
| Golden video | A recorded, labelled clip replayed in CI to catch regressions |
| HBNR | FTC Health Breach Notification Rule |
| Hysteresis | Separate enter and exit thresholds for a movement phase, so pauses do not create phantom reps |
| KB card | Clinician-approved knowledge-base text with sources, reviewer and review date |
| LTV36 | Contribution per payer over 36 months (net revenue − AI − infrastructure − free-user AI) |
| MAU | Monthly active users |
| MDSW | Medical device software (EU MDR) |
| MHMDA | Washington's My Health My Data Act |
| OBO / MAE / PCK | Off-by-one rep-count accuracy / mean absolute error / percentage of correct keypoints |
| One Euro filter | Speed-adaptive low-pass filter used to smooth keypoints |
| Quality volume | Load × reps counted only for assessed reps without a GA error |
| RIR / RPE | Reps in reserve / rating of perceived exertion |
| ROM | Range of motion |
| RxNorm / RxCUI / RxClass | NLM drug vocabulary / its concept identifier / its drug-class mapping |
| SPL | Structured product labeling (FDA drug label) |
| STEADI | CDC toolkit whose functional tests include the 30-second chair stand |
| Strength-dose adherence | Share of users with ≥2 camera-verified strength sessions per week in ≥3 of 4 weeks |
| VBT / velocity loss | Velocity-based training / percentage drop in concentric rep speed versus the best early rep of the set |
| Wellness (general) | FDA category for low-risk products that make no disease, diagnosis or treatment claims |
| ZDR | Zero data retention arrangement with Anthropic |

*End of canon.*

# RepSight spec pack

RepSight (working name, see decision D-01) is a phone-only AI strength coach for iOS and Android. It checks your form through the phone camera in real time, and an AI coach plans each session around your nutrition and the medicines you take, within safety rules that clinicians review. This folder holds everything needed to build it. The research is current as of October 2026.

## The short answer to the original idea

- **Camera form correction and a fitness/diet chatbot already exist.** Peloton IQ, Tonal, Zing, Kemtai, Google Health Coach, WHOOP Coach and the MyFitnessPal AI Coach all ship them ([04 §1](04-innovative-features.md)). They cannot be the unique selling point on their own.
- **What we found no one doing** is the closed loop. RepSight sees every rep, adapts the next set and session to what it saw, and adjusts the training plan (never the medicine) to the medicines you list. We found no consumer app doing this, especially for people on GLP-1 weight-loss medicines who want to keep their strength.
- **Seven innovative features (IF-1 to IF-7)** carry that difference, each checked for novelty with sources ([04](04-innovative-features.md)).

## The documents

| File | Answers | Main readers |
|---|---|---|
| [01-business-requirements-document.md](01-business-requirements-document.md) | What we build, for whom, and why. Objectives, personas, every feature with functional requirements (FR) and acceptance criteria, non-functional requirements (NFR), business rules, success criteria | Founders, investors, product, QA |
| [02-technical-specification.md](02-technical-specification.md) | How it works. Architecture, pinned tech stack, the on-device camera pipeline and exercise rules language, ML and data plan, AI coach and safety layer, API, database schema, security, infrastructure, testing | Engineers, Claude Code |
| [03-product-roadmap-and-strategy.md](03-product-roadmap-and-strategy.md) | When and how we win. Phases and milestones, feature prioritisation, competitors, go-to-market, acquisition, unit economics, budget, risks, KPIs | Founders, investors, growth |
| [04-innovative-features.md](04-innovative-features.md) | What makes RepSight different. The honest uniqueness check and a deep dive on each innovative feature: benefit, novelty evidence, complexity, metrics, safe wording | Founders, product, investors |
| [05-build-playbook.md](05-build-playbook.md) | How Claude Code builds it. Repo layout, setup, conventions, epics E0–E15 with tasks and acceptance criteria, test gates, human checkpoints, copy-paste prompts | Claude Code, engineers |
| [../CLAUDE.md](../CLAUDE.md) | Standing instructions Claude Code loads automatically in this folder | Claude Code |
| [research/](research/) | The six research briefs with their sources (R1–R6), and the decision record the documents were written from (`00-product-canon.md`) | Anyone checking a fact |

The documents are long because they are meant to be built from. Each one starts with a summary and a table of contents.

## Reading order

- **Founders and investors (about 30 minutes):** 01 §1 Executive Summary, then 04 §1, then 03 §1 Strategy on a Page, §7 Business Model & Financial Plan and §8 Budget.
- **Engineers:** 02 §1–3, then 05 §1–6, then the epic you are working on.
- **Claude Code:** `CLAUDE.md` → 05 §1–2 → the current epic in 05 §6 → the sections of 01 and 02 that the epic cites.

## Starting the build with Claude Code

1. Open this folder (`GYM.V1`) in Claude Code. `CLAUDE.md` loads automatically.
2. Complete the human-only steps first: accounts, legal entity, and the decisions below (05 §4.3, §8).
3. Paste the epic E0 prompt from 05 §9.1. Then go epic by epic. Claude Code keeps `docs/PROGRESS.md` and `docs/DECISIONS.md` up to date as it goes.
4. Claude Code stops and asks at every human checkpoint (05 §8), for example clinical sign-off, legal text, store submission and payments.

## Decisions needed in the first weeks

| Decision | Recommended default | Deadline |
|---|---|---|
| Confirm with Anthropic that clinician-approved medication cards plus fixed safety routing fit its usage policy that takes effect on 2026-11-12 | Ask before that date (canon §11.6 item 1) | 2026-11-12 |
| D-17 Budget scenario and funding | Lean plan, India-based core team, about $318k to V1.0; raise for 18+ months of runway (03 §8) | 2026-11-06 |
| D-03 Legal entity | US Delaware C-corp with an Indian subsidiary | 2026-11-13 |
| D-07 Clinical lead | US-licensed PharmD (Doctor of Pharmacy) leads the medication rules; a sports-medicine physician advises | 2026-11-13 |
| D-01 Product name | "RepSight" after trademark and app-store checks | 2026-11-20 |
| D-06 Anthropic data terms | Apply for zero data retention now | 2026-11-27 |

All 17 open decisions (D-01 to D-17) are listed with their defaults in 01 §16 and 03 §12.

## Please read before relying on this pack

- Market numbers, prices and the financial model are **estimates**. Their assumptions are stated where they are used.
- Facts were checked as of **October 2026**. Library versions are pinned and must be checked again at build time (02 §3).
- Regulatory positioning follows the research, but it is **not legal advice**. Counsel reviews it before launch (01 §15).
- Medication rules, safety templates and nutrition limits are **drafts until clinicians sign them off**. Code ships them behind `CLINICAL_REVIEW_REQUIRED` gates (05 §2).

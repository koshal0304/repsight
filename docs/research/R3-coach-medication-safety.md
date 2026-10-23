# R3: AI Coach for Fitness, Diet and Medication. Knowledge Base, Clinical Safety and LLM Platform Facts (as of 2026-10-17)

Scope: the in-app fitness, diet and medication coach. Evidence: the R3 digest (159 tool results, 2026-10-16) plus 12 re-checks (2026-10-17). Citations are inline as [n](URL). Confidence: **H** = primary source, **M** = secondary or partial, **L** = weak. ★ = set only by the user's prescriber.

## Summary

- **Policy sets the product line.** Anthropic's Usage Policy (effective **2026-11-12**) treats "recommending, starting, stopping, or adjusting a treatment or medication, including dose" and "interpreting an individual's symptoms… to triage… advise on treatment risks or side effects" as High-risk Medical recommendations. These need qualified-person review before delivery, plus AI disclosure. The policy excludes "Wellness content… nutrition, or exercise" and "applying a fixed rule, formula, or algorithm where the model exercises no judgment" [[1]](https://www.anthropic.com/aup) (H). → Medication guidance is clinician-authored fixed rules and verbatim cards. The LLM explains and routes; it never judges.
- The AUP in force today (2025-09-15) already requires professional review and session-start disclosure for "medical guidance". It bans glamorizing "disordered eating and unhealthy or compulsive exercise" [[2]](https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944) (H).
- **15-class medication matrix (§2),** anchored to 2025–2026 FDA labels, ADA 2026, CDC, AHA and NHS. Examples: beta-blockers → RPE instead of HR zones; SGLT2 inhibitors → no keto plans; anticoagulants → no contact sports; fluoroquinolones → tendon-protect mode; seven heat-sensitive classes → heat alerts.
- **GLP-1/GIP:** in STEP 1, 38% of a 13.6 kg loss was lean mass. The 2025 ACLM/ASN/OMA/TOS advisory recommends strength training at least 3×/week, at least 150 min/week aerobic, and 1.2–1.6 g/kg/day protein (or 80–120 g/day) [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/) (H). No GLP-1-specific ACSM consensus was found (M). Oral options: the Wegovy pill (approved 2025-12-22) and Foundayo/orforglipron (2026-04-01) [[43]](https://api.fda.gov/drug/drugsfda.json?search=products.brand_name:%22WEGOVY%22)[[44]](https://api.fda.gov/drug/drugsfda.json?search=products.brand_name:%22FOUNDAYO%22) (H).
- **Diabetes (ADA 2026):** at least 150 min/week aerobic, 2–3 resistance sessions/week, and sitting broken up every 30 min. Insulin and secretagogue users "may need to ingest carbohydrates if pre-exercise glucose levels are <90 mg/dL" [[11]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690188) (H). The coach prompts and educates; it never adjusts insulin.
- **Never rules:** no dose changes or stopping medicines; no dose calculators [[83]](https://developer.apple.com/app-store/review/guidelines/); no thyroid hormone for weight loss [[42]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c903249-69e9-4168-a9d1-22e6c2c1eb22); no pro-eating-disorder or "compensatory exercise" content [[1]](https://www.anthropic.com/aup).
- **Drug data:** RxNorm/RxNav, openFDA and DailyMed are enough for the MVP. NLM's free interaction API was discontinued around 2024-01-02 [[54]](https://lhncbc.nlm.nih.gov/RxNav/) (H). Interaction screening needs a commercial database and moves toward clinical decision support, so defer it.
- **Nutrition data:** USDA FDC (CC0) and Open Food Facts (ODbL) for the MVP. fatsecret Premier Free or Edamam ($14–$299/month) for NLP and photo logging. IFCT 2017 needs NIN permission, and Nutritionix is partner-only [[60]](https://fdc.nal.usda.gov/api-guide/)[[62]](https://openfoodfacts.github.io/openfoodfacts-server/api/)[[67]](https://platform.fatsecret.com/api-editions)[[66]](https://developer.edamam.com/food-database-api)[[63]](https://www.nin.res.in/ifct_book.html)[[65]](https://www.nutritionix.com/business/api).
- **We must build crisis routing ourselves:** US 988; UK 999 / NHS 111 / Samaritans 116 123; India Tele-MANAS 14416 and 112; ANAD and Beat for eating disorders. Claude's ThroughLine banner is documented only for Claude's own apps [[10]](https://support.claude.com/en/articles/13171706-crisis-helpline-support-in-claude) (M).
- **Tessa lesson:** a generative "upgrade" advised a tester to keep a 500–1,000 kcal/day deficit, and NEDA disabled Tessa on 2023-05-30 [[68]](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea) (H). → Change control, an eating-disorder-safe mode, numeric floors, human helplines.
- **Age:** launch 18+. Anthropic's consumer services are 18+ [[9]](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers). Products serving minors need age verification, moderation and audits [[8]](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors). COPPA compliance has been required since 2026-04-22 [[84]](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm). India's DPDP duties start around 2027-05 (M).
- **Evaluation:** HealthBench (5,000 conversations, 262 physicians) [[75]](https://arxiv.org/abs/2505.08775), a custom red-team set, and an LLM judge calibrated to clinicians. In MedHELM, an LLM jury reached ICC 0.47, versus 0.43 between clinicians [[77]](https://arxiv.org/abs/2505.23802). Threat model: OWASP LLM Top 10 (2025) and Agentic Top 10 (2026).
- **Anthropic platform:**
  - No training on API data by default.
  - Deletion within 30 days; flagged content kept up to 2 years.
  - ZDR by approval.
  - A HIPAA-ready API via self-serve BAA: per organization, permanent, and it blocks Batch, Files and compaction.
  - No PHI in JSON schemas.
  - `inference_geo` is `global` or `us` only (US costs 1.1×), and storage is US-only, so there is no India or EU residency [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)[[4]](https://platform.claude.com/docs/en/manage-claude/data-residency)[[6]](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)[[7]](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-training) (H).
- **Architecture (§5):** deterministic guards; RAG over a versioned, clinician-reviewed knowledge base with citations; strict tools; consented memory; verbatim card rendering; the safety eval on every change.

## 1. Policy and regulatory frame: what the coach may say

| Source (status) | What it says | Implication for the coach | Conf. |
|---|---|---|---|
| Anthropic AUP, new version, effective 2026-11-12 [[1]](https://www.anthropic.com/aup) | **High-risk "Medical":** "diagnosing a condition; recommending, starting, stopping, or adjusting a treatment or medication, including dose; interpreting an individual's symptoms or test results to triage, provide a diagnosis, advise on treatment risks or side effects, or create a treatment plan".<br>**Human review:** a qualified person (licensed where law requires) must "meaningfully review… before it is delivered".<br>**Disclosure:** clear AI disclosure (no need to name Claude).<br>**Excluded:** general education "without applying it to the individual's circumstances"; "Wellness content, such as education on sleep, stress, nutrition, or exercise"; "applying a fixed rule, formula, or algorithm where the model exercises no judgment about the individual". | Medication statements come only from clinician-approved cards chosen by deterministic rules. Personalized medical questions (dose, side effects, symptoms) get a fixed "ask your prescriber/pharmacist" reply or go to a clinician-review queue. | H (text); M (our reading) |
| AUP previous version, effective 2025-09-15, in force until 2026-11-12 [[2]](https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944) | **Healthcare scope:** "healthcare decisions, medical diagnosis, patient care, therapy, mental health, or other medical guidance".<br>**Wellness:** "Wellness advice (e.g., advice on sleep, stress, nutrition, exercise, etc.) does not fall under this category".<br>**Requirements:** professional review "prior to dissemination"; AI disclosure "at the beginning of each session".<br>**Prohibited:** glamorizing "self-harm, including disordered eating and unhealthy or compulsive exercise". | The same design satisfies both versions. | H |
| AUP 2026-11-12: chatbots, eating disorders, bodies, emotions [[1]](https://www.anthropic.com/aup) | **Chatbots:** disclose AI "at the beginning of each chat session or in the product interface".<br>**Eating disorders:** bans pro-ED content, including "methods for restriction, purging, or compensatory exercise".<br>**Bodies:** bans "harmful idealization of body weight, shape, or type, including shaming, ranking, or critiquing people's bodies".<br>**Emotion recognition:** bans emotion-recognition systems "except for medical or safety reasons". | A persistent "AI coach" label. The camera form-correction feature must never comment on body shape or size. No mood-from-face features. | H |
| FDA General Wellness guidance, Final, Jan 2026 [[81]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices); CDS guidance, Final, Jan 2026 [[82]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software) | The wellness exclusion applies only to software "unrelated to the diagnosis, cure, mitigation, prevention, or treatment of a disease or condition". | Keep the MVP to wellness plus education. Get regulatory counsel before any interaction checker, dosing or symptom-triage feature. | H (status); M (applicability) |
| Apple App Review Guidelines 1.4.1/1.4.2 (updated 2026-06-08) [[83]](https://developer.apple.com/app-store/review/guidelines/) | **1.4.1:** medical apps get "greater scrutiny" and should "remind users to check with a doctor".<br>**1.4.2:** drug dosage calculators must come from a manufacturer, hospital, university, insurer, pharmacy or other approved entity, or be FDA-approved. | No dose calculators. Add in-app "check with your doctor" reminders. | H |
| California AB 489 (in effect 2026-01-01) [[88]](https://psychology.ca.gov/laws_regs/ab489_advisory.pdf)[[89]](https://www.cmadocs.org/newsroom/news/view/ArticleId/51003/CMA-sponsored-bill-to-protect-patients-from-misleading-AI-chatbots-signed-into-law) | AI must not present health advice as coming from a licensed professional. Bans misleading titles, post-nominal letters, or phrases implying clinical authority. Licensing boards enforce it, per violation. | The persona must not use "Dr.", "RD", "PT", "nurse" or "prescribe". | M |
| California SB 243 (signed 2025-10-13; effective 2026-01-01) [[86]](https://www.gunder.com/en/news-insights/insights/client-insight-california-sb-243-new-compliance-requirements-for-operators-of-ai-companion-chatbots)[[87]](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and-accoun.html) | Duties for "companion chatbot" operators:<br>• AI disclosure<br>• suicide/self-harm crisis protocols<br>• break reminders every 3 hours for known minors<br>• annual reporting from 2027-07-01<br>• private right of action: the greater of actual damages or $1,000 per violation | It is unverified whether a task-focused coach counts as a "companion chatbot"; ask counsel. Build the crisis protocol regardless. | M |
| FTC Health Breach Notification Rule (2024 amendments) [[85]](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule) | Vendors of personal health records must notify consumers after breaches of unsecured data; media notice applies at 500 or more people. | Breach runbook needed. | H |

## 2. Medication ↔ exercise knowledge base by drug class

**Governance:** every row needs physician or pharmacist sign-off, plus an exercise physiologist or dietitian. Label facts come from current FDA labels (openFDA `effective_time` pulled 2026-10-16; DailyMed links). "Coach rule" is our product rule, not a guideline.

| Class (examples) | Exercise-relevant facts (source, conf.) | Coach rule: education + plan constraint | Escalate / hard stop |
|---|---|---|---|
| **Beta-blockers** (metoprolol, atenolol, propranolol) | **Heart-rate targets (M):** AHA says slowed HR may mean the target heart rate needs to "adjust"; a clinician sets it with a stress test, or use the talk test [[19]](https://www.heart.org/en/health-topics/consumer-healthcare/medication-information/how-do-beta-blocker-drugs-affect-exercise).<br>**Max HR (M):** beta-blockade can cut max HR by 20–30% [[21]](https://bjsm.bmj.com/content/31/2/114).<br>**RPE (M):** ACSM material uses RPE for people on beta-blockers: 12–13 = moderate, 14–16 = vigorous [[20]](https://acsm.org/wp-content/uploads/2025/02/Exercising-Your-Way-to-Lowering-Your-Blood-Pressure-handout.pdf).<br>**Label (H):** may "mask early warning signs" of hypoglycemia; abrupt cessation may exacerbate ischemia [[25]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a46cbf09-20e3-4f0d-ab41-221f60fde068).<br>**Heat (H):** decreased sweating and fainting risk [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html). | Turn off HR-zone prescriptions; use RPE or the talk test. Use HR targets only if the user's clinician supplied them ★. Add hypoglycemia education if the user has diabetes. Turn on heat alerts. | Never suggest stopping or skipping a dose. Chest pain or fainting → emergency template. |
| **Other antihypertensives** (amlodipine; lisinopril, losartan; nitrates; alpha-blockers) | **CDC (H):** lower BP raises "risk of fainting and falls"; ACE inhibitors and ARBs reduce thirst; nitrates worsen hypotension [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html).<br>**Lisinopril label (H):** "excessive perspiration and dehydration may lead to an excessive fall in blood pressure" [[26]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aa5d68e7-c2b9-41eb-ade4-2cd57edc1533).<br>**Cool-down (M):** an ACSM-derived summary says alpha-blockers, CCBs and vasodilators may drop BP too far if exercise stops abruptly, so extend the cool-down [[22]](https://www.ideafit.com/acsm-onexercise-and-hypertension); ACE suggests 5–10 min [[23]](https://www.acefitness.org/continuing-education/certified/september-2024/8709/exercise-programming-for-clients-who-have-hypertension/). | A mandatory 5–10 min graded cool-down; "rise slowly" prompts after floor work; hydration prompts in heat. | Dizziness or syncope → stop + template. Severe or uncontrolled BP → clinician clearance [[22]](https://www.ideafit.com/acsm-onexercise-and-hypertension). |
| **Diuretics** (furosemide, HCTZ) | **CDC (H):** "Electrolyte imbalance", volume depletion, reduced thirst, fainting and falls [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html).<br>**Furosemide label (H):** dehydration and hypokalemia. Warning signs include thirst, weakness, "muscle pains or cramps", hypotension and arrhythmia [[27]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=dba00759-87b4-4ecf-998e-ba03ed3d2f1a). | Hydration plan, heat alerts and cramp check-ins. No potassium or electrolyte supplement advice ★. | Cramps with weakness or palpitations → urgent template. |
| **Insulin and secretagogues** (insulin glargine, glipizide) | **ADA 2026 (H):** hypoglycemia risk if dose or carbs are not adjusted. Users "may need to ingest carbohydrates if pre-exercise glucose levels are <90 mg/dL (<5.0 mmol/L)"; the approach "should be individualized" [[11]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690188).<br>**Glipizide label (H):** hypoglycemia is more likely "after severe or prolonged exercise", with low intake, alcohol, or several glucose-lowering drugs, and is harder to recognize on beta-blockers [[29]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00729e82-150a-464a-abe7-a3319721fbdb).<br>**Insulin label (H):** monitor glucose more often when physical activity changes; regimen changes only "under close medical supervision" [[28]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0ad21db3-2b1c-4ed9-a687-bdd6a74d0aae). | Pre-workout glucose prompt, a "carry fast carbs" checklist, a post-workout check-in, and the ADA card verbatim. Carb or insulin adjustments only from the user's own diabetes plan ★. | Never change insulin or sulfonylurea doses. Reported lows or symptoms → hypoglycemia template (the clinical lead sets thresholds). |
| **SGLT2 inhibitors** (empagliflozin, dapagliflozin) | **Jardiance label (H):** ketoacidosis can occur with glucose "less than 250 mg/dL". Precipitants include "reduced caloric intake, ketogenic diet… volume depletion, and alcohol"; volume-depletion warning [[30]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=59ed43d9-b4e0-72a2-e063-6394a90a327d).<br>**ADA 5.26 (H):** educate on DKA, provide ketone tools, "discourage a ketogenic eating pattern" [[11]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690188). | Block keto and very-low-carb templates, prolonged fasts and aggressive deficits. Stress hydration on long or hot sessions. | Nausea, vomiting, abdominal pain, malaise or shortness of breath (label list) → urgent template. |
| **GLP-1 RA and GIP/GLP-1** (semaglutide injection and pill, tirzepatide, orforglipron) | **Labels (H):** acute kidney injury "due to volume depletion" after GI adverse events; hypoglycemia with insulin or a secretagogue [[31]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f5e548d0-cc79-4c34-a3f5-e20a5b8b6564)[[32]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=487cd7e7-434c-4925-99fa-aa80b1cc776b)[[33]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8ac446c5-feba-474f-a103-23facb9b5c62).<br>**Wegovy (H):** "Monitor for depression or suicidal thoughts" [[31]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f5e548d0-cc79-4c34-a3f5-e20a5b8b6564).<br>Lean-mass evidence: §2.1. | Lean-mass protection on automatically (§2.1); GI-friendly meals, hydration, and an intake-floor flag. | Persistent vomiting or diarrhea with dizziness or low urine → urgent. Suicidal language → crisis flow. |
| **Statins** (atorvastatin) | **Label (H):** myopathy and rhabdomyolysis. Risk is higher at age 65+, with uncontrolled hypothyroidism, renal impairment, interacting drugs, or higher doses. Patients should "promptly report unexplained muscle pain, tenderness, or weakness, particularly if accompanied by malaise or fever" [[34]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d9adb9e4-c495-9530-e5e3-7e3b01d53e4c).<br>**MedlinePlus (H):** causes include statins and "severe exertion"; signs include dark or cola-colored urine [[46]](https://medlineplus.gov/ency/article/000473.htm). | Check-ins separating normal soreness (DOMS) from red flags; a conservative ramp after a statin start or dose increase (product rule; clinician to confirm). | Dark urine, unexplained pain or weakness, or fever → urgent template. |
| **Anticoagulants and antiplatelets** (apixaban, rivaroxaban, warfarin; aspirin, clopidogrel) | **Eliquis label (H):** "serious, potentially fatal, bleeding"; patients "may bruise or bleed more easily"; boxed warning against premature discontinuation [[35]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a454cd24-0c6d-46e8-b1e4-197388606175).<br>**NHS (M):** non-contact sports (running, cycling, tennis) are fine with protective gear; avoid contact sports such as martial arts and kickboxing (the rivaroxaban page adds football, rugby, hockey, horse riding) [[47]](https://www.nhs.uk/medicines/apixaban/common-questions-about-apixaban)[[48]](https://www.nhs.uk/medicines/rivaroxaban/common-questions-about-rivaroxaban/).<br>**CDC:** antiplatelets reduce superficial vasodilation in heat [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html). | Exclude contact, combat and high-fall-risk drills from plans. Helmet and protective-gear prompts. Flag co-use with an SSRI [[40]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7d598f1a-6c76-458a-a155-7a6a0743a2d3). | Head impact, a fall, bleeding that won't stop, blood in vomit or cough, or severe headache → emergency template [[47]](https://www.nhs.uk/medicines/apixaban/common-questions-about-apixaban). |
| **Fluoroquinolones** (levofloxacin, ciprofloxacin) | **Boxed warning (H):** tendinitis and rupture, most often the Achilles, "within hours or days… or as long as several months after completion".<br>**Risk factors:** age over 60, corticosteroids, transplants. "Strenuous physical activity" raises risk independently.<br>**Action:** "rest at the first sign of tendinitis" [[36]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5a65b2bc-9edc-f193-e063-6394a90a0104). | Tendon-protect mode during the course and for a post-course window (length set by the clinical lead): no plyometrics, sprints, or heavy eccentric lower-limb loading. | Tendon pain or swelling → stop the activity and contact the prescriber. |
| **Systemic corticosteroids** (prednisone) | **Label (H):** osteoporosis risk. Encourages "weight-bearing exercise for 30-60 minutes daily" and "a weight-bearing exercise program that maintains muscle mass". Acute myopathy at high doses. May raise glucose. Tendon rupture risk rises when combined with fluoroquinolones [[37]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0062fcc7-aa08-4990-9d33-d798725907f1). | Encourage weight-bearing and resistance training (label-supported); glucose prompts for users with diabetes; steroid plus fluoroquinolone → tendon-protect mode. | New weakness → clinician. |
| **ADHD stimulants** (amphetamine, methylphenidate) | **Labels (H):** mean BP rises about 2–4 mmHg and HR about 3–6 bpm; sudden death reported with structural cardiac abnormalities [[38]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0)[[39]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=effd952d-ac94-47bb-b107-589a4934dcca).<br>**CDC (H):** "Increased body temperature" [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html). | Heat and hydration alerts; warn against stacking caffeine or pre-workout stimulants; flag that HR zones may need recalibrating. | Chest pain, fainting or palpitations → emergency template. |
| **Antidepressants** (SSRIs/SNRIs, TCAs) | **Sertraline label (H):** hyponatremia (headache, confusion, weakness, unsteadiness, which may lead to falls), with higher risk in elderly, diuretic or volume-depleted users. Bleeding risk rises with NSAIDs, antiplatelets or anticoagulants [[40]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7d598f1a-6c76-458a-a155-7a6a0743a2d3).<br>**CDC:** TCAs decrease sweating. The page is internally inconsistent about SSRIs/SNRIs [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html). | Heat alerts. Never suggest NSAIDs. Hyponatremia-symptom check on long endurance sessions. | Confusion or unsteadiness → urgent. Self-harm language → crisis flow. |
| **Anticholinergics and heat-impairing drugs** (diphenhydramine, promethazine, doxylamine, oxybutynin; also antipsychotics, lithium, topiramate) | **CDC (H):** "Decreased sweating" and "Impaired thermoregulation". Antipsychotics impair sweating; lithium carries a "Risk for toxicity in setting of dehydration"; topiramate decreases sweating [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html).<br>**Oxybutynin label (H):** "heat prostration (fever and heat stroke due to decreased sweating)" in high temperatures [[41]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1a08a16a-f16d-4ef1-95bb-6943bcae0737). | Weather and heat-index warnings for outdoor sessions; suggest indoor or cooler slots. | Heat-illness signs → emergency template. |
| **Thyroid hormone** (levothyroxine) | **Boxed warning (H):** "should not be used for the treatment of obesity or for weight loss". Overtreatment raises HR and can cause arrhythmia (atrial fibrillation), angina, and lower bone mineral density [[42]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c903249-69e9-4168-a9d1-22e6c2c1eb22).<br>**CDC:** "Excessive sweating" [[24]](https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html). | Refuse "thyroid for fat loss" requests. Otherwise train normally. | Palpitations or chest pain → template. |
| **Supplements** (caffeine, creatine, pre-workouts) | See §2.2. | Ingredient checks and a daily caffeine counter. | Unlawful ingredient → warning card. |

### 2.1 GLP-1/GIP, obesity and diabetes: lean mass, protein, resistance training

**Lean mass (as reported in the 2025 joint advisory; H)** [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/):
- STEP 1: a 13.6 kg mean loss was 8.3 kg fat (62%) and 5.3 kg lean (38%); muscle was about 20% of the weight lost.
- SURMOUNT-1 (pooled doses): total lean mass fell by 8.5 absolute percentage points.
- Modeling without structured strength training: muscle is 10–15% (women) or 20–25% (men) of the weight lost.

**Joint advisory (ACLM/ASN/OMA/TOS; *Obesity*, Aug 2025, and *AJCN*, Jul 2025; H)** [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/). GLP-1s "should be prescribed together with a structured exercise program":
- **Exercise:** strength training at least 3×/week, plus at least 150 min/week of moderate aerobic activity.
- **Protein:**
  - The RDA is 0.8 g/kg/day; 1.2–1.6 g/kg/day is "proposed during active weight reduction".
  - Actual body weight "can significantly overestimate" needs. Instead, use 1.5 g/kg of lean mass (needs body-composition data) or 80–120 g/day.
  - Never below 0.4–0.5 g/kg/day; avoid prolonged intake at or above 2 g/kg/day.
- **Micronutrients:** risk rises below 1,200 kcal/day (women) or 1,800 (men).
- **GI tactics:** small meals every 3–4 h for nausea; avoid large or high-fat meals.

**ADA 2026 Section 5 (doi 10.2337/dc26-S005, released 2025-12-08; H)** [[11]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690188)[[12]](https://diabetes.org/newsroom/press-releases/american-diabetes-association-releases-standards-care-diabetes-2026):
- On obesity pharmacotherapy, "additional emphasis on meeting physical activity guidelines, particularly muscle-strengthening activities, is warranted".
- **5.23:** prevent "protein insufficiency and micronutrient deficiencies" (grade E).
- **5.36:** at least 150 min/week over at least 3 days, with no more than 2 consecutive days off. 75 min of vigorous or interval training may suffice for fitter people.
- **5.37:** 2–3 resistance sessions/week on non-consecutive days.
- **5.34:** break up sitting every 30 min.

**Consensus status (M):**
- No GLP-1-specific ACSM consensus was found (searches 2026-10-16/17). ukActive (Dec 2025) recommends resistance training "to limit muscle loss" but notes little protocol research [[15]](https://www.ukactive.com/wp-content/uploads/2025/12/GLP-1-medications-and-muscle-mass-preservation.-Implications-and-recommendations.pdf).
- ACSM's 2026 resistance-training Position Stand (healthy adults; 137 systematic reviews; H) gives dose parameters [[16]](https://pubmed.ncbi.nlm.nih.gov/41843416/):
  - strength improves with loads of at least 80% 1RM, 2–3 sets, and at least 2 sessions/week
  - hypertrophy improves with at least 10 sets/week
  - training to failure did not consistently matter
- ACSM *GETP* 12th edition was published in 2025 [[18]](https://www.tomlinsons-online.com/p-39931785-acsms-guidelines-for-exercise-testing-and-prescription.aspx) (M; text not reviewed).

**Product rule (★ RD or physician sign-off):** "Lean-mass protection" is on for every GLP-1/GIP user:
- Beginner-scaled resistance training 3×/week.
- A clinician-approved protein formula (g/kg of adjusted weight, capped at 80–120 g/day).
- A flag, not an auto-plan, when logged intake falls below 1,200 or 1,800 kcal.
- No protein targets for users who report kidney disease; refer them to a dietitian.

### 2.2 Supplements

- **Caffeine (H):**
  - FDA: 400 mg/day is "not generally associated with negative effects" for most adults. Rapid intake of about 1,200 mg ("less than 1/2 teaspoon of pure caffeine") can be toxic. Pregnant or breastfeeding users should ask a provider [[49]](https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much).
  - ISSN 2021: ergogenic at 3–6 mg/kg, usually taken 60 min pre-exercise; 9 mg/kg brings a "high incidence of side-effects" [[50]](https://pubmed.ncbi.nlm.nih.gov/33388079/).
  - **Rule:** a 400 mg/day adult cap that counts pre-workouts. Never suggest pure or powdered caffeine [[52]](https://www.fda.gov/food/dietary-supplements/information-select-dietary-supplement-ingredients-and-other-substances).
- **Creatine (H):**
  - ISSN 2017: up to "30 g/day for 5 years" is "safe and well-tolerated" in healthy people and several patient groups [[51]](https://pubmed.ncbi.nlm.nih.gov/28615996/).
  - **Rule:** education only. Kidney disease, nephrotoxic drugs or diuretics, or pregnancy → clinician ★.
- **Pre-workouts (H):** the FDA directory (2026-05-01) [[52]](https://www.fda.gov/food/dietary-supplements/information-select-dietary-supplement-ingredients-and-other-substances) lists:
  - DMAA, DMHA, BMPEA, phenibut and methylsynephrine as not dietary ingredients
  - DMBA as needing new-dietary-ingredient notification
  - SARMs and tianeptine as the subject of safety communications
  - ephedrine alkaloids as banned since 2004
  - **Rule:** a "never recommend" list, label-scan warnings, and stimulant-stack checks against ADHD drugs and beta-blockers.

## 3. Drug and nutrition data sources (licensing, cost, MVP vs later)

| Source | Use | Licence / cost / limits (as of 2026-10-16) | Phase | Conf. |
|---|---|---|---|---|
| **RxNorm / RxNav** (NLM) | Normalize medicines to RxCUI; RxClass maps classes | Free. Max 20 req/s per IP (100 with a UTS key). No licence needed except SNOMED CT in RxClass. Apps must state "This product uses publicly available data from the U.S. National Library of Medicine (NLM)" [[53]](https://lhncbc.nlm.nih.gov/RxNav/TermsofService.html). Self-hosting via RxNav-in-a-Box [[55]](https://lhncbc.nlm.nih.gov/RxNav/APIs/index.html). | MVP | H |
| RxNav interaction API | n/a | Discontinued "on or about January 2, 2024". The site showed a funding-lapse banner on 2026-10-16, so cache or self-host [[54]](https://lhncbc.nlm.nih.gov/RxNav/). | n/a | H |
| **openFDA** | Knowledge-base evidence; label and approval monitoring | 240 req/min. 1,000/day per IP without a key; 120,000/day with one [[56]](https://open.fda.gov/apis/authentication/). Label data can lag: the Wegovy label was dated 2024-04-23 despite 2026 supplements [[31]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f5e548d0-cc79-4c34-a3f5-e20a5b8b6564)[[43]](https://api.fda.gov/drug/drugsfda.json?search=products.brand_name:%22WEGOVY%22). | MVP (backend) | H/M |
| **DailyMed** v2 | Canonical labels; `/spls/{setid}/history` | GET-only, JSON or XML. No stated cost or limits [[57]](https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm). | MVP | H |
| DrugBank | Interactions | Free academic licence only. Datasets are CC BY-NC 4.0. Commercial pricing is not public [[58]](https://go.drugbank.com/releases/latest). | Later | M |
| FDB MedKnowledge | Interactions, contraindications, dosing | SDK, **MCP server**, or web API. Pricing is not public [[59]](https://www.fdbhealth.com/solutions/medknowledge-drug-database). | Later | M |
| Medi-Span | FDB alternative | Not verified (page returned 403) | Later | L |
| **USDA FDC** | Core nutrients | CC0. Needs a data.gov key. 1,000 req/h per IP. Attribution requested [[60]](https://fdc.nal.usda.gov/api-guide/). | MVP | H |
| **Open Food Facts** | Barcodes, including India | ODbL/DbCL/CC BY-SA: attribution plus share-alike [[61]](https://world.openfoodfacts.org/terms-of-use). 15 req/min for reads, 10 req/min for search. Custom User-Agent [[62]](https://openfoodfacts.github.io/openfoodfacts-server/api/). | MVP (cache) | H |
| IFCT 2017 (ICMR-NIN) | Indian foods | 542 foods across six regions; the GitHub code is AGPL and the data licence is unstated [[64]](https://github.com/ifct2017/compositions). "All Rights Reserved" [[63]](https://www.nin.res.in/ifct_book.html). | India, with NIN permission | M |
| Nutritionix | NLP logging | Website "temporarily offline". API for "registered partners" only [[65]](https://www.nutritionix.com/business/api). | Avoid | M |
| Edamam | NLP and photo logging | $14/mo (100k calls), $69 (750k), $299 (5M), or custom. Attribution is mandatory [[66]](https://developer.edamam.com/food-database-api). | Option | H |
| fatsecret | Search, barcode, NLP, photo | **Basic:** free, 5,000 calls/day, US data, attribution required.<br>**Premier Free:** start-ups under US$1M revenue *and* under US$1M raised.<br>**Premier:** 62+ countries, 26 languages [[67]](https://platform.fatsecret.com/api-editions). | Option | H |

## 4. Safety design for the consumer health chatbot

### 4.1 Red-flag triage and escalation
- **Onboarding screen.** ACSM screening uses current activity, signs or symptoms (or known cardiovascular, metabolic or renal disease), and the intended intensity. Cardiac events "are often preceded by warning signs/symptoms" [[17]](https://pubmed.ncbi.nlm.nih.gov/26473759/) (H). Screen at onboarding and keep detecting in chat.
- **Detection:** deterministic rules plus an LLM classifier (`{flag, tier}`) map to **fixed, clinician-approved templates**, never free text. This matches the AUP fixed-rule exclusion [[1]](https://www.anthropic.com/aup) (M).
- **Tiers:**
  - **Emergency** (chest pain or fainting during exercise, head injury on an anticoagulant, heat illness, suicidal intent): stop, show the local emergency number.
  - **Urgent** (rhabdomyolysis signs, DKA signs on an SGLT2 inhibitor, tendon pain on a fluoroquinolone, persistent vomiting on a GLP-1, recurrent lows): see a clinician today.
  - **Crisis** (self-harm, eating-disorder behaviours): crisis line plus a human.
  - **Gate** (pregnancy, new diagnosis or new medicine): pause the affected features until a clinician clears them. Pregnancy stop signs (ACOG CO 804 via Tommy's): breathlessness, dizziness, chest pain, racing or irregular heartbeat [[94]](https://www.tommys.org/pregnancy-information/im-pregnant/exercise-pregnancy/when-stop-exercising-pregnancy) (M).

### 4.2 Crisis and escalation resources (verified Oct 2026)

| Region | Crisis / emergency | Eating-disorder support |
|---|---|---|
| US | **988:** call or text, or chat at chat.988lifeline.org; "available 24/7/365"; Spanish text and chat [[69]](https://988lifeline.org/) (H). Emergencies: 911 [[10]](https://support.claude.com/en/articles/13171706-crisis-helpline-support-in-claude). | **ANAD:** (888) 375-7767, Mon–Fri 9am–9pm CST, free peer support, "We do not provide therapy or anything medical" [[74]](https://anad.org/get-help/) (H). NEDA closed its helpline in 2023 [[68]](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea). |
| UK | If life is at risk: 999 or A&E. Otherwise: NHS 111 "mental health option" or Samaritans 116 123 [[70]](https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/) (H; page last reviewed 2023-04-26). | **Beat** (3–8pm Mon–Fri, plus web chat) [[73]](https://www.beateatingdisorders.org.uk/get-information-and-support/get-help-for-myself/i-need-support-now/helplines/) (H):<br>• England 0808 801 0677<br>• Scotland 0808 801 0432<br>• Wales 0808 801 0433<br>• Northern Ireland 0808 801 0434 |
| India | **Tele-MANAS:** 14416 or 1-800-891-4416 (MoHFW; numbers confirmed in the official site's code) [[71]](https://telemanas.mohfw.gov.in/) (H). Emergencies: **112**, the ERSS number; coverage varies by state, and an undated source lists 24 states/UTs [[72]](https://www.vikaspedia.in/social-welfare/women-and-child-development/emergency-response-support-system) (M). | None verified |

Claude's apps get crisis resources from "a separate detection system" (ThroughLine); the article does not mention the API [[10]](https://support.claude.com/en/articles/13171706-crisis-helpline-support-in-claude), so we build our own.

### 4.3 Eating-disorder safeguards (lessons from Tessa)
- **What happened (H)** [[68]](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea):
  - NEDA promoted Tessa while closing its helpline.
  - The studied version was rule-based: "all of the responses were pre-programmed".
  - The operator, Cass, added a generative "enhanced question and answer feature" in a "systems upgrade". NEDA says it "was never advised".
  - A tester was told to lose 1–2 lb/week and eat no more than 2,000 kcal/day with a 500–1,000 kcal/day deficit.
  - NEDA disabled Tessa on May 30, 2023.
- **Controls:**
  1. Any model, prompt, knowledge-base or vendor change re-runs the safety eval and needs clinical sign-off. Pin model IDs.
  2. An eating-disorder-safe mode hides calories, weight, BMI and deficits. It is triggered by opt-in, a clinician-chosen screener, or chat signals.
  3. No plan goes below clinician-set kcal floors (default flag 1,200/1,800 [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/)) or above a set weekly loss rate.
  4. No "burn it off" framing. No body ranking or critique, including from the camera [[1]](https://www.anthropic.com/aup).
  5. Always offer a human helpline.
  6. The UK Online Safety Act treats eating-disorder content as "primary priority content" for children and requires highly effective age assurance [[92]](https://www.gov.uk/government/publications/online-safety-act-explainer/online-safety-act-explainer)[[93]](https://www.judiciary.uk/wp-content/uploads/2025/03/2025-0139-Response-from-Department-for-Science-Innovation-and-Technology-.pdf) (M).

### 4.4 No dose changes, disclaimers, persona
- **Never rules (unit-tested):**
  - Never tell users to start, stop, skip, re-time or adjust any medicine.
  - No dose calculators [[83]](https://developer.apple.com/app-store/review/guidelines/).
  - Never encourage stopping a beta-blocker or anticoagulant [[25]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a46cbf09-20e3-4f0d-ab41-221f60fde068)[[35]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a454cd24-0c6d-46e8-b1e4-197388606175).
  - Insulin changes only under medical supervision [[28]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0ad21db3-2b1c-4ed9-a687-bdd6a74d0aae).
- **Disclosure:** AI disclosure at each session start plus a persistent label [[1]](https://www.anthropic.com/aup); "check with your doctor" reminders [[83]](https://developer.apple.com/app-store/review/guidelines/); no professional titles [[88]](https://psychology.ca.gov/laws_regs/ab489_advisory.pdf).
- **Out-of-scope medication questions** get a fixed "ask your prescriber/pharmacist" reply, plus an export for the user's clinician.

### 4.5 Age gating
- **Anthropic (H):** its consumer services are "restricted to users 18 years and older" [[9]](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers). API products open to minors need age verification, moderation, monitoring, education, a child-safety prompt and public COPPA compliance, and Anthropic audits them (guidelines updated 2026-03-16) [[8]](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors).
- **US COPPA (H):** the amendments took effect 2025-06-23; compliance has been required since 2026-04-22 [[84]](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm).
- **India DPDP Rules (M):** notified 13 or 14 Nov 2025. They require verifiable parental consent, with most duties starting about 18 months later, around 2027-05 [[90]](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/)[[91]](https://www.ey.com/en_in/insights/cybersecurity/transforming-data-privacy-digital-personal-data-protection-rules-2025).
- **Decision:** 18+ with an age gate and an 18+ store rating. A user signalling they are under 18 → coach locked, resources shown.

### 4.6 Evaluation
- **HealthBench** (May 2025): 5,000 multi-turn conversations, 262 physicians, 48,562 rubric criteria. The Consensus subset has 34 dimensions; on the Hard subset the top score was 32% at release. Open source [[75]](https://arxiv.org/abs/2505.08775) (H).
- **MedHELM:** 121 tasks; an LLM jury agreed with clinicians at ICC 0.47, versus 0.43 between clinicians [[77]](https://arxiv.org/abs/2505.23802) (H).
- **MedSafetyBench:** safety measured against the AMA *Principles of Medical Ethics* [[76]](https://arxiv.org/abs/2403.03744) (H).
- **Our plan:**
  - A custom R3 red-team set (15 classes × benign, edge, red-flag, jailbreak, eating-disorder risk, minor, crisis), written with clinicians.
  - An Opus 5.5 judge scoring against per-item rubrics.
  - Clinician double-review of a stratified sample and every failure.
  - Release gate: zero never-rule or crisis-routing failures.
  - Re-run on every change; sample production weekly.

### 4.7 OWASP threat model
Sources: LLM Top 10 2025 [[78]](https://genai.owasp.org/llm-top-10/) (H) and Agentic Top 10 for 2026 (published 2025-12-09) [[79]](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/); the ASI IDs come from a secondary list [[80]](https://www.humansecurity.com/learn/blog/owasp-top-10-agentic-applications/) (M).

| Risk | Where it bites this app | Control |
|---|---|---|
| LLM01 Prompt Injection / ASI01 Goal Hijack | Open Food Facts text, user notes, synced app data | Treat tool output as data; output validator; the model cannot override rules |
| LLM02 Sensitive Information Disclosure | Medicines and conditions | Least-privilege tools, log redaction, no PHI in JSON schemas [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) |
| LLM06 Excessive Agency / ASI02 Tool Misuse | Plan edits | Tools only *propose*; rules validator plus user confirmation; no outbound messaging tools |
| LLM09 Misinformation | Health claims | RAG over the reviewed knowledge base, citations, verbatim cards |
| ASI06 Memory & Context Poisoning | Long-term memory | Memory is written only from user turns via validated tools, and the user can see it |
| ASI09 Human-Agent Trust Exploitation | A clinician-like persona | Disclosure, no professional titles |
| LLM10 Unbounded Consumption | Cost abuse | Per-user token and rate budgets |

## 5. Architecture pattern

**Pipeline:**
1. **Input guard.** Deterministic rules plus an LLM classifier (structured output). An Emergency or Crisis result returns the fixed template and stops.
2. **Context.**
   - Profile and medicines: RxCUI → RxClass → **constraint set**.
   - Retrieved knowledge-base cards, passed as `search_result` or document blocks so citations are returned.
   - Consented memory.
3. **Generation.** Model `claude-opus-5-5`, effort `medium`. Output uses `output_config.format` → `{reply_text, kb_card_ids[], plan_change_proposal?, red_flag?}`. Forced `tool_choice` and prefill are not supported, so use `tool_choice: auto` with strict tools (provided facts).
4. **Output guard.**
   - A classifier blocks medication directives in `reply_text`.
   - Numeric checks enforce kcal floors and loss rates.
   - Cards render verbatim.
   - A `refusal` stop reason → fixed fallback plus resources.
5. **Audit.** Model ID, prompt version, knowledge-base version, eval-run ID.

**Constraint engine** (clinician-owned config, not model output):

| Drug class flag | Constraint |
|---|---|
| beta-blocker | `intensity=RPE`, HR zones off |
| SGLT2 inhibitor | Block keto plans and prolonged fasts |
| anticoagulant / antiplatelet | Block contact, combat and high-fall-risk activities |
| fluoroquinolone (active course or within window) | `tendon_protect` on |
| GLP-1 / GIP | `lean_mass_program` on, protein rule, kcal-floor flag |
| insulin / secretagogue | Pre-workout glucose prompt |
| statin | Rhabdomyolysis check-ins |
| CCB / alpha-blocker / vasodilator / ACE inhibitor / ARB | Cool-down of at least 5 min |
| heat-sensitive set (§2) | Heat alerts |
| stimulant | Caffeine-stack warning |
| levothyroxine | Refuse "thyroid for weight loss" |

**Knowledge-base versioning:**
- **Card fields:** `id`, `drug_class` (RxClass), claim, adjustment, red flags, `sources[]` (URL, publisher, SPL set ID / `effective_time`), reviewer, `approved_at`, `review_due`, `status`.
- **Workflow:** author → clinical review → eval → publish. The UI shows "last reviewed".
- **Automatic review tickets** open on:
  - DailyMed SPL-history changes [[57]](https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm)
  - openFDA `effective_time` changes and new Drugs@FDA approvals [[56]](https://open.fda.gov/apis/authentication/)
  - each annual ADA release (the 2026 edition came out 2025-12-08) [[12]](https://diabetes.org/newsroom/press-releases/american-diabetes-association-releases-standards-care-diabetes-2026)

**Tools and memory:**
- Strict read tools: `get_meds`, `get_workouts`, `get_wearable_summary`, `get_food_log`. Write tools only *propose* changes.
- The Memory tool is client-side storage "where you control data retention" and is ZDR- and HIPAA-eligible [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention). Keep memory in our database with separate opt-in for health memories; users can view, edit and delete it.
- Server-side compaction is ZDR-eligible but **not** HIPAA-eligible [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention), so a HIPAA organization needs client-side summaries.

**Illustrative cost** (from the provided prices, not measured): an Opus 5.5 turn with a 10K cached prefix, 2K fresh input and 600 output tokens ≈ **$0.022** ($0.024 with `us`), excluding cache writes and thinking tokens. A Haiku 5.5 pre-screen ≈ $0.000125. Moving off Opus is a product-owner decision based on evals.

## 6. Anthropic platform facts (verified on official pages)

| Topic | Fact (as of) | Consequence | Conf. |
|---|---|---|---|
| Training | Commercial and API data is not used for training "by default". Exceptions: feedback sent to Anthropic (kept up to 5 years) or opt-in (article dated 2026-08-18) [[7]](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-training). | Don't forward user feedback to Anthropic. | H |
| Retention | Deleted "within 30 days". Flagged content is kept up to 2 years and safety scores up to 7 years (page dated 2026-07-01) [[6]](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data). Flagged data can be kept even under ZDR or HIPAA [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention). | Disclose in the privacy policy. | H |
| ZDR | Per organization, after sales approval; nothing is stored after the response. **Not covered:** Console, Managed Agents, Batch (29-day retention), Files, code execution, MCP connector. No CORS, so use a backend proxy. Safety-classifier results are still kept [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)[[5]](https://privacy.claude.com/en/articles/8956058-is-anthropic-willing-to-sign-a-business-associate-agreement-baa-with-customers-handling-protected-health-information-phi). | Request ZDR. No Batch or Files with health data. | H |
| HIPAA | BAA is self-serve (standard terms) or through sales. **Organization-level and permanent.** Ineligible features return a 400 error. Covers only the HIPAA-ready Claude API: not Bedrock or Google Cloud, Claude Platform on AWS, Foundry or Claude Code; beta features only if listed. **No PHI in JSON schemas** (cached up to 24 h) [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention). | A separate HIPAA org, only for B2B or covered-entity work. | H |
| Feature eligibility | **ZDR and HIPAA:** Messages, caching, citations, search results, structured outputs and strict tools, Memory tool, mid-conversation system messages, effort, data residency.<br>**ZDR only:** compaction, context editing, web fetch.<br>**Neither:** Batch, Files, code execution, MCP connector, Managed Agents [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention). | The coach stack is fully eligible. | H |
| Covered Models | Fable 5/5.1 and Mythos 5/5.1 need 30-day retention and are not available under ZDR. Opus, Sonnet and Haiku 5.5 are not listed [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention). | Avoid Covered Models for health chats. | H |
| Data residency | `inference_geo` is `global` (default) or `us` only, on Claude 4.6 and later. `us` costs 1.1×. Storage is `us` only. Not applicable on Bedrock or Google Cloud; Foundry uses a US Data Zone [[4]](https://platform.claude.com/docs/en/manage-claude/data-residency). | No in-region processing for India or the EU; legal review for transfers. | H |

## Recommendations for the docs

**BRD**
1. **Scope statement:** "The coach gives wellness education and medication-aware training adjustments from clinician-approved rules. It does not diagnose, dose, check interactions, or triage beyond fixed safety routing." This keeps it inside the AUP wellness and fixed-rule exclusions and the FDA wellness framing [[1]](https://www.anthropic.com/aup)[[81]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices).
2. **Clinical governance:** a named clinical lead (physician or pharmacist), a dietitian and an exercise physiologist sign off every card and rule. Re-review at least every 12 months and on any label change.
3. **Launch and KPIs:** adults-only in the US, UK and India, with region-specific crisis tables (§4.2). KPIs: zero never-rule failures; red-flag recall at or above the clinical lead's target; citation rate on medication answers.

**Technical specification**
4. **Services (§5):** safety guard, clinician-owned constraint engine (YAML), versioned knowledge base with DailyMed/openFDA monitors, RAG via `search_result` blocks and citations, Claude client, consented memory, audit log.
5. **Claude client:** `claude-opus-5-5`, effort `medium`, `output_config.format`, strict tools with `tool_choice: auto`, at most 4 cache breakpoints (policy → knowledge-base index → profile), `refusal` handling, and mid-conversation system messages for constraint updates.
6. **Platform rules:** backend proxy only (no CORS under ZDR); apply for ZDR; no PHI in schemas; no Batch or Files for user data; `inference_geo` defaults to `global`, with `us` only if contracted (+10%) [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)[[4]](https://platform.claude.com/docs/en/manage-claude/data-residency).
7. **Data model:** `medication{rxcui, rxclass_ids, start, end}` (the fluoroquinolone window comes from `end`), `ed_safe_mode`, `kcal_floor`, `kb_card{sources[], approved_at, review_due}`.

**Roadmap**
8. **MVP:** 15-class constraint engine and about 45 cards. The free drug stack, USDA FDC, Open Food Facts, and fatsecret Premier Free or Edamam. Eating-disorder-safe mode, crisis routing, eval harness.
9. **v1.x:** a clinician-review queue for personalized medication questions (the AUP human-in-the-loop path); a "share with my clinician" PDF; wearable HR for RPE calibration; IFCT after NIN permission.
10. **v2+:** a separate HIPAA-ready organization for clinic or employer partners; a commercial drug database only after FDA CDS review; teen mode only after COPPA, DPDP, Online Safety Act and SB 243 analysis.

**Innovative features:** a "med-aware autopilot" that combines RPE mode, heat-risk forecasts by medicine class and weather, tendon-protect windows, GLP-1 lean-mass protection with protein tracking, a pre-workout glucose check, and a supplement-label scanner checked against the FDA ingredient directory [[52]](https://www.fda.gov/food/dietary-supplements/information-select-dietary-supplement-ingredients-and-other-substances).

**Build Playbook (for Claude Code)**
11. Unit-test the never rules, crisis templates and constraint rules. Keep the knowledge base as versioned JSON/YAML with source URLs and `effective_time`.
12. CI runs the R3 safety eval and blocks merges on any never-rule failure or unreviewed card. Pin model IDs, feature-flag each drug class, and log model, prompt and knowledge-base versions per message.

## Unverified / conflicting

1. **Retention wording:** the Privacy Center says deletion happens "within 30 days" [[6]](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data), but the docs say conversation content "is not retained by default", except for Covered Models [[3]](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention). Assume up to 30 days unless ZDR or HIPAA readiness applies.
2. **AUP reading:** that pre-approved clinician cards satisfy the human-review rule, or the fixed-rule exclusion, is our interpretation. Confirm with Anthropic before 2026-11-12.
3. **California:** SB 243's application to a fitness coach is unconfirmed. AB 489's signing date (Oct 11 or 13, 2025) and its penalties are unverified.
4. **India:** the DPDP notification date (13 or 14 Nov 2025) and phase dates come from secondary sources, and cross-border transfer rules were not checked. Tele-MANAS's 24/7 and 20-language claims are secondary. Coverage of 112 by state is uncertain.
5. **UK:** the text of Online Safety Act s.61 was not fetched. The NHS page doesn't say whether 111's mental-health option is England-only, and its review date passed on 2026-04-26.
6. **Exercise physiology:**
   - ACSM RPE ranges and the extended cool-down come from secondary summaries; the ACSM handout returned 403.
   - GETP 12th edition was not reviewed.
   - The 2025 AHA/ACC hypertension guideline's exercise recommendations were not retrieved.
   - The AHA beta-blocker page is known only via a search summary.
7. **Excluded as weakly sourced:**
   - Delayed post-exercise hypoglycemia at 6–15 h, with sensitivity lasting 24–48 h (CDCES study guide).
   - "About 25% of GLP-1 weight loss is fat-free mass" (narrative review).
8. **GLP-1:**
   - The SURMOUNT-1 figure is as reported by the advisory (also in *AJCN* [[14]](https://pubmed.ncbi.nlm.nih.gov/40450457/)).
   - Foundayo's indication comes from news coverage [[45]](https://www.healio.com/news/endocrinology/20260401/fda-approves-orforglipron-an-oral-glp1-for-adults-with-obesity).
   - Not finding an ACSM GLP-1 statement does not prove none exists.
9. **Data vendors:**
   - Commercial pricing for DrugBank, FDB, Medi-Span and Nutritionix is not public.
   - IFCT's commercial licence is unknown, and no newer edition was found.
   - The openFDA Wegovy label (2024-04-23) may be out of date.
10. **Anthropic and legal:**
    - ThroughLine licensing and API-level crisis features are undocumented.
    - Aptible (secondary) says BAAs signed before 2025-12-02 cover the API only.
    - Whether a direct-to-consumer app needs HIPAA is for legal to decide; the FTC Health Breach Notification Rule applies either way [[85]](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule).
11. **Other:**
    - HealthBench's grader design is not in the abstract.
    - The OWASP agentic IDs come from a secondary list.
    - The CDC page contradicts itself on SSRI/SNRI sweating.
    - Opus 5.5 cache-write premiums and thinking-token billing are not in the provided facts; measure them.

## Sources

1. Anthropic Usage Policy (effective 2026-11-12) — https://www.anthropic.com/aup
2. Anthropic Usage Policy, archived (effective 2025-09-15) — https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944
3. Claude Docs: API and data retention — https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
4. Claude Docs: Data residency — https://platform.claude.com/docs/en/manage-claude/data-residency
5. Anthropic Privacy Center: BAA for PHI — https://privacy.claude.com/en/articles/8956058-is-anthropic-willing-to-sign-a-business-associate-agreement-baa-with-customers-handling-protected-health-information-phi
6. Anthropic Privacy Center: How long do you store my organization's data? — https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
7. Anthropic Privacy Center: Is my data used for training? — https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-training
8. Claude Help Center: Guidelines for organizations serving minors — https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors
9. Claude Help Center: Child safety guidance for developers — https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers
10. Claude Help Center: Crisis helpline support in Claude — https://support.claude.com/en/articles/13171706-crisis-helpline-support-in-claude
11. ADA Standards of Care in Diabetes—2026, Section 5 (doi 10.2337/dc26-S005) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12690188 (text read from the copy at https://education.weitzmaninstitute.org/sites/default/files/course/2025-12/Facilitating%20Positive%20Health%20Behaviors%20and%20Well-being%20to%20Improve%20Health%20Outcomes%20-%20Standards%20of%20Care%20in%20Diabetes-2026.pdf)
12. ADA press release: Standards of Care 2026 — https://diabetes.org/newsroom/press-releases/american-diabetes-association-releases-standards-care-diabetes-2026
13. Mozaffarian et al., Nutritional priorities to support GLP-1 therapy for obesity (joint advisory, Obesity 2025) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/
14. Same advisory, AJCN 2025 (PubMed 40450457) — https://pubmed.ncbi.nlm.nih.gov/40450457/
15. ukActive: GLP-1 medications and muscle mass preservation (Dec 2025) — https://www.ukactive.com/wp-content/uploads/2025/12/GLP-1-medications-and-muscle-mass-preservation.-Implications-and-recommendations.pdf
16. ACSM Position Stand: Resistance Training Prescription (MSSE 2026) — https://pubmed.ncbi.nlm.nih.gov/41843416/
17. Riebe et al., Updating ACSM's preparticipation health screening (MSSE 2015) — https://pubmed.ncbi.nlm.nih.gov/26473759/
18. ACSM's Guidelines for Exercise Testing and Prescription, 12th ed. (listing) — https://www.tomlinsons-online.com/p-39931785-acsms-guidelines-for-exercise-testing-and-prescription.aspx
19. AHA: How do beta blocker drugs affect exercise? — https://www.heart.org/en/health-topics/consumer-healthcare/medication-information/how-do-beta-blocker-drugs-affect-exercise
20. ACSM handout: Exercising your way to lowering your blood pressure (Feb 2025) — https://acsm.org/wp-content/uploads/2025/02/Exercising-Your-Way-to-Lowering-Your-Blood-Pressure-handout.pdf
21. Eston & Thompson, RPE with beta-blockade (BJSM 1997) — https://bjsm.bmj.com/content/31/2/114
22. IDEA Fit: ACSM on exercise and hypertension — https://www.ideafit.com/acsm-onexercise-and-hypertension
23. ACE: Exercise programming for clients who have hypertension (2024) — https://www.acefitness.org/continuing-education/certified/september-2024/8709/exercise-programming-for-clients-who-have-hypertension/
24. CDC: Heat and Medications – Guidance for Clinicians (2025-09-18) — https://www.cdc.gov/heat-health/hcp/clinical-guidance/heat-and-medications-guidance-for-clinicians.html
25. DailyMed: Metoprolol succinate ER label (eff. 2026-09-16) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a46cbf09-20e3-4f0d-ab41-221f60fde068
26. DailyMed: Lisinopril label (2026-09-10) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aa5d68e7-c2b9-41eb-ade4-2cd57edc1533
27. DailyMed: Furosemide label (2026-08-17) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=dba00759-87b4-4ecf-998e-ba03ed3d2f1a
28. DailyMed: Basaglar (insulin glargine) label (2026-06-16) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0ad21db3-2b1c-4ed9-a687-bdd6a74d0aae
29. DailyMed: Glipizide label (2026-08-27) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00729e82-150a-464a-abe7-a3319721fbdb
30. DailyMed: Jardiance label (2026-08-26) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=59ed43d9-b4e0-72a2-e063-6394a90a327d
31. DailyMed: Wegovy injection label (openFDA eff. 2024-04-23) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f5e548d0-cc79-4c34-a3f5-e20a5b8b6564
32. DailyMed: Zepbound label (2026-08-28) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=487cd7e7-434c-4925-99fa-aa80b1cc776b
33. DailyMed: Foundayo label (2026-07-29) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8ac446c5-feba-474f-a103-23facb9b5c62
34. DailyMed: Atorvastatin label (2026-09-08) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d9adb9e4-c495-9530-e5e3-7e3b01d53e4c
35. DailyMed: Eliquis label (2026-04-24) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a454cd24-0c6d-46e8-b1e4-197388606175
36. DailyMed: Levofloxacin label (2026-09-01) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5a65b2bc-9edc-f193-e063-6394a90a0104
37. DailyMed: Prednisone label (2026-09-08) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0062fcc7-aa08-4990-9d33-d798725907f1
38. DailyMed: Adderall XR label (2026-04-30) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0
39. DailyMed: Ritalin LA label (2025-09-23) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=effd952d-ac94-47bb-b107-589a4934dcca
40. DailyMed: Sertraline label (2026-09-03) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7d598f1a-6c76-458a-a155-7a6a0743a2d3
41. DailyMed: Oxybutynin label (2026-07-28) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1a08a16a-f16d-4ef1-95bb-6943bcae0737
42. DailyMed: Levothyroxine label (2026-09-10) — https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c903249-69e9-4168-a9d1-22e6c2c1eb22
43. openFDA Drugs@FDA: Wegovy (NDA218316 tablets, original approval 2025-12-22) — https://api.fda.gov/drug/drugsfda.json?search=products.brand_name:%22WEGOVY%22
44. openFDA Drugs@FDA: Foundayo (NDA220934, original approval 2026-04-01) — https://api.fda.gov/drug/drugsfda.json?search=products.brand_name:%22FOUNDAYO%22
45. Healio: FDA approves orforglipron (2026-04-01) — https://www.healio.com/news/endocrinology/20260401/fda-approves-orforglipron-an-oral-glp1-for-adults-with-obesity
46. MedlinePlus: Rhabdomyolysis (reviewed 2025-09-02) — https://medlineplus.gov/ency/article/000473.htm
47. NHS: Common questions about apixaban — https://www.nhs.uk/medicines/apixaban/common-questions-about-apixaban
48. NHS: Common questions about rivaroxaban — https://www.nhs.uk/medicines/rivaroxaban/common-questions-about-rivaroxaban/
49. FDA: Spilling the beans – how much caffeine is too much? — https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much
50. ISSN position stand: caffeine and exercise performance (2021) — https://pubmed.ncbi.nlm.nih.gov/33388079/
51. ISSN position stand: creatine supplementation (2017) — https://pubmed.ncbi.nlm.nih.gov/28615996/
52. FDA: Information on select dietary supplement ingredients (2026-05-01) — https://www.fda.gov/food/dietary-supplements/information-select-dietary-supplement-ingredients-and-other-substances
53. NLM RxNav Terms of Service — https://lhncbc.nlm.nih.gov/RxNav/TermsofService.html
54. NLM RxNav home and news (DDI API discontinuation) — https://lhncbc.nlm.nih.gov/RxNav/
55. NLM RxNav APIs overview — https://lhncbc.nlm.nih.gov/RxNav/APIs/index.html
56. openFDA: Authentication and rate limits — https://open.fda.gov/apis/authentication/
57. DailyMed web services — https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm
58. DrugBank releases and academic licence — https://go.drugbank.com/releases/latest
59. FDB MedKnowledge — https://www.fdbhealth.com/solutions/medknowledge-drug-database
60. USDA FoodData Central API guide — https://fdc.nal.usda.gov/api-guide/
61. Open Food Facts terms of use — https://world.openfoodfacts.org/terms-of-use
62. Open Food Facts API documentation — https://openfoodfacts.github.io/openfoodfacts-server/api/
63. ICMR-NIN: IFCT 2017 book page — https://www.nin.res.in/ifct_book.html
64. ifct2017/compositions (GitHub) — https://github.com/ifct2017/compositions
65. Nutritionix business API — https://www.nutritionix.com/business/api
66. Edamam Food Database API — https://developer.edamam.com/food-database-api
67. fatsecret Platform API editions — https://platform.fatsecret.com/api-editions
68. NPR: An eating disorders chatbot offered dieting advice (2023-06-08) — https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea
69. 988 Suicide & Crisis Lifeline — https://988lifeline.org/
70. NHS: Where to get urgent help for mental health — https://www.nhs.uk/nhs-services/mental-health-services/where-to-get-urgent-help-for-mental-health/
71. Tele-MANAS (MoHFW) — https://telemanas.mohfw.gov.in/
72. Vikaspedia: Emergency Response Support System (112) — https://www.vikaspedia.in/social-welfare/women-and-child-development/emergency-response-support-system
73. Beat: Helplines — https://www.beateatingdisorders.org.uk/get-information-and-support/get-help-for-myself/i-need-support-now/helplines/
74. ANAD: Get help — https://anad.org/get-help/
75. HealthBench (arXiv 2505.08775) — https://arxiv.org/abs/2505.08775
76. MedSafetyBench (arXiv 2403.03744) — https://arxiv.org/abs/2403.03744
77. MedHELM (arXiv 2505.23802) — https://arxiv.org/abs/2505.23802
78. OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/
79. OWASP Top 10 for Agentic Applications for 2026 — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
80. HUMAN Security: OWASP Top 10 for Agentic Applications (list) — https://www.humansecurity.com/learn/blog/owasp-top-10-agentic-applications/
81. FDA: General Wellness – Policy for Low Risk Devices (Jan 2026) — https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices
82. FDA: Clinical Decision Support Software (Jan 2026) — https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software
83. Apple App Review Guidelines (updated 2026-06-08) — https://developer.apple.com/app-store/review/guidelines/
84. Federal Register: COPPA Rule amendments (2025-04-22) — https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm
85. FTC: Health Breach Notification Rule — https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule
86. Gunderson Dettmer: California SB 243 — https://www.gunder.com/en/news-insights/insights/client-insight-california-sb-243-new-compliance-requirements-for-operators-of-ai-companion-chatbots
87. Jones Walker: SB 243 mandates companion AI safety — https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and-accoun.html
88. California Board of Psychology: AB 489 advisory — https://psychology.ca.gov/laws_regs/ab489_advisory.pdf
89. CMA: AB 489 signed into law — https://www.cmadocs.org/newsroom/news/view/ArticleId/51003/CMA-sponsored-bill-to-protect-patients-from-misleading-AI-chatbots-signed-into-law
90. AMS Shardul: Enforcement of DPDP Act and notification of DPDP Rules — https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/
91. EY India: DPDP Rules, 2025 — https://www.ey.com/en_in/insights/cybersecurity/transforming-data-privacy-digital-personal-data-protection-rules-2025
92. GOV.UK: Online Safety Act explainer — https://www.gov.uk/government/publications/online-safety-act-explainer/online-safety-act-explainer
93. DSIT response on Online Safety Act duties (2025) — https://www.judiciary.uk/wp-content/uploads/2025/03/2025-0139-Response-from-Department-for-Science-Innovation-and-Technology-.pdf
94. Tommy's: When to stop exercising in pregnancy (citing ACOG CO 804) — https://www.tommys.org/pregnancy-information/im-pregnant/exercise-pregnancy/when-stop-exercising-pregnancy

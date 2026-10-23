# R4: Regulatory, Privacy and App-Store Compliance for a Camera-Based AI Fitness App with a Fitness/Diet/Medication Coach (US, EU/UK, India)

As of 2026-10-17. Written for the people drafting the BRD, Technical Specification, Roadmap & Strategy, Innovative Features and Build Playbook. This is research, not legal advice. Items marked Medium or Low need review by counsel before launch. Inline links use the numbering in the Sources section. "Wellness" here means outside medical-device regulation.

## Summary

- **The core product can stay outside medical-device law if it is positioned as general wellness.** FDA's General Wellness guidance (2026-01-06) covers "physical fitness" and "weight management" claims [[2]](https://www.fda.gov/media/90652/download). MDCG 2019-11 rev.1 says "wellness or fitness apps" are not medical device software [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf). High.
- **Treatment is the bright line.** A product loses wellness status if its "labeling, advertising, user interface, or functionality" refers to diseases or diagnostic thresholds, prompts "specific clinical action", or informs "treatment decisions (e.g., medication dosing)" [[2]](https://www.fda.gov/media/90652/download). The chatbot's answers count as user interface. High.
- **Medication features: a log, reminders and label information only.**
  - FDA uses enforcement discretion for user-configured reminders and for drug-interaction information given to patients [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion).
  - Apple accepts dose calculators only from approved entities [[75]](https://developer.apple.com/app-store/review/guidelines/).
  - EU guidance treats adherence software that recommends doses as a device [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf).
  - India bars AI from counselling patients or prescribing [[22]](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc).

  Medium-High.
- **FDA has no consumer generative-AI policy yet.** The 2026 clinical decision support (CDS) guidance covers clinician-facing tools only and is silent on AI [[5]](https://www.cov.com/en/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance). FDA's GenAI discussion paper (2026-08-18) says patient-facing functions may sit higher on its risk scale [[9]](https://innolitics.com/articles/fda-generative-ai-medical-devices-discussion-paper/). Medium.
- **For the consumer app, the US federal privacy rule is the FTC's Health Breach Notification Rule (HBNR), not HIPAA.** HIPAA reaches covered entities and business associates, "not most standalone consumer apps" [[24]](https://www.ftc.gov/business-guidance/resources/mobile-health-apps-interactive-tool). The HBNR counts unauthorised disclosure as a breach. Notices are due within 60 days, and penalties reach $53,088 per violation [[25]](https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0). High.
- **State health-data laws are the strictest US layer.** Washington's My Health My Data Act (MHMDA) covers body measurements, medication use, biometric data and health data inferred by machine learning. Collecting or sharing it beyond what the requested service needs requires consent, and consent to share must be separate [[31]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010) [[32]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.030). Nevada and Connecticut have similar laws. New York's bill was vetoed [[37]](https://www.nysenate.gov/legislation/bills/2025/S929). High.
- **Pose skeletons are probably not biometric identifiers, but face points and stored movement data raise the risk.**
  - BIPA covers a "scan of hand or face geometry" [[42]](https://lig.ilga.gov/legislation/ilcs/documents/074000140K10.htm).
  - MediaPipe's pose model outputs 11 face points [[45]](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker).
  - Washington and the amended COPPA rule list gait patterns [[31]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010) [[44]](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm).

  Process frames on the device, drop the face points, and store only per-rep summaries. Medium.
- **EU/UK: treat workout, diet and medication data as health data.** That means explicit consent and a DPIA (data protection impact assessment). Video counts as biometric data only when processed to identify someone uniquely [[46]](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_en_0.pdf). Most of the UK Data (Use and Access) Act's data-protection changes commenced on 2026-02-05 [[49]](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/). High.
- **India DPDP: the main duties apply from 2027-05-13.** They cover notice, consent, security, a 72-hour breach report and parental consent for users under 18 [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/). A proposal to bring them forward was never notified [[55]](https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/) [[56]](https://dpdprules.org/blog/dpdp-18-months-to-12-months-proposal). High/Medium.
- **EU AI Act Article 50 has applied since 2026-08-02.** Users must be told they are chatting with an AI. The Digital Omnibus delayed only the high-risk rules [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force), and a wellness app is not high-risk [[62]](https://artificialintelligenceact.eu/article/6/). High.
- **US AI laws target companion and therapy chatbots:** California SB 243, Utah HB 452, Illinois's WOPR Act and New York's companion law [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/) [[69]](https://casrai.org/compare/ai-therapy-laws-illinois-nevada-utah-compared). Colorado replaced its AI Act with SB 26-189, effective 2027-01-01 [[64]](https://www.jdsupra.com/legalnews/colorado-ai-law-in-flux-comprehensive-2107294/). Medium.
- **Both app stores add health rules.**
  - **Apple:** an accuracy methodology, doctor reminders, explicit consent before sharing data "with third-party AI", and no health data in iCloud [[75]](https://developer.apple.com/app-store/review/guidelines/).
  - **Google:** a Health apps declaration, a "not a medical device" disclaimer, and in-app reporting of AI output [[78]](https://support.google.com/googleplay/android-developer/answer/16679511) [[81]](https://support.google.com/googleplay/android-developer/answer/13985936).

  High.
- **After launch, the main risks are claims and subscriptions.**
  - Health claims need "competent and reliable scientific evidence" [[85]](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance).
  - Enforcement under the Restore Online Shoppers' Confidence Act (ROSCA) continues even though the FTC's click-to-cancel rule was vacated [[90]](https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/).
  - California's auto-renewal changes (2025-07-01) and the EU withdrawal function (2026-06-19) apply [[92]](https://btlaw.com/en/insights/alerts/2025/california-expands-automatic-renewal-law-new-requirements-now-in-effect) [[94]](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en).

  High.
- **Accessibility: build to WCAG 2.2 AA** [[102]](https://www.w3.org/TR/WCAG22/). Whether the European Accessibility Act covers fitness subscription apps is unresolved [[104]](https://www.iubenda.com/en/help/179096-eaa-compliance). Medium.

## 1. Medical-device boundary

### 1.1 United States (FDA)

- **General Wellness (final, 2026-01-06; docket FDA-2014-N-1039)** [[1]](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices) [[2]](https://www.fda.gov/media/90652/download).
  - **Wellness means one of two things.** Either claims with no disease reference (weight management, physical fitness), or healthy-lifestyle claims where the link to a disease is generally accepted. FDA's example of the second kind: "Product X promotes physical activity, which... may help reduce the risk of high blood pressure".
  - **Not wellness:** "treat or diagnose obesity", "treat an eating disorder", "treat muscle atrophy".
  - **Example 3:** food logging that alerts "the user, healthcare provider, or family member of unhealthy dietary activity" is not a device function [[2]](https://www.fda.gov/media/90652/download).

  High.
- **Exclusions.** These apply to "labeling, advertising, user interface, or functionality" [[2]](https://www.fda.gov/media/90652/download):
  1. Disease or threshold references.
  2. Prompts for "specific clinical action".
  3. Treatment guidance.
  4. "Clinical grade" or equivalence claims.
  5. Intended uses that target disease.

  A "see a professional" notice is allowed only if it names no disease, does not call results "abnormal", and gives no thresholds or treatment advice. High.
- **Physiologic estimates.** Non-invasive estimates (blood pressure, SpO2, heart-rate variability) can now count as wellness if they are validated and make no clinical claims [[2]](https://www.fda.gov/media/90652/download) [[3]](https://faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance). This followed FDA's 2025-07-14 warning letter to WHOOP [[4]](https://www.honigman.com/alert-3236). Apple still rejects claims to measure blood pressure, temperature, glucose or SpO2 "using only the sensors on the device" [[75]](https://developer.apple.com/app-store/review/guidelines/). Keep camera vital signs out of the MVP.
- **Enforcement discretion** (page dated 2022-09-29) [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion). FDA lists these functions:
  - Medication tracking with "user-configured reminders" (item 11).
  - Drug–drug interaction information for patients (item 18).
  - Herb–drug look-ups (item 5).
  - Videos or games that motivate physical-therapy exercises (item 4).
  - Symptom checkers (items 7–8).

  These are still devices; FDA simply chooses not to police them. Its page of regulated examples has no consumer exercise example [[7]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-device-software-functions-fda-regulates). Medium-High.
- **CDS and generative AI.** The CDS guidance (2026-01-06) is for clinicians only and is "silent on AI". FDA plans to revise its software policy in FY26 [[5]](https://www.cov.com/en/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance).
  - **Discussion paper (2026-08-18):** FDA "does not regulate GenAI as such; it regulates medical devices", and an LLM function with a medical intended use is a device [[8]](https://www.fda.gov/medical-devices/digital-health-center-excellence/considerations-regulation-generative-ai-enabled-medical-devices-discussion-paper-and-request) [[9]](https://innolitics.com/articles/fda-generative-ai-medical-devices-discussion-paper/).
  - **Guidance:** promised, with no date [[10]](https://www.statnews.com/2026/08/24/fda-rick-abramson-generative-ai-guidances-are-coming/).
  - **Advisory committee (2025-11-06):** covered GenAI mental-health devices only [[11]](https://www.orrick.com/en/insights/2025/11/fdas-digital-health-advisory-committee-considers-generative-ai-therapy-chatbots-for-depression).
  - **January 2025 draft guidance on AI devices:** not reported as final [[12]](https://fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing).

  Medium.

### 1.2 EU, UK and India

- **EU.** MDCG 2019-11 rev.1 (2025-06-17, not legally binding) says "wellness or fitness apps, do not qualify as MDSW" (medical device software) [[13]](https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en) [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf).
  - **Rule 11:** software that informs diagnostic or therapeutic decisions is class IIa, or IIb/III where harm could be serious or fatal. "All other software is classified as class I."
  - **MDSW examples for lay users:** "personalised rehabilitation exercises" for a musculoskeletal pathology to "alleviate pain"; insulin dose recommendations; adherence software recommending "next doses" [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf).
  - **Reform:** an MDR revision was proposed on 2025-12-16 [[15]](https://www.complifegroup.com/2026/01/16/mdr-ivdr-reform/).

  High.
- **UK.** The MHRA's software guidance (page updated 2023-07-01) turns on intended purpose [[16]](https://www.gov.uk/government/publications/medical-devices-software-applications-apps). Commentary flags dose calculators as likely devices [[17]](https://cms.law/en/gbr/legal-updates/mhra-issues-updated-guidance-on-ehealth-stand-alone-software-including-apps). The National Commission's 44 recommendations (2026-09-10), including a possible wellbeing carve-out, are proposals only [[18]](https://www.gov.uk/government/publications/national-commission-into-the-regulation-of-ai-in-healthcare-recommendations-for-a-future-regulatory-framework) [[19]](https://www.raps.org/resource/euro-roundup-mhra-commission-makes-recommendations-on-ai-regulatory-framework-in-the-uk.html). Medium.
- **India.**
  - CDSCO's draft software guidance (2025-10-21) classifies software A–D by intended use and severity, and is "aimed only for creating public awareness". Its text has no wellness carve-out [[20]](https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadPublic_NoticesFiles/Draft%20guidance%20document%20on%20Medical%20Device%20Software%2021%2010%202025.pdf) [[21]](https://india-briefing.com/news/cdsco-draft-guidance-medical-software-40691.html).
  - Under the Telemedicine Practice Guidelines 2020, AI/ML platforms "cannot counsel patients or prescribe medicines" [[22]](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc) [[23]](https://conventuslaw.com/report/india-note-on-telemedicine-practice-guidelines/).

  Medium.

### 1.3 Feature-by-feature boundary

| Feature | US | EU / UK | India | Guardrail |
|---|---|---|---|---|
| Camera rep count, joint angles, tempo, technique cues | Wellness [[2]](https://www.fda.gov/media/90652/download) | Not MDSW [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) | Not a device (intended-use test) [[20]](https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadPublic_NoticesFiles/Draft%20guidance%20document%20on%20Medical%20Device%20Software%2021%2010%202025.pdf) | No injury-diagnosis or rehab claims |
| Rehab or "pain" programmes for a condition | Device; physical-therapy motivation is under enforcement discretion only [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion) | MDSW [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) | Likely a device | Not in MVP |
| Diet logging and weight-loss coaching for adults | Wellness [[2]](https://www.fda.gov/media/90652/download) | Not MDSW | Not a device | No "treats obesity" or eating-disorder claims |
| Medication log and user-set reminders | Enforcement discretion [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion) | Needs a qualification memo [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) | Allowed; no AI counselling [[22]](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc) | No adherence scoring tied to a disease |
| Drug–exercise or drug–drug information | Enforcement discretion for patients [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion) | Risky; the clinician-facing interaction tool is MDSW [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) | Do not deliver through the chatbot | Label-sourced text plus "ask your clinician" |
| Dose advice; start, stop or switch | Device [[2]](https://www.fda.gov/media/90652/download) | MDSW | AI barred [[22]](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc) | Hard refusal |
| Camera vital signs | Wellness only if validated and non-clinical [[2]](https://www.fda.gov/media/90652/download); Apple bars BP and SpO2 [[75]](https://developer.apple.com/app-store/review/guidelines/) | MDSW if clinical | — | Defer |
| Symptom checker | Enforcement discretion [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion) | Likely MDSW | — | Red flags lead to "seek care" only |

**Conclusion.** Form feedback, fitness programming, adult diet coaching and general education are wellness everywhere. Anything that targets a condition (pain, rehab, obesity, diabetes), informs medication decisions or claims clinical accuracy is regulated, or depends on FDA's discretion.

## 2. Privacy and data protection

### 2.1 US federal law

- **HIPAA.** It covers covered entities and business associates, "not most standalone consumer apps" [[24]](https://www.ftc.gov/business-guidance/resources/mobile-health-apps-interactive-tool). The direct-to-consumer app is outside it. Deals with healthcare providers or health plans would probably make the company a business associate, which means a BAA (business associate agreement) and a security programme. This is an inference; Medium. Apple 5.1.3(i) allows benefits based on health data, such as reduced insurance premiums, only if the benefit provider submits the app [[75]](https://developer.apple.com/app-store/review/guidelines/).
- **The FTC Health Breach Notification Rule** (2024 rule; notice dated 2024-05-30) [[26]](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule):
  - **Scope:** it covers vendors of personal health records that can "draw information from multiple sources".
  - **What counts as a breach:** it includes "a company's disclosure of covered information without a person's authorization".
  - **Notices:** to affected people within 60 days; to the FTC at the same time if 500+ people are affected; to the media if 500+ residents of one state are affected.
  - **Penalties:** up to $53,088 per violation [[25]](https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0).
  - **2026 change:** on 2026-09-09 the FTC withdrew its 2021 policy statement, because the 2024 rule already covers health apps [[27]](https://www.ftc.gov/news-events/news/press-releases/2026/09/ftc-withdraws-obsolete-policy-statement).

  The app combines user input, HealthKit/Health Connect data and camera metrics, so it fits the rule. High.
- **Precedents:**
  - **GoodRx:** $1.5M for sharing with ad platforms and showing a misleading HIPAA seal [[28]](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising).
  - **BetterHelp:** $7.8M and a ban on sharing health data for ads [[29]](https://sourcepoint.com/blog/what-to-know-about-betterhelps-ftc-health-data-privacy-settlement/).
  - **Meta / Flo:** a 2025-08-01 jury verdict under the California Invasion of Privacy Act (CIPA) against Meta over Flo app data [[30]](https://www.lawdragon.com/news-features/2025-08-25-big-tech-on-trial-jury-finds-meta-liable-for-misusing-women-health-data).

  Design rule: no ad or attribution SDKs or pixels on health, camera or chat screens.

### 2.2 US state law

- **Washington MHMDA.**
  - **Who it covers:** any entity that does business in Washington or targets its consumers, small businesses included [[31]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010).
  - **What counts as consumer health data:** "bodily functions, vital signs, symptoms, or measurements"; prescribed-medication use; biometric data, including identifying "gait patterns"; and data inferred "including algorithms or machine learning".
  - **Consent:** collecting or sharing beyond what the requested service needs requires consent first. Consent to share must be "separate and distinct", and the request must state the categories, the uses, the recipients and how to withdraw [[32]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.030).
  - **Enforcement:** violations are unfair or deceptive acts under the Consumer Protection Act [[33]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.090).

  High.
- **Other states.**
  - **Nevada SB 370 (in force 2024-03-31):** a similar consent rule, enforced only by the Attorney General [[34]](https://dwt.com/gcp/state-privacy-laws-tracker/broad-state-privacy-law-tracker/nevada) [[35]](https://media.clarkhill.com/wp-content/uploads/2025/10/12140220/The-New-Health-Data-Laws-Every-Retailer-Must_11.11.pdf).
  - **Connecticut:** health-data controllers are covered at any size. Consent is needed to sell health data or to process sensitive data. Geofencing health facilities is banned. Universal opt-out signals must be honoured from 2025-01-01 [[36]](https://portal.ct.gov/ag/sections/privacy/the-connecticut-data-privacy-act).
  - **New York:** S929 was vetoed on 2025-12-19 [[37]](https://www.nysenate.gov/legislation/bills/2025/S929).
- **California CCPA/CPRA.** It applies only above $26,625,000 in revenue, 100,000+ consumers, or 50% of revenue from selling data [[41]](https://www.jacksonlewis.com/insights/navigating-california-consumer-privacy-act-30-essential-faqs-covered-businesses-including-clarifying-regulations-effective-1126). Once the app is in scope:
  - Risk assessments for processing sensitive data (by 2027-12-31 for processing already under way; submissions by 2028-04-01).
  - Rules on automated decision-making from 2027-01-01 [[38]](https://cppa.ca.gov/regulations/ccpa_updates.html) [[39]](https://www.mofo.com/resources/insights/251007-ccpa-regulations-on-cybersecurity-risk-assessments).
  - A right-to-limit notice wherever sensitive data is collected [[40]](https://www.dlapiper.com/insights/publications/2025/09/ccpa-2025-updated-regulations).

### 2.3 Biometric laws and camera/pose data

- **The definitions:**
  - **Illinois BIPA:** "retina or iris scan, fingerprint, voiceprint, or scan of hand or face geometry". Photographs and physical descriptions are excluded [[42]](https://lig.ilga.gov/legislation/ilcs/documents/074000140K10.htm).
  - **Texas CUBI:** "record of hand or face geometry". Consent is needed before capture, sale is banned, the data must be destroyed within one year after its purpose ends, and fines reach $25,000 per violation [[43]](https://texas.public.law/statutes/tex._bus._and_com._code_section_503.001).
  - **COPPA (compliance date 2026-04-22):** now covers "gait patterns; facial templates; or faceprints" [[44]](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm).
  - **EDPB (GDPR):** biometric data must be processed to identify someone uniquely. Categorising people without identifying them is outside Article 9 [[46]](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_en_0.pdf).
  - **ICO (UK):** its biometric guidance is under review [[47]](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/).
- **Assessment (Medium).** MediaPipe's 33 landmarks include face points 0–10, and the model is "optimized for on-device, real-time fitness applications" [[45]](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker). Body skeletons used for form scoring are probably not biometric identifiers. The risk comes from three things: face points, stored movement series (gait), and any feature that recognises who is training.
- **Design rules:**
  1. Run inference on the device, and do not upload frames by default.
  2. Drop landmarks 0–10 immediately. If a head angle is needed, keep only that one derived number.
  3. Store only per-rep summaries.
  4. No face recognition, re-identification, embeddings or segmentation masks.
  5. Upload clips only with a separate opt-in and on-device face blurring, and delete them within Texas's one-year limit [[43]](https://texas.public.law/statutes/tex._bus._and_com._code_section_503.001).
  6. For store labels: Apple does not count on-device-only processing as "collected" [[77]](https://developer.apple.com/app-store/app-privacy-details/). Google requires ephemeral off-device processing to be declared [[82]](https://support.google.com/googleplay/android-developer/answer/10787469).

### 2.4 EU and UK

- **Health data.** GDPR defines it as data "related to the physical or mental health of a natural person" [[48]](https://gdpr-info.eu/art-4-gdpr/). Treat workout, diet and medication data as health data.
  - **Legal basis:** explicit consent under Article 9(2)(a). The EDPB names it as the usual basis for biometric processing [[46]](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_en_0.pdf); applying it to health data is our inference.
  - **DPIA:** run one before beta.
- **Transfers.** The EU-US Data Privacy Framework was upheld on 2025-09-03, and an appeal (C-703/25 P) is pending [[51]](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework). Use certified vendors and keep Standard Contractual Clauses (SCCs) as a fallback. The Digital Omnibus changes to GDPR are stalled [[52]](https://acompli.ie/news/digital-omnibus-gdpr-cookies-status-september-2026/).
- **UK.** Most of the remaining Data (Use and Access) Act provisions commenced on 2026-02-05 [[50]](https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/):
  - Recognised legitimate interests.
  - Limits on automated decisions, now mainly where special-category data is used. This app uses such data.
  - Some analytics cookies allowed with an opt-out.
  - PECR fines raised to UK GDPR level.

  A complaints procedure is required from 2026-06-19 [[49]](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/).

### 2.5 India (DPDP Act 2023 and Rules 2025)

- **Timeline.** The Rules were notified on 2025-11-13. Consent managers start on 2026-11-13, and Rules 3 and 5–16 apply from 2027-05-13 [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/). AZB gives dates one day earlier [[54]](https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/). The proposal to compress the timeline to 12 months was never notified [[55]](https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/) [[56]](https://dpdprules.org/blog/dpdp-18-months-to-12-months-proposal).
- **Duties from 2027-05-13** [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/):
  - A clear, itemised notice.
  - Encryption, access control, and logging with logs kept for one year.
  - Prompt notice to users after a breach, plus a detailed report to the Data Protection Board within 72 hours.
  - Erasure, with 48 hours' notice to the user.
  - Replies to grievances within 90 days.
  - Verifiable parental consent for users under 18, using existing age data, details the user provides, or DigiLocker-type tokens.
- **Children and penalties (Medium).**
  - Section 9(3) bans tracking, behavioural monitoring and targeted ads aimed at children.
  - Penalties reach ₹250 crore for security failures and ₹200 crore for children's-data breaches.
  - If designated a Significant Data Fiduciary, the company must add DPIAs, audits and algorithmic checks [[57]](https://iitbhu.ac.in/contents/institute/cf/cis/doc/dpdp_act_rules_summary.pdf) [[58]](https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/pdf/2025/11/ey-india-dpdp-act-2023-and-rules-2025-pov.pdf).
- **Age policy.** Launch for adults (18+) only, in every market. The reasons:
  - **India:** parental consent for all under-18s [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/).
  - **US:** COPPA [[24]](https://www.ftc.gov/business-guidance/resources/mobile-health-apps-interactive-tool).
  - **UK:** CAP 13.3 [[86]](https://www.asa.org.uk/type/non_broadcast/code_section/13.html).
  - **California:** SB 243 duties for minors [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/).

## 3. AI-specific rules

- **EU AI Act Article 50** [[61]](https://artificialintelligenceact.eu/article/50/):
  - **50(1):** people must be "informed that they are interacting with an AI system" unless that is obvious.
  - **50(2):** providers of generative systems must mark synthetic audio, images, video or text in a machine-readable form.
  - **50(3):** people exposed to emotion recognition or biometric categorisation must be told.
  - **50(5):** the information must come "at the latest at the time of the first interaction" and must be accessible.

  These duties have applied since 2026-08-02. The Digital Omnibus (in force 2026-07-27) gave only a 50(2) grace period, to 2026-12-02, and only for systems already on the market before 2026-08-02. A new app gets none [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) [[60]](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html). High.
- **High-risk.** These rules start on 2027-12-02 (Annex III) or 2028-08-02 (Annex I products such as medical devices) [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force). Under Article 6(1), AI is high-risk only as, or inside, an Annex I product that needs third-party conformity assessment [[62]](https://artificialintelligenceact.eu/article/6/). The wellness app is therefore not high-risk. Certification by a notified body under the MDR would change that.
- **Fatigue is not emotion recognition.** Recital 18 excludes "pain or fatigue" and "the mere detection of readily apparent expressions, gestures or movements" [[63]](https://artificialintelligenceact.eu/recital/18/). Fatigue detection from rep speed is fine. Do not infer mood from the face or voice.
- **FTC.** "There is no AI exemption from the laws on the books" (2024-09-25) [[70]](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes). The FTC's 6(b) study of companion chatbots (2025-09-11) looks at harm to minors, monetisation, testing and disclosures [[71]](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions). "As good as a human coach" claims need substantiation [[85]](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance).
- **Colorado.** SB25B-004 delayed SB 24-205 to 2026-06-30 [[65]](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205). It was then replaced by SB 26-189 (signed 2026-05-14, effective 2027-01-01) [[64]](https://www.jdsupra.com/legalnews/colorado-ai-law-in-flux-comprehensive-2107294/):
  - Duties are notice-based and apply when automated decision-making technology makes "consequential decisions".
  - There is no general duty to disclose AI interaction.
  - A 2026-04-27 federal order in xAI's lawsuit pauses enforcement.

  A wellness coach is unlikely to be covered. Recheck before any insurer or employer deal. Medium.
- **State chatbot laws** [[66]](https://fpf.org/wp-content/uploads/2026/02/Enacted-AI-Legislation-Chart-.pdf):
  - **California SB 243 (from 2026-01-01):** companion chatbots must remind users at least every 3 hours that they are not human, and must publish self-harm protocols. Reporting starts 2027-07-01, and there is a private right of action [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/).
  - **Utah HB 452 (2025-05-07):** disclosures and data limits for mental-health chatbots [[68]](https://fpf.org/?p=244909).
  - **Illinois WOPR Act (2025-08-04):** no AI therapy without a licensed clinician, with fines up to $10,000 [[69]](https://casrai.org/compare/ai-therapy-laws-illinois-nevada-utah-compared).
  - **New York companion law (November 2025):** up to $15,000 per day [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/).

  Build to the strictest version: AI disclosure, crisis referral, and no therapy or companion positioning. Medium.
- **India.**
  - Under the amended IT Rules (in force 2026-02-20), intermediaries must label synthetic media and attach provenance metadata [[72]](https://www.hoganlovells.com/en/publications/india-introduces-mandatory-labelling-for-ai-and-3hour-takedown-for-illegal-content).
  - ASCI's labelling guidelines for synthetic content (final 2026-09-29; effective around 2026-12-29 or 2027-01-01) ban fabricated endorsements and exaggerated features [[73]](https://www.khaitanco.com/sites/default/files/2026-10/Ergo_ASCI%20Guidelines%20on%20SGC%20Labelling_12%2010%202026.pdf) [[74]](https://www.exchange4media.com/advertising-news/asci-issues-guidelines-on-responsible-labelling-of-ai-generated-ad-content-158710.html).

## 4. App stores

**Apple** (App Review Guidelines, last updated 2026-06-08) [[75]](https://developer.apple.com/app-store/review/guidelines/)

| Rule | Requirement | Build implication |
|---|---|---|
| 1.4.1 | Disclose the data and methodology behind accuracy claims. No blood pressure, temperature, glucose or SpO2 from device sensors alone. Remind users to "check with a doctor". | A methodology page; doctor reminders in onboarding and chat |
| 1.4.2 | Dose calculators only from approved entities | None in the app |
| 5.1.1(i)–(iv) | Privacy policy linked in the app and in metadata. Consent even for "anonymous" data. Purpose strings must "clearly and completely describe" the use. Paid features cannot depend on data access. | Specific usage strings for camera, microphone and HealthKit; a consent centre |
| 5.1.1(v) | In-app account deletion. Deactivation alone is not enough. Revoke Sign in with Apple tokens [[76]](https://developer.apple.com/support/offering-account-deletion-in-your-app/). | Settings > Delete account |
| 5.1.1(ix) | Healthcare and sensitive-data apps are submitted by a legal entity | Enrol as an organisation |
| 5.1.2(i) | Explicit permission before sharing data "with third-party AI"; App Tracking Transparency for tracking | An AI-processing consent screen before the first chat |
| 5.1.2(vi), 5.1.3 | Camera, ARKit and HealthKit data may not be used for marketing or ads. Disclose which health data is collected. No personal health information in iCloud. | No ad use; health store excluded from iCloud backup |
| 3.1.2 | Subscriptions of 7+ days, with what the user gets stated before purchase | Paywall copy |

**Apple privacy labels.** "Collect" means transmitting data off the device for longer than real-time servicing needs. Data processed only on the device is not collected. Data that SDKs collect counts [[77]](https://developer.apple.com/app-store/app-privacy-details/).

**Google Play**

- **Health:** every developer files a Health apps declaration. Health apps that are not medical devices state in their description that the app is "not a medical device and does not diagnose, treat, cure, or prevent any medical condition", and remind users to "consult a healthcare professional". Misleading health claims are barred [[78]](https://support.google.com/googleplay/android-developer/answer/16679511).
- **User Data:** a prominent disclosure and affirmative consent before permission prompts. "Third-party AI integrations" are covered. Account deletion must work both in the app and on the web [[79]](https://support.google.com/googleplay/android-developer/answer/10144311).
- **Health Connect:** requires a declaration. "Fitness coaching" is an approved use. No ads and no sale [[80]](https://support.google.com/googleplay/android-developer/answer/9888170). The Google Fit APIs are deprecated in 2026 [[84]](https://developers.google.com/fit).
- **AI-Generated Content:** in-app reporting "without needing to exit the app" [[81]](https://support.google.com/googleplay/android-developer/answer/13985936).
- **Data safety:** "collect" means sending data off the device. Ephemeral processing is still declared [[82]](https://support.google.com/googleplay/android-developer/answer/10787469).
- **Target API:** API 36 is required from 2026-08-31, with an extension to 2026-11-01 [[83]](https://support.google.com/googleplay/android-developer/answer/11926878).

## 5. Consumer protection and advertising

- **Substantiating claims.**
  - **FTC:** health claims need "competent and reliable scientific evidence", and randomised controlled trials are "the most reliable form of evidence". The guidance covers apps. Testimonials are not substantiation, and "results not typical" disclaimers do not cure a misleading claim [[85]](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance).
  - **UK CAP Code s.13** [[86]](https://www.asa.org.uk/type/non_broadcast/code_section/13.html):
    - No weight-control marketing to under-18s or people with a BMI below 18.5.
    - Weight loss above 2 lb a week is "unlikely to be compatible" with good practice.
    - No promises of precise losses or of fat loss from specific body parts.
    - Diet plans must be nutritionally balanced.
    - Claims about exercise leading to weight loss must be substantiated.
  - **India:** the Drugs and Magic Remedies Act schedule includes obesity [[87]](https://www.indiacode.nic.in/indiacode/bitstream/123456789/1412/1/A1954-21.pdf). Health and food advertisers file self-declaration certificates [[88]](https://foxmandal.in/News/new-advisory-limits-self-declaration-requirement-to-food-health-ads/).
- **Auto-renewal and cancellation.**
  - **US federal:** the Eighth Circuit vacated the click-to-cancel rule on procedural grounds in July 2025. The FTC published a new ANPRM (advance notice of proposed rulemaking) on 2026-03-13 and continues to enforce ROSCA (for example, its suit against JustAnswer on 2026-01-13) [[89]](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule) [[90]](https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/). The Amazon order (2025-09-25; $1B penalty plus $1.5B in refunds) requires a prominent decline option, clear terms, and cancellation through the same channel as sign-up [[91]](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon).
  - **California ARL (from 2025-07-01)** [[92]](https://btlaw.com/en/insights/alerts/2025/california-expands-automatic-renewal-law-new-requirements-now-in-effect) [[93]](https://www.sheppard.com/insights/blogs/californias-auto-renewal-law-takes-effect-on-july-1):
    - Express affirmative consent, with proof kept for 3 years or 1 year after the contract ends, whichever is longer.
    - An annual reminder.
    - Online click-to-cancel, through the same channel as sign-up.
    - Notice of material price changes.
    - Free trials that convert to paid are covered.
  - **EU:** from 2026-06-19, online contracts need a labelled, always-available two-step "withdrawal function", and an acknowledgement on a durable medium. Member State implementation varies [[94]](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en) [[95]](https://www.hoganlovells.com/en/publications/eu-consumer-protection-law-update-new-mandatory-withdrawal-button-what-online-traders-need-to-know) [[96]](https://vbb.com/wp-content/uploads/2026/06/8-06-26-The-online-withdrawal-button.pdf).
  - **UK:** the government responded on the DMCC subscription regime on 2026-04-02. Secondary legislation is pending, with no start date [[97]](https://www.gov.uk/government/consultations/consultation-on-the-implementation-of-the-new-subscription-contracts-regime).
  - **India:**
    - E-mandates need authentication when registered. Later debits are authentication-free up to ₹15,000, or ₹1,00,000 for mutual funds, insurance and credit-card bills. Users get pre-debit notices and an opt-out [[98]](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12570&Mode=0) [[99]](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12341).
    - The Dark Patterns Guidelines 2023 ban a "subscription trap", meaning cancellation that is impossible or cumbersome. A June 2025 advisory asked platforms to self-audit within three months [[100]](https://www.jsalaw.com/?p=49613) [[101]](https://www.exchange4media.com/marketing-news/ccpa-gives-ecomm-players-3-months-to-root-out-dark-patterns-144202.html).

## 6. Accessibility

- **WCAG 2.2** (W3C Recommendation, latest version dated 2024-12-12) adds these A/AA criteria: Focus Not Obscured (Minimum), Dragging Movements, Target Size (Minimum), Consistent Help, Redundant Entry and Accessible Authentication (Minimum). It removes 4.1.1 Parsing [[102]](https://www.w3.org/TR/WCAG22/). High.
- **European Accessibility Act.** It applies to services provided to consumers after 2025-06-28 and covers e-commerce [[103]](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en). Micro-enterprises that provide services (fewer than 10 staff and no more than €2M turnover) are exempt. Whether a fitness subscription app is in scope is unresolved [[104]](https://www.iubenda.com/en/help/179096-eaa-compliance). Medium.
- **Design implications.**
  - Form cues need an audio or haptic channel as well as the visual overlay.
  - Video needs captions.
  - Live overlays need screen-reader labels.
  - The Article 50 AI notice must itself be accessible [[61]](https://artificialintelligenceact.eu/article/50/).

## 7. Key upcoming dates (for the Roadmap)

| Date | Event |
|---|---|
| 2026-10-19 | Comments close on FDA's GenAI discussion paper [[9]](https://innolitics.com/articles/fda-generative-ai-medical-devices-discussion-paper/) |
| 2026-11-01 | End of the Google Play extension for targeting API 36 [[83]](https://support.google.com/googleplay/android-developer/answer/11926878) |
| 2026-11-13 | DPDP Rule 4 (consent managers) takes effect [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/) |
| 2026-12-02 | End of the AI Act 50(2) marking grace period for systems on the market before 2026-08-02 [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) |
| ~2026-12-29 / 2027-01-01 | ASCI labelling guidelines for synthetic ad content take effect [[73]](https://www.khaitanco.com/sites/default/files/2026-10/Ergo_ASCI%20Guidelines%20on%20SGC%20Labelling_12%2010%202026.pdf) |
| 2027-01-01 | Colorado SB 26-189 takes effect [[64]](https://www.jdsupra.com/legalnews/colorado-ai-law-in-flux-comprehensive-2107294/); CCPA rules on automated decision-making apply [[39]](https://www.mofo.com/resources/insights/251007-ccpa-regulations-on-cybersecurity-risk-assessments) |
| 2027-05-13 | DPDP substantive duties apply [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/) |
| 2027-07-01 | SB 243 annual reporting begins [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/) |
| 2027-12-02 / 2028-08-02 | AI Act high-risk rules apply (Annex III / Annex I) [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) |
| 2027-12-31 / 2028-04-01 | CCPA risk assessments due, then submissions (only if the app is in scope) [[39]](https://www.mofo.com/resources/insights/251007-ccpa-regulations-on-cybersecurity-risk-assessments) |

## 8. Compliance matrix

What "Due" means:

- **MVP:** designed into the MVP build.
- **Beta:** working before data from external testers is collected.
- **Launch:** before public release in that market.
- **B2B:** before the first contract with a provider, health plan, employer or insurer.

| Requirement | Jurisdiction | Applies? Why | Implication | Due | Source |
|---|---|---|---|---|---|
| Wellness intended use; claims discipline across labeling, UI and ads | US | Yes. The exemption depends on claims, and the UI includes the chatbot. | Intended-use statement, claims register, chatbot scope policy | MVP | [[2]](https://www.fda.gov/media/90652/download) |
| No dosing or treatment outputs | All | Yes. This is the main device trigger. | Hard refusals; no dose calculators | MVP | [[2]](https://www.fda.gov/media/90652/download) [[75]](https://developer.apple.com/app-store/review/guidelines/) |
| Medication reminders and interaction info only under enforcement discretion | US | If medication features ship | User-configured reminders only; label-sourced information | Beta | [[6]](https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion) |
| Qualification memo showing the app is not medical device software | EU, UK | Yes | Covers medication features; no rehab or pain claims | Launch | [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) [[16]](https://www.gov.uk/government/publications/medical-devices-software-applications-apps) |
| AI may not counsel patients or prescribe | IN | Yes | Medication answers limited to general information plus "see a doctor" | Launch | [[22]](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc) |
| HIPAA business associate | US | No for the consumer app; yes for provider or health-plan deals | BAA, HIPAA security programme, separate tenant | B2B | [[24]](https://www.ftc.gov/business-guidance/resources/mobile-health-apps-interactive-tool) |
| FTC Health Breach Notification Rule | US | Likely. The record draws from several sources. | 60-day breach runbook; no unauthorised disclosure | Beta | [[25]](https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0) |
| FTC Act: health data sharing and privacy promises | US | Yes | No ad or attribution SDKs in health flows; no "HIPAA" seals | MVP | [[28]](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising) |
| Washington MHMDA | US-WA | Yes, with no revenue threshold | Consent beyond the requested service; separate consent to share; a consumer health data policy | Beta | [[31]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010) [[32]](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.030) |
| Nevada SB 370 and Connecticut CTDPA | US-NV, CT | Yes | Same consent stack; no sale; honour universal opt-out (CT) | Beta | [[34]](https://dwt.com/gcp/state-privacy-laws-tracker/broad-state-privacy-law-tracker/nevada) [[36]](https://portal.ct.gov/ag/sections/privacy/the-connecticut-data-privacy-act) |
| CCPA/CPRA: sensitive data and risk assessment | US-CA | Only above the thresholds | Right-to-limit notice; risk assessment once in scope | Launch (plan) | [[41]](https://www.jacksonlewis.com/insights/navigating-california-consumer-privacy-act-30-essential-faqs-covered-businesses-including-clarifying-regulations-effective-1126) [[39]](https://www.mofo.com/resources/insights/251007-ccpa-regulations-on-cybersecurity-risk-assessments) |
| BIPA and Texas CUBI | US-IL, TX | Only if face geometry is captured | Drop face landmarks; run on device; no face ID | MVP | [[42]](https://lig.ilga.gov/legislation/ilcs/documents/074000140K10.htm) [[43]](https://texas.public.law/statutes/tex._bus._and_com._code_section_503.001) |
| COPPA | US | Only if users are under 13 | 18+ age gate | MVP | [[44]](https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm) |
| GDPR Article 9 explicit consent and DPIA | EU | Yes (health data) | Consent for each purpose; a DPIA | Beta | [[48]](https://gdpr-info.eu/art-4-gdpr/) [[46]](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_en_0.pdf) |
| GDPR transfers | EU | Yes (US cloud and LLM) | Vendors certified under the Data Privacy Framework, with SCCs as fallback | Beta | [[51]](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework) |
| UK GDPR and the Data (Use and Access) Act | UK | Yes | Complaints procedure; safeguards for automated decisions | Launch | [[49]](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/) [[50]](https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/) |
| DPDP: notice, consent, security, breach, erasure | IN | Yes, from 2027-05-13 | Itemised notice; one-year log retention; 72-hour Board report; 48-hour erasure notice | Launch; build by 2027-05 | [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/) |
| DPDP: children | IN | Only if users are under 18 | Launch 18+; no behavioural ads | MVP | [[57]](https://iitbhu.ac.in/contents/institute/cf/cis/doc/dpdp_act_rules_summary.pdf) |
| AI Act 50(1) and 50(5): AI disclosure | EU | Yes (chatbot) | Accessible "You're chatting with an AI" notice at the first interaction | Launch | [[61]](https://artificialintelligenceact.eu/article/50/) |
| AI Act 50(2): marking AI output | EU | Likely, if we are the provider of the generative system | Machine-readable marks or metadata on AI output | Launch | [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force) |
| AI Act high-risk rules | EU | No while it is a wellness app | Keep the wellness scope | — | [[62]](https://artificialintelligenceact.eu/article/6/) |
| US chatbot laws (CA SB 243, UT, IL, NY) | US states | Partly; depends on companion or mental-health scope | AI disclosure, self-harm protocol, no therapy | Launch | [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/) [[69]](https://casrai.org/compare/ai-therapy-laws-illinois-nevada-utah-compared) |
| Colorado SB 26-189 | US-CO | Unlikely, as there are no consequential decisions | Reassess before insurer or employer deals | B2B | [[64]](https://www.jdsupra.com/legalnews/colorado-ai-law-in-flux-comprehensive-2107294/) |
| Apple 1.4.1, 1.4.2, 5.1.1–5.1.3, 3.1.2 | iOS | Yes | Methodology page; deletion; AI-sharing consent; no personal health data in iCloud; submit as organisation | Beta | [[75]](https://developer.apple.com/app-store/review/guidelines/) |
| Apple privacy labels | iOS | Yes | Labels that reflect on-device processing; SDK inventory | Beta | [[77]](https://developer.apple.com/app-store/app-privacy-details/) |
| Google Play: Health declaration, disclaimer, User Data, Data safety | Android | Yes | Declaration; description disclaimer; web deletion URL; Data safety form | Beta | [[78]](https://support.google.com/googleplay/android-developer/answer/16679511) [[79]](https://support.google.com/googleplay/android-developer/answer/10144311) |
| Health Connect declaration | Android | Only if Health Connect is used | Declare "fitness coaching"; no ads | Beta | [[80]](https://support.google.com/googleplay/android-developer/answer/9888170) |
| AI-Generated Content policy; target API 36 | Android | Yes | In-chat report button; target SDK 36 | Beta | [[81]](https://support.google.com/googleplay/android-developer/answer/13985936) [[83]](https://support.google.com/googleplay/android-developer/answer/11926878) |
| Health-claim substantiation | US, UK, IN | Yes | An evidence file for each claim; a validation study of form scoring | Launch | [[85]](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance) |
| Weight-loss advertising rules | UK, IN | Yes | No under-18 targeting; no spot-reduction or precise-loss claims | Launch | [[86]](https://www.asa.org.uk/type/non_broadcast/code_section/13.html) [[87]](https://www.indiacode.nic.in/indiacode/bitstream/123456789/1412/1/A1954-21.pdf) |
| Auto-renewal (ROSCA, California ARL) | US | Yes | Records of affirmative consent; annual reminder; click-to-cancel | Launch | [[90]](https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/) [[92]](https://btlaw.com/en/insights/alerts/2025/california-expands-automatic-renewal-law-new-requirements-now-in-effect) |
| EU withdrawal function | EU | Yes, for web or direct online contracts | Two-step withdrawal button | Launch | [[95]](https://www.hoganlovells.com/en/publications/eu-consumer-protection-law-update-new-mandatory-withdrawal-button-what-online-traders-need-to-know) |
| RBI e-mandates and dark-patterns rules | IN | E-mandates only with direct billing; dark-patterns rules always | Pre-debit notices; easy cancellation | Launch | [[99]](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12341) [[100]](https://www.jsalaw.com/?p=49613) |
| WCAG 2.2 AA; European Accessibility Act | All; EU | Best practice; EAA scope uncertain | Audio and haptic cues; target sizes; captions | Launch | [[102]](https://www.w3.org/TR/WCAG22/) [[104]](https://www.iubenda.com/en/help/179096-eaa-compliance) |

## 9. Positioning and claims guide

**Positioning statement** (for the store description and onboarding): "A fitness and nutrition coaching app for healthy adults, with camera-based technique feedback and an AI coach. Not a medical device; it does not diagnose, treat, cure, or prevent any medical condition. Consult a healthcare professional for medical advice." The disclaimer wording follows Google's required text [[78]](https://support.google.com/googleplay/android-developer/answer/16679511); the doctor reminder follows Apple 1.4.1 [[75]](https://developer.apple.com/app-store/review/guidelines/).

| Topic | Do say | Don't say | Why |
|---|---|---|---|
| Form | "Real-time technique feedback"; "counts reps, tracks range of motion and tempo" | "Detects injuries"; "diagnoses posture problems" | Diagnosis makes it a device [[2]](https://www.fda.gov/media/90652/download) |
| Safety | "Cues to help you keep good form"; "stop if you feel pain" | "Prevents injuries"; "injury-proof" | Needs substantiation; condition framing [[85]](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance) |
| Rehab | "Mobility and strength routines" | "Physical therapy"; "rehab your knee"; "relieves back pain" | Rehab for a condition is MDSW [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf) |
| Weight and diet | "Build healthy eating habits"; "supports your weight-loss goals" | "Treats obesity"; "for eating disorders"; "lose 5 kg in 2 weeks"; "burn belly fat" | Excluded under GW [[2]](https://www.fda.gov/media/90652/download); CAP 13.9–13.10 [[86]](https://www.asa.org.uk/type/non_broadcast/code_section/13.html) |
| Chronic disease | "As part of a healthy lifestyle, regular activity may help reduce the risk of high blood pressure" | "Reverses diabetes"; "lowers your blood pressure" | Allowed vs. excluded GW wording [[2]](https://www.fda.gov/media/90652/download) |
| Medication | "Log your medicines and set your own reminders"; "general label information — check with your clinician" | "Tells you what dose to take"; "safe to stop, start or combine"; "adjusts your GLP-1 dose" | Dosing [[2]](https://www.fda.gov/media/90652/download) [[75]](https://developer.apple.com/app-store/review/guidelines/); India AI ban [[22]](https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc) |
| Accuracy | "How our form scores work, and their limits" | "Clinically proven"; "medical-grade"; "as accurate as a physio" | GW exclusion 4 [[2]](https://www.fda.gov/media/90652/download); Apple 1.4.1 |
| Vital signs | Nothing in v1 | "Measures your heart rate, BP or SpO2 with the camera" | Apple 1.4.1 [[75]](https://developer.apple.com/app-store/review/guidelines/) |
| AI coach | "AI coach — not a doctor, dietitian or therapist" | "AI doctor"; "AI dietitian"; "therapy"; "your AI companion" | Illinois WOPR [[69]](https://casrai.org/compare/ai-therapy-laws-illinois-nevada-utah-compared); SB 243 [[67]](https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/) |
| Out-of-range results | "You may want to talk to a health professional" | "Your result is abnormal"; "you may have X" | GW limits on notifications [[2]](https://www.fda.gov/media/90652/download) |
| Privacy | "Video is processed on your phone" (only if true in every mode) | "HIPAA-compliant"; "100% anonymous" | GoodRx's HIPAA seal [[28]](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising); Apple consent rules for anonymous data [[75]](https://developer.apple.com/app-store/review/guidelines/) |

**Chatbot guardrails for the Build Playbook**

1. **Refuse these topics:**
   - Dosing, and starting, stopping, switching or combining medicines.
   - Diagnosis and interpreting lab results.
   - Treatment plans for a disease.
   - Therapy.
   - Content that promotes eating disorders.
   - Weight loss for minors.
2. **Red-flag symptoms** (chest pain, fainting, suicidal thoughts): end the session and route the user to emergency or crisis services for their country.
3. **AI disclosure:** show it at the first message and keep a persistent label [[61]](https://artificialintelligenceact.eu/article/50/).
4. **Medication facts:** use only a curated drug-label source, cite it, and add "ask your clinician".
5. **Consent before data goes to the LLM vendor** [[75]](https://developer.apple.com/app-store/review/guidelines/) [[79]](https://support.google.com/googleplay/android-developer/answer/10144311). No training on chats unless the user opts in, because Apple 5.1.2(ii) bars repurposing data without further consent.
6. **In-chat report button** [[81]](https://support.google.com/googleplay/android-developer/answer/13985936).
7. **Testing and monitoring:** a red-team suite before launch, and harm monitoring after it. This matches the FTC's 6(b) themes [[71]](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions).

## 10. Compliance documents and processes needed

1. Intended-use statement and regulatory qualification memo covering the US, EU, UK and India [[2]](https://www.fda.gov/media/90652/download) [[14]](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf).
2. Claims register, substantiation file and a review procedure for marketing and in-app copy.
3. Validation report and public methodology page for form scoring (Apple 1.4.1).
4. Chatbot safety case: scope policy, refusal list, red-team results, published self-harm protocol, and a change log for models and prompts.
5. Privacy notices: a global policy; a Washington/Nevada consumer health data policy; an itemised DPDP notice; just-in-time notices.
6. Consent management: consent per purpose, a separate consent to share, consent for AI processing, withdrawal, and consent records.
7. Data map, register of processing, SDK and vendor inventory, data processing agreements with LLM and cloud vendors, and the transfer mechanism (DPF or SCCs).
8. GDPR DPIA. Add a CCPA risk assessment once the app is in scope, and a DPDP DPIA if it is designated a Significant Data Fiduciary.
9. Camera and biometric data policy, with a retention and destruction schedule.
10. Security programme: encryption, access control, logging (logs kept at least one year for India), backups.
11. Incident response plan: HBNR 60 days, DPDP 72-hour report, state laws. Run a tabletop exercise.
12. Rights and deletion procedure: in-app and web deletion, 48-hour pre-erasure notice and 90-day grievance response (India), and the UK complaints procedure.
13. Age-assurance policy (18+).
14. Subscription procedure: consent records, annual reminders, click-to-cancel, the EU withdrawal button, and RBI pre-debit notices.
15. WCAG 2.2 AA conformance report and an accessibility statement.
16. App-store submission kit:
    - **Apple:** privacy labels, usage strings, reviewer notes, organisation account.
    - **Google:** Health apps declaration, Data safety form, Health Connect declaration, deletion URL.
17. B2B pack: BAA template, security questionnaire, DPA, and a review under Colorado law and insurer rules.
18. Regulatory watch log: FDA GenAI guidance, DPDP timing, the GDPR omnibus, SB 243's scope, the UK DMCC regime.

## Recommendations for the docs

- **BRD:**
  - Set the scope to "general wellness for healthy adults 18+".
  - Include the intended-use statement and the claims guide.
  - Declare these out of scope for v1: dosing, rehab or pain programmes, camera vital signs, symptom checking, minors, and therapy.
  - Define the medication feature as a log, user-set reminders and label-sourced information.
  - In the EU and UK, ship medication features only after the qualification memo.
  - In India, the chatbot does no medication counselling.
- **Technical Specification:**
  - An on-device pose pipeline that drops face landmarks 0–10, and a schema that stores only per-rep summaries.
  - No storage of raw video.
  - A consent service with flags for each purpose.
  - An LLM gateway that checks consent, minimises personal data, classifies scope, inserts refusal templates and adds AI labels and metadata.
  - No ad or attribution SDKs.
  - The health store excluded from iCloud backup.
  - Region-aware storage and transfer controls, a deletion pipeline, and audit logs kept for at least one year.
- **Roadmap and Strategy:**
  - Launch in the US first; the wellness path there is clearest.
  - Then the UK and EU, after the qualification memo, a DPIA and the Article 50 notices.
  - In India, build flows that are DPDP-ready before 2027-05-13.
  - Put B2B with healthcare providers (HIPAA), clinician sharing, teen programmes and any camera vital signs into later phases.
  - Reassess when FDA publishes GenAI guidance.
- **Innovative Features:**
  - Frame medication-aware coaching as context plus clinician-set limits, never advice. This is consistent with R6.
  - Fatigue detection is fine under the AI Act. Emotion inference is not.
  - Any "injury risk" score needs evidence and non-diagnostic wording.
- **Build Playbook:**
  - Use the compliance matrix as acceptance criteria.
  - Add the store declarations to the definition of done.
  - Ship a chatbot refusal test suite.
  - Lint in-app strings in CI against a list of banned words.
  - Keep a release checklist for each market.

## Unverified / conflicting

- **DPDP dates.** Sources give 13 or 14 November 2025 for notification. The substantive date is given as 12, 13 or 14 May 2027 [[53]](https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/) [[54]](https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/). The 12-month compression was not notified as of trackers dated late Sept–Oct 2026; check the Gazette. Details on Significant Data Fiduciary duties and the children's exemptions (Rule 10 vs Rule 12) come from secondary sources only.
- **California SB 243.** The definition of "companion chatbot", its exclusions, and whether the 3-hour reminder covers all users or only minors were not fetched.
- **California AB 489** (AI implying a healthcare licence): the text could not be retrieved. Avoiding "doctor", "nurse" and "dietitian" titles is a precaution.
- **Colorado.**
  - The reported AG proposed rules (2026-08-11, with comments to 2026-10-26) come from one source [[105]](https://casrai.org/guides/colorado-ai-act-explained).
  - Whether SB 26-189 keeps health care as a "consequential decision" is unknown.
  - One outlet claimed SB 24-205 took effect on 2026-06-30. That conflicts with the repeal.
- **Not fetched in this run:** Washington's consumer-health-data policy section (RCW 19.373.020); how its private right of action works through RCW 19.86; BIPA §15 duties (e.g., a written retention policy); the CCPA statutory definition of sensitive personal information; and GDPR Articles 33 and 35. Whether face landmarks count as a "scan of face geometry" is untested in court.
- **FTC items.**
  - The effective date of the 2024 HBNR rule (widely reported as 2024-07-29) is not shown on the FTC page, whose notice is dated 2024-05-30.
  - The Premom settlement is reported as both $100,000 and $200,000.
  - The Cerebral order could not be verified (the FTC page returned 404).
  - The comment deadline for the negative-option ANPRM and the outcome are open.
- **ASCI effective date:** 2026-12-29 or 2027-01-01. **RBI:** the 24-hour pre-debit timing and a "2026 consolidated e-mandate framework" come from secondary sources only.
- **EU Accessibility Act:** whether it covers fitness subscription apps, and the national laws that implement it, were not checked. **MHRA:** the Spring 2027 consultation and the draft Medical Devices (Amendment) Regulations 2026 come from search summaries only.
- **FDA's enforcement-discretion page** is dated 2022-09-29. The planned FY26 revision of the software policy could change how medication features are treated.
- **Gaps:** Apple privacy-manifest details (page body not retrieved), crisis-line numbers for each market, and how Article 50(2) applies to text from an integrated third-party LLM (provider vs deployer) are all unverified. Check the Commission's transparency guidelines of 2026-07-20 [[59]](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force).

## Sources

1. FDA, General Wellness: Policy for Low Risk Devices (guidance page, Jan 2026): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices
2. FDA, General Wellness guidance PDF (issued 2026-01-06): https://www.fda.gov/media/90652/download
3. Faegre Drinker, Key updates in FDA's 2026 General Wellness and CDS guidance: https://faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance
4. Honigman, FDA's recent updates to General Wellness and CDS policies: https://www.honigman.com/alert-3236
5. Covington, 5 key takeaways from FDA's revised CDS guidance: https://www.cov.com/en/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance
6. FDA, Examples of software functions for which FDA will exercise enforcement discretion: https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-software-functions-which-fda-will-exercise-enforcement-discretion
7. FDA, Examples of device software functions the FDA regulates: https://www.fda.gov/medical-devices/device-software-functions-including-mobile-medical-applications/examples-device-software-functions-fda-regulates
8. FDA, Considerations for the Regulation of Generative AI-Enabled Medical Devices (discussion paper): https://www.fda.gov/medical-devices/digital-health-center-excellence/considerations-regulation-generative-ai-enabled-medical-devices-discussion-paper-and-request
9. Innolitics, FDA GenAI medical devices discussion paper: what's inside: https://innolitics.com/articles/fda-generative-ai-medical-devices-discussion-paper/
10. STAT, FDA digital health leader promises generative AI guidance (2026-08-24): https://www.statnews.com/2026/08/24/fda-rick-abramson-generative-ai-guidances-are-coming/
11. Orrick, FDA Digital Health Advisory Committee considers GenAI therapy chatbots: https://www.orrick.com/en/insights/2025/11/fdas-digital-health-advisory-committee-considers-generative-ai-therapy-chatbots-for-depression
12. FDA, AI-Enabled Device Software Functions: Lifecycle Management draft guidance: https://fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing
13. European Commission, Update: MDCG 2019-11 rev.1 (2025-06-17): https://health.ec.europa.eu/latest-updates/update-mdcg-2019-11-rev1-qualification-and-classification-software-regulation-eu-2017745-and-2025-06-17_en
14. MDCG 2019-11 rev.1, Qualification and classification of software (PDF): https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf
15. Complife, MDR and IVDR reform: the Commission's proposal: https://www.complifegroup.com/2026/01/16/mdr-ivdr-reform/
16. MHRA, Medical device stand-alone software including apps: https://www.gov.uk/government/publications/medical-devices-software-applications-apps
17. CMS, MHRA updated guidance on stand-alone software including apps: https://cms.law/en/gbr/legal-updates/mhra-issues-updated-guidance-on-ehealth-stand-alone-software-including-apps
18. GOV.UK, National Commission into the Regulation of AI in Healthcare: recommendations: https://www.gov.uk/government/publications/national-commission-into-the-regulation-of-ai-in-healthcare-recommendations-for-a-future-regulatory-framework
19. RAPS, Euro Roundup: Commission recommendations on UK AI framework (2026-09-17): https://www.raps.org/resource/euro-roundup-mhra-commission-makes-recommendations-on-ai-regulatory-framework-in-the-uk.html
20. CDSCO, Draft guidance document on Medical Device Software (2025-10-21): https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/UploadPublic_NoticesFiles/Draft%20guidance%20document%20on%20Medical%20Device%20Software%2021%2010%202025.pdf
21. India Briefing, CDSCO moves to regulate medical device software: https://india-briefing.com/news/cdsco-draft-guidance-medical-software-40691.html
22. IBA, India's new telemedicine guidelines: https://www.ibanet.org/article/15234243-b534-45f6-b303-4919cfe9a2dc
23. Conventus Law, Note on Telemedicine Practice Guidelines: https://conventuslaw.com/report/india-note-on-telemedicine-practice-guidelines/
24. FTC, Mobile Health Apps Interactive Tool: https://www.ftc.gov/business-guidance/resources/mobile-health-apps-interactive-tool
25. FTC, Complying with FTC's Health Breach Notification Rule: https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0
26. FTC, Health Breach Notification Rule (rule page): https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule
27. FTC, FTC Withdraws Obsolete Policy Statement (2026-09-09): https://www.ftc.gov/news-events/news/press-releases/2026/09/ftc-withdraws-obsolete-policy-statement
28. FTC, Enforcement action to bar GoodRx from sharing health info for advertising (2023-02-01): https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising
29. Sourcepoint, What to know about BetterHelp's FTC settlement: https://sourcepoint.com/blog/what-to-know-about-betterhelps-ftc-health-data-privacy-settlement/
30. Lawdragon, Jury finds Meta liable for misusing women's health data (Flo): https://www.lawdragon.com/news-features/2025-08-25-big-tech-on-trial-jury-finds-meta-liable-for-misusing-women-health-data
31. Washington RCW 19.373.010 (MHMDA definitions): https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010
32. Washington RCW 19.373.030 (consent): https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.030
33. Washington RCW 19.373.090 (enforcement): https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.090
34. Davis Wright Tremaine, Nevada SB 370 tracker: https://dwt.com/gcp/state-privacy-laws-tracker/broad-state-privacy-law-tracker/nevada
35. Clark Hill, The New Health Data Laws Every Retailer Must Know: https://media.clarkhill.com/wp-content/uploads/2025/10/12140220/The-New-Health-Data-Laws-Every-Retailer-Must_11.11.pdf
36. Connecticut AG, The Connecticut Data Privacy Act: https://portal.ct.gov/ag/sections/privacy/the-connecticut-data-privacy-act
37. NY Senate, S929 (NY Health Information Privacy Act): https://www.nysenate.gov/legislation/bills/2025/S929
38. CPPA, CCPA Updates, Cybersecurity Audits, Risk Assessments and ADMT regulations: https://cppa.ca.gov/regulations/ccpa_updates.html
39. Morrison Foerster, CCPA regulations on cybersecurity, risk assessments and ADMT: https://www.mofo.com/resources/insights/251007-ccpa-regulations-on-cybersecurity-risk-assessments
40. DLA Piper, CCPA 2025 updated regulations: https://www.dlapiper.com/insights/publications/2025/09/ccpa-2025-updated-regulations
41. Jackson Lewis, CCPA: 30 essential FAQs for covered businesses: https://www.jacksonlewis.com/insights/navigating-california-consumer-privacy-act-30-essential-faqs-covered-businesses-including-clarifying-regulations-effective-1126
42. Illinois 740 ILCS 14/10 (BIPA definitions): https://lig.ilga.gov/legislation/ilcs/documents/074000140K10.htm
43. Texas Bus. & Com. Code §503.001 (CUBI): https://texas.public.law/statutes/tex._bus._and_com._code_section_503.001
44. Federal Register (govinfo), COPPA Rule amendments (2025-04-22): https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm
45. Google AI Edge, MediaPipe Pose Landmarker: https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker
46. EDPB, Guidelines 3/2019 on processing of personal data through video devices (PDF): https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_en_0.pdf
47. ICO, Biometric data guidance: biometric recognition: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/
48. GDPR Article 4 (definitions), gdpr-info.eu: https://gdpr-info.eu/art-4-gdpr/
49. ICO, Statement on the commencement of the DUAA (2026-02-05): https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/
50. DLA Piper, UK: commencement of the DUAA data protection provisions: https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/
51. WilmerHale, CJEU to review challenge to EU-U.S. Data Privacy Framework: https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework
52. Acompli, Digital Omnibus GDPR and cookie reforms stall (Sept 2026): https://acompli.ie/news/digital-omnibus-gdpr-cookies-status-september-2026/
53. SCC Online, MeitY notified Digital Personal Data Protection Rules 2025: https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/
54. AZB & Partners, DPDP Act phased rollout and key milestones: https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/
55. S.S. Rana, MeitY plans to cut short DPDP compliance timeline (2026-02-13): https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/
56. dpdprules.org, Is the 18-month window being cut to 12 months?: https://dpdprules.org/blog/dpdp-18-months-to-12-months-proposal
57. IIT BHU, DPDP Act and Rules summary: https://iitbhu.ac.in/contents/institute/cf/cis/doc/dpdp_act_rules_summary.pdf
58. EY India, DPDP Act 2023 and Rules 2025 point of view: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/pdf/2025/11/ey-india-dpdp-act-2023-and-rules-2025-pov.pdf
59. Goodwin, EU AI Act transparency obligations now in force (Aug 2026): https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force
60. Jones Walker, Yes, August 2 still matters: https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html
61. EU AI Act Article 50: https://artificialintelligenceact.eu/article/50/
62. EU AI Act Article 6: https://artificialintelligenceact.eu/article/6/
63. EU AI Act Recital 18: https://artificialintelligenceact.eu/recital/18/
64. JD Supra (McDermott), Colorado AI law in flux (2026-05-28): https://www.jdsupra.com/legalnews/colorado-ai-law-in-flux-comprehensive-2107294/
65. Akin, Colorado postpones implementation of SB 24-205: https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205
66. Future of Privacy Forum, Enacted AI Legislation Chart (Feb 2026): https://fpf.org/wp-content/uploads/2026/02/Enacted-AI-Legislation-Chart-.pdf
67. Carpenter Wellington, New state AI companion chatbot laws impose safety standards: https://carpenterwellington.com/post/new-state-ai-companion-chatbot-laws-impose-safety-standards/
68. Future of Privacy Forum, Chatbots in check: Utah's latest AI legislation: https://fpf.org/?p=244909
69. CASRAI, AI therapy laws: Illinois, Nevada, Utah compared: https://casrai.org/compare/ai-therapy-laws-illinois-nevada-utah-compared
70. FTC, Operation AI Comply (2024-09-25): https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
71. FTC, Inquiry into AI chatbots acting as companions (2025-09-11): https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions
72. Hogan Lovells, India introduces mandatory labelling for AI: https://www.hoganlovells.com/en/publications/india-introduces-mandatory-labelling-for-ai-and-3hour-takedown-for-illegal-content
73. Khaitan & Co, ASCI Guidelines on SGC labelling (2026-10-12): https://www.khaitanco.com/sites/default/files/2026-10/Ergo_ASCI%20Guidelines%20on%20SGC%20Labelling_12%2010%202026.pdf
74. Exchange4media, ASCI issues guidelines on labelling AI-generated ad content: https://www.exchange4media.com/advertising-news/asci-issues-guidelines-on-responsible-labelling-of-ai-generated-ad-content-158710.html
75. Apple, App Review Guidelines (last updated 2026-06-08): https://developer.apple.com/app-store/review/guidelines/
76. Apple, Offering account deletion in your app: https://developer.apple.com/support/offering-account-deletion-in-your-app/
77. Apple, App privacy details on the App Store: https://developer.apple.com/app-store/app-privacy-details/
78. Google Play, Health Content and Services policy: https://support.google.com/googleplay/android-developer/answer/16679511
79. Google Play, User Data policy: https://support.google.com/googleplay/android-developer/answer/10144311
80. Google Play, Health Connect permissions policy: https://support.google.com/googleplay/android-developer/answer/9888170
81. Google Play, AI-Generated Content policy: https://support.google.com/googleplay/android-developer/answer/13985936
82. Google Play, Data safety section: https://support.google.com/googleplay/android-developer/answer/10787469
83. Google Play, Target API level requirements: https://support.google.com/googleplay/android-developer/answer/11926878
84. Google, Google Fit APIs: https://developers.google.com/fit
85. FTC, Health Products Compliance Guidance: https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance
86. ASA/CAP, CAP Code Section 13 (weight control and slimming): https://www.asa.org.uk/type/non_broadcast/code_section/13.html
87. India Code, Drugs and Magic Remedies (Objectionable Advertisements) Act 1954: https://www.indiacode.nic.in/indiacode/bitstream/123456789/1412/1/A1954-21.pdf
88. Fox Mandal, Advisory limits self-declaration requirement to food and health ads: https://foxmandal.in/News/new-advisory-limits-self-declaration-requirement-to-food-health-ads/
89. FTC, Negative Option Rule: https://www.ftc.gov/legal-library/browse/rules/negative-option-rule
90. Gibson Dunn, FTC restarts negative option rulemaking after Eighth Circuit vacatur: https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/
91. FTC, Historic $2.5 billion settlement against Amazon (2025-09-25): https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon
92. Barnes & Thornburg, California expands Automatic Renewal Law: https://btlaw.com/en/insights/alerts/2025/california-expands-automatic-renewal-law-new-requirements-now-in-effect
93. Sheppard Mullin, California's auto-renewal law takes effect on July 1: https://www.sheppard.com/insights/blogs/californias-auto-renewal-law-takes-effect-on-july-1
94. European Commission, Consumer Rights Directive: https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en
95. Hogan Lovells, EU mandatory withdrawal button: https://www.hoganlovells.com/en/publications/eu-consumer-protection-law-update-new-mandatory-withdrawal-button-what-online-traders-need-to-know
96. Van Bael & Bellis, The online withdrawal button (2026-06-08): https://vbb.com/wp-content/uploads/2026/06/8-06-26-The-online-withdrawal-button.pdf
97. GOV.UK, Consultation on the new subscription contracts regime: https://www.gov.uk/government/consultations/consultation-on-the-implementation-of-the-new-subscription-contracts-regime
98. RBI, Processing of e-mandates for recurring transactions (2023-12-12): https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12570&Mode=0
99. RBI, e-mandate notification: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12341
100. JSA, CCPA (India) Guidelines for Prevention and Regulation of Dark Patterns 2023: https://www.jsalaw.com/?p=49613
101. Exchange4media, CCPA gives e-commerce players 3 months to root out dark patterns: https://www.exchange4media.com/marketing-news/ccpa-gives-ecomm-players-3-months-to-root-out-dark-patterns-144202.html
102. W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
103. European Commission, European Accessibility Act: https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en
104. iubenda, European Accessibility Act guide: https://www.iubenda.com/en/help/179096-eaa-compliance
105. CASRAI, Colorado AI Act explained: https://casrai.org/guides/colorado-ai-act-explained

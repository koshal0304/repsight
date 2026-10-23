# R6: Novelty Check for Candidate "Unique" Features (Camera Form Correction + Fitness/Diet/Medication AI Coach)

As of 2026-10-16. Written for the people drafting the BRD, Technical Specification, Roadmap & Strategy, Innovative Features and Build Playbook documents. Inline links use the numbering in the Sources section.

## Summary

- **The core idea is not new on its own.** Peloton IQ (launched 2025-10-01) gives real-time camera form feedback with visual and audio cues, counts reps, suggests weights and auto-logs workouts on the Cross Training Bike+, Tread+ and Row+ [[1]](https://www.onepeloton.com/peloton-iq) [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features) [[3]](https://www.axios.com/2025/10/01/peloton-cross-training-ai-bike). Tonal 2 has "Smart View with Coaching Cues" [[5]](https://knowledge.tonal.com/kb/guide/en/troubleshooting-tonal-2-camera-YUcew2ZBxF/Steps/3980893), and many phone apps already offer live form checks (Kemtai, Zing Vision, Strive, AiKYNETIX, CueForm AI, CoachAI, formcoach AI) [[8]](https://www.sensai.fit/blog/best-ai-workout-form-check-apps-2026). Confidence: High.
- **AI health coach chat is mainstream too.** Fitbit's Gemini coach (preview October 2025, expanded February 2026) adjusts plans for injuries [[11]](https://blog.google/products-and-platforms/devices/fitbit/personal-health-coach-public-preview/) [[12]](https://www.techrepublic.com/article/news-fitbit-ai-coach-expands-ios-five-markets/). WHOOP Coach [[13]](https://apps.apple.com/us/app/whoop/id933944389) and the MyFitnessPal Premium AI Coach [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718) do similar work. Confidence: High.
- **Medication awareness is the least-served and most regulated area.** Apple Watch counts "medications that might affect your heart rate" in its cardio fitness (VO2 max) estimate [[16]](https://support.apple.com/en-us/108790). Samsung Health warns about drug–drug and drug–food/caffeine/alcohol interactions [[17]](https://www.androidcentral.com/apps-software/samsung-health-medications). Noom and MyFitnessPal have GLP-1 features [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718) [[15]](https://apps.apple.com/us/app/noom-healthy-weight-loss/id634598719). No shipping product was found that changes the training plan itself from a medication list (C1). Verdict: NOVEL. Confidence: Medium.
- **Medication data is now readable.** Apple's HealthKit Medications API (WWDC25) gives apps read access to medications and dose events, coded in RxNorm, with permission granted per medication [[18]](https://developer.apple.com/videos/play/wwdc2025/321/). Android Health Connect Medical Records accepts FHIR medication records, but it is experimental and needs the Android 16 SDK [[19]](https://developer.android.com/health-and-fitness/health-connect/medical-records) [[20]](https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format). Confidence: High.
- **FDA rules constrain C1, C6, C12, C14 and C18.** The General Wellness guidance (2026-01-06) excludes products with outputs "used to make treatment decisions (e.g., medication dosing)", references to diseases or diagnostic thresholds, or "prompts that recommend or require specific clinical action". It also lists a claim to "treat muscle atrophy" as a non-wellness claim [[21]](https://www.fda.gov/media/90652/download). Confidence: High.
- **Camera velocity tracking (VBT) already exists.** Metric VBT gives an audio alert at a velocity-loss threshold you set (5–45%) [[32]](https://www.metric.coach/articles/introducing-real-time-feedback); SetSync measures velocity loss with a "fatigue cutoff" [[34]](https://setsync.app/); RepSpeed has stop thresholds [[35]](https://apps.apple.com/us/app/repspeed/id1584279988). No single phone product combines velocity loss, form drift and automatic next-set prescription (C2). It is the strongest training feature in the list, even though no single part of it is new.
- **Accuracy is the main limit.** A 2024 PeerJ study found poor-to-moderate agreement between Metric's mean velocity and a Vicon lab system [[33]](https://peerj.com/articles/17789). A 2026 roundup calls single-camera tools "screening aids rather than measurement instruments" [[8]](https://www.sensai.fit/blog/best-ai-workout-form-check-apps-2026). Confidence: Medium.
- **Several candidates are crowded and easy to copy:** equipment scanning (C4: GymScan, GymVision, Vyro, ANDES, LiftLens) [[49]](https://apps.apple.com/us/app/gymscan-gym-equipment-scanner/id6751796947) [[50]](https://apps.apple.com/us/app/gymvision/id6752872750); camera-verified rep duels (C5: RepChamp, FitDuel, REPcount, FITROX) [[54]](https://play.google.com/store/apps/details?id=com.repchamp.app&hl=en) [[55]](https://play.google.com/store/apps/details?id=com.thefitduel) [[56]](https://apps.apple.com/ch/app/repcount-exercise-counter/id6756521008?l=en-GB); ghost and overlay replays (C10: SetSync, OnForm, RivalRep) [[34]](https://setsync.app/) [[75]](https://apps.apple.com/US/app/id1490334045).
- **Clinical MSK companies (Hinge Health, Sword Health, Kemtai) already measure ROM, symmetry and rep quality by camera with clinicians in the loop, but sell B2B** [[39]](https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools) [[64]](https://swordhealth.com/newsroom/introducing-phoenix) [[66]](https://kemtai.com/product). Consumer strength apps do not do this.
- **"Video never leaves your phone" (C15) is a common claim, not a differentiator.** REPcount, RepChamp, Form Coach, formcoach AI and Sency all make it [[56]](https://apps.apple.com/ch/app/repcount-exercise-counter/id6756521008?l=en-GB) [[46]](https://nocamels.com/?p=110976). Treat it as a trust requirement.
- **Two exact specs were not found anywhere:** the full C1 engine, and C9's camera alert for a failed rep or pinned bar. Fall detection on watches and Tonal's motorized Spotter already exist [[73]](https://support.apple.com/en-us/108896) [[6]](https://tonal.com/blog/why-tonals-spotter-is-a-game-changer). Confidence: Medium/Low, because searching stopped early.
- **Our uniqueness has to come from the combination.** No product found combines live phone-camera form tracking, medication-aware training changes, diet coaching tied to training and medications, and sharing with a clinician. Confidence: Medium.
- **Recommended headline features:**
  1. A Safety & Context Layer that knows the user's medications, kept in wellness framing, with limits set by the user's clinician (C1+W2).
  2. Camera autoregulation with "quality volume" (C2+C16).
  3. Pain-aware adaptation with live ROM caps and a report to share with a physio (C6+C11+W1).
  4. A GLP-1 strength-preservation track with camera functional tests (C12+W4).

  Push C4, C5, C10, C17 and C18 later. Use C8 (voice) as the way users interact with the product, not as a headline.

## Method, definitions and limits

- **Evidence base:** about 45 web searches and 45 direct page fetches on 2026-10-16. Sources were official product pages, App Store and Google Play listings, FDA documents, Apple and Android developer docs, and peer-reviewed abstracts. A shared search budget ran out partway through, so Reddit sweeps, patent databases and some vendor pages were not checked (see "Unverified / conflicting").
- **Classes:** NOVEL = no shipping implementation found; NICHE = small or B2B products only; MAINSTREAM = a major app or wearable (Apple, Google/Fitbit, Samsung, Peloton, Tonal, WHOOP, Oura, MyFitnessPal, Noom, Fitbod) or a large clinical MSK company (Hinge Health, Sword Health). The **Verdict** grades the candidate's main novelty claim; **Exact spec found?** says whether any single product does the whole candidate.
- **Ratings:** Impact 1–5; Feasibility 1–5 (3–6 engineers, phone-only, 6–12 months); Defensibility 1–5 (proprietary data, clinical validation, network effects); Regulatory risk Low/Med/High under the US FDA wellness and CDS guidance of January 2026 (EU, UK and India not assessed).
- Vendor accuracy figures and user counts are reported as claims, not facts.

## 1. What the core already competes with

| Capability | Mainstream | Niche / B2B | Implication |
|---|---|---|---|
| Live camera form feedback + rep counting | Peloton IQ on Cross Training Bike+ ($2,695), Tread+ ($6,695), Row+ ($3,495); All-Access goes to $49.99/mo [[3]](https://www.axios.com/2025/10/01/peloton-cross-training-ai-bike) [[4]](https://athletechnews.com/peloton-new-era-ai-fitness-coaching-equipment-overhaul/). Tonal 2 Smart View [[5]](https://knowledge.tonal.com/kb/guide/en/troubleshooting-tonal-2-camera-YUcew2ZBxF/Steps/3980893). Tempo joint tracking through the iPhone camera [[7]](https://apps.apple.com/app/id1501671678) | Kemtai, Zing Vision, Strive, AiKYNETIX, CueForm AI, FormCheck AI [[8]](https://www.sensai.fit/blog/best-ai-workout-form-check-apps-2026); CoachAI [[68]](https://apps.apple.com/us/app/coach-ai/id6504732473); formcoach AI [[69]](https://hunted.space/product/formcoach-ai-form-coach); Rep-IQ (waitlist) [[89]](https://rep-iq.app/) | Not a differentiator. Barbell lifts are still weak because the bar hides body keypoints [[8]](https://www.sensai.fit/blog/best-ai-workout-form-check-apps-2026) |
| Automatic next-weight suggestion | Peloton IQ uses form and rep performance [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features); Tonal adaptive weight and Spotter [[6]](https://tonal.com/blog/why-tonals-spotter-is-a-game-changer); Tempo asks reps in reserve (2021 review) [[93]](https://connectthewatts.com/2021/12/23/tempo-move-review-iphone-powered-fitness-for-great-value-with-an-even-better-design/) | Vitruve "Smart Auto-Regulation" (uses an encoder) [[36]](https://vitruve.fit/?p=678) | The phone-camera-plus-velocity version is the opening (C2) |
| Chat AI coach | Fitbit Gemini coach [[11]](https://blog.google/products-and-platforms/devices/fitbit/personal-health-coach-public-preview/); WHOOP Coach [[13]](https://apps.apple.com/us/app/whoop/id933944389); MyFitnessPal AI Coach [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718); Noom [[15]](https://apps.apple.com/us/app/noom-healthy-weight-loss/id634598719) | Vora (readiness score, Voice Chat; $12.99/mo) [[48]](https://askvora.com/voice-coaching) | Generic chat is a commodity. Grounding it in camera and medication data is not |
| Spoken in-workout coaching | Apple Workout Buddy (watchOS 26; on-device; English; needs headphones and an iPhone that supports Apple Intelligence) [[9]](https://9to5mac.com/2025/06/09/watchos-26/) [[10]](https://heise.de/-10475361); Peloton voice control and audio cues [[1]](https://www.onepeloton.com/peloton-iq) | CoachAI, formcoach AI, Form Coach, Tracked, Superset [[68]](https://apps.apple.com/us/app/coach-ai/id6504732473) [[71]](https://www.tracked.gg/features/voice-commands) | Voice is the expected interface (C8), not a moat |
| Medication tracking | Apple Health Medications plus a read API [[18]](https://developer.apple.com/videos/play/wwdc2025/321/); Samsung Health [[17]](https://www.androidcentral.com/apps-software/samsung-health-medications); WHOOP journal [[13]](https://apps.apple.com/us/app/whoop/id933944389); MyFitnessPal GLP-1 [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718) | Visible (manual heart-rate-zone guidance) [[27]](https://help.makevisible.com/en/articles/10632785-using-visible-with-medications-that-impact-heart-rate) | Medications are tracked but never turned into training decisions (C1) |

## 2. Scorecard

| ID | Candidate | Verdict | Exact spec found? | Closest existing (named) | Unique with our core? | Impact | Feas. | Def. | Reg. | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Medication-aware training engine | **NOVEL** | No | Apple VO2 max medication factor; Samsung interaction warnings; Visible/SmartGym manual zones; Enhance-d (type 1 diabetes) | **Yes, strongly** | 4 | 3 | 3 | **High** | M |
| C2 | Velocity loss + form drift autoregulation | NICHE | No | Metric VBT, SetSync, RepSpeed; Peloton IQ and Tonal (hardware) | Yes (the combination) | 4 | 3 | 3 | Low | M-H |
| C3 | Longitudinal movement fingerprint | NICHE | No (consumer lifting) | Hinge Movement Analysis (B2B), Apple Walking Asymmetry (gait only), AIMO | Partly | 3 | 3 | 4 | Med | M |
| C4 | Room/equipment scan + machine lens | NICHE (crowded) | Yes | GymScan, GymVision, Vyro, ANDES, LiftLens; Technogym/Liftd QR codes | No | 3 | 4 | 1 | Low | H |
| C5 | Camera-verified reps for challenges | NICHE | Yes (consumer) | RepChamp, FitDuel, REPcount, FITROX; AIMO (insurers) | Weak | 3 | 3 | 2 | Med | H |
| C6 | Pain-aware adaptation + physio report | MAINSTREAM (injury swaps) | No | Fitbod Injuries/Limitations, Fitbit coach; Injurymap; Hinge/Sword | Yes, if ROM caps are camera-enforced | 4 | 4 | 3 | Med | M |
| C7 | 60-second movement screen + readiness | NICHE | Partly | BLACKROLL app, SquatScreen, AIMO, Sency, Hinge | Weak | 3 | 4 | 2 | Low (Med if it claims injury risk) | M |
| C8 | Hands-free conversational voice coach | MAINSTREAM (partial) | No | Peloton IQ voice and audio cues; Apple Workout Buddy; CoachAI, formcoach AI, Tracked (voice RPE) | Partly (capturing pain and effort) | 4 | 3 | 2 | Low | H |
| C9 | Spotter/safety mode (camera) | **NOVEL** (camera version) | No | Apple Fall Detection; Tonal Spotter (motor) | Yes, but carries liability | 3 | 3 | 2 | Med | M-L |
| C10 | Ghost-rep overlay / replay | NICHE | Partly | SetSync ghost outline, OnForm overlay, RivalRep | No | 2 | 4 | 1 | Low | H |
| C11 | Coach/physio portal with AI-flagged clips | NICHE | No | TrueCoach (manual), Kemtai CARE, Sword, Hinge, SetSync coach portal | Yes, in a consumer-to-clinic flow | 4 | 4 | 3 | Med | M |
| C12 | GLP-1 companion | MAINSTREAM | Partly | Noom "Muscle Defense", MyFitnessPal GLP-1 | Only via camera-verified strength (+W4) | 5 | 4 | 2 | Med | H |
| C13 | Cycle/menopause-aware training | MAINSTREAM (insights) | Partly | WHOOP, Oura, Fitbit coach; Wild.AI (unverified) | No | 4 | 4 | 2 | Low | M |
| C14 | Meal photo tied to training load + meds | NICHE (full linkage) | No | MyFitnessPal Meal Scan, Noom AI logging; Hexis (load-based fuelling) | Yes (adding meds and camera load) | 4 | 4 | 2 | Med | M |
| C15 | 100% on-device video | NICHE (widespread) | Yes | REPcount, RepChamp, Form Coach, formcoach AI, Sency | No (table stakes) | 4 | 4 | 1 | Low | H |
| C16 | Form-quality-adjusted progress | NICHE (partial) | No | FitDuel (clean reps only), Rep-IQ per-rep score, Peloton IQ form-aware weights | Yes (a PR ledger that counts only quality reps) | 3 | 3 | 3 | Low | M |
| C17 | Multi-person tracking with one phone | NICHE (for coaching) | No (phone strength coaching) | Nex Playground (up to 4 players, motion games), Lumin studios, GymCam research | Weak | 2 | 2 | 2 | Low | M |
| C18 | Return to training with clinician clearance | NICHE (clinical/research) | No (consumer) | Hinge/Sword PT programs; Back in the Game research app; return-to-play platforms | Yes (B2B2C) | 3 | 2 | 4 | **High** | L-M |

## 3. Candidate-by-candidate evidence

Ratings are in the Scorecard; each entry below gives only the reasoning behind them.

### C1. Medication-aware training engine: NOVEL as a whole (Confidence: Medium)

- **Exists, measurement correction (mainstream):** Apple's cardio fitness estimate counts "Medications that might affect your heart rate" and warns that they "might cause an overestimation of your VO2 max" [[16]](https://support.apple.com/en-us/108790). An Apple patent family describes selecting beta blockers when setting up low-cardio-fitness notifications [[26]](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11194455). Neither changes the training advice.
- **Exists, interaction warnings and logging (mainstream):** Samsung Health Medications (US December 2023, India October 2024) sends reminders and warns about drug–drug and drug–food/caffeine/alcohol interactions, e.g. simvastatin with grapefruit [[17]](https://www.androidcentral.com/apps-software/samsung-health-medications). WHOOP logs medication as one of 160+ journal behaviors [[13]](https://apps.apple.com/us/app/whoop/id933944389). MyFitnessPal logs GLP-1 side effects and sends dose reminders [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718). None links to exercise.
- **Exists, manual workarounds (niche):** Visible tells members on heart-rate-altering drugs such as beta blockers to re-set their zones until they match perceived effort [[27]](https://help.makevisible.com/en/articles/10632785-using-visible-with-medications-that-impact-heart-rate). SmartGym recommends custom zones for beta-blocker users [[28]](https://help.smartgymapp.com/article/152-how-to-set-custom-heart-rate-zones). Both rest on the fact that beta blockers blunt the heart-rate response, so perceived exertion (RPE) is the usual substitute [[31]](https://pmc.ncbi.nlm.nih.gov/articles/PMC6087665).
- **Exists, type 1 diabetes (niche):** Enhance-d shows glucose response to workouts. It has 20 ratings and gives no dosing or carbohydrate prescriptions [[29]](https://apps.apple.com/us/app/enhance-d/id6497331467). The PACTAID app is still in a clinical trial [[30]](https://clinicaltrials.gov/study/NCT06730906).
- **Not found:** any product that changes exercise choice, the intensity measure (heart rate vs RPE), timing, fuelling or safety prompts based on a medication list.
- **With our core:** strongly unique. The camera and voice add three things heart-rate apps lack:
  - ROM and strength drops, which can feed muscle-symptom check-ins;
  - fall- and impact-aware exercise filtering;
  - RPE captured by voice when heart rate is unreliable.
- **Why the ratings:** data access is solved (HealthKit read API with RxNorm codes [[18]](https://developer.apple.com/videos/play/wwdc2025/321/); Health Connect FHIR medications, still experimental [[20]](https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format)). Feasibility therefore depends on clinically reviewed rules and testing. The moat is a versioned rule library with clinical review and outcome data, but Apple, Google and Samsung already hold users' medication lists. Regulatory risk is High (section 4).
- **For the docs:** build it as a "Safety & Context Layer." It gives no dose advice and no numeric disease thresholds unless the product deliberately takes the medical-device (SaMD) route. Clinical values are set by the user's clinician (W2).

### C2. Fatigue and form-breakdown autoregulation: NICHE (Confidence: Medium-High)

- **Exists, camera velocity tracking (niche):**
  - Metric VBT reads the phone camera at 60 fps, announces velocity for each rep, chimes for target zones and alerts at a velocity-loss threshold set between 5% and 45% (published 2024-06-17). It mentions no next-set prescription or form analysis [[32]](https://www.metric.coach/articles/introducing-real-time-feedback).
  - SetSync uses the plate as its measuring scale. From recorded video it reports bar speed, "velocity loss with a fatigue cutoff", load-velocity profiles and estimated 1RM, plus a beta form check covering 44 movements [[34]](https://setsync.app/).
  - RepSpeed has stop thresholds and spoken rep speed (beta). It has 17 ratings; v0.41.0 shipped 2025-12-23 [[35]](https://apps.apple.com/us/app/repspeed/id1584279988).
- **Exists, sensors and hardware:**
  - Vitruve's bar-mounted encoder beeps at intra-set velocity loss and offers "Smart Auto-Regulation & e1RM" [[36]](https://vitruve.fit/?p=678).
  - Perch puts 3D cameras on team racks [[37]](https://perch.fit/tracking).
  - Peloton IQ suggests weights based on "form, and rep performance" [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features).
  - Tonal's Spotter lowers the load on a struggling rep [[6]](https://tonal.com/blog/why-tonals-spotter-is-a-game-changer).
- **Not found:** one phone product combining velocity loss, form drift, a stop-the-set prompt and an automatic next-set prescription.
- **Why the ratings:** accuracy limits feasibility. A 2024 PeerJ study found poor-to-moderate agreement between Metric's mean velocity and Vicon [[33]](https://peerj.com/articles/17789); Metric's own comparison reports smaller error. The moat is a dataset linking fatigue to form.
- **For the docs:**
  - Use velocity loss relative to the set's first rep, not absolute m/s.
  - Calibrate scale from the plate or the user's height.
  - Prompt only above a confidence threshold, and always let the user override.
  - Present all numbers as estimates.

### C3. Longitudinal "movement fingerprint": NICHE (Confidence: Medium)

- **Exists:**
  - The iPhone measures walking asymmetry for its Walking Steadiness score. This covers walking only (iOS 15+) [[38]](https://appleinsider.com/articles/22/04/03/how-to-enable-walking-steadiness-notifications-in-ios-15).
  - Hinge Health's Movement Analysis (October 2025, built on TrueMotion) records joint angles, symmetry and endurance, and combines them with questions to produce "Hinge Scores". It is sold to businesses [[39]](https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools) [[40]](https://www.hingehealth.com/resources/articles/truemotion-turning-a-phone-camera-into-a-3d-motion-lab/).
  - AIMO turns compensations seen in a phone movement scan into a score for insurers [[44]](https://www.genre.com/us/knowledge/publications/2020/june/netletterrc20-2-de).
  - Research: a phone computer-vision app measuring knee valgus showed test-retest ICC of 0.859–0.933 and r = 0.931 against Kinovea, a free video-analysis tool. The retest gap was only one week [[41]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10177945/).
- **Not found:** a consumer lifting app that tracks asymmetry, ROM and compensations rep by rep over months and suggests prehab.
- **Why the ratings:** a longitudinal personal dataset is hard to copy (Defensibility 4). Regulatory risk rises to Med if it is framed as predicting injury.
- **For the docs:** use a standard monthly "check-in set" with the same camera angle and distance, and show trends with error bands.

### C4. Room/equipment scan and "machine lens": NICHE but crowded (Confidence: High)

- **Exists:**
  - GymScan claims to recognize 200+ machines in under 2 seconds and shows form guides and starter weights [[49]](https://apps.apple.com/us/app/gymscan-gym-equipment-scanner/id6751796947).
  - GymVision scans a video to find 94 equipment types and builds workouts for each saved "Space". It has 7 ratings [[50]](https://apps.apple.com/us/app/gymvision/id6752872750).
  - Vyro, ANDES, LiftLens, PhotoFit AI, NeuroFlex and SpotLift advertise the same. A Gymeo user reports that it misidentifies machines [[51]](https://mwm.ai/apps/gymeo-scan-workout-tracker/6748888066).
  - Without a camera: Liftd uses QR/NFC tags covering 1,300+ models from 50+ brands [[52]](https://play.google.com/store/apps/details?id=ai.liftd.android&hl=en_US), and the Technogym app logs a session from a QR code on the machine [[53]](https://stir.ac.uk/student-life/sport-at-stirling/health-and-fitness/technogym-training-app).
- **Why the ratings:** general-purpose multimodal AI models can identify equipment too, so there is no moat.
- **For the docs:** an onboarding convenience that reuses the meal-photo vision model. Do not headline it.

### C5. Camera-verified reps for challenges and proof of workout: NICHE (Confidence: High)

- **Exists:**
  - RepChamp: 1v1 duels and leaderboards; processing on the device and no video upload [[54]](https://play.google.com/store/apps/details?id=com.repchamp.app&hl=en).
  - FitDuel: "only clean reps score", with ranked leagues [[55]](https://play.google.com/store/apps/details?id=com.thefitduel).
  - REPcount: a "verified reps" social network that records no video [[56]](https://apps.apple.com/ch/app/repcount-exercise-counter/id6756521008?l=en-GB).
  - FITROX: push-up battles with a $500 monthly prize; the terms were not checked [[57]](https://fitrox.app/).
  - RepCam AI [[90]](https://play.google.com/store/apps/details?id=com.repcamai.app&hl=en).
  - Peloton IQ: camera-logged workouts count toward challenges and streaks [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features).
  - Insurers: AIMO says its score was validated with Zurich, Momentum, Talanx, HDI and Gen Re [[44]](https://www.genre.com/us/knowledge/publications/2020/june/netletterrc20-2-de). The AIMO Fit app is tied to reimbursement by German statutory health insurers [[45]](https://apps.apple.com/app/id1621294451).
- **Not found:** verification that resists cheating (spoof-resistant) for employer or insurer incentive programs at scale.
- **Why the ratings:** cash prizes bring contest/sweepstakes law and insurer incentives bring wellness-program rules (Med; neither assessed here).
- **For the docs:** P2. If built, it needs device attestation, liveness checks and server-side plausibility checks.

### C6. Pain-aware adaptation: MAINSTREAM for injury-based swaps; full spec not found (Confidence: Medium)

- **Exists (mainstream):**
  - Fitbod's "Injuries / Limitations" removes exercises that load the injured area and suggests alternatives, labelled "not medical advice" [[58]](https://help.fitbod.me/hc/en-us/articles/37629269518103). Its App Store listing does not mention the feature [[59]](https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543).
  - Fitbit's coach adjusts plans when told "My knee is bugging me" [[11]](https://blog.google/products-and-platforms/devices/fitbit/personal-health-coach-public-preview/).
  - Freeletics limits its "Limitations" feature to muscle soreness (DOMS), not injuries [[60]](https://www.freeletics.com/en/blog/posts/coach-feedback/).
- **Exists (niche):**
  - Injurymap adjusts the plan after each session from pain and effort feedback [[61]](https://apps.apple.com/us/app/injurymap-physiotherapy-app/id1102375789). One source says the Danish Medicines Agency approved it for muscle and joint pain [[62]](https://ds-sundhed.dk/en/injurymap/), a sign that pain-driven adaptation pulls products toward medical-device status.
  - The Prehab app lets users swap exercises manually [[63]](https://apps.apple.com/us/app/prehab-physical-therapy-pain/id1626839977).
  - Sword and Hinge run clinician-led programs [[64]](https://swordhealth.com/newsroom/introducing-phoenix) [[39]](https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools).
- **Not found:** body-map pain check-ins, plus a live camera ROM cap (e.g. squat depth held to the pain-free range), plus a pain/ROM trend report to share with a physio.
- **For the docs:** call it "train around discomfort." Add red-flag questions that route the user to a clinician, and avoid "treat" or "rehab" claims.

### C7. 60-second movement screen with corrective plan and readiness: NICHE (Confidence: Medium)

- **Exists:**
  - BLACKROLL's app analyzes an overhead squat through the phone camera, sorts it into "several predefined types of dysfunction" and suggests exercises. It is labelled "not a medical diagnosis" [[42]](https://blackroll.com/eu/en/service/transparenz-blackroll-app).
  - SquatScreen and PostureScreen are paid professional tools that suggest corrective exercises [[43]](https://appfollow.io/ios/squatscreen/1249748805?country=us).
  - Sency runs assessments on the device and claims 1.5M+ members across its partners (2024) [[46]](https://nocamels.com/?p=110976) [[47]](https://athletechnews.com/sency-transforms-fitness-market-ai-motion-tracking/).
  - AIMO [[45]](https://apps.apple.com/app/id1621294451) and Hinge Movement Analysis [[39]](https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools) also screen movement.
  - Readiness scores are common in wearable apps, e.g. Vora's 0–100 score [[48]](https://askvora.com/voice-coaching).
- **Not found:** a daily readiness signal based on camera movement quality.
- **For the docs:** use the screen for onboarding and repeat it monthly. Do not market a camera readiness score until it has been validated against an outcome.

### C8. Hands-free conversational voice coach: MAINSTREAM in part (Confidence: High)

- **Exists (mainstream):**
  - Peloton IQ has "Ok Peloton" voice control, "Accept" to take a suggested weight, and audio form cues [[1]](https://www.onepeloton.com/peloton-iq) [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features).
  - Apple Workout Buddy (watchOS 26) gives spoken encouragement on the device, based on heart rate, pace, rings and milestones, in a voice built from Fitness+ trainers. It is not form coaching and not a two-way conversation [[9]](https://9to5mac.com/2025/06/09/watchos-26/) [[10]](https://heise.de/-10475361).
- **Exists (niche):**
  - CoachAI speaks rep counts and posture cues mid-set, every rep, 5 reps or 10 reps [[68]](https://apps.apple.com/us/app/coach-ai/id6504732473).
  - formcoach AI runs Apple Vision and Speech on the device and takes voice commands [[69]](https://hunted.space/product/formcoach-ai-form-coach).
  - Form Coach gives voice cues on the device [[70]](https://mwm.ai/apps/form-coach/6770110788).
  - Tracked logs weight, reps and RPE by voice [[71]](https://www.tracked.gg/features/voice-commands).
  - Superset logs sets you speak aloud [[72]](https://trysuperset.app/best).
- **Not found:** a real-time voice coach the user can talk to and interrupt, which also records pain and effort and knows the user's medication context.
- **Why the ratings:** latency, noisy gyms and interruptions limit feasibility, and voice on its own is no moat.

### C9. Spotter/safety mode: NOVEL as a camera feature; MAINSTREAM without one (Confidence: Medium-Low)

- **Exists:**
  - Apple Watch Fall Detection turns on automatically for users aged 55+ and can be set to "Only on during workouts". After about a minute without movement it counts down 30 seconds, then calls emergency services and sends the user's location to their emergency contacts [[73]](https://support.apple.com/en-us/108896).
  - Tonal's Spotter lowers the load on a struggling rep and restores it afterwards [[6]](https://tonal.com/blog/why-tonals-spotter-is-a-game-changer).
  - RepSpeed classifies a failed lift as technical or strength-related, but only after the set [[35]](https://apps.apple.com/us/app/repspeed/id1584279988).
  - GymCam (Carnegie Mellon research) tracks several exercisers with one camera [[74]](https://karan-ahuja.com/gymcam.html).
- **Not found:** live phone-camera detection of a pinned or stalled bar, or a collapse, with an alert and escalation.
- **Why the ratings:** telling a deliberate rest from a pinned lifter is hard. The main exposure is product liability, not FDA.
- **For the docs:** use the watch's fall detection where the user has one. The camera adds a heuristic of "no movement plus bar in a pinned position". Label it beta and never present it as a safety guarantee.

### C10. Ghost-rep overlay: NICHE (Confidence: High)

- **Exists:**
  - SetSync compares up to 4 lifts side by side, overlaid, or as a "ghost outline", lined up by phase. Pro costs $9.99 one-time at launch, then $14.99 [[34]](https://setsync.app/).
  - OnForm offers overlay comparison and skeleton tracking for coaches [[75]](https://apps.apple.com/US/app/id1490334045).
  - RivalRep has you race a "ghost" of your own personal best at push-ups and pull-ups [[76]](https://dev.to/rivalrep_creator/i-built-an-app-to-duel-your-past-self-in-push-ups-and-pull-ups-1k9b).
  - Coach's Eye offers side-by-side comparison [[77]](https://vitruve.fit/blog/top-10-camera-based-apps-for-tracking-your-athletes-workouts/).
- **Not found:** a live AR "ghost" of the user's own best rep during the set. Replay after the set is common.
- **For the docs:** ship it only as replay with timestamped errors marked on it. This reuses the C11 clip pipeline.

### C11. Coach/physio portal with AI-flagged rep clips: NICHE (Confidence: Medium)

- **Exists (manual):** TrueCoach clients attach form videos per set for their coach to review [[78]](https://capterra.com/p/155784/truecoach/reviews/). Trainerize users have asked for built-in form videos and work around it with messages or Loom [[79]](https://ideas.abcfitness.com/forums/167887-coach-trainer-abc-trainerize/suggestions/38467258-allow-videos-photos-to-be-attached-for-comments-f).
- **Exists (AI-assisted, B2B):**
  - Kemtai's clinician app reports adherence and performance per user, per exercise and per rep. KemtaiCARE is reported as FDA-listed and 510(k)-exempt [[66]](https://kemtai.com/product) [[67]](https://intuitionlabs.ai/software/physical-occupational-therapy/rom-and-goniometry-tracking/kemtai).
  - Sword's Phoenix summarizes each session for the clinician [[65]](https://medcitynews.com/2024/06/sword-health-financing-ai-musculoskeletal/).
  - SetSync has web portals for coaches and athletes, priced $11.99–$34.99/mo for coaches [[34]](https://setsync.app/).
- **Not found:** a consumer app that automatically picks out the worst reps as short clips for a coach or physio to review later.
- **Why the ratings:** the network of coaches and clinics is the moat. Clinic customers can bring HIPAA requirements, a business associate agreement (BAA) and billing for remote therapeutic monitoring (RTM), hence Med.
- **For the docs:** make clip sharing opt-in and per clip. This is the only flow that sends video off the phone (see C15).

### C12. GLP-1 / weight-loss-drug companion: MAINSTREAM (Confidence: High)

- **Exists:**
  - Noom advertises a "GLP-1 Companion Program with Muscle Defense™ to lose fat, protect muscle, & build healthy habits" [[15]](https://apps.apple.com/us/app/noom-healthy-weight-loss/id634598719).
  - MyFitnessPal lets users log how they feel on GLP-1 medications and set dose reminders. Its version 26.34.0 notes say the features are "now available in both the US and Canada" [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718).
  - WeightWatchers, Shotsy and GLP-1 content from Peloton or Tonal were not checked this session.
- **Our angle:** strength training whose dose is verified by the camera, plus monthly camera functional tests (W4) as a stand-in for lean mass and strength. Protein comes from photo logging (C14).
- **Why the ratings:** FDA lists "a claim that a product will treat muscle atrophy" as **not** a wellness claim [[21]](https://www.fda.gov/media/90652/download), hence Med.
- **For the docs:** say "maintain strength while losing weight", not "prevent drug-induced muscle loss".

### C13. Menstrual-cycle / menopause-aware training: MAINSTREAM for insights, NICHE for training prescription (Confidence: Medium)

- **Exists:**
  - WHOOP offers "tailored cycle-based insights" [[13]](https://apps.apple.com/us/app/whoop/id933944389).
  - Oura offers cycle patterns and a "Fertile Window" [[80]](https://apps.apple.com/us/app/oura/id1043837948).
  - Fitbit's coach covers life stages, with "menopause symptoms" as an example [[11]](https://blog.google/products-and-platforms/devices/fitbit/personal-health-coach-public-preview/).
  - Apps that change training by cycle phase (Wild.AI, FitrWoman) could not be checked. Wild.AI's domain did not resolve on 2026-10-16.
- **For the docs:** an option the user turns on, personalized from symptom check-ins rather than fixed per-phase rules. Avoid fertility or contraception claims.

### C14. Meal-photo logging tied to training load and medications: NICHE for the full linkage (Confidence: Medium)

- **Exists:**
  - Photo logging is mainstream. MyFitnessPal Premium offers "meal scan & voice logging" and an AI Coach that reads photos [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718). Noom offers AI meal logging [[15]](https://apps.apple.com/us/app/noom-healthy-weight-loss/id634598719).
  - Fuelling tied to training load is niche. Hexis "Carb Coding" colours each meal by the training already done and the training ahead. It integrates Garmin, TrainingPeaks, Intervals.icu, WHOOP and Apple Health, and mentions no photo logging [[81]](https://www.hexis.live/).
  - Medication-aware nutrition exists only inside GLP-1 programs [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718).
- **Not found:** a product that links a meal photo to both the camera-measured session and the medication schedule.
- **Why the ratings:** nutrition advice to people on insulin counts as disease management, hence Med.

### C15. Privacy-first, 100% on-device video: common claim, not novel (Confidence: High)

- **Exists:**
  - On-device claims from REPcount, RepChamp, Form Coach and formcoach AI [[56]](https://apps.apple.com/ch/app/repcount-exercise-counter/id6756521008?l=en-GB) [[54]](https://play.google.com/store/apps/details?id=com.repchamp.app&hl=en) [[70]](https://mwm.ai/apps/form-coach/6770110788) [[69]](https://hunted.space/product/formcoach-ai-form-coach), and from the Sency SDK [[46]](https://nocamels.com/?p=110976).
  - Apple Workout Buddy also processes on the device [[9]](https://9to5mac.com/2025/06/09/watchos-26/).
  - Peloton links to a Consumer Health Data Policy and makes no on-device claim [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features).
- **For the docs:** state the promise precisely: "raw video is processed on-device and never uploaded unless you share a clip." Keypoints and metrics still sync. This conflicts with C11 and with cloud LLMs, so define exactly what does leave the phone.

### C16. Form-quality-adjusted progress ("quality volume"): NICHE, partial (Confidence: Medium)

- **Exists:**
  - FitDuel scores "only clean reps" in duels [[55]](https://play.google.com/store/apps/details?id=com.thefitduel).
  - Rep-IQ scores every rep. It is still on a waitlist (£11.99/mo) and does not say whether bad reps are excluded from personal records [[89]](https://rep-iq.app/).
  - Peloton IQ takes form into account when suggesting weights [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features).
- **Not found:** a progress and PR ledger that counts only reps meeting a form standard.
- **Why the ratings:** false negatives (good reps marked bad) demotivate users, hence Feasibility 3.
- **For the docs:** show total volume and quality volume side by side. Never silently drop a rep, and set form standards per exercise.

### C17. Multi-person tracking with one phone: NICHE for coaching (Confidence: Medium)

- **Exists:**
  - Nex Playground, a camera console for motion games, tracks up to 4 players at once. The company says it sold 650k+ units in 2025 [[82]](https://naavik.co/digest/nex-playground-and-motion-gamings-second-act/) [[83]](https://insider-gaming.com/console-nex-playground-topped-ps5-sales-us/).
  - Lumin Fitness studios track reps at each workout station [[84]](https://athletechnews.com/?p=98528).
  - GymCam tracks many exercisers with one camera (research) [[74]](https://karan-ahuja.com/gymcam.html).
- **Not found:** strength-form coaching for several people from one phone.
- **Why the ratings:** people blocking each other, keeping track of who is who, and phone compute all limit feasibility. The privacy issues are consent from other people in the frame, and minors.

### C18. Return to training after injury with a clinician-clearance flow: NICHE, clinical or research (Confidence: Low-Medium)

- **Exists:**
  - Return-to-play platforms that gate progression on objective tests are rated early-stage (technology readiness level 6 of 9) [[85]](https://www.envisioning.com/research/stride/return-to-play-orchestration).
  - Back in the Game is an ACL-recovery app studied in research [[86]](https://www.epistemonikos.org/en/documents/245c0f7794966252849e97854e003668a4c8b19c).
  - Hinge and Sword run physical-therapist-led programs [[39]](https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools) [[64]](https://swordhealth.com/newsroom/introducing-phoenix).
- **Not found:** a consumer strength app with a clearance gate.
- **Why the ratings:** signing up clinicians is the hard part, and deciding clearance is a clinical decision, hence High.
- **For the docs:** the app records the clinician's clearance and enforces limits the clinician sets. It never decides clearance itself.

## 4. Regulatory guardrails that shape these features (US lens)

- **The two kinds of wellness claim.** FDA's General Wellness guidance (2026-01-06) allows two groups of claims [[21]](https://www.fda.gov/media/90652/download):
  - claims about a general state of health, such as "weight management" or "physical fitness," including "improve muscle size or body tone";
  - claims that a healthy lifestyle "may help reduce the risk of" or "may help living well with" certain chronic conditions. Examples given include type 2 diabetes and high blood pressure.
- **What takes a product out of wellness.** The same guidance excludes products whose labeling or functionality includes any of these [[21]](https://www.fda.gov/media/90652/download):
  - "references to specific diseases, clinical conditions, or diagnostic thresholds";
  - "alerts, alarms, or prompts that recommend or require specific clinical action";
  - "treatment guidance intended to inform or direct medical management";
  - outputs "used to make treatment decisions (e.g., medication dosing)."
- **What a notification may say.** A notification may suggest that evaluation by a healthcare professional "may be helpful." It must not name a disease, call a result abnormal, give thresholds or treatment advice, or keep alerting as a way of managing a disease [[21]](https://www.fda.gov/media/90652/download). This is the template for C1, C6 and C14 messages.
- **WHOOP precedent.** FDA sent WHOOP a warning letter over Blood Pressure Insights on 2025-07-14 [[24]](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-07142025). After WHOOP changed the feature, FDA sent a close-out letter on 2026-06-17 that covers only the modified version [[25]](https://www.massdevice.com/fda-closes-warning-letter-whoop-blood-pressure/). The lesson: claim wording and UI decide the outcome, not the sensor.
- **CDS guidance.** The clinical decision support guidance (2026-01-06) now gives enforcement discretion to software for healthcare professionals that presents a single recommendation, if it meets the other criteria [[22]](https://www.kslaw.com/insights/articles/fda-updates-general-wellness-and-clinical-decision-support-guidance-documents) [[23]](https://www.fda.gov/media/109618/download). This is relevant to the clinician portal (C11, W2). It does not cover software that gives advice directly to patients.
- **Phrasing to use and avoid:**

| Feature | Risky phrasing | Safer phrasing |
|---|---|---|
| C1 | "Your insulin dose means eat 20 g carbs if glucose < X" | "Glucose-lowering medicines can change how exercise feels. Plan snacks and check-ins with your care team" |
| C6 | "Treats knee pain" | "Train around discomfort; tell your physio if pain persists" |
| C12 | "Prevents GLP-1 muscle loss" | "Helps you keep strength while losing weight" |

## 5. Additional white-space ideas (up to 5)

| ID | Idea | Closest evidence | Class | Impact | Feas. | Def. | Reg. | Conf. |
|---|---|---|---|---|---|---|---|---|
| W1 | **Movement–symptom link**: correlate camera-measured compensations (valgus, depth, hip shift, asymmetry) and load with pain check-ins, e.g. "knee discomfort days follow sets where valgus grew late in the set"; shareable with a physio | Hinge combines movement measures and questions into Hinge Scores (B2B) [[39]](https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools); Fitbod injury swaps [[58]](https://help.fitbod.me/hc/en-us/articles/37629269518103); Injurymap pain feedback [[61]](https://apps.apple.com/us/app/injurymap-physiotherapy-app/id1102375789) | NOVEL in consumer apps | 4 | 3 | 4 | Med | M |
| W2 | **Clinician-set guardrails**: a physio, cardiac-rehab or diabetes clinician sets heart-rate/RPE ceilings, ROM limits, banned movements and medication cautions in a portal; the camera and voice coach enforce them and report adherence | Kemtai clinicians assign protocols and see rep-level data (rehab) [[67]](https://intuitionlabs.ai/software/physical-occupational-therapy/rom-and-goniometry-tracking/kemtai); Visible leaves medication zone changes to the user [[27]](https://help.makevisible.com/en/articles/10632785-using-visible-with-medications-that-impact-heart-rate) | NICHE in rehab, NOVEL for general strength | 4 | 3 | 4 | Med | M |
| W3 | **Personal cue learning**: the coach tries cue variants (internal vs external focus, analogies) and learns which cue fixes this user's fault fastest, measured on the next rep | CoachAI only lets users choose cue frequency [[68]](https://apps.apple.com/us/app/coach-ai/id6504732473); research on attentional focus in motor learning (Wulf) [[88]](https://doi.org/10.1080/1750984X.2012.723728) | NOVEL (not specifically searched) | 3 | 4 | 4 | Low | L-M |
| W4 | **Camera functional tests**: automated, CDC STEADI-style 30-second chair stand, 4-stage balance and Timed Up and Go tests, framed as monthly strength benchmarks for GLP-1 users and older adults | STEADI defines these tests for clinicians [[87]](https://www.cdc.gov/steadi/hcp/clinical-resources/index.html); Apple Walking Steadiness (walking only) [[38]](https://appleinsider.com/articles/22/04/03/how-to-enable-walking-steadiness-notifications-in-ios-15); Noom Muscle Defense [[15]](https://apps.apple.com/us/app/noom-healthy-weight-loss/id634598719) | NOVEL in consumer fitness (not specifically searched) | 4 | 4 | 3 | Med (Low if framed as fitness, not fall risk) | L-M |
| W5 | **Pre-workout stimulant/supplement check**: the user photographs a pre-workout or supplement label; caffeine and stimulants are checked against the medication list and today's heart rate, and the user is pointed to a pharmacist | Samsung Health warns about caffeine/alcohol/food interactions with medications, with no workout link [[17]](https://www.androidcentral.com/apps-software/samsung-health-medications); MyFitnessPal AI Coach reads photos [[14]](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718) | NOVEL in fitness (not specifically searched) | 3 | 3 | 3 | Med | L |

- **W1 and W2** turn camera and medication data into a clinician-facing asset and a B2B2C channel that Peloton and Fitbod lack.
- **W4** makes the crowded GLP-1 segment camera-native.
- **W5** needs a licensed drug-interaction data source; it stays informational and points users to a pharmacist.

## Recommendations for the docs

**BRD**
1. **Do not claim uniqueness** for camera form correction, AI chat coaching, voice coaching, equipment scanning, rep challenges, cycle syncing, GLP-1 support or on-device privacy. Each already ships (see the Scorecard).
2. **Position on the combination:** "a coach that sees every rep and knows your medications, pain and goals." Keep a claims register, and allow "first", "only" or "unique" only after a legal and evidence review.
3. **Priority tiers:**
   - **P0 (MVP):**
     - live form feedback and rep counting;
     - C8 voice cues plus voice logging of reps, RPE and pain;
     - the C15 on-device architecture;
     - C2-lite: velocity loss within the set plus form drift trigger a stop prompt, and the user confirms the suggested next set;
     - C1-lite Safety & Context Layer with three rule families, each reviewed by a clinician:
       - heart-rate-limiting drugs → RPE-first intensity;
       - glucose-lowering drugs → check-ins before and after the session, with no numeric thresholds;
       - GLP-1 drugs → resistance training and protein emphasis, in wellness wording.
   - **P1:** C6 with camera-enforced ROM caps; C16; C11 opt-in clips with W2 clinician guardrails; C12 with W4 tests; C14 linked to that day's measured session.
   - **P2:** C3 (it needs months of data anyway), C7 (an onboarding version can come earlier), W1, W3, and C13 as an option the user turns on.
   - **Backlog or partner-led:** C4 (cheap onboarding add-on), C5, C9 (beta, supplementing watch fall detection), C10 (replay only), C17, and C18 (only through clinic partners).
4. **Primary personas**, where the gap is real:
   - GLP-1 users who want to keep their strength;
   - adults on everyday cardiometabolic drugs (beta blockers, statins, glucose-lowering drugs);
   - people who lift alone at home;
   - patients moving from physio care into the gym.

**Technical Specification**
- **Medication ingestion.** On iOS, use the HealthKit Medications API (read-only, permission per medication, RxNorm codes) [[18]](https://developer.apple.com/videos/play/wwdc2025/321/). On Android, Health Connect Medical Records is experimental: it needs the Android 16 SDK and Jetpack 1.1.0-beta02, and its Play policy is still pending [[19]](https://developer.android.com/health-and-fitness/health-connect/medical-records). Spec manual entry with RxNorm lookup as the fallback on both.
- **Safety rules engine:**
  - deterministic and versioned;
  - each rule records its provenance (drug label or guideline), reviewer and effective date;
  - rules run before and after the LLM, and the LLM cannot override them;
  - the engine never outputs dosing;
  - every rule has unit tests.
- **Camera metrics:** each rep carries a confidence score, and prompts only fire above a threshold. Calibrate from the plate diameter or the user's height. Store keypoints and metrics, not video.
- **Data entities:** Rep (velocity, ROM, form flags, quality flag, confidence), Set, Session, PainCheckIn (body region, 0–10), MedicationContext, ClinicianGuardrail, SharedClip (consent, retention).
- **Clip pipeline (C10/C11):** cut the clip on the device and upload it encrypted only after consent for that clip, with a retention limit. This is the only route by which video leaves the phone.

**Roadmap and Strategy**
- **Build the moat in this order:**
  1. rep-level form, fatigue, pain and medication data;
  2. a clinician network (W2/C11);
  3. validated outcomes.
- **Competitor watch-list:**
  - Fitbit's Gemini coach, which already adapts to injuries and could add medications [[11]](https://blog.google/products-and-platforms/devices/fitbit/personal-health-coach-public-preview/);
  - Apple (medications API, Workout Buddy);
  - Peloton IQ's form-aware weight suggestions [[2]](https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features);
  - consumer moves by Hinge or Sword;
  - GLP-1 features at MyFitnessPal and Noom.

**Innovative Features doc**
- Give each feature an honest "exists elsewhere" line from the Scorecard.
- Headline the four bundles: C1+W2, C2+C16, C6+C11+W1, C12+W4.

**Build Playbook**
- **Validate before launch**, against thresholds set in advance:
  - camera velocity against a linear position transducer or encoder;
  - ROM against goniometer or Kinovea measurements;
  - rep-detection precision and recall across body types, clothing, lighting and camera angles.

  Remember the poor-to-moderate agreement reported for one camera VBT app [[33]](https://peerj.com/articles/17789).
- **Red-team the coach** with prompts about medication dosing, stopping medication and pain red flags. It must refuse dosing advice, escalate red flags and use the FDA-compatible notification template (section 4).
- **Regulatory gate.** C1, C6, C12, C14, C18, W2, W4 and W5 need regulatory review before release. All user-facing copy for these features gets checked against the FDA exclusion list.

## Unverified / conflicting

- **Search coverage was cut short.** The shared search budget ran out. Reddit, patent databases, Exer Health, Physitrack, Uplift Labs, DARI, My Jump Lab, HRV4Training, Cal AI, Oura Meals and perimenopause features, WHOOP Strength Trainer, WeightWatchers GLP-1, Shotsy, and Peloton/Tonal GLP-1 content were **not** verified. Some classifications could change. In particular, the NOVEL verdicts for C1, C9, W3, W4 and W5 rest on searches that found nothing, not on proof that nothing exists.
- **Fitbod Injuries/Limitations:** a help-center article describes the feature (the page returned 403 to a direct fetch; the description comes from a search snippet saying it was rolling out to iOS), but the App Store listing does not mention it [[58]](https://help.fitbod.me/hc/en-us/articles/37629269518103) [[59]](https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543).
- **Tempo and Tonal 2:** Tempo's current camera and reps-in-reserve features come from a listing and from reviews dated 2021–2023. For Tonal 2's Smart View, the only primary source is a support article.
- **Third-party app roundup:** details on Zing Vision, AiKYNETIX, CueForm AI, FormCheck AI and Strive come from a roundup written by a competing vendor (SensAI) [[8]](https://www.sensai.fit/blog/best-ai-workout-form-check-apps-2026).
- **Metric accuracy conflict:** the PeerJ 2024 finding came from a search snippet because the article returned 403. Metric's own comparison reports smaller error.
- **Hinge Movement Analysis** details come from press-release snippets; the direct fetch was blocked.
- **Injurymap** being approved by the Danish Medicines Agency rests on a single source [[62]](https://ds-sundhed.dk/en/injurymap/).
- **Nex Playground's** 650k units is a company claim.
- **Sency's** 1.5M members and "270% better engagement" are company claims from 2024.
- **AIMO's** list of insurer partners comes from its own marketing.
- **MyFitnessPal's** GLP-1 US/Canada rollout appears in version 26.34.0, dated "Aug 25." The year (likely 2026) is inferred from the version numbering.
- **Fitbit coach cycle and nutrition features:** a report says they were added after launch, but we could not read it (403), so the date is unclear. Coverage also conflicts on whether Premium is required [[12]](https://www.techrepublic.com/article/news-fitbit-ai-coach-expands-ios-five-markets/).
- **Peloton IQ eligibility:** the UK page limits features to Bike+, while US and AU pages name Bike+, Tread+ and Row+ [[1]](https://www.onepeloton.com/peloton-iq).
- **Clinical content for C1 is not verified here.** Examples are statin muscle symptoms, fluoroquinolone tendon risk, anticoagulant bleeding/fall caution and hypoglycemia management. All of it must come from drug labels and professional guidelines and be reviewed by clinicians before anything is built.
- **Non-US regulation** (EU MDR, UK MHRA, India CDSCO) was not assessed in this brief.

## Sources

1. Peloton IQ (US product page): https://www.onepeloton.com/peloton-iq
2. Peloton IQ strength training features (Peloton UK blog, 24 Nov 2025): https://www.onepeloton.com/en-GB/blog/peloton-iq-strength-training-features
3. Axios, Peloton debuts AI coaching and new products (1 Oct 2025): https://www.axios.com/2025/10/01/peloton-cross-training-ai-bike
4. Athletech News, Peloton new era: AI fitness coaching and equipment overhaul: https://athletechnews.com/peloton-new-era-ai-fitness-coaching-equipment-overhaul/
5. Tonal Knowledge Base, Troubleshooting Tonal 2 camera: https://knowledge.tonal.com/kb/guide/en/troubleshooting-tonal-2-camera-YUcew2ZBxF/Steps/3980893
6. Tonal blog, Why Tonal's Spotter is a game changer: https://tonal.com/blog/why-tonals-spotter-is-a-game-changer
7. Tempo: Home Workout & Fitness (App Store): https://apps.apple.com/app/id1501671678
8. SensAI, Best AI Workout Form Check Apps (2026) (vendor-authored; modified 15 Oct 2026): https://www.sensai.fit/blog/best-ai-workout-form-check-apps-2026
9. 9to5Mac, watchOS 26 (9 Jun 2025): https://9to5mac.com/2025/06/09/watchos-26/
10. heise, How Apple's AI trainer Workout Buddy works: https://heise.de/-10475361
11. Google Blog, Fitbit's personal health coach public preview (27 Oct 2025): https://blog.google/products-and-platforms/devices/fitbit/personal-health-coach-public-preview/
12. TechRepublic, Fitbit's Gemini AI Coach Expands to iPhone, 5 New Countries: https://www.techrepublic.com/article/news-fitbit-ai-coach-expands-ios-five-markets/
13. WHOOP (App Store listing, fetched 16 Oct 2026): https://apps.apple.com/us/app/whoop/id933944389
14. MyFitnessPal (App Store listing, fetched 16 Oct 2026): https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718
15. Noom (App Store listing, fetched 16 Oct 2026): https://apps.apple.com/us/app/noom-healthy-weight-loss/id634598719
16. Apple Support, Track your cardio fitness levels: https://support.apple.com/en-us/108790
17. Android Central, Samsung Health update helps you keep track of your medications: https://www.androidcentral.com/apps-software/samsung-health-medications
18. Apple WWDC25 session 321, Meet the HealthKit Medications API: https://developer.apple.com/videos/play/wwdc2025/321/
19. Android Developers, Health Connect Medical Records: https://developer.android.com/health-and-fitness/health-connect/medical-records
20. Android Developers, Medical records data format: https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format
21. FDA, General Wellness: Policy for Low Risk Devices (issued 6 Jan 2026): https://www.fda.gov/media/90652/download
22. King & Spalding, FDA Updates General Wellness and Clinical Decision Support Guidance Documents (Jan 2026): https://www.kslaw.com/insights/articles/fda-updates-general-wellness-and-clinical-decision-support-guidance-documents
23. FDA, Clinical Decision Support Software guidance (6 Jan 2026): https://www.fda.gov/media/109618/download
24. FDA, Warning Letter to WHOOP, Inc. (14 Jul 2025): https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-07142025
25. MassDevice, FDA closes warning letter to Whoop over blood pressure feature: https://www.massdevice.com/fda-closes-warning-letter-whoop-blood-pressure/
26. USPTO, US 11,194,455 "User interfaces for health applications" (Apple patent family): https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11194455
27. Visible Help Center, Using Visible with medications that impact heart rate: https://help.makevisible.com/en/articles/10632785-using-visible-with-medications-that-impact-heart-rate
28. SmartGym Help, How to set custom heart rate zones: https://help.smartgymapp.com/article/152-how-to-set-custom-heart-rate-zones
29. Enhance-d: Diabetes & Exercise (App Store): https://apps.apple.com/us/app/enhance-d/id6497331467
30. ClinicalTrials.gov NCT06730906, PACTAID app in adults with type 1 diabetes: https://clinicaltrials.gov/study/NCT06730906
31. PMC6087665, RPE and heart-rate response in people taking beta blockers: https://pmc.ncbi.nlm.nih.gov/articles/PMC6087665
32. Metric, Introducing Real-Time Velocity Feedback (17 Jun 2024): https://www.metric.coach/articles/introducing-real-time-feedback
33. PeerJ, Validation of a commercially available mobile application for velocity-based resistance training (2024): https://peerj.com/articles/17789
34. SetSync, Strength Video Analysis: https://setsync.app/
35. RepSpeed (App Store): https://apps.apple.com/us/app/repspeed/id1584279988
36. Vitruve, Mobile App: https://vitruve.fit/?p=678
37. Perch, Tracking: https://perch.fit/tracking
38. AppleInsider, How to enable Walking Steadiness notifications in iOS 15: https://appleinsider.com/articles/22/04/03/how-to-enable-walking-steadiness-notifications-in-ios-15
39. Business Wire, Hinge Health unveils new AI-powered care tools (21 Oct 2025): https://www.businesswire.com/news/home/20251021731830/en/Hinge-Health-unveils-new-AI-powered-care-tools
40. Hinge Health, TrueMotion: turning a phone camera into a 3D motion lab (10 Nov 2025): https://www.hingehealth.com/resources/articles/truemotion-turning-a-phone-camera-into-a-3d-motion-lab/
41. PMC10177945, A beta version of a computer-vision application for knee valgus assessment: validity and reliability (2023): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10177945/
42. BLACKROLL, Transparency notice for the BLACKROLL app (AI overhead squat analysis): https://blackroll.com/eu/en/service/transparenz-blackroll-app
43. AppFollow, SquatScreen (PostureCo) listing: https://appfollow.io/ios/squatscreen/1249748805?country=us
44. Gen Re, netletter on the AIMO movement score (2020): https://www.genre.com/us/knowledge/publications/2020/june/netletterrc20-2-de
45. AIMO Fit (App Store): https://apps.apple.com/app/id1621294451
46. NoCamels, Sency on-device movement assessment: https://nocamels.com/?p=110976
47. Athletech News, Sency transforms fitness market with AI motion tracking (May 2024): https://athletechnews.com/sency-transforms-fitness-market-ai-motion-tracking/
48. Vora, Voice AI fitness coach: https://askvora.com/voice-coaching
49. GymScan: Gym Equipment Scanner (App Store): https://apps.apple.com/us/app/gymscan-gym-equipment-scanner/id6751796947
50. GymVision: AI Workout Planner (App Store): https://apps.apple.com/us/app/gymvision/id6752872750
51. Gymeo, Scan & Workout Tracker (mwm.ai listing): https://mwm.ai/apps/gymeo-scan-workout-tracker/6748888066
52. Liftd, Gym Workout Tracker (Google Play): https://play.google.com/store/apps/details?id=ai.liftd.android&hl=en_US
53. University of Stirling, Technogym Training App: https://stir.ac.uk/student-life/sport-at-stirling/health-and-fitness/technogym-training-app
54. RepChamp: Fitness Duel (Google Play): https://play.google.com/store/apps/details?id=com.repchamp.app&hl=en
55. FitDuel: AI Workout Challenge (Google Play): https://play.google.com/store/apps/details?id=com.thefitduel
56. REPcount, Exercise Counter (App Store): https://apps.apple.com/ch/app/repcount-exercise-counter/id6756521008?l=en-GB
57. FITROX, AI Push-Up Competition: https://fitrox.app/
58. Fitbod Help Center, Injuries / Limitations: https://help.fitbod.me/hc/en-us/articles/37629269518103
59. Fitbod (App Store, fetched 16 Oct 2026): https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543
60. Freeletics blog, Coach feedback and Limitations: https://www.freeletics.com/en/blog/posts/coach-feedback/
61. Injurymap, Physiotherapy App (App Store): https://apps.apple.com/us/app/injurymap-physiotherapy-app/id1102375789
62. Danish health service page on Injurymap: https://ds-sundhed.dk/en/injurymap/
63. Prehab: Physical Therapy, Pain (App Store): https://apps.apple.com/us/app/prehab-physical-therapy-pain/id1626839977
64. Sword Health, Introducing Phoenix (4 Jun 2024): https://swordhealth.com/newsroom/introducing-phoenix
65. MedCity News, Sword Health financing and AI care specialist (Jun 2024): https://medcitynews.com/2024/06/sword-health-financing-ai-musculoskeletal/
66. Kemtai, Product: https://kemtai.com/product
67. IntuitionLabs, Kemtai profile: https://intuitionlabs.ai/software/physical-occupational-therapy/rom-and-goniometry-tracking/kemtai
68. CoachAI (App Store): https://apps.apple.com/us/app/coach-ai/id6504732473
69. formcoach AI (hunted.space): https://hunted.space/product/formcoach-ai-form-coach
70. Form Coach: Camera Rep Counter (mwm.ai listing): https://mwm.ai/apps/form-coach/6770110788
71. Tracked, Voice commands: https://www.tracked.gg/features/voice-commands
72. Superset, Log your workout by talking: https://trysuperset.app/best
73. Apple Support, Use Fall Detection with Apple Watch: https://support.apple.com/en-us/108896
74. GymCam (Carnegie Mellon research): https://karan-ahuja.com/gymcam.html
75. Onform: Video Analysis App (App Store): https://apps.apple.com/US/app/id1490334045
76. DEV Community, RivalRep: duel your past self in push-ups and pull-ups: https://dev.to/rivalrep_creator/i-built-an-app-to-duel-your-past-self-in-push-ups-and-pull-ups-1k9b
77. Vitruve, Top 10 camera-based apps for tracking athletes' workouts: https://vitruve.fit/blog/top-10-camera-based-apps-for-tracking-your-athletes-workouts/
78. Capterra, TrueCoach reviews: https://capterra.com/p/155784/truecoach/reviews/
79. ABC Trainerize ideas forum, attach videos for exercise form: https://ideas.abcfitness.com/forums/167887-coach-trainer-abc-trainerize/suggestions/38467258-allow-videos-photos-to-be-attached-for-comments-f
80. Oura (App Store, fetched 16 Oct 2026): https://apps.apple.com/us/app/oura/id1043837948
81. Hexis, Personalised fuel plans: https://www.hexis.live/
82. Naavik, Nex Playground and motion gaming's second act: https://naavik.co/digest/nex-playground-and-motion-gamings-second-act/
83. Insider Gaming, Nex Playground topped PS5 sales in the US: https://insider-gaming.com/console-nex-playground-topped-ps5-sales-us/
84. Athletech News, Lumin Fitness AI studio: https://athletechnews.com/?p=98528
85. Envisioning, Return-to-play orchestration systems: https://www.envisioning.com/research/stride/return-to-play-orchestration
86. Epistemonikos, Back in the Game: a smartphone app supporting return to sport after serious injury: https://www.epistemonikos.org/en/documents/245c0f7794966252849e97854e003668a4c8b19c
87. CDC STEADI, Clinical resources (functional assessments): https://www.cdc.gov/steadi/hcp/clinical-resources/index.html
88. Wulf G., Attentional focus and motor learning: a review of 15 years (Int. Review of Sport and Exercise Psychology; DOI): https://doi.org/10.1080/1750984X.2012.723728
89. Rep-IQ, AI form coach (waitlist): https://rep-iq.app/
90. RepCam AI, Rep Counter AI (Google Play): https://play.google.com/store/apps/details?id=com.repcamai.app&hl=en
91. (reserved, not used)
92. (reserved, not used)
93. Connect the Watts, Tempo Move review (23 Dec 2021): https://connectthewatts.com/2021/12/23/tempo-move-review-iphone-powered-fitness-for-great-value-with-an-even-better-design/

# R1: Competitive Landscape, October 2026. Camera Form Feedback, AI Fitness/Health Coaches, and Nutrition/Medication-Aware Fitness

Prepared 2026-10-16 for the writers of the BRD, Technical Specification, Product Roadmap & Strategy, Innovative Features and Build Playbook.

**Confidence key.** High: a primary source (official page, app-store listing, company press release) read directly in Oct 2026. Medium: reputable secondary press, or a primary source seen only through a search summary. Low: a single weak or aggregator source, or a conclusion drawn from the absence of evidence.

**Method and limits.** Official pages, App Store listings and 2025-2026 press were checked on 2026-10-16. The session's web-search quota ran out partway through, so the remaining checks used direct page fetches. Noom's website, Ro, Hims & Hers, OpenAI and some Sword Health pages blocked automated fetching; facts about them are marked. Reddit threads were not sampled. Evidence of user complaints comes from App Store reviews and expert reviewers instead.

## Summary

- **Camera form correction already exists commercially (High).** Peloton IQ (launched Oct 1, 2025) gives real-time written and audio form cues and counts reps, but only on camera-equipped hardware: Bike+ $2,695, Row+ $3,495, Tread Vision $3,495 and Tread+ $6,695, plus a membership ([S1](https://www.onepeloton.com/peloton-iq), [S2](https://www.onepeloton.com/blog/what-is-peloton-iq), [S3](https://www.onepeloton.com/en-GB/blog/whats-new-2026-treadmill-updates)). Tonal 2 ($4,295 plus $59.95/mo) gives real-time "coaching cues" from a 120-degree camera ([S9](https://www.tonal.com/products/tonal-2)).
- **Phone-only real-time form feedback also exists (High).** Zing AI combines "Zing Vision" camera technique feedback with an AI chat coach and has 4.8 stars from about 31K ratings ([S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792)). Indie apps such as Coach.AI do the same ([S18](https://apps.apple.com/us/app/coach-ai/id6504732473)). At least nine "upload a video" form-check apps are listed on the App Store ([S24](https://apps.apple.com/us/app/id6745452870)-[S30](https://apps.apple.com/app/id6744373919)).
- **Clinical musculoskeletal (MSK) care has used camera-guided exercise for years, and that market is consolidating (High).** Hinge Health added TrueMotion "Movement Analysis" and the "Robin" AI assistant (Oct 21, 2025) ([S33](https://ir.hingehealth.com/news/news-details/2025/Hinge-Health-unveils-new-AI-powered-care-tools/default.aspx)). Sword Health bought Kaia Health, maker of the camera-based Motion Coach, for $285M (announced Jan 28, 2026) ([S34](https://swordhealth.com/newsroom/sword-acquires-kaia-health)).
- **The computer-vision layer is commoditized (High).** Google MediaPipe Pose Landmarker returns 33 3D landmarks on Android, iOS and the web ([S45](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker)). B2B SDKs sell rep counting and form feedback off the shelf: QuickPose (MediaPipe-based, on-device), Sency and Kemtai (111 body points, edge processing) ([S44](https://quickpose.ai/), [S43](https://www.sency.ai/), [S42](https://kemtai.com/)). The defensible part is what a product does with the signal, not the pose estimation itself.
- **Every major wearable platform now ships an LLM coach (High).** Google renamed the Fitbit app "Google Health" and launched the Gemini-powered Google Health Coach (rollout from May 19, 2026; $9.99/mo or ₹99/mo in India). It builds fitness plans, logs meals from photos and summarizes medical records ([S53](https://techcrunch.com/?p=3120136), [S54](https://www.cgmagonline.com/news/google-fitbit-air-and-google-health-app/), [S55](https://www.tech2.com/gadgets/google-replaces-fitbit-app-with-google-health-brings-health-coach-to-india-text-ws-l-10080257.html)). The others:
  - WHOOP added "My Memory", proactive check-ins, and EHR access through HealthEx (May 2026) ([S58](https://hlth.com/insights/news/whoop-expands-digital-health-offering-with-healthex-integration-and-clinician-video-visits)).
  - Oura has Advisor, Meals (photo logging) and Dexcom Stelo glucose ([S61](https://ouraring.com/blog/oura-advisor/), [S62](https://www.businesswire.com/news/home/20250506997981/en)).
  - Samsung Health Assistant entered US beta on July 21, 2026 ([S65](https://aiweekly.co/alerts/samsung-opens-health-assistant-ai-beta-to-us-galaxy-users)).
- **Apple scaled back its AI health coach (High).** Bloomberg reported on Feb 5, 2026 that "Project Mulberry" was cut back ([S70](https://9to5mac.com/2026/02/05/apple-reportedly-scales-back-plans-for-ai-powered-health-coach/)). What Apple ships with iOS and watchOS 27:
  - Workout Buddy, which is spoken motivation rather than chat, in English and Spanish.
  - A Siri camera mode that shows nutrition information for a food.
  - A redesigned Health app "coming in late 2026."

  Sources: [S67](https://www.apple.com/os/watchos/), [S68](https://www.apple.com/os/ios/), [S69](https://www.apple.com/health/).
- **Consumer apps already combine nutrition, medication and an AI coach (High).** MyFitnessPal has an AI Coach tab, Meal Scan and Voice Log, and free "GLP-1 Support" (Apr 28, 2026) covering dose logging, side effects and reminders. It also acquired Cal AI (Mar 2026) ([S77](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718), [S78](https://www.bakersfield.com/ap/news/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build/article_594b029e-ed9b-5c1a-ac3b-a4ea46e70908.html), [S82](https://insider.fitt.co/myfitnesspal-acquires-rival-food-tracker-cal-ai/)). Oura "GLP-1 Insights" (May 28, 2026) logs doses and side effects, and its Advisor points out Readiness dips after a dose. It is available in India ([S63](https://ouraring.com/blog/glp-1-insights/)).
- **GLP-1 companion programs all promise muscle preservation, but they deliver it as content or human PTs (High).**
  - WeightWatchers GLP-1 Success offers strength videos and a protein target of 1 g/kg of starting body weight ([S89](https://www.weightwatchers.com/us/how-it-works/glp-1-program)).
  - Noom offers "Muscle Defense" ([S88](https://apps.apple.com/us/app/noom-weight-loss-glp-1-care/id634598719)).
  - Sword Pulse (employer channel) combines PTs, smart scales and wearables ([S37](https://insider.fitt.co/sword-health-expands-ai-led-specialty-care/)).

  None of these was found to check training quality or volume with a camera.
- **General AI assistants now read health data, so a chat-only coach is a commodity (Medium-High).** ChatGPT Health launched in Jan 2026 for early users, with connectors including Apple Health, MyFitnessPal, WeightWatchers and Peloton ([S100](https://m.gsmarena.com/openai_launches_chatgpt_health_with_apple_health_and_myfitnesspal_integration-news-71006.php), [S101](https://runningmagazine.ca/health-nutrition/chatgpt-health-to-partner-with-popular-fitness-apps/)). Claude announced HealthEx and Function connectors for US Pro/Max subscribers, with Apple Health and Health Connect in beta (Jan 11, 2026) ([S102](https://fortune.com/2026/01/11/anthropic-unveils-claude-for-healthcare-and-expands-life-science-features-partners-with-healthex-to-let-users-connect-medical-records/)).
- **Training that adapts to medications other than GLP-1 is essentially absent (Medium, inferred from absence).** The only mainstream example found is Apple using "medications that might affect heart rate" as an input to its VO2 max estimate ([S71](https://support.apple.com/en-us/HT211856)). No consumer fitness app found changes the exercise prescription for beta-blockers, insulin or sulfonylureas, statins or anticoagulants.
- **Verdict on the founder's two ideas: neither is unique on its own.** One combination was not found in any mainstream consumer product as of 2026-10-16: phone-only, real-time camera verification of training that feeds a coach which also reasons over nutrition and the medication schedule, starting with the GLP-1 dose cycle. The closest products each miss one piece:
  - Sword Health: employer-only, PT-led and sensor-based.
  - Zing: camera plus chat, but no nutrition or medications.
  - MyFitnessPal and Oura: chat plus nutrition plus GLP-1, but no check that workouts were done well.
- **Fastest likely copiers:**
  - Google: owns MediaPipe and the Gemini coach.
  - Peloton: has form models, and its CTO wants form feedback "across all of our modalities."
  - MyFitnessPal with Cal AI: has nutrition, GLP-1 support and the AI coach.
  - Sword: has GLP-1 support, PTs and Kaia's computer vision.
  - Oura and WHOOP: have chat and GLP-1 logging.
- **Recurring user complaints:**
  - Missed reps and camera placement problems ([S31](https://apps.apple.com/us/app/metric-strength-training/id1595510857), [S14](https://techcrunch.com/?p=1951028)).
  - Sync and duplicate-workout bugs ([S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792)).
  - Rigid workouts ([S19](https://apps.apple.com/us/app/freeletics-workouts-fitness/id654810212)).
  - AI insights that feel thin or are wrong ([S74](https://the5krunner.com/2026/04/20/garmin-connect-plus-review/), [S52](https://www.dcrainmaker.com/2025/07/apple-watchos-26-workout-beta-real-world.html)).
  - Consent and privacy friction ([S66](https://www.webpronews.com/samsungs-new-ai-health-assistant-turns-wearable-data-into-actionable-advice/)).
- **India (High/Medium):**
  - The Google Health Coach tier costs ₹99/mo ([S55](https://www.tech2.com/gadgets/google-replaces-fitbit-app-with-google-health-brings-health-coach-to-india-text-ws-l-10080257.html)).
  - Healthify has a GLP-1 support partnership with Novo Nordisk India (Dec 2025) and expects more than a third of its paid subscriptions to come from GLP-1 ([S84](https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20)).
  - cult.fit's current listing advertises no camera or AI-coach features, despite its 2021 acquisition of Onyx ([S50](https://apps.apple.com/in/app/cult-fit-gym-workout-fitness/id1217794588), [S47](https://venturebeat.com/business/cure-fit-acquires-ai-body-tracker-onyx-to-enable-two-way-workout-videos)).
- **US price anchors:**

  | Offer | Price |
  |---|---|
  | AI tiers on wearable platforms (Garmin, Google) | $6.99-$9.99/mo |
  | MyFitnessPal Premium | $79.99/yr |
  | Peloton App One | $15.99/mo |
  | Peloton App+ | $28.99/mo |
  | Ladder | $29.99/mo |
  | Human coaching (Future) | $199/mo |
  | GLP-1 clinical programs (excluding drugs) | about $69-$199/mo |

## 1. Camera-based exercise form feedback

### 1.1 Connected hardware (camera built into the machine)

**Peloton (Peloton IQ, Cross Training Series, Vision treadmills). Status: active and expanding.**
- **Launch and camera features.** Peloton IQ arrived on Oct 1, 2025. On the Cross Training Bike+, Tread+ and Row+, a front-facing "Movement-Tracking Camera" does the following ([S2](https://www.onepeloton.com/blog/what-is-peloton-iq)):
  - Counts reps and total lifting volume.
  - Gives real-time written and audio form cues during instructor-led and self-paced strength classes. Peloton's example is a squat cue such as "keep your back straight." Users can change cue frequency or turn cues off.
  - Powers Suggested Weights, a Strength Workout Generator, Strength Benchmarking and "OK Peloton" voice control.
- **Model coverage.** Base models get only the non-camera IQ features: plans, performance estimates, weekly insights and recommendations ([S1](https://www.onepeloton.com/peloton-iq)).
- **Privacy and cost.** The camera is optional, and Peloton states that "images and videos ... are not recorded or stored." IQ costs nothing extra, but needs All-Access. It can draw on Apple Health, Garmin or Fitbit data. **No conversational chat is described** (High).
- **Hardware prices (US):** Bike $1,695, Bike+ $2,695, Tread $3,495, Tread+ $6,695, Row+ $3,495 ([S1](https://www.onepeloton.com/peloton-iq)).
- **New in Sept 2026: Tread Vision.** Announced Sept 22, 2026, it adds the movement-tracking camera for strength form feedback and rep tracking ([S3](https://www.onepeloton.com/en-GB/blog/whats-new-2026-treadmill-updates)). It also adds "Run Analysis," which measures cadence, vertical oscillation and stride length in real time and gives a 1-100 Running Efficiency Score.
  - Software rolls out from Oct 1, 2026.
  - Tread Vision starts at $3,495 and Tread+ Vision at $6,695 ([S5](https://www.onepeloton.com/new-2026-tread-vision), [S4](https://www.onepeloton.com/new-2026-tread-plus-vision)).
  - Form feedback covers "select movements during class" ([S4](https://www.onepeloton.com/new-2026-tread-plus-vision)).
  - A foldable Tread Flex is due in spring 2027 (High).
- **Peloton Guide discontinued.** The Guide was the $295 add-on camera device. Its sales ended July 30, 2025, and existing owners keep support ([S6](https://theclipout.com/peloton-guide-discontinued/)) (Medium-High; fan sites quoting Peloton).
- **Phone app has no camera features.** The Peloton App costs $15.99/mo or $159/yr (App One) and $28.99/mo or $289/yr (App+). Its listing mentions no camera form feedback, so form feedback today is hardware-only ([S8](https://apps.apple.com/us/app/id792750948)) (High).
- **Intent to expand.** CTO Nick Caldwell said in a Reddit AMA, as reported Oct 14, 2025: "At some point I want form feedback across all of our modalities" ([S7](https://www.pelobuddy.com/form-feedback-more/)). The Tread Vision's Run Analysis is the first step.

**Tonal 2. Status: active.**
- **Price.** $4,295 ($5,085 bundle). Membership is $59.95/mo with a 12-month commitment. A rental through Whim costs $279/mo under an Oct 2026 promotion ([S9](https://www.tonal.com/products/tonal-2)).
- **Camera.** A 120-degree built-in camera ("Smart View") gives real-time coaching cues and makes post-workout clips. A mobile device supplies a second, side-on angle; Tonal 1 relies on the mobile device alone ([S9](https://www.tonal.com/products/tonal-2), [S10](https://knowledge.tonal.com/kb/guide/en/troubleshooting-tonal-2-camera-YUcew2ZBxF/Steps/3980893)).
- **Daily Lift.** Launched July 23, 2025, it generates a workout each day from the user's history, performance and fatigue, plus Tonal 2 camera data ([S11](https://athletechnews.com/tonal-daily-lift-ai-workouts/)).
- **Not covered by the source.** The product page names no chat coach and does not list which movements get cues. The Tonal 2 launch was reported Jan 8, 2025 ([S12](https://insider.fitt.co/tonal-2-release/)).

**Tempo. Status: appears pivoted (Medium).**
- Tempo originally sold the Studio and Move, which used 3D/iPhone camera tracking ([S107](https://tempo.fit/blog/introducing-the-tempo-move)). An early review found that its computer vision "doesn't always register every rep, especially if your posture is off" ([S14](https://techcrunch.com/?p=1951028)).
- Today the homepage sells "Virtual Personal Training" from $39/mo, a smart-weights home-gym add-on from +$20/mo, and 3D body scans. It does not mention form feedback or rep counting ([S13](https://tempo.fit/)).

**Lumin Fitness. Status: franchising; no 2026 news found (Low-Medium).**
- It runs AI and motion-tracking studios with LED walls. The first opened in Irving, TX in Sept 2023.
- It signed a 13-unit Texas franchise deal and an 8-unit Louisiana deal (June 2024) ([S15](https://dallasinnovates.com/dallas-gamified-lumin-fitness-inks-franchise-agreement-for-13-new-texas-clubs/), [S16](https://athletechnews.com/ai-powered-studio-lumin-fitness-signs-louisiana-franchise-deal/)).
- It is a gym concept, not an app competitor.

### 1.2 Phone-only consumer apps with real-time feedback

**Zing AI (Zing Coach Inc.).** The closest consumer analog to the founder's camera idea (High, from the App Store listing [S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792)).
- **Features:**
  - "Zing Vision" tracks movement through the phone camera in real time and gives technique insights.
  - An AI Coach checks in daily on energy, mood and sleep, and users can "ask anything" in chat, with four coach personalities.
  - An AI Body Scan estimates body fat and lean mass from photos.
  - Les Mills content was added in Mar 2026.
  - Integrates with Apple Watch and Apple Health.
- **Gap.** **There is no calorie or nutrition logging; the developer confirmed this in a reply to a review.** Medications are not covered.
- **Price and ratings.** Premium in-app purchases cost $18.99-$59.99 (3 months is $29.99), and a Body Scan Report is $19.99. Rating is 4.8 from about 31K ratings.
- **Complaints:** Apple Health sync inflated workout minutes and duplicated workouts, users can't reorder or skip exercises when equipment is busy, and audio and video drop out.
- **Not verified:** Android availability and an explicit rep-counting feature.

**Coach.AI (Coach AI Technologies FZE).** The founder's concept minus medications, already built by an indie team (High for listing content, Low for traction; [S18](https://apps.apple.com/us/app/coach-ai/id6504732473)).
- **Features:** real-time camera form checks "rep by rep," hands-free rep counting with tempo tracking, nutrition plans and an AI coach. The developer claims "camera data never leaves your phone."
- **Platform and price:** iPhone only. PRO costs $12.99 or $125.99 and ELITE $24.99 or $199.
- **Traction:** version 1.0 shipped Apr 30 (year not shown on the listing). The app has too few ratings to show a score.

**Freeletics.** Has an AI Coach plus the Coach+ LLM chatbot (2024), trained on "anonymised data from over 59m user journeys" ([S20](https://www.freeletics.com/blog/posts/freeletics-coach-plus/)).
- An undated Red Bull feature said Freeletics was testing a mode that lets users record themselves so the app can check squat depth ([S21](https://www.redbull.com/gb-en/ai-coaches-are-the-future-of-fitness)). The Oct 2026 listing mentions no camera feature (High for the listing, Low for the test).
- **Price:** Training Coach costs $34.99-$79.99 for 3 to 12 months. Nutrition is a separate app.
- **Complaints:** exercises can't be swapped, progress is lost if a workout is quit, and users can only rate whole workouts ([S19](https://apps.apple.com/us/app/freeletics-workouts-fitness/id654810212)).

**Fitbod.** Its "proprietary algorithm" builds plans, and beginners get "expert demos and cues." The site mentions no camera form check and no AI chat ([S22](https://fitbod.me/)).
- A competitor's review (SensAI) reports a June 2026 price rise to $15.99/mo or $95.99/yr and describes Fitbod as rules-based, not conversational ([S23](https://www.sensai.fit/blog/fitbod-review-2026)) (Medium; the source is not neutral).

### 1.3 Upload-a-video "AI form check" (post-hoc analysis)

This category is crowded and mostly indie, and the accuracy claims come only from the developers (Medium):

| App | What it claims | Evidence |
|---|---|---|
| Form Fix: AI Form Check Coach | Upload squat or deadlift video; returns a form score. Released May 2025 | [S24](https://apps.apple.com/us/app/id6745452870) |
| Formax: AI Workout Feedback | Squat/deadlift scoring for form, control and range of motion. First release Jan 12, 2026; free tier includes 1 analysis | [S25](https://mwm.ai/apps/formax-ai-workout-feedback/6756526116) |
| GymSpotter | Multi-lift analysis; flags depth and bar path | [S26](https://apps.apple.com/app/id6758680413) |
| SquatEye | Squat depth pass/fail to the IPF hip-crease standard | [S27](https://apps.apple.com/ca/app/id6758864722) |
| FormCheck AI | Squat, deadlift, bench press, overhead press | [S28](https://apps.apple.com/lb/app/formcheck-ai/id6741048432) |
| Gym Assistant - AI Form Check | Posture and range of motion from a recorded clip. Released Jun 2026 | [S29](https://appgoblin.info/apps/6782565845) |
| Gymscore | Record or upload; third-party summary claims 2,500+ exercises and a 0-100 score | [S30](https://apps.apple.com/app/id6744373919) |

Takeaway: post-hoc checks are cheap to build and already plentiful. They are not a differentiator on their own.

### 1.4 Specialist: camera-based velocity-based training (VBT)

**Metric (Core Advantage Pty Ltd).** Uses the iPhone or iPad camera, with no extra hardware ([S31](https://apps.apple.com/us/app/metric-strength-training/id1595510857), [S32](https://metric.coach)).
- **Features:** bar velocity on 60+ exercises, velocity-loss tracking, estimated 1RM, bar-path traces and frame-by-frame review.
- **Price:** Pro $10.99/mo or $79.99/yr.
- **Ratings:** 4.0 from only 45 ratings. Reviews are the clearest public evidence of camera-tracking friction:
  - A 2025 reviewer said it failed to record reps "no matter where I put the camera."
  - A 2024 reviewer said, "I don't feel like I can trust the measured data."
  - The developer replies by asking users to send sample videos.

### 1.5 Clinical MSK / digital physical therapy (B2B2C through employers and health plans)

| Company | Camera / form capability | AI | Oct 2026 status | Evidence |
|---|---|---|---|---|
| Hinge Health (NYSE: HNGE) | TrueMotion computer vision. "Movement Analysis" captures joint angles, symmetry and endurance, which feed "Hinge Scores" | "Robin" AI Care Assistant, 24/7: triages flare-ups and summarizes for the PT | Active; launched Oct 21, 2025 | [S33](https://ir.hingehealth.com/news/news-details/2025/Hinge-Health-unveils-new-AI-powered-care-tools/default.aspx) (High) |
| Sword Health | "Phoenix" AI Care Specialist (Jun 2024) guides members during sessions "through natural conversation." Move uses a wearable | Pulse (2026), an AI lifestyle program for GLP-1 users: strength training, protein guidance and body-composition monitoring. Dawn mental-health chatbot is direct-to-consumer | Active; bought Kaia for $285M (Jan 2026); valued at $4B (Jun 2025) | [S36](https://swordhealth.com/articles/introducing-phoenix), [S34](https://swordhealth.com/newsroom/sword-acquires-kaia-health), [S37](https://insider.fitt.co/sword-health-expands-ai-led-specialty-care/), [S38](https://swordhealth.com/newsroom/sword-health-launches-pulse-ai-cardiometabolic-care), [S106](https://tech.eu/2025/06/17/sword-health-raises-40m-at-4b-valuation-to-expand-ai-first-care-into-mental-health/) (High; Pulse details Medium) |
| Kaia Health | Phone-camera "Motion Coach" | n/a | **Acquired by Sword.** Sword will move Kaia's US MSK members onto Sword's platform; Germany (DiGA) gives Sword reimbursed market entry | [S34](https://swordhealth.com/newsroom/sword-acquires-kaia-health), [S35](https://www.mobihealthnews.com/news/sword-health-acquires-kaia-health-285m) (Medium-High) |
| Exer AI (formerly Exer Labs) | Range of motion, rep counting and real-time form correction for major joints | n/a | Active. Patient app runs "exclusively through healthcare partners." Mayo Clinic deployment; about 144 assessments | [S40](https://apps.apple.com/app/id1505858367), [S41](https://www.mobihealthnews.com/news/exclusive-exer-ai-expands-partnership-mayo-clinic-clinical-deployment) (Medium) |
| Kemtai | 111 body points; real-time audio and visual correction; 2,000+ exercises; processing on the device, no video recording | n/a | Active, B2B. Company states it is FDA-listed and CE-marked; Jan 2026 blog post on GLP-1 and sarcopenia | [S42](https://kemtai.com/) (High for claims, which are company-reported) |

### 1.6 B2B SDKs and open building blocks

- **QuickPose:** iOS, Android and React Native SDKs. Offers rep counters, form feedback, range of motion and yoga pose detection. It is "Powered by MediaPipe," runs on the device, and claims "500+ apps built." Its testimonials are placeholder text, so treat those claims cautiously ([S44](https://quickpose.ai/)) (Medium).
- **Sency:** "Motion SDK" and "M-OS." Claims 487M movements analyzed and 1.5M users. JustFit is the only named customer ([S43](https://www.sency.ai/)) (Medium).
- **Google MediaPipe Pose Landmarker:** 33 3D landmarks; image, video and live-stream modes; Lite, Full and Heavy models; Android, iOS, Web and Python ([S45](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker)) (High).
- **Apple Vision:** `VNDetectHumanBodyPose3DRequest` provides 3D body pose ([S46](https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest)). The page did not render, so the OS minimum, believed to be iOS 17, is Medium.

### 1.7 Gone, absorbed or pivoted (lessons)

- **Peloton Guide:** discontinued July 2025 ([S6](https://theclipout.com/peloton-guide-discontinued/)). A cheap standalone camera device did not survive, while camera features did move into premium hardware.
- **Onyx:** a "3D motion capture on phone" app. Cure.fit acquired it in Jan 2021, reportedly in a share swap of about $12.7M ([S47](https://venturebeat.com/business/cure-fit-acquires-ai-body-tracker-onyx-to-enable-two-way-workout-videos), [S48](https://entrackr.com/?p=100850)). No evidence was found of a standalone app today (Low).
- **cult.fit (India):** around 2021 it described AI posture correction, rep counting and a live "energy meter" ([S51](https://analyticsindiamag.com/the-tech-powering-cult-fits-live-fitness-offerings/)). Its current App Store listing (4.8, 138K ratings) mentions none of these. It sells cultpass LIVE at ₹449/month, ₹999/quarter and ₹1,999/year, plus ELITE and PRO gym passes ([S50](https://apps.apple.com/in/app/cult-fit-gym-workout-fitness/id1217794588)). A Gurgaon listing shows ELITE at ₹18,975/yr plus GST ([S105](https://www.cure.fit/cult/cult-pass/gurgaon/Cult-Gym-Eros-Sector-49/590)).
- **Zenia (camera yoga app):** the US App Store listing returns 404 (checked Oct 2026), and Dealroom lists the company as "Acquired" without naming a buyer ([S49](https://app.dealroom.co/companies/zenia)) (Low-Medium).
- **trainwell (formerly CoPilot):** renamed May 30, 2024 "to differentiate itself from AI chatbot services." It pairs human trainers with Apple Watch motion data. It cost $99/mo in 2023 ([S97](https://trainwell.net/copilot), [S98](https://techcrunch.com/2023/10/04/copilot-app-pairs-users-with-one-on-one-remote-fitness-coaches-raises-6-3m)); the current price was not verified.

### 1.8 What users complain about (camera products)

1. **Missed reps and accuracy:** Metric reviews ([S31](https://apps.apple.com/us/app/metric-strength-training/id1595510857)) and Tempo's missed reps when posture was off ([S14](https://techcrunch.com/?p=1951028)).
2. **Setup friction:** Tonal 2 needs a second device for a side angle ([S9](https://www.tonal.com/products/tonal-2)). Metric requires the phone side-on and steady ([S32](https://metric.coach)). Peloton limits feedback to "select movements" ([S4](https://www.onepeloton.com/new-2026-tread-plus-vision)).
3. **Privacy:** market leaders now promise no video storage and on-device processing (Peloton, Kemtai, QuickPose, Coach.AI), so this is table stakes.
4. **Peloton IQ feedback:** no user-complaint data was gathered (see Unverified).

## 2. AI coach chatbots (fitness, health, nutrition)

| Product | Chat coach (model) | What data it sees | Nutrition logging | Medication awareness | Price | Notable 2025-2026 changes | Evidence |
|---|---|---|---|---|---|---|---|
| **Google Health Coach** (formerly the Fitbit app) | Yes (Gemini). At onboarding it asks about goals, routine, **equipment and injuries**; workout suggestions sit in the Fitness tab | Fitness, sleep, cycle tracking, nutrition, environment; US medical records with consent (US and Japan at GA) | Yes: dictation, **meal photo** or file; calorie and macro targets | Not mentioned (medical records may include medications; unverified) | Premium $9.99/mo or $99/yr; included with Google AI Pro/Ultra. **India ₹99/mo or ₹999/yr** | Public preview from Oct 2025; iOS and 5 more countries Feb 2026; renamed Google Health with GA rollout from May 19, 2026; Fitbit Air band $99.99. Coach first works with Fitbit and Pixel Watch, other devices "coming soon" | [S53](https://techcrunch.com/?p=3120136), [S54](https://www.cgmagonline.com/news/google-fitbit-air-and-google-health-app/), [S55](https://www.tech2.com/gadgets/google-replaces-fitbit-app-with-google-health-brings-health-coach-to-india-text-ws-l-10080257.html), [S56](https://blog.google/products/fitbit/personal-health-coach-public-preview/), [S57](https://www.techrepublic.com/article/news-fitbit-ai-coach-expands-ios-five-markets/) (High) |
| **WHOOP Coach** | Yes (LLM). "My Memory" lets members view, edit and delete context; proactive check-ins | Strain, recovery and sleep; Journal (voice or text) for behaviors, supplements and life events | Not documented in sources read | Clinical history including **diagnoses, medications, procedures** through HealthEx (US); US clinician video visits | One $199/yr, Peak $239/yr, Life $359/yr (Medium) | May 2026 AI and clinical update; $575M Series G at a $10.1B valuation | [S58](https://hlth.com/insights/news/whoop-expands-digital-health-offering-with-healthex-integration-and-clinician-video-visits), [S59](https://www.businesswire.com/news/home/20260508464188/en), [S60](https://trackervs.com/pricing/whoop-pricing/) |
| **Oura Advisor** | Yes, an LLM assistant (Mar 2025). Stores "Memories"; tone and check-in settings; women's-health LLM added Apr 2026 | Sleep, activity, readiness, resilience, stress, tags, glucose (Dexcom Stelo) | Yes: **Meals** photo analysis, focused on macros (May 2025) | **GLP-1 Insights** (May 28, 2026): medication, dose and schedule; side effects; reminders; Advisor flags Readiness dips about 48 h after a weekly dose | Not re-verified | GLP-1 Insights available in the US, **India**, EU, UK and more; LillyDirect partnership | [S61](https://ouraring.com/blog/oura-advisor/), [S62](https://www.businesswire.com/news/home/20250506997981/en), [S63](https://ouraring.com/blog/glp-1-insights/) (High) |
| **Samsung Health Assistant** | Yes, "AI-powered personal health assistant" in **US beta from July 21, 2026**; model not disclosed | Sleep, activity, nutrition, mindfulness, vitals; needs Galaxy Watch or Ring; Android 11+ | Uses Samsung Health nutrition data (photo logging not verified) | Not mentioned; no diagnosis or treatment advice | Not stated (beta) | Users on X raised consent concerns that AI-training approval is tied to data syncing (unconfirmed) | [S64](https://news.samsung.com/global/samsung-launches-health-assistant-beta-first-fully-integrated-ai-powered-personal-health-assistant), [S65](https://aiweekly.co/alerts/samsung-opens-health-assistant-ai-beta-to-us-galaxy-users), [S66](https://www.webpronews.com/samsungs-new-ai-health-assistant-turns-wearable-data-into-actionable-advice/) (Medium-High) |
| **Apple** (Workout Buddy, Health) | **No chat coach.** Workout Buddy gives spoken pep talks, milestones and summaries; English and Spanish; needs an Apple Intelligence iPhone and Bluetooth headphones | Workout history, pace, distance, rings, training load | iOS 27 "Siri mode in Camera can show nutrition information" for a food | VO2 max estimate takes "medications that might affect heart rate" as an input | Bundled with the devices | Project Mulberry scaled back (Feb 2026); Health app redesign "coming in late 2026"; a camera-based **walking** analysis and a wellbeing chatbot were reportedly still planned | [S67](https://www.apple.com/os/watchos/), [S68](https://www.apple.com/os/ios/), [S69](https://www.apple.com/health/), [S70](https://9to5mac.com/2026/02/05/apple-reportedly-scales-back-plans-for-ai-powered-health-coach/), [S71](https://support.apple.com/en-us/HT211856) (High) |
| **Garmin Connect+** | "Active Intelligence" AI insights (not chat; still beta at launch); a 2026 reviewer calls the insights thin | Garmin health and activity data | Yes, since **Jan 5, 2026**: barcode plus **photo** food recognition; replaces the MyFitnessPal link | No | $6.99/mo or $69.99/yr | Nutrition launched at CES 2026 | [S72](https://www.techradar.com/health-fitness/garmin-adds-premium-garmin-connect-tier-with-ai-features-but-promises-your-free-experience-is-not-going-away), [S73](https://www.dcrainmaker.com/2026/01/garmin-connect-nutrition-logging-connect.html), [S74](https://the5krunner.com/2026/04/20/garmin-connect-plus-review/) (High) |
| **Strava / Runna** | Runna plans (AI-adaptive running); "Athlete Intelligence" summaries not re-verified | Activities | No | No | Strava $79.99/yr; Runna $19.99/mo or $119.99/yr; bundle $149.99/yr | Runna beginner plans became paid Jun 5, 2026 | [S75](https://the5krunner.com/2026/10/14/is-runna-free/), [S76](https://www.wareable.com/sport/strava-runna-combined-subscription-announcement-price) (High for prices) |
| **MyFitnessPal** | Yes, **AI Coach** tab (Premium): insights based on the user's logging history; multi-image prompts; fridge-photo meal ideas | Food logs, exercise, steps, more than 40 integrations | Yes: Meal Scan (photo), Voice Log, barcode; Cal AI acquired | **GLP-1 Support** (free, Apr 28, 2026): dose logs, reminders, side-effect patterns; generic semaglutide logging in the US and Canada | Premium $79.99/yr, Premium+ $99.99/yr | Cal AI acquisition announced Mar 2, 2026; ChatGPT Health connector | [S77](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718), [S78](https://www.bakersfield.com/ap/news/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build/article_594b029e-ed9b-5c1a-ac3b-a4ea46e70908.html), [S79](https://www.wareable.com/health-and-wellbeing/myfitnesspal-nutrition-ai-coach-feature-announcement), [S80](https://lite.aol.com/sports/other/story/0022/20260224/9659625.htm), [S81](https://athletechnews.com/myfitnesspal-cal-ai-acquisition) (High) |
| **Cal AI** (owned by MyFitnessPal, run as a standalone app) | Not a coach | Food photos; the phone's depth sensor estimates food volume | Yes: photo, barcode, text. The site says it is "about 80% accurate" (self-reported) | Not mentioned | 3-day trial; price not shown | >$40M sales in 12 months; 15M+ downloads (press) | [S82](https://insider.fitt.co/myfitnesspal-acquires-rival-food-tracker-cal-ai/), [S83](https://www.calai.app/) (High/Medium) |
| **Healthify / HealthifyMe** (India) | Ria, an AI nutritionist (Medium) | Nutrition and health metrics | Photo logging (not re-verified) | **GLP-1 patient-support program**; Novo Nordisk India partnership (Dec 2025) | Not verified | GLP-1 is its "fastest-growing" offering; expects more than 1/3 of paid subscriptions from it; about 45M users | [S84](https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20), [S85](https://www.storyboard18.com/brand-marketing/novo-nordisk-india-and-healthify-launch-ai-driven-support-programme-for-obesity-care-85277.htm) (High for the partnership) |
| **Fittr** (India) | Human coaches; AI features not verified | Workouts and nutrition | Not verified | Not verified | Fittr Hart X2 ring ₹19,499 | n/a | [S87](https://www.smartprix.com/smart_rings/fittr-hart-x2-smart-ring-ppd1gjer3vue) (Low-Medium) |
| **Noom** | Optional 1:1 **human** coaching; "Log meals with AI"; face and body scans | Food, steps, weight, wearables (Apple Health, Fitbit, Garmin, Withings) | AI food logging | Noom Med / GLP-1Rx (Wegovy, Zepbound, etc., plus compounded options and microdose); **GLP-1 Companion "Muscle Defense"** | Noom Weight from $17/mo (billed $209/yr); Noom Med from $69/mo excluding drugs | n/a | [S88](https://apps.apple.com/us/app/noom-weight-loss-glp-1-care/id634598719) (High) |
| **WeightWatchers** | Coach chat (human); **AI Body Scan** (3D) | Points, food, weight | Camera meal tracking | Med+ (prescriptions through WW Clinic); **GLP-1 Success**: injection dose and site logs, side effects, strength videos | $25 first month, then $74/mo (12-month plan) or $84/mo (6-month plan); drugs extra | n/a | [S89](https://www.weightwatchers.com/us/how-it-works/glp-1-program), [S90](https://www.weightwatchers.com/us/plans) (High) |
| **Future** | Human coach; "NEW health coaching: nutrition, sleep"; no AI coach advertised | Apple Watch workouts | Via health coaching (no detail) | No | $50 first month, then $199/mo | n/a | [S94](https://www.future.co/) (High) |
| **Ladder** | Coach-written team plans, in-ear coaching, team chat; **no AI or form feedback** | Workouts | Photo, text and barcode logging (iOS) | No | $29.99/mo or $179.99/yr | iOS and web only, no Android | [S95](https://www.joinladder.com/), [S96](https://www.joinladder.com/pricing) (High) |
| **ChatGPT Health** (OpenAI) | General LLM with a separate health space and separate memory | Apple Health, MyFitnessPal, WeightWatchers, Peloton, Function, AllTrails, Instacart; US medical records through b.well | Through connectors | From records | Early users outside the EEA, Switzerland and the UK (Jan 2026); waitlist | Health chats not used to train models | [S99](https://openai.com/blog/introducing-chatgpt-health), [S100](https://m.gsmarena.com/openai_launches_chatgpt_health_with_apple_health_and_myfitnesspal_integration-news-71006.php), [S101](https://runningmagazine.ca/health-nutrition/chatgpt-health-to-partner-with-popular-fitness-apps/) (Medium-High; official page blocked fetch) |
| **Claude** (Anthropic) | General LLM | HealthEx (records from more than 50,000 health systems), Function; Apple Health and Health Connect in beta | n/a | Records, including medications | US Pro and Max (Jan 2026) | Health data "never used for model training" | [S102](https://fortune.com/2026/01/11/anthropic-unveils-claude-for-healthcare-and-expands-life-science-features-partners-with-healthex-to-let-users-connect-medical-records/) (High) |

**Observations**
- **Table-stakes chat features in 2026:** user-editable memory (WHOOP My Memory, Oura Memories), proactive check-ins, photo or voice meal logging, and an opt-out of AI training on health data (Google, OpenAI, Anthropic).
- **No AI coach sees workout quality.** None of the coaches above gets rep-by-rep form or range-of-motion data from a camera. Peloton's camera data stays inside Peloton IQ, which has no chat. Zing has a camera and chat, but no nutrition or medications.
- **Reviewers flag wrong or thin AI output:**
  - Workout Buddy's beta announced wrong splits and streaks ([S52](https://www.dcrainmaker.com/2025/07/apple-watchos-26-workout-beta-real-world.html)).
  - Garmin's AI insights are "thin" ([S74](https://the5krunner.com/2026/04/20/garmin-connect-plus-review/)).
  - Garmin photo logging defaults to a 100 g portion, according to reader comments ([S73](https://www.dcrainmaker.com/2026/01/garmin-connect-nutrition-logging-connect.html)).

## 3. Nutrition- and medication-aware fitness (GLP-1 first)

### 3.1 Market context

- **New oral GLP-1 option (High for approval; Medium for price).** The FDA approved Lilly's **Foundayo (orforglipron)**, a once-daily oral GLP-1, on **Apr 1, 2026**. LillyDirect shipments began Apr 6. Reported self-pay pricing starts at $149/mo for the lowest dose ([S103](https://scientificamerican.com/article/how-eli-lillys-new-glp-1-pill-stacks-up-against-wegovy-and-other-weight-loss), [S104](https://pharmashots.com/32510/eli-lilly-reports-us-fda-approval-of-foundayo-orforglipron-for-weight-loss/)). Telehealth providers already list Wegovy pills and Foundayo ([S92](https://joinfound.com/)), so any medication module must cover **weekly injectables and daily pills**.
- **India.** Reuters (Dec 5, 2025) reports that the semaglutide patent "expires in 2026" and that generic makers are expected to enter ([S84](https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20)). Specific generic launches and prices were not verified.

### 3.2 GLP-1 programs and features

| Product | Prescribes? | Companion features | Training / muscle component | Camera use | Price | Evidence |
|---|---|---|---|---|---|---|
| Noom (Med, GLP-1Rx, Companion) | Yes (US) | AI food logging, coaching, GLP-1 Companion | "Muscle Defense" ("protect muscle while losing fat"); Noom Move classes | Face and body scans ("educational") | $69/mo or more, drugs extra | [S88](https://apps.apple.com/us/app/noom-weight-loss-glp-1-care/id634598719) |
| WeightWatchers (Med+, GLP-1 Success) | Yes (WW Clinic) | Dose and site logs, side-effect logs, protein (1 g/kg starting weight), fiber, hydration, dietitians | On-demand strength videos "to retain muscle" | AI Body Scan (3D) | $74-$84/mo after the first month, drugs extra | [S89](https://www.weightwatchers.com/us/how-it-works/glp-1-program), [S90](https://www.weightwatchers.com/us/plans) |
| Calibrate ("Metabolic Reset") | Yes | 1:1 video coaching, lessons; employer coverage | Not mentioned | No | From $199/mo | [S91](https://www.joincalibrate.com/) |
| Found | Yes: compounded and branded, **including Foundayo** | Provider check-ins, in-app tracking and community | Not described | No | Compounded from $99/mo (insurance) or $169/mo (cash) with medication included; branded Wegovy or Zepbound from $650/mo or more | [S92](https://joinfound.com/) |
| Omada | Yes ("GLP-1 Prescribing") | GLP-1 Support, Enhanced GLP-1 Care Track (employers and health plans) | Not detailed | No | Employer or plan | [S93](https://www.omadahealth.com/) (Medium) |
| Sword Pulse | Coordinates with prescribers | Smart scales, wearables, protein guidance, body-composition monitoring | **PT-guided strength training** for GLP-1 users | Sword's Move uses a wearable; Kaia's camera tech has been acquired | Employer-sponsored | [S37](https://insider.fitt.co/sword-health-expands-ai-led-specialty-care/), [S38](https://swordhealth.com/newsroom/sword-health-launches-pulse-ai-cardiometabolic-care), [S39](https://swordhealth.com/articles/exercise-on-glp-1) (Medium) |
| MyFitnessPal GLP-1 Support | No | Dose logs, reminders, side-effect patterns, nutrition | Not described | Meal photo only | Free | [S77](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718), [S78](https://www.bakersfield.com/ap/news/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build/article_594b029e-ed9b-5c1a-ac3b-a4ea46e70908.html) |
| Oura GLP-1 Insights | No (LillyDirect partner) | Dose, schedule, side effects, weight, reminders; Advisor links doses to Readiness | **None.** Oura says to consult a doctor before changing workouts | Meal photo only | Oura membership | [S63](https://ouraring.com/blog/glp-1-insights/) |
| Healthify (India) | Patient support with Novo Nordisk India | AI- and dietitian-guided care | Not verified | Not verified | Not verified | [S84](https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20), [S85](https://www.storyboard18.com/brand-marketing/novo-nordisk-india-and-healthify-launch-ai-driven-support-programme-for-obesity-care-85277.htm) |
| Ro, Hims & Hers | Yes (US telehealth) | Not re-verified; sites blocked automated fetch | Not verified | Not verified | Not verified | See Unverified |

### 3.3 Does any app adapt TRAINING to medications?

- **GLP-1.** Muscle preservation is universal *messaging*, delivered as videos (WW), named programs (Noom "Muscle Defense") or human PTs (Sword Pulse, employer-only). No consumer product was found that does either of the following (Medium):
  - Changes training load according to dose day or side-effect logs.
  - Uses objective rep, form or load data to check that a GLP-1 user is actually doing enough resistance training.
- **The nearest signal.** Oura spots Readiness dips in the roughly 48 hours after a weekly dose. Oura then tells members to consult a clinician before changing workouts, and it does not program training ([S63](https://ouraring.com/blog/glp-1-insights/)).
- **Heart-rate-limiting drugs (beta-blockers and similar).** Apple feeds "medications that might affect heart rate" into its VO2 max estimate. It warns that such medications "might cause an overestimation of your VO2 max" ([S71](https://support.apple.com/en-us/HT211856)). No app was found that switches users on such drugs from HR-zone training to RPE- or talk-test intensity.
- **Insulin and sulfonylureas, statins, anticoagulants, diuretics.** No consumer fitness app found offers exercise safety rules for these drug classes, such as hypoglycemia checks, muscle-symptom flags, fall or impact cautions, or heat and hydration limits. This conclusion rests on the absence of evidence across every product reviewed (Low-Medium). Clinical programs such as Omada handle diabetes care, including CGMs, but through employers and with clinicians ([S93](https://www.omadahealth.com/)).

## 4. Comparison matrix (consumer-reachable products, Oct 2026)

Key: RT = real-time; Upl = post-hoc upload; HW = proprietary hardware required. "Meds" = medication-specific features.

| Product | Camera form feedback | Reps from camera | LLM chat coach | Photo nutrition | Meds | Training adapts to meds | Wearables | Platforms | Price (US / India) |
|---|---|---|---|---|---|---|---|---|---|
| Peloton IQ | RT, HW (select strength moves; Run Analysis on Tread Vision) | Yes | No | No | No | No | Apple Health, Garmin, Fitbit | Peloton HW; app has no camera features | HW $1,695-$6,695 plus membership; app $15.99-$28.99/mo / not checked |
| Tonal 2 | RT cues, HW plus phone side angle | Not verified | No | No | No | No | n/a | Tonal HW | $4,295 plus $59.95/mo / n/a |
| Tempo | Not advertised (pivoted) | Not advertised | No | No | No | No | n/a | App plus weights | VPT from $39/mo |
| Zing AI | RT, phone | Not stated | Yes | **No** | No | No | Apple Watch/Health | iOS (Android not verified) | $18.99-$59.99 in-app purchases |
| Coach.AI | RT, phone, on-device | Yes | Yes | Plans only | No | No | Apple Health | iPhone | $12.99-$24.99 per period |
| Upload form-check apps | Upl | Varies | Mostly no | No | No | No | Varies | Mostly iOS | Freemium |
| Metric VBT | Bar velocity and path (per set) | Yes (complaints) | No | No | No | No | Apple Watch | iOS/iPadOS | $10.99/mo |
| Freeletics | No (camera test unverified) | No | Yes (Coach+) | Separate app | No | No | Apple Watch/Health | iOS/Android | $34.99-$79.99 per 3-12 months |
| Google Health Coach | No | No | Yes (Gemini) | Yes | Records only | No | Fitbit, Pixel Watch | Android/iOS | $9.99/mo / ₹99/mo |
| WHOOP | No | No | Yes | Not documented | EHR meds (US) | No | WHOOP band | iOS/Android | $199-$359/yr / not checked |
| Oura | No | No | Yes | Yes | **GLP-1 Insights** | No | Ring, Stelo CGM | iOS/Android | Not verified / available in India |
| Samsung Health Assistant | No | No | Yes (US beta) | Not verified | No | No | Galaxy Watch/Ring | Android | Not stated |
| Apple Health / Workout Buddy | No | No | No (voice only) | Siri camera nutrition info | Logs; VO2 input | VO2 estimate only | Apple Watch | iOS | Bundled |
| Garmin Connect+ | No | No | Insights only | Yes | No | No | Garmin | iOS/Android | $6.99/mo |
| MyFitnessPal (+Cal AI) | No | No | Yes (Premium) | Yes | **GLP-1 Support** | No | 40+ | iOS/Android | $79.99-$99.99/yr |
| Noom | Face/body scan only | No | Human coach | AI logging | GLP-1Rx, Companion | Content only | Apple Health, Fitbit, Garmin, Withings | iOS/Android | $17/mo; Med $69/mo or more |
| WeightWatchers | AI Body Scan only | No | Human coach | Yes | GLP-1 Success, Med+ | Videos only | Not checked | iOS/Android | $74-$84/mo |
| Sword (Pulse, Phoenix) | Phoenix form guidance (wearable; Kaia CV acquired) | Not verified | Yes (Phoenix, Dawn) | Not verified | GLP-1 program | **PT-guided** | Smart scale, wearables | Employer | Employer-paid |
| Hinge Health | Yes, TrueMotion CV | Not verified | Robin (triage) | No | No | No | n/a | Employer | Employer-paid |
| Healthify (India) | No | No | Ria (AI) | Not verified | GLP-1 program | Not verified | Not checked | iOS/Android | Not verified |
| cult.fit (India) | Not advertised now | Not advertised | No | No | No | No | Google Fit, Apple Health, Fitbit (Medium) | iOS/Android | LIVE ₹449/mo |
| ChatGPT Health / Claude | No | No | Yes | Through connectors | Records | No | Apple Health, Health Connect | Apps/web | Plan-dependent |

**Reading the matrix:** apart from Sword, which is employer-only, no row reaches past "Content only" in the "Training adapts to meds" column. Rows with real-time phone camera feedback (Zing, Coach.AI) have no medication features. Rows with medication features (Oura, MyFitnessPal, Noom, WW, Google records) have no camera feedback on training.

## 5. White space: capabilities no mainstream product offers today

| # | Capability | Evidence that it is unserved | Confidence |
|---|---|---|---|
| W1 | **A coach that knows what the camera saw.** One consumer product where phone camera form and rep data, nutrition logs and medication context feed one conversational coach | Every row in Section 4 lacks at least one of the three. Zing has camera and chat but no nutrition or meds ([S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792)). MyFitnessPal and Oura have chat, nutrition and GLP-1, but no workout verification ([S77](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718), [S63](https://ouraring.com/blog/glp-1-insights/)). Peloton has a camera but no chat ([S2](https://www.onepeloton.com/blog/what-is-peloton-iq)) | Medium-High |
| W2 | **Camera-verified muscle-preservation training for GLP-1 users** (reps, range of motion, load progression, effort), shown as a "muscle protection" score | WW offers videos, Noom "Muscle Defense," Sword PTs (employer-only). Body scans exist (WW, Noom, Zing, Tempo), but none of these verifies the training itself ([S89](https://www.weightwatchers.com/us/how-it-works/glp-1-program), [S88](https://apps.apple.com/us/app/noom-weight-loss-glp-1-care/id634598719), [S37](https://insider.fitt.co/sword-health-expands-ai-led-specialty-care/)) | Medium |
| W3 | **Dose-cycle-aware scheduling**: move hard sessions away from post-dose fatigue or nausea days, and deload when side effects are logged | Oura detects the post-dose Readiness dip but explicitly does not change workouts. MyFitnessPal logs side effects only ([S63](https://ouraring.com/blog/glp-1-insights/), [S78](https://www.bakersfield.com/ap/news/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build/article_594b029e-ed9b-5c1a-ac3b-a4ea46e70908.html)) | Medium |
| W4 | **Medication-class exercise safety rules beyond GLP-1** (beta-blockers: RPE instead of HR zones; insulin or sulfonylureas: hypoglycemia precautions; anticoagulants: impact and fall caution; diuretics: heat and hydration) | Only Apple's VO2 max input was found ([S71](https://support.apple.com/en-us/HT211856)) | Low-Medium (absence of evidence) |
| W5 | **Phone-only form feedback for gym barbell lifts that people trust** | Real-time is on $2.7k+ hardware ([S1](https://www.onepeloton.com/peloton-iq)). Phone apps are post-hoc or draw accuracy complaints ([S31](https://apps.apple.com/us/app/metric-strength-training/id1595510857)) | Medium |
| W6 | **India-first version**: Hindi/Hinglish voice cues, Indian-food photo logging, support for the generic-semaglutide era, priced against ₹99-₹449/mo anchors | Healthify covers nutrition and GLP-1 without a camera. cult.fit no longer advertises camera features. Google's coach costs ₹99 but has no camera ([S84](https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20), [S50](https://apps.apple.com/in/app/cult-fit-gym-workout-fitness/id1217794588), [S55](https://www.tech2.com/gadgets/google-replaces-fitbit-app-with-google-health-brings-health-coach-to-india-text-ws-l-10080257.html)) | Medium |

Already table stakes, so **not** white space: AI meal photo logging, chat over wearable data, GLP-1 dose and side-effect logging, camera body-composition scans, upload-a-video form checks, and on-device "no video stored" privacy promises.

## 6. Are the founder's ideas already served? The honest answer

**Idea 1: correct exercise form with the phone camera. Already served; not unique.**
- Peloton and Tonal do it in real time on hardware ([S2](https://www.onepeloton.com/blog/what-is-peloton-iq), [S9](https://www.tonal.com/products/tonal-2)).
- Zing and Coach.AI do it in real time on a phone ([S17](https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792), [S18](https://apps.apple.com/us/app/coach-ai/id6504732473)).
- At least nine apps analyze uploaded videos.
- Hinge, Sword/Kaia, Exer and Kemtai do it clinically.
- QuickPose, Sency and Kemtai sell it as an SDK; QuickPose claims 500+ apps ([S44](https://quickpose.ai/)).

**Idea 2: a "special agent" chatbot for fitness, diet and medication. Largely served; not unique.**
- Google Health Coach covers fitness plans, meal photos and medical records ([S53](https://techcrunch.com/?p=3120136)).
- MyFitnessPal combines an AI Coach with GLP-1 Support ([S77](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718)).
- Oura combines Advisor, Meals and GLP-1 Insights ([S63](https://ouraring.com/blog/glp-1-insights/)).
- WHOOP Coach has EHR access, including medications ([S59](https://www.businesswire.com/news/home/20260508464188/en)).
- ChatGPT Health and Claude reason over medical records and app data ([S100](https://m.gsmarena.com/openai_launches_chatgpt_health_with_apple_health_and_myfitnesspal_integration-news-71006.php), [S102](https://fortune.com/2026/01/11/anthropic-unveils-claude-for-healthcare-and-expands-life-science-features-partners-with-healthex-to-let-users-connect-medical-records/)).

**What is still defensibly differentiated: the closed loop, not either feature alone.**
1. **See.** On-device pose estimation turns each set into structured data: reps, range of motion, tempo, form-error codes, and an estimated rep quality or reps in reserve (RIR).
2. **Reason.** A coach grounded on that training data plus nutrition (especially protein) plus the medication schedule and side effects plus wearables.
3. **Adapt.** The next sessions change: dose-cycle-aware load, deloads after side effects, and RPE instead of HR for heart-rate-limiting drugs. Every change has a visible "why."
4. **Prove.** Show GLP-1 users a muscle-preservation trend built from verified strength progression, not just weight or body-scan estimates.

The wedge is "**strength coaching for people on weight-loss medication, verified by your camera**." Nobody owns it in consumer apps as of Oct 2026. It turns two commodity features into one outcome that GLP-1 programs talk about but do not measure.

The moat has three parts:
1. A labeled form-error dataset that grows with use.
2. A clinician-reviewed library of medication-exercise rules.
3. Outcome data on strength retention.

Pose-estimation code is not a moat.

## 7. Threats: who could copy fast, and how

| Player | Assets that make copying easy | Likely move | Speed |
|---|---|---|---|
| **Google (Google Health)** | Owns MediaPipe pose ([S45](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker)); Gemini coach already asks about equipment and injuries and reads medical records ([S53](https://techcrunch.com/?p=3120136)); ₹99/mo India price | Add a camera "form check" inside the Fitness tab; read medications from records | Fast (months) |
| **Peloton** | Form models from Guide and IQ; camera hardware fleet; CTO wants form feedback "across all of our modalities" ([S7](https://www.pelobuddy.com/form-feedback-more/)); App+ has mass reach ([S8](https://apps.apple.com/us/app/id792750948)) | Port camera form feedback to the phone app; add GLP-1 strength programs | Medium |
| **MyFitnessPal (+Cal AI)** | Nutrition, GLP-1 Support and AI Coach; serial acquirer (Intent, Cal AI) ([S81](https://athletechnews.com/myfitnesspal-cal-ai-acquisition)) | License a CV SDK or acquire a form-check app; add a "GLP-1 strength plan" | Fast (acquisition) |
| **Sword Health** | Pulse (GLP-1 strength plus PT), Phoenix conversational AI, Kaia's camera tech, Dawn shows direct-to-consumer intent ([S37](https://insider.fitt.co/sword-health-expands-ai-led-specialty-care/), [S34](https://swordhealth.com/newsroom/sword-acquires-kaia-health)) | Launch Pulse direct to consumers | Medium |
| **Oura / WHOOP** | GLP-1 Insights and Advisor; WHOOP's $10.1B valuation and EHR medications ([S63](https://ouraring.com/blog/glp-1-insights/), [S58](https://hlth.com/insights/news/whoop-expands-digital-health-offering-with-healthex-integration-and-clinician-video-visits)); WHOOP lists "expanded strength training analytics" as planned | Add training adaptations to GLP-1 features; partner for CV | Medium |
| **Apple** | Vision 3D body pose, Workout Buddy, Health redesign late 2026, a planned camera-based walking analysis ([S70](https://9to5mac.com/2026/02/05/apple-reportedly-scales-back-plans-for-ai-powered-health-coach/), [S69](https://www.apple.com/health/)) | Camera features in Health or Fitness | Slow-Medium (recently retrenched) |
| **GLP-1 telehealth** (Noom, WW, Ro, Hims, Found, Calibrate, Healthify) | Patient distribution and prescribing; they already promise muscle preservation | License an SDK such as QuickPose or Kemtai ([S44](https://quickpose.ai/), [S42](https://kemtai.com/)) | Fast. They could also become **partners or customers** |
| **General assistants** (ChatGPT, Claude, Gemini) | Free or cheap chat over Apple Health and records | Make chat-only coaching a commodity | Already here |

## Recommendations for the docs

1. **Positioning (BRD).** Do not claim "first camera form correction" or "first fitness, diet and medication chatbot"; both are false (Section 6). Claim the closed loop instead: "the strength coach that sees your reps and plans around your medication." Make GLP-1 users the launch segment.
2. **MVP scope (BRD, Roadmap).**
   - Phone-only, with no hardware. Peloton Guide's exit and the $2.7k+ hardware pricing show the hardware path is closed to a startup.
   - Real-time feedback for a **small, validated movement set**: 8-12 bodyweight and dumbbell basics.
   - Post-hoc upload analysis for barbell lifts in the gym.
   - Peloton itself limits feedback to "select movements" ([S4](https://www.onepeloton.com/new-2026-tread-plus-vision)).
3. **Camera spec (Tech Spec).**
   - On-device pose using MediaPipe Pose Landmarker or Apple Vision ([S45](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker)).
   - Camera-angle guidance for each exercise, a lighting and framing check, and confidence gating: say nothing rather than give a wrong cue.
   - Publish rep-count and cue accuracy targets as release gates. Metric and Tempo reviews show missed reps destroy trust ([S31](https://apps.apple.com/us/app/metric-strength-training/id1595510857), [S14](https://techcrunch.com/?p=1951028)).
   - Default to "video never stored," matching Peloton and Kemtai ([S1](https://www.onepeloton.com/peloton-iq), [S42](https://kemtai.com/)).
4. **Coach spec (Tech Spec, Innovative Features).**
   - Ground the LLM in structured data: per-set form metrics, sessions, meals, medications, side effects and wearables.
   - Parity features: user-editable memory (WHOOP and Oura), proactive check-ins, and photo, voice and barcode meal logging.
   - Differentiators: every plan change explains itself in terms of form, nutrition and medication events.
   - Opt out of AI training by default, and keep AI-training consent separate from core app functions. Samsung's beta drew criticism for linking them ([S66](https://www.webpronews.com/samsungs-new-ai-health-assistant-turns-wearable-data-into-actionable-advice/)).
5. **Medication module (BRD, Tech Spec, Playbook).**
   - Phase 1 covers GLP-1 class drugs in weekly injectable and daily oral forms (Wegovy, Zepbound, Foundayo, generics): dose, schedule and side-effect logging; protein and fiber targets; dose-cycle-aware training (W2, W3).
   - Phase 2 adds a clinician-reviewed rules engine for heart-rate-limiting drugs, glucose-lowering drugs, anticoagulants and diuretics (W4).
   - Never advise on dosing. Copy Oura-style disclaimers ([S63](https://ouraring.com/blog/glp-1-insights/)).
   - Route this through the regulatory brief, because medication-specific advice may raise medical-device questions.
6. **Pricing (Roadmap).** Anchors are Google $9.99 (₹99), Garmin $6.99, MyFitnessPal $79.99/yr, Ladder $29.99, Future $199, and GLP-1 programs at $69-$199 excluding drugs. One option to test: a consumer tier around $9.99-$14.99/mo, with GLP-1-specific features as a premium or B2B2C add-on. This is a recommendation, not market data.
7. **Go-to-market.** Pitch GLP-1 telehealth and pharma patient-support programs as a white-label "verified muscle-preservation" module. Healthify already does patient support with Novo Nordisk India ([S84](https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20)).
8. **India.** Hindi and English voice cues, an Indian food database, and support for generic semaglutide names. Plan pricing against the ₹99 and ₹449 anchors.
9. **Integrations.** Read Apple Health and Health Connect for weight, heart rate and sleep. Do not depend on one wearable. Consider being a data source for ChatGPT Health and Claude rather than competing with them on generic chat.
10. **Competitive monitoring.** Assign owners to watch the Peloton app (camera port), Google Health Coach (camera or medications), the Apple Health redesign (late 2026), MyFitnessPal acquisitions, Sword Pulse going direct to consumers, and Oura or WHOOP strength features.

## Unverified / conflicting

- **Peloton:** US All-Access price was not verified; the only figure found is UK All-Access at £45/mo ([S3](https://www.onepeloton.com/en-GB/blog/whats-new-2026-treadmill-updates)). No user feedback on Peloton IQ form accuracy was gathered. The "2,000+ movement-tracking workouts" figure came from a search summary only.
- **Tread+ Vision warranty:** Peloton's own page states both 3-year and 5-year terms ([S4](https://www.onepeloton.com/new-2026-tread-plus-vision)).
- **Tonal:** rep counting by the camera versus the motor was not verified. The Tonal 2 announcement date is reported as Jan 2025 ([S12](https://insider.fitt.co/tonal-2-release/)).
- **Zing:** Android availability, explicit rep counting, and the "1M downloads / $10M Series A" figures (secondary sources) were not verified.
- **Fitbod:** the June 2026 price ($15.99/mo) comes from a competitor ([S23](https://www.sensai.fit/blog/fitbod-review-2026)). An aggregator claims a beta "AI form-check" feature; it is unconfirmed.
- **Freeletics:** the camera testing claim is undated ([S21](https://www.redbull.com/gb-en/ai-coaches-are-the-future-of-fitness)).
- **Metric:** the annual Pro price is $79.99 on the live listing but $62.99 in a search snippet.
- **trainwell:** the current price was not verified ($99/mo in 2023).
- **WHOOP:** tier prices come from aggregators.
- **Oura:** membership price and India price were not verified.
- **Google Health Coach:** sources disagree on Apple HealthKit data and non-Fitbit device support ("coming soon" per [S53](https://techcrunch.com/?p=3120136)). Medication awareness is not stated.
- **Samsung Health Assistant:** the model behind it is not disclosed, and the privacy-consent controversy is reported, not confirmed.
- **Apple Workout Buddy languages:** English-only at launch; English and Spanish on the watchOS 27 page.
- **Strava Athlete Intelligence:** current status was not re-verified. The Strava + Runna bundle is $149.99 on one site and $119.99 in a Wareable article ([S75](https://the5krunner.com/2026/10/14/is-runna-free/), [S76](https://www.wareable.com/sport/strava-runna-combined-subscription-announcement-price)).
- **Cal AI:** the site claims "5M users," while the press reports "15M+ downloads." The "about 80% accurate" figure is self-reported.
- **Healthify:** pricing, Ria's role in the GLP-1 program, and photo logging were not re-verified (site blocked).
- **India semaglutide generics:** launch dates and prices were not verified.
- **Ro and Hims & Hers:** current offerings, prices and app features could not be fetched. Do not cite specifics.
- **Sword:** Pulse launch date and channel (employer vs consumer) are unclear. "Real-time form correction" for Phoenix rests on an undated LinkedIn post. A reported Sword-Headspace deal appears only in an aggregator.
- **Status checks:** Lumin Fitness (no 2026 news), Zenia (status unclear) and Onyx (standalone status unknown) need confirmation.
- **Kemtai:** partner names were inferred from logo filenames.
- **Foundayo:** self-pay prices vary by dose; reports range from $149 to $349.
- **Apple Vision 3D pose:** the documentation page did not render, so the OS minimum is not confirmed.

## Sources

1. [S1] Peloton IQ (product page): https://www.onepeloton.com/peloton-iq
2. [S2] Peloton blog, "What is Peloton IQ" (Oct 1, 2025): https://www.onepeloton.com/blog/what-is-peloton-iq
3. [S3] Peloton UK blog, "What's new: 2026 treadmill updates" (Sep 22, 2026): https://www.onepeloton.com/en-GB/blog/whats-new-2026-treadmill-updates
4. [S4] Peloton Tread+ Vision: https://www.onepeloton.com/new-2026-tread-plus-vision
5. [S5] Peloton Tread Vision: https://www.onepeloton.com/new-2026-tread-vision
6. [S6] The Clip Out, "Peloton has stopped sales on The Guide": https://theclipout.com/peloton-guide-discontinued/
7. [S7] Pelo Buddy, "Form feedback & more" (Oct 14, 2025): https://www.pelobuddy.com/form-feedback-more/
8. [S8] App Store, Peloton: Fitness & Workouts: https://apps.apple.com/us/app/id792750948
9. [S9] Tonal 2 product page: https://www.tonal.com/products/tonal-2
10. [S10] Tonal Knowledge Base, Tonal 2 camera troubleshooting: https://knowledge.tonal.com/kb/guide/en/troubleshooting-tonal-2-camera-YUcew2ZBxF/Steps/3980893
11. [S11] Athletech News, Tonal Daily Lift (Jul 23, 2025): https://athletechnews.com/tonal-daily-lift-ai-workouts/
12. [S12] Fitt Insider, Tonal 2 release (Jan 8, 2025): https://insider.fitt.co/tonal-2-release/
13. [S13] Tempo homepage: https://tempo.fit/
14. [S14] TechCrunch, Tempo review: https://techcrunch.com/?p=1951028
15. [S15] Dallas Innovates, Lumin Fitness 13-unit franchise deal: https://dallasinnovates.com/dallas-gamified-lumin-fitness-inks-franchise-agreement-for-13-new-texas-clubs/
16. [S16] Athletech News, Lumin Fitness Louisiana deal: https://athletechnews.com/ai-powered-studio-lumin-fitness-signs-louisiana-franchise-deal/
17. [S17] App Store, Zing AI: Home & Gym Workouts: https://apps.apple.com/us/app/zing-ai-personal-trainer/id1552207792
18. [S18] App Store, Coach.AI: https://apps.apple.com/us/app/coach-ai/id6504732473
19. [S19] App Store, Freeletics: https://apps.apple.com/us/app/freeletics-workouts-fitness/id654810212
20. [S20] Freeletics blog, Coach+: https://www.freeletics.com/blog/posts/freeletics-coach-plus/
21. [S21] Red Bull, "AI coaches are the future of fitness": https://www.redbull.com/gb-en/ai-coaches-are-the-future-of-fitness
22. [S22] Fitbod homepage: https://fitbod.me/
23. [S23] SensAI, Fitbod review 2026: https://www.sensai.fit/blog/fitbod-review-2026
24. [S24] App Store, Form Fix: AI Form Check Coach: https://apps.apple.com/us/app/id6745452870
25. [S25] Formax listing: https://mwm.ai/apps/formax-ai-workout-feedback/6756526116
26. [S26] App Store, GymSpotter: https://apps.apple.com/app/id6758680413
27. [S27] App Store, SquatEye: https://apps.apple.com/ca/app/id6758864722
28. [S28] App Store, FormCheck AI: https://apps.apple.com/lb/app/formcheck-ai/id6741048432
29. [S29] AppGoblin, Gym Assistant - AI Form Check: https://appgoblin.info/apps/6782565845
30. [S30] App Store, Gymscore: https://apps.apple.com/app/id6744373919
31. [S31] App Store, Metric - Strength Training: https://apps.apple.com/us/app/metric-strength-training/id1595510857
32. [S32] Metric homepage: https://metric.coach
33. [S33] Hinge Health IR, "Hinge Health unveils new AI-powered care tools" (Oct 21, 2025): https://ir.hingehealth.com/news/news-details/2025/Hinge-Health-unveils-new-AI-powered-care-tools/default.aspx
34. [S34] Sword newsroom, "Sword acquires Kaia Health" (Jan 28, 2026): https://swordhealth.com/newsroom/sword-acquires-kaia-health
35. [S35] MobiHealthNews, Sword acquires Kaia ($285M): https://www.mobihealthnews.com/news/sword-health-acquires-kaia-health-285m
36. [S36] Sword, "Introducing Phoenix" (Jun 4, 2024): https://swordhealth.com/articles/introducing-phoenix
37. [S37] Fitt Insider, Sword expands AI-led specialty care (Mar 12, 2026): https://insider.fitt.co/sword-health-expands-ai-led-specialty-care/
38. [S38] Sword newsroom, Pulse launch: https://swordhealth.com/newsroom/sword-health-launches-pulse-ai-cardiometabolic-care
39. [S39] Sword, "Exercise on GLP-1" (Dec 19, 2025): https://swordhealth.com/articles/exercise-on-glp-1
40. [S40] App Store, Exer Health: https://apps.apple.com/app/id1505858367
41. [S41] MobiHealthNews, Exer AI and Mayo Clinic: https://www.mobihealthnews.com/news/exclusive-exer-ai-expands-partnership-mayo-clinic-clinical-deployment
42. [S42] Kemtai homepage: https://kemtai.com/
43. [S43] Sency homepage: https://www.sency.ai/
44. [S44] QuickPose homepage: https://quickpose.ai/
45. [S45] Google AI Edge, MediaPipe Pose Landmarker: https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker
46. [S46] Apple Developer, VNDetectHumanBodyPose3DRequest: https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest
47. [S47] VentureBeat, Cure.fit acquires Onyx: https://venturebeat.com/business/cure-fit-acquires-ai-body-tracker-onyx-to-enable-two-way-workout-videos
48. [S48] Entrackr, Curefit-Onyx deal: https://entrackr.com/?p=100850
49. [S49] Dealroom, Zenia: https://app.dealroom.co/companies/zenia
50. [S50] App Store India, cult.fit: https://apps.apple.com/in/app/cult-fit-gym-workout-fitness/id1217794588
51. [S51] Analytics India Magazine, tech behind cult.fit live: https://analyticsindiamag.com/the-tech-powering-cult-fits-live-fitness-offerings/
52. [S52] DC Rainmaker, watchOS 26 Workout Buddy real-world beta (Jul 2025): https://www.dcrainmaker.com/2025/07/apple-watchos-26-workout-beta-real-world.html
53. [S53] TechCrunch, Google Health app and Health Coach (May 7, 2026): https://techcrunch.com/?p=3120136
54. [S54] CGMagazine, Fitbit Air and Google Health app: https://www.cgmagonline.com/news/google-fitbit-air-and-google-health-app/
55. [S55] Tech2, Google Health Coach comes to India (May 8, 2026): https://www.tech2.com/gadgets/google-replaces-fitbit-app-with-google-health-brings-health-coach-to-india-text-ws-l-10080257.html
56. [S56] Google blog, personal health coach public preview: https://blog.google/products/fitbit/personal-health-coach-public-preview/
57. [S57] TechRepublic, Fitbit AI coach expands to iOS: https://www.techrepublic.com/article/news-fitbit-ai-coach-expands-ios-five-markets/
58. [S58] HLTH, WHOOP HealthEx integration and clinician visits (May 13, 2026): https://hlth.com/insights/news/whoop-expands-digital-health-offering-with-healthex-integration-and-clinician-video-visits
59. [S59] Business Wire, WHOOP expands health platform (May 8, 2026): https://www.businesswire.com/news/home/20260508464188/en
60. [S60] TrackerVS, WHOOP pricing 2026: https://trackervs.com/pricing/whoop-pricing/
61. [S61] Oura blog, Oura Advisor: https://ouraring.com/blog/oura-advisor/
62. [S62] Business Wire, Oura Meals and Glucose (May 6, 2025): https://www.businesswire.com/news/home/20250506997981/en
63. [S63] Oura blog, GLP-1 Insights (May 28, 2026): https://ouraring.com/blog/glp-1-insights/
64. [S64] Samsung Newsroom, Health Assistant beta: https://news.samsung.com/global/samsung-launches-health-assistant-beta-first-fully-integrated-ai-powered-personal-health-assistant
65. [S65] AI Weekly, Samsung Health Assistant US beta: https://aiweekly.co/alerts/samsung-opens-health-assistant-ai-beta-to-us-galaxy-users
66. [S66] WebProNews, Samsung AI Health Assistant: https://www.webpronews.com/samsungs-new-ai-health-assistant-turns-wearable-data-into-actionable-advice/
67. [S67] Apple, watchOS 27: https://www.apple.com/os/watchos/
68. [S68] Apple, iOS 27: https://www.apple.com/os/ios/
69. [S69] Apple, Health: https://www.apple.com/health/
70. [S70] 9to5Mac, Apple scales back AI health coach (Feb 5, 2026): https://9to5mac.com/2026/02/05/apple-reportedly-scales-back-plans-for-ai-powered-health-coach/
71. [S71] Apple Support, cardio fitness (VO2 max) on Apple Watch: https://support.apple.com/en-us/HT211856
72. [S72] TechRadar, Garmin Connect+ launch: https://www.techradar.com/health-fitness/garmin-adds-premium-garmin-connect-tier-with-ai-features-but-promises-your-free-experience-is-not-going-away
73. [S73] DC Rainmaker, Garmin Connect nutrition logging (Jan 5, 2026): https://www.dcrainmaker.com/2026/01/garmin-connect-nutrition-logging-connect.html
74. [S74] the5krunner, Garmin Connect+ review (2026): https://the5krunner.com/2026/04/20/garmin-connect-plus-review/
75. [S75] the5krunner, "Is Runna free?" (Oct 14, 2026): https://the5krunner.com/2026/10/14/is-runna-free/
76. [S76] Wareable, Strava + Runna bundle price: https://www.wareable.com/sport/strava-runna-combined-subscription-announcement-price
77. [S77] App Store, MyFitnessPal: https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718
78. [S78] AP via Bakersfield.com, MyFitnessPal launches GLP-1 Support (Apr 28, 2026): https://www.bakersfield.com/ap/news/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build/article_594b029e-ed9b-5c1a-ac3b-a4ea46e70908.html
79. [S79] Wareable, MyFitnessPal AI Coach: https://www.wareable.com/health-and-wellbeing/myfitnesspal-nutrition-ai-coach-feature-announcement
80. [S80] AP via AOL, MyFitnessPal 2026 Winter Release (Feb 24, 2026): https://lite.aol.com/sports/other/story/0022/20260224/9659625.htm
81. [S81] Athletech News, MyFitnessPal acquires Cal AI: https://athletechnews.com/myfitnesspal-cal-ai-acquisition
82. [S82] Fitt Insider, MyFitnessPal acquires Cal AI (Mar 2, 2026): https://insider.fitt.co/myfitnesspal-acquires-rival-food-tracker-cal-ai/
83. [S83] Cal AI homepage: https://www.calai.app/
84. [S84] Reuters via MarketScreener, Healthify and Novo Nordisk (Dec 5, 2025): https://uk.marketscreener.com/news/india-s-healthify-eyes-more-weight-loss-drugmaker-tie-ups-after-novo-nordisk-pact-ce7d51dcda81ff20
85. [S85] Storyboard18, Novo Nordisk India and Healthify program: https://www.storyboard18.com/brand-marketing/novo-nordisk-india-and-healthify-launch-ai-driven-support-programme-for-obesity-care-85277.htm
86. [S86] Inc42, India's GLP-1 era and Healthify: https://inc42.com/features/ozempic-mounjaro-india-healthify-weight-loss-shift
87. [S87] Smartprix, FITTR HART X2 price: https://www.smartprix.com/smart_rings/fittr-hart-x2-smart-ring-ppd1gjer3vue
88. [S88] App Store, Noom: https://apps.apple.com/us/app/noom-weight-loss-glp-1-care/id634598719
89. [S89] WeightWatchers, GLP-1 Success program: https://www.weightwatchers.com/us/how-it-works/glp-1-program
90. [S90] WeightWatchers, plans: https://www.weightwatchers.com/us/plans
91. [S91] Calibrate homepage: https://www.joincalibrate.com/
92. [S92] Found homepage: https://joinfound.com/
93. [S93] Omada Health homepage: https://www.omadahealth.com/
94. [S94] Future homepage: https://www.future.co/
95. [S95] Ladder homepage: https://www.joinladder.com/
96. [S96] Ladder pricing: https://www.joinladder.com/pricing
97. [S97] trainwell, "CoPilot has renamed to trainwell": https://trainwell.net/copilot
98. [S98] TechCrunch, CoPilot one-on-one coaching (Oct 4, 2023): https://techcrunch.com/2023/10/04/copilot-app-pairs-users-with-one-on-one-remote-fitness-coaches-raises-6-3m
99. [S99] OpenAI, "Introducing ChatGPT Health": https://openai.com/blog/introducing-chatgpt-health
100. [S100] GSMArena, ChatGPT Health with Apple Health and MyFitnessPal: https://m.gsmarena.com/openai_launches_chatgpt_health_with_apple_health_and_myfitnesspal_integration-news-71006.php
101. [S101] Canadian Running, ChatGPT Health partners with fitness apps: https://runningmagazine.ca/health-nutrition/chatgpt-health-to-partner-with-popular-fitness-apps/
102. [S102] Fortune, Anthropic unveils Claude for Healthcare (Jan 11, 2026): https://fortune.com/2026/01/11/anthropic-unveils-claude-for-healthcare-and-expands-life-science-features-partners-with-healthex-to-let-users-connect-medical-records/
103. [S103] Scientific American, Foundayo vs Wegovy: https://scientificamerican.com/article/how-eli-lillys-new-glp-1-pill-stacks-up-against-wegovy-and-other-weight-loss
104. [S104] PharmaShots, FDA approval of Foundayo: https://pharmashots.com/32510/eli-lilly-reports-us-fda-approval-of-foundayo-orforglipron-for-weight-loss/
105. [S105] cure.fit, Gurgaon cultpass listing: https://www.cure.fit/cult/cult-pass/gurgaon/Cult-Gym-Eros-Sector-49/590
106. [S106] tech.eu, Sword raises $40M at a $4B valuation (Jun 17, 2025): https://tech.eu/2025/06/17/sword-health-raises-40m-at-4b-valuation-to-expand-ai-first-care-into-mental-health/
107. [S107] Tempo blog, "Introducing the Tempo Move": https://tempo.fit/blog/introducing-the-tempo-move

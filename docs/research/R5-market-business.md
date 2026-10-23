# R5: Market, Pricing and Subscription/Acquisition Benchmarks for an AI Form-Correction and AI-Coach Fitness App (US, UK/EU, India)

As of 16 Oct 2026. This brief is for the people writing the BRD, Tech Spec, Roadmap, Innovative Features doc and Build Playbook.

**Confidence labels.** High means a primary page was read directly in this session. Medium means a reputable secondary source, or a primary page with some ambiguity. Low means a vendor or aggregator figure, or a search snippet that was not opened. Bracketed numbers point to the Sources list. The web-search budget ran out partway through the research. After that, facts were checked only by fetching known primary URLs directly, and anything left unchecked is listed under "Unverified / conflicting".

## Summary

- **Market size depends a lot on who you ask.** Estimates for the global fitness-app market in 2026 range from $13.8B to $28.7B. Grand View Research (GVR) puts it at $12.1B in 2025, $13.9B in 2026 and $33.6B in 2033, a 13.4% CAGR [1]. Use GVR as the base case. GVR's country figures for 2025 are US $4.10B, UK $455M and India $602M, and India grows fastest at a 14.9% CAGR [6][7][8]. (High that GVR says this; Low that any single number is "true".)
- **GLP-1 users are now a mass market in the US.** Gallup found that 11% of US adults were taking a GLP-1 for weight loss in May–June 2026, up from 3% in 2024 [18]. KFF found 12% taking one for any reason in Oct–Nov 2025, and 18% had ever taken one [17]. That is about 29–31M adults, every one of whom is told to protect muscle. Gallup links regular exercise to higher perceived drug effectiveness [19]. (High)
- **India's GLP-1 prices have collapsed.** The core semaglutide patents expired in March 2026. Generics now cost about ₹1,290–₹4,200/month, against more than ₹10,000/month for the brand before. Novo cut starting-dose prices by up to 48% [22][23][24]. (Medium-High)
- **Camera form feedback is not new, so it cannot be the headline differentiator.** Zing already does real-time form monitoring with a phone camera ("Zing Vision") [35]. Peloton IQ offers Form Feedback and Rep Tracking through a camera on its Plus hardware, at no extra charge [32]. Tempo (hardware) and Kemtai (clinical, B2B) do too [37][40]. The founder's "not in any fitness app" premise is false. Differentiate on GLP-1/medication-aware muscle preservation, accuracy on free-weight lifts with only a phone, and India.
- **US price bands.** AI strength coaches charge $15–$30/month or $60–$180/year (Fitbod $15.99/$95.99, Zing ~$19.99/$59.99, Ladder $29.99/$179.99) [26][35][50]. Platform subscriptions sit around $10/month (Apple Fitness+, Google Health Premium, Oura at $5.99) [29][43][42]. Noom's GLP-1 programs cost $199–$299/month including medication [44]. Human remote coaching runs about $199/month [51]. India's digital ceiling is ₹149–₹449/month or ₹999–₹2,000/year (Apple Fitness+ ₹149/₹999, cult.fit LIVE ₹449/₹1,999, Fitbod ₹399/₹1,999) [31][53][28].
- **Health & Fitness is the best-monetizing subscription category, but the medians are modest.** RevenueCat's 2026 report gives D30 download→trial 6.9%, trial→paid 37.7%, D35 download→paid 2.9%, and median prices of $9.99/month and $39.94/year [56]. Adapty puts install LTV at $1.21, the highest category, and says annual plans' share of Health & Fitness revenue rose from 51% to 61% between 2023 and 2025 [58]. (High)
- **The first renewal is where subscribers are lost.** Across all apps, median year-1 retention is 28% for annual plans (down from 31%) and 8% for monthly. Median first renewal for annual plans is 26% in North America and 22% in India/SE Asia [56]. Refund medians are 3–5%, but 7.7% in India/SE Asia [56]. Health & Fitness had a 4.71% refund rate in the 2025 report [57]. (High)
- **India converts much worse than the US.** Comparing North America with India/SE Asia: trial→paid 34.2% vs 15.2%, D35 download→paid 2.8% vs 0.7%, and D60 revenue per install $0.55 vs $0.11 [56]. Adapty's weekly-price index for Health & Fitness is 1.3 in the UK, France and Germany and 0.3 in India [58]. (High)
- **Acquisition costs.** On Apple Ads, the US cost per tap is $1.58 and the cost per download is $2.51. Health & Fitness niches cost $1.89–$3.97 per download [59]. In the US, Health & Fitness has the highest Apple Ads install→paid rate at 7.80%, which implies roughly $32–$41 per paying subscriber [60]. India Health & Fitness installs cost about $0.20 on Android and $0.60 on iOS (vendor-compiled, Low) [61].
- **AI cost is material on Opus 5.5.** In the usage model below, Opus 5.5 costs about $2.23 per active premium user-month. That is 18–22% of net revenue at $14.99/month or $89.99/year. Sonnet 5.5 is about half that and Haiku 5.5 about $0.06. The hidden cost is AI in the free tier: at $0.35 of Opus usage per install and 3% install→paid, free users cost $11.67 per acquired payer.
- **US base case only breaks even at the default settings.** It gives LTV36/CAC of 1.08 with payback around month 25. Four changes each improve it: raising the price to $119.99/year (1.63), more organic installs (1.62), top-quartile conversion (2.44), and capping free-tier AI (1.22–1.26). The pessimistic case loses money even before CAC.
- **India at ₹2,499/year does not work on Opus.** LTV36/CAC is 0.38. It works only with tight quotas plus a cheaper model approved through evals (Haiku: 1.36), or with B2B revenue.
- **Draft pricing.** A free tier with on-device form checks. Premium at $14.99/month, $89.99/year, £12.99/£79.99, or ₹349/₹2,499. Premium+ ("GLP-1 Strength") at $29.99/month, $179.99/year, £24.99/£149.99, or ₹699/₹4,999. A 7-day trial on annual plans only.
- **Store fees.** Apple takes 15% under the Small Business Program; otherwise 30% in a subscriber's first year and 15% after [69][70]. US apps may now link out to web checkout [71]. Google Play subscriptions pay 15%, which from 30 Jun 2026 in the US, UK and EEA is 10% plus a 5% billing fee [72]. UK prices include 20% VAT [75].
- **B2B anchors.** Physitrack charges $18.99 per practitioner per month plus $8 per active remote-monitoring patient per month [67][68]. Trainerize runs from free to $248/month [64]. In the US, 83% of large firms run wellness programs and 43% of firms with 5,000+ workers cover GLP-1s for weight loss [21]. Global corporate wellness is $55.1B [11].

## 1. Market size and growth

### 1.1 Global fitness-app market: the spread between firms

| Publisher (date) | 2025 | 2026 | Long-range | CAGR | Notes | Conf. |
|---|---|---|---|---|---|---|
| Grand View Research (2026–33 edition) [1] | $12.1B | $13.9B | $33.6B (2033) | 13.4% (2026–33) | North America 39.8% share; iOS 52.0%; exercise & weight-loss 53.7%; smartphones 66.7% | High |
| Towards Healthcare (updated 21 Aug 2026) [2] | $12.1B | $13.81B | $45.45B (2035) | 14.15% | Same base year as GVR, longer horizon | High |
| The Business Research Co. (via GII listing) [3] | $17.71B | $22.36B | — | 26.2% (2025–26) | Wider definition likely | Low |
| Wellness Creatives [4] | — | $28.7B | — | — | Method unknown | Low |
| Allied Market Research (older) [5] | — | — | $120.37B (2030) | — | Much broader scope; treat as an outlier | Low |

Use GVR as the base. It is the only publisher where we also have matching country figures, and Towards Healthcare independently shows the same $12.1B for 2025.

### 1.2 Country figures (GVR Horizon, revenue)

| Market | 2025 | 2033 | CAGR 2026–33 | Conf. |
|---|---|---|---|---|
| US [6] | $4,097.9M | $10,301.5M | 12.0% | High |
| UK [7] | $455.3M | $1,293.4M | 13.7% | High |
| India [8] | $601.6M | $1,847.9M | 14.9% | High |

An EU-wide figure was not retrieved, so that is a gap.

### 1.3 Adjacent segments

- **Connected gym equipment** (Peloton, Tonal and Tempo-style hardware): $3.0B in 2025, $3.4B in 2026, $14.0B by 2033, a 22.2% CAGR. North America holds 51.14% [9]. (High; the FAQ on the same page misprints "USD 14.0 million".)
- **GLP-1 receptor-agonist drugs**: $66.4B in 2025, $82.0B in 2026, $185.3B by 2033, a 12.4% CAGR. North America holds 75.5%. Obesity and chronic weight management is the fastest-growing use at 25.3% CAGR [10]. (High)
- **Corporate wellness**: $55.1B in 2025 and $70.1B by 2033, a 3.1% CAGR. North America holds 39.0% [11]. India is $664.5M in 2025 and $912.5M by 2033, a 4.1% CAGR [12]. (High)
- **"AI fitness"** as its own segment could not be verified. The GVR pages tried returned no market data.

### 1.4 Users, gyms and trainers

- **US commercial fitness facilities**: 55,000+ (Health & Fitness Association, HFA) [14]. (High)
- **US gym member totals**: HFA's 2025 US Consumer Report (2024 data, published 7 Apr 2025) is paywalled at $199, so the number was not verified [15].
- **US fitness trainers and instructors**: 388,400 jobs in 2025. Median pay was $22.67/hour ($47,160/year) in May 2025. Projected growth is 7% for 2025–35 (BLS; page modified 27 Aug 2026) [13]. (High) This is a wage floor, not a consumer price.
- **Fitness-app user counts, and India gym members**: no primary source was verified (gap).

### 1.5 Personal-training prices (the comparison a "trainer in your pocket" makes)

| Market | Verified anchor | Conf. |
|---|---|---|
| US, remote human coaching | Future: about $199/month after a $50 first month; about $149/month prepaid annually (review dated Sep 2026) [51] | Low-Medium |
| US, in-person | Not verified. BLS wage only: $22.67/hour median [13] | — |
| UK | Not verified (cost-guide pages blocked) | — |
| India, metro gyms | ₹12,000–₹30,000/month. Cult.fit ₹15–25k (Delhi/Mumbai) and ~₹18k (Bengaluru); Gold's ₹18–30k; Anytime Fitness ₹12–20k (2026 marketplace blog) [16] | Low-Medium |

Implication: Premium+ at $29.99/month is about 15% of the price of remote human coaching. India Premium at ₹2,499/year (about ₹208/month) is under 2% of a metro trainer's monthly fee.

## 2. GLP-1 trend and the muscle-preservation segment

### 2.1 US usage

| Survey | Fieldwork | Current use | Ever used | Other findings | Conf. |
|---|---|---|---|---|---|
| KFF Health Tracking Poll, published 14 Nov 2025 [17] | 27 Oct–2 Nov 2025, n=1,350 | **12%**, any purpose (up from 6% in May 2024) | 18% | Women 15% vs men 9%. Ages 50–64: 22%; 65+: 9%. 56% of users found the drugs hard to afford. 27% of insured users paid full cost. 14% stopped because of cost, 13% because of side effects. Sources: own doctor 76%, online provider 17%, medical spa 9%. 22% of non-users are interested (7% "very"). | High |
| Gallup Well-Being Index, published 7 Jul 2026, re-weighted 8 Sep 2026 [18] | 28 May–5 Jun 2026, n=5,065 | **11%**, for weight loss (3% in 2024) | 15% | Awareness 90%. Of current users, 66% use brand-name drugs, 18% compounded, 13% unsure. Adult obesity 36.8% in 2026, down from a 39.9% peak in 2022. | High |

**Employer coverage.** In 2025, coverage of GLP-1s used mainly for weight loss was 16% at firms with 200–999 workers, 30% at 1,000–4,999 and 43% at 5,000+ (KFF Employer Health Benefits Survey, 22 Oct 2025) [21]. (High)

**Why exercise is the product hook.** Gallup (27 Aug 2026) found that GLP-1 users who exercise 30+ minutes on at least 5 days a week rate the drugs "extremely effective" about 11 points more often. Gallup says exercise helps preserve muscle mass, and notes this is an association, not proof of cause [19]. An HFA white paper (14 Jun 2026) models adding structured exercise to GLP-1 therapy. It estimates $120B of US value over 10 years, a 496% ROI, and a 164% 10-year ROI for the UK [20]. (Medium: this is industry-association modelling.)

### 2.2 India: semaglutide goes generic (2026)

| Item | Price and detail | Src | Conf. |
|---|---|---|---|
| Patent | Core semaglutide patents expired March 2026 (Reuters-reported date: 20 Mar) | [24][25] | Medium-High |
| Natco | ₹1,290/month | [23] | Medium |
| Dr. Reddy's "Obeda" (type 2 diabetes) | ₹4,200/month for 2 mg or 4 mg pens | [22][23] | Medium-High |
| Sun "Noveltreat" (chronic weight management, 0.25–2.4 mg) | ~₹900–₹2,000/week | [22] | Medium |
| Sun "Sematrinity" (type 2 diabetes) | ~₹750–₹1,300/week | [22] | Medium |
| Glenmark "GLIPIQ" (type 2 diabetes, vials) | ~₹325–₹440/week | [22] | Medium |
| Zydus | ~₹2,200/month on average | [22][23] | Medium |
| Novo Nordisk | Ozempic was ~₹2,200/week (~₹11,175/month). On 31 Mar 2026 Novo cut starting doses 36% (Ozempic) and 48% (Wegovy), and averages 24% and 27% across doses; the 0.25 mg dose is now ₹1,415/week | [22][24][25] | Medium-High |

Implication: Indian GLP-1 users now pay roughly ₹1,300–₹8,000/month for the drug. A ₹349–₹699/month companion app is a small add-on to that spend, which makes pharmacy, doctor and pharma partnerships plausible distribution channels.

### 2.3 Sizing the "GLP-1 user who needs muscle preservation" segment

Every multiplier below is an assumption except the usage rates.

| Step (US) | Low | Base | High | Basis |
|---|---|---|---|---|
| US adults | 260M | 260M | 260M | Assumption (the 2020 Census counted ~258M adults; not re-checked) |
| Currently on a GLP-1 | 11% = 28.6M | 11% = 28.6M | 12% = 31.2M | Gallup [18] / KFF [17] |
| Would follow an app-guided strength plan (SAM) | 20% = 5.7M | 30% = 8.6M | 40% = 12.5M | Assumption |
| Paid share of SAM by year 3 | 3% = 172k | 5% = 429k | 8% = 998k | Assumption |
| Blended ARPU (Premium/Premium+) | $80/year | $100/year | $120/year | §9 |
| **Annual revenue pool** | **~$14M** | **~$43M** | **~$120M** | Arithmetic |

**India.** No reliable count of users was found. As a sensitivity, for every 1M Indian GLP-1 users, 2% paying ₹2,499/year gives 20,000 payers and ₹5.0 crore (about $0.53M at ₹94/$) gross per year, before 18% GST and store fees.

## 3. Competitor pricing (checked Oct 2026)

"Camera form" means the product itself claims camera-based form or rep feedback.

| Product | US price | UK / India price | Camera form | AI coach | Src | Conf. |
|---|---|---|---|---|---|---|
| Fitbod | $15.99/month, $95.99/year (legacy $12.99/$79.99) | £14.99/£99.99; ₹399/₹1,999 | Not claimed | Algorithmic plans | [26][27][28] | High |
| Zing AI | In-app purchases $18.99, $29.99 (3 months), $39.99, $59.99; body scan $19.99. Press: ~$19.99/month, $59.99/year, 1-week trial | — | **Yes**, phone camera ("Zing Vision", real-time form) | Yes | [35][36] | High (store) / Medium |
| Peloton App | App One $15.99/month, App+ $28.99/month, All-Access $49.99/month (since 1 Oct 2025); 30-day trial | — | **Yes**, but only on Cross Training Bike+, Tread+ and Row+ hardware; Peloton IQ included with All-Access at no extra charge | Peloton IQ | [32][33][82] | High (IQ) / Medium (prices) |
| Apple Fitness+ | $9.99/month, $79.99/year; 1 month free | £9.99/£79.99; ₹149/₹999 | No | No | [29][30][31] | High |
| Freeletics | In-app purchases $34.99–$89.99 ("Training Coach", "Training and Nutrition Bundle"; durations not labelled) | — | No | "AI Coach" | [34] | High (store) |
| Future | ~$199/month for a human coach | — | No | Human | [51] | Low-Medium |
| Kemtai | Now a B2B digital physiotherapy and remote-monitoring platform; pricing on request | — | **Yes**, webcam/phone | — | [37] | High |
| Tempo | Membership ~$39/month; 3D form tracking needs Tempo hardware | — | **Yes**, hardware only | — | [40] | Low-Medium |
| Tonal | Membership $59.95/month with a 12-month commitment; Tonal 2 MSRP $4,295 | — | Sensors (not camera) | Yes | [39] | Medium |
| Whoop | One $199/year, Peak $239/year, Life $359/year (device included) | — | No | Yes | [41] | Medium |
| Oura | $5.99/month or $69.99/year (plus the ring); includes "Oura Advisor" AI; 1 month free | — | No | Yes | [42] | High |
| Google Health Premium (formerly Fitbit Premium) | $9.99/month; annual price reported raised from $79.99 to $99.99; Gemini coach leaving preview from 19 May 2026 | — | No | Yes (Gemini) | [43] | Medium |
| Noom | Weight: $70/month to $209/year. GLP-1Rx: from $149, then $299/month. Microdose: from $79, then $199/month (new pricing from 31 Mar 2026) | — | No | Coaching | [44] | High |
| MyFitnessPal | Premium $19.99/month, $79.99/year. Premium+ reported at $24.99/month, $99.99/year | India store lists Premium SKUs at ₹619–₹1,799/month and ₹3,099–₹7,200/year | No | Yes | [45][46][47] | High / Medium |
| Cal AI | In-app purchases $2.99–$29.99 (unlabelled). Acquired by MyFitnessPal (announced ~4 Mar 2026; stays a standalone app) | — | Photo calorie AI | — | [48][49] | High / Medium |
| Ladder | $29.99/month, or $179.99/year (works out to $14.99/month); 7-day trial with no payment details collected up front | — | No | Human-led programs | [50] | High |
| HealthifyMe (India) | — | Smart Plan in-app purchases ₹499–₹4,199; Healthify+ ₹499/₹1,899 | No | Yes | [52] | High (store) |
| cult.fit (India) | — | Cultpass LIVE ₹449/month, ₹999/quarter, ₹1,999/year; "cultpass HOME" covers unlimited digital at-home classes | No | — | [53][54] | High |
| FITTR (India) | — | Accountability groups ₹249; coach-led programs ₹7,599 (duration not stated); 700+ coaches | No | Human | [55] | High (store) |

**Takeaways for positioning and pricing**

1. **US price bands.** Commodity digital fitness costs about $10/month or $60–$100/year. AI strength coaches cost $15–$30/month or $60–$180/year. GLP-1 programs that include medication cost $199–$299/month, and human coaching about $199/month. Annual plans are usually discounted about 50% against 12 months of the monthly price (Fitbod, Ladder) or more (MyFitnessPal about 67%).
2. **Camera form feedback is table stakes in a niche, not a moat.** The opportunity is phone-only and multi-angle accuracy on barbell and dumbbell lifts, combined with GLP-1 phase-aware strength dosing and medication-aware nutrition (protein and fibre targets, side-effect logging). No reviewed competitor combines those.
3. **India ceiling.** Mass digital fitness sells for ₹149–₹449/month or ₹999–₹2,000/year. Coach-led products sell for ₹1,899–₹7,599 per package.

## 4. Subscription benchmarks (Health & Fitness)

Three sources are used. RevenueCat's *State of Subscription Apps 2026* covers 115k+ apps, $16B+ of revenue and 2025 data; its page assets are dated March 2026 [56]. RevenueCat's 2025 edition covers 2024 data [57]. Adapty's *State of In-App Subscriptions 2026* covers 16k+ apps and $3B of revenue; its Health & Fitness article is dated 27 Mar 2026 [58]. Abbreviations: RC = RevenueCat, H&F = Health & Fitness, UQ = upper quartile.

| Metric | RevenueCat 2026 (2025 data) | RevenueCat 2025 (2024 data) | Adapty 2026 | Conf. |
|---|---|---|---|---|
| Download→trial | H&F D30 median 6.9% (top performers >23%). All categories, by region: NA 7.1%, W. Europe 5.0%, IN/SEA and others 3.0–3.7% | — | H&F weekly-plan funnel 9.5%. All categories 11.2%; NA 14.5% | High |
| Trial→paid | H&F 37.7% (UQ >51.4%). All categories, by region: NA 34.2%, W. Europe 29.7%, IN/SEA 15.2%. By trial length: ≤4 days 25.5%, 5–9 days 37.4%, 17–32 days 42.5% | H&F 39.9% (top 10% at 68.3%) | H&F weekly 42.2% | High |
| Download→paid (D35) | H&F 2.9% (UQ >6.2%); H&F on iOS 3.5%. All categories, by region: NA 2.8%, IN/SEA 0.7%. Hard paywall 10.7% vs freemium 2.1% | Hard paywall 12.11% vs freemium 2.18% | Direct install→paid ~3.7% overall; onboarding paywall with trial 1.78% | High |
| When trials start | 82.1% of H&F trials start on Day 0; 54% of H&F trials last 5–9 days | — | H&F: 86.1% on Day 0, plus a 2.6% bump on Days 4–14 | High |
| Median prices, H&F | $4.99/week, $9.99/month, $39.94/year. Median yearly price across all apps rose from $31.60 to $34.80 | — | High-priced H&F annual plans earn $70 one-year LTV vs $17 for low-priced plans | High |
| Plan mix, H&F | Internally inconsistent: "68% annual adoption", "59% of revenue from annual", and also "monthly-heavy (68%)" | Yearly plans are 67% of H&F subscriptions | Annual share of H&F revenue rose from 51% (2023) to 61% (2025) | Medium |
| Refunds | Most categories 3–4% median. NA 3.4%, IN/SEA 7.7%. By price: low 2.7%, mid 3.9%, high 4.5% | H&F 4.71% (second-highest category) | — | High |
| Revenue per install | H&F D14 $0.48, D60 $0.66 (highest category). All categories D60: NA $0.55 vs IN/SEA $0.11 | H&F D14 $0.44, D60 $0.63 | Install LTV over 12 months: H&F $1.21 (highest category) | High |
| Revenue per payer | H&F month 1 $24.23 (UQ >$39); H&F year 1 $35.64. Yearly plans by user region: W. Europe $26.64, NA $26.07, IN/SEA $19.32. Year 1 by developer HQ: NA $32, W. Europe $25, IN/SEA $14 | H&F month 1 $16.44 (UQ $31.12) | — | High |
| Retention (all categories) | Year-1 retention: annual 28% (was 31%), monthly 8% (was 10%), weekly ~1.2%. First renewal: monthly 53–61%, annual 23–40%. First annual renewal by region: NA 26%, W. Europe 28%, IN/SEA 22%. First monthly renewal: NA 55%, IN/SEA 46%. Annual first renewal by price: low 37%, high 24%. H&F leads the yearly "active renewal rate" at 86.4% | — | Renewal survival: 1st 59.2%, 2nd 45.1%, 3rd 37.1% | High |
| Why people churn | Cost 25–45%; not using it enough 26–40%. Month 1 accounts for 35% of all annual-plan cancellations. Billing errors cause 32.2% of Google Play cancellations vs 15.2% on the App Store | — | — | High |
| AI apps | 41% more revenue per customer but churn 30% faster. Download→trial 8.5% vs 5.6%; download→paid 2.4% vs 2.0%. 59.8% of AI-app plans are monthly. AI apps are tightening free tiers, shortening trials and pushing annual plans to cover LLM costs | AI apps' D60 revenue per install ≥$0.63 | — | High |
| Market structure | Only 4.6% of new apps reach $10K MRR within 2 years. Web purchases are 3.2% of revenue globally, 4.9% in NA, 0.8% in IN/SEA | — | Top 10% of H&F apps take 92.6% of category revenue. 31% more apps launched in 2025; median monthly revenue per new app fell 22% | High |

**Design rules these numbers support**

1. Lead the paywall with the annual plan and use a free trial. Adapty finds trials raise annual-plan LTV in H&F [58].
2. Put the paywall inside onboarding, because 82–86% of trials start on Day 0. Plan a second prompt at Day 4–7 tied to the user's progress.
3. Be careful with hard paywalls. They convert about 5× better, with the same year-1 retention, but they kill virality [56]. A free tier with on-device form checks is the growth engine, so the paywall should be soft but placed early.
4. Size the product around the first renewal. Month-1 cancellations and the month-12 renewal cliff are where retention work should go [56].
5. The A/B tests most likely to win are localization (62.3% of tests improve LTV), trial structure (59.6%) and plan duration (58.7%). Visual-only changes win 34.6% of the time [58].

## 5. Acquisition benchmarks

### 5.1 Apple Ads (Adapty, published 10 Jun 2026; Jan–Dec 2025 data; 90 countries) [59]

| Market or niche | Cost per tap | Tap→download | Cost per download | Conf. |
|---|---|---|---|---|
| United States | $1.58 | 62.71% | $2.51 | High |
| Great Britain | $1.31 | — | $2.02 | High |
| All countries | — | — | Median $0.51; spend-weighted $1.34 | High |
| Health Tracker (niche) | $1.25 | 66.04% | $1.89 | High |
| Calorie & Weight Tracker | $1.72 | 64.11% | $2.69 | High |
| Health & Fitness (niche) | $1.64 | 54.21% | $3.02 | High |
| Fitness & Workouts | $1.60 | 49.95% | $3.20 | High |
| Yoga | $2.16 | 54.46% | $3.97 | High |

These are costs per **download**. Cost per install (first open) runs about 10% higher. Custom Product Pages raise tap-through by 12.1% and conversion by 9.6%, about 23% more downloads in total [59].

**Cost per paying subscriber.** Adapty's *Apple Ads for Subscription Apps 2026* report (published 7 Jul 2026; 8,000+ apps) finds the US delivers 15 paying subscribers per $1,000 of spend (about $67 each, all categories). The UK delivers 19 (about $53). US Health & Fitness has the highest Apple Ads install→paid rate at 7.80%. That implies about $32–$41 per H&F payer from Apple Ads alone ($2.51–$3.20 ÷ 7.8%). Apple Ads users start trials at 3.66% vs 1.45% from other paid channels. Matching the paywall to the search intent raised install→trial by 41.5% and trial→paid by 24.2% [60]. (Medium-High; this is press coverage of the primary report.)

### 5.2 India [61][62] (Low: vendor data)

- A vendor tool compiling "10+ industry sources (2025–26)" gives median Health & Fitness CPI in India of $0.20 (₹19) on Android and $0.60 (₹56) on iOS. It puts India's CPI at 0.12× the US and Android's share above 95%.
- The same vendor's own sample (48 Indian apps, May–Jul 2026, blended CPI including organic installs) has a median just under ₹20. Health & Fitness had too few apps to report a median.

### 5.3 Creators (Shopify, 22 Jun 2026; aggregated, not fitness-specific) [63]

| Tier (followers) | Instagram per post | TikTok per post | YouTube per video |
|---|---|---|---|
| Nano (1k–10k) | $25–$150 | $5–$200 | $200–$1,000 |
| Micro (10k–100k) | $250–$5,000 | $200–$1,200 | $1,000–$10,000 |
| Mid (100k–500k) | $1,600–$10,000 | $1,200–$5,000 | $9,000–$25,000 |
| Macro (500k–1M) | $5,000–$25,000 | $5,000–$15,000 | $10,000–$50,000 |
| Mega (1M+) | $10,000–$50,000+ | $7,000–$20,000+ | $20,000–$50,000+ |

Indian creator rates, the organic vs paid install split, and referral-program benchmarks could not be verified. They appear as assumptions in §10.

## 6. B2B channels and what buyers pay

| Buyer | Verified anchors | Conf. |
|---|---|---|
| Employers (US) | 83% of large firms (200+ workers) offer at least one wellness program, as do 56% of firms with 10–199. 63% of larger firms offer weight-loss programs (84% of 5,000+). 46% of larger firms with programs pay incentives (61% at 5,000+). GLP-1 weight-loss coverage: 16% / 30% / 43% by firm size (2025) [21] | High |
| Corporate wellness market | $55.1B globally (2025); India $664.5M [11][12] | High |
| Personal trainers and gyms | ABC Trainerize: Free (1 client); Grow $9/month (2 clients); Pro from $23/month (5 clients, scaling to 200); Studio Plus $248/month (500 clients). A branded app is an add-on, or Enterprise with its own store listing. A comparison table also shows $10/$79/$275 per month, so the billing basis is unclear [64] | Medium-High |
| Gyms (management plus white-label app) | Virtuagym and ABC Glofox are quote-only ("request demo and pricing") [65][66] | High (that pricing is unpublished) |
| Physio clinics | Physitrack: $18.99 per practitioner per month (under 20 practitioners); 2-week trial. Remote monitoring: $8 per active patient per month. US bundle of home-exercise programs, remote monitoring and courses: $30 per user per month [67][68] | High |
| Physio clinics (US, Medicare) | Remote therapeutic monitoring (RTM) code changes took effect 1 Jan 2026, adding codes for 2–15 days of data. A vendor example puts reimbursement at about $19–$55 per code per month and about $336 for a 3-month episode [38] | Low |
| Insurers | No verified incentive amounts (gap) | — |

Implication: the clearest per-patient price in the market is about $8/month for remote monitoring. That makes camera-verified home-exercise adherence a credible clinic product. Employer and insurer prices per member per month are not verified, so treat them as pilot hypotheses (§9).

## 7. Store fees, taxes and payments (inputs to margin)

- **Apple.** Small Business Program members (up to $1M proceeds in the prior year) pay 15% [69]. Otherwise auto-renewing subscriptions net 70% in a subscriber's first paid year and 85% afterwards, "minus applicable taxes" [70]. US-storefront apps may include buttons and external links to web purchase without an entitlement (guideline 3.1.1(a)). Real-time one-to-one services, including fitness training, may use non-App-Store payment; one-to-few and one-to-many must use in-app purchase (3.1.3(d)) [71]. (High)
- **Google Play.** Subscriptions pay 15%. In the US, UK and EEA from 30 Jun 2026, auto-renewing subscriptions pay a 10% service fee plus a 5% billing fee when Play Billing is used. In India and Korea, alternative billing reduces the fee by 4 points [72]. (High)
- **Web checkout.** Stripe Billing costs 0.7% of billing volume, plus card fees: 2% for domestic Indian cards and 3% for international cards, as shown to an India-based visitor. Razorpay costs 2% + GST [73][74]. The US card rate was not verified; the model assumes about 3%.
- **Taxes.** UK VAT is 20% [75], and UK store prices include it: £79.99 is £66.66 before VAT. Indian prices are modelled as including 18% GST (assumption, not re-verified).

## 8. AI inference cost (Claude), using the prices in the task

**Prices** (all per 1M tokens; matched against the official pricing page on 16 Oct 2026 [76]):

| Model | Input | Output | Cache hit | Cache write (5 min / 1 h) |
|---|---|---|---|---|
| Opus 5.5 | $4 | $20 | $0.20 | $5 / $8 |
| Sonnet 5.5 | $2 | $10 | $0.20 in the task; **$0.10 on the official page** | $2.50 / $4 |
| Haiku 5.5 (prompts ≤100K tokens) | $0.10 | $0.50 | $0.01 | — |

Other pricing rules from the official page:

- Haiku 5.5 prompts over 100K tokens cost $0.50 input and $2.50 output.
- The Batch API is 50% off.
- Pinning inference to the US (`inference_geo`) multiplies all prices by 1.1 [76].
- Opus 5.5 thinking cannot be switched off. Its default effort is "medium", so thinking tokens are billed as output [77].

**Usage model per active premium user-month.** These are assumptions to replace with eval telemetry. Pose estimation runs on the phone, so there is no per-frame server cost, and the server receives only derived joint-angle metrics, not video.

| Task | Calls/month | Tokens per call | Opus cost per call | Opus cost per month |
|---|---|---|---|---|
| Coach chat turn | 30 | 1K new input + 5K cache hit; 0.8K output (thinking included) | $0.021 | $0.63 |
| Conversation cache writes | 10 | 5K | $0.025 | $0.25 |
| Post-workout form summary (from on-device metrics) | 12 | 3K in; 0.6K out | $0.024 | $0.29 |
| Weekly plan regeneration | 4 | 8K in; 2.5K out | $0.082 | $0.33 |
| Meal-photo analysis | 45 | 2.6K in (image included); 0.3K out | $0.016 | $0.74 |
| **Total** | | | | **Opus $2.23 · Sonnet $1.13 · Haiku $0.06** |

**AI cost as a share of net revenue** (after 4% refunds and a 15% store fee):

- An annual Premium payer at $89.99 nets $73.43 in year 1. Assuming they are active in 60% of months, AI costs $16.08 on Opus (22% of net), $8.15 on Sonnet (11%) or $0.41 on Haiku (1%).
- A monthly payer at $14.99 nets $12.74. AI costs 18% of that on Opus, 9% on Sonnet and under 1% on Haiku.
- Weekly plans and summaries can run through the Batch API, which halves their cost.

**Free tier is the risk.** At $0.35 of lifetime Opus usage per install and 3% install→paid, free users cost $11.67 per acquired payer. That is about 20% of the base CAC.

## 9. Pricing recommendation (draft for the BRD)

| Tier | US | UK (incl. VAT) | India (incl. GST) | Contents |
|---|---|---|---|---|
| Free | $0 | £0 | ₹0 | On-device rep counting and form cues for 5 foundational movements; 1 starter program; manual food log. A small AI quota capped at ≤$0.10 lifetime Opus cost per install (about 3 coach turns and 2 meal scans a month), widened only if evals approve a cheaper model for the free tier |
| Premium | **$14.99/month · $89.99/year** | £12.99 · £79.99 | ₹349 · ₹2,499 | Full free-weight form-correction library, adaptive programming, AI coach (~30 turns/month fair use), meal-photo logging (~45/month), wearable sync |
| Premium+ "GLP-1 Strength" | **$29.99/month · $179.99/year** | £24.99 · £149.99 | ₹699 · ₹4,999 | Premium, plus a GLP-1 phase-aware muscle-preservation program, protein and fibre targets, a dose-schedule and side-effect log (non-prescriptive), a clinician-shareable report, and 1.8× AI quota |

Pricing rules:

- **Trial:** 7-day free trial on annual plans only. A/B test 7 vs 14 days; longer trials convert better (42.5% at 17–32 days) but cost more AI per trial user [56].
- **Annual discount:** 50% off 12 months of the monthly price.
- **Price testing:** test $119.99/year, which raises LTV/CAC from 1.08 to 1.63 in the model.
- **Price anchors:**
  - US: Fitbod $95.99, Ladder $179.99, Zing $59.99 per year.
  - UK: Fitbod £99.99, Apple Fitness+ £79.99 per year.
  - India: Fitbod ₹1,999, cult.fit ₹1,999, HealthifyMe up to ₹4,199 per year; generic GLP-1s cost ₹1,290+/month.
- **Live 1:1 coaching:** a later human-coach add-on may bill outside the App Store under guideline 3.1.3(d) [71].

**B2B pilot hypotheses** (to validate, not verified):

- **Physio clinics:** $29 per practitioner per month plus $8 per active patient per month for camera-verified adherence data that supports remote-monitoring billing (anchor: Physitrack [67][68]).
- **Trainers and gyms:** from $19/month per coach (10 clients), and white-label at $299+ per location per month (anchor: Trainerize $248 plus the branded-app add-on [64]).
- **Employers and insurers:** price per employee or per enrolled member per month. No verified benchmark exists, so pilot with outcome-linked fees.

## 10. Funnel and unit economics (36-month horizon, per acquired payer)

The model is `unit_econ.py`, kept in the session scratchpad and not shipped. It includes self-checks.

### 10.1 Assumptions (US, Premium/Premium+ blend)

| Input | Pessimistic | Base | Optimistic | Anchor |
|---|---|---|---|---|
| Install→paid (all channels) | 1.8% | 3.0% | 6.0% | H&F median 2.9%, UQ 6.2% [56] |
| Share of installs that are paid | 75% | 60% | 40% | Assumption |
| Paid CPI | $4.50 | $3.00 | $2.50 | Apple Ads H&F $1.89–$3.97 [59] |
| Annual-plan share of payers | 50% | 65% | 72% | [56][58] |
| Monthly renewals (1st / 2nd / 3rd / then each month) | 45/65/75/82% | 55/70/78/85% | 60/75/82/88% | [56] |
| Annual renewals (1st / 2nd) | 25/45% | 33/55% | 45/65% | [56] |
| Refunds | 6% | 4% | 3% | [56][57] |
| Store fee in year 1 / later | 27% / 15% | 15% / 15% | 10% / 10% | [69][70][72] |
| AI cost per active month on Opus (annual payers active ×) | $4.47 (×0.75) | $2.23 (×0.6) | $1.34 (×0.5) | §8 |
| Premium+ share of payers (2× price, 1.8× AI) | 5% | 10% | 15% | Assumption |
| Free/trial AI per install | $0.80 | $0.35 | $0.15 | Assumption |
| Infrastructure per paying month | $0.35 | $0.20 | $0.12 | Assumption |

### 10.2 Results (US; contribution = net revenue − AI − infrastructure − free-user serving cost)

| Scenario | CAC | Free-user serving cost per payer | Net revenue 12 / 36 months | Contribution 12 / 36 months | LTV36/CAC | Payback month |
|---|---|---|---|---|---|---|
| Pessimistic | $187.50 | $44.44 | $47.91 / $63.83 | −$26.43 / −$19.36 | <0 | Never |
| **Base** | **$60.00** | **$11.67** | **$69.35 / $99.55** | **$41.65 / $64.87** | **1.08** | **25** |
| Optimistic | $16.67 | $2.50 | $82.95 / $136.78 | $71.05 / $118.86 | 7.13 | 1 (annual upfront) |

**What moves the base case** (one change at a time, LTV36/CAC):

| Change | LTV36/CAC |
|---|---|
| Free-tier AI capped at $0.10 per install | 1.22 |
| Free tier on Haiku | 1.26 |
| All Sonnet | 1.34 |
| 60% organic installs | 1.62 |
| $119.99/year and $19.99/month | 1.63 |
| Top-quartile conversion (6.2%) | 2.44 |
| $59.99/year and $9.99/month | 0.53 |
| Apple's standard 30% first-year fee | 0.88 |
| Blended 9% fees through web checkout | 1.20 |

### 10.3 India (₹2,499/year, ₹349/month; 18% GST; 15% Play fee; ₹94/$)

Assumptions: AI quota at 40% of US usage; install→paid 1.2%; CPI $0.30; 50% organic; annual first renewal 22%; refunds 7.7%.

| Scenario | CAC | Net revenue 36 months | Contribution 36 months | LTV36/CAC |
|---|---|---|---|---|
| Base, Opus | $12.50 | $18.79 | $4.71 | 0.38 |
| Base, Haiku (if evals pass) | $12.50 | $18.79 | $16.94 | 1.36 (payback month 4) |
| Pessimistic, Opus (0.6% conversion, $0.50 CPI) | $41.67 | $18.79 | −$13.62 | <0 |
| Optimistic, Opus (2.0% conversion, $0.20 CPI) | $5.00 | $18.79 | $8.88 | 1.78 |

**UK net per annual plan:** £79.99 is £66.66 before VAT and £56.66 after a 15% store fee. The UK behaves like the US once VAT is accounted for.

## Recommendations for the docs

**BRD**

- Position the product as "the strength coach for the GLP-1 era: phone-camera form checks that protect your muscle while the medication takes the weight off". Do not claim to be the first app with camera form correction (§3).
- Primary market is the US, launching on iOS first. UK follows with VAT-inclusive prices. India comes third, with a free-heavy model, B2B clinic and pharmacy partnerships, and lower AI quotas.
- Launch KPIs:
  - D30 download→trial ≥9% (US) and trial→paid ≥38%.
  - D35 download→paid ≥3%.
  - Refunds ≤4% in the US and ≤8% in India.
  - First annual renewal ≥33%.
  - AI cost ≤15% of net revenue.
  - Free-tier AI ≤$0.10 per install.
  - LTV36/CAC ≥1.5 before scaling paid acquisition.
- Adopt the §9 price table. Treat $119.99/year as a launch price test.

**Tech Spec**

- Pose estimation runs on the device. Upload derived metrics only, not video, by default; this keeps server cost flat and limits privacy exposure.
- Put every LLM call behind a model-routing layer with per-tier and per-user token budgets. Opus 5.5 is the default. Switching any route to Sonnet 5.5 or Haiku 5.5 is an owner decision, gated by evals.
- Cost controls: prompt caching of the system prompt and user profile, the Batch API (50% off) for weekly plans and summaries, and a per-request cost log that feeds a dashboard.
- Entitlements must cover the App Store, Google Play (including the US/UK/EEA fee change from 30 Jun 2026), US web checkout under guideline 3.1.1(a), and India web checkout via Razorpay. Handle Google Play billing retries, since billing errors cause 32% of Play cancellations.
- Paywall configuration must be remote and support per-storefront localized prices, trial lengths and plan sets. These are the A/B tests most likely to win [58].

**Roadmap and strategy**

- **Phase 1 (US iOS):** Free + Premium, with Premium+ GLP-1 at launch or soon after.
- **Phase 2:** Android and UK, Custom Product Pages per search intent, and the creator program (nano and micro tiers).
- **Phase 3:** India pricing and a clinic B2B pilot priced against Physitrack's $8 per patient.

**Innovative Features**

- GLP-1 phase-aware "minimum effective strength dose", with camera-verified sets.
- Protein and fibre targets that adapt to appetite suppression.
- A clinician-shareable adherence report that can also serve as a remote-monitoring data feed for clinics.
- Paywall copy matched to search intent, a measured +41.5% lift in install→trial [60].

**Build Playbook**

- Wire up funnel analytics (trial start, Day 4–7 conversions, first renewal) and AI cost per user before launch.
- Ship the unit-economics model with real telemetry, and re-run §10 monthly.

## Unverified / conflicting

- **Market size.** 2026 estimates range from $13.8B to $28.7B. The Business Research Co., Wellness Creatives and Allied ($120B by 2030) figures come from listings or snippets and were not read in full [3][4][5]. GVR's connected-gym FAQ says "USD 14.0 million by 2033", which conflicts with $14.0 billion on the same page [9].
- **Not found or paywalled:**
  - US and India gym-member totals (the HFA 2025 report is $199).
  - Personal-training penetration.
  - UK and US in-person PT session prices.
  - Fitness-app user counts.
  - Sensor Tower, AppsFlyer and Liftoff 2026 fitness benchmarks.
  - App-usage D30 retention.
  - Organic vs paid install share.
  - Referral benchmarks.
  - Indian creator rates.
  - Insurer incentive amounts.
  - Employer price per employee per month.
- **Gallup.** Press coverage reported 68% brand / 19% compounded / 12% unsure and 91% awareness. Gallup's 8 Sep 2026 re-weighting shows 66/18/13 and 90% [18][79]. Coverage also cited an 8% figure for 2025 that is not on Gallup's page.
- **Federal pricing deal.** KFF says its poll was fielded before a Nov 2025 presidential announcement on GLP-1 cost and coverage [17]. The deal's terms (Medicare coverage, TrumpRx cash prices) and the US launch price of oral Wegovy were not verified.
- **Lean mass.** The share of GLP-1 weight loss that comes from lean mass (often cited as roughly 25–40% in trials) was not verified here; check it in the clinical brief.
- **India.** The ~101M people with diabetes figure (ICMR-INDIAB 2023) could not be re-fetched. Sun's weekly generic prices are reported, not taken from company lists [22]. Reuters is the source for the 20 Mar patent-expiry date; Business Today gives only "March 2026" [24][25].
- **RevenueCat plan mix.** The 2026 report says Health & Fitness is both "68% annual" and "monthly-heavy (68%)", and gives 59% vs 68% annual revenue share in different places [56]. Adapty's 61% annual share is consistent with "annual-led" [58].
- **Retention definitions differ.** Adapty's "Utilities lead at 22.1% one-year annual retention" [58] conflicts with RevenueCat's 20–40% annual year-1 medians [56].
- **Secondary-only prices (Medium or Low):**
  - Peloton tier prices [33], whose original article now returns 404.
  - Whoop [41], Google Health Premium [43], Tempo [40] and Future [51].
  - MyFitnessPal Premium+ [47] and the Cal AI acquisition [49].
  - Zing monthly/annual mapping [36], and HealthifyMe plan names and durations [80].
  - Fitbod's price-rise timing [81].
- **SplitMetrics Apple Ads, US Health & Fitness, Apr–Jun 2026.** A search snippet gave tap-through 9.4%, conversion 62.7%, cost per tap $1.50 and cost per download $2.38. The page was not opened [78].
- **Remote-monitoring payments.** The amounts are vendor estimates using placeholder code names, not the CMS fee schedule [38].
- **Claude pricing.** The task gives Sonnet 5.5 cache reads at $0.20; the official page shows $0.10 [76]. The impact on the model is negligible.
- **FX and tax.** ₹94/$ (the vendor's rate) and 18% Indian GST are assumptions. The US card-processing rate is not verified.

## Sources

1. Grand View Research — Fitness Apps Market Report 2026–2033: https://www.grandviewresearch.com/industry-analysis/fitness-app-market
2. Towards Healthcare — Fitness App Market (updated 21 Aug 2026): https://www.towardshealthcare.com/insights/fitness-app-market-sizing
3. GII listing — The Business Research Company, Fitness App Global Market Report: https://cn.gii.tw/report/tbrc1973524-fitness-app-global-market-report.html
4. Wellness Creatives — Fitness App Market: https://www.wellnesscreatives.com/fitness-app-market/
5. Allied Market Research — Fitness App Market press release: https://www.alliedmarketresearch.com/press-release/fitness-app-market.html
6. Grand View Research Horizon — US Fitness App Market: https://www.grandviewresearch.com/horizon/outlook/fitness-app-market/united-states
7. Grand View Research Horizon — UK Fitness App Market: https://www.grandviewresearch.com/horizon/outlook/fitness-app-market/uk
8. Grand View Research Horizon — India Fitness App Market: https://www.grandviewresearch.com/horizon/outlook/fitness-app-market/india
9. Grand View Research — Connected Gym Equipment Market: https://www.grandviewresearch.com/industry-analysis/connected-gym-equipment-market
10. Grand View Research — GLP-1 Receptor Agonist Market: https://www.grandviewresearch.com/industry-analysis/glp-1-receptor-agonist-market
11. Grand View Research — Corporate Wellness Market: https://www.grandviewresearch.com/industry-analysis/corporate-wellness-market
12. Grand View Research Horizon — India Corporate Wellness Market: https://www.grandviewresearch.com/horizon/outlook/corporate-wellness-market/india
13. US BLS — Occupational Outlook Handbook: Fitness Trainers and Instructors (modified 27 Aug 2026): https://www.bls.gov/ooh/personal-care-and-service/fitness-trainers-and-instructors.htm
14. Health & Fitness Association — homepage (US facilities): https://www.healthandfitness.org/
15. HFA — 2025 U.S. Health & Fitness Consumer Report (7 Apr 2025): https://www.healthandfitness.org/2025-us-health-fitness-consumer-report/
16. magicpin — Personal Trainer Cost in India 2026: https://magicpin.com/blog/india/mumbai/fitness/personal-trainer-fees-savings
17. KFF — Poll: 1 in 8 adults currently taking a GLP-1 (14 Nov 2025): https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/
18. Gallup — In U.S., GLP-1 Usage Reaches New High (7 Jul 2026; updated 8 Sep 2026): https://news.gallup.com/poll/712157/glp-usage-reaches-new-high.aspx
19. Gallup — Five Aspects of Wellbeing Linked to GLP-1 Effectiveness (27 Aug 2026): https://news.gallup.com/poll/713360/five-aspects-wellbeing-linked-glp-effectiveness.aspx
20. HFA — From Weight Loss to Lasting Value: Structured Exercise and the Economics of GLP-1 Therapy (14 Jun 2026): https://www.healthandfitness.org/from-weight-loss-to-lasting-value-structured-exercise-and-the-economics-of-glp-1-therapy/
21. KFF — 2025 Employer Health Benefits Survey (22 Oct 2025): https://www.kff.org/health-costs/report/2025-employer-health-benefits-survey/
22. Outlook Business (PTI) — Sun Pharma, Dr Reddy's, Glenmark launch generic semaglutide (21 Mar 2026): https://www.outlookbusiness.com/corporate/sun-pharma-dr-reddys-glenmark-launch-generic-semaglutide-injection-in-india
23. Medical Dialogues — Indian pharma firms launch generic semaglutide (23 Mar 2026): https://health.medicaldialogues.in/latest-news/indian-pharma-firms-launch-generic-semaglutide-for-diabetes-treatment-167054
24. Business Today — Novo further cuts semaglutide prices as generics enter India (31 Mar 2026): https://www.businesstoday.in/amp/industry/pharma/story/novo-further-cuts-semaglutide-prices-as-generics-enter-india-523336-2026-03-31/
25. Outlook Business — Novo Nordisk cuts Ozempic, Wegovy prices by up to 48%: https://www.outlookbusiness.com/corporate/novo-nordisk-cuts-ozempic-wegovy-prices-by-up-to-48-amid-generic-pressure
26. App Store (US) — Fitbod: https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543
27. App Store (UK) — Fitbod: https://apps.apple.com/gb/app/fitbod-gym-fitness-planner/id1041517543
28. App Store (India) — Fitbod: https://apps.apple.com/in/app/fitbod-gym-fitness-planner/id1041517543
29. Apple — Apple Fitness+ (US): https://www.apple.com/apple-fitness-plus/
30. Apple — Apple Fitness+ (UK): https://www.apple.com/uk/apple-fitness-plus/
31. Apple — Apple Fitness+ (India): https://www.apple.com/in/apple-fitness-plus/
32. Peloton — Peloton IQ: https://www.onepeloton.com/peloton-iq
33. AOL — Peloton raises prices, unveils new equipment (Oct 2025; link now 404): https://www.aol.com/news/peloton-raises-prices-unveils-equipment-151628090.html
34. App Store (US) — Freeletics: https://apps.apple.com/us/app/freeletics-workouts-fitness/id654810212
35. App Store (US) — Zing AI: Home & Gym Workouts: https://apps.apple.com/us/app/zing-ai-home-gym-workouts/id1552207792
36. TechRadar — Zing Coach review: https://www.techradar.com/health-fitness/zing-coach-is-an-app-that-reveals-the-true-power-of-ai-training
37. Kemtai — Digital Physical Therapy Platform: https://kemtai.com/
38. Kemtai — 2026 RTM Changes: What You Need to Know: https://kemtai.com/blog/2026-rtm-changes-what-you-need-to-know
39. Tonal — Tonal 2 trainer: https://tonal.com/products/tonal-2-trainer
40. Tempo — Move Pro with membership: https://shop.tempo.fit/products/tempo-move-pro-with-membership
41. TrackerVS — WHOOP Pricing 2026: https://trackervs.com/pricing/whoop-pricing/
42. Oura — Membership: https://ouraring.com/membership
43. Android Authority — Google Health Premium price and features: https://androidauthority.com/google-health-premium-price-inclusions-features-3664507/
44. Noom — How much does Noom Weight cost in 2026 (updated 3 Jun 2026): https://www.noom.com/blog/how-much-does-noom-cost
45. App Store (US) — MyFitnessPal: https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718
46. App Store (India) — MyFitnessPal: https://apps.apple.com/in/app/myfitnesspal-calorie-counter/id341232718
47. Garage Gym Reviews — MyFitnessPal review (Premium+ pricing): https://www.garagegymreviews.com/myfitnesspal-review
48. App Store (US) — Cal AI: https://apps.apple.com/us/app/cal-ai-calorie-tracker/id6480417616
49. Pulse 2 — MyFitnessPal acquires Cal AI: https://pulse2.com/myfitnesspal-acquires-cal-ai-to-expand-ai-powered-nutrition-tracking-portfolio
50. Ladder — Pricing: https://joinladder.com/pricing
51. SensAI — Future App Review 2026: https://www.sensai.fit/blog/future-app-review-2026
52. App Store (India) — Healthify: AI Calorie Tracker: https://apps.apple.com/in/app/id943712366
53. App Store (India) — cult.fit: https://apps.apple.com/in/app/id1217794588
54. cult.fit support — services accessible to a cultpass HOME member: https://support.cure.fit/support/solutions/articles/25000023151-what-are-the-services-accessible-to-a-cultpass-home-member-
55. App Store (India) — FITTR: https://apps.apple.com/in/app/fittr-health-fitness-app/id1332568703
56. RevenueCat — State of Subscription Apps 2026: https://www.revenuecat.com/state-of-subscription-apps
57. RevenueCat — State of Subscription Apps 2025: https://www.revenuecat.com/state-of-subscription-apps-2025
58. Adapty — In-app subscription benchmarks for Health & Fitness apps (27 Mar 2026): https://adapty.io/blog/health-fitness-app-subscription-benchmarks/
59. Adapty — Apple Ads benchmarks 2026 (10 Jun 2026): https://adapty.io/blog/apple-ads-benchmarks-2026/
60. PPC Land — Apple Ads gives Brazil 76 paid subscribers per $1,000, US gets 15 (Adapty report, Jul 2026): https://ppc.land/apple-ads-gives-brazil-76-paid-subscribers-per-1-000-us-gets-15/
61. Linkrunner — CPI Benchmark Explorer: https://linkrunner.io/cost-per-install-benchmark
62. Linkrunner — India app CPI benchmarks by category (2026): https://deeplinks.linkrunner.io/blog/india-app-cpi-benchmarks-by-category
63. Shopify — Influencer Pricing: The Cost of Influencers in 2026 (22 Jun 2026): https://www.shopify.com/blog/influencer-pricing
64. ABC Trainerize — Pricing: https://www.trainerize.com/pricing/
65. Virtuagym — Prices: https://business.virtuagym.com/our-prices
66. ABC Glofox — Get a price quote: https://www.glofox.com/pricing/
67. Physitrack — Pricing: https://www.physitrack.com/physitrack-pricing
68. Physitrack — homepage (RTM pricing): https://www.physitrack.com/
69. Apple — App Store Small Business Program: https://developer.apple.com/app-store/small-business-program/
70. Apple — Auto-renewable subscriptions: https://developer.apple.com/app-store/subscriptions/
71. Apple — App Review Guidelines (3.1.1(a), 3.1.3(d)): https://developer.apple.com/app-store/review/guidelines/
72. Google Play Console Help — Service fees: https://support.google.com/googleplay/android-developer/answer/112622?hl=en
73. Stripe — Pricing: https://stripe.com/pricing
74. Razorpay — Pricing: https://razorpay.com/pricing/
75. GOV.UK — VAT rates: https://www.gov.uk/vat-rates
76. Anthropic — Claude pricing: https://platform.claude.com/docs/en/about-claude/pricing
77. Anthropic — Models overview (Opus 5.5 thinking and effort behaviour per the bundled Claude API reference, cached 6 Oct 2026): https://platform.claude.com/docs/en/about-claude/models/overview
78. SplitMetrics — Apple Ads blog: https://www.splitmetrics.com/blog/apple-search-ads
79. Gizmodo — 11% of Americans are currently taking a GLP-1: https://gizmodo.com/11-of-americans-are-currently-taking-a-glp-1-weight-loss-drug-like-wegovy-2000782666
80. NutriScan — HealthifyMe pricing 2026 (conflicting plan structure): https://nutriscan.app/blog/posts/healthifyme-pricing-2026-india-plans-63a87b21d0
81. SensAI — Fitbod review 2026 (price-rise timing): https://www.sensai.fit/blog/fitbod-review-2026
82. Peloton — Peloton App (30-day trial): https://www.onepeloton.com/app

# R2 — Real-time on-device exercise form correction: pose models, methods, datasets and the mobile stack (as of 17 Oct 2026)

> Input brief for the spec pack (BRD, Technical Specification, Roadmap & Strategy, Innovative Features, Build Playbook). Registry and version checks (npm, PyPI, Google Maven, CocoaPods CDN, GitHub, python.org, postgresql.org) were taken on **16 Oct 2026 (IST)** unless stated otherwise. Inline links are numbered and resolve in **Sources**.
> Confidence: **High** = primary source read directly; **Medium** = vendor claim on old hardware, secondary summary or abstract only; **Low** = inference or partial evidence. Speed figures are vendor-published unless marked independent.

## Summary

- **Primary pose engine: MediaPipe Pose Landmarker (BlazePose GHUM Lite/Full/Heavy).** It outputs 33 landmarks as image and world coordinates, with an optional segmentation mask [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker). The model card is Apache-2.0, lists "Fitness and repetition counting" as an intended use, and states the training images include 30K consented images and 85K fitness poses [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). That makes it the cleanest legal basis of any option. **High**
- **Speed evidence is old and vendor-only.** Pixel 3 TFLite GPU: Lite 20 ms, Full 25 ms, Heavy 53 ms [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md). On Pixel 3 CPU, Heavy runs at about 4 FPS [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). No independent 2024–2026 mid-range benchmark was found, so a device-lab benchmark is a gating task. Ship **Full** as the default, fall back to **Lite**, and use Heavy only offline. **Medium**
- **Distribution is a pitfall.** On Android, `com.google.mediapipe:tasks-vision` is at 1.1.1 (14 Oct 2026), with minSdk 24 [7](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/maven-metadata.xml) [9](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.aar). On iOS, CocoaPods only has `MediaPipeTasksVision` 1.0.0 [11](https://cdn.cocoapods.org/all_pods_versions_9_9_0.txt), while Google documents Swift Package Manager [12](https://developers.google.com/edge/mediapipe/solutions/setup_ios). CocoaPods trunk stops accepting new podspecs on **2 Dec 2026** [13](https://blog.cocoapods.org/CocoaPods-Specs-Repo/). **High**
- **Fallbacks and exclusions.** Apple Vision is a free iOS-only fallback: 2D since iOS 14, and 3D with body height since iOS 17 [18](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest) [21](https://developer.apple.com/documentation/vision/humanbodypose3dobservation). ML Kit Pose is still **beta** with no Maven release since Aug 2024 [14](https://developers.google.com/ml-kit/vision/pose-detection) [15](https://dl.google.com/android/maven2/com/google/mlkit/pose-detection/maven-metadata.xml). Ultralytics YOLO is AGPL-3.0, so a closed-source app needs an Enterprise License, including for custom-trained models [29](https://www.ultralytics.com/license). Sapiens is CC BY-NC [33](https://github.com/facebookresearch/sapiens). The Sapiens2 license bars "biometric processing" [34](https://github.com/facebookresearch/sapiens2). **High**
- **Viable secondary models.** RTMPose has Apache-2.0 code, and RTMPose-s runs in 13.89 ms on a Snapdragon 865 at 72.2 COCO AP [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose). MoveNet is Apache-2 according to NGC [25](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ace/containers/vision-ai-movenet). RF-DETR Keypoint is Apache-2.0 but still a preview benchmarked on a T4 GPU [30](https://rfdetr.roboflow.com/latest/learn/run/keypoints/). **Medium**
- **Single-camera physics limits what can be promised.** BlazePose depth (z) is "not metric but up to scale" [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). MediaPipe underestimated knee flexion by −13.9 ± 15.1° against an IMU, and lateral views were much better [60](https://iris.uniecampus.it/handle/11389/91575). Even the best in-the-wild "knees-inward" detector reached only F1 0.53 [40](https://arxiv.org/abs/2202.14019). **Medium**
- **MVP method: deterministic per-exercise state machines.** Use hysteresis rep counting as Google describes [4](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose_classification.md), plus view-specific rules, One Euro smoothing [66](https://gery.casiez.net/1euro/) and visibility/presence gating [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). Add learned temporal models later. For reference, PoseRAC reaches OBO 0.56 against 0.29 for TransRAC [51](https://github.com/MiracleDance/PoseRAC). **Medium**
- **Do not use VLMs for real-time cues.** On QEVD, zero-shot VLMs scored only 1.29–2.27 out of 5 on LLM-accuracy, and the fine-tuned streaming baseline reached 2.45 [44](https://arxiv.org/abs/2407.08101). An LLM should only narrate structured metrics after a set. **High**
- **Almost no public form or rep dataset allows commercial training.** Fitness-AQA, Fit3D, QEVD, EgoExo-Fitness and MyoMechanix are all research-only [39](https://github.com/ParitoshParmar/Fitness-AQA) [41](https://fit3d.imar.ro/legal) [45](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Dataset-Research-License-Feb-25-2025.pdf) [56](https://github.com/iSEE-Laboratory/EgoExo-Fitness) [57](https://github.com/HaoYin116/FLEX). RepCount and Countix are YouTube-sourced and carry no license [49](https://svip-lab.github.io/dataset/RepCount_dataset.html) [53](https://storage.googleapis.com/deepmind-media/Datasets/countix.tar.gz). The MM-Fit video record (CC BY 4.0) is the notable exception [48](https://zenodo.org/records/7672767). That puts **proprietary consented data on the critical path.** **High**
- **Mobile stack (as of 16 Oct 2026):** React Native 0.88.0, Expo SDK 58 (58.0.12; React 19.3.0, Reanimated 4.7.1, Worklets 0.13.0, Skia 2.14.0) [69](https://www.npmjs.com/package/react-native) [72](https://www.npmjs.com/package/expo). Add VisionCamera 5.2.3 with `react-native-vision-camera-worklets` 5.2.3 and Nitro Modules 0.37.1 [76](https://www.npmjs.com/package/react-native-vision-camera) [79](https://www.npmjs.com/package/react-native-vision-camera-worklets). Pin TypeScript ~6.0.3, the version the SDK 58 template uses [75](https://www.npmjs.com/package/expo-template-default). TypeScript 7.0.2 ships without a programmatic API [96](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/). **High**
- **New Architecture pitfalls.** RN ≥0.82 runs only on the New Architecture, and the remaining legacy code was removed in 0.84 [70](https://reactnative.dev/blog/2025/10/08/react-native-0.82) [71](https://reactnative.dev/blog). VisionCamera v5 frame processors need Software Mansion's `react-native-worklets`, not `worklets-core` [78](https://visioncamera.margelo.com/docs/guides/frame-processors). The fast-tflite integration for VisionCamera v5 is private and sponsor-gated [85](https://github.com/mrousavy/react-native-fast-tflite), and community MediaPipe RN plugins are v4-era or stale [87](https://www.npmjs.com/package/react-native-mediapipe). So **write our own Swift/Kotlin Nitro module.** **High**
- **Backend versions:** Python 3.14.8 (3.15.0 is only from 9 Oct 2026) [98](https://www.python.org/downloads/), FastAPI 0.143.3, Pydantic 2.14.1, SQLAlchemy 2.1.4, Alembic 1.20.0, PostgreSQL 18.6 + pgvector 0.8.7, Celery 5.6.3 and anthropic 1.15.0. Avoid arq, which is in maintenance-only mode [106](https://github.com/python-arq/arq). **High**
- **Framework recommendation: React Native (Expo dev builds) for the app, with a native Swift/Kotlin CV module.** Flutter has no maintained MediaPipe Tasks plugin on pub.dev, and its ML Kit wrapper sits on a stalled beta API [92](https://pub.dev/packages/google_mlkit_pose_detection) [95](https://pub.dev/packages/mediapipe_core). Fully native doubles the UI work. **Medium**
- **Proposed acceptance targets** (to validate in a spike, not measured): ≥30 FPS on Tier A, ≥20 FPS on Tier B and a 15 FPS floor; ≥95% of sets counted exactly under guided setup; per-cue precision ≥0.90 before any form cue ships. **Low (proposal)**

## 1. Pose-estimation models for a closed-source commercial app

### 1.1 Shortlist

| Model | Output | Runtime / platforms | Published speed (device, source year) | Published accuracy | License and commercial use | Verdict |
|---|---|---|---|---|---|---|
| **MediaPipe Pose Landmarker** (BlazePose GHUM Lite/Full/Heavy) | 33 landmarks (x, y, z, visibility, presence); world landmarks; optional mask. Detector input 224², landmarker 256², float16 [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker) [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) | Tasks API: Android, iOS, Web, Python [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker) | Pixel 3 GPU: 20 / 25 / 53 ms [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md). Pixel 3 CPU (XNNPack): ~44 / ~18 / ~4 FPS. Pixel 3 GPU: ~49 / ~40 / ~19 FPS [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) | HIIT PCK@0.2: 93.5 / 95.7 / 97.5 [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md). Geographic PDJ: 87.0 / 91.8 / 94.2 [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) | Apache-2.0 card and SDK [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) [8](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.pom). Commercial use OK | **Primary** (High) |
| **Apple Vision 2D** | 19 joints [18](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest). Swift `DetectHumanBodyPoseRequest` (iOS 18+) has `detectsHands` and revision2 [16](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest) [17](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest/revision-swift.enum) | iOS only (VN API iOS 14+) | Not published | In Google's run: PCK@0.2 82.7 / 91.4 / 88.6 (Yoga / Dance / HIIT), against 95.5 / 96.3 / 95.7 for BlazePose Full. Vendor test, pre-revision2 [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md) | OS framework, no model to ship | iOS fallback and cross-check (Medium) |
| **Apple Vision 3D** | 17 joints; camera-relative positions; `bodyHeight` (m); `cameraOriginMatrix` [21](https://developer.apple.com/documentation/vision/humanbodypose3dobservation) | iOS 17+ (VN), iOS 18+ (Swift) [19](https://developer.apple.com/documentation/vision/detecthumanbodypose3drequest) [20](https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest) | Not published | Not published | OS framework | Optional height calibration; untested (Low) |
| **ML Kit Pose Detection** | 33 landmarks. Z is "experimental… not a true 3D value". The face must be visible [14](https://developers.google.com/ml-kit/vision/pose-detection) | Android, iOS | Base SDK: ~30 FPS on Pixel 4, ~45 FPS on iPhone X [14](https://developers.google.com/ml-kit/vision/pose-detection) | Not published | Beta, "not subject to any SLA or deprecation policy". Last release 18.0.0-beta5 (Aug 2024) [15](https://dl.google.com/android/maven2/com/google/mlkit/pose-detection/maven-metadata.xml) | **Avoid** as primary (High) |
| **MoveNet** Lightning / Thunder | 17 COCO keypoints [23](https://github.com/tensorflow/tfjs-models/blob/master/pose-detection/src/movenet/README.md) | TFLite / LiteRT, TF.js | Pixel 5 FP16: Lightning 25 ms GPU / 60 ms CPU; Thunder 45 / 155 ms [24](https://blog.tensorflow.org/2021/08/pose-estimation-and-classification-on-edge-devices-with-MoveNet-and-TensorFlow-Lite.html) | mAP 63.0 / 72.0 on a single-person COCO subset [24](https://blog.tensorflow.org/2021/08/pose-estimation-and-classification-on-edge-devices-with-MoveNet-and-TensorFlow-Lite.html) | Apache-2 per NGC [25](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ace/containers/vision-ai-movenet); Kaggle card not verified | Backup. No heels, foot index or hand points (Medium) |
| **RTMPose** t / s / m / l | 17 COCO keypoints, plus Body8/Halpe26 variants [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose) | ncnn, ONNX Runtime, TensorRT. Needs a person detector (RTMDet-nano) | Snapdragon 865, ncnn-FP16: 9.02 / 13.89 / 26.44 / 45.37 ms [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose) | COCO AP 68.5 / 72.2 / 75.8 / 76.5 [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose) | Code Apache-2.0 [27](https://github.com/open-mmlab/mmpose). Weights are trained on academic datasets (AIC+COCO, Body8); their commercial status is **unverified** | Secondary candidate (Medium) |
| **YOLO26-pose** n–x | 17 keypoints, 640 px [28](https://docs.ultralytics.com/tasks/pose/) | CoreML / LiteRT / NCNN export | CPU ONNX: n 40.3 ms; T4 TensorRT: n 1.8 ms [28](https://docs.ultralytics.com/tasks/pose/) | mAP50-95 57.2–71.6 [28](https://docs.ultralytics.com/tasks/pose/) | AGPL-3.0 or Enterprise License. "All Ultralytics YOLO trained models fall under the AGPL-3.0 License by default" [29](https://www.ultralytics.com/license) | **Exclude** unless a licence is bought (High) |
| **RF-DETR Keypoint** (Preview, June 2026) | 17 keypoints; 576²; 40.7M params [30](https://rfdetr.roboflow.com/latest/learn/run/keypoints/) | `rfdetr` package; no mobile export documented | 9.7 ms on T4 (TensorRT FP16) [30](https://rfdetr.roboflow.com/latest/learn/run/keypoints/) | 71.8 AP [30](https://rfdetr.roboflow.com/latest/learn/run/keypoints/) | Apache-2.0. API and weights may change before stable [30](https://rfdetr.roboflow.com/latest/learn/run/keypoints/) [31](https://docs.roboflow.com/changelog/explore-by-month/june-2026/rf-detr-keypoint-preview) | Watchlist (Medium) |
| **ViTPose** | Transformer pose model | Server-class (no mobile numbers gathered) | — | — | Repo Apache-2.0 [32](https://github.com/ViTAE-Transformer/ViTPose) | Candidate for server-side pre-labeling only (Low) |
| **Sapiens / Sapiens2** | High-resolution human foundation models. Sapiens2 (ICLR 2026, released 24 Apr 2026) is pretrained on 1B human images [34](https://github.com/facebookresearch/sapiens2) | Server-class | — | — | Sapiens: CC BY-NC 4.0 [33](https://github.com/facebookresearch/sapiens). Sapiens2: bans "biometric processing" and inferring health data without consents [34](https://github.com/facebookresearch/sapiens2) | **Exclude** (High) |
| SAM 3D Body; LMFormer, LiPE | — | — | — | — | SAM 3D Body: custom licence, not reviewed [35](https://github.com/facebookresearch/sam-3d-body). LMFormer and LiPE appear in a Feb 2026 review, with no license or perf data in its summary [36](https://mobile.fhstp.ac.at/?p=15652) | Not evaluated |

### 1.2 Notes that change decisions

- **Provenance favours MediaPipe.** The BlazePose card names its training data (consented images) and runs a fairness evaluation across 14 geographic subregions. Across regions, PDJ varies by 4.8 points for Full and 6.5 for Lite [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). No other candidate documents this. **High**
- **Limits stated in the model card** [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf):
  - It tracks a single person.
  - It is out of scope beyond ~4 m (14 ft) or when the head is not visible.
  - It is "sensitive to face position, scale and orientation".
  - It tolerates about 10% shift/scale and 8° roll.
  - Quality degrades in low light, noise and motion.
  - It is "not intended for human life-critical decisions. The primary intended application is entertainment."

  Copy should therefore say "form guidance", not injury prevention or diagnosis. **High**
- **The model is from 2021.** The card is dated 16 Apr 2021, and no newer pose model card was found. The Pose Landmarker page was updated on 9 Oct 2026 but announces no new pose model [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker). Recent MediaPipe releases (v1.1.0 on 7 Oct, v1.1.1 on 14 Oct 2026) concentrate on LiteRT, embedding and retrieval features [6](https://github.com/google-ai-edge/mediapipe/releases). **Medium**
- **Web-runtime numbers.** For BlazePose GHUM on Pixel 5, MediaPipe (WASM + GPU) runs at 25 / 21 / 8 FPS, and on iPhone 11 TF.js WebGL runs at 43 / 32 / 22 FPS [5](https://blog.tensorflow.org/2021/08/3d-pose-detection-with-mediapipe-blazepose-ghum-tfjs.html). These are browser numbers, not native, and only a lower bound. **Medium**
- **Buy option.** The QuickPose SDK is "Powered by MediaPipe", processes on-device, and offers native iOS/Android SDKs plus a React Native SDK in its navigation. Pricing is not published, and its testimonials contain placeholder text [38](https://quickpose.ai/). It is a fallback if building the CV module slips. **Medium**
- **Qualcomm AI Hub port.** The AI Hub page for MediaPipe-Pose lists the detector at 3.14 MB / 815K params and the landmarker at 12.9 MB / 3.36M params, both float, Apache-2.0. The page shows no latency for any chipset [37](https://aihub.qualcomm.com/models/mediapipe_pose). **Medium**

## 2. Form assessment and rep counting

### 2.1 Method options

| Approach | How it works | Reported results | Data needed | Use in product |
|---|---|---|---|---|
| **Rules + per-exercise state machine** | Joint angles and distances drive phase states. Google's recipe uses a k-NN pose classifier on pairwise-distance features with EMA smoothing. Its enter and exit thresholds differ so that pauses do not create "phantom counts" [4](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose_classification.md) | No accuracy figure published | "about a few hundred samples for each terminal state of each exercise", covering several angles, environments and body shapes [4](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose_classification.md) | **MVP** |
| **Pose-sequence counter** (PoseRAC) | Transformer over landmarks, trained on "salient pose" labels | On RepCount: MAE 0.236, OBO 0.560 at 20 ms. TransRAC scores 0.443 / 0.291 at 200 ms; RepNet 0.995 / 0.013 [51](https://github.com/MiracleDance/PoseRAC) | Pose-level annotations | v2, retrained on our own data |
| **Video-level counters** (RepNet, TransRAC) | Temporal self-similarity or video transformers [54](https://arxiv.org/abs/2006.15418) [50](https://github.com/SvipRepetitionCounting/TransRAC) | Weaker than PoseRAC on RepCount (row above) | Large video corpora | Not on-device |
| **3D-pose GCN classifier + corrector** (EC3D) | A graph network has a mistake-classification branch and a pose-correction branch [43](https://github.com/Jacoo-Zhao/3D-Pose-Based-Feedback-For-Physical-Exercises) | 90.9% mistake identification; 94.2% of mistakes corrected. Lab data, 3 exercises [43](https://github.com/Jacoo-Zhao/3D-Pose-Based-Feedback-For-Physical-Exercises) | Labelled 3D sequences | v2 architecture reference |
| **Self-supervised error detection** (Fitness-AQA) | Cross-view, cross-subject pose-contrastive learning plus motion disentangling [40](https://arxiv.org/abs/2202.14019) | In-the-wild back-squat F1 (best vs off-the-shelf pose baselines) [40](https://arxiv.org/abs/2202.14019):<br>• knees-inward: **0.526** (OpenPose 2D 0.414; SPIN 3D 0.288)<br>• knees-forward: 0.847 (OpenPose 0.812)<br>• shallow-squat: 0.869 (OpenPose 0.834) | Large unlabelled set plus expert labels | Evidence of which errors are hard |
| **VLM / streaming VLM** (QEVD) | Video-language models generate spoken feedback | Zero-shot: METEOR 0.047–0.104, LLM-Acc 1.29–2.27 out of 5. Fine-tuned Stream-VLM: 0.127 / 2.45. Timing T-F-Score 0.56 vs 0.50 for non-interactive baselines [44](https://arxiv.org/abs/2407.08101) | 474+ h of coaching video. The baseline code (FitCoach, BSD-3-Clause-Clear) needs LLaMA-2-7B weights [46](https://github.com/Qualcomm-AI-research/FitCoach) | **Not** for live cues. An LLM only narrates structured metrics after the set |

**Takeaway.** Only the rule and state-machine approach can ship before we own a licensed dataset. Learned models become the v2 upgrade once proprietary data exists (§3.2). **High**

### 2.2 Failure modes and what the evidence says

| Factor | Evidence | Design response |
|---|---|---|
| **Depth ambiguity** | BlazePose z is "not metric but up to scale", fitted from GHUM synthetic data [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). ML Kit z is "not a true 3D value" [14](https://developers.google.com/ml-kit/vision/pose-detection). Depth-order labels cut depth-ordering errors from 25% to 3% in GHUM fitting, but the result is still not metric [5](https://blog.tensorflow.org/2021/08/3d-pose-detection-with-mediapipe-blazepose-ghum-tfjs.html) | Measure each angle in the view where it lies in the image plane. Treat z and world coordinates as advisory |
| **Systematic angle bias** | Knee flexion vs IMU: −13.9 ± 15.1°, 95% limits of agreement −43.5° to +15.5°. Lateral views showed smaller deviation, and tight trousers were more stable than shorts [60](https://iris.uniecampus.it/handle/11389/91575). In a squat-to-box trial MediaPipe read about 15° below IMU and MoCap [61](https://arxiv.org/pdf/2503.14760). For general limb movements, a 2022 study found MediaPipe close to Kinect V2 against a Qualisys reference [64](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9824231/). Abstract-level evidence | Use a per-user range-of-motion (ROM) baseline and relative thresholds. Require side view for depth cues. Include a clothing tip in setup |
| **Frontal-plane (valgus) validity** | Against Kinect V2 (254 athletes): small coronal and moderate sagittal differences, with MediaPipe underestimating both [62](https://link.springer.com/article/10.1007/s11548-024-03156-5). Against 3D mocap (single-leg drop landing): MediaPipe significantly higher, with no concurrent validity for absolute values [63](https://doaj.org/article/2d283f6411874c82988f54dd2e60829f). 2D frontal-plane projection angle (FPPA) validity depends on depth, stance leg and whether valgus is present [65](https://ijspt.scholasticahq.com/article/35706.pdf) | Treat valgus as a beta, trend-based cue relative to the user's baseline. Never give a hard verdict |
| **Gym conditions** | Off-the-shelf estimators struggle with camera angles, equipment occlusion, illumination and clothing [40](https://arxiv.org/abs/2202.14019) | Setup checks. Abstain from a verdict when confidence is low |
| **Framing and distance** | Single person, at most 4 m, head visible, 25% margin, tolerance of 10% shift/scale and 8° roll [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). ML Kit needs the face visible [14](https://developers.google.com/ml-kit/vision/pose-detection). Google's evaluation placed people 2–4 m from the camera [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md) | The setup coach enforces 2–4 m with full body and head in frame |
| **Multi-camera upside** | OpenCap with 2 iPhones: 4.5° mean absolute error (range 1.7–10.3°) vs mocap. More cameras added little, and single-camera use was not validated [59](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462) | Optional dual-phone "Pro" mode later |
| **Thermal throttling** | iOS `ThermalState` runs nominal, fair, serious, critical [67](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum). Android has thermal status plus headroom (API 30); do not call headroom more than once per 10 s [68](https://developer.android.com/games/optimize/adpf/thermal) | Step down Full → Lite → lower FPS → counting only |

### 2.3 Which view for which error

| Error or metric | Required view | Basis | Confidence |
|---|---|---|---|
| Squat / lunge depth; hip and knee flexion ROM | Side | Lateral views reduced flexion error [60](https://iris.uniecampus.it/handle/11389/91575). Knees-forward reached F1 0.85 in the wild [40](https://arxiv.org/abs/2202.14019) | Medium |
| Knee travel forward, torso lean, bar path, lumbar rounding | Side | Sagittal-plane quantities (inference). Fitness-AQA labels these error types [40](https://arxiv.org/abs/2202.14019) | Low–Medium |
| Knees caving (valgus), stance width, lateral hip shift, left/right asymmetry | Front | Measured as 2D FPPA in the frontal plane [65](https://ijspt.scholasticahq.com/article/35706.pdf). Validity is weak [63](https://doaj.org/article/2d283f6411874c82988f54dd2e60829f), and best in-the-wild F1 is 0.53 [40](https://arxiv.org/abs/2202.14019) | Low |
| Push-up hip sag or pike, plank line, push-up depth | Side | Sagittal-plane (inference only) | Low |
| Overhead press: lumbar extension (side); arm symmetry (front) | Side / front | Inference. Fitness-AQA covers OHP, but per-view results were not extracted [40](https://arxiv.org/abs/2202.14019) | Low |

**Product rule.** Each exercise declares the view it requires. The app verifies orientation before it enables view-specific cues. A user filming from the wrong angle still gets rep counting and view-independent cues, plus a prompt to re-position.

### 2.4 Smoothing, gating and calibration (spec-ready)

- **One Euro filter** (Casiez, Roussel, Vogel, CHI 2012) is a speed-adaptive low-pass filter with parameters `mincutoff` and `beta` [66](https://gery.casiez.net/1euro/).
  - Published tuning: set `beta` = 0 and `mincutoff` ≈ 1 Hz, then tune `mincutoff` to remove jitter at rest.
  - Then raise `beta`, starting near 0.001 and changing it by factors of 10, to cut lag on fast moves.
  - Reference implementations are BSD or MIT licensed.
  - Apply it per 2D keypoint before computing angles, and tune per exercise tempo. **High**
- **Confidence gating.** BlazePose returns per-keypoint *visibility* (in frame and not occluded) and *presence* (in frame) [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). The Tasks API exposes `min_pose_detection_confidence`, `min_pose_presence_confidence` and `min_tracking_confidence` (each default 0.5), plus `num_poses` (default 1) and the IMAGE / VIDEO / LIVE_STREAM modes [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker).
  - Proposed rule: a cue may fire only if every joint it depends on clears the visibility threshold in ≥80% of the rep's frames.
  - Otherwise the rep is counted and marked "form not assessed".
- **Hysteresis.** Use separate enter and exit thresholds per phase [4](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose_classification.md).
- **Calibration flow (proposed)** [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md) [21](https://developer.apple.com/documentation/vision/humanbodypose3dobservation):
  1. Placement guide: 2–4 m away, at the view the exercise requires.
  2. Framing check: full body, head and margin in frame.
  3. Three slow reference reps to record the user's ROM baseline.
  4. Optional height entry, or Apple 3D `bodyHeight` on iOS 17+.
  5. Automatic re-check whenever tracking confidence drops.
- **Cue timing.** QEVD scores "when to say it" as well as "what to say" [44](https://arxiv.org/abs/2407.08101). Fire cues at rep boundaries: at most one corrective cue per rep, plus periodic positive reinforcement.

## 3. Datasets, licences, and what a commercial product may train on

### 3.1 Public datasets (licences verified where linked)

| Dataset | Content | Licence or terms | Commercial training? |
|---|---|---|---|
| **Fitness-AQA** (ECCV 2022) | Back squat, barbell row and overhead press clips from Instagram and YouTube, labelled by 2 professional trainers [40](https://arxiv.org/abs/2202.14019) | CC BY-NC 4.0. "Research, non-commercial purposes… will not be included as part of any commercial software package or product" [39](https://github.com/ParitoshParmar/Fitness-AQA) | **No** (High) |
| **Fit3D** | 611 multi-view sequences, >3M images, 2,964,236 3D skeletons, 37+ exercises, GHUM/SMPL-X fits, ≥5 reps annotated per sequence [42](https://fit3d.imar.ro/) | Non-commercial. "Prohibits the use of the Software to train methods/algorithms/neural networks/etc. for commercial use". Commercial licence via licenses@imar.ro [41](https://fit3d.imar.ro/legal) | **No** unless licensed (High) |
| **EC3D** (ACCV 2022) | 3 exercises with 3D poses and mistake labels [43](https://github.com/Jacoo-Zhao/3D-Pose-Based-Feedback-For-Physical-Exercises) | No licence in the repo; data on Google Drive [43](https://github.com/Jacoo-Zhao/3D-Pose-Based-Feedback-For-Physical-Exercises) | **No** (no grant) (Medium) |
| **QEVD** (NeurIPS 2024 D&B) | 474+ h of video [44](https://arxiv.org/abs/2407.08101):<br>• FIT-300K: 281,660 train / 16,429 test clips, 1,800+ participants, 148 exercises, 573,637 feedbacks<br>• FIT-COACH: 149 / 74 long videos | Qualcomm "Data License Agreement – Research Use": "solely for non-profit research purposes… excludes any Commercial Use". It also covers trained "Results", with injunction and profit-disgorgement remedies [45](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Dataset-Research-License-Feb-25-2025.pdf). The crowd-worker agreements permit commercial use [44](https://arxiv.org/abs/2407.08101), so a commercial licence would have to be negotiated with Qualcomm | **No** (High) |
| **MM-Fit** | Phone, watch and earbud IMU plus RGB-D video; >800 min; 10 exercises [47](https://mmfit.github.io/) | The Zenodo video record (20 sessions) is CC BY 4.0 [48](https://zenodo.org/records/7672767). Full-dataset terms are not stated [47](https://mmfit.github.io/) | **Partly**: video subset with attribution; confirm consent scope (Medium) |
| **RepCount** (TransRAC, CVPR 2022) | 1,451 videos, 19,280 annotations; Part-A sourced from YouTube [49](https://svip-lab.github.io/dataset/RepCount_dataset.html) | No licence stated [49](https://svip-lab.github.io/dataset/RepCount_dataset.html). Code is Apache-2.0 [50](https://github.com/SvipRepetitionCounting/TransRAC) | **No** (third-party video) (Medium) |
| **LLSP** | TransRAC training scripts load `LLSP_npz`, so LLSP appears to be RepCount's internal name [50](https://github.com/SvipRepetitionCounting/TransRAC) | Same as RepCount | **No** (Low) |
| **RepCount-pose** (PoseRAC) | Salient-pose annotations on RepCount [51](https://github.com/MiracleDance/PoseRAC) | Repo is MIT; the underlying videos come from YouTube | Annotations only (Low) |
| **Countix** (RepNet, CVPR 2020) | CSV of YouTube IDs, Kinetics class and counts [53](https://storage.googleapis.com/deepmind-media/Datasets/countix.tar.gz); "~90 times larger than existing datasets" [54](https://arxiv.org/abs/2006.15418) | No licence text in the archive README [53](https://storage.googleapis.com/deepmind-media/Datasets/countix.tar.gz), and none on the project page [52](https://sites.google.com/view/repnet) | **No** (third-party video) (Medium) |
| **InfiniteForm** (synthetic) | 60k images, 15 fitness pose categories [55](https://arxiv.org/abs/2110.01330) | The arXiv page shows CC BY 4.0, which may cover only the paper. Dataset terms not verified | Maybe; verify (Low) |
| **EgoExo-Fitness** (ECCV 2024) | Egocentric and exocentric fitness video [56](https://github.com/iSEE-Laboratory/EgoExo-Fitness) | Research only. "Testing commercial systems" counts as commercial use [56](https://github.com/iSEE-Laboratory/EgoExo-Fitness) | **No**, not even for benchmarking (High) |
| **MyoMechanix** (arXiv, Aug 2026) | Multi-view RGB, 3D pose, sEMG, action quality assessment (AQA) [57](https://github.com/HaoYin116/FLEX) | Academic only; no commercial use; no redistribution [57](https://github.com/HaoYin116/FLEX) | **No** (High) |
| **SMPL / SMPL-X** (for synthetic pipelines) | Parametric body model [58](https://smpl.is.tue.mpg.de/modellicense.html) | Non-commercial; bars training for commercial use. Commercial licence via Meshcapade [58](https://smpl.is.tue.mpg.de/modellicense.html) | Only with a commercial licence (High) |

**Implications**

- Keep research-only sets out of every pipeline, including internal benchmarking. EgoExo-Fitness names "testing commercial systems" explicitly [56](https://github.com/iSEE-Laboratory/EgoExo-Fitness). QEVD's "Commercial Use" covers processing data to generate results for products [45](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Dataset-Research-License-Feb-25-2025.pdf). **High**
- Pretrained weights differ in risk:
  - MediaPipe's model was trained on Google's own consented images [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf), so its risk is low.
  - RTMPose and ViTPose weights come from academic datasets, so they need legal review before shipping.

### 3.2 Proprietary data collection and labelling plan (proposed)

1. **Sources**
   - Paid recording sessions with written releases that name model training as a purpose.
   - Opt-in in-app contribution: keypoint sequences by default, video only with a separate explicit consent.
   - Coach-directed sets that induce specific errors.

   Fitness-AQA warns that deliberately faked errors made without load are exaggerated [40](https://arxiv.org/abs/2202.14019), so mix natural errors under load with coached ones.
2. **Coverage matrix per exercise**
   - Views: front, 45° and side.
   - Distance: 2, 3 and 4 m [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md).
   - Lighting: bright, dim and backlit.
   - Clothing: shorts and tight trousers [60](https://iris.uniecampus.it/handle/11389/91575).
   - Equipment occlusion [40](https://arxiv.org/abs/2202.14019), clutter, body size, skin tone and age band.

   Report results stratified, the way the BlazePose card's 14-region fairness table does [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf).
3. **Labels**
   - Rep start and end, plus phase.
   - Per-rep error tags with severity 0–2.
   - View tag and quality flags (occlusion, out of frame).
   - Two certified coaches label each clip, plus an adjudicator. Track inter-rater agreement; Fitness-AQA used two professional trainers [40](https://arxiv.org/abs/2202.14019).
4. **Volume**
   - Start from "a few hundred samples for each terminal state" for pose classifiers [4](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose_classification.md).
   - For each error cue, keep collecting until held-out precision and recall meet the §5 targets.
5. **Splits**
   - Split by subject, so no person appears in both train and test.
   - Freeze the test set per exercise × view, and include multiple device models.
6. **Privacy**
   - Blur faces on stored clips; Fitness-AQA's own terms require it [39](https://github.com/ParitoshParmar/Fitness-AQA).
   - Store keypoints by default and limit retention.
   - Revoking consent removes a person's data from future training sets.
   - Legal detail is in R4.
7. **Pre-labelling.** Run BlazePose Heavy offline (Apache-2.0 [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf)) to pre-label keypoints. Humans label reps and errors.

## 4. Exact current versions (registry snapshot 16 Oct 2026) and New Architecture pitfalls

### 4.1 Mobile app

| Package | Version (publish date) | Notes |
|---|---|---|
| `react-native` | **0.88.0** (15 Oct 2026) [69](https://www.npmjs.com/package/react-native) | Recent minors: 0.87.0 on 11 Aug 2026, 0.86.0 on 9 Jun 2026 [69](https://www.npmjs.com/package/react-native) |
| `expo` | **58.0.12** (16 Oct 2026). SDK 58.0.0 shipped 29 Sep 2026 [72](https://www.npmjs.com/package/expo) | SDK 58 requires [73](https://docs.expo.dev/versions/latest/):<br>• RN 0.88<br>• Android 7+ (compileSdk 37, targetSdk 36)<br>• iOS 16.4+<br>• Xcode 26.4+<br>• Node 22.13.x |
| `react` | **19.3.0**, bundled with SDK 58 [72](https://www.npmjs.com/package/expo) | — |
| `react-native-reanimated` | **4.7.1** (2 Oct 2026) [84](https://www.npmjs.com/package/react-native-reanimated) | Peers: RN 0.86–0.88, worklets 0.13.x |
| `react-native-worklets` (Software Mansion) | **0.13.0** (18 Sep 2026) [81](https://www.npmjs.com/package/react-native-worklets) | Peers: RN 0.86–0.88 |
| `@shopify/react-native-skia` | **2.14.0** (1 Oct 2026) [83](https://www.npmjs.com/package/@shopify/react-native-skia) | Peers: React ≥19, RN ≥0.78, worklets ≥0.7, Reanimated ≥4 |
| `react-native-vision-camera` | **5.2.3** (20 Aug 2026), MIT [76](https://www.npmjs.com/package/react-native-vision-camera) [77](https://github.com/mrousavy/react-native-vision-camera) | The README requires `react-native-nitro-modules` and `react-native-nitro-image`. The package sets Android minSdk 23 |
| `react-native-vision-camera-worklets` / `-skia` | **5.2.3** / **5.2.3** [79](https://www.npmjs.com/package/react-native-vision-camera-worklets) [80](https://www.npmjs.com/package/react-native-vision-camera-skia) | The worklets add-on peers on `react-native-worklets` (not `-core`). The Skia add-on peers on Skia, Reanimated and the worklets add-on |
| `react-native-nitro-modules` / `-nitro-image` | **0.37.1** (27 Aug 2026) / **0.15.2** [86](https://www.npmjs.com/package/react-native-nitro-modules) [121](https://www.npmjs.com/package/react-native-nitro-image) | Base for a custom pose module |
| `react-native-fast-tflite` | **3.0.1** (21 Apr 2026), MIT [85](https://github.com/mrousavy/react-native-fast-tflite) | Built on Nitro. Bundles LiteRT 1.4.0 on Android and TensorFlowLiteC 2.17.0 on iOS. Delegates: CoreML, Android GPU, NNAPI (NNAPI is deprecated on Android 15). **The VisionCamera v5 integration is private** |
| `react-native-worklets-core` | 1.6.3 (12 Feb 2026) [82](https://www.npmjs.com/package/react-native-worklets-core) | VisionCamera v4-era. Do not use with v5 |
| `expo-camera` / `expo-dev-client` | ~58.0.10 / ~58.0.13 (bundled) [72](https://www.npmjs.com/package/expo) | A dev client is mandatory (§4.4) |
| `expo-speech` / `expo-haptics` | 58.0.3 / 58.0.6 [125](https://www.npmjs.com/package/expo-speech) [126](https://www.npmjs.com/package/expo-haptics) | Audio cues and haptics |
| `typescript` | Pin **~6.0.3**, the version the SDK 58 template uses [75](https://www.npmjs.com/package/expo-template-default). Latest is 7.0.2 (8 Jul 2026) [97](https://www.npmjs.com/package/typescript) | TS 7.0 "does not ship with an API". `@typescript/typescript6` provides a side-by-side `tsc6`. TS 7 also dropped `target: es5`, `moduleResolution: node/node10` and `baseUrl`, and made `strict` the default [96](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) |
| Other on-device runtimes | onnxruntime-react-native 1.24.3 [90](https://www.npmjs.com/package/onnxruntime-react-native); react-native-executorch 0.10.5 [89](https://www.npmjs.com/package/react-native-executorch) | Not needed for the MVP |
| Community MediaPipe RN plugins | react-native-mediapipe 0.6.0 (Dec 2024; peers on VisionCamera and worklets-core) [87](https://www.npmjs.com/package/react-native-mediapipe); @thinksys/react-native-mediapipe 0.0.21 (Apr 2026) [88](https://www.npmjs.com/package/@thinksys/react-native-mediapipe) | Stale or pre-1.0. Do not depend on them |

### 4.2 Native CV dependencies

| Component | Version | Notes |
|---|---|---|
| MediaPipe Tasks Vision, Android | **1.1.1** (Maven lastUpdated 14 Oct 2026) [7](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/maven-metadata.xml) | Apache-2.0. Optional dependency on `litertlm-android` 0.18.0 [8](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.pom). The AAR declares minSdk 24 and targetSdk 34 [9](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.aar) |
| MediaPipe Tasks Vision, iOS | **1.0.0** on CocoaPods: iOS 15.0, static xcframework, build source dated 27 Jul 2026 [10](https://cdn.cocoapods.org/Specs/9/9/0/MediaPipeTasksVision/1.0.0/MediaPipeTasksVision.podspec.json) [11](https://cdn.cocoapods.org/all_pods_versions_9_9_0.txt) | Google documents Swift Package Manager: products `MediaPipeTasksVision` etc., iOS 15+ [12](https://developers.google.com/edge/mediapipe/solutions/setup_ios). The v1.1.1 notes mention "Update WASM and SPM files" [6](https://github.com/google-ai-edge/mediapipe/releases) |
| MediaPipe Web / Python | `@mediapipe/tasks-vision` 1.1.1 [127](https://www.npmjs.com/package/@mediapipe/tasks-vision); `mediapipe` 1.1.1 (14 Oct 2026) [110](https://pypi.org/project/mediapipe/) | Python is used for offline replay and pre-labelling |
| LiteRT Android | **2.3.0** (6 Oct 2026) [119](https://dl.google.com/android/maven2/com/google/ai/edge/litert/litert/maven-metadata.xml) | For v2 learned models. Server-side export tooling: onnxruntime 1.31.0 [123](https://pypi.org/project/onnxruntime/), executorch 1.5.1 [124](https://pypi.org/project/executorch/) |

### 4.3 Backend

| Component | Version (date) | Notes |
|---|---|---|
| Python | **3.14.8** (30 Sep 2026) recommended. 3.15.0 was released 9 Oct 2026 [98](https://www.python.org/downloads/) | Core wheels already ship for 3.15 (asyncpg, SQLAlchemy and others) [112](https://pypi.org/project/asyncpg/) [101](https://pypi.org/project/SQLAlchemy/). MediaPipe's build only added 3.13 and 3.14 support in v1.1.0 [6](https://github.com/google-ai-edge/mediapipe/releases) |
| FastAPI / Uvicorn | **0.143.3** (16 Oct 2026; Python ≥3.10; MIT) [99](https://pypi.org/project/fastapi/) / **0.54.0** [109](https://pypi.org/project/uvicorn/) | — |
| Pydantic / pydantic-settings | **2.14.1** (11 Oct 2026) [100](https://pypi.org/project/pydantic/) / **2.16.0** (Python ≥3.11) [113](https://pypi.org/project/pydantic-settings/) | — |
| SQLAlchemy / Alembic | **2.1.4** (7 Oct 2026; Python ≥3.11) [101](https://pypi.org/project/SQLAlchemy/) / **1.20.0** (11 Sep 2026) [102](https://pypi.org/project/alembic/) | — |
| Postgres drivers | asyncpg **0.32.0** (Apache-2.0) [112](https://pypi.org/project/asyncpg/); psycopg **3.3.6** (LGPL-3.0-only) [111](https://pypi.org/project/psycopg/) | — |
| PostgreSQL | **18.6** (13 Aug 2026). 18 is the current major, supported until 14 Nov 2030. PG 14 reaches end of life 12 Nov 2026 [114](https://www.postgresql.org/versions.json) | — |
| pgvector | Extension **0.8.7** (tag commit 1 Oct 2026) [115](https://github.com/pgvector/pgvector/tags); Python **0.5.1** [103](https://pypi.org/project/pgvector/) | — |
| Redis / Valkey | Redis **8.10.2** (17 Sep 2026) [117](https://github.com/redis/redis/releases), licensed under a choice of RSALv2, SSPLv1 or AGPLv3 [116](https://raw.githubusercontent.com/redis/redis/unstable/LICENSE.txt). Valkey **9.0.6 / 9.1.2**, BSD-3-Clause [118](https://github.com/valkey-io/valkey/releases). redis-py **8.1.0** [104](https://pypi.org/project/redis/) | A managed service sidesteps the licence question |
| Task queue | Celery **5.6.3** (26 Mar 2026; BSD-3) [105](https://pypi.org/project/celery/). Alternatives: Taskiq **0.13.0** (MIT) [107](https://pypi.org/project/taskiq/), Dramatiq **2.2.1** [122](https://pypi.org/project/dramatiq/) | **Avoid arq** (0.28.0), which is in maintenance-only mode [106](https://github.com/python-arq/arq) |
| Anthropic SDK | `anthropic` **1.15.0** (15 Oct 2026; MIT; Python ≥3.10) [108](https://pypi.org/project/anthropic/) | Model choice is covered in R3 |
| Do not add | `ultralytics` 8.4.178 (AGPL-3.0) [120](https://pypi.org/project/ultralytics/) | Licence (§1) |

### 4.4 New Architecture requirements and pitfalls (checklist for the Build Playbook)

1. **New Architecture only.** RN ≥0.82 runs only on the New Architecture, and `newArchEnabled=false` and `RCT_NEW_ARCH_ENABLED=0` are ignored. Expo SDK 54 and RN 0.81 were the last versions to allow the legacy architecture [70](https://reactnative.dev/blog/2025/10/08/react-native-0.82). RN 0.84 removed legacy components and made Hermes V1 and precompiled iOS binaries the default [71](https://reactnative.dev/blog). Every native dependency must be New-Architecture-ready. **High**
2. **Lockstep versions.** Reanimated 4.7.1, Worklets 0.13.x and RN 0.86–0.88 must move together [84](https://www.npmjs.com/package/react-native-reanimated) [81](https://www.npmjs.com/package/react-native-worklets). Install versions aligned with SDK 58 (Expo's bundled module list [72](https://www.npmjs.com/package/expo)) rather than "latest". **High**
3. **Two worklet runtimes.** VisionCamera v5 frame processors need `react-native-vision-camera-worklets` plus `react-native-worklets` [78](https://visioncamera.margelo.com/docs/guides/frame-processors). Plugins built on `react-native-worklets-core`, such as react-native-mediapipe 0.6.0, will not plug in [87](https://www.npmjs.com/package/react-native-mediapipe). This is inferred from peer dependencies. **Medium**
4. **No public fast-tflite glue for v5.** The fast-tflite README says its VisionCamera v5 integration is "currently part of a private project" [85](https://github.com/mrousavy/react-native-fast-tflite). Run the pose model inside our own native module. **High**
5. **Frame discipline** [78](https://visioncamera.margelo.com/docs/guides/frame-processors) [77](https://github.com/mrousavy/react-native-vision-camera):
   - Dispose every Frame, using try/finally.
   - When the buffer pool fills, the pipeline stalls and drops frames.
   - RGB uses about 2.6× the bandwidth of YUV, and LiteRT prefers RGB.
   - `useAsyncRunner` moves heavy work off the camera thread, and `runAsync` returning false is the signal to drop the frame.

   **High**
6. **No Expo Go.** Custom native code needs a development build (`expo-dev-client`). Run `npx expo prebuild --clean` after adding native libraries or changing app config [74](https://docs.expo.dev/develop/development-builds/introduction/). **High**
7. **iOS packaging spike.** Three facts collide:
   - CocoaPods trunk goes read-only on 2 Dec 2026. Existing pods keep resolving [13](https://blog.cocoapods.org/CocoaPods-Specs-Repo/).
   - MediaPipe 1.1.x is not on CocoaPods [11](https://cdn.cocoapods.org/all_pods_versions_9_9_0.txt).
   - RN's SwiftPM support is still experimental in 0.87–0.88 [71](https://reactnative.dev/blog).

   Options: pin the 1.0.0 pod, vendor the xcframework, or add SPM through a config plugin. **High** for the facts, **Low** for which option works.
8. **Toolchain floors.** SDK 58 needs Node 22.13.x, Xcode 26.4+ and compileSdk 37 [73](https://docs.expo.dev/versions/latest/). RN 0.87 needs AGP 9 and Kotlin 2.0+ [71](https://reactnative.dev/blog). **High**
9. **Android.** Prefer the GPU delegate, since NNAPI is deprecated on Android 15 [85](https://github.com/mrousavy/react-native-fast-tflite). MediaPipe's minSdk 24 matches the Android 7 floor of Expo SDK 58 [9](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.aar) [73](https://docs.expo.dev/versions/latest/). **High**
10. **TypeScript.** Keep 6.0.x for lint and test tooling, because TS 7.0 has no programmatic API [96](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/). **High**

## 5. Recommended on-device pipeline, targets and device matrix

### 5.1 Pipeline (MVP)

```
VisionCamera v5 frame output (~HD 16:9, 30 fps)
 └─ useAsyncRunner worklet: drop the frame if busy, always dispose()
     └─ PoseEngine (custom Nitro HybridObject, Kotlin/Swift)
         MediaPipe PoseLandmarker, VIDEO mode, num_poses=1,
         Full model (Lite on low tier or thermal stress)
         → 33×(x,y,z,visibility,presence) + 33 world points
           (typed arrays; no pixels back to JS)
 └─ Worklet: visibility gate → One Euro → normalise (hip-centred, torso-scaled) → angles
 └─ Exercise state machine (phases + hysteresis) → rep events + per-rep metrics
 └─ View-aware rule engine (abstains on low confidence)
    → cue scheduler (rep boundaries, ≤1 corrective cue/rep)
 └─ Outputs: Skia skeleton overlay; TTS + haptics; session log (keypoints + metrics only)
 └─ Thermal governor (iOS ThermalState / Android thermal status) → model and FPS step-down
```

- **Run inference natively.** The MediaPipe SDKs are native [7](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/maven-metadata.xml) [10](https://cdn.cocoapods.org/Specs/9/9/0/MediaPipeTasksVision/1.0.0/MediaPipeTasksVision.podspec.json). VisionCamera's `Frame` is a Nitro HybridObject with Swift and Kotlin implementations, so a Nitro module can accept it directly (from `Frame.nitro.ts` in the package source) [77](https://github.com/mrousavy/react-native-vision-camera). **Medium**
- **Use VIDEO mode, not LIVE_STREAM.** VIDEO mode is synchronous and timestamped, while LIVE_STREAM uses a callback [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker). VIDEO keeps frames and results aligned inside the async runner. This is a proposal.
- **iOS fallback.** If MediaPipe fails to initialise, fall back to Apple Vision 2D [16](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest). On iOS 17+, Apple's 3D `bodyHeight` can optionally scale the world coordinates [21](https://developer.apple.com/documentation/vision/humanbodypose3dobservation).
- **v2.** Add a learned temporal classifier on keypoint sequences, run through LiteRT 2.3.0 inside the native module [119](https://dl.google.com/android/maven2/com/google/ai/edge/litert/litert/maven-metadata.xml), or standalone through fast-tflite 3.0.1 [85](https://github.com/mrousavy/react-native-fast-tflite).

### 5.2 Performance and accuracy targets (proposed, not measured; confirm in the spike)

| Metric | Tier A | Tier B | Tier C (floor) | Anchor evidence |
|---|---|---|---|---|
| Sustained pose FPS over a 20-min session | ≥30 | ≥20 | ≥15 with Lite; else counting-only | Pixel 3 GPU: Full 25 ms, Lite 20 ms [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md). Lite ~44 FPS on CPU [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). RTMPose-s 13.9 ms on Snapdragon 865 [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose) |
| Frame-to-overlay latency (p95) | ≤100 ms | ≤150 ms | ≤200 ms | Proposal |
| Rep end to audio cue | ≤500 ms | ≤500 ms | ≤700 ms | Proposal. Timing matters per QEVD [44](https://arxiv.org/abs/2407.08101) |
| Rep count, guided setup | Exact on ≥95% of sets; within ±1 on ≥99% | Same | Same | Proposal. In-the-wild state of the art is only OBO 0.56 [51](https://github.com/MiracleDance/PoseRAC), hence the guided setup |
| Form-cue precision / recall on a held-out proprietary set | ≥0.90 / ≥0.70 per cue | Same | Form cues off | Proposal. In-the-wild knees-inward F1 is 0.53 [40](https://arxiv.org/abs/2202.14019) |
| Sagittal angle MAE vs lab reference (side view) | ≤10° | ≤10° | n/a | OpenCap with 2 cameras: 4.5° [59](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462). MediaPipe lateral view at 90°: −2.3 ± 6.4° (abstract) [60](https://iris.uniecampus.it/handle/11389/91575) |
| Thermal | No "serious" state within 20 min | Same | Degrade gracefully | [67](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum) [68](https://developer.android.com/games/optimize/adpf/thermal) |

### 5.3 Reference device matrix (proposed)

| Tier | iOS | Android | Rationale |
|---|---|---|---|
| A: current flagship | Current iPhone on iOS 27 | A Galaxy S24–S26-class phone | AI Hub's device list includes the Galaxy S21–S26 [37](https://aihub.qualcomm.com/models/mediapipe_pose) |
| B: mid-range or older flagship | iPhone 11 and iPhone SE (2nd gen), the oldest iOS 27 devices [22](https://www.apple.com/ios/) | A Snapdragon 865-class phone, the RTMPose benchmark chip [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose); a Snapdragon 7 Gen 4 device (on the AI Hub list [37](https://aihub.qualcomm.com/models/mediapipe_pose)); Galaxy S21 | Covers the bulk of active users (assumption) |
| C: floor | A device on iOS 16.4, the SDK 58 floor [73](https://docs.expo.dev/versions/latest/) | An Android 7–10 device with a Mali GPU [85](https://github.com/mrousavy/react-native-fast-tflite), at the API 24 floor [9](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.aar) | Validates degrade paths |
| Cross-check | — | Pixel 5, which has published MoveNet and BlazePose numbers [24](https://blog.tensorflow.org/2021/08/pose-estimation-and-classification-on-edge-devices-with-MoveNet-and-TensorFlow-Lite.html) [5](https://blog.tensorflow.org/2021/08/3d-pose-detection-with-mediapipe-blazepose-ghum-tfjs.html) | Sanity-checks our harness against vendor figures |

## 6. React Native vs Flutter vs native

| Criterion | React Native + Expo SDK 58 | Flutter 3.47.7 (stable, 8 Oct 2026, Dart 3.13.5) [91](https://storage.googleapis.com/flutter_infra_release/releases/releases_macos.json) | Native Swift + Kotlin |
|---|---|---|---|
| Camera frames and overlay | VisionCamera 5.2.3 worklet frame output, plus Skia overlay add-on [76](https://www.npmjs.com/package/react-native-vision-camera) [80](https://www.npmjs.com/package/react-native-vision-camera-skia) | `camera` 0.12.1 [94](https://pub.dev/packages/camera) | Full control |
| Pose integration | No maintained plugin. Wrap the native MediaPipe SDKs in a Nitro module (§5.1) | `google_mlkit_pose_detection` 0.16.1 wraps the ML Kit beta [92](https://pub.dev/packages/google_mlkit_pose_detection) [15](https://dl.google.com/android/maven2/com/google/mlkit/pose-detection/maven-metadata.xml). `mediapipe_core` is still 0.0.1 from 2024 [95](https://pub.dev/packages/mediapipe_core). MediaPipe 1.1.1 added Flutter host environments to its C API, which hints at an official path [6](https://github.com/google-ai-edge/mediapipe/releases). `tflite_flutter` 0.12.1 [93](https://pub.dev/packages/tflite_flutter) | Direct MediaPipe Tasks and Apple Vision |
| Languages for Claude Code | TypeScript for UI and logic; Swift/Kotlin only for the CV module; Python backend | Dart plus native plugin code | Two full UIs |
| Main risk | iOS packaging and the native module (§4.4) | MediaPipe plugin gap; ML Kit beta stagnation | About twice the UI effort |

**Verdict: React Native + Expo (dev builds) with a native Swift/Kotlin `PoseEngine`.** The CV hot path has to be native in every option, and RN keeps everything else in one typed language for the build agent. Revisit Flutter only if Google publishes an official MediaPipe Tasks Flutter package. **Medium**

## Recommendations for the docs

**BRD**
1. **MVP promise.** Camera rep counting plus view-aware form cues for a small set of exercises, behind a guided setup. Use "form guidance" wording, never injury prevention or diagnosis. The pose model's own card says it is not for life-critical decisions [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf).
2. **On-device by default.** No video leaves the phone by default, and keypoint-only telemetry is opt-in. Each cue carries a maturity flag (GA or beta); valgus-type cues start as beta [63](https://doaj.org/article/2d283f6411874c82988f54dd2e60829f) [40](https://arxiv.org/abs/2202.14019).
3. **Data rule.** No research-licensed dataset may be used for training, benchmarking or demos (§3.1) [45](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Dataset-Research-License-Feb-25-2025.pdf) [56](https://github.com/iSEE-Laboratory/EgoExo-Fitness). Budget for proprietary collection and coach labelling from month one.

**Technical Specification**
4. **Pinned baseline.** Freeze the §4 tables as the baseline; any change needs a version-bump ADR. MediaPipe Pose Landmarker (Full, with Lite fallback) is the engine of record, and Apple Vision is the iOS fallback (§1).
5. **Interfaces to specify:**
   - `PoseEngine` (Nitro): start/stop, `setModel(lite|full)`, target FPS, and a result of 33×5 plus 33×3 floats with timestamp and inference time.
   - `ExerciseDefinition`: required view, joints, phases with hysteresis thresholds, rules, cue copy, maturity.
   - `RepEvent` and `SessionLog`: never contain pixels.
6. **Remote tuning.** Thresholds and cue copy ship as versioned remote config, so tuning needs no app release. Also specify the One Euro parameters, the visibility gate and the thermal degrade ladder (§2.2, §2.4).

**Roadmap & Strategy**
7. **Phase 0 spike (gate).** Benchmark Lite and Full on the §5.3 matrix, settle iOS MediaPipe packaging (§4.4 item 7), and build the golden-video replay harness. Exit when the §5.2 FPS targets are met on Tiers A and B.
8. **Phase 1.** Rules MVP for 4–6 exercises chosen from spike results, with data collection running in parallel.
9. **Phase 2.** Learned counter (PoseRAC-style [51](https://github.com/MiracleDance/PoseRAC)) and per-error classifiers (EC3D-style GCN [43](https://github.com/Jacoo-Zhao/3D-Pose-Based-Feedback-For-Physical-Exercises)), trained only on our own data. Promote beta cues when they meet the §5.2 precision and recall targets.
10. **Phase 3.**
    - Dual-phone "Pro" mode [59](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462).
    - Apple 3D calibration.
    - Re-evaluate RF-DETR Keypoint and RTMPose, and YOLO only with an Enterprise licence.

**Innovative Features** (grounded in this evidence)
11. **Setup Coach.** Checks distance, view, framing and clothing, and explains why each matters [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf) [60](https://iris.uniecampus.it/handle/11389/91575).
12. **Confidence-aware coaching.** Say "I can't see your left knee — turn side-on" instead of giving a silent or wrong cue [1](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker).
13. **Personal ROM baseline and trends,** with thresholds set relative to the user [60](https://iris.uniecampus.it/handle/11389/91575).
14. **Post-set LLM debrief** built from structured metrics only, not live VLM cues [44](https://arxiv.org/abs/2407.08101).

**Build Playbook**
15. **Project setup.**
    - Start from the SDK 58 template (`expo-template-default` 58.0.21, TypeScript ~6.0.3) [75](https://www.npmjs.com/package/expo-template-default).
    - Add VisionCamera 5.2.3, `react-native-vision-camera-worklets`, `react-native-worklets`, Nitro modules/image, Skia and Reanimated at SDK-aligned versions [72](https://www.npmjs.com/package/expo).
    - Use dev builds and `npx expo prebuild --clean` [74](https://docs.expo.dev/develop/development-builds/introduction/).
16. **Native module.** Scaffold `PoseEngine` in Swift and Kotlin around MediaPipe Tasks Vision: Android 1.1.1, and on iOS the 1.0.0 pod or SPM [7](https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/maven-metadata.xml) [10](https://cdn.cocoapods.org/Specs/9/9/0/MediaPipeTasksVision/1.0.0/MediaPipeTasksVision.podspec.json) [12](https://developers.google.com/edge/mediapipe/solutions/setup_ios). Follow the §4.4 frame discipline.
17. **Golden-video tests.** Recorded clips run through Python `mediapipe` 1.1.1 [110](https://pypi.org/project/mediapipe/) and the same JSON exercise definitions to produce expected reps and cues. CI fails on regressions, and a device-lab job tracks FPS, latency and thermal state.

## Unverified / conflicting

- **RN 0.88 date.** npm shows 0.88.0 published 15 Oct 2026 [69](https://www.npmjs.com/package/react-native), but the blog-index summary dated the 0.88 post "October 19, 2026", after this brief's date [71](https://reactnative.dev/blog). Treat npm as authoritative.
- **MoveNet licence.** Apache-2 is confirmed only through NGC [25](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ace/containers/vision-ai-movenet). The Kaggle model card could not be read [128](https://www.kaggle.com/models/google/movenet).
- **No independent mid-range benchmark.** None from 2024–2026 was found. Every latency figure here is a vendor number on 2018–2020 hardware (Pixel 3/4/5, iPhone X/11/12, Snapdragon 865).
- **Apple vs MediaPipe.** The Apple Vision vs BlazePose accuracy table was run by Google and predates Apple's revision2 [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md) [17](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest/revision-swift.enum). A search found no new WWDC26 / iOS 27 body-pose API, and none was ruled out.
- **iOS SPM.** MediaPipe 1.1.x via SPM is inferred from the release notes ("Update WASM and SPM files") [6](https://github.com/google-ai-edge/mediapipe/releases) and has not been build-tested with Expo SDK 58.
- **World-landmark units.** Legacy docs and the TF blog say metres, hip-centred [3](https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md) [5](https://blog.tensorflow.org/2021/08/3d-pose-detection-with-mediapipe-blazepose-ghum-tfjs.html). The model card says z is "up to scale" [2](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf). Treat world coordinates as approximate.
- **Valgus bias direction conflicts.** MediaPipe reads lower than Kinect V2 [62](https://link.springer.com/article/10.1007/s11548-024-03156-5) but higher than 3D mocap [63](https://doaj.org/article/2d283f6411874c82988f54dd2e60829f). Both rest on abstract-level evidence. The Cosoli et al. lateral-view and clothing figures came from a garbled abstract extraction [60](https://iris.uniecampus.it/handle/11389/91575).
- **Weight licensing.** Whether RTMPose and ViTPose weights are commercially usable, given their academic training data, was not determined [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose) [32](https://github.com/ViTAE-Transformer/ViTPose).
- **Sapiens2.** Whether form analysis counts as "biometric processing" is a legal question [34](https://github.com/facebookresearch/sapiens2).
- **Licences not reviewed:**
  - SAM 3D Body [35](https://github.com/facebookresearch/sam-3d-body).
  - InfiniteForm: the dataset terms may differ from the paper's CC BY [55](https://arxiv.org/abs/2110.01330).
  - MM-Fit: no licence is stated for the full dataset [47](https://mmfit.github.io/).
- **LLSP = RepCount.** This is inferred from TransRAC code paths only [50](https://github.com/SvipRepetitionCounting/TransRAC).
- **Not evaluated:**
  - RTMO, the one-stage multi-person RTMPose variant [26](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose).
  - expo-camera frame access.
  - QuickPose pricing and terms [38](https://quickpose.ai/).
- **Proposed targets.** Every target in §5.2 and the §5.3 device tiers is a proposal, not a measurement.

## Sources

1. MediaPipe Pose Landmarker guide (updated 2026-10-09) — https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker
2. Model Card: BlazePose GHUM 3D (16 Apr 2021) — https://storage.googleapis.com/mediapipe-assets/Model%20Card%20BlazePose%20GHUM%203D.pdf
3. MediaPipe legacy docs: Pose (quality and latency tables) — https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose.md
4. MediaPipe legacy docs: Pose Classification (k-NN, rep counting) — https://raw.githubusercontent.com/google-ai-edge/mediapipe/master/docs/solutions/pose_classification.md
5. TensorFlow Blog: 3D Pose Detection with MediaPipe BlazePose GHUM and TF.js (2021) — https://blog.tensorflow.org/2021/08/3d-pose-detection-with-mediapipe-blazepose-ghum-tfjs.html
6. MediaPipe GitHub releases (v1.1.0, v1.1.1) — https://github.com/google-ai-edge/mediapipe/releases
7. Google Maven: com.google.mediapipe:tasks-vision metadata — https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/maven-metadata.xml
8. tasks-vision 1.1.1 POM — https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.pom
9. tasks-vision 1.1.1 AAR (manifest minSdk) — https://dl.google.com/android/maven2/com/google/mediapipe/tasks-vision/1.1.1/tasks-vision-1.1.1.aar
10. CocoaPods: MediaPipeTasksVision 1.0.0 podspec — https://cdn.cocoapods.org/Specs/9/9/0/MediaPipeTasksVision/1.0.0/MediaPipeTasksVision.podspec.json
11. CocoaPods CDN version index (MediaPipeTasksVision) — https://cdn.cocoapods.org/all_pods_versions_9_9_0.txt
12. MediaPipe iOS setup guide (SPM) — https://developers.google.com/edge/mediapipe/solutions/setup_ios
13. CocoaPods blog: Specs repo / trunk read-only plan — https://blog.cocoapods.org/CocoaPods-Specs-Repo/
14. ML Kit Pose Detection (Beta) — https://developers.google.com/ml-kit/vision/pose-detection
15. Google Maven: ML Kit pose-detection metadata — https://dl.google.com/android/maven2/com/google/mlkit/pose-detection/maven-metadata.xml
16. Apple: DetectHumanBodyPoseRequest — https://developer.apple.com/documentation/vision/detecthumanbodyposerequest
17. Apple: DetectHumanBodyPoseRequest.Revision — https://developer.apple.com/documentation/vision/detecthumanbodyposerequest/revision-swift.enum
18. Apple: VNDetectHumanBodyPoseRequest — https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest
19. Apple: DetectHumanBodyPose3DRequest — https://developer.apple.com/documentation/vision/detecthumanbodypose3drequest
20. Apple: VNDetectHumanBodyPose3DRequest — https://developer.apple.com/documentation/vision/vndetecthumanbodypose3drequest
21. Apple: HumanBodyPose3DObservation — https://developer.apple.com/documentation/vision/humanbodypose3dobservation
22. Apple: iOS 27 (compatible devices) — https://www.apple.com/ios/
23. TF.js MoveNet README — https://github.com/tensorflow/tfjs-models/blob/master/pose-detection/src/movenet/README.md
24. TensorFlow Blog: Pose estimation and classification on edge devices with MoveNet and TensorFlow Lite (2021) — https://blog.tensorflow.org/2021/08/pose-estimation-and-classification-on-edge-devices-with-MoveNet-and-TensorFlow-Lite.html
25. NVIDIA NGC: vision-ai-movenet — https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ace/containers/vision-ai-movenet
26. MMPose RTMPose project README — https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose
27. MMPose repository (Apache-2.0) — https://github.com/open-mmlab/mmpose
28. Ultralytics docs: Pose (YOLO26) — https://docs.ultralytics.com/tasks/pose/
29. Ultralytics licensing — https://www.ultralytics.com/license
30. RF-DETR docs: Keypoints (Preview) — https://rfdetr.roboflow.com/latest/learn/run/keypoints/
31. Roboflow changelog: RF-DETR Keypoint Preview (June 2026) — https://docs.roboflow.com/changelog/explore-by-month/june-2026/rf-detr-keypoint-preview
32. ViTPose repository — https://github.com/ViTAE-Transformer/ViTPose
33. Meta Sapiens repository (CC BY-NC 4.0) — https://github.com/facebookresearch/sapiens
34. Meta Sapiens2 repository and LICENSE.md — https://github.com/facebookresearch/sapiens2
35. Meta SAM 3D Body repository — https://github.com/facebookresearch/sam-3d-body
36. FH St. Pölten: State of the Art in Real-Time 2D Pose Estimation using Smartphones (Feb 2026) — https://mobile.fhstp.ac.at/?p=15652
37. Qualcomm AI Hub: MediaPipe-Pose — https://aihub.qualcomm.com/models/mediapipe_pose
38. QuickPose SDK — https://quickpose.ai/
39. Fitness-AQA repository and dataset licence — https://github.com/ParitoshParmar/Fitness-AQA
40. Parmar et al., Domain Knowledge-Informed Self-Supervised Representations for Workout Form Assessment (arXiv 2202.14019) — https://arxiv.org/abs/2202.14019
41. Fit3D licence — https://fit3d.imar.ro/legal
42. Fit3D dataset — https://fit3d.imar.ro/
43. EC3D / 3D Pose Based Feedback for Physical Exercises (repo; arXiv 2208.03257) — https://github.com/Jacoo-Zhao/3D-Pose-Based-Feedback-For-Physical-Exercises
44. Panchal et al., What to Say and When to Say it: Live Fitness Coaching as a Testbed for Situated Interaction (QEVD) — https://arxiv.org/abs/2407.08101
45. Qualcomm Data License Agreement – Research Use (QEVD, 25 Feb 2025) — https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Dataset-Research-License-Feb-25-2025.pdf
46. Qualcomm FitCoach repository — https://github.com/Qualcomm-AI-research/FitCoach
47. MM-Fit dataset site — https://mmfit.github.io/
48. Zenodo: MM-Fit Dataset – workout sessions (video), CC BY 4.0 — https://zenodo.org/records/7672767
49. RepCount dataset page — https://svip-lab.github.io/dataset/RepCount_dataset.html
50. TransRAC repository — https://github.com/SvipRepetitionCounting/TransRAC
51. PoseRAC repository — https://github.com/MiracleDance/PoseRAC
52. RepNet project page (Countix) — https://sites.google.com/view/repnet
53. Countix archive (README + CSVs) — https://storage.googleapis.com/deepmind-media/Datasets/countix.tar.gz
54. Dwibedi et al., Counting Out Time (RepNet, CVPR 2020) — https://arxiv.org/abs/2006.15418
55. InfiniteForm: A synthetic, minimal bias dataset for fitness applications — https://arxiv.org/abs/2110.01330
56. EgoExo-Fitness repository and License Agreement — https://github.com/iSEE-Laboratory/EgoExo-Fitness
57. MyoMechanix repository (FLEX) — https://github.com/HaoYin116/FLEX
58. SMPL model licence — https://smpl.is.tue.mpg.de/modellicense.html
59. Uhlrich et al., OpenCap (PLOS Comput Biol 2023) — https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011462
60. Cosoli, Arnesano, Scalise (2026), MediaPipe vs IMU knee flexion in squats (abstract) — https://iris.uniecampus.it/handle/11389/91575
61. Validation of Human Pose Estimation and Human Mesh Recovery for Extracting Clinically Relevant Motion Data from Videos (arXiv 2503.14760) — https://arxiv.org/pdf/2503.14760
62. MediaPipe vs Kinect V2 in athletic stress tests (Springer, 2024) — https://link.springer.com/article/10.1007/s11548-024-03156-5
63. Heliyon (Sep 2024): MediaPipe knee valgus in single-leg drop landing vs 3D motion analysis — https://doaj.org/article/2d283f6411874c82988f54dd2e60829f
64. Validation of Angle Estimation Based on Body Tracking Data from RGB-D and RGB Cameras (Sensors 2022) — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9824231/
65. IJSPT: 2-D frontal plane projection angle during single-leg squat — https://ijspt.scholasticahq.com/article/35706.pdf
66. Casiez et al., 1€ Filter — https://gery.casiez.net/1euro/
67. Apple: ProcessInfo.ThermalState — https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum
68. Android Developers: Thermal API (ADPF) — https://developer.android.com/games/optimize/adpf/thermal
69. npm: react-native — https://www.npmjs.com/package/react-native
70. React Native 0.82 release post — https://reactnative.dev/blog/2025/10/08/react-native-0.82
71. React Native blog index — https://reactnative.dev/blog
72. npm: expo (incl. bundledNativeModules) — https://www.npmjs.com/package/expo
73. Expo SDK reference / version table — https://docs.expo.dev/versions/latest/
74. Expo: Development builds introduction — https://docs.expo.dev/develop/development-builds/introduction/
75. npm: expo-template-default — https://www.npmjs.com/package/expo-template-default
76. npm: react-native-vision-camera — https://www.npmjs.com/package/react-native-vision-camera
77. VisionCamera repository (MIT; package source incl. Frame.nitro.ts, useAsyncRunner) — https://github.com/mrousavy/react-native-vision-camera
78. VisionCamera docs: Frame Processors — https://visioncamera.margelo.com/docs/guides/frame-processors
79. npm: react-native-vision-camera-worklets — https://www.npmjs.com/package/react-native-vision-camera-worklets
80. npm: react-native-vision-camera-skia — https://www.npmjs.com/package/react-native-vision-camera-skia
81. npm: react-native-worklets — https://www.npmjs.com/package/react-native-worklets
82. npm: react-native-worklets-core — https://www.npmjs.com/package/react-native-worklets-core
83. npm: @shopify/react-native-skia — https://www.npmjs.com/package/@shopify/react-native-skia
84. npm: react-native-reanimated — https://www.npmjs.com/package/react-native-reanimated
85. react-native-fast-tflite repository/README — https://github.com/mrousavy/react-native-fast-tflite
86. npm: react-native-nitro-modules — https://www.npmjs.com/package/react-native-nitro-modules
87. npm: react-native-mediapipe — https://www.npmjs.com/package/react-native-mediapipe
88. npm: @thinksys/react-native-mediapipe — https://www.npmjs.com/package/@thinksys/react-native-mediapipe
89. npm: react-native-executorch — https://www.npmjs.com/package/react-native-executorch
90. npm: onnxruntime-react-native — https://www.npmjs.com/package/onnxruntime-react-native
91. Flutter release manifest (macOS) — https://storage.googleapis.com/flutter_infra_release/releases/releases_macos.json
92. pub.dev: google_mlkit_pose_detection — https://pub.dev/packages/google_mlkit_pose_detection
93. pub.dev: tflite_flutter — https://pub.dev/packages/tflite_flutter
94. pub.dev: camera — https://pub.dev/packages/camera
95. pub.dev: mediapipe_core — https://pub.dev/packages/mediapipe_core
96. Microsoft: Announcing TypeScript 7.0 — https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
97. npm: typescript — https://www.npmjs.com/package/typescript
98. Python downloads / releases — https://www.python.org/downloads/
99. PyPI: fastapi — https://pypi.org/project/fastapi/
100. PyPI: pydantic — https://pypi.org/project/pydantic/
101. PyPI: SQLAlchemy — https://pypi.org/project/SQLAlchemy/
102. PyPI: alembic — https://pypi.org/project/alembic/
103. PyPI: pgvector — https://pypi.org/project/pgvector/
104. PyPI: redis — https://pypi.org/project/redis/
105. PyPI: celery — https://pypi.org/project/celery/
106. arq repository (maintenance-only notice) — https://github.com/python-arq/arq
107. PyPI: taskiq — https://pypi.org/project/taskiq/
108. PyPI: anthropic — https://pypi.org/project/anthropic/
109. PyPI: uvicorn — https://pypi.org/project/uvicorn/
110. PyPI: mediapipe — https://pypi.org/project/mediapipe/
111. PyPI: psycopg — https://pypi.org/project/psycopg/
112. PyPI: asyncpg — https://pypi.org/project/asyncpg/
113. PyPI: pydantic-settings — https://pypi.org/project/pydantic-settings/
114. PostgreSQL versions feed — https://www.postgresql.org/versions.json
115. pgvector tags — https://github.com/pgvector/pgvector/tags
116. Redis LICENSE (tri-licence) — https://raw.githubusercontent.com/redis/redis/unstable/LICENSE.txt
117. Redis releases — https://github.com/redis/redis/releases
118. Valkey releases — https://github.com/valkey-io/valkey/releases
119. Google Maven: LiteRT metadata — https://dl.google.com/android/maven2/com/google/ai/edge/litert/litert/maven-metadata.xml
120. PyPI: ultralytics — https://pypi.org/project/ultralytics/
121. npm: react-native-nitro-image — https://www.npmjs.com/package/react-native-nitro-image
122. PyPI: dramatiq — https://pypi.org/project/dramatiq/
123. PyPI: onnxruntime — https://pypi.org/project/onnxruntime/
124. PyPI: executorch — https://pypi.org/project/executorch/
125. npm: expo-speech — https://www.npmjs.com/package/expo-speech
126. npm: expo-haptics — https://www.npmjs.com/package/expo-haptics
127. npm: @mediapipe/tasks-vision — https://www.npmjs.com/package/@mediapipe/tasks-vision
128. Kaggle: Google MoveNet model page — https://www.kaggle.com/models/google/movenet

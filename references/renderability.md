# Renderability: Green/Red Lists, Formats, Model Profiles

What current video models render reliably vs. what fails. Tags and confidence labels: legend in sources.md.

## 1. Green list (reliable)
Single-subject action with one camera move · dialogue in shot/reverse-shot coverage · weather, fog, dust, embers · fire/water/smoke as atmosphere (not as hero physics) · slow reveals · stylized 3D (most forgiving discipline) · high-action anime · UGC/handheld realism · reflections and light rhythm across cuts (Seedance 2.5) · macro/product turns · creatures from image references.

## 2. Red/yellow list (avoid or mitigate)
| Element | Failure | Mitigation |
|---|---|---|
| **In-frame text — unified rule** | Text, logos, subtitles, formulas render as scribble or drift between frames | Default: ALL exact on-screen text goes to post-compositing (officially confirmed by the model vendor's guide). Two documented exceptions: (a) **static short text locked via master plate** — content frozen in the reference image + prompt lock "exactly this one line, frozen and identical in every frame" (production-proven, platforms-models ch. 13b); (b) 🟡 MiniMax H3 has an official quoted-text channel (visible text in double quotes, verbatim, untranslated [MM-off]) and renders UI/text comparatively stably — syntax documented, quality practitioner-rated: test before relying. Dynamic/changing text stays red everywhere. |
| Crowds | Clone extras, melting faces in distance | Multi-variant sheet (production-pipeline ch. 3) with extras as silhouette-distinct CLASSES ("heavy brute" / "light scout") — classes, not outfit variants, kill the clone read; crowds to mid/background; small faces stay unreliable even at high res; fog capped at a stated distance ("visibility 20 m") hides background glitches at army scale (less needed at 4K, still works) [H-off, P25] |
| Hands + fine object manipulation | Finger errors, object morphing | Close-ups only as short single-action beats, cut away before the fine work; the handling invariant is written as a POSITIVE LOCKS line in the ch. 12 structure ("ALWAYS by the handle") — there is no separate CRITICAL block |
| Vehicles/wheels/mechanics | Wrong rotation, illogical mechanics | See rescue paths below |
| Long continuous camera moves | Collapse after several moves (proven in 2.5 too) | One move per shot; cuts instead of tours |
| Instrument fingering, precise sports technique | Approximate only | Frame around it; cutaways |
| Physics as hero (glass shattering exactly, complex fluid pours) | Plausible-but-wrong | Describe end state; hide peak behind cut |
| **Wide shots** (stylized 3D; photoreal crowd scale too) | Scale and distance break at wide range; a flat camera path at constant height/speed leaves characters as dots (vendor-confirmed on Higgsfield's own short and its Hell Grind rebuild) | Open the take on a close/medium of the character and transition into the wide inside the same generation; positions locked by the previs/clay render, not by the wide (pixar-look §10) |
| Faces that must stay blank (silent passengers, listeners with no beat) | Model animates them anyway — micro-expressions, drift | Hide by design with a motivated occlusion: reflective glass, backlight silhouette, hat brim, distance — copy-ready GLASS block in video-prompting 12e |
| **Mirror/reflection beats** where a reflected face or pose must match the subject frame-exactly | Reflected face/pose diverges from the subject; reflection doubled, missing, or lagging a beat behind | 🟡 (derivation, not yet [PP]-tested) Reflections as texture/light — glass, water, wet street, chrome — stay GREEN on Seedance 2.5 (§1). For a story mirror beat: Seedance 2.5 only, static camera, ONE readable face in frame — either the reflection alone (subject from behind / over the shoulder) or the subject alone with the mirror as shape (film-craft §2 frame-in-frame); never subject and reflection both readable; otherwise split subject and reflection across a cut. |

**Feasibility answer ("can this scene be generated?") — fixed shape:** one verdict line (green / yellow with rescues / red), then the SKILL rule-10 risk register as a table: Beat or element | Rating 🟢🟡🔴 | Failure (§2 row) | Rescue (§3) | Decision (keep / rescue / cut — the director's, left blank until they decide). Never answer in prose only and never rewrite the scene silently.

## 3. Rescue paths for red/yellow action elements
- **Fights/multi-person action:** never one long choreography. Decompose into **attack–reaction beats as separate short clips** (attack = clip, reaction = clip), characters locked via references; the EDIT is the fight choreography. Write contacts + settling per beat (video-prompting ch. 14).
- **Stunt that will not generate → shoot it yourself [H-off, P24]:** two bodies in constant contact over a prop (a struggle for a gun in a car: limbs fused, weapon vanishing) would not converge in text; the feature-film fix was stunt performers in a real car filmed on a phone, fed as MOTION reference — the model laid the cast, interior and light over it. One day of phone footage instead of a week of iterations; the only place a text-to-video-only production stepped outside its rule (production-pipeline ch. 8 phone-shot blocking).
- **Dance/choreography move by move [H-off, P48]:** "'dances' means nothing to Seedance" — write the moves: "two head nods, shoulders rolling one at a time, a knee dip, a finger snap, a quarter spin at the door"; per cut one register ("slow head bob left and right" · "sharp footwork, skips, stomps, quick weight shifts" · "locking style, arms snapping into frozen geometric poses" · "wide arms, shoulder isolations, stopping on the beat"); the track as timing input (video-prompting ch. 14b).
- **Vehicles/wheels:** hide wheel rotation — night/rain (motivated motion blur), framing above wheel height, parallel tracking (wheel detail unreadable), cockpit coverage; wheel close-ups only as short beats with water/mud eruption as distraction.
- **Subject vs. camera motion:** never combine opposing directions (subject runs right + dolly-in = mush) — one motion direction dominates per shot.
- **Animals:** short single beats, no long behavior chains; image reference instead of species name for fantasy/hybrid creatures.
- **Moving crowds:** multi-variant sheet + crowd in mid/background layer only; foreground extras directed individually.
- **Crowd scale — never a number, always three layers [H-off, P25]:** "the prompt never says show a thousand samurai": one sharp warrior up front, a dense crowd behind him, silhouettes fading into the mist — about 40 soldiers read clearly and the brain fills in the rest. Pair with the fog cap (§2) and silhouette classes. A synchronised army drop-into-stance is a legitimate held ENDING STATE (formation reads as drilled, not as animation — the async rule applies to individuals, video-prompting ch. 12).
- **Degradation looks as rescue style:** VHS/CCTV/16mm grain has built-in fault tolerance — a footage format (style-control §6b) is a legitimate rescue for risk shots.

## 4. Format matrix (what each look forgives)
| Format | Fit | Note |
|---|---|---|
| **Pixar/stylized 3D** | **Excellent — safest "cinema look"** | Stylization absorbs physics/texture errors; audiences expect no real physics. Look definition and evidence: pixar-look.md |
| High-action anime | Excellent | Speed lines/held poses mask model weaknesses |
| UGC/found footage | Excellent | Degradation hides artifacts |
| Photoreal drama, static dialogue | Good with discipline | Reverse plates + framing recycling mandatory |
| Flat 2D/limited animation | Hard | Punishes every wobble; simple motion only (style-control §5b) |
| Photoreal action with hero physics | Hardest | Plan rescue cuts per risk shot |

## 5. Camera & cut rules
One camera verb per shot · fixed camera grammar per sequence, repeated verbatim · lock positions by previs/clay render or plate, not by the take's opener — the establishing wide is a SHOT, not the opening beat, wherever crowd scale or stylized 3D is involved (open close/medium, arrive at the wide by transition — §2 wide-shot row, pixar-look §10); a plain photoreal two-hander may still open wide · never cross the axis (state it) · match cuts across scene borders bind on identical motion · hectic cuts exactly at hard motion = model hiding failure → reject take.

## 5b. Lighting consistency: directional light vs. whole-body brightness [PP]
🟢 **Directional light and whole-body brightness adjectives on the same object are mutually exclusive.** Once a prompt demands a light DIRECTION, phase, or partial shading on an object (moon phase, backlight, terminator, half-shadow, rim light), never pair it with global brightness words for that same object — "bright", "fully lit", "luminous", "brightly glowing", "strong contrast". Whole-body words grab the entire object and override the phase: documented failure — a moon prompted with a side-lit phase (lit side toward a low sun, shadow side away) PLUS "clear bright lunar disc" rendered as a fully lit disc with no shadow side, physically inconsistent with the stated sun position.
🟢 **Instead:** describe light exclusively per direction — which side/surface is lit, which lies in shadow. If contrast is wanted, name the contrast of the LIT EDGE against the background ("the lit edge stands out against the black sky"), never the brightness of the whole object.
Memory hook: a phase instruction only wins when no contradicting brightness word stands next to it.

## 6. Model quick profiles (for shot assignment)
| Model | Strengths | Limits / slop accent |
|---|---|---|
| **Seedance 2.0** | resolution: native 4K last documented on Higgsfield under HF-CS4-HIST@2026-08 (platforms-models ch. 13 archive, unverified since — working assumption 1080p until the live output dropdown shows 4K), 15-s takes, cost/quality champion, UGC home turf | Peak at take end fails; plastic skin tendency |
| **Seedance 2.5** | 30-s takes (extension chains ≈60 s; 180 s beta is Dreamina-only), 50 refs (30i/10v/10a incl. @Clay Render + voice refs), **edit suite** (region/timestamp-scoped, camera-perspective, green-screen, subject-swap, audio-category — video-prompting ch. 14b), complex continuous camera, choreography with weight, in-shot transformations, multi-stage emotions, reflections, skin texture | ~2× price; resolution platform-dependent (Higgsfield 1080p since Aug 2026, one practitioner aggregator run at 1080p/30 s with sound, Sep 2026 [P19], Dreamina 480/720p; 4K on Higgsfield only via Upscale / FLUX 3 Video Upscaler per HF-WEB@2026-08-31 — no native 2K/4K verified; other surfaces: read the live form); real-face references are rejected by most hosted surfaces (moderation plan + face-grid fallback: post-audio-legal ch. 20); baked-in artifacts → upscaler; logic decays with take length; in-frame text still broken |
| **Veo 3.1** | Polished cinematic realism, environments, ingredients/first-last/extension | Physics-correct motion fights stylized looks |
| **Kling 3.0** | Directed movement, multi-shot storytelling, strongest stylization of the photoreal class, MotionControl | Style drifts per generation → repeat keywords+style ref every prompt; 2–3× rerolls for anime |
| **MiniMax H3 (Hailuo 3)** | 2D/anime line quality, official quoted-text channel + stable UI/text 🟡, LoRA style lock, physics (passes glass test), cheap, native 2K hosted, Ref2VA omni mode (9i/3v/3a), V2V edits without masks, L2VA (events before the image) | Plastic under realism demands [P43], audio loops 🟡 [W], one beat per shot [MM-off], weak IP moderation 🟡 [W] (legally risky) |
| **Grok Imagine 1.5** | Native stylization bias (anime/cartoon/art-directed), fast, cheap, native audio | Drifts cartoonish on photoreal intent; negatives unreliable; Grok Imagine 1.5: 1080p only in specific modes (mode names unverified — read the live selector), 720p otherwise; plan the upscale path unless the receipt shows 1080p |
| **Wan 2.6/2.7** (open-weight family; version per surface) | Open-weight, LoRA, multi-shot, reference-to-video, 1080p, budget | Less polished than top class |
| **PixVerse** | Fast social iteration, transition mode | Not for long-form/high-end. No syntax profile in this skill — if a PixVerse prompt is requested, say so and use the generic ch. 12 block structure with the platform's live docs as the receipt |

⚠️ **Resolution/duration cells above are capability notes, not receipts.** Before any resolution or duration goes into a Render Slate `Settings` row: apply the platform-ui-workflows.md output-configuration rule — use the LOWER verified value for the surface (Higgsfield: 1080p / 30 s under HF-CS4@2026-08-31), ask the user to read the live model/plan dropdown, and write `unverified` in the slate if neither is possible. Never write a reference key you did not check.

No universal winner: run the motion ladder (post-audio-legal ch. 19) per style/model before committing.
⚠️ **Retired/wound down — do not plan pipelines on:** Sora 2 (wind-down 2026) · Runway Gen-3 family (retired Jul 2026) · OpenArt Workflows (sunset Jan 2026). Current surfaces + retirement tracking: platform-ui-workflows.md.

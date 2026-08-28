# Renderability: Green/Red Lists, Formats, Model Profiles

What current video models render reliably vs. what fails. Confidence labels as in pipeline.md.

## 1. Green list (reliable)
Single-subject action with one camera move · dialogue in shot/reverse-shot coverage · weather, fog, dust, embers · fire/water/smoke as atmosphere (not as hero physics) · slow reveals · stylized 3D (most forgiving discipline) · high-action anime · UGC/handheld realism · reflections and light rhythm across cuts (Seedance 2.5) · macro/product turns · creatures from image references.

## 2. Red/yellow list (avoid or mitigate)
| Element | Failure | Mitigation |
|---|---|---|
| **In-frame text — unified rule** | Text, logos, subtitles, formulas render as scribble or drift between frames | Default: ALL exact on-screen text goes to post-compositing (officially confirmed by the model vendor's guide). Two documented exceptions: (a) **static short text locked via master plate** — content frozen in the reference image + prompt lock "exactly this one line, frozen and identical in every frame" (production-proven, pipeline ch. 13); (b) 🟡 MiniMax H3 renders UI/text comparatively stably (single-source claim — test before relying). Dynamic/changing text stays red everywhere. |
| Crowds | Clone extras, melting faces in distance | Multi-variant sheet (ch. 3); crowds to mid/background; small faces stay unreliable even at high res |
| Hands + fine object manipulation | Finger errors, object morphing | Close-ups short; handling invariants as CRITICAL block ("ALWAYS by the handle") |
| Vehicles/wheels/mechanics | Wrong rotation, illogical mechanics | See rescue paths below |
| Long continuous camera moves | Collapse after several moves (proven in 2.5 too) | One move per shot; cuts instead of tours |
| Instrument fingering, precise sports technique | Approximate only | Frame around it; cutaways |
| Physics as hero (glass shattering exactly, complex fluid pours) | Plausible-but-wrong | Describe end state; hide peak behind cut |

## 3. Rescue paths for red/yellow action elements
- **Fights/multi-person action:** never one long choreography. Decompose into **attack–reaction beats as separate short clips** (attack = clip, reaction = clip), characters locked via references; the EDIT is the fight choreography. Write contacts + settling per beat (ch. 14).
- **Vehicles/wheels:** hide wheel rotation — night/rain (motivated motion blur), framing above wheel height, parallel tracking (wheel detail unreadable), cockpit coverage; wheel close-ups only as short beats with water/mud eruption as distraction.
- **Subject vs. camera motion:** never combine opposing directions (subject runs right + dolly-in = mush) — one motion direction dominates per shot.
- **Animals:** short single beats, no long behavior chains; image reference instead of species name for fantasy/hybrid creatures.
- **Moving crowds:** multi-variant sheet + crowd in mid/background layer only; foreground extras directed individually.
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
One camera verb per shot · fixed camera grammar per sequence, repeated verbatim · open takes with a wide establishing to lock positions · never cross the axis (state it) · match cuts across scene borders bind on identical motion · hectic cuts exactly at hard motion = model hiding failure → reject take.

## 5b. Lighting consistency: directional light vs. whole-body brightness [PP]
🟢 **Directional light and whole-body brightness adjectives on the same object are mutually exclusive.** Once a prompt demands a light DIRECTION, phase, or partial shading on an object (moon phase, backlight, terminator, half-shadow, rim light), never pair it with global brightness words for that same object — "bright", "fully lit", "luminous", "brightly glowing", "strong contrast". Whole-body words grab the entire object and override the phase: documented failure — a moon prompted with a side-lit phase (lit side toward a low sun, shadow side away) PLUS "clear bright lunar disc" rendered as a fully lit disc with no shadow side, physically inconsistent with the stated sun position.
🟢 **Instead:** describe light exclusively per direction — which side/surface is lit, which lies in shadow. If contrast is wanted, name the contrast of the LIT EDGE against the background ("the lit edge stands out against the black sky"), never the brightness of the whole object.
Memory hook: a phase instruction only wins when no contradicting brightness word stands next to it.

## 6. Model quick profiles (for shot assignment)
| Model | Strengths | Limits / slop accent |
|---|---|---|
| **Seedance 2.0** | Native 4K (in-platform), 15-s takes, cost/quality champion, UGC home turf | Peak at take end fails; plastic skin tendency |
| **Seedance 2.5** | 30-s takes (extensions to 180 s beta), 50 refs (30i/10v/10a), complex continuous camera, choreography with weight, in-shot transformations, multi-stage emotions, reflections, skin texture | ~2× price; resolution platform-dependent (Higgsfield 1080p since Aug 2026, Dreamina 480/720p; 2K/4K unlock plausible — verify current caps); baked-in artifacts → upscaler; logic decays with take length; in-frame text still broken |
| **Veo 3.1** | Polished cinematic realism, environments, ingredients/first-last/extension | Physics-correct motion fights stylized looks |
| **Kling 3.0** | Directed movement, multi-shot storytelling, strongest stylization of the photoreal class, MotionControl | Style drifts per generation → repeat keywords+style ref every prompt; 2–3× rerolls for anime |
| **MiniMax H3 (Hailuo 3)** | 2D/anime line quality, stable on-screen text/UI 🟡, LoRA style lock, physics (passes glass test), cheap, up to 2K | Plastic under realism demands, audio loops, one beat per shot, weak IP moderation (legally risky) |
| **Grok Imagine 1.5** | Native stylization bias (anime/cartoon/art-directed), fast, cheap, native audio | Drifts cartoonish on photoreal intent; negatives unreliable; 720p cap (1080p in modes) |
| **Wan 2.6** | Open-weight, LoRA, multi-shot, reference-to-video, 1080p, budget | Less polished than top class |
| **Sora 2** | Physics coherence benchmark | Being wound down; don't build pipelines on it |
| **PixVerse** | Fast social iteration, transition mode | Not for long-form/high-end |

No universal winner: run the motion ladder (ch. 19) per style/model before committing.

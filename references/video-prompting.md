# Video Prompting: Block Structure & Sequence Prompting (ch. 12, 14, 15)


Source-tagged knowledge base. Confidence labels: 🟢 multi-source/official/production-proven · 🟡 plausible, single-source or untested · 🔴 marketing claim, verify yourself. Source tags: [A]=platform academy docs, [P1–P18]=practitioner video protocols (archive file), [PP]=first-party production-session evidence, [W]=web research (multi-source), [H-off]=Higgsfield official, [BD-off]=ByteDance official guide (via verified reproductions), [F]=fal.ai official, [R-off]=Runway official, [X-ext]=community skill (partially officially confirmed), [OAI-off]=OpenAI cookbook, [G2]/[NB]=image-model guide clusters.

## 12. The prompt block structure (the core prompt-writing method)

**This is the default way to write any Seedance / Cinema Studio prompt.** It is the officially documented Seedance block system, adopted as our standard because it beats loose prose: each concern has one home, nothing is forgotten, nothing collides. Binding for Seedance 2.0/2.5 and Cinema Studio; for other video models (H3, Kling, Veo, Grok) it is the starting scaffold — adapt block names to that model's syntax (platforms-models ch. 21), keep the ordering logic. Treat the guidance as holding for 2.5 as well as 2.0 unless a model-specific note says otherwise.

**Core principle — write the visible.** The model reacts to what can be seen and measured, not to mood words. Translate every abstraction into something observable: not "tense scene" but "man freezes, slowly clenches his fist, light only from the side, half his face in shadow". Fewer precise words beat many vague ones. Before generating, mentally *watch* the prompt: is the first frame non-empty, is it clear where each subject is and looks, where the light comes from.

**Output is a single standalone prompt in a code block.** Each generation is a blank slate with no memory of other shots — a prompt is a sealed single-shot document. Never carry in scene numbers, script headings, prior-scene summaries, "as above / continues" phrasing, or unused tags/characters/props.

### Block order (use only the blocks the shot needs; drop the rest)
```
SCENE CONTEXT       1–2 sentences: what happens, where, when. Geo-positions of characters.
ACTIVE REFERENCES   @tag + minimal anchor of critical details + "100% matches the reference".
LOCATION MAP        foreground / midground / background; where the camera sits; where light comes
                    from; movement paths. Naturalistic colour can live here.
FIRST FRAME/BLOCKING who is where in the first frame: positions, orientation, gaze. Composition
                    rule for THIS scene.
FORMAT MODE         one continuous shot / sequential cuts / timed multishot (see ch. 14 cuts).
OPTICS              shot size + FOV° per segment + lens character. Multishot: add "no drift mid-segment".
CAMERA              operator behaviour: height, distance, movement, focus; camera-body tonal
                    character as a LOOK, not a model name.
ACTION              events at the precision the shot needs; camera motion and subject motion stated
                    separately; cause before reaction.
PERFORMANCE         (when acting matters) muscle-level emotion, precise eye-line, catch-lights,
                    breath, pore-level skin realism.
PHYSICS             (when it matters) mass, inertia, contact shadows, fluids, particles.
LIGHTING            source, direction, exposure, key/fill, haze — priority block.
COLOR GRADE         (only when the grade is strong/stylised) palette as material + light + role;
                    omit for naturalistic looks and fold colour into LOCATION/LIGHTING.
WARDROBE            (when costume matters) material + condition, scene-logical.
AUDIO               only the needed sound / line (brackets: ch. 12b).
STYLE               technical-style suffix: overall look in words, photoreal, format, grain.
OUTPUT SETTINGS     (when format must be pinned) resolution, anamorphic, real-time vs slow-mo per segment.
POSITIVE LOCKS      short hard fixers against likely failures, restating critical info once;
                    continuity lives here.
```

### The three placement rules that make it work
1. **Nothing style-related opens the prompt.** The prompt starts on SCENE CONTEXT / ACTIVE REFERENCES. **There is no style-prefix block** — style is not one thing in one place; each aspect lives in the block that already governs it (light → LIGHTING, colour → COLOR GRADE or LOCATION, optics → OPTICS, acting/skin → PERFORMANCE, physics → PHYSICS). Only *technical* style (resolution, grain, fps, overall look word) sits as a short suffix stack (STYLE, OUTPUT SETTINGS) just before POSITIVE LOCKS. (This overrides the older "glued style prefix" idea — see style-control §1: prefixes were a single creator's convenience note and are ignored by GPT Image 2 and Seedance in practice.)
2. **CAMERA sits in the 3rd position of the core layer order** (subject → action → camera → style → constraints). Moved to the end, FOV gets ignored; moved to the front, it fights identity. This is a hard ordering rule, not a preference.
3. **A lock is placed next to what it protects** and phrased positively ("headlights stay glowing in every shot"). Write densely where control matters, sparsely where it doesn't; say each important thing once.

If the user supplies their own prefix or block text, use it verbatim.

## 12b. Reference tagging & audio syntax

🟢 **Reference + text split:** the `@tag` image sets appearance and identity; text sets what happens and locks critical details. Both are required. Keep the character description in the prompt MINIMAL — long appearance text conflicts with the image and degrades it. Anchor line format: `@TAG: age + role/build + current state + unique visible features + action-critical details + voice (only if it has a line). 100% matches the reference.`
🟢 State critical details (small text, logos, colour) in words even if they appear on the reference — the model can drop them. **Never place an `@tag` in a shot where that object is not present** — the model forces it into frame.
🟢 **Tag naming:** user's explicit `@tag_name` wins; else by load order (`@image1 @image2…` / `@video1…` / `@audio1…`); tags are not portable across platforms.
🟢 **Mode A** @image-tags by upload order; **Mode B** no tags — describe the visible feature ("the woman with the silver streak").
🟢 **Reference budgets (officially confirmed):** ≤8 image subjects (stretch 9–12), ≤5 video/audio subjects, clips 5–10 s; >5 subjects → single-view images, separate angles, never a collage grid. Trim order when over budget: characters > props > scene > style. (Seedance 2.5: up to 50 references incl. video/audio — still select per scene, "a casting pool, not a shopping list", ch. 14.)
🟢 **Audio bracket syntax:** parentheses ( ) spoken line · < > delivery/tone directions · { } sound effects · 【 】 music/ambience directives. Exclude music by default (production-pipeline ch. 6). Storyboard grids/sheets used as references: exclude their own drawing style and panel borders explicitly. Prompt length: stay under ~5000 characters; every vague word is a coin flip. Generation parameters (ratio, duration, resolution) are platform settings, never prompt text.

## 12c. Quantification doctrine (write measurable, not moody)
🟢 The single highest-leverage habit across all block writing — replace adjectives with units the model can measure:
- **Speeds in km/h:** not "fast/slow" → "moves at 40 km/h", "camera pans at 5 km/h".
- **Atmosphere in %/metres:** not "light fog" → "fog density 40%", "haze visible at 15 metres depth". Atmosphere builds in STEPS across shots (shot 1: 20% → shot 2: 40% → shot 3: 60%).
- **Giant scale via human-height comparison:** not "huge"/"three metres tall" → "stands as tall as four humans stacked head to toe".
- **White balance in Kelvin,** fixed within a scene (3200K / 4000K / 5600K / 8500K), set to scene mood.
- **Left/right is from the camera.** "Subject moves left" = left from the camera's view.
- **Colour tied to material + light beam + compositional role,** never a flat list: not "the woman wears red" → "crimson silk scarf catching the cold tungsten spill from the corridor".
- **Environment interaction stated physically:** snow melts on skin, rain runs down hair, wind moves fabric.
- **Emotion through muscle movement, not labels** (ch. 14 emotion formula). **Equipment as a look, never gear names** — camera/film/lens model names get ignored or break complex moves. **Camera on the shadow side,** operator axis stated. **Background in explicit foreground/midground/background layers.**

## 12d. Optics: shot size + FOV in degrees
🟢 Two levers define how a shot is framed: **shot size** and **focal length**. Write shot size as an abbreviation and focal length as **FOV in degrees** (mm is for thinking, degrees go in the prompt).

**Shot sizes:** ECU (extreme close-up: eyes, button, headlight) · CU (full face) · MCU (head + shoulders) · MS (to the waist) · WS (full figure + surroundings) · EWS (scale, location).

**FOV anchor table — use only these discrete steps (never "23°" → use 18° or 29°):**
| FOV | mm equiv | Purpose | When |
|---|---|---|---|
| 180° | fisheye | spherical distortion | POV, dream-state |
| 107° | 14–16mm | architectural ultra-wide | huge interiors, epic establish |
| 84° | 20–24mm | wide | establish, group blocking |
| 63° | 28–35mm | observational | wide observation, reportage |
| 47° | 40–50mm | neutral human perspective | universal establish, medium |
| 29° | 75–85mm | portrait compression | medium-isolate, dialogue bust |
| 18° | 100–135mm | natural portrait | close-portrait, identity-preserving |
| 12° | 180–200mm | tele-detail | hands, objects, detail-on-wide |
| 8° | 300–400mm | extreme compression | observation, broadcast |

In a multishot, set FOV **per segment** and add "no drift mid-segment".

## 12e. Optical technique patterns (copy-ready)
🟢 **Observation / hidden-camera effect — all three at once:** (1) foreground occlusion out of focus over 20–30% of frame (wall, pillar, branch), (2) atmospheric haze between camera and subject, (3) distance vantage at 8–12° super-tele, operator anchored far away. Change the occlusion type between beats; keep the vantage single.
🟢 **Sports broadcast:** 8° super-tele + handheld 1–2 cm tremor + "anchored at distance, finding the action".
🟢 **Detail-on-wide (snake cam):** 84° wide FOV + low angle right up against a small object — foreground object exaggerated, background recedes.
🟢 **Intimate wide:** 63–84° wide FOV on a close face — face centred, surroundings readable without blur.
🟢 **Tele compressed air column** (8–12°): "dust suspended in the long compressed air column between camera and subject", "heat shimmer compressed into a wall of haze in front of the figure".

## 12f. Special protocols
🟢 **Extreme-FOV multishot (8° or 107°) needs a 4-mechanism consistency stack** or it breaks after 2–3 beats: (1) sequence-wide identity lock — single location reference across all beats; (2) LENS LOCK opener — explicit FOV phrase at the start of each beat; (3) LENS CHECK closer — confirm FOV at the end of the beat; (4) colour via material + light, not a list. All four required.
🟢 **Whip-pan timing:** a whip under 0.8 s renders as a hard cut without blur. Pattern: `0.3s subject A settled → 0.8s WHIP motion-blur transition → 1.4s subject B settled`.
🟢 **Mixed time-speed (real-time + slow-mo):** hard cuts only between speed modes; each shot is ONE speed start to finish.
🟢 **Cracks/breaks without impact (anti-impact lock):** "crowd PRESSES, not strikes" · "fracture originates from edge stress, not centre impact" · "no impact point — pressure-based crack" · sequential timing edge-to-centre, not radial from a point.

## 12g. Adapting the block structure to other video models

The block structure (ch. 12) is Seedance/CS-native. Other models want the same *ingredients* — subject, action, scene, camera, lighting, audio, references — but in a **different block order**, and they disagree on one thing above all: **where the camera goes**. Keep the ch. 12 blocks and their content rules (quantification 12c, FOV table 12d, reference tagging 12b); reorder the opening spine per model. Cross-model camera vocabulary itself is portable (all these models trained on professional film footage); only the ordering and a few model quirks change. [W, multi-source]

**The one rule that flips per model — camera position in the spine:**
| Model | Camera goes | Spine (documented) |
|---|---|---|
| **Seedance / CS** | **3rd** (subject → action → CAMERA → style → constraints) | ch. 12 block order |
| **Kling 3.0** | **FIRST** — lead with the lens, it sets 3D space before anything moves | Camera → Scene → Action → Vibe/Lighting → Time/Audio |
| **Veo 3.1** | **FIRST** — Google's official formula leads on cinematography | Cinematography → Subject → Action → Context → Style & Ambiance |
| **MiniMax H3** | **after action** — lead with the subject's physical action, camera follows | Subject/identity → Scene/time → Action (chronological) → Camera → Lighting/style → Audio → References |
| **Grok Imagine** | **after action**, style-qualifier FIRST | Subject → Action → Camera → Scene → Style → Sound → one Constraint (short verb-led for I2V) |

**Per-model adaptation notes:**
🟢 **MiniMax H3** — official usage-manual framing: `full prompt = reference notes + core idea + scene-by-scene description`. Declare what each uploaded file is for FIRST (@image1/@video2/@audio3 in upload order, cited inline), then subject/place/event/style, then action over time (timestamps optional, platforms-models ch. 21). Audio is a first-class timeline layer, not a suffix: keep spoken words in the `<d>[lang]…</d>` block, describe the voice *outside* it, put physical sound in an overall-soundscape slot and audience music in a separate non-diegetic slot (or N/A for none). The first frame already defines appearance — don't re-describe it. Physical action leads; camera follows the action. [W: official manual via Pixo/Hailuo3/APIDot]
🟢 **Kling 3.0** — camera FIRST is the single biggest lever ("Slow dolly push forward" opens the prompt and sets the 3D space). Then ground the scene, then ONE subject doing ONE clear thing, then vibe/lighting, then time/audio. Anchor identity in the first sentence and reuse the exact descriptor every prompt of a sequence (Kling interprets each generation independently — platforms-models ch. 21). Element budget is version-dependent (2.6: ~5–7 elements, older tiers 3–4) — over-budget prompts overload and morph. Add a motion endpoint ("…then settles back into place") to prevent the 99%-hang failure. [W]
🟢 **Veo 3.1** — Google's official five-part formula leads on cinematography, then subject, action, context, style & ambiance. Multi-shot in one clip via timestamp prompting (`[00:00–00:02] medium shot, [00:02–00:04] reverse shot`). Physics-correct motion fights stylized looks — prompt the motion grammar (platforms-models ch. 21 / style-control §5b). Native audio (SFX line) is Veo-specific; the visual camera language is portable to the others. [W]
🟢 **Grok Imagine (1.5)** — style qualifier at the very START (native stylization bias), then the compact brief: subject + action + camera + scene + style + sound + ONE stability constraint. **I2V is the strong path** (xAI's top-ranked I2V) — when the source still already carries the look, switch to a short verb-led prompt (`"she blinks slowly"`) and let the image carry aesthetics; extra words override what the image already says. Iterate in passes: structure (subject+action+camera) → style (light/color/texture) → stability (constraints) → variants (3 style variants, keep the most stable). Negatives phrase positively where possible; 720p cap → upscale path. [W]

**What stays identical across all models:** the quantification doctrine (12c), the FOV-in-degrees discipline (12d), reference-tag-then-address (12b), one main action + one camera move per shot, cause-before-reaction, and "write the visible". Port those unchanged; only reorder the spine and respect each model's camera-position and audio-handling quirk.

## 14. Sequence prompting (the generation unit)
**Doctrine: write shot-first, prompt sequence-first.** The sequence (take of 2–3 internal shots) is the generation unit; state chains across takes.

🟢 **fal 9-part production note:** FORMAT (ratio/duration handled by platform) → REFERENCE MAP (one job per reference) → GLOBAL STYLE → TIMELINE (time-ranged beats) → CAMERA → AUDIO → CONSISTENCY anchors → **ENDING STATE** (explicit final frame description — the next take's start) → CONSTRAINTS. [F]
🟢 **State chaining:** every take's prompt begins from the previous ENDING STATE ("continue forward, do not replay"); harvest the final frame as the next start frame.
🟢 **Cause before reaction:** contact → movement → sound → reaction as separate ordered actions.
🟢 **Occlusion continuity:** if a subject passes behind something, state that it re-emerges unchanged.
🟢 **Negative rule (revised — official docs overruled the earlier strict taxonomy):** negations are established practice in official sources, BOTH kinds: procedural prohibitions ("no cuts, no slow motion, no duplicated props, no speed-ramps") AND content exclusions ("no subtitles, no logos, no music", "NOT plastic", "NO blood") — evidenced in fal prompts with shown results, Runway official examples, the ByteDance guide ("**Omission is not a reliable negative instruction** — unwanted elements MUST be named"), and Higgsfield's official CS production prompts. Remaining caution where positive-only still holds: (1) **image generators/stills** — negations process unreliably; describe materials positively ("matte, powdery, light-absorbing" instead of "no reflections"); (2) **negated emotion/state descriptions in Seedance 2.0** ("he's not crying" → documented confusion). Motto: **prohibitions and exclusions may be negative; descriptions of appearance and emotion stay positive.** Scope: proven for Seedance 2.5 (API/Dreamina/Runway); untested for Cinema Studio 4.0 specifically — 🟡 there until your own test run. [H-off, F, R-off, BD-off; overrules the P1 generalization]

### Official ByteDance guide additions [BD-off]
🟢 **Base formula (6 elements, 4 lines):** [Subject] performs [action] in [scene]. / The visuals feature [style]. / Use [shot size, angle, movement, cuts]. / Audio includes [dialogue, ambience, SFX, music]. Drop unused lines; generation parameters stay out.
🟢 **Casting system for many references:** group blocks [Characters]/[Props]/[Scenes]; write every mapping individually ("<Conservator> corresponds to @Image 1. Use only appearance, hairstyle, clothing.") — collective mappings ("@Images 1–4 define four characters respectively") bind nothing. "Do not interchange their appearances." Declare prop ownership ("belongs only to <X>"). ONE profile per recurring character incl. a do-not-use line; **select references per scene** — "Fifty references is a casting pool, not a shopping list."
🟢 **Stage format** (official; matches state chaining): [Generation Goal] → [Stage N: Initial state / Primary event / End state] → [Maintain Consistency]. ONE main change per stage.
🟢 **Timing patterns:** range (budget) / exact point (one critical beat) / **relative** ("three seconds after he presses the button…"). Ranges consecutive, non-overlapping; three actions in one second don't work.
🟢 **Edit format:** [Edit Goal] / [Source Video Role: "@Video 1 is the sole editing master"] / [Edit Scope] / [Content to Preserve]. **Subject swaps must inherit the original timeline** (write out every entrance, movement, occlusion, exit with identical timing/path/tempo). Audio edits as their own instruction. Edit inherits ratio + duration (±0.3 s); source clip <20 s + 1–5 ref images.
🟢 **Extension rules:** describe the boundary frame BEFORE the new action. Backward guard: mark materials that belong ONLY to the original clip, or later figures/props appear too early; "connect to the source video" is not enough — write the source's start frame as an explicit end state.
🟢 **First/last frame & keyframes:** name each anchor separately (combined mention binds neither); both images same ratio or stretch. Multi-keyframes: "use @Image 1 through N as keyframes in this order" + state per image; **separate images beat grid collages**. 3D blockouts: rough = timing/blocking/camera/cut points (map every gray shape by name), fine = re-render with held structure; **remove path lines, axes, camera frustums beforehand — they get rendered.** 3D whitebox is its own reference type: lay out set + camera path before the first render.
🟢 **Emotion formula:** trigger → immediate visible reaction → gradual shift (eyes/brows/mouth/breath/gaze/hand) → settled; 2–4 cues suffice; chain multiple shifts to events.
🟢 **Translate camera technique:** keep the term AND write the visible change ("Rack focus: … leaves gradually blur while the face changes from soft to sharp"); dolly zoom/bullet time/speed ramp need defined parameters.
🟢 **Language pattern:** language → regional variety/accent → delivery → speaker → line; "authentic Los Angeles English" beats "English". Restate the language if the model switches.
🟢 **Precision limits (official):** timestamps = budgets; edits without frame guarantees; seamless transitions = continuity, not pixel identity; **subtitles, formulas, signage, product specs that must be exact → post-compositing.**

### Aggregator/community confirmations
🟢 Review in separate passes (identity → continuity → timing → camera → audio); **fix the weakest instruction first**; score adherence before polish; the correction belongs in the NEXT prompt, not only in post. Endings need their own time range; drift in the second half → reduce events + restate the anchor at the failing transition.
🟡 Prompt pack as a constant benchmark: identical brief + references across platforms/models for fair comparisons.

## 15. Style enforcement & reference integration
Fully externalized to **`style-control.md`** (style stack hierarchy, model-specific mechanics for GPT Image 2 / Nano Banana Pro / video models — incl. the production-proven 4-section Pixar prompt structure in §2 — 15 style vocabularies, footage/era/optics styles, reference integration protocol, diagnosis). Read that file for ANY stylized-look task and whenever writing prompts that use references.


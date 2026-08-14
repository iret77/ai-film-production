# Production Pipeline & Prompting Doctrine

Source-tagged knowledge base. Confidence labels: 🟢 multi-source/official/production-proven · 🟡 plausible, single-source or untested · 🔴 marketing claim, verify yourself. Source tags: [A]=platform academy docs, [P1–P16]=practitioner video protocols (archive file), [W]=web research (multi-source), [H-off]=Higgsfield official, [BD-off]=ByteDance official guide (via verified reproductions), [F]=fal.ai official, [R-off]=Runway official, [X-ext]=community skill (partially officially confirmed), [OAI-off]=OpenAI cookbook, [G2]/[NB]=image-model guide clusters.

## 1. Pipeline principles
🟢 **Stills-first:** every shot exists as an approved still (start frame) before any video generation. The look is won in the image; video inherits it. Cheap iteration happens at the image stage.
🟢 **Order: location plates → characters → props → composite stills → motion tests → production takes.** Characters are shot INTO approved plates, never invented alongside them.
🟢 **Review loop:** generate → review against acceptance criteria → fix the weakest instruction in the NEXT prompt (not only in post) → regenerate. Worth knowing: a defect accepted at the still stage propagates into motion, so a still that is "close enough" often costs more later — the user decides when it is good enough to move on.
🟢 **Sheets vs. in-scene stills:** reference sheets (neutral light) maximize consistency; in-scene stills (scene light) maximize realism. Both exist; sheets feed identity, in-scene stills feed the take.
🟢 **Label discipline:** every asset gets a stable ID (@name) reused verbatim in prompts, filenames, and the continuity ledger (ch. 19).

## 2. Script & treatment for generability
🟢 Write the script in stages: logline → ~10 candidate synopses (cheap ideation, pick one) → treatment → shot-level script. At each stage, run a renderability pass (renderability.md) and cut or rescue red elements — rescue cuts are a writing tool, not a defeat.
🟢 **Complexity budget per take:** one primary event per shot; 2–3 shots per 15/30-s take with explicit labels ("Shot 1/2/3") and HARD CUT markers.
🟢 Open on a hook (first 2 s earn the rest); write endings as their own beat with its own time range.

## 3. Characters
🟢 **Minimal sheet:** front, side, back, face close-up, clothing detail — one character per image, neutral even light, plain background. 🟢 Official course variant: a 3-view sheet (full-body front, full-body back, frontal close-up) generated FROM a reference photo on a grey background — the close-up is what locks the face. 🟢 **Defensive anatomy locks are official practice:** character prompts carry insurance lines ("Both arms whole and both hands normal, intact human hands — no missing limbs") and anti-sheen skin lines ("skin matte and low-sheen — no oily highlights, no specular hotspots") — pre-empting the two most common character defects. [H-off Stage 2] **One-face rule:** exactly one canonical face; never let a second "almost right" face into any reference set.
🟢 **State sheets:** any persistent change (wet, wounded, dirty, costume change) is a NEW sheet order, never a prompt adjective. The ledger (ch. 19) tracks which state sheet each shot uses.
🟢 **Anti-drift ladder:** (1) sheet as reference in every generation, (2) verbatim identity anchor line in every prompt, (3) frame-harvest a well-liked generation as an additional reference, (4) if drift persists: regenerate the sheet, don't patch outputs.
🟢 Voice: the sheet locks the voice along with the face on audio-capable models — accept the native voice where it fits; otherwise replace via the voice pipeline (ch. 18).
🟢 **Crowd sheet:** one multi-variant sheet (6–12 distinct extras) referenced for background population — prevents clone crowds.

## 4. Locations & props
🟢 Per location: one master wide plate + 2–3 detail plates at ONE shared exposure/palette. **Reverse decision up front:** does this location need counter-angles (dialogue, cross-room action)? → build the multi-plate set (ch. 13). Pass-through/B-roll → one wide suffices. Missing reverse plates ordered late are the most expensive single mistake in the pipeline (ch. 16).
🟢 Props with narrative state changes get a **state pair/series of stills** (before/after), treated like character state sheets.
🟢 Screenshot workaround: frames from an approved video generation are legitimate (often superior) plate sources — they carry light and geography correctly.

## 5. Image model selection
| Model | Use for | Notes |
|---|---|---|
| Soul Cinema | Photoreal characters/locations from scratch | Cinematic default; not the stylization specialist |
| **GPT Image 2** | Stylized plates/sheets, reverse angles WITH layout-map input, structured/text-dense assets | Reasoning model; style-block-first mechanics → style-control §2 |
| Nano Banana Pro | Style transfer with identity lock, multi-character scaffolding, manga pages, edits | Style-medium-LAST mechanics → style-control §3 |
| Seedream | Edits with texture preservation | |
| Midjourney | Discovery/moodboards | Not a pipeline production tool |

### 5b. Higgsfield UI object model ⚠️ version-volatile (verify in app)
🟢 Assets live as **Elements** (characters/locations/props) scoped to the project, pulled via @tags; a **Scene** = hero shot composed from elements → becomes the start frame; save explicitly. 🟢 **Exact-name rule:** add each asset under Elements with EXACTLY the tag name used in script and prompts — scene generation auto-matches inputs by these tags; a name mismatch silently unbinds the reference. [H-off] Director panel applies settings at generation time (ch. 13). AI Cast builds reusable actors (genre, era, archetype, physique, outfit, distinguishing details). Multi-shot auto/manual. Documented against the 2.5-era UI; 4.0 keeps the model but renames/extends — check the live UI before writing UI-dependent instructions.

## 6. Video prompting basics
🟢 **Keep list (officially rewarded):** subject specificity, active verbs with direction/speed, scene with time-of-day/weather, ONE committed visual style, one camera verb per shot, audio always described.
🟢 Choreography beats adjectives: write micro-cues (eyes, brows, mouth, breathing, hands) instead of emotion labels; cause before reaction (contact → movement → sound → reaction) — never leave the causal link to the model.
🟢 Timestamps are pacing budgets, not frame guarantees; a timestamped beat = short take.
🟢 **Position lock:** state where every subject starts, faces, and ends.
🟢 **Audio:** describe diegetic sound naturally; **always exclude music** ("original fictional score" only where a score is wanted as diegetic; the real score is built in post, ch. 18).

## 7. Dialogue scenes
🟢 **Framing recycling:** exactly two repeated framings (single ↔ over-shoulder); "shot 3 repeats shot 1's framing" — repetition is what sells coverage.
🟢 Reverse-environment references are mandatory (multi-plate, ch. 13); **180° lock:** name the axis and forbid crossing it in every dialogue prompt.
🟢 One line per shot beat; speaker tags per platform syntax (ch. 12/21); never two characters speaking simultaneously.

## 8. Geometry inputs (when language won't pin space)
🟢 Ascending: **layout map** (top-down schematic generated as an image, fed as reference) → annotated sketch → arrow annotation on a plate → camera-path line drawing. "One drawing tells the model what 10 sentences can't." Remove any helper geometry you don't want rendered (ch. 14).

## 9. Alternative production paths
🟢 **Storyboard-to-sequence:** a clean storyboard grid (<15 panels, clean line art, minimal text, stated reading order, grid style excluded) drives a sequence at ~70–80% adherence — cheap pre-viz, not final control. **Higgsfield Popcorn** is the platform's sequence-aware storyboard generator: Auto (one prompt → arc) or Manual (per-frame direction), up to 8 frames/run, longer arcs via bridge-frame chaining (last frame = next run's reference), 1–4 reference inputs, export toward video models. [H-off]
🟢 **VFX hybrid:** shoot real plates, generate elements/extensions; and the inverse **restyle path** (live footage as motion scaffold → full style transfer) — style-control §5b.
🟢 **Extension chains:** forward/backward extension to build beyond single-take limits (2.5: toward 180 s beta) with the guards from ch. 14; long single generations (60 s+) only for montage content, not held scenes.
🟢 **Audio-to-video:** a finished audio track (dialogue/music beat) as timing skeleton for generation where supported.

## 10. QA & slop control
🟢 **Four slop tells:** plastic/waxy skin · drifting faces between cuts · AI shimmer on texture · hectic cutting exactly at hard motion (model hiding failure). Any tell = reject take.
🟢 **Batch protocol:** generate 4, watch ALL fully (failures teach the next prompt), review in the separate passes of ch. 19.
🟢 **Keeper phases:** draft tier for exploration → standard tier only for near-final prompts → hero renders last.
🟢 **Resolution ladder:** iterate at 480/720p, render finals at target resolution; judge an upscaler on one exported frame before batch-processing (ch. 17).

## 11. Model choice inside the Seedance family
🟢 "2.5 is a .5 improvement, not a revolution" — choose PER SHOT: 2.0 for UGC realism, cost efficiency, validation drafts; 2.5 for long takes, choreography with weight, in-shot transformations, multi-stage emotion, reflection-heavy scenes, slow controlled camera moves (2.0 overshoots the subject). Mini/Fast tiers for drafting only.

## 12. The prompt block structure (the core prompt-writing method)

**This is the default way to write any Seedance / Cinema Studio prompt.** It is the officially documented Seedance block system, adopted as our standard because it beats loose prose: each concern has one home, nothing is forgotten, nothing collides. Binding for Seedance 2.0/2.5 and Cinema Studio; for other video models (H3, Kling, Veo, Grok) it is the starting scaffold — adapt block names to that model's syntax (ch. 21), keep the ordering logic. Treat the guidance as holding for 2.5 as well as 2.0 unless a model-specific note says otherwise.

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
🟢 **Audio bracket syntax:** parentheses ( ) spoken line · < > delivery/tone directions · { } sound effects · 【 】 music/ambience directives. Exclude music by default (ch. 6). Storyboard grids/sheets used as references: exclude their own drawing style and panel borders explicitly. Prompt length: stay under ~5000 characters; every vague word is a coin flip. Generation parameters (ratio, duration, resolution) are platform settings, never prompt text.

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
🟢 **MiniMax H3** — official usage-manual framing: `full prompt = reference notes + core idea + scene-by-scene description`. Declare what each uploaded file is for FIRST (@image1/@video2/@audio3 in upload order, cited inline), then subject/place/event/style, then action over time (timestamps optional, ch. 21). Audio is a first-class timeline layer, not a suffix: keep spoken words in the `<d>[lang]…</d>` block, describe the voice *outside* it, put physical sound in an overall-soundscape slot and audience music in a separate non-diegetic slot (or N/A for none). The first frame already defines appearance — don't re-describe it. Physical action leads; camera follows the action. [W: official manual via Pixo/Hailuo3/APIDot]
🟢 **Kling 3.0** — camera FIRST is the single biggest lever ("Slow dolly push forward" opens the prompt and sets the 3D space). Then ground the scene, then ONE subject doing ONE clear thing, then vibe/lighting, then time/audio. Anchor identity in the first sentence and reuse the exact descriptor every prompt of a sequence (Kling interprets each generation independently — ch. 21). Element budget is version-dependent (2.6: ~5–7 elements, older tiers 3–4) — over-budget prompts overload and morph. Add a motion endpoint ("…then settles back into place") to prevent the 99%-hang failure. [W]
🟢 **Veo 3.1** — Google's official five-part formula leads on cinematography, then subject, action, context, style & ambiance. Multi-shot in one clip via timestamp prompting (`[00:00–00:02] medium shot, [00:02–00:04] reverse shot`). Physics-correct motion fights stylized looks — prompt the motion grammar (ch. 21 / style-control §5b). Native audio (SFX line) is Veo-specific; the visual camera language is portable to the others. [W]
🟢 **Grok Imagine (1.5)** — style qualifier at the very START (native stylization bias), then the compact brief: subject + action + camera + scene + style + sound + ONE stability constraint. **I2V is the strong path** (xAI's top-ranked I2V) — when the source still already carries the look, switch to a short verb-led prompt (`"she blinks slowly"`) and let the image carry aesthetics; extra words override what the image already says. Iterate in passes: structure (subject+action+camera) → style (light/color/texture) → stability (constraints) → variants (3 style variants, keep the most stable). Negatives phrase positively where possible; 720p cap → upscale path. [W]

**What stays identical across all models:** the quantification doctrine (12c), the FOV-in-degrees discipline (12d), reference-tag-then-address (12b), one main action + one camera move per shot, cause-before-reaction, and "write the visible". Port those unchanged; only reorder the spine and respect each model's camera-position and audio-handling quirk.

## 13. Higgsfield Cinema Studio
### Settings reference (official; ⚠️ documented from the 3.5 tutorial — 4.0 extends palettes to 50+ and adds Era + Emotion Wheel; option names may shift, verify in app)
Guiding principle, verbatim: "**The prompt describes what happens. The settings describe the world it happens in.**" Every setting answers a question the model would otherwise answer itself.

| Setting | Options (exact, 3.5 base) |
|---|---|
| Genre | General (neutral) · Action (camera tied to moving subject) · Epic (scale, environments as protagonists) · Drama (camera as witness) · Comedy (air in framing) · Horror (uncomfortable angles, withholding light) · Noir (shadow logic) |
| Color Palette | Auto · Naturalistic Clean · Bleached Warm · Hyper Neon · Teal & Orange Epic · Sodium Decay (thriller anxiety) · Cold Steel (military/noir/sci-fi) · Bleach Bypass (war/gritty) · Classic B&W — 4.0: 50+ palettes |
| Camera MoveSet Style | Auto · Classic Static ("Hitchcock") · Silent Machine ("Fincher") · One Take ("Lubezki") · Epic Scale ("Hoytema"/IMAX) · Intimate Observer ("Sean Baker") · Impossible Camera · Documentary Snap · Raw Chaos ("Greengrass") · Dreamy Flow ("Doyle") |
| Lighting | Auto · Soft Cross (90° side, half face in shadow) · Overhead Fall (crown-lit, eyes shadowed — temples, high rooms) · Contre-jour (backlit halo — sunsets, romance) · Window · Practicals (ONLY in-frame sources, no hidden fill — candles, explosions, headlights) · Silhouette |
| Camera | Raw 16mm (real stock grain) · Fine Film (35mm warmth) · Clean Digital |
| Lens | Auto · Clinical Sharp · Extreme Macro · Anamorphic (oval bokeh, horizontal flares) · Warm Halation · Vintage Haze |
| Focal Length | 8 · 14 · 35 · 50 · 75 mm |
| Aperture | f/1.4 Wide Open · f/4 Moderate · f/11 Deep Focus |
| 4.0 additions | Era (decade selector: grain/grade/lens auto-adjust) · Tempo (Chaotic/Dynamic/Calm/Single Shot) · Emotion Wheel (8+ types incl. anger, joy, fear, trust — per @character tag; ⚠️ full type list not published) |

🟢 **Preset choice is causal, not aesthetic:** the wrong lighting preset feeds the model wrong world information (lavender field + Overhead Fall = parking-lot look; candle scene + Soft Cross = hidden fill destroys the atmosphere). Practicals for any scene whose light lives IN frame.
🟢 Official settings recipes as starting points: war = Action + Bleach Bypass + Raw Chaos + Practicals + Fine Film + Clinical Sharp 14mm f/4 · rally chase = Action + Cold Steel + Raw Chaos + Practicals + Fine Film + Anamorphic 14mm f/4 · epic fantasy = Epic + Teal & Orange Epic + Epic Scale + Contre-jour + Fine Film + Anamorphic 35mm f/4. FAQ rules: portrait → 50/75 mm; landscape → f/11.
🟢 **Dials before prompt:** camera, optics/aperture, light, color, tempo go into SETTINGS; the prompt carries scene, action, reference roles, timeline, continuity. Avoid double control (settings AND prompt text) — conflicts.
🟢 **Style anchor duty for stylized looks:** CS and Seedance default to photorealism; Pixar/cartoon/anime must be anchored actively — look-carrying references AND/OR an explicit style anchor; weak anchoring tips into photorealism (full mechanics: style-control).

### CS 4.0 platform (official pages, Aug 2026)
🟢 **Multi-model support** — engine chosen PER SHOT (Seedance et al. run natively; UI reports also name Higgsfield Native, Kling, Sora, Veo) — the ch.-11 selection matrix maps directly onto the UI. **Montage Pacing** ("cuts, rhythm and flow built in — no timeline, no post"). **Mr. Higgs / Personal Assistant** (the 3.5 docs' "Claude Chat"): picks camera/light, writes prompts with real @tags, breaks scripts into shots — never triggers Generate itself. **Subfoldering** (scenes/versions/deliverables for 200-shot productions), **Canvas**, team layer (live co-directing, shared elements), **Color Grading** as a fine-tune pass. Credits by length × resolution × model.
🟢 Specs — resolution is a MOVING TARGET, documented states: launch blog (Aug 2026) said up to 30 s / max 720p; **platform update later in Aug 2026: Seedance 2.5 inside Higgsfield now renders 1080p**; the product page additionally claims native 4K and up to one minute (partly unverified). Since Seedance 2.5 is technically 4K-capable, a later 2K/4K unlock on Higgsfield is plausible — the cap is a platform resource/cost decision, not a model limit. 🟡 Agents: **web-verify the current resolution tier before planning any resolution pipeline.** Constant: up to 50 references, forward/**backward** extend, 30+ camera presets. The verified native-4K route today remains Seedance 2.0 direct (`seedance_2_0, 21:9, 4k`).
🔴 Marketing claims, test yourself: "anti-slop camera pipeline" (no plastic skin, no drifting faces, no AI shimmer) and AI-Cast/location persistence ("same street, same weather, next week") — advertising only; validate against the proven drift rules (ch. 3/6).

### Official prompt patterns (from published production prompts)
🟢 DoP names as legal style references ("References in spirit, fully original execution: Deakins, Hoytema…") · ABSOLUTE ANTI-IP block as a standard section (generic settings, no insignia/logos, original score, "all on-screen text in POST") · percentage color distribution (60/30/10) · keyframe placeable mid-sequence ("Reproduce the KEYFRAME composition EXACTLY at Shot 3 — BUT his action is changed: …") · CRITICAL handling blocks for standing invariants ("ALWAYS by the HANDLE, NEVER on the blade").
🟢 **Multi-plate set for dialogue:** @room1 master + @room2 reverse + @room3 detail — "three angles of ONE set at ONE shared exposure"; the axis (180° line) named in every prompt.
🟢 **Master-screen trick** for locked in-frame text: freeze the text in the reference plate, lock via prompt ("exactly this one line, frozen and identical in every frame") — the plate-locked exception of the unified text rule (renderability §2).
🟢 **Locked prompt template of the official prompt-builder skill** (`/higgsfield-seedance-prompt`): scene context → references → shot-by-shot action → lighting → locks; audio always real-world sound only, music added in the edit. Invocation is a natural-language scene brief with @tags ("@hero is searching @loc_cabin … finds @map_prop …") — the skill expands it into the full schema. One prompt covers a whole beat: cuts, dialogue line, and sound from a single generation. [H-off Stage 3]
🟢 **Official zero-motion / rack-focus block** (copy-ready camera language): "The camera stays planted in one immovable position from the first frame to the last. Zero motion — no drift, no shake, no breathing, no stabilization float, no micro-drift. Hold sharp on [plane A — the far anchor]; then rack once to [plane B — the near subject]; then follow focus on the subject if they move toward the lens. The rack is slow, smooth and continuous with no hunting and no overshoot; the follow focus tracks without breathing." — the pattern for static dialogue/tension shots. [H-off Academy]
🟢 **BEAT structure** for takes: numbered beats with time ranges, one primary event each.
🟢 Negations of both kinds are official CS practice — governed by the revised negative rule in ch. 14.

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
Fully externalized to **`style-control.md`** (style stack hierarchy, model-specific mechanics for GPT Image 2 / Nano Banana Pro / video models, 15 style vocabularies, footage/era/optics styles, reference integration protocol, diagnosis). Read that file for ANY stylized-look task and whenever writing prompts that use references.

## 16. Perspective changes & coverage (cost-ranked)
**Core problem:** image models lack true spatial understanding — free-text reverse/new-angle stills of the same scene are unreliable. Video models switch angles reliably WITHIN a take. Hence the ladder — cheap/reliable to expensive/risky; exhaust each rung first:

**Rung 1 — angle changes inside the generation (default):** new angles as **internal shots of the same take** (ch. 2 labels, HARD CUTs) — the model holds set and figures because it builds them in one context. Dialogue: framing recycling (ch. 7). By far the cheapest reliable coverage.
**Rung 2 — harvest angles from existing video:** screenshots from a successful generation are the best references for follow-up angles (light, palette, geography already correct); last frame + "continue forward, do not replay". 🟡 2.5 camera-perspective editing (officially announced, practice-unconfirmed); same class: Runway Aleph "generate new camera angles" on real footage.
**Rung 3 — dedicated image tools instead of free-text reverse:** when an angle is needed as a STILL: never "same scene from behind" via free text — use purpose-built tools (below) or GPT Image 2 WITH a layout map/master plate as input. Reverse test afterward: anchors, openings, light side, palette must match the master plate. Planned dialogue sets: pre-produce the multi-plate system (ch. 13) — 2–3 plates save dozens of failed generations.
**Rung 4 — geometry inputs** (ch. 8) when nothing pins.
**Per location, worth deciding up front:** whether it needs reverse angles (ch. 4) — settling it early is cheaper than discovering it mid-production, but it stays the user's call.

### Higgsfield tools for perspective (verified) [H-off]
🟢 **Angles** (Apps): change the camera angle of any image — full 360° incl. behind the subject; "generate from all angles" = 12 perspectives in one batch. THE tool for reverse plates.
🟢 **Shots** (Apps): one image → storyboard coverage; walks around the subject and **preserves the original's style/grading**. Best input 3:4/4:3 for the widest angle range.
🟢 **Popcorn** (storyboard generator): sequence-aware frames with held identity/lighting — usable as an angle/coverage explorer before committing plates (ch. 9).
🟢 **DoP** (Video Tools): a camera-motion-trained model with 100+ presets. Two rules: (1) the line "**preserve the original face, lighting, and geometry**" goes into the prompt; (2) pick the preset in the app AND repeat the move in prompt text. One main move per clip.
🟢 **Start & End Frame:** lock both ends as images; the platform animates the path — perspective change as a controlled move between two known framings instead of a lottery.
🟡 **WAN Camera Control / Multi-Axis:** physics-based camera paths; CS allows stacking up to 3 moves — ⚠️ conflicts with the proven one-move rule; stack only with test budget.

## 17. Post-production & delivery
🟢 **Upscale ladder:** (1) bring the source still to max quality BEFORE video generation (a 4K start frame gives the model detail budget). (2) Video upscaling as its own pass: Topaz Video AI is reference class; model by material: **Astra for AI-generated video**, Proteus generic, Iris faces, Starlight heavy degradation, Apollo/Aion interpolation/slow-motion. Alternatives integrated in Resolve/Premiere; open-source Video2X/Real-ESRGAN. Judge one exported frame before batch renders. [W]
🟢 **Grading as the final pass** over the edited film (not per clip) — unifying palette/contrast is the strongest single lever against the "assembled" feel.
🟢 **Exposure matching across generations:** shared master plates + identical Kelvin/exposure lines in every prompt of a location (ch. 13 schema) keep takes gradable; residual mismatch is normal and belongs to the grading pass — never re-generate for exposure alone.
🟢 **Trim rule:** AI clips have soft starts/ends — trim the first and last ~0.5 s per clip. [H-off]
🟢 **Master strategy:** master at highest available quality (ProRes/H.265 high bitrate); derive deliveries. Archive original generations + final prompts (re-render capability).
🟡 **Format strategy:** fix the master aspect ratio BEFORE production; plan multi-format derivation (3:4/4:3-near sources allow the widest crops); compose critical content inside the tightest target crop's safe area. Ratio is a platform setting, never prompt text.

## 18. Audio post: music, SFX, voices
🟢 **Three legitimate music paths** (choice = rights question, not just sound):
1. **Self-produced** — DAW/composition route incl. AI-assisted vocal/instrument synthesis (e.g. ACE Studio): full rights, full control, score composed to picture. Cleanest path for ambitious projects.
2. **Classically licensed** — library/stock music or commissioned score with sync license.
3. **Generative** (Suno, Udio, ElevenLabs Music, Stable Audio 3, AIVA) — with licensing caution: paid plans grant a **usage license to the output, not copyright ownership**; free tiers exclude commercial use; the legal landscape is in motion (label suits/settlements). Licensing-first options: ElevenLabs Music and Stable Audio 3 (licensed training data; Stable Audio adds an SFX model and open weights), AIVA for orchestral/MIDI export. ⚠️ Udio is currently a walled garden (downloads disabled). Read the terms BEFORE any commercial release. [W]
🟢 **MiniMax Music 3 (open-weights release Aug 2026):** creative concept + optional lyrics → a complete, structurally coherent song up to 5 min in one generation, 32 kHz/16-bit stereo; hybrid architecture (8B global LLM initialized from Qwen3-8B modeling long-range song structure + a second LM + continuous synthesis stage); design focus: sustained expressive intent across the full track, physically realistic instruments, vocals that read as performed rather than synthesized. Hosted API: `music-3.0` at $0.15/generation (up to 5 min), `music-3.0-free` at 3 req/min, lyrics generation $0.01 — the lowest published per-track price of current frontier music vendors. Family tools: Music 2.5 adds paragraph-level structure control (14+ tags: Intro/Bridge/Hook/Build-up…) and instrumental-only mode; a dedicated cover/remix model reworks 6-s–6-min reference audio with automatic ASR lyric extraction — rights in the source material are YOURS to clear. **Open weights = pipeline ownership** (runs in ComfyUI — the music equivalent of Wan on the video side). ⚠️ Licensing story is thin (training-data provenance undocumented) — apply the same commercial caution as the rest of this bucket. 🟡 Availability on aggregators (Higgsfield, fal & co.) is expected but unverified at time of writing — check current hosting before planning. [W: official MiniMax research blog + ComfyUI + API docs]
🟢 **Score rule:** never generate music inside the video model (ch. 6) — the score is built over the edited film; the music on the timeline then dictates re-cut needs. Diegetic sound comes from generation; fill gaps via SFX libraries or SFX generators.
🟢 **Voice consistency as a system:** per character one **voice profile** (description in the prompt sheet + where available a cloned/saved voice, e.g. a voice library) instead of re-rolling voices per shot. Accept the native generation voice where it fits (the sheet locks it); for control: re-record the dialogue track via TTS/voice clone and replace in the edit — lip-sync realignment via dedicated tools when on-camera. Expressivity: stability low for character delivery (~0.25), mid for narration (~0.4); always the newest speech model (older ones sound flatter). 🟢 **Voice-changer path for character voicing:** perform the line YOURSELF (timing, emphasis, emotion = directing work) and convert via speech-to-speech into the character voice — preserves intonation and cadence, beats pure TTS for acted scenes; multiple characters from one performer are possible. [W]
🟢 **Non-English dialogue / dubbing:** two classes — audio dub (voice + timing preserved, NO lip sync: fine for animation/off-camera) vs. video dub with lip-sync realignment (needed on-camera). Voice cloning only with documented consent.
🟢 **Audio finishing:** loudness-normalize the final mix to the target platform — streaming/online typically **−14 LUFS integrated** (YouTube/Spotify class), EU broadcast **−23 LUFS (EBU R128)**, true peak ≤ −1 dBTP; mix dialogue first, then SFX/ambience, score last; keep stems (dialogue/SFX/music) exported separately for fixes and dubs. [established standards]

## 19. Continuity supervision & sign-off templates
🟢 **Continuity ledger as a mandatory document** (the script-supervisor role): one table across all shots — character state (which state sheet), key props (whose hand, what state), time of day/weather, light direction, screen direction per character, emotional state (what the character just experienced). Check against the previous row before every generation; a state change spawns a sheet order (ch. 3), never a prompt wish.
🟢 **Anchor discipline:** non-negotiable details as short, verbatim-identical anchor sentences early in EVERY prompt; reinforce drifting details in the next prompt instead of patching in post.
🟢 **Copy-ready checklists:**
- **Still sign-off (before motion test):** identity = sheet? · light motivated + direction noted? · no 3D-game look? · material doctrine met? · reverse need settled? · target-crop safe area clear?
- **Take sign-off (batch of 4, watch FULLY):** pass 1 identity (recognizable after every cut?) · pass 2 continuity (ledger row met? props constant?) · pass 3 timing (actions inside budget, no padding break?) · pass 4 camera (one move, axis held, no quick-cut hiding?) · pass 5 audio (diegetic only, sync, no music). Fix the weakest instruction first; correction goes into the NEXT prompt.
- **Motion ladder (model/style approval):** identical character through: subtle portrait → head turn → walk → fast action → interaction. Only after passing, commit the production style.

## 20. Legal, licensing & disclosure
🟢 **IP baselines** (consolidated): styles are free; named characters/franchises/songs are not (active enforcement documented across studios, anime rights holders, labels). Standard protection: the ANTI-IP prompt block (ch. 13). Director/DoP names as style references are established; "in the spirit of, fully original execution" is the official formula.
🟢 **Real people:** photos only with consent as references; voice cloning only with documented consent; no recognizable third parties without a release.
🟢 **Commercial output rights per platform:** rights hang on the plan (free tiers often non-commercial) and change — read the current terms of the generation platform AND music/voice services before release; budget for moderation/eligibility checks.
🟢 **Copyrightability of AI output:** under current US Copyright Office guidance, purely AI-generated output is **not copyrightable**; protection requires human authorship — creative selection, arrangement, editing, or substantial human-authored elements can be protected as such. EU member states similarly require human creative input. Practical rule: **document your human creative contribution** (treatment, shot design, prompt authorship, edit decisions) — it is your protectable layer and your evidence. [established guidance]
🟢 **Disclosure duty (EU AI Act Art. 50, effective 2026-08-02):** synthetic content that could pass as real needs (a) human-readable disclosure and (b) machine-readable marking; the EU practice code names **C2PA Content Credentials** as the primary technical solution (plus invisible watermarks like SynthID). Applies to anyone whose content reaches EU audiences.
🟢 **Platform labels as a second mandatory layer:** Meta "AI Info", TikTok AIGC labels, YouTube disclosure, LinkedIn CR badge partly read C2PA automatically — but some platforms **strip C2PA manifests on upload** (documented): file metadata alone is insufficient; set the native platform label as well. AI disclosure does not replace ad disclosure and vice versa. Keep an archive copy WITH the manifest. [W]

## 21. Cross-model syntax profiles: MiniMax H3, Kling 3.0, Veo 3.1, Grok Imagine
For shots routed to a non-Seedance model via the ch.-11/renderability matrix. Never port prompts 1:1 (style-control §5b). ⚠️ **Source caveat:** the H3 profile relies primarily on one detailed engineering guide plus blogs claiming to mirror the official MiniMax docs — the official docs were not fetched directly. Rules below carry 🟡 where single-source; verify the exact syntax against MiniMax's current documentation before a production run.

### MiniMax H3 (Hailuo 3) — full syntax profile
🟢 Specs (official model card, multi-cited): 4–15 s, 24 fps, 32-kHz stereo audio native; 768p base, 2K via separate "H3-Regenerate-2K" module (re-feed, not a classic upscaler); ratios 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. **One beat per shot** — a second action = a second shot.
🟢 6-layer formula: Subject (specific!) + Action (active verbs with direction/speed) + Scene + Visual Style (ONE, committed) + Camera (one move) + **Audio (never omit — otherwise random ambience)**.
🟡 **Timestamp system (exact syntax, single-source):**
```
MM:SS.mmm–MM:SS.mmm [shot description incl. camera + audio]
```
Ranges gapless-sequential, no overlap; start 00:00.000, end = total duration; **shots 2–5 s, never <1.5 s**. Shot budget: 4–6 s → 1–2 shots · 7–10 s → 2–3 (sweet spot) · 11–15 s → 3–5 (consistency risk rises).
🟡 **Dialogue tag:** `<d>[English] line text</d>` inline in the shot; the language tag steers synthesis; max 1–2 sentences per shot; quality decent — replace hero VO externally (ch. 18). Describe sound in natural language; state music directives explicitly ("no music, only ambient sounds").
🟢 **Three modes:** **T2VA** (describe everything) · **I2VA** — image = frame 1: **do NOT re-describe the image; describe the evolution** ("The woman walks forward, wind catching her hair…") · **Ref2VA** — reference steers style/subject, the scene is NEW (series consistency). Plus FL2VA (first/last frame). Official docs separate: visual timeline / dialogue / physical sound / audience music as distinct prompt layers.
🟡 Don'ts (tested by the guide): no transition language (H3 cuts itself) · no on-screen text requests · no slideshow prompts (each shot needs continuous motion) · no FPS/frame counts · no meta words ("high quality", "viral") · never overlap timestamps.
🟢 Unique capabilities: LoRA training for style/character/motion lock (style-control §5b); comparatively stable on-screen text/UI 🟡; holds 2D line quality; identity mapping per image ("Character A uses Image 1 for face, hair, outfit").

### Kling 3.0 — compact profile
🟢 Strengths: multi-shot storytelling (holds art style across shots), directed movement, elements/reference system, native audio (CN/EN/JP/KR/ES + accents), MotionControl (reference action video + face binding). Prompt logic: clear scene direction — subject, action, setting, light, camera movement as precise motion instruction; composition comes from the input image. **Repeat style keywords + the style reference image in EVERY prompt of a sequence** (each generation is interpreted independently — drifts otherwise). Anime: 5–8 s, 2–3× reroll budget, never mix realism + anime.

### Veo 3.1 — compact profile
🟢 Strengths: polished cinematic realism, natural environments, integrated audiovisual, ingredients (references), first/last frames, scene extension, camera controls. Prompt logic: descriptive natural language + a micro beat sheet in the prompt; request continuity explicitly ("consistent wardrobe, props, positions", "keep character on-model across shots"). Camera phrasing: "lateral tracking shot, camera moves with subject" / "camera cranes upward". Physics-correct motion fights stylized looks — prompt the motion grammar along (style-control §5b).

### Grok Imagine (1.5) — compact profile
🟢 Fast iteration, native audio, strong instruction-following for movement/pacing/transitions; native stylization bias (cartoon/anime/art-directed). Rules: **style qualifiers at the prompt START**; negatives unreliable → phrase positively; strong I2V; 720p cap (1.5: 1080p in modes) → plan the upscale path. Use for stylized shots, mood/concept tests, fast exploration.

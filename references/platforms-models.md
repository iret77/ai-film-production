# Platforms & Cross-Model Profiles: Higgsfield CS, H3, Kling, Veo, Grok (ch. 13, 21)


Source-tagged knowledge base. Confidence labels: 🟢 multi-source/official/production-proven · 🟡 plausible, single-source or untested · 🔴 marketing claim, verify yourself. Source tags: [A]=platform academy docs, [P1–P18]=practitioner video protocols (archive file), [PP]=first-party production-session evidence, [W]=web research (multi-source), [H-off]=Higgsfield official, [BD-off]=ByteDance official guide (via verified reproductions), [F]=fal.ai official, [R-off]=Runway official, [X-ext]=community skill (partially officially confirmed), [OAI-off]=OpenAI cookbook, [G2]/[NB]=image-model guide clusters.

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
🟢 **Settings are VIDEO controls, not still controls [PP]:** the CS settings panel (Genre, Palette, Lighting, Camera, Era, Tempo…) applies at video generation. Still prompts in the stills-first phase do NOT reference these settings — the still carries its look entirely in prompt + references; the settings become relevant at the motion test. Keep the two control layers strictly separate in any prompt document.
🟢 **Style anchor duty for stylized looks:** CS and Seedance default to photorealism; Pixar/cartoon/anime must be anchored actively — look-carrying references AND/OR an explicit style anchor; weak anchoring tips into photorealism (full mechanics: style-control).

### CS 4.0 platform (official pages, Aug 2026)
🟢 **Multi-model support** — engine chosen PER SHOT (Seedance et al. run natively; UI reports also name Higgsfield Native, Kling, Sora, Veo) — the ch.-11 selection matrix maps directly onto the UI. **Montage Pacing** ("cuts, rhythm and flow built in — no timeline, no post"). **Mr. Higgs / Personal Assistant** (the 3.5 docs' "Claude Chat"): picks camera/light, writes prompts with real @tags, breaks scripts into shots — never triggers Generate itself. **Subfoldering** (scenes/versions/deliverables for 200-shot productions), **Canvas**, team layer (live co-directing, shared elements), **Color Grading** as a fine-tune pass. Credits by length × resolution × model. **Blender plugin (free) [P18]:** Bridge connector links the LLM to Blender for 3D blockouts; a Higgsfield panel inside Blender drops assets/models/scenes — the blocking-first path of production-pipeline ch. 8.
🟢 Specs — resolution is a MOVING TARGET, documented states: launch blog (Aug 2026) said up to 30 s / max 720p; **platform update later in Aug 2026: Seedance 2.5 inside Higgsfield now renders 1080p**; the product page additionally claims native 4K and up to one minute (partly unverified). Since Seedance 2.5 is technically 4K-capable, a later 2K/4K unlock on Higgsfield is plausible — the cap is a platform resource/cost decision, not a model limit. 🟡 Agents: **web-verify the current resolution tier before planning any resolution pipeline.** Constant: up to 50 references, forward/**backward** extend, 30+ camera presets. The verified native-4K route today remains Seedance 2.0 direct (`seedance_2_0, 21:9, 4k`).
🔴 Marketing claims, test yourself: "anti-slop camera pipeline" (no plastic skin, no drifting faces, no AI shimmer) and AI-Cast/location persistence ("same street, same weather, next week") — advertising only; validate against the proven drift rules (production-pipeline ch. 3/6).

### Official prompt patterns (from published production prompts)
🟢 DoP names as legal style references ("References in spirit, fully original execution: Deakins, Hoytema…") · ABSOLUTE ANTI-IP block as a standard section (generic settings, no insignia/logos, original score, "all on-screen text in POST") · percentage color distribution (60/30/10) · keyframe placeable mid-sequence ("Reproduce the KEYFRAME composition EXACTLY at Shot 3 — BUT his action is changed: …") · CRITICAL handling blocks for standing invariants ("ALWAYS by the HANDLE, NEVER on the blade").
🟢 **Multi-plate set for dialogue:** @room1 master + @room2 reverse + @room3 detail — "three angles of ONE set at ONE shared exposure"; the axis (180° line) named in every prompt.
🟢 **Master-screen trick** for locked in-frame text: freeze the text in the reference plate, lock via prompt ("exactly this one line, frozen and identical in every frame") — the plate-locked exception of the unified text rule (renderability §2).
🟢 **Locked prompt template of the official prompt-builder skill** (`/higgsfield-seedance-prompt`): scene context → references → shot-by-shot action → lighting → locks; audio always real-world sound only, music added in the edit. Invocation is a natural-language scene brief with @tags ("@hero is searching @loc_cabin … finds @map_prop …") — the skill expands it into the full schema. One prompt covers a whole beat: cuts, dialogue line, and sound from a single generation. [H-off Stage 3]
🟢 **Official zero-motion / rack-focus block** (copy-ready camera language): "The camera stays planted in one immovable position from the first frame to the last. Zero motion — no drift, no shake, no breathing, no stabilization float, no micro-drift. Hold sharp on [plane A — the far anchor]; then rack once to [plane B — the near subject]; then follow focus on the subject if they move toward the lens. The rack is slow, smooth and continuous with no hunting and no overshoot; the follow focus tracks without breathing." — the pattern for static dialogue/tension shots. [H-off Academy]
🟢 **BEAT structure** for takes: numbered beats with time ranges, one primary event each.
🟢 Negations of both kinds are official CS practice — governed by the revised negative rule in video-prompting ch. 14.

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
🟡 **Dialogue tag:** `<d>[English] line text</d>` inline in the shot; the language tag steers synthesis; max 1–2 sentences per shot; quality decent — replace hero VO externally (post-audio-legal ch. 18). Describe sound in natural language; state music directives explicitly ("no music, only ambient sounds").
🟢 **Three modes:** **T2VA** (describe everything) · **I2VA** — image = frame 1: **do NOT re-describe the image; describe the evolution** ("The woman walks forward, wind catching her hair…") · **Ref2VA** — reference steers style/subject, the scene is NEW (series consistency). Plus FL2VA (first/last frame). Official docs separate: visual timeline / dialogue / physical sound / audience music as distinct prompt layers.
🟡 Don'ts (tested by the guide): no transition language (H3 cuts itself) · no on-screen text requests · no slideshow prompts (each shot needs continuous motion) · no FPS/frame counts · no meta words ("high quality", "viral") · never overlap timestamps.
🟢 Unique capabilities: LoRA training for style/character/motion lock (style-control §5b); comparatively stable on-screen text/UI 🟡; holds 2D line quality; identity mapping per image ("Character A uses Image 1 for face, hair, outfit").

### Kling 3.0 — compact profile
🟢 Strengths: multi-shot storytelling (holds art style across shots), directed movement, elements/reference system, native audio (CN/EN/JP/KR/ES + accents), MotionControl (reference action video + face binding). Prompt logic: clear scene direction — subject, action, setting, light, camera movement as precise motion instruction; composition comes from the input image. **Repeat style keywords + the style reference image in EVERY prompt of a sequence** (each generation is interpreted independently — drifts otherwise). Anime: 5–8 s, 2–3× reroll budget, never mix realism + anime.

### Veo 3.1 — compact profile
🟢 Strengths: polished cinematic realism, natural environments, integrated audiovisual, ingredients (references), first/last frames, scene extension, camera controls. Prompt logic: descriptive natural language + a micro beat sheet in the prompt; request continuity explicitly ("consistent wardrobe, props, positions", "keep character on-model across shots"). Camera phrasing: "lateral tracking shot, camera moves with subject" / "camera cranes upward". Physics-correct motion fights stylized looks — prompt the motion grammar along (style-control §5b).

### Grok Imagine (1.5) — compact profile
🟢 Fast iteration, native audio, strong instruction-following for movement/pacing/transitions; native stylization bias (cartoon/anime/art-directed). Rules: **style qualifiers at the prompt START**; negatives unreliable → phrase positively; strong I2V; 720p cap (1.5: 1080p in modes) → plan the upscale path. Use for stylized shots, mood/concept tests, fast exploration.

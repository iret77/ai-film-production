# Production Pipeline: Principles, Assets, QA, Coverage (ch. 1–11, 16)


Source-tagged knowledge base. Confidence labels: 🟢 multi-source/official/production-proven · 🟡 plausible, single-source or untested · 🔴 marketing claim, verify yourself. Source tags: [A]=platform academy docs, [P1–P18]=practitioner video protocols (archive file), [PP]=first-party production-session evidence, [W]=web research (multi-source), [H-off]=Higgsfield official, [BD-off]=ByteDance official guide (via verified reproductions), [F]=fal.ai official, [R-off]=Runway official, [X-ext]=community skill (partially officially confirmed), [OAI-off]=OpenAI cookbook, [G2]/[NB]=image-model guide clusters.

## 1. Pipeline principles
🟢 **Stills-first:** every shot exists as an approved still (start frame) before any video generation. The look is won in the image; video inherits it. Cheap iteration happens at the image stage.
🟢 **Order: location plates → characters → props → composite stills → motion tests → production takes.** Characters are shot INTO approved plates, never invented alongside them.
🟢 **Inverted order for Pixar/stylized projects (hard rule) [PP]:** stylized environments generated WITHOUT a figure default to photoreal on every image model — because stylized-feature environments are themselves near-photoreal, the model has nothing to stylize against. The figure in frame forces the whole render into the stylized mode; figure + environment together IS the look. Build order therefore inverts: (1) character sheets (neutral grey, no location needed) → (2) location ANCHOR plates generated WITH a figure in frame → (3) empty location backgrounds derived via edit model (remove the figure — the style stays baked in). Alternative for figure-less environment stills: the prompt-only style-forcing method (pixar-look ch. 9) — reliable in bright light; dark scenes need a self-generated bright style anchor. Applies to Pixar and comparable stylized-3D looks; photoreal projects keep the location-first order above.
🟢 **Review loop:** generate → review against acceptance criteria → fix the weakest instruction in the NEXT prompt (not only in post) → regenerate. Worth knowing: a defect accepted at the still stage propagates into motion, so a still that is "close enough" often costs more later — the user decides when it is good enough to move on.
🟢 **Sheets vs. in-scene stills:** reference sheets (neutral light) maximize consistency; in-scene stills (scene light) maximize realism. Both exist; sheets feed identity, in-scene stills feed the take.
🟢 **Label discipline:** every asset gets a stable ID (@name) reused verbatim in prompts, filenames, and the continuity ledger (post-audio-legal ch. 19).

## 2. Script & treatment for generability
🟢 Write the script in stages: logline → ~10 candidate synopses (cheap ideation, pick one) → treatment → shot-level script. At each stage, run a renderability pass (renderability.md) and cut or rescue red elements — rescue cuts are a writing tool, not a defeat.
🟢 **Complexity budget per take:** one primary event per shot; 2–3 shots per 15/30-s take with explicit labels ("Shot 1/2/3") and HARD CUT markers.
🟢 Open on a hook (first 2 s earn the rest); write endings as their own beat with its own time range.

## 3. Characters
🟢 **Minimal sheet:** front, side, back, face close-up, clothing detail — one character per image, neutral even light, plain background. 🟢 Official course variant: a 3-view sheet (full-body front, full-body back, frontal close-up) generated FROM a reference photo on a grey background — the close-up is what locks the face. 🟢 **Defensive anatomy locks are official practice:** character prompts carry insurance lines ("Both arms whole and both hands normal, intact human hands — no missing limbs") and anti-sheen skin lines ("skin matte and low-sheen — no oily highlights, no specular hotspots") — pre-empting the two most common character defects. [H-off Stage 2] **One-face rule:** exactly one canonical face; never let a second "almost right" face into any reference set.
🟢 **State sheets:** any persistent change (wet, wounded, dirty, costume change) is a NEW sheet order, never a prompt adjective. The ledger (post-audio-legal ch. 19) tracks which state sheet each shot uses.
🟢 **Anti-drift ladder:** (1) sheet as reference in every generation, (2) verbatim identity anchor line in every prompt, (3) frame-harvest a well-liked generation as an additional reference, (4) if drift persists: regenerate the sheet, don't patch outputs.
🟢 Voice: the sheet locks the voice along with the face on audio-capable models — accept the native voice where it fits; otherwise replace via the voice pipeline (post-audio-legal ch. 18).
🟢 **Animation sheet variant [P17]:** for ANIMATION projects, expressions beat views — animated video carries far more facial expression than cinematic footage. Layout: one full-body pose + 8 distinct expression panels (instead of the multi-view emphasis); the video model draws on the expression range during acting. Cinematic/photoreal projects keep the multi-view sheet above.
🟢 **Crowd sheet:** one multi-variant sheet (6–12 distinct extras) referenced for background population — prevents clone crowds.

### Copy-ready sheet & board templates [G2-gallery]
🟢 **Character reference sheet (image prompt, works verbatim):** "Based on this character [reference attached], create a character reference sheet similar to official setting materials: three-view drawings (front, side, back) · facial expression variations · detailed parts breakdown of clothing and equipment · a color palette · organized layout, white background, [style] illustration." Adapt the style word; keep the structure.
🟢 **Expression grid (feeds the expression-sheet order):** "Create a [N]-panel expression grid of [character, reference attached]. Face shape, hairstyle, and clothing must remain highly consistent across all panels. Expressions: [list them explicitly — happy, sad, angry, surprised, shy, contemplative, scared…]." Naming each expression beats "various emotions".
🟢 **Multi-variant cast grid (THE crowd-sheet tool):** "A single landscape image containing a clean [2×5] character grid. Each panel shows a different [role archetype list — one distinct hairstyle, outfit, prop, and expression each]. Keep all panels consistent in art direction: [style tokens], tidy white gutters, small name tag per panel — a collectible cast-sheet feel." Distinct archetypes per panel prevent clone crowds; the shared art-direction line prevents style drift across panels.
🟢 **Multi-panel consistency rules (all grids/sheets/boards):** state the grid count exactly (3×3, 2×5, 16-panel) · give each panel a role or beat · one shared art-direction sentence covering all panels · white gutters + per-panel labels where identification matters. Structure (canvas, ratio, grid) goes BEFORE subject description — otherwise the model spends its detail budget on the subject and improvises the layout.

## 4. Locations & props
🟢 Per location: one master wide plate + 2–3 detail plates at ONE shared exposure/palette. **Reverse decision up front:** does this location need counter-angles (dialogue, cross-room action)? → build the multi-plate set (platforms-models ch. 13). Pass-through/B-roll → one wide suffices. Missing reverse plates ordered late are the most expensive single mistake in the pipeline (ch. 16).
🟢 Props with narrative state changes get a **state pair/series of stills** (before/after), treated like character state sheets.
🟢 Screenshot workaround: frames from an approved video generation are legitimate (often superior) plate sources — they carry light and geography correctly.

## 5. Image model selection
| Model | Use for | Notes |
|---|---|---|
| Soul Cinema | Photoreal characters/locations from scratch | Cinematic default; not the stylization specialist |
| **GPT Image 2** | Geography consistency, reverse angles WITH layout-map input, edits/derivatives, structured/text-dense assets; stylized stills via the proven 4-section structure (style-control §2); **stylized environments from scratch via the style-forcing blocks (priority/thumbnail/flat-color/render-treatment/avoid — pixar-look ch. 9); dark scenes: add a bright self-generated style anchor + lighting override [PP]** | Reasoning model; for Pixar figure+environment from scratch, Nano Banana Pro renders stronger [PP]; grain/noise tell on stylized renders [P17] |
| **Nano Banana Pro** | **Strongest model for Pixar/stylized stills from scratch (environment+figure in one render, 4K) [PP]**; style transfer with identity lock, multi-character scaffolding, manga pages, props, edits | Beats GPT Image 2 on CG render quality (AO, subsurface scattering); weakness: ruler-symmetry and stock-photo lifelessness on figure-LESS scenes — pair with the figure-anchor rule (ch. 1). Style-medium-LAST mechanics → style-control §3 |
| Seedream 5.0 Pro | Edits with texture preservation; 🟡 character sheets from scratch (single-source, [P17]) | Version on Higgsfield as of Aug 2026; 4.5 edit notes still apply |
| Midjourney | Discovery/moodboards | Not a pipeline production tool |

🟢 **Mix and match per asset [P17]:** no single image model wins across a project — pick per asset and compare; image credits are cheap, video credits are not: "spend more time getting the best image than fixing it in video generations."

### 5b. Higgsfield UI object model ⚠️ version-volatile (verify in app)
🟢 Assets live as **Elements** (characters/locations/props) scoped to the project, pulled via @tags; a **Scene** = hero shot composed from elements → becomes the start frame; save explicitly. 🟢 **Exact-name rule:** add each asset under Elements with EXACTLY the tag name used in script and prompts — scene generation auto-matches inputs by these tags; a name mismatch silently unbinds the reference. [H-off] Director panel applies settings at generation time (platforms-models ch. 13). AI Cast builds reusable actors (genre, era, archetype, physique, outfit, distinguishing details). Multi-shot auto/manual. Documented against the 2.5-era UI; 4.0 keeps the model but renames/extends — check the live UI before writing UI-dependent instructions.

## 6. Video prompting basics
🟢 **Keep list (officially rewarded):** subject specificity, active verbs with direction/speed, scene with time-of-day/weather, ONE committed visual style, one camera verb per shot, audio always described.
🟢 Choreography beats adjectives: write micro-cues (eyes, brows, mouth, breathing, hands) instead of emotion labels; cause before reaction (contact → movement → sound → reaction) — never leave the causal link to the model.
🟢 Timestamps are pacing budgets, not frame guarantees; a timestamped beat = short take.
🟢 **Position lock:** state where every subject starts, faces, and ends.
🟢 **Audio:** describe diegetic sound naturally; **always exclude music** ("original fictional score" only where a score is wanted as diegetic; the real score is built in post, post-audio-legal ch. 18).

## 7. Dialogue scenes
🟢 **Framing recycling:** exactly two repeated framings (single ↔ over-shoulder); "shot 3 repeats shot 1's framing" — repetition is what sells coverage.
🟢 Reverse-environment references are mandatory (multi-plate, platforms-models ch. 13); **180° lock:** name the axis and forbid crossing it in every dialogue prompt. Strongest spatial lock for multi-person dialogue: the 3D blockout path (ch. 8) — seat positions, eye-lines, and cuts pre-decided in gray boxes hold where text-only prompting swaps seats [P18].
🟢 One line per shot beat; speaker tags per platform syntax (video-prompting ch. 12/21); never two characters speaking simultaneously.

## 8. Geometry inputs (when language won't pin space)
🟢 Ascending: **layout map** (top-down schematic generated as an image, fed as reference) → annotated sketch → arrow annotation on a plate → camera-path line drawing → **full 3D blockout video (strongest form, below)**. "One drawing tells the model what 10 sentences can't." Remove any helper geometry you don't want rendered (video-prompting ch. 14).
🟢 **3D blockout via the Higgsfield Blender plugin [P18] — the strongest spatial/camera control available:** the free plugin bridges the LLM to Blender (Bridge URL → connector → plugin in the viewport); the LLM builds editable gray-box scenes, camera rails, and cuts from natural language — no Blender skills required, and existing keyframes steer the AI directly for those who have them. Workflow: describe scene + shot list → iterate the blocking in words ("more handheld sway", "add texture", "recut scene 3") → viewport-render the blocking (1080p/24/MP4) → attach the render and ask the LLM to **write the video prompt second-by-second matching the clip's camera moves** → generate with the duration set to the blocking length. Documented result class: multi-move camera chains (orbit→profile→top-down), floor-rise and robo-arm moves, and a 6-person/4-cut dialogue with zero seat swaps — first try; the identical prompt WITHOUT the blockout drifted, broke the 180° axis, and burned ~5,000 credits without one clean take.
🟢 **Gray-box rules [P18]:** the blockout controls camera + timing, the references control visuals — keep the split explicit in the prompt ("the gray boxes are [who/what]; visuals come from @refs"). Elements that can't be blocked (liquids, magic) stay BLANK/black in the blockout — the model fills them. Camera follows a separate offset target next to the subject (not locked on the head) for a realistic feel; add a subtle handheld pass in words after the mechanical pass. A followed path with control points is drag-editable — tweak angles in Blender, never by re-prompting.
🟢 **Two-halves principle [P18]:** every blocking-driven prompt has a structural half (the reference video: cuts, camera, timing — never changes) and a style half (what the world looks like). Client notes and restyles touch ONLY one half: recut the blocking for structural notes, swap the style layer for a different world — one edit renders as 2.5D, flat 2D, or toy-box 3D with frame-matched camera. Pitch workflow: three visual worlds on one approved edit in a day.

## 9. Alternative production paths
🟢 **Storyboard-to-sequence:** a clean storyboard grid (<15 panels, clean line art, minimal text, stated reading order, grid style excluded) drives a sequence at ~70–80% adherence — cheap pre-viz, not final control. **Higgsfield Popcorn** is the platform's sequence-aware storyboard generator: Auto (one prompt → arc) or Manual (per-frame direction), up to 8 frames/run, longer arcs via bridge-frame chaining (last frame = next run's reference), 1–4 reference inputs, export toward video models. [H-off]
🟢 **Copy-ready storyboard prompt template [G2-gallery]:** "A [6]-panel film storyboard laid out as a [3×2] grid, landscape 16:9. Each panel is a rectangular pencil-and-marker sketch with a white margin border and a small information strip underneath. Scene: [one-line sequence description]. Panel 1 — [SHOT TYPE + content]. Info: 'PANEL 1 · [INT/EXT. LOCATION · TIME] · [WIDE/OTS/CU/LOW ANGLE] / [static|pan-L 45°|tilt-up|crane-down] / [2s]' … [repeat per panel] … Art direction: classic animation-school storyboard — pencil line-work, grey marker shading, red-pencil arrow annotations for camera moves and action arcs, off-white paper texture." The per-panel info strips (shot type / camera move / duration / SFX) are exactly the panel annotations Seedance reads as direction (storyboard-to-sequence above); the arrow annotations double as geometry input (ch. 8).
🟢 **VFX hybrid:** shoot real plates, generate elements/extensions; and the inverse **restyle path** (live footage as motion scaffold → full style transfer) — style-control §5b.
🟢 **Extension chains:** forward/backward extension to build beyond single-take limits (2.5: toward 180 s beta) with the guards from video-prompting ch. 14; long single generations (60 s+) only for montage content, not held scenes.
🟢 **Audio-to-video:** a finished audio track (dialogue/music beat) as timing skeleton for generation where supported.

## 10. QA & slop control
🟢 **Four slop tells:** plastic/waxy skin · drifting faces between cuts · AI shimmer on texture · hectic cutting exactly at hard motion (model hiding failure). Any tell = reject take.
🟢 **Batch protocol:** generate 4, watch ALL fully (failures teach the next prompt), review in the separate passes of post-audio-legal ch. 19. Review ADJACENT shots together, not clips in isolation — continuity errors live between shots, never inside one. [W]
🟢 **Keeper phases:** draft tier for exploration → standard tier only for near-final prompts → hero renders last.
🟢 **Resolution ladder:** iterate at 480/720p, render finals at target resolution; judge an upscaler on one exported frame before batch-processing (post-audio-legal ch. 17).

## 11. Model choice inside the Seedance family
🟢 "2.5 is a .5 improvement, not a revolution" — choose PER SHOT: 2.0 for UGC realism, cost efficiency, validation drafts; 2.5 for long takes, choreography with weight, in-shot transformations, multi-stage emotion, reflection-heavy scenes, slow controlled camera moves (2.0 overshoots the subject). Mini/Fast tiers for drafting only.

## 16. Perspective changes & coverage (cost-ranked)
**Core problem:** image models lack true spatial understanding — free-text reverse/new-angle stills of the same scene are unreliable. Video models switch angles reliably WITHIN a take. Hence the ladder — cheap/reliable to expensive/risky; exhaust each rung first:

**Rung 1 — angle changes inside the generation (default):** new angles as **internal shots of the same take** (ch. 2 labels, HARD CUTs) — the model holds set and figures because it builds them in one context. Dialogue: framing recycling (ch. 7). By far the cheapest reliable coverage.
**Rung 2 — harvest angles from existing video:** screenshots from a successful generation are the best references for follow-up angles (light, palette, geography already correct); last frame + "continue forward, do not replay". 🟡 2.5 camera-perspective editing (officially announced, practice-unconfirmed); same class: Runway Aleph "generate new camera angles" on real footage.
**Rung 3 — dedicated image tools instead of free-text reverse:** when an angle is needed as a STILL: never "same scene from behind" via free text — use purpose-built tools (below) or GPT Image 2 WITH a layout map/master plate as input. Reverse test afterward: anchors, openings, light side, palette must match the master plate. Planned dialogue sets: pre-produce the multi-plate system (platforms-models ch. 13) — 2–3 plates save dozens of failed generations.
**Rung 4 — geometry inputs** (ch. 8) when nothing pins.
**Per location, worth deciding up front:** whether it needs reverse angles (ch. 4) — settling it early is cheaper than discovering it mid-production, but it stays the user's call.

### Higgsfield tools for perspective (verified) [H-off]
🟢 **Angles** (Apps): change the camera angle of any image — full 360° incl. behind the subject; "generate from all angles" = 12 perspectives in one batch. THE tool for reverse plates.
🟢 **Shots** (Apps): one image → storyboard coverage; walks around the subject and **preserves the original's style/grading**. Best input 3:4/4:3 for the widest angle range.
🟢 **Popcorn** (storyboard generator): sequence-aware frames with held identity/lighting — usable as an angle/coverage explorer before committing plates (ch. 9).
🟢 **DoP** (Video Tools): a camera-motion-trained model with 100+ presets. Two rules: (1) the line "**preserve the original face, lighting, and geometry**" goes into the prompt; (2) pick the preset in the app AND repeat the move in prompt text. One main move per clip.
🟢 **Start & End Frame:** lock both ends as images; the platform animates the path — perspective change as a controlled move between two known framings instead of a lottery.
🟡 **WAN Camera Control / Multi-Axis:** physics-based camera paths; CS allows stacking up to 3 moves — ⚠️ conflicts with the proven one-move rule; stack only with test budget.


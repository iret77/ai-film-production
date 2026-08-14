---
name: ai-film-production
description: Plan and produce AI-generated video/film end to end - treatments, scripts, screenplays, shot lists, asset orders (character sheets, locations, props), and Seedance video prompts - optimized for current video models (Seedance 2.x, Veo 3.x, Kling 3.x, Sora, PixVerse, Hailuo) and the Higgsfield Cinema Studio pipeline. Use this skill whenever the user wants to write, review, or fix a treatment, script, Drehbuch, storyboard, shot list, scene, asset order, or generation prompt for an AI-generated film, short, ad, or social video — also when they ask "can this scene be generated?", "make this script AI-ready", "plan my AI film", or mention writing for Seedance / Veo / Kling / Higgsfield Cinema Studio. Trigger even if they don't say "AI" but the production path is clearly generative video.
---

# AI Film Treatment & Script Writing

Write scripts whose every shot is renderable by today's video models without looking AI-generated. The craft: design around the models' six failure classes (temporal inconsistency, physics errors, anatomy errors, interaction errors, identity drift across cuts, broken in-frame text) instead of fighting them in post.

Output language follows the user (German user → German treatment), keep this skill's technical terms (shot, plate, reverse, anchor) as-is.


**Scope & version:** v1.0-en (2026-08). Universal skill for AI film production; prompt syntax is Seedance-2.x/Higgsfield-first with a full MiniMax H3 syntax profile and compact syntax profiles for Kling 3.0, Veo 3.1, and Grok Imagine (pipeline ch. 21); Wan/LTX and others are covered as selection/style matrices only. Knowledge is source-tagged with confidence labels throughout the reference files; nothing project- or person-specific is contained.

**How this skill is meant to be used.** The agent advises and moderates; the user directs and decides. This skill is a box of guidelines and craft, not a set of rules or gates to enforce on the user. When the user is experimenting, exploring, or chasing a creative idea, help them get there fast — offer the relevant knowledge, flag a real risk once in plain language, and then follow their call. Do not block, do not gate, do not cite chapter numbers at the user, do not repeat a warning they have already heard. The user is the only approval instance for their own project. Surface trade-offs when they help; never turn them into permission checks.

## Workflow

### 1. Intake — settle these before writing

Ask only what the conversation hasn't answered yet:

1. **Format/look**: photoreal ("Realfilm"), Pixar/3D, cartoon/anime, or UGC/doku-handheld? If the user is undecided, recommend by risk: stylized (Pixar/cartoon) and UGC absorb model errors; photoreal demands the strictest shot discipline; the dangerous zone is "almost-photoreal" (uncanny valley → instant AI suspicion).
2. **Target length & platform** (a "film" = a chain of 4–12 s shots; nothing else exists at generation level).
3. **Deliverable**: Treatment, Drehbuch/screenplay, shot list, or all three.
4. **Model stack** if known (default assumption: Seedance 2.x for motion, stills-first pipeline à la Higgsfield Cinema Studio). Model-specific limits → `references/renderability.md`.
5. **Dialogue language**: native English lip-sync is fine; non-English dialogue → plan voice-clone dubbing or voiceover/doku structure in the script itself.

### 2. Write shot-first, prompt sequence-first

Structure every scene as numbered shots of **4–12 seconds**. Per shot, budget complexity: **max one main action + one camera move + max two characters**. Split complexity across cuts rather than stacking it — cutting is cheap and filmic; long takes (>12–15 s) drift and are never worth it.

Map shots to generation units — **plan in shots, generate in sequences**: one generation carries a whole sequence (a continuous take with timeline blocks, or a multi-shot chain "Shot 1 … End state … Shot 2 …"), where each block inherits the physical state of the previous one and the prompt closes with an explicit ENDING STATE. The unit sizes are model-dependent: **one Seedance 2.0 generation = one 15-s take in 4K; one Seedance 2.5 generation = one 30-s take at 720p only.** A take may contain 2–3 internal shots with real camera-angle changes (label them Shot 1/2/3 inside the prompt). Plan pacing to the target model — never place a dramatic peak at the end of a 15-s 2.0 take (the clock runs out exactly there); reserve 2.5 for complex continuous camera work, choreography, and in-shot transformations, and 2.0 (or an upscale path) for 4K deliverables and hero close-ups. When character positioning must hold, open the generation with a wide establishing shot — Seedance locks everyone's position for the whole take. If a scene feels rushed inside 15 s, split it into two generations rather than cramming. Voice direction (tone, micro pauses, trembling) belongs in the prompt; for standalone voice lines, generate a throwaway shot just for the audio and overlay it in edit.

Per shot, specify (this is what makes the script "AI-ready" rather than a normal Drehbuch):

- **Shot type & lens** from a fixed camera grammar defined once per sequence and repeated verbatim (e.g. "35mm handheld tracking, golden-hour key, shallow DoF"). One camera verb per shot.
- **Blocking anchored to an object**, never to screen direction: "between the sofa's hall-side arm and the window", not "on the left".
- **Assets referenced by name** (`@char_`, `@loc_`, `@prop_`) — see step 4.
- **Match-action cue** to the next shot where continuity matters ("continues turning right").

Sequence dramaturgy: Establish → Action → Reaction → Detail. Dialogue as shot/reverse-shot, never two-shot with body contact — and every shot/reverse-shot scene requires reverse-angle environment references of the room (both sides as images) in pre-production, plus explicit 180°-rule and prop-size locks in the prompt, or backgrounds and props will jump between cuts. Never change palette or time-of-day mid-sequence.

### 3. Lint against the red list

After drafting (and when reviewing someone else's script), scan every shot against the forbidden/risky elements in `references/renderability.md` and rewrite hits. The non-negotiables:

- No readable in-frame text (signs, labels, newspapers) — text goes in post
- No mirrors/reflective story beats; no eating/drinking in close-up
- No hand close-ups or fine motor actions (typing, sewing, card handling)
- No crowds with readable faces; no continuous fight choreography
- No physics showcases (water dynamics, fire, collisions) as hero shots
- **Ellipsis instead of simulation**: "he catches the falling glass" → Shot A: glass tips. Cut. Shot B: hand holds glass.

For every remaining risky shot, write a **rescue cut** into the script: a fallback resolution (different framing, reaction instead of action) the production can drop to without rewriting.

### 4. Plan pre-production as script sections

An AI script has two phases a normal script doesn't. Write them into the treatment as explicit sections *before* the scene text:

- **Set build**: every location, with its locks (geography/entrances/3 depth planes, one motivated light, blocking anchor object, 3/4-master + reverse required? or B-roll-wide-only?). A location that must survive a reverse angle is a bigger production item than one that won't.
- **Casting**: every character as a character-sheet order (identity description, wardrobe, the 6–8 reference poses/expressions the production will need). Reused characters need this; one-shot extras don't.
- **Style anchor**: palette, light logic, lens set, grading — one paragraph, reused verbatim in every prompt downstream.

Pipeline rationale and asset contracts (why stills-first, what Seedance reads from a sheet, the review loop): `references/pipeline.md`. Read it when the user asks *why* a constraint exists, or when producing prompts/asset orders rather than just the script.

### 5. Deliver

- **Treatment**: prose per scene, but each scene ends with its shot breakdown table (Nr | Länge | Shot | Aktion | Assets | Risiko | Rescue).
- **Drehbuch**: standard screenplay format + per-shot technical block.
- **Shot list**: table with per-shot renderability rating (grün/gelb/rot) and, if a model stack was given, model assignment per shot.
- **Storyboard** (fast path for animation/tests): a multi-panel storyboard image with embedded panel annotations, generated via GPT Image at max resolution, fed to Seedance with a minimal prompt — trades shot-level precision for speed; Seedance hits the story beats, not the exact frames. Specify diegetic-only audio and "no text" in the video prompt.
- **Prompt shot list** (when the user wants generation-ready prompts): write every Seedance / Cinema Studio prompt with the **block structure in pipeline ch. 12** — it is the default method, not an optional reference. Each prompt is a single standalone prompt in a code block, opening on SCENE CONTEXT / ACTIVE REFERENCES (never a style prefix — style is distributed into its home blocks, ch. 12 rule 1), with CAMERA in the 3rd position, FOV in degrees from the ch. 12d table, and quantified values (km/h, fog %, Kelvin — ch. 12c). Name prompts (1A, 1B, 2A …) so single ones can be edited in isolation. Write choreography move by move (never "he dances"), bind opening cuts to the previous scene's closing motion for match cuts, and flag any shot whose geography needs a **layout map** (GPT Image schematic as prompt input) instead of prose. Every prompt that uses references MUST contain a reference block (one line per reference: tag + "controls only [job]" + "do not copy [exclusions]") and MUST end with an attachment checklist in upload order — a reference the prompt does not address does not exist for the model. For other video models (H3, Kling, Veo, Grok), keep the block ordering logic and adapt names to that model's syntax (ch. 21). For stylized looks (Pixar, cartoon, anime), apply the full style stack from style-control.md; a style word alone will be ignored.

Always end with a short **risk register**: the shots that remain yellow/red after linting, why they're kept, and their rescue cuts.

## Reference files

- `references/renderability.md` — green/red element lists, format matrix, camera/cut rules, model quick profiles. **Read before linting (step 3) and before assigning models.**
- `references/pipeline.md` — the consolidated production rulebook (21 chapters). Every rule carries a confidence label (🟢 verified across sources / 🟡 plausible single-source / 🔴 marketing claim — test yourself) and source tags. **Read the chapters relevant to the current task: ch. 2 for script work, ch. 3–5 for asset orders, ch. 6–8 for generation prompts, ch. 10 for review/QA, ch. 11 for model choice, ch. 12 for THE core prompt-writing method — the block structure (block order, the three placement rules incl. no-style-prefix and CAMERA-in-3rd, reference tagging, quantification doctrine, the FOV-degree table, optical-technique patterns, special protocols); this is the default template for every Seedance/CS prompt, ch. 13 for the official Higgsfield 14-section Seedance prompt schema and Cinema Studio 4.0 UI controls, ch. 14 for sequence-prompting (timeline blocks, state chaining, ending states, final-frame chaining, Runway modes), ch. 15 pointer → style enforcement now lives in its own file (see below), ch. 16 for perspective changes & coverage — the cost-ranked ladder (in-take angle changes → frame harvesting → dedicated tools like Higgsfield Angles/Shots/DoP → geometry inputs) plus the per-location reverse decision. **Read ch. 16 before ordering any reverse angle or new camera position** — wrong ordering here is the most expensive single mistake in the pipeline. Ch. 17 covers post-production & delivery (upscale ladder, grading, trim rule, format strategy), ch. 18 audio post (three music paths incl. self-produced/licensed/generative with licensing caveats, voice-profile system, dubbing), ch. 19 continuity supervision & sign-off checklists, ch. 20 legal/licensing/AI-disclosure (EU AI Act Art. 50, C2PA, platform labels). Ch. 21 holds the cross-model syntax profiles (full MiniMax H3 incl. timestamp format and dialogue tags; compact Kling/Veo/Grok) — read it before writing any prompt for a non-Seedance model.** When sources conflict, the label and ⚠️ marks tell you which side is safer.
- `references/style-control.md` — style enforcement across image AND video models: the style stack hierarchy, model-specific mechanics (GPT Image 2 style-block-first + negation anchor + rendering cues; Nano Banana Pro style-medium-last + feature locks; Soul Cinema role), style vocabularies (Pixar, Hanna-Barbera, rubber hose, anime, retro-90s, monochrome manga, chibi), and the reference-integration protocol with attachment checklists. **Read for ANY stylized-look task and whenever writing prompts that use reference images.**
- `references/worked-example.md` — a compact end-to-end mini production (brief → assets → two full prompts → QA) showing how the chapters connect. Read it once before your first production task.
- `references/pixar-look.md` — sourced look bible for Pixar/3D-stylized projects; read at intake step 1 when the format is Pixar/3D, and again when writing the style anchor.
- `references/protocols-archive.md` — raw source protocols (Higgsfield Academy + 16 transcript condensates + web research). Only read when the user asks where a rule comes from or wants the unconsolidated detail.

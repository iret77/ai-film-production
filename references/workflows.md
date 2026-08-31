# Workflows: The Typical Jobs, as Runbooks (ch. 25)

Named, ordered procedures for the recurring jobs of an AI-film production. They add NO new rules — they chain the existing chapters into the order that has proven to work, so a session never improvises the sequence. Every step that writes a prompt runs the per-prompt checklist (SKILL.md); every workflow ends by updating the production bible where the project keeps one (rule 11). Every external generation/edit first receives a platform receipt (`platform → route → surface/tool → model + mode → version/snapshot → source/check date → workspace`) in that bible. Pick the workflow by trigger; if two apply, run the earlier-numbered one first.

## W1 — New project (trigger: a new film/short/ad/social video begins)
1. Genre named or evident? Read `genre-baselines.md` FIRST — it pre-answers craft defaults and names the files THIS project type needs.
2. Story intake gate (story-structures ch. 23): the story comes from the user; offer a dramaturgical container before any craft settles.
3. Settle only what the conversation hasn't: format/look (stylized and UGC absorb errors; photoreal demands discipline; ~70% realism is the uncanny danger zone) · target length & platform · deliverable · model stack (renderability quick profiles) · dialogue language (non-English → plan dubbing/VO now).
4. Style direction: user names a director/DoP or a mood → W7.
5. Create the production bible (ch. 22) BEFORE the first asset order; register the decisions above as canon.
Exit: bible exists, container chosen, look decided, model stack named.

## W2 — Asset & reference-pool build-out (trigger: project has a bible, no approved assets yet; or a new character/location/prop enters)
1. Order of build: location plates → characters → props → composite stills (production-pipeline ch. 1). Pixar/stylized projects INVERT: character sheets first, location anchor plates WITH a figure, then derive empty plates (hard rule, ch. 1).
2. Per character: minimal sheet (or animation variant: 1 pose + 8 expressions), defensive anatomy locks, one-face rule (ch. 3). Persistent state changes = NEW state sheets, never prompt adjectives.
3. Per location: master wide + 2–3 detail plates at ONE exposure; decide reverses UP FRONT (ch. 4/16 — late reverse plates are the most expensive single mistake).
4. Build the reference POOL as a deliverable (ch. 14b): wardrobe details, prop stills, style stills, motion clips, voice/audio refs, clay blockouts — one reference for every element that must stay consistent anywhere.
5. Register everything as named elements with EXACT tag names (@hero, @loc_x, @anchor_1A); a name mismatch silently unbinds (production-pipeline ch. 7).
Exit: every element the script needs exists as an approved, tagged reference; bible asset registry updated.

## W3 — Produce one shot (trigger: a numbered shot needs its first take)
1. ROUTE RECEIPT: record the exact platform, access route, active surface/tool, model + mode/endpoint, vendor version or dated UI snapshot, source/check date and account/workspace. Do not choose controls until this exists.
2. CANON: read the beat in treatment/script/bible (rule 13).
3. Lint the shot against `renderability.md` (red list) — rewrite or attach a rescue BEFORE spending a render.
4. Stills-first: generate the shot's still (per-prompt checklist; style mechanics per style-control) → user approves → register as `@anchor_<shot>`.
5. Motion test at draft resolution (480/720p, 10 s) from the anchor; judge with the recipe's Verify line + shot criteria (review loop, ch. 1).
6. Production take only after the motion test sits: target resolution, full duration. A defect accepted at the still stage propagates — surface that trade-off, the user decides.
Exit: approved take; anchor + statuses in the bible.

## W4 — Build a scene/sequence (trigger: several shots of one scene; anything longer than one take)
1. Plan in shots (4–12 s), generate in sequences: 2–3 internal shots per take, explicit ENDING STATE, never a dramatic peak at a take's end (rules 2, ch. 14).
2. Write take prompts with state chaining: each begins from the previous ENDING STATE ("continue forward, do not replay"); harvest final frames as next start frames.
3. On Seedance 2.5, build length by EXTENSION, not by cold stitching: 30 s base + one extension round (chain ≈60 s), boundary-frame contract every round; then re-anchor a fresh generation from the original references (ch. 14b).
4. Dialogue scenes: shot/reverse-shot with the multi-plate set + 180° lock (ch. 7/13); strongest lock = 3D blockout path (ch. 8).
5. Assemble; the score is built in post — never in the video model (rule 9).
Exit: scene cut together from approved takes; continuity ledger updated (ch. 19).

## W5 — Repair a faulty take (trigger: an APPROVED or near-approved take has a local fault)
Never reroll wholesale (rule 12). Route by fault:
| Fault | Fix |
|---|---|
| Wrong object/face/detail in a region or time window | `video_edit`, region description + explicit time scope (ch. 14b/14) |
| Right performance, wrong camera | camera-perspective edit — segmented camera plan, everything else locked (ch. 14b) |
| Right performance, wrong environment | green-screen relocation via `omni_reference` (ch. 14b) |
| Wrong subject, right timeline | subject swap + Timeline Inheritance clause (ch. 14) |
| Audio only (music/voice/language/SFX) | audio-category edit — never touch pixels (ch. 14b) |
| Too short / scene continues | `video_extension` with boundary-frame contract (ch. 14b) |
| Fault is global (style, light, physics everywhere) | back to the prompt: fix the weakest instruction, regenerate (ch. 1 review loop) |
Constraints: source ≤20 s recommended, ≤3 edit iterations then branch from best intermediate; edits bill full source duration.
Exit: fixed take approved; its exact platform receipt noted in the bible.

## W6 — Get a new angle / coverage (trigger: a reverse, insert, or B-camera view is needed)
Climb the ladder, exhaust each rung (ch. 16):
1. New angles as internal shots of the SAME take (cheapest, most reliable).
2. Harvest frames from an existing successful generation as references; or camera-perspective edit on the approved take (B-camera pass).
3. Still needed as a STILL: purpose-built tools (Angles/Shots apps) or GPT Image 2 WITH a layout map — never free-text "same scene from behind". Reverse test: anchors, openings, light side, palette against the master plate.
4. Nothing pins → geometry inputs: 3D blockout/clay render (ch. 8, 14b).
Exit: coverage that passes the reverse test.

## W7 — Define & lock a style (trigger: user names a director/film/mood, or the look drifts)
1. User names a direction → `director-recipes.md` selection index; mix max TWO recipes, one dominant.
2. Build the project style block from look-defining references via LLM reverse-engineering (style-control §7), or from the vocabulary packages (§6) — compact anchor, 4–8 tokens, reused verbatim.
3. Stylized 3D: figure anchor or style-forcing blocks (rule 8; pixar-look ch. 8/9).
4. Validate on ONE still + one motion-ladder test per model before rolling out (style-control §5b); the recipe's Verify line becomes the standing reroll gate.
5. Write the final style anchor into the bible; from then on it is canon, reused verbatim.
Exit: style anchor in the bible + a passing verify still.

## W8 — A generation keeps failing (trigger: 2+ failed runs on the same axis)
1. Suspect the PROMPT first (~8/10 presumed model limits were prompt faults, rule 14): lint for internal contradictions, missing positive lock on the failing axis, stacked instructions on one axis, meta commentary (ch. 24b).
2. Rewrite short from scratch — never patch past 3 iterations.
3. Still failing → change CHANNEL, not vocabulary: reference/sketch/mask/clay render/seed reroll/other model (ch. 24b.7; stills ladders ch. 24c–g; video ch. 14b).
4. Only after a clean minimal prompt fails twice on the same axis: declare a model limit, route the shot to another model (renderability matrix) or rescue/rewrite the beat (renderability rescue paths). Flag a kept risk in the register.
Exit: working result, or a documented model limit with a rescue.

## W9 — Session open & close (trigger: every working session in an existing project)
Open: load the production bible FIRST (rule 11); read only what the next step needs; revalidate the platform receipt for every active generation route (surface/tool, model + mode, UI/MCP version or dated snapshot, source/check date, account/workspace) before relying on a control.
Close: update the bible LAST — add each actual generation/edit's Receipt ID to the shot board or delivery note; statuses only on user approval, decisions as canon, open risks in the register; nothing outside the bible is canon. Offer ONCE to feed genuinely new production findings back to the public skill (generalized, no project content — SKILL.md closing section).

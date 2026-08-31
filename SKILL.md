---
name: ai-film-production
description: Plan and produce AI-generated video/film end to end - treatments, scripts, screenplays, shot lists, asset orders (character sheets, locations, props), and Seedance video prompts - optimized for current video models (Seedance 2.x, Veo 3.x, Kling 3.x, PixVerse, Hailuo) and the Higgsfield Cinema Studio pipeline. Use this skill whenever the user wants to write, review, or fix a treatment, script, Drehbuch, storyboard, shot list, scene, asset order, or generation prompt for an AI-generated film, short, ad, or social video — also when they ask "can this scene be generated?", "make this script AI-ready", "plan my AI film", or mention writing for Seedance / Veo / Kling / Higgsfield Cinema Studio. Trigger even if they don't say "AI" but the production path is clearly generative video.
---


# AI Film Production

Write, plan, and prompt AI-generated film so no shot looks AI-generated: design around the models' failure classes (identity drift, physics errors, anatomy, interaction, broken in-frame text) instead of fighting them in post. Output language follows the user (German user → German deliverables); keep technical terms (shot, plate, reverse, anchor) as-is.

**Role.** The agent is the user's full crew — DoP, editor, gaffer, script consultant, line producer — and the user is the director and only approval instance. Advise and moderate; the user directs and decides. Offer craft knowledge, flag a real risk ONCE in plain language, then follow their call. Do not gate, do not cite chapter numbers at the user, do not repeat heard warnings. When the user gives a feeling, propose the craft; when they give an instruction, execute it and briefly note its effect; when they name a style, start from the recipes.

**Scope & version:** v2.5-en (2026-08). Universal — nothing project- or person-specific. Prompt syntax is Seedance-2.x/Higgsfield-first with full cross-model profiles. Every rule carries a confidence label (🟢 verified/production-proven · 🟡 single-source · 🔴 marketing claim) and source tags; source conflicts are marked ⚠️, and [PP] marks first-party production evidence. **Platform/UI/MCP evidence rule:** every stored or user-facing platform claim must identify `platform → surface/tool → model + mode → vendor version or unversioned-UI snapshot → source URL + checked date`. For MCP also retain server URL, exposed tool/schema, provider account/workspace and billing route. Never invent a semantic UI/MCP version; write `unversioned UI @ date` instead.

## Task routing — read exactly this, then act

| Task at hand | Read (one file, fully) |
|---|---|
| Resume a running project; "where were we"; project state, asset registry, shot status | `references/production-bible.md` — load the project's bible FIRST, then only what the next step needs |
| Project start with a known genre ("Actionfilm", "Horror-Kurzfilm", "Doku-Stil" …) | `references/genre-baselines.md` — craft defaults + recipe shortlist + which files to load for THIS project type. Read FIRST, before other references |
| User brings a story/idea and needs the dramaturgical shape; story completeness check | `references/story-structures.md` — intake gate + container library (3-act, hero's journey, kishōtenketsu, A24 elevated-genre, sitcom, sketch, doc spines …) |
| Write/fix ANY video prompt (Seedance/CS) | `references/video-prompting.md` — block structure ch. 12 is the mandatory template; sequence prompting ch. 14 |
| Prompt syntax/profile for H3 / Kling / Veo / Grok (not current UI controls) | `references/platforms-models.md` — preserve its named model-version scope and verify live syntax before a paid run |
| Current Higgsfield Cinema Studio settings or any Higgsfield UI/MCP control | `references/platform-ui-workflows.md` — `HF-CS4@2026-08-31` is the current Cinema reference; never use the archived Cinema 3.5 table as a current selector list |
| Current UI, selectable modes, MCP versus web-UI scope, real user workflows, limits, or learning resources for Higgsfield / fal.ai / Runway / OpenArt / Arcads / ChatGPT | `references/platform-ui-workflows.md` — verify the live model subform and connected account/workspace before suggesting a paid generation |
| Treatment, script, shot list; asset orders (sheets, plates, props); model choice for stills; QA batches; reverse angles/coverage | `references/production-pipeline.md` |
| Any stylized look; any prompt that uses reference images; image-model mechanics | `references/style-control.md` |
| Position/size/count/exclusion problems in image prompts; a model "ignoring" an instruction; how generators process prompts | `references/image-model-logic.md` — ch. 24: generator writing contract (24b), control ladders, negation channel table, mask strictness |
| Lint a script/shot for feasibility; assign models; rescue risky action; lighting-consistency check | `references/renderability.md` |
| Cinematography/editing/light/color/dramaturgy advice; "how should this scene feel" | `references/film-craft.md` |
| User wants a style starting point or names a director or DoP | `references/director-recipes.md` — selection index (brief signal → shortlist + constraint filter), 31 director recipes + 11 DoP signatures, each with a Verify line (the reroll gate for stills/takes) |
| Pixar/3D-stylized projects | `references/pixar-look.md` (figure-anchor hard rule ch. 8, figure-less method ch. 9) |
| Post, upscaling, music/voices, continuity ledger, legal/AI-disclosure | `references/post-audio-legal.md` |
| Any recurring production job — new project, asset build-out, produce a shot/scene, repair a take, coverage, style lock, failing generation, session open/close | `references/workflows.md` — ch. 25: the runbook per job; pick by trigger |
| First production task ever / "how does this all connect" | `references/worked-example.md` |

Chapter numbers are global IDs — "ch. 12" always means the block structure, wherever cited.

## The rules that always apply (no file read needed)

1. **Stills-first:** every shot exists as an approved still before video; the look is won in the image.
2. **Plan in shots (4–12 s), generate in sequences** (15-s takes on Seedance 2.0 / 30-s on 2.5, 2–3 internal shots, explicit ENDING STATE; never a dramatic peak at a take's end).
3. **Complexity budget per shot:** one main action + one camera move + max two characters; split across cuts.
4. **Every video prompt uses the ch. 12 block structure** — standalone prompt in a code block, no style prefix, CAMERA in 3rd position, FOV in degrees, quantified values (km/h, %, Kelvin).
5. **References: attach → address — and plan the set BEFORE the prose.** Every reference gets a job line + exclusions; end with an attachment checklist in upload order. Assets carry stable @names, verbatim everywhere — approved shot anchors are registered as named elements too (`@anchor_1A`) and addressed by tag, never manually attached. On Seedance 2.5, every element that must stay consistent gets its OWN reference (30 images + 10 video + 10 audio per generation; classes incl. @Clay Render for staging/size and @Audio for voice) — prose is for what happens, references are for what persists (ch. 14b).
6. **Write the visible, in generator logic:** a prompt is a scene description for a caption-trained generator, not instructions to a reader (ch. 24b) — micro-cues instead of emotion labels, cause before reaction, positive locks next to what they protect, and ZERO internal contradictions (the model blends conflicts silently, it never warns). Descriptions of appearance/emotion stay positive; prohibitions may be negative — in the channel ch. 24f / ch. 14 assigns for the target model.
7. **Red-list lint before delivery:** no readable in-frame text, no mirror beats, no hand close-up actions, no readable-face crowds, no hero physics — ellipsis over simulation; write a rescue cut for every kept risk.
8. **Stylized 3D needs an anchor:** a figure in frame or the style-forcing blocks (pixar-look ch. 9) — a style word alone will be ignored.
9. **Audio:** diegetic only, describe it always, never generate music in the video model — the score is built in post.
10. **Deliver complete prompts as Render Slates:** every prompt the user is expected to execute ships with the slate table directly above its code block (contract after the checklist) — the code block stays pure prompt; operational context (route, settings, inputs, IDs) lives in the slate, never in the prompt prose. Then a short risk register: kept yellow/red shots, why, and their rescues.
11. **The production bible is canon:** multi-session projects keep ONE living bible (ch. 22) — read it first, update it last; statuses move only on user approval; if it isn't in the bible, it isn't canon.
12. **Repair before reroll (Seedance 2.5):** an approved take is fixed with the edit suite — region/timestamp-scoped, camera-perspective, green-screen, audio-category edits — or extended, never regenerated wholesale for a local fault. Draft at 10 s; grow to 30 s once the beats lock; from then on every fix is an edit (ch. 14b).
13. **Canon before invention — no guessed content, ever.** Every content claim in a prompt — what happens in the beat, who moves, what the light does — is READ from the treatment/script/bible for that exact beat before it is written, and checked once against scene physics and story logic. If the canon is silent on the question, SAY SO ("the treatment doesn't specify this beat"), offer 1–2 clearly-labeled PROPOSALS, and wait for the director's call — a proposal enters a prompt only after approval. Never invent a beat and translate it straight into a delivery prompt: packaging a guess in full prompt form (blocks, locks, QA gates) launders it into false authority, ships confidently, and burns render budget on slop. Before delivering ANY prompt, re-read it once against the canon passage and answer: does anything here contradict or exceed what is written? Fix or flag — never deliver silently.
14. **Prompt first, model last:** when a generation fails repeatedly, the default suspect is YOUR prompt, not the model — in production ~8 of 10 presumed "model limits" were badly written prompts. Before blaming the model, switching methods, or proposing to cut the shot, lint your own prompt: internal contradictions (e.g. tiny size + rich visible detail), missing positive lock on exactly the failing aspect, several stacked instructions on one axis (they average out, not add up), meta-commentary addressed at the model. Then rewrite short from scratch — never patch the same prompt past 3 iterations. A model limit may be declared only after a clean, minimal, contradiction-free prompt has failed on the same axis twice — and three failed runs on one axis mean the wrong CHANNEL, not the wrong words: escalate to reference/sketch/mask/seed/model (ch. 24b.7), never to a fourth vocabulary variant.
15. **Version receipt before an external generation:** every UI/MCP/API recommendation and every stored platform fact includes the active reference key (or the full five-part evidence record from Scope & version). For a paid run, recheck the live form/MCP tool schema and record the actual model/mode/account-workspace. “Current” without that receipt is not a usable production claim.

## The per-prompt checklist — run for EVERY new image or video prompt, in this order, no exceptions

Whenever a prompt for a new still or video generation (or edit/extension) is to be written, walk these seven steps top to bottom. Skipping a step is how slop happens; the steps exist because each one has failed expensively when skipped.

1. **CANON** — read the treatment/script/bible passage for this exact beat or asset. Every content claim must be readable there. Canon silent? Say so, offer labeled PROPOSALS, wait for the director (rule 13).
2. **ROUTE** — pick the target platform/surface, model and mode BEFORE writing, and attach the version receipt: platform → tool → model/mode → UI/MCP/API version or snapshot → source + check date. Stills: model matrix (production-pipeline ch. 5) + style mechanics (style-control). Video on Seedance 2.5: `t2v` / `omni_reference` / `video_edit` / `video_extension` — and first ask: is this actually a repair or extension of an existing take rather than a new generation (rule 12, ch. 14b)?
3. **REFERENCES** — plan the reference set before any prose: every element that must persist gets its own reference (@Image / @Video / @Audio / @Clay Render), each with a job line + exclusions, pulled from the project pool by exact tag (rule 5, ch. 14b). Prose is for what happens; references are for what persists.
4. **WRITE** — in the model's structure (video: ch. 12 block order; stills: style-control §2 / the ch. 24 control ladders), in generator logic (rule 6, ch. 24b): describe, don't argue; positive-first; one instruction per axis; numbers only into numeric channels; must-have element first.
5. **LINT** — three passes before anything is delivered: (a) contradiction lint — size vs. detail, conflicting styles/materials, positive vs. negative on the same attribute (ch. 24b: the model blends, it never warns); (b) renderability/red-list lint + rescue for every kept risk (rule 7); (c) canon re-read — does anything contradict or exceed the written beat? Fix or flag (rule 13).
6. **DELIVER** — as a Render Slate: slate table directly above the standalone prompt code block (contract below) — Render ID, intent, verified run-route (= the rule-15 receipt), settings, inputs in upload order; then the risk register with rescues (rules 4, 5, 10, 15).
7. **AFTER THE RESULT** — review in separate passes (identity → continuity → timing → camera → audio); on a fault, fix the weakest instruction in the NEXT prompt; on an approved take, every fix is an edit, never a reroll (rule 12); three failures on one axis = change channel, not vocabulary (rule 14).

## The Render Slate — delivery wrapper for every executable prompt

A director running several agents, sessions, platforms, and parallel renders cannot see from a bare code block what a prompt is for, where to run it, or what it needs. That context is operational information, not prompt prose — it goes in a compact **Render Slate**: a Markdown table immediately above the code block (key-value list where tables don't render). Use only applicable rows, in this order; omit unknown rows — no placeholders, no invented values. Adapt row labels to the user's output language; keep IDs and @tags ASCII-verbatim.

| Row | Content |
|---|---|
| `Render ID` | Collision-resistant ID of this exact prompt package: `<PROJECT>_<Shot ID>__<platform-model>__<operation>__P<nn>` |
| `Intent` | One director-readable line: shot, action, decisive creative constraint |
| `Run in` | Verified route: platform → project/workspace → surface/tool → model → operation/mode (= the rule-15 receipt) |
| `Settings` | Executable UI values (ratio, resolution, duration, audio, non-default controls) — settings live HERE, never duplicated inside the prompt (no double control) |
| `Inputs` | One reference per line: stable @tag + its one job, in upload order (carries rule 5's attachment checklist) |
| `Store in` | Known platform project/folder or local destination — omit rather than invent |
| `Handoff` | Only for linked work: extension boundary states, edit source + scope, or a continuity boundary |

**ID discipline:** the **Shot ID** is project canon from the shot board (`1A`, `SQ03_SC12_12A`) — never invent missing sequence/scene data. The **Render ID** appends platform/model, operation, and prompt-package revision (`…__HF-SD25__T2V__P01`; a rewrite is `P02`). A **Take ID** (`TK01`, `TK02`…) exists only once a generated result exists — never as a synonym for a prompt revision. Variant tokens only for deliberate creative alternatives, not reruns.

## Workflow

1. **Intake** — resuming? Load the production bible first (ch. 22). New project: if a genre is named or evident, read `genre-baselines.md` first (it pre-answers defaults and tells you which files this project needs). The story comes from the user — run the story intake gate and offer a dramaturgical container (story-structures ch. 23) before craft settles. Then settle only what the conversation hasn't: format/look (stylized and UGC absorb errors; photoreal demands discipline; almost-photoreal is the uncanny danger zone) · target length & platform · deliverable (treatment/script/shot list/prompts) · model stack · dialogue language (non-English → plan dubbing or VO structure now).
2. **Write shot-first, canon-first** — re-read the treatment/script/bible passage for the beat BEFORE writing anything (rule 13); content the canon doesn't answer is settled with the director first, never improvised into the prompt. Then: numbered shots with fixed camera grammar per sequence, object-anchored blocking (never screen directions), @asset names, match-action cues. Sequence dramaturgy: Establish → Action → Reaction → Detail; dialogue as shot/reverse-shot with reverse plates + 180° lock (strongest lock: the 3D blockout path, ch. 8).
3. **Lint** against renderability.md; rewrite or rescue every hit.
4. **Pre-production sections in the treatment** — set build (locations with locks + reverse decision), casting (sheet orders; for animation: expression sheets), style anchor (one paragraph, reused verbatim).
5. **Deliver** per the routing table's file for the format — treatments end each scene with its shot table (No. | Length | Shot | Action | Assets | Risk | Rescue); prompt shot lists follow rule 4 and rule 10. Close every work block by updating the production bible where the project keeps one (rule 11).

## Reference files (one line each)

- `video-prompting.md` — ch. 12 block structure (THE prompt template), 12b–12g, ch. 14 sequence prompting, ch. 14b Seedance 2.5 doctrine (reference-maximal control, edit suite, extension chains), ch. 15 style pointer.
- `production-pipeline.md` — ch. 1–11 pipeline/assets/QA/model choice, ch. 16 coverage ladder (read before ordering ANY reverse angle).
- `platforms-models.md` — archival Higgsfield Cinema context plus H3/Kling/Veo/Grok prompt-syntax profiles; never the authority for current UI/MCP selectors.
- `platform-ui-workflows.md` — dated, primary-source UI/workflow reference for Higgsfield, fal.ai, Runway, OpenArt, Arcads, and ChatGPT/GPT Image 2; web-versus-MCP routing, current capabilities/limits, learning links, and a re-verification gate.
- `post-audio-legal.md` — ch. 17 post & delivery, ch. 18 audio/music/voices, ch. 19 continuity checklists, ch. 20 legal & AI disclosure.
- `style-control.md` — style stack, GPT Image 2/Nano Banana mechanics, 15+ vocabularies, reference-integration protocol.
- `image-model-logic.md` — ch. 24: how generators read prompts; binding writing contract, position/scale/count ladders, negation channel table, edit locality & mask strictness per platform.
- `production-bible.md` — ch. 22 project-state convention: living bible template, session rules, platform mapping (Higgsfield Elements · Runway re-uploads · local/fal file tree), reroll budget.
- `story-structures.md` — ch. 23 dramaturgical containers: story intake gate, classic/alternative/format-specific structures, choosing and mixing rules.
- `renderability.md` — green/red lists, rescue paths, format matrix, lighting-consistency rule, model quick profiles.
- `film-craft.md` — composition, camera, editing, light, color, timing, dramaturgy; the combination logic.
- `director-recipes.md` — 31 director recipes + 11 DoP signatures + harmony map as optional starting points.
- `genre-baselines.md` — 13 genre entry points with subgenres, craft defaults, recipe shortlists, and per-genre skill filters.
- `pixar-look.md` — sourced Pixar look bible incl. figure-anchor rule and figure-less style forcing.
- `workflows.md` — ch. 25: nine runbooks chaining the chapters for the typical jobs (W1 new project · W2 asset/reference pool · W3 shot · W4 scene · W5 repair · W6 coverage · W7 style lock · W8 failing generation · W9 session open/close).
- `worked-example.md` — compact end-to-end mini production.

## Feeding production experience back

This skill is maintained publicly (github.com/iret77/ai-film-production). When production experience contradicts or extends a rule — a workaround that worked, a rule that failed, a platform behavior nobody documented — offer ONCE to draft a GitHub issue with the technical finding (no project content, no personal data). If the user declines, drop it and do not raise it again.

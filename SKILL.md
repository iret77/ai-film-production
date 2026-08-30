---
name: ai-film-production
description: Plan and produce AI-generated video/film end to end - treatments, scripts, screenplays, shot lists, asset orders (character sheets, locations, props), and Seedance video prompts - optimized for current video models (Seedance 2.x, Veo 3.x, Kling 3.x, Sora, PixVerse, Hailuo) and the Higgsfield Cinema Studio pipeline. Use this skill whenever the user wants to write, review, or fix a treatment, script, Drehbuch, storyboard, shot list, scene, asset order, or generation prompt for an AI-generated film, short, ad, or social video — also when they ask "can this scene be generated?", "make this script AI-ready", "plan my AI film", or mention writing for Seedance / Veo / Kling / Higgsfield Cinema Studio. Trigger even if they don't say "AI" but the production path is clearly generative video.
---


# AI Film Production

Write, plan, and prompt AI-generated film so no shot looks AI-generated: design around the models' failure classes (identity drift, physics errors, anatomy, interaction, broken in-frame text) instead of fighting them in post. Output language follows the user (German user → German deliverables); keep technical terms (shot, plate, reverse, anchor) as-is.

**Role.** The agent is the user's full crew — DoP, editor, gaffer, script consultant, line producer — and the user is the director and only approval instance. Advise and moderate; the user directs and decides. Offer craft knowledge, flag a real risk ONCE in plain language, then follow their call. Do not gate, do not cite chapter numbers at the user, do not repeat heard warnings. When the user gives a feeling, propose the craft; when they give an instruction, execute it and briefly note its effect; when they name a style, start from the recipes.

**Scope & version:** v2.4-en (2026-08). Universal — nothing project- or person-specific. Prompt syntax is Seedance-2.x/Higgsfield-first with full cross-model profiles. Every rule carries a confidence label (🟢 verified/production-proven · 🟡 single-source · 🔴 marketing claim) and source tags; source conflicts are marked ⚠️, and [PP] marks first-party production evidence.

## Task routing — read exactly this, then act

| Task at hand | Read (one file, fully) |
|---|---|
| Resume a running project; "where were we"; project state, asset registry, shot status | `references/production-bible.md` — load the project's bible FIRST, then only what the next step needs |
| Project start with a known genre ("Actionfilm", "Horror-Kurzfilm", "Doku-Stil" …) | `references/genre-baselines.md` — craft defaults + recipe shortlist + which files to load for THIS project type. Read FIRST, before other references |
| User brings a story/idea and needs the dramaturgical shape; story completeness check | `references/story-structures.md` — intake gate + container library (3-act, hero's journey, kishōtenketsu, A24 elevated-genre, sitcom, sketch, doc spines …) |
| Write/fix ANY video prompt (Seedance/CS) | `references/video-prompting.md` — block structure ch. 12 is the mandatory template; sequence prompting ch. 14 |
| Prompt for H3 / Kling / Veo / Grok; Higgsfield UI/settings questions | `references/platforms-models.md` |
| Treatment, script, shot list; asset orders (sheets, plates, props); model choice for stills; QA batches; reverse angles/coverage | `references/production-pipeline.md` |
| Any stylized look; any prompt that uses reference images; image-model mechanics | `references/style-control.md` |
| Lint a script/shot for feasibility; assign models; rescue risky action; lighting-consistency check | `references/renderability.md` |
| Cinematography/editing/light/color/dramaturgy advice; "how should this scene feel" | `references/film-craft.md` |
| User wants a style starting point or names a director or DoP | `references/director-recipes.md` — selection index (brief signal → shortlist + constraint filter), 31 director recipes + 11 DoP signatures, each with a Verify line (the reroll gate for stills/takes) |
| Pixar/3D-stylized projects | `references/pixar-look.md` (figure-anchor hard rule ch. 8, figure-less method ch. 9) |
| Post, upscaling, music/voices, continuity ledger, legal/AI-disclosure | `references/post-audio-legal.md` |
| First production task ever / "how does this all connect" | `references/worked-example.md` |

Chapter numbers are global IDs — "ch. 12" always means the block structure, wherever cited.

## The rules that always apply (no file read needed)

1. **Stills-first:** every shot exists as an approved still before video; the look is won in the image.
2. **Plan in shots (4–12 s), generate in sequences** (15-s takes on Seedance 2.0 / 30-s on 2.5, 2–3 internal shots, explicit ENDING STATE; never a dramatic peak at a take's end).
3. **Complexity budget per shot:** one main action + one camera move + max two characters; split across cuts.
4. **Every video prompt uses the ch. 12 block structure** — standalone prompt in a code block, no style prefix, CAMERA in 3rd position, FOV in degrees, quantified values (km/h, %, Kelvin).
5. **References: attach → address.** Every reference gets a job line + exclusions; end with an attachment checklist in upload order. Assets carry stable @names, verbatim everywhere — approved shot anchors are registered as named elements too (`@anchor_1A`) and addressed by tag, never manually attached.
6. **Write the visible:** micro-cues instead of emotion labels, cause before reaction, positive locks next to what they protect. Descriptions of appearance/emotion stay positive; prohibitions may be negative.
7. **Red-list lint before delivery:** no readable in-frame text, no mirror beats, no hand close-up actions, no readable-face crowds, no hero physics — ellipsis over simulation; write a rescue cut for every kept risk.
8. **Stylized 3D needs an anchor:** a figure in frame or the ch.-9 style-forcing blocks — a style word alone will be ignored.
9. **Audio:** diegetic only, describe it always, never generate music in the video model — the score is built in post.
10. **Deliver complete prompts** (named 1A/1B/2A…), then a short risk register: kept yellow/red shots, why, and their rescues.
11. **The production bible is canon:** multi-session projects keep ONE living bible (ch. 22) — read it first, update it last; statuses move only on user approval; if it isn't in the bible, it isn't canon.

## Workflow

1. **Intake** — resuming? Load the production bible first (ch. 22). New project: if a genre is named or evident, read `genre-baselines.md` first (it pre-answers defaults and tells you which files this project needs). The story comes from the user — run the story intake gate and offer a dramaturgical container (story-structures ch. 23) before craft settles. Then settle only what the conversation hasn't: format/look (stylized and UGC absorb errors; photoreal demands discipline; almost-photoreal is the uncanny danger zone) · target length & platform · deliverable (treatment/script/shot list/prompts) · model stack · dialogue language (non-English → plan dubbing or VO structure now).
2. **Write shot-first** — numbered shots with fixed camera grammar per sequence, object-anchored blocking (never screen directions), @asset names, match-action cues. Sequence dramaturgy: Establish → Action → Reaction → Detail; dialogue as shot/reverse-shot with reverse plates + 180° lock (strongest lock: the 3D blockout path, ch. 8).
3. **Lint** against renderability.md; rewrite or rescue every hit.
4. **Pre-production sections in the treatment** — set build (locations with locks + reverse decision), casting (sheet orders; for animation: expression sheets), style anchor (one paragraph, reused verbatim).
5. **Deliver** per the routing table's file for the format — treatments end each scene with its shot table (No. | Length | Shot | Action | Assets | Risk | Rescue); prompt shot lists follow rule 4 and rule 10. Close every work block by updating the production bible (rule 11).

## Reference files (one line each)

- `video-prompting.md` — ch. 12 block structure (THE prompt template), 12b–12g, ch. 14 sequence prompting, ch. 15 style pointer.
- `production-pipeline.md` — ch. 1–11 pipeline/assets/QA/model choice, ch. 16 coverage ladder (read before ordering ANY reverse angle).
- `platforms-models.md` — ch. 13 Higgsfield CS settings/platform, ch. 21 H3/Kling/Veo/Grok syntax profiles.
- `post-audio-legal.md` — ch. 17 post & delivery, ch. 18 audio/music/voices, ch. 19 continuity checklists, ch. 20 legal & AI disclosure.
- `style-control.md` — style stack, GPT Image 2/Nano Banana mechanics, 15+ vocabularies, reference-integration protocol.
- `production-bible.md` — ch. 22 project-state convention: living bible template, session rules, platform mapping (Higgsfield Elements · Runway re-uploads · local/fal file tree), reroll budget.
- `story-structures.md` — ch. 23 dramaturgical containers: story intake gate, classic/alternative/format-specific structures, choosing and mixing rules.

## Feeding production experience back

This skill is maintained publicly (github.com/iret77/ai-film-production). When production experience contradicts or extends a rule — a workaround that worked, a rule that failed, a platform behavior nobody documented — offer ONCE to draft a GitHub issue with the technical finding (no project content, no personal data). If the user declines, drop it and do not raise it again.
- `renderability.md` — green/red lists, rescue paths, format matrix, lighting-consistency rule, model quick profiles.
- `film-craft.md` — composition, camera, editing, light, color, timing, dramaturgy; the combination logic.
- `director-recipes.md` — 31 director recipes + 11 DoP signatures + harmony map as optional starting points.
- `genre-baselines.md` — 12 genre entry points with subgenres, craft defaults, recipe shortlists, and per-genre skill filters.
- `pixar-look.md` — sourced Pixar look bible incl. figure-anchor rule and figure-less style forcing.
- `worked-example.md` — compact end-to-end mini production.

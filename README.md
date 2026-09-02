# ai-film-production

![From clay blockout to final take — one continuous scene, one method](assets/hero.jpg)

[![Download the latest skill (.skill)](https://img.shields.io/badge/download-latest%20skill%20(.skill)-2563eb?style=flat-square)](https://github.com/iret77/ai-film-production/releases/latest/download/ai-film-production.skill)

A complete film-production methodology for Claude — 25 chapters of sourced, confidence-labeled craft that turn the model into your crew: DoP, editor, gaffer, script consultant, line producer. You stay the director. Built for a **Seedance 2.5 / Higgsfield Cinema Studio** stills-first pipeline, with a MiniMax H3 profile rebuilt on MiniMax's official prompt-writing guides and compact syntax profiles for Kling 3.0, Veo 3.1, and Grok Imagine.

## The problem

AI video is easy to generate and hard to direct. The default way people prompt a video model looks like this:

```
Epic cinematic shot of a hero on a wooden ship in a violent storm,
ultra realistic, 8k, dramatic lighting, masterpiece, trending
```

What comes back: a drifting face, physics from a dream, a camera that does whatever it wants, quality words the model never reads — and after five rerolls, render budget spent on slop. There is room for something better. How about:

```
SCENE CONTEXT   Ilias crosses the storm deck toward the mast while the crew
                hauls a torn sail. Night, mid-Aegean.
ACTIVE REFERENCES
                @ilias — 30s, lean deckhand, soaked linen shirt, rope-scarred
                hands. 100% matches the reference.
CAMERA          Handheld at chest height, 3 m behind @ilias, matching his
                pace at 5 km/h; no drift mid-segment.
ACTION          0-4s: @ilias grabs the rail, a wave bursts over the bow —
                spray hits him a beat later, he flinches, keeps moving. …
LIGHTING        Single practical: swinging deck lantern, 3200K, hard swings
                of shadow with the ship's roll.
POSITIVE LOCKS  Lantern stays lit in every frame. The crew stays aft of the
                mast. One continuous shot, no cuts.
```

Same model. The difference is method: every aspect has one home, everything is measurable, and the prompt is written in the logic the model was trained on — not in the logic of a human reader.

## How it works

It starts the moment you say "plan my short film." The skill doesn't jump into prompts. It reads your genre's craft baseline, asks for the story before the style, and offers a dramaturgical container. Then it builds the way productions build: locations and cast as approved reference assets first, every shot as an approved still before any video — attached as a reference anchor, not as a start frame, unless a take must chain frame-exactly onto an existing clip — every prompt through a fixed seven-step checklist — canon, routing, references, writing, lint, delivery, review. When a take comes back 90% right, it doesn't reroll; it repairs the 10% with the platform's edit modes. And everything that survives your approval becomes canon in a living production bible, so the next session picks up exactly where this one stopped.

Claude just runs a film production.

## Quick start

1. [Download the latest `ai-film-production.skill`](https://github.com/iret77/ai-film-production/releases/latest/download/ai-film-production.skill) — built automatically for every release. It's a zip with a custom suffix; macOS won't auto-extract it.
2. Upload it in Claude's skill settings (the dialog takes `.skill` directly), or unzip into your agent's skills path (e.g. `~/.claude/skills/` for Claude Code).
3. Talk to it like a director:

> "Break this logline into a treatment with a shot list: a lighthouse keeper finds a message that was never sent."
> "Make this scene AI-ready — can it even be generated?"
> "The take is perfect except the camera. Fix it without touching the performance."

The skill triggers on its own whenever the production path is clearly generative video — treatments, scripts, shot lists, asset orders, Seedance/Veo/Kling/Higgsfield prompts.

## What's inside

**25 chapters · 16 always-on rules · a 7-step per-prompt checklist · 9 workflow runbooks · 13 genre baselines · 31 director recipes + 11 DoP signatures · 15+ style vocabularies · 6 video models profiled.**

- **Direction & craft** — model-independent film language (composition, editing, light, color, dramaturgy), director and DoP recipes with per-recipe verify gates, genre entry points, story structures from three-act to kishōtenketsu.
- **Prompting method** — the block-structure prompt template with camera-third ordering and FOV-in-degrees discipline; how image models actually read prompts (position, scale, count, negation — with the research receipts); style enforcement that survives more than one shot.
- **Production operations** — stills-first pipeline, asset and reference-pool build-out, renderability linting with green/red lists and rescue paths, coverage ladder, continuity ledger, a living production-bible convention for multi-session projects.
- **Platform knowledge** — Seedance 2.5 doctrine (50-reference control incl. clay-render staging — Blender-built or Seedance-generated — the edit suite, extension chains), Higgsfield Cinema Studio settings, the MiniMax H3 official schema (cut-point timestamps, six-section reference form, retention markers), compact profiles for Kling, Veo, and Grok, production rules distilled from Higgsfield's open-sourced feature films (headless sheets, one asset per state, speech-count lock, crowd scale in three layers, the negation third class), dated platform caveats, and a real-face moderation plan for licensed likenesses.

## Why you'd use it — and why you wouldn't

**Use it if** you want AI footage that doesn't look AI-generated: the whole method designs every shot around the failure classes of current video models — identity drift, physics errors, broken in-frame text, interaction errors — instead of fighting them in post. And if you burn money on rerolls: the checklist, the lint passes, and the repair-before-reroll rule exist because every skipped step has already cost real render budget.

**Skip it if** you want a one-click text-to-video toy — this is a methodology that expects a director's decisions, and it will ask for them. Skip it if your pipeline is built on a stack it doesn't cover deeply (it's Seedance/Higgsfield-first; MiniMax H3 gets a full official-schema profile, Kling, Veo, and Grok compact profiles, everything else principles only). And know that model facts age in weeks: version-volatile claims are marked as such and should be re-verified against the live platforms before a production run.

## Where the rules come from

No rule ships without a label: 🟢 verified across sources / official / production-proven · 🟡 plausible but single-source or untested · 🔴 marketing claim — test yourself. Source tags ([H-off], [BD-off], [MM-off], [F], [P1–P49] — itemized in `references/sources.md` —, [PP], [W], …) trace every rule to its origin — official platform docs and prompt-writing guides, the vendor's own open-sourced feature-film breakdowns, practitioner protocols, deep-research passes over papers and benchmarks, and first-party production sessions whose lessons flow back here as generalized rules. Where sources conflict, the conflict is documented with ⚠️ instead of silently resolved.

## Philosophy

- **Stills-first** — the look is won in the image; video only secures it.
- **Canon before invention** — every beat is read from the script, never guessed into a prompt.
- **References over prose** — prose is for what happens; references are for what persists.
- **Repair before reroll** — an approved take is edited, never re-diced.
- **Ellipsis over simulation** — what the model can't render, the edit implies.

## Structure

<details>
<summary>All 19 files at a glance</summary>

| File | Role |
|---|---|
| `SKILL.md` | Entry point: task routing table, 16 inline always-rules, the mandatory per-prompt checklist, 5-step project workflow |
| `references/genre-baselines.md` | 13 genre entry points (incl. Commercial/Ad): craft defaults, subgenres, recipe shortlists, per-genre skill filters |
| `references/production-pipeline.md` | Ch. 1–11 + 16: pipeline principles, assets, QA, model choice, coverage ladder, interview production path (7b) |
| `references/video-prompting.md` | Ch. 12 + 14 + 14b: THE block-structure prompt template, cross-model adaptation, sequence prompting, negation classes, Seedance 2.5 doctrine (reference-maximal control, edit suite, extension chains, large casts, montage ceiling, Dreamina-only surfaces) |
| `references/platforms-models.md` | Ch. 13 + 21: archival Higgsfield Cinema Studio notes; MiniMax H3 profile on the official guides (three-field base form, six-section Ref2VA, camera vocabulary, dialogue tags); Kling/Veo/Grok compact profiles |
| `references/platform-ui-workflows.md` | Current, source-linked UI/workflow reference and version ledger: which web/MCP/ChatGPT surface owns each selectable setting in Higgsfield, fal.ai, Runway, OpenArt, Arcads, and GPT Image 2; plus re-verification rules |
| `references/post-audio-legal.md` | Ch. 17–20: post, audio/music/voices, continuity, legal & AI disclosure |
| `references/style-control.md` | Style enforcement across image and video models, vocabularies, reference protocol |
| `references/image-model-logic.md` | Ch. 24: how generators read prompts — writing contract, position/scale/count/negation recipes, mask strictness per platform |
| `references/renderability.md` | Green/red lists, rescue paths, format matrix, model quick profiles |
| `references/film-craft.md` | Model-independent film language: composition, camera, editing, light, color, timing, dramaturgy |
| `references/director-recipes.md` | 31 director recipes + 11 DoP signatures; selection index, per-recipe Verify gates, harmony map |
| `references/pixar-look.md` | Sourced Pixar look bible incl. figure-anchor rule, style-forcing method, and the hybrid previs-to-AI case study (wide-shot rescue, hidden faces, style donor) |
| `references/production-bible.md` | Ch. 22: living project-state document — template, session rules, platform mapping |
| `references/story-structures.md` | Ch. 23: dramaturgical containers — intake gate, classic/alternative structures, series poles & online-native formats |
| `references/workflows.md` | Ch. 25: nine runbooks for the typical production jobs — project start to session close |
| `references/worked-example.md` | Compact end-to-end mini production |
| `references/sources.md` | Registry of practitioner and vendor-thread protocols P17–P49 plus the official MiniMax guides [MM-off] (date, URL, sponsorship flag) behind the source tags |
| `LICENSE` | MIT |

</details>

## Versioning

v2.9-en (2026-09). Universal — contains nothing project- or person-specific. This repository is the source of truth for the skill; lessons from production flow back here via commits, and every release ships an upload-ready `.skill` package.

## License

[MIT](LICENSE).

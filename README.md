# ai-film-production

[![Download the latest skill (.skill)](https://img.shields.io/badge/download-latest%20skill%20(.skill)-2563eb?style=flat-square)](https://github.com/iret77/ai-film-production/releases/latest/download/ai-film-production.skill)

A [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) for planning and producing AI-generated video and film end to end: treatments, scripts, shot lists, asset orders (character sheets, locations, props), and generation-ready video prompts.

Optimized for a **Seedance 2.x / Higgsfield Cinema Studio 4.0** stills-first pipeline, with a full MiniMax H3 syntax profile and compact profiles for Kling 3.0, Veo 3.1, and Grok Imagine. The core craft it encodes: design every shot around the failure classes of current video models (identity drift, physics errors, broken in-frame text, interaction errors) instead of fighting them in post — so the result doesn't look AI-generated.

## Structure

| File | Role |
|---|---|
| `SKILL.md` | Entry point: task routing table, inline always-rules, 5-step workflow |
| `references/genre-baselines.md` | 12 genre entry points: craft defaults, subgenres, recipe shortlists, per-genre skill filters |
| `references/production-pipeline.md` | Ch. 1–11 + 16: pipeline principles, assets, QA, model choice, coverage ladder |
| `references/video-prompting.md` | Ch. 12 + 14: THE block-structure prompt template, cross-model adaptation, sequence prompting |
| `references/platforms-models.md` | Ch. 13 + 21: Higgsfield Cinema Studio, H3/Kling/Veo/Grok syntax profiles |
| `references/post-audio-legal.md` | Ch. 17–20: post, audio/music/voices, continuity, legal & AI disclosure |
| `references/style-control.md` | Style enforcement across image and video models, vocabularies, reference protocol |
| `references/renderability.md` | Green/red lists, rescue paths, format matrix, model quick profiles |
| `references/film-craft.md` | Model-independent film language: composition, camera, editing, light, color, timing, dramaturgy |
| `references/director-recipes.md` | 21 director recipes + 9 DoP signatures + harmony map |
| `references/pixar-look.md` | Sourced Pixar look bible incl. figure-anchor rule and style-forcing method |
| `references/worked-example.md` | Compact end-to-end mini production |

## Confidence system

Every rule carries a label: 🟢 verified across sources / official / production-proven · 🟡 plausible but single-source or untested · 🔴 marketing claim — test yourself. Source tags ([H-off], [BD-off], [F], [P1–P18], [W], …) trace each rule to its origin; conflicts between sources are documented with ⚠️ marks rather than silently resolved.

## Installation

**Fastest (Claude apps):** [download the latest `ai-film-production.skill`](https://github.com/iret77/ai-film-production/releases/latest/download/ai-film-production.skill) — built automatically for every release — and upload it in Claude's skill settings. The upload dialog takes a `.skill` package directly, and macOS won't auto-extract it on download (a `.skill` is a zip with a custom suffix).

Or do it by hand: package the repo as a skill (zip `SKILL.md` + `references/` with the folder name `ai-film-production`) and upload it in Claude's skill settings, or place the directory in your agent's skills path (e.g. `~/.claude/skills/` for Claude Code).

## Scope & versioning

v2.0-en (2026-08). Universal — contains nothing project- or person-specific. Model capabilities, platform UIs, and pricing change fast; version-volatile facts are marked as such in the references and should be re-verified in the live platforms before production runs. This repository is the source of truth for the skill; lessons from production flow back here via commits.

## License

See [LICENSE](LICENSE).

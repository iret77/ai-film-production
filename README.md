# ai-film-production

A [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) for planning and producing AI-generated video and film end to end: treatments, scripts, shot lists, asset orders (character sheets, locations, props), and generation-ready video prompts.

Optimized for a **Seedance 2.x / Higgsfield Cinema Studio 4.0** stills-first pipeline, with a full MiniMax H3 syntax profile and compact profiles for Kling 3.0, Veo 3.1, and Grok Imagine. The core craft it encodes: design every shot around the failure classes of current video models (identity drift, physics errors, broken in-frame text, interaction errors) instead of fighting them in post — so the result doesn't look AI-generated.

## Structure

| File | Role |
|---|---|
| `SKILL.md` | Entry point: trigger description + 5-step workflow (intake → shot-first writing → renderability lint → pre-production sections → delivery) |
| `references/pipeline.md` | The consolidated production rulebook, 21 chapters — pipeline principles through cross-model syntax profiles |
| `references/style-control.md` | Style enforcement across image and video models: style stack hierarchy, per-model mechanics, 15+ style vocabularies, reference-integration protocol |
| `references/renderability.md` | Green/red element lists, rescue paths for risky action, format matrix, model quick profiles |
| `references/pixar-look.md` | Sourced look bible for Pixar/3D-stylized projects |
| `references/worked-example.md` | A compact end-to-end mini production showing how the chapters connect |
| `references/protocols-archive.md` | Raw source protocols (German-language appendix) — the unconsolidated research the rules were distilled from |

## Confidence system

Every rule carries a label: 🟢 verified across sources / official / production-proven · 🟡 plausible but single-source or untested · 🔴 marketing claim — test yourself. Source tags ([H-off], [BD-off], [F], [P1–P16], [W], …) trace each rule to its origin; conflicts between sources are documented with ⚠️ marks rather than silently resolved.

## Installation

Package the repo as a skill (zip `SKILL.md` + `references/` with the folder name `ai-film-production`) and upload it in Claude's skill settings, or place the directory in your agent's skills path (e.g. `~/.claude/skills/` for Claude Code).

## Scope & versioning

v1.0-en (2026-08). Universal — contains nothing project- or person-specific. Model capabilities, platform UIs, and pricing change fast; version-volatile facts are marked as such in the references and should be re-verified in the live platforms before production runs. This repository is the source of truth for the skill; lessons from production flow back here via commits.

## License

See [LICENSE](LICENSE).

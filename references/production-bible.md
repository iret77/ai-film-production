# Production Bible: Project State Across Sessions (Ch. 22)

One living markdown document per project — the single source of truth for everything a fresh session needs to continue losslessly. Industry ground rule: **if it isn't in the bible, it isn't canon** — a decision that lives only in a chat that ended does not exist. The bible is operational memory; the creative grammar it carries (recipe, style anchor) is decided once and then quoted, not re-litigated.

## 22a. Rules

1. **Session boot:** on any resumed project, read the bible FIRST — before answering, before generating. No bible offered? Ask for it once, or offer to create one from the conversation.
2. **Session close:** update the bible at the end of every work block (statuses, decisions, handoff). The agent proposes the update; wording of decisions stays terse.
3. **Approval is the user's:** statuses move forward (draft → approved → locked) only on explicit user approval. The agent never self-approves; a regenerated asset resets to draft.
4. **The bible mirrors platforms, it does not replace them.** Binary assets live in the platform (Higgsfield Elements/Soul ID, OpenArt characters, local files for fal pipelines); the bible holds names, IDs, statuses, and pointers. On conflict, the approved image/element is the visual truth, the bible is the record of WHICH one is approved.
5. **Compact by force:** the whole bible stays pasteable into a fresh chat (target: 2–4 pages). Superseded decisions and finished shots move to an ARCHIVE section at the bottom or a second file; the active surface stays small.
6. **One bible per project.** Series/episodic work: one project bible (world, cast, style contract) + one slim episode sheet per episode (shot board, episode decisions). The pole decides the split (story-structures ch. 23d): **episodic** — universe facts live ONLY in the project bible and change only at season boundaries, episode sheets stay throwaway-slim; **serialized** ("the overlong film") — shot board and continuity ledger span the season in the project bible, episode sheets carry only the episode's micro-shape and status.
7. **Platform receipt is mandatory.** Before a generation, edit, or model-choice decision becomes canon, record: `platform → access route (web UI / MCP / ChatGPT / API) → surface/tool → model + mode/endpoint → vendor version or unversioned UI snapshot → source URL + checked date → account/workspace/project`. Never transfer a setting merely because two surfaces share a provider or model name.

## 22b. Template (copy, fill, keep)

```markdown
# <PROJECT> — Production Bible          last update: <date> · by <session/user>

## 1 · Frame
Format/length: … · Platform target(s) + aspect ratio(s): …
Model stack: stills … · motion … · edit/post …
Dialogue language: … · AI-disclosure duty: … (post-audio-legal ch. 20)

## 1b · Platform / UI / MCP version receipts
| Receipt ID | Platform + access route | Surface / tool | Model + mode / endpoint | Vendor version or UI snapshot | Evidence URL + checked date | Account / workspace / project | Result / asset IDs |
|---|---|---|---|---|---|---|---|
| HF-CS4@2026-08-31 | Higgsfield · web UI | Cinema Studio | … | Cinema Studio 4.0 | … · checked 2026-08-31 | … | … |

For an unversioned web form write `unversioned UI @ YYYY-MM-DD`; for MCP also retain its server URL and the exposed tool/schema. Every actual generation/edit cites its Receipt ID in the shot board or delivery note. The live selected form and connected workspace always outrank an old receipt.

## 2 · Style contract (decided — quote, don't re-litigate)
Premise (one sentence the ending proves): …
Container: <structure from ch. 23, one line> · Series pole (if series): episodic / serialized / anthology
Recipe: <name or synthesis, one line why>
Style anchor (VERBATIM in every prompt):
> …
Verify line (QA gate for every still/take): …
Genre baseline: <genre> — deviations: …

## 3 · Asset registry
| @name | Type | Status | Source of truth | Platform IDs / path | Job line + exclusions |
|---|---|---|---|---|---|
| @hero | character | locked | sheet v3 (link/element) | HF element …, Soul ID … / file … | face+outfit lock; never: … |
| @loc_bar | location | approved | master plate v2 | … | light side left; reverse: @loc_bar_rev |
| @anchor_1A | anchor | approved | still 1A final | HF element … / file … | reference anchor take 1A |
Types: character · location · prop · anchor · style-ref. Every approved shot still
becomes an @anchor_* entry (production-pipeline ch. 1).

## 4 · Shot board
| Shot | Len | Status | Anchor | Platform receipt | Risk → rescue | Takes used |
|---|---|---|---|---|---|---|
| 1A | 8s | final | @anchor_1A | HF-CS4@2026-08-31 | — | 3 |
| 1B | 6s | stills | @anchor_1B | … | hands close-up → cut to reaction | 0 |
Status ladder: planned → stills (approved still exists) → take (approved take) → final (in edit).
ID discipline (SKILL.md Render Slate): Shot ID = canon here; Render IDs (`…__P01`) identify prompt-package revisions; Take IDs (`TK01`…) exist only for generated results — "Takes used" counts Take IDs, never prompt revisions.

## 5 · Reroll budget & spend priorities
Planned takes per shot class: standard … · face/emotion peaks … · long takes/oners …
Spend the budget where the recipe says (its AI note); stop rule: after N failed
rerolls, fix the weakest instruction or invoke the shot's rescue — don't spin.
Spent so far: … (update per block)

## 6 · Decision log (append-only, one line each)
<date> — <decision> — <why / alternative rejected>

## 7 · Continuity log (never closes — post-audio-legal ch. 19)
Wardrobe/props/light state per scene; changes only via decision log entry.

## 8 · Handoff
Last state: … · Next: 1) … 2) … · Open questions for the user: …

## ARCHIVE
<superseded decisions, finished-and-delivered shots>
```

## 22c. Platform mapping (what the registry means per platform)

**Version boundary:** these are storage/continuity patterns, not promises about the current selector set of a platform. For live UI or MCP choices, first record a version receipt above and consult `platform-ui-workflows.md` for the matching dated reference key.

- 🟢 **Higgsfield / Cinema Studio:** Elements (characters, locations, props — and registered anchors, platforms-models ch. 13) and Soul ID persist platform-side; the registry's "Platform IDs" column records the element names verbatim so prompts and bible use identical tags. The platform's own shared Project Brief may exist for teams — the bible remains the agent-facing source of truth and must not contradict it.
- 🟡 **Runway:** references do not reliably persist across sessions (Director Mode re-anchors per session — competitor-sourced claim, verify on current version ⚠️). Consequence: the registry's "Source of truth" column must point to re-uploadable files for every character/style ref, and the session-boot step includes re-attaching them.
- 🟡 **OpenArt:** character objects persist but community reports drift; keep the sheet-based anchor discipline (production-pipeline ch. 3) as the real lock, the platform character as convenience.
- 🟢 **fal via MCP/API, local pipelines:** treat the local file tree as the durable asset store unless the selected, version-recorded fal endpoint/workspace says otherwise. The registry's path column is canonical; keep one folder per asset type (`assets/characters/`, `assets/locations/`, `assets/anchors/`, `takes/`), filenames = @names + version (`anchor_1A_v2.png`). The bible lives at the project root next to them.
- **Mixed stacks** (e.g. stills local via fal, motion on Higgsfield): one registry row can carry both a path and an element ID; the status column is shared — an asset is approved once, everywhere.

## 22d. Why this exists

Working studio pipelines converge on the same shape: script → shot breakdown → references → generation with planned retakes → review → post, with a shared brief and a reusable asset store carrying consistency. The failure mode this file prevents: project knowledge scattered across chat histories, loose anchor images, and platform sessions — each resumed session rebuilding context from memory, drifting a little each time. The bible is the fixed point; sessions come and go.

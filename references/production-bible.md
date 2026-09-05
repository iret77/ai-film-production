# Production Bible: Project State Across Sessions (Ch. 22)

One living markdown document per project — the single source of truth for everything a fresh session needs to continue losslessly. Industry ground rule: **if it isn't in the bible, it isn't canon** — a decision that lives only in a chat that ended does not exist. The bible is operational memory; the creative grammar it carries (recipe, style anchor) is decided once and then quoted, not re-litigated. Bible sections are cited as `bible section B3`, never as `ch. 3`.

## 22a. Rules

1. **Session boot:** on any resumed project, read the bible FIRST — before answering, before generating. No bible offered? Ask for it once (once = once per session when no bible exists), or offer to create one from the conversation. EVERY project gets a bible before its first asset order (SKILL rule 11, W1 step 5).
2. **Session close:** update the bible at the end of every work block (statuses, decisions, handoff). The agent proposes the update; wording of decisions stays terse. Shot-list edits follow "update only what changed": rewrite ONLY the named shot (1A, 1B) and reproduce every other shot word for word — never let the rewrite drift into neighbouring prompts [H-off, P47]. A rewritten prompt is a NEW revision, never an overwrite: bump the Render ID (`…__P01` → `…__P02`, SKILL.md ID discipline), set the shot board's `Current Render ID` to it, and append one row to the render/take log (section B4b; full text in the iteration log, section B9) — the earlier revision text stays retrievable so the revision that produced an approved take can be re-run. When a prompt has grown by accretion and contradicts itself, sanitize it from scratch (SKILL rule 14) — that rewrite is also a new P-revision.
3. **Approval is the user's:** statuses move forward (draft → approved → locked) only on explicit user approval; "locked" additionally requires the ten-of-ten stress test of production-pipeline ch. 3 (W2 step 6) to have passed — approval alone yields "approved". The agent never self-approves; a regenerated asset resets to draft. Every generated result — including an edit or extension of an approved take — is a NEW Take ID (TK02 from TK01, the slate's Handoff row names the source) and starts in draft; the source take keeps its status.
4. **The bible mirrors platforms, it does not replace them.** Binary assets live in the platform (Higgsfield Elements/Soul ID, OpenArt characters, Runway tagged References, local files for fal pipelines); the bible holds names, IDs, statuses, and pointers. On conflict, the approved image/element is the visual truth, the bible is the record of WHICH one is approved.
5. **Compact by force:** the whole bible stays pasteable into a fresh chat (target: 2–4 pages). Superseded decisions and finished shots move to an ARCHIVE section at the bottom or a second file; the active surface stays small; the full iteration log lives outside the active surface (section B9).
6. **One bible per project.** Series/episodic work: one project bible (world, cast, style contract) + one slim episode sheet per episode (shot board, episode decisions). The pole decides the split (story-structures ch. 23d): **episodic** — universe facts live ONLY in the project bible and change only at season boundaries, episode sheets stay throwaway-slim; **serialized** ("the overlong film") — shot board and continuity ledger span the season in the project bible, episode sheets carry only the episode's micro-shape and status.
7. **Platform receipt is mandatory.** Before a generation, edit, or model-choice decision becomes canon, record the RECEIPT line as defined in SKILL.md Scope & version (KEY grammar there; receipt states `live-checked <date>` / `from reference <KEY>`, SKILL rule 16) in section B1b. Never transfer a setting merely because two surfaces share a provider or model name.

## 22b. Template (copy, fill, keep)

```markdown
# <PROJECT> — Production Bible          last update: <date> · by <session/user>

## B1 · Frame
Format/length: … · Platform target(s) + aspect ratio(s): …
Model stack: stills … [token] · motion … [token] · edit/post … [token] — Render-ID tokens in brackets, fixed once here (SKILL.md ID discipline; e.g. `motion Seedance 2.5 on Higgsfield [HF-SD25]`)
Dialogue language: … · Route: native in-model / audio dub / video dub (test-take result + date) · AI-disclosure duty: … (post-audio-legal ch. 20)

## B1b · Platform / UI / MCP receipts (one RECEIPT line per row, SKILL.md Scope & version order)
| KEY | Platform → access route | Account / workspace / project | Surface / tool | Model + mode id ("UI label") | Vendor version or UI snapshot | Source URL · state (live-checked <date> / from reference <KEY>) | Result / asset IDs |
|---|---|---|---|---|---|---|---|
| HF-CS4@<check date> | Higgsfield → web UI | … | Cinema Studio | Seedance 2.5 · t2v ("…") | Cinema Studio 4.0 | … · live-checked <date> | … |

For an unversioned web form write `unversioned UI @ YYYY-MM-DD`; for MCP also retain its server URL and the exposed tool/schema. Every actual generation/edit cites its KEY in the shot board and in the delivery's Render Slates. The live selected form and connected workspace always outrank an old receipt.

## B2 · Style contract (decided — quote, don't re-litigate)
Premise (one sentence the ending proves): …
Container: <structure from ch. 23, one line> · Series pole (if series): episodic / serialized / anthology
Recipe: <name or synthesis, one line why>
Style anchor (project style contract — distributed per SKILL.md Workflow step 4, never pasted as a prefix):
> …
Look tokens (4–8, verbatim in every prompt's STYLE / image style section): …
Verify line (QA gate for every still/take; recipe's line, or DEFAULT line derived from style anchor + genre baseline — never empty; W1 step 5): …
Genre baseline: <genre> — deviations: …

## B3 · Asset registry (= the reference pool)
| @name | Type (reference class) | Status | Source of truth | Platform IDs / path | Job line + exclusions |
|---|---|---|---|---|---|
| @hero | character (@Image) | locked | sheet v3 (link/element) | HF element …, Soul ID … / file … | face+outfit lock; never: … |
| @loc_bar | location (@Image) | approved | master plate v2 | … | light side left; reverse: @loc_bar_rev |
| @anchor_1A | anchor (@Image) | approved | still 1A final | HF element … / file … | reference anchor shot 1A |
| @clay_sc3 | clay-render (@Clay Render) | approved | blockout v2 | HF element … / file assets/clay/clay_sc3_v2.mp4 | camera move + staging + subject trajectory only; never: lighting, texture |
| @voice_hero | voice/audio (@Audio) | approved | voice ref v1 (<30 s) | HF element … / file assets/audio/voice_hero_v1.mp4 | "@Audio 1 defines @hero's voice"; never: motion, identity |
Types (column 2 = asset type + the ch. 14b reference class it is attached as): character (@Image) · location (@Image) · prop (@Image) · wardrobe (@Image) · style-ref (@Image) · anchor (@Image) · layout-schematic (@Image, production-pipeline ch. 8) · motion-clip (@Video — motion/pacing only unless the job line says otherwise) · voice/audio (@Audio; on surfaces without an audio slot attached as @Video black-screen MP4, post-audio-legal ch. 18) · clay-render (@Clay Render — staging/camera only, never lighting). Every approved shot still becomes an @anchor_* entry (production-pipeline ch. 1). Every element of the W2 reference pool gets a row — a reference without a row is not canon.

## B4 · Shot board
| Shot | Seq. take | Len | Status | Anchor | Current Render ID | Approved-take Render ID | Platform receipt (KEY) | Risk → rescue (from the delivery risk registers) | Takes used (= Take IDs in B4b) |
|---|---|---|---|---|---|---|---|---|---|
| 1A | S1 (1A+1B) | 8s | final | @anchor_1A | LIGHTHOUSE_1A__HF-SD25__T2V__P02 | …__T2V__P02 (TK03) | HF-CS4@2026-08-31 | — | 3 |
| 1B | S1 (1A+1B) | 6s | stills | @anchor_1B | LIGHTHOUSE_1B__HF-SD25__T2V__P01 | — | … | hands close-up → cut to reaction · ACCEPTED by user <date> | 0 |
Status ladder: planned → stills (approved still exists) → take (approved take) → final (in edit).
ID discipline (SKILL.md Render Slate): Shot ID = canon here; Shot IDs enter this board verbatim from the delivered shot table (SKILL.md ID discipline, Bootstrap) — Shot/Len/Risk → rescue mirror the treatment shot table (SKILL.md Workflow 5). Seq. take = the generation unit (SKILL rule 2: 1–3 internal shots per take); label `S<n>` = sequence take, never `TK` (that is a Take ID of a generated result). Render IDs (`…__P01`) identify prompt-package revisions; Take IDs (`TK01`…) exist only for generated results — "Takes used" counts Take IDs, never prompt revisions. `Current Render ID` = the latest prompt package; `Approved-take Render ID` = the revision that produced the approved take (with its TK) — never overwrite this once status ≥ take. Risk → rescue holds one entry per kept red/yellow element of the shot, copied from the delivery risk register at session close (`<risk> → <rescue>`), plus heard warnings as `ACCEPTED by user <date>`; there is no separate register section in the bible.

## B4b · Render / take log (one row per prompt package; move a shot's rows to ARCHIVE when it is final)
| Render ID | KEY | Changed vs previous | Take IDs | Verdict / approved take |
|---|---|---|---|---|
| LIGHTHOUSE_1A__HF-SD25__T2V__P01 | HF-CS4@2026-08-31 | first package | TK01–TK02 | TK02 lever pre-lit; TK01 face drift |
| LIGHTHOUSE_1A__HF-SD25__T2V__P02 | HF-CS4@2026-08-31 | rewrite: lever lock moved next to the action line | TK03 | TK03 approved |
| LIGHTHOUSE_1A__HF-SD25__EDIT__P01 | HF-CS4@2026-08-31 | region edit 5–7 s, lever only (source TK03) | TK01 | final |
Counting rule (SKILL rule 14): 3 failed iterations with the same operation on one shot = clean rewrite + channel change; 10–15 Take IDs on one shot = simplify the shot (production-pipeline ch. 10).

## B5 · Reroll budget & spend priorities
Planned takes per shot class: standard … · face/emotion peaks … · long takes/oners …
Spend the budget where the recipe says (its AI note); stop rule = the SKILL rule-14 ladder: 3 failed iterations → clean rewrite + channel change; 2 clean failures → model limit; 10–15 iterations per shot → simplify the shot.
Spent so far: … (update per block)

## B6 · Decision log (append-only, one line each)
<date> — <decision> — <why / alternative rejected>
<date> — ASSUMED: <item> = <value> — confirm
<date> — feedback-to-skill offer: made / declined

## B7 · Continuity ledger (never closes — post-audio-legal ch. 19)
| Shot | Character state (sheet) | Key props (whose hand, state) | Time of day / weather | Light direction | Screen direction per character | Emotional state |
|---|---|---|---|---|---|---|
| 1A | @hero sheet v3 | lantern in @hero's left hand, unlit | night, clear | key from left, moon | @hero faces right | resolved, tired |
One row per shot; check the new row against the previous one before every generation; a state change spawns a sheet order, never a prompt adjective (post-audio-legal ch. 19); changes only via decision log entry.

## B8 · Handoff
Last state: … · Next: 1) … 2) … · Open questions for the user: … · Reviews pending: `TKnn — review pending (director)`

## B9 · Iteration log (pointer)
Lives OUTSIDE the active bible surface (rule 5): file `<PROJECT>-iteration-log.md` next to the bible, or the ARCHIVE section if the project is small. One line per run, append-only:
`<Render ID> · <TK or 'no result'> · what changed (one line) · verdict (reject/tell/coverage/approved)`
The full prompt text of every P-revision that produced an approved take or coverage is kept verbatim in that file (production-pipeline ch. 10); B4b is its per-shot summary.

## ARCHIVE
<superseded decisions, finished-and-delivered shots>
```

## 22c. Platform mapping (what the registry means per platform)

**Version boundary:** these are storage/continuity patterns, not promises about the current selector set of a platform. For live UI or MCP choices, first record a RECEIPT line in section B1b and consult `platform-ui-workflows.md` for the matching dated reference key.

- 🟢 **Higgsfield / Cinema Studio:** Elements (characters, locations, props — and registered anchors, platforms-models ch. 13b) and Soul ID persist platform-side; the registry's "Platform IDs" column records the element names verbatim so prompts and bible use identical tags (tag token rule: video-prompting ch. 12b). The platform's own shared Project Brief may exist for teams — the bible remains the agent-facing source of truth and must not contradict it.
- 🟢 **Runway (RW-WEB@2026-08-31, platform-ui-workflows §3):** tagged Gen-4 Image References persist in the Runway Assets library (max three per generation); Gen-4.5 video takes text or text + one image only, no References. The registry's "Platform IDs" column records the Reference tag name verbatim; "Source of truth" still points to the local file so the asset survives a plan/library change. Session boot: confirm the tagged References still appear in Assets — if not, re-upload from the local file and record a new receipt. The live UI outranks this line; do not ask the user to verify beyond what the panel shows.
- 🟡 **OpenArt:** character objects persist but community reports drift; keep the sheet-based anchor discipline (production-pipeline ch. 3) as the real lock, the platform character as convenience.
- 🟢 **fal via MCP/API, local pipelines:** treat the local file tree as the durable asset store unless the selected, version-recorded fal endpoint/workspace says otherwise. The registry's path column is canonical; keep one folder per asset type (`assets/characters/`, `assets/locations/`, `assets/props/`, `assets/wardrobe/`, `assets/style/`, `assets/anchors/`, `assets/layouts/`, `assets/motion/`, `assets/audio/`, `assets/clay/`, `takes/`), filenames = @names + version (`anchor_1A_v2.png`). The bible lives at the project root next to them. Every reference is re-attached per run and addressed by the upload-order form the surface shows (video-prompting ch. 12b tag token rule).
- **Mixed stacks** (e.g. stills local via fal, motion on Higgsfield): one registry row can carry both a path and an element ID; the status column is shared — an asset is approved once, everywhere.

## 22d. Why this exists

Working studio pipelines converge on the same shape: script → shot breakdown → references → generation with planned retakes → review → post, with a shared brief and a reusable asset store carrying consistency. The failure mode this file prevents: project knowledge scattered across chat histories, loose anchor images, and platform sessions — each resumed session rebuilding context from memory, drifting a little each time. The bible is the fixed point; sessions come and go.

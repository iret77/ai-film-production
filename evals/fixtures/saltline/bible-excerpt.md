# SALTLINE — production bible (cold-test fixture; fictional project, technique A)

Excerpt of a running project's bible for the prompt test of `references/agent-models.md`. Every row below is canon for the test; nothing outside this file is.

## B1 · Frame
Format/length: photoreal live-action-look short, 60 s · Platform target: YouTube, 16:9
Model stack: stills Nano Banana Pro on Higgsfield [HF-NBP] · motion Seedance 2.5 on Higgsfield [HF-SD25] · edit/post Seedance 2.5 Edit on Higgsfield [HF-SD25E]
Dialogue language: English · Route: native in-model (draft-resolution test take approved 2026-09-20) · AI-disclosure duty: platform label (post-audio-legal ch. 20)
Prompting technique (SKILL rule 4): A Caption Spine · decided with the director on 2026-09-20 (draft batch on shot 1A reproduced the beat structure 4 of 4) — every video prompt of this project uses it

## B1b · Platform / UI / MCP receipts
| KEY | Platform → access route | Account / workspace / project | Surface / tool | Model + mode id ("UI label") | Vendor version or UI snapshot | Source URL · state | Result / asset IDs |
|---|---|---|---|---|---|---|---|
| HF-WEB@2026-09-04 | Higgsfield → web UI | project SALTLINE | Video | Seedance 2.5 · t2v (UI label unverified — read the live task dropdown) | unversioned UI @ 2026-08-31 | https://higgsfield.ai/generate/video · from reference HF-WEB@2026-09-04 | — |

## B2 · Style contract (decided — quote, don't re-litigate)
Coastal noir, photoreal. Night exteriors under sodium-vapour dock lamps, rain visible only inside the lamp cones, wet steel deck, faces lit from one side, muted palette, fine grain. No teal-and-orange grade. Camera handheld only where the treatment says so.
STYLE tokens (ch. 12h): photoreal · night · sodium-vapour practicals · rain in the lamp cones · wet steel deck · single-side faces · muted palette · fine grain.

## B3 · Asset registry (= the reference pool)
| @name | Type (reference class) | Status | Source of truth | Platform IDs / path | Job line |
|---|---|---|---|---|---|
| @mara | character (@Image) | locked | sheet v2 | HF element mara_v2 | face + yellow oilskin jacket — identity only |
| @tomas | character (@Image) | locked | sheet v1 | HF element tomas_v1 | face + grey wool cap — identity only |
| @loc_ferrydeck | location (@Image) | approved | master plate v3 (night, rain, lamp on) | HF element ferrydeck_v3 | deck geometry, cleat and lamp positions; light side left; wheelhouse window aft |
| @anchor_2B | anchor (@Image) | approved | still 2B final | HF element anchor_2B | reference anchor shot 2B |

## B4 · Shot board (scene 2 rows)
| Shot | Seq. take | Internal TC | Cut type | Continuity lock | State | Len | Status | Anchor | Current Render ID | Approved-take Render ID | Platform receipt (KEY) | Risk → rescue | Takes used |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2A | S2 (2A) | 0:00–0:06 | manual (cut to 2B) | @mara at the foot of the ladder, facing the bow | — | 6 s | final | @anchor_2A | SALTLINE_2A__HF-SD25__T2V__P02 | …__T2V__P02 (TK02) | HF-WEB@2026-09-04 | — | 3 |
| 2B | S3 (2B) | 0:00–0:08 | manual (ellipsis to 3A) | @mara at the bow cleat, facing aft; @tomas behind the wheelhouse glass | mooring line: slack → tied off | 8 s | stills | @anchor_2B | — | — | HF-WEB@2026-09-04 | 🟡 hands on the cleat → tie-off as one short beat, cut to her face before the knot | 0 |

## Approved treatment, scene 2 (canon for shots 2A–2B; approved by the director 2026-09-21)
Night, rain. The ferry lies tied up at the island pier, bow lamp on. 2A: Mara comes down the wheelhouse ladder onto the deck. 2B: Mara hauls the slack mooring line taut with both hands and ties it off on the bow cleat; a swell lifts the hull and the line jerks once before it holds. She looks up at the lit wheelhouse window. Tomas stands behind the glass and has not moved. End on Mara's upturned face in the lamp light, the line still in her hand.

Shot table row 2B: `| 2B | 8 s | medium, low at deck level, from the bow looking aft toward the wheelhouse | Mara hauls the line taut, ties it off, the hull lifts, she looks up at Tomas in the window | @mara @tomas @loc_ferrydeck @anchor_2B | 🟡 hands on the cleat | tie-off as one short beat, cut to her face before the knot |`

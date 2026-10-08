# WHEELHOUSE — production bible (cold-test fixture; fictional project, technique B)

Excerpt of a running project's bible for the dialogue test of `references/agent-models.md`. Every row below is canon for the test; nothing outside this file is.

## B1 · Frame
Format/length: photoreal live-action-look short, 90 s · Platform target: festival screener, 2.39:1
Model stack: stills Nano Banana Pro on Higgsfield [HF-NBP] · motion Seedance 2.5 on Higgsfield [HF-SD25] · edit/post Seedance 2.5 Edit on Higgsfield [HF-SD25E]
Dialogue language: English · Route: native in-model (draft-resolution test take approved 2026-09-22) · AI-disclosure duty: festival form (post-audio-legal ch. 20)
Prompting technique (SKILL rule 4): B block structure · decided with the director on 2026-09-22 (the director wants explicit per-axis control for the dialogue scenes) — every video prompt of this project uses it

## B1b · Platform / UI / MCP receipts
| KEY | Platform → access route | Account / workspace / project | Surface / tool | Model + mode id ("UI label") | Vendor version or UI snapshot | Source URL · state | Result / asset IDs |
|---|---|---|---|---|---|---|---|
| HF-WEB@2026-09-04 | Higgsfield → web UI | project WHEELHOUSE | Video | Seedance 2.5 · t2v (UI label unverified — read the live task dropdown) | unversioned UI @ 2026-08-31 | https://higgsfield.ai/generate/video · from reference HF-WEB@2026-09-04 | — |

## B2 · Style contract (decided — quote, don't re-litigate)
Photoreal chamber drama. One practical: the chart-table lamp, warm tungsten, everything else falls off into the dark; faces lit from the table side; rain on the wheelhouse glass; muted palette. No handheld; the camera sits on the chart table.

## B3 · Asset registry (= the reference pool)
| @name | Type (reference class) | Status | Source of truth | Platform IDs / path | Job line |
|---|---|---|---|---|---|
| @ida | character (@Image) | locked | sheet v3 | HF element ida_v3 | face + dark oilskin — identity only |
| @bram | character (@Image) | locked | sheet v2 | HF element bram_v2 | face + white beard + wool cap — identity only |
| @loc_wheelhouse | location (@Image) | approved | master plate v2 (night, lamp on) | HF element wheelhouse_v2 | wheelhouse geometry, chart table and lamp position; light side right |
| @anchor_3A | anchor (@Image) | approved | still 3A final | HF element anchor_3A | reference anchor shot 3A |
| @voice_bram | voice/audio (@Audio) | approved | voice ref v1 (<30 s) | HF element voice_bram_v1 | "@Audio 1 defines @bram's voice — timbre and manner only" |

## B4 · Shot board (scene 3 rows)
| Shot | Seq. take | Internal TC | Cut type | Continuity lock | State | Len | Status | Anchor | Current Render ID | Approved-take Render ID | Platform receipt (KEY) | Risk → rescue | Takes used |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3A | S4 (3A) | 0:00–0:08 | manual (cut to 3B) | @bram at the wheel, facing forward; @ida at the chart table, facing him | — | 8 s | stills | @anchor_3A | — | — | HF-WEB@2026-09-04 | — | 0 |

## Approved treatment, scene 3 (canon for shots 3A–3C; approved by the director 2026-09-23)
Night. Wheelhouse, rain on the glass, the chart-table lamp the only light. 3A: Ida stands at the chart table, her wet hands flat on the chart. Bram, at the wheel, does not turn around. Bram says: "You tied it wrong." Ida looks down at her hands and says nothing. End on Ida turning toward the door, Bram still facing forward.

Shot table row 3A: `| 3A | 8 s | medium two-shot, static, from the chart table looking forward past Ida to Bram at the wheel | Ida at the chart, Bram speaks without turning, Ida looks at her hands, turns to the door | @ida @bram @loc_wheelhouse @anchor_3A @voice_bram | — | — |`

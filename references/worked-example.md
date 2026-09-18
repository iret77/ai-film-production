# Worked Example: 20-Second Spot, End to End

**Contents — read once end to end on first use; afterwards only the part a pointer names:** §1 canon → shot plan · §1b route receipt · §2 assets · §3 sequence take S1 in technique B (block structure, for comparison) · §3b the same take in technique A (Caption Spine — the technique this project chose) · §3c production take of S1 · §4 sequence take S2, extension round · §5 QA and log.

A compact walkthrough applying the pipeline to a fictional brief — read once to see how the chapters connect; every deliverable below is in the form the rules require (per-prompt checklist steps 1–7, Render Slate, risk register, bible rows). Style: Pixar-adjacent stylized 3D (in a real project the style is picked via the director-recipes selection index — here fixed for brevity). Model path: Nano Banana Pro (figure-anchored anchor plate, sheets) → GPT Image 2.5 (derived empty plate, reverse plate) → Seedance 2.5 on Higgsfield (motion). Project slug: `LIGHTCAT`. Element tags (Higgsfield Elements, verbatim everywhere — tag token rule, video-prompting ch. 12b): `@cat`, `@loc_lamproom`, `@loc_lamproom_rev`, `@prop_lever`, `@anchor_1A`, `@anchor_1B`. On a Dreamina/ModelArk surface the same prompts would carry `@Image 1…n` by upload order. Sequence take S1 is shown in BOTH prompt shapes on the same canon: §3b is the Caption Spine — the technique this example project chose at intake (SKILL rule 4; read this one first) — and §3 is the same take in the block structure, for comparison; the extension round (§4) is in the Caption Spine. Both carry the same Render ID: the technique is a project constant, not a prompt variant.

## 1. Canon → shot plan (SKILL rule 14, production-pipeline ch. 2)
Canon comes from the director's treatment — never from the agent. Treatment excerpt (the passage every canon-bound claim below is read from): "Sc. 1, night, rain. The keeper's cat slips through the hatch into the dark lamp room, shakes off, rears up and pushes the brass lever with its whole body. The lamp ignites; the cat sits and watches the beam." Canon is silent on where the cat enters from → delivered as `PROPOSAL — not canon` ("hatch at the left wall"), approved by the director before it entered any prompt. Camera height and light direction are craft-fillable (rule 14) — decided by the crew and listed in each slate's `Crew choices` row; the lens, the composition inside the named shot size and the cut timing are left to the model by default (SKILL.md Economy and division of labour), and the `Crew choices` row says so. Intake decision (SKILL rule 4): technique A, Caption Spine — a calm single-event beat with clear canon and a look the anchors carry; no draft takes were needed. Recorded in the bible frame (section B1).
Renderability pass: paw-level object manipulation 🟡 (renderability §2 hands row) → rescue: whole-body push (big motion, no finger-class precision); rescue cut if it fails: lever-only insert + reaction MCU. Both takes contain a cut for coverage; a calm single-event beat would be ONE shot in one take (production-pipeline ch. 2).

Shot table (SKILL.md Workflow step 5 schema; these Shot IDs ARE the bible shot board's IDs):
| Shot ID | Len | Framing | Action | Assets | Risk | Rescue |
|---|---|---|---|---|---|---|
| 1A | 4 s | medium-wide, static, low, from the rear-left corner | wet cat squeezes through the hatch, shakes, looks up at the dark lamp | @cat @loc_lamproom @anchor_1A | 🟡 wide opening (stylized 3D) | open on the medium, arrive at the wide by transition |
| 1B | 6 s | close-up insert on the lever, then back to 1A's setup | cat rears up, pushes the lever with its whole body; lamp ignites; cat settles | @cat @prop_lever @anchor_1B | 🟡 paw manipulation | whole-body push; cut to lever insert + reaction MCU |
| 1C | 4 s | medium, static, same position | cat blinks in the warm light, breathes out | @cat | — | — |
| 1D | 6 s | wide, low, counter-angle | the beam starts to rotate; the sweep crosses the cat's face | @cat @loc_lamproom_rev | — | — |
Sequence takes (SKILL rule 2): S1 = 1A + 1B (10-s `t2v` take, three internal shots: 1A → 1B insert → return to 1A's setup) · S2 = 1C + 1D (10-s `video_extension` of S1's production take, counter-angle as internal shot 2 after the HARD CUT). A multi-shot take carries the Render ID of its FIRST internal shot; every internal shot's board row points to it.

## 1b. Route receipt (SKILL rule 17, checklist step 2)
`HF-WEB@2026-09-04 · Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 · t2v (UI label unverified — read the live task dropdown) / video_extension ("Extend") → unversioned UI @ 2026-08-31 → https://higgsfield.ai/generate/video · from reference HF-WEB@2026-09-04` — no live read this session, so the state is `from reference`; whoever has the form open confirms model/mode/workspace before Generate (the Generate-time gate). Stills: `HF-WEB@2026-09-04 · Higgsfield → web UI → project LIGHTCAT → Image → Nano Banana Pro (live label to confirm) → unversioned UI @ 2026-08-31 → <source URL from the HF-WEB ledger row> · from reference HF-WEB@2026-09-04` (surface label to be written exactly as shown on the live form, production-pipeline ch. 5 label-mismatch note). Both rows go into bible section B1b.

## 2. Assets (production-pipeline ch. 1, 3–5; pixar-look §8; style-control §2–3)
Every order ships as a Render Slate + still prompt (asset order shape, production-pipeline ch. 3). One shown in full, the rest as one-line orders:
| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_cat__HF-NBP__SHEET__P01` |
| Intent | Cat character sheet, stylized 3D, one canonical face — CG turnaround (production-pipeline ch. 3 selector: stylized 3D) |
| Crew choices | neutral grey background, even studio light, 3/4 face close-up as the identity carrier |
| Run in | Higgsfield → web UI → project LIGHTCAT → Image → Nano Banana Pro (live label to confirm) — from reference HF-WEB@2026-09-04, not live-checked this session |
| Settings | 16:9 · 2K · 1 image |
| Inputs | none (from scratch) |
| Format | CG turnaround: A-pose front + back full body + large 3/4 face close-up · state: dry (state sheet #2 "wet fur" is a separate order) |
| Locks | one canonical face · both arms whole, both hands intact · skin/fur matte, low-sheen · identity props: none · clutter stripped |
| Register as | `@cat · character (@Image) · status draft` → bible section B3 |
```
Character reference sheet on a plain neutral grey background, landscape 16:9, three panels separated by white gutters. Panel 1 (left): full-body front view, A-pose — a small grey tabby cat with a white chest patch and green eyes, rounded simplified forms, matte fur with soft subsurface scattering. Panel 2 (centre): full-body back view, same pose. Panel 3 (right, largest): close portrait in 3/4 view, neutral expression, mouth closed, slightly oversized expressive eyes, one small notch in the left ear. Even, shadowless neutral studio light; fur matte and low-sheen. All four paws complete and intact. Stylized animated-feature design, NOT photorealistic. Avoid: text, labels, oily highlights, photographic rendering, any recognisable studio or franchise design.
```
- `@cat` state sheet #2 "wet fur" — a sheet order, not an adjective (`LIGHTCAT_cat_wet__HF-NBP__SHEET__P01`).
- `@loc_lamproom` anchor plate (Nano Banana Pro — the anchor-render model, pixar-look §8): generated WITH the cat in frame (figure-anchor hard rule); lamp room, brass lever on the right wall, rain-streaked glass, dark lamp above; 24mm wide-angle, camera in the rear-left corner (`…__PLATE__P01`). Empty plate derived from it via edit (GPT Image 2.5 — `gpt-image-2.5-sunburst`, the edit-precision route: remove the figure + preserve list, style-control §2 selector, third bullet).
- `@loc_lamproom_rev` reverse plate: decided NOW because 1D is a counter-angle (production-pipeline ch. 16 rung 3 — GPT Image 2.5 with the master plate + a layout map attached, never free-text "same room from behind"); reverse-tested against the master (anchors, openings, light side, palette) (`…__ANGLE__P01`).
- `@prop_lever`: brass lever, state pair down/up as two separate stills (`…__PLATE__P01`, edit for the "up" state).
- Anchor stills 1A and 1B (`LIGHTCAT_1A__HF-NBP__STILL__P01`, `LIGHTCAT_1B__HF-NBP__STILL__P01`) → after approval registered as Elements `@anchor_1A`, `@anchor_1B` (rule 5).

## 3. Sequence take S1 (shots 1A+1B) — technique B, block structure (video-prompting ch. 12/12b/14; style-control §5/§7) — shown for comparison
This example project chose technique A (§1); the same take in the block structure shows what B costs and buys: every axis is steered explicitly — camera, optics, light, continuity — which a project picks when it deliberately wants that control (SKILL rule 4). Canon, route and Render ID are identical to §3b.
| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_1A__HF-SD25__T2V__P01` (multi-shot take S1 = 1A+1B) |
| Intent | The wet cat enters the dark lamp room and pushes the lever with its whole body; the lamp ignites — three internal shots, medium-wide → lever insert → medium-wide |
| Crew choices | Left to the model: the cat's body mechanics, wet-fur and brass rendering, the light bloom, the cut timing inside the declared ranges. Decided by the crew — the look controls technique B steers deliberately, each a paid line: medium-wide 63° / close-up 47°, window key 8500K, lamp key 3200K, camera height and distance as relations, the two-shake rain shed as the reaction cue |
| Run in | Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 → t2v (UI label unverified — read the live task dropdown) — from reference HF-WEB@2026-09-04 (checked 2026-09-04), not live-checked this session; confirm model/mode/workspace on the live form before Generate |
| Settings | 16:9 · 720p (draft tier) · 10 s · audio on · no Cinema Studio controls (Video page) |
| Lint | words 467 · chars 2,645/5,000 · negations 1/1 (the AUDIO music exclusion — once per governing block) · numerals outside TC: 63°, 47°, 8500K, 3200K — deliberate look controls listed in Crew choices · absolute measures 0/0 · double mentions none (ENDING STATE restates the last frame by contract, ch. 14) |
| Inputs | 1. `@anchor_1A` = approved still 1A — opening composition of SHOT 1 and SHOT 3 (reference, not start frame) · 2. `@anchor_1B` = approved still 1B — opening composition of SHOT 2 from the HARD CUT (reference, not start frame) · 3. `@loc_lamproom` = lamp-room master plate — set only · 4. `@cat` = cat sheet, wet state — identity only · 5. `@prop_lever` = lever detail, state down — prop only (all five are Higgsfield Elements addressed by name; no upload) |
| Store in | Higgsfield project LIGHTCAT / SC01 |

```
SCENE CONTEXT: Night, rain, lamp room of a lighthouse. @cat has just slipped in through the hatch and will push the brass lever to relight the dark lamp above.
ACTIVE REFERENCES: @anchor_1A is the opening composition of SHOT 1 (0.0–4.0 s) and of SHOT 3 (7.0–10.0 s); the take opens already in motion. @anchor_1B is the opening composition of SHOT 2, from the HARD CUT at 4.0 s onward. @cat controls only the cat — small grey tabby, wet clumped fur, white chest patch, green eyes, one notch in the left ear. 100% matches the reference. @loc_lamproom controls only the set. 100% matches the reference. @prop_lever controls only the lever — shape, state: down. 100% matches the reference.
LOCATION MAP: foreground wet floorboards; midground the brass lever on the right wall, the hatch on the left wall; background rain-streaked windows, the dark lamp above centre. Camera in the rear-left corner of the room.
FIRST FRAME/BLOCKING: the cat mid-squeeze through the half-open hatch, body toward frame centre, gaze up at the lamp.
FORMAT MODE: sequential cuts, three shots, 10 s total — Shot 1 0.0–4.0 s, Shot 2 4.0–7.0 s, Shot 3 7.0–10.0 s.
OPTICS: Shots 1 and 3 medium-wide at 63°; Shot 2 close-up at 47°; soft rounded rendering.
CAMERA: Shots 1 and 3 static, lens at the height of the cat's shoulders; Shot 2 static, lens level with the lever and close enough that the lever fills the frame's height.
ACTION: SHOT 1 (0.0–4.0 s): the cat lands on the floorboards, shakes rain off in two shakes — droplets catch the window light — then looks up at the lamp. HARD CUT; the cat's pose at the end of Shot 1 exactly matches its start in Shot 2. SHOT 2 (4.0–7.0 s): the cat rears up and pushes the brass lever with both forepaws and its whole body weight; the lever tips up with one heavy clunk; only then a warm glow blooms from above. HARD CUT. SHOT 3 (7.0–10.0 s): the cat settles onto its haunches in the amber light, eyes widening, ears rising, and goes still.
LIGHTING: Shot 1 one cold key from the windows screen-right, 8500K, low exposure, the cat's far side in shadow; from the ignition in Shot 2 a warm 3200K top light, brighter than the window key, contact shadows under the cat.
AUDIO: {rain on glass, continuous} {two wet shakes} {one heavy metallic clunk at 6.0 s} {low warm hum from the lamp from 6.0 s} 【no music, no BGM — room tone and effects only】
ENDING STATE: cat seated on its haunches facing the lit lamp, lever up, room in warm amber, rain continuing on the glass.
STYLE: stylized 3D animated-feature look, matte rendered materials, soft global illumination; clean, grain-free image.
POSITIVE LOCKS: exactly one cat in every frame.
```
The attachment list lives in the slate's `Inputs` row, never inside the prompt (SKILL rule 11).

## 3b. Sequence take S1 (shots 1A+1B) — technique A, Caption Spine — the technique this project chose (checklist steps 3–6; video-prompting ch. 12h; SKILL.md Economy and division of labour)
The same canon as §3, written for a specialist model: the agent states what is in the scene, what happens in which order and where each beat rests, gives each reference one job and writes one camera line for the return cut; composition inside the shot sizes, cut timing, the cat's body mechanics, wet fur, brass and the light bloom are the model's. Three references (identity, opening composition, insert framing) — the anchor stills stay references, not start frames (rule 1).
| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_1A__HF-SD25__T2V__P01` (multi-shot take S1 = 1A+1B) |
| Intent | The wet cat enters the dark lamp room and pushes the lever with its whole body; the lamp ignites — medium-wide → insert on the lever → medium-wide |
| Crew choices | Left to the model: camera composition inside the named shot sizes, the cut timing around the insert, the cat's body mechanics, wet-fur and brass rendering, the light bloom. Decided by the crew: shot-size words per beat; one camera line (low, looking toward the lever, holding still — continuity of the return cut); the rain shake as the reaction cue; window light cold / lamp light warm, as words |
| Run in | Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 → t2v (UI label unverified — read the live task dropdown) — from reference HF-WEB@2026-09-04 (checked 2026-09-04), not live-checked this session; confirm model/mode/workspace on the live form before Generate |
| Settings | 16:9 · 720p (draft tier) · 10 s · audio on · no Cinema Studio controls (Video page) |
| Lint | words 256/300 · negations 1/1 · numerals outside TC 0/0 · absolute measures 0/0 · double mentions none |
| Inputs | 1. `@cat` = cat sheet, wet state — identity only · 2. `@anchor_1A` = approved still 1A — exact background and opening composition (reference, not start frame) · 3. `@anchor_1B` = approved still 1B — exact framing of the lever insert (reference, not start frame) (all three Higgsfield Elements addressed by name; no upload) |
| Store in | Higgsfield project LIGHTCAT / SC01 |

```
Create a 10-second stylized 3D animated short inside the dark lamp room of a lighthouse on a rainy night.
STYLE: matte rendered materials, soft global illumination, cold window light, wet reflective floorboards, shallow depth of field, hushed mood, slow deliberate motion, room-tone sound.
@cat is a small grey tabby cat with wet clumped fur, a white chest patch, green eyes and a notch in its left ear. Keep the cat visually consistent throughout.
@anchor_1A is the exact background and the opening composition: the brass lever on the right wall, the half-open hatch on the left wall, rain-streaked windows and the unlit lamp above. @anchor_1B is the exact framing of the lever insert.
Camera: low, at the height of the cat's shoulders, looking across the floorboards toward the lever; the camera holds still.
0–4 s, medium-wide: the cat drops from the hatch onto the floorboards, shakes the rain off and looks up at the lamp; the lever stays down; rain drums on the glass.
4–7 s, close-up on the lever: the cat rears into frame and pushes the lever with its forepaws and its whole body until the lever tips up with a heavy clunk, and a warm glow blooms from above.
7–10 s, medium-wide: the cat settles onto its haunches and looks up at the lamp; its ears rise and it goes still; a low hum joins the rain.
End with the cat seated and still beneath the lamp, the room warm amber.
No dialogue, no subtitles, no text, no music. Maintain the same look throughout.
```
What is deliberately NOT in this prompt, and why: no OPTICS/FOV, no camera distance, no Kelvin, no PHYSICS block, no POSITIVE LOCKS — those axes are the model's (Division of labour); the lever's start state and the return to the medium-wide are each said once, inside the beat they belong to; the anchors carry the geography, so the beats never re-describe the room; the only negation is the closing sentence. If a run pushes with the head instead of the flank, the first repair step is still REMOVE (is anything on the push stated twice, or on an axis the model owns?), the second changes the half-sentence in beat two ("pushes the lever with its flank"), only the third adds one (SKILL rule 15).

**Risk register** (SKILL rule 11 — one table after the last slate of the delivery; covers §3 and §3b):
| Shot | Kept risk | List (red/yellow, renderability §2) | Why kept | Rescue |
|---|---|---|---|---|
| 1B | object manipulation (lever push) | yellow | it is the story beat; whole-body push, no toes/fingers visible | paws morph → cut to lever-only insert (`@prop_lever` state pair) + reaction MCU |
| 1A | wide opening in stylized 3D | yellow | single-room interior at close range | positions locked by `@anchor_1A`; if scale breaks, open on the medium and arrive at the wide by transition (pixar-look §10) |

## 3c. Production take of S1 (W3 step 6) — same prompt, new settings row
The draft batch sits (§5: TK03 approved at 720p), so the production take is a NEW generation of the locked §3b prompt at target resolution and the planned duration — same Render ID, new settings row (SKILL rule 13; W3 step 6) — never a `video_extension` of the draft take. The prompt text is the §3b block verbatim; only the rows below differ from the §3b slate.
| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_1A__HF-SD25__T2V__P01` (unchanged: rerunning the same text yields new Take IDs, never a new P — production-bible 22e) |
| Intent | as §3b — production take of sequence take S1 at target resolution |
| Run in | Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 → t2v (UI label unverified — read the live task dropdown) — from reference HF-WEB@2026-09-04 (checked 2026-09-04), not live-checked this session; confirm model/mode/workspace on the live form before Generate |
| Settings | 16:9 · 1080p · 10 s · audio on (production take, W3 step 6 — a new generation of the locked prompt, not an extension of the draft) |
| Lint | as §3b (text unchanged) |
| Inputs | as §3b (the same three Elements; references, not start frames) |
| Store in | Higgsfield project LIGHTCAT / SC01 |
Result (§5): Take IDs TK05–TK08, TK07 approved → `Approved-take Render ID` = `LIGHTCAT_1A__HF-SD25__T2V__P01` (TK07); S2 (§4) extends TK07 at 1080p. W3 step 6's exception (draft → scoped `video_edit` / upscale when the 1080p generation loses scale or structure) was not needed here.

## 4. Sequence take S2 (shots 1C+1D) — extension round in the Caption Spine (video-prompting ch. 14b, 12h; mode routing first)
On Seedance 2.5 a continuation is `video_extension` of the approved production take (§3c, TK07), never a harvested start frame (ch. 14b, W4 step 2); the counter-angle is internal shot 2 after a HARD CUT (production-pipeline ch. 16 rung 1), NOT the opening frame — the first frame of an extension is the source's last clean frame. The reverse plate keeps its own tag; tags are never re-used for a different asset. The boundary state is WRITTEN from the harvested last clean frame of the raw S1 export (ch. 14b boundary-frame contract; boundary-frame source ch. 14) — in the Caption Spine it IS the title sentence of the extension prompt.

| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_1C__HF-SD25__EXT__P01` (multi-shot take S2 = 1C+1D) |
| Intent | Cat holds at the lit lamp, then a low counter-angle as the beam starts to turn — 2 internal shots |
| Crew choices | Left to the model: composition inside the two shot sizes, the cut into the counter-angle, the beam's rendering and the light sweep. Decided by the crew: shot 1 holds the S1 end position (medium); shot 2 a low wide from the lamp side; the beam rotation as the light event |
| Run in | Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 → video_extension ("Extend", forward) — from reference HF-WEB@2026-09-04, not live-checked this session; confirm the Extend control on the live form before Generate |
| Settings | inherits 16:9 · 1080p · +10 s · audio on |
| Lint | words 189/300 · negations 1/1 · numerals outside TC 0/0 · absolute measures 0/0 · double mentions none |
| Inputs | 1. `@Video 1` = approved production take of S1 `LIGHTCAT_1A__HF-SD25__T2V__P01__TK07` (source; 🟡 token form unverified — match the upload label before running) · 2. `@cat` = identity only · 3. `@loc_lamproom_rev` = exact background of shot 2 only |
| Handoff | Boundary = S1 ENDING STATE at the last clean frame (9.8 s of TK07's raw export): cat seated facing the lit lamp, lever up, room warm amber, rain on glass |

```
Extend @Video 1 forward for 10 seconds, directly continued from its last frame: the seated cat beneath the lit lamp, the lever up, the room warm amber, rain on the glass.
STYLE: matte rendered materials, soft global illumination, warm lamp light, wet reflective floorboards, shallow depth of field, hushed mood, slow deliberate motion, room-tone sound.
@cat is the same small grey tabby cat with wet clumped fur, a white chest patch and green eyes. Keep the cat visually consistent throughout.
@loc_lamproom_rev is the exact background of the second shot, the room seen from the lamp side.
0–4 s, medium: the cat blinks slowly in the warm light and breathes out; its tail settles; the low hum and the rain continue.
4–10 s, wide from the lamp side, low: the beam begins a slow rotation overhead and its sweep passes across the cat's face; the cat's ears lift and it follows the beam with its eyes; a slow mechanical turning joins the hum.
End with the cat watching the turning beam and a slow fade to black.
No dialogue, no subtitles, no text, no music. Maintain the same look throughout.
```
The lever is fixed once, in the boundary sentence; `@prop_lever` is not attached because nothing about the lever changes in this round (12b tag rule: no tag for an object with no job). The counter-angle is carried by `@loc_lamproom_rev` and the shot-size words — no second camera line.
On a model without an extension mode (Seedance 2.0 and others): harvest S1's last clean frame as the literal start frame (the chain case, SKILL rule 1), keep Shot 1 on that angle, place the counter-angle as internal Shot 2 after the HARD CUT — in the project's technique, unchanged.

## 5. QA and log (production-pipeline ch. 10 · post-audio-legal ch. 17–19 · SKILL rules 13, 15)
Draft batch of 4 (`…__T2V__P01__TK01–TK04`, 720p), watched fully — by the director when the agent cannot view the result — in six passes (identity → continuity → timing → camera → audio → style/Verify line), verdict order post-audio-legal ch. 19 (hard rejects → rank by emotion → repair local faults). Failure example: TK02 renders the lever already up at 4.0 s → a hard continuity fault in a rejected take; TK02 is one bad roll of four (rule 15) — the prompt is not touched; only if three or four of the four rolls failed on the lever state would `…__T2V__P02` follow, in the rule-15 order — first REMOVE (is the lever stated twice, or anything written on an axis the model owns?), then CHANGE the half-sentence 'the lever stays down' inside beat one, add only third; the word count does not rise. TK03 approved at draft tier → the draft batch sits; the production take follows (§3c: same prompt, 1080p, TK05–TK08), TK07 approved → its Render ID with its Take ID becomes the shot board's `Approved-take Render ID` (`…__T2V__P01` (TK07)); from now on every local fault on TK07 is a `video_edit` (new Take ID), never a reroll. Grading, trim (±0.5 s, assembled cut only), score and loudness (−14 LUFS) in post.

Bible rows written at close (section B4b render/take log):
| Render ID | KEY | Changed vs previous | Take IDs | Verdict / approved take |
|---|---|---|---|---|
| LIGHTCAT_1A__HF-SD25__T2V__P01 | HF-WEB@2026-09-04 | first package (draft batch, 720p) | TK01–TK04 | TK02 lever pre-lit (one bad roll, reject); TK03 approved — draft sits |
| LIGHTCAT_1A__HF-SD25__T2V__P01 | HF-WEB@2026-09-04 | same text, new settings row: production take at 1080p (W3 step 6) | TK05–TK08 | TK07 approved |
| LIGHTCAT_1C__HF-SD25__EXT__P01 | HF-WEB@2026-09-04 | extension of TK07, counter-angle as shot 2 | TK01–TK04 | TK01 approved |
Bible section B1 row: `Prompting technique (SKILL rule 4): A Caption Spine · decided with the director on <date>, no draft takes needed (calm single-event beat, clear canon)`

# Worked Example: 20-Second Spot, End to End

A compact walkthrough applying the pipeline to a fictional brief — read once to see how the chapters connect; every deliverable below is in the form the rules require (per-prompt checklist steps 1–7, Render Slate, risk register, bible rows). Style: Pixar-adjacent stylized 3D (in a real project the style is picked via the director-recipes selection index — here fixed for brevity). Model path: Nano Banana Pro (figure-anchored anchor plate, sheets) → GPT Image 2 (derived empty plate, reverse plate) → Seedance 2.5 on Higgsfield (motion). Project slug: `LIGHTCAT`. Element tags (Higgsfield Elements, verbatim everywhere — tag token rule, video-prompting ch. 12b): `@cat`, `@loc_lamproom`, `@loc_lamproom_rev`, `@prop_lever`, `@anchor_1A`, `@anchor_1B`. On a Dreamina/ModelArk surface the same prompts would carry `@Image 1…n` by upload order.

## 1. Canon → shot plan (SKILL rule 13, production-pipeline ch. 2)
Canon comes from the director's treatment — never from the agent. Treatment excerpt (the passage every canon-bound claim below is read from): "Sc. 1, night, rain. The keeper's cat slips through the hatch into the dark lamp room, shakes off, rears up and pushes the brass lever with its whole body. The lamp ignites; the cat sits and watches the beam." Canon is silent on where the cat enters from → delivered as `PROPOSAL — not canon` ("hatch at the left wall"), approved by the director before it entered any prompt. Camera height, FOV and light colour are craft-fillable (rule 13) — decided by the crew, listed in each slate's `Crew choices` row.
Renderability pass: paw-level object manipulation 🟡 (renderability §2 hands row) → rescue: whole-body push (big motion, no finger-class precision); rescue cut if it fails: lever-only insert + reaction MCU. Both takes contain a cut for coverage; a calm single-event beat would be ONE shot in one take (production-pipeline ch. 2).

Shot table (SKILL.md Workflow step 5 schema; these Shot IDs ARE the bible shot board's IDs):
| Shot ID | Len | Framing | Action | Assets | Risk | Rescue |
|---|---|---|---|---|---|---|
| 1A | 5 s | WS 63°, static, rear-left corner | wet cat squeezes through the hatch, shakes, looks up at the dark lamp | @cat @loc_lamproom @anchor_1A | — | — |
| 1B | 5 s | MS 47°, static, at the lever | cat rears up, pushes the lever with its whole body; lamp ignites; cat settles | @cat @prop_lever @anchor_1B | 🟡 paw manipulation | whole-body push; cut to lever insert + reaction MCU |
| 1C | 4 s | MS 47°, static, same position | cat blinks in the warm light, breathes out | @cat | — | — |
| 1D | 6 s | WS 63°, low, counter-angle | the beam starts to rotate; the sweep crosses the cat's face | @cat @loc_lamproom_rev | — | — |
Sequence takes (SKILL rule 2): **S1** = 1A+1B (10-s `t2v` take, 2 internal shots) · **S2** = 1C+1D (10-s `video_extension` of S1, counter-angle as internal shot 2 after the HARD CUT). A multi-shot take carries the Render ID of its FIRST internal shot; every internal shot's board row points to it.

## 1b. Route receipt (SKILL rule 16, checklist step 2)
`HF-WEB@2026-09-04 · Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 · t2v (UI label unverified — read the live task dropdown) / video_extension ("Extend") → unversioned UI @ 2026-08-31 → https://higgsfield.ai/generate/video · from reference HF-WEB@2026-09-04` — no live read this session, so the state is `from reference`; whoever has the form open confirms model/mode/workspace before Generate (the Generate-time gate). Stills: `HF-WEB@2026-09-04 · Higgsfield → web UI → Image → Nano Banana Pro` (surface label to be written exactly as shown on the live form, production-pipeline ch. 5 label-mismatch note). Both rows go into bible section B1b.

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
Character reference sheet on a plain neutral grey background, landscape 16:9, three panels separated by white gutters. Panel 1 (left): full-body front view, A-pose — a small grey tabby cat with a white chest patch and green eyes, stylized 3D animated-feature design, rounded simplified forms, matte fur with soft subsurface scattering. Panel 2 (centre): full-body back view, same pose. Panel 3 (right, largest): close portrait in 3/4 view, neutral expression, mouth closed, slightly oversized expressive eyes, one small notch in the left ear. Even neutral studio light, no shadows on the face; fur matte and low-sheen — no oily highlights. All four paws complete and intact. No text, no labels. Stylized animated-feature aesthetic, not a photograph, not a physically based render; do not imitate any particular studio, film, franchise, or character design.
```
- `@cat` state sheet #2 "wet fur" — a sheet order, not an adjective (`LIGHTCAT_cat_wet__HF-NBP__SHEET__P01`).
- `@loc_lamproom` anchor plate (Nano Banana Pro — the anchor-render model, pixar-look §8): generated WITH the cat in frame (figure-anchor hard rule); lamp room, brass lever on the right wall, rain-streaked glass, dark lamp above; 24mm wide-angle, camera in the rear-left corner (`…__PLATE__P01`). Empty plate derived from it via edit (GPT Image 2: remove the figure + preserve list, style-control §2 selector, third bullet).
- `@loc_lamproom_rev` reverse plate: decided NOW because 1D is a counter-angle (production-pipeline ch. 16 rung 3 — GPT Image 2 with the master plate + a layout map attached, never free-text "same room from behind"); reverse-tested against the master (anchors, openings, light side, palette) (`…__ANGLE__P01`).
- `@prop_lever`: brass lever, state pair down/up as two separate stills (`…__PLATE__P01`, edit for the "up" state).
- Anchor stills 1A and 1B (`LIGHTCAT_1A__HF-NBP__STILL__P01`, `LIGHTCAT_1B__HF-NBP__STILL__P01`) → after approval registered as Elements `@anchor_1A`, `@anchor_1B` (rule 5).

## 3. Take S1 (shots 1A+1B) — Render Slate + ch. 12 prompt (checklist steps 3–6; video-prompting ch. 12/12b/14; style-control §5/§7)
| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_1A__HF-SD25__T2V__P01` (multi-shot take S1 = 1A+1B) |
| Intent | The wet cat enters the dark lamp room and pushes the lever with its whole body; the lamp ignites — 2 internal shots, static wide → medium |
| Crew choices | camera rear-left corner 40 cm high (1A) and 60 cm high at the lever (1B); WS 63° / MS 47°; window key 8500K, lamp key 3200K at 7.0 s; two-shake rain shed as the reaction cue |
| Run in | Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 → t2v (UI label unverified — read the live task dropdown) — from reference HF-WEB@2026-09-04 (checked 2026-09-04), not live-checked this session; confirm model/mode/workspace on the live form before Generate |
| Settings | 16:9 · 720p (draft tier) · 10 s · audio on · no Cinema Studio controls (Video page) |
| Inputs | 1. `@anchor_1A` = approved still 1A — look, geometry, blocking of SHOT 1 (reference, not start frame) · 2. `@anchor_1B` = approved still 1B — framing and blocking of SHOT 2 from the HARD CUT (reference, not start frame) · 3. `@loc_lamproom` = lamp-room master plate — set only · 4. `@cat` = cat sheet, wet state — identity only · 5. `@prop_lever` = lever detail, state down — prop only (all five are Higgsfield Elements addressed by name; no upload) |
| Store in | Higgsfield project LIGHTCAT / SC01 |

```
SCENE CONTEXT: Night, rain, lamp room of a lighthouse. @cat has just slipped in through the hatch (screen-left) and will push the brass lever (screen-right) to relight the dark lamp above. Two internal shots, 10 s.
ACTIVE REFERENCES: @anchor_1A controls only look, geometry and blocking of SHOT 1 (0.0–5.0 s); the take opens already in motion, it is not frame 1. @anchor_1B controls only framing and blocking of SHOT 2, from the HARD CUT at 5.0 s — not before. @cat controls only the cat — small grey tabby, wet clumped fur, white chest patch, green eyes, one notch in the left ear. 100% matches the reference. Do not copy its neutral pose or grey background. @loc_lamproom controls only the set — brass lever on the right wall, rain-streaked glass, dark lamp above. 100% matches the reference. Do not copy its emptiness. @prop_lever controls only the lever — shape, wall position, state: down. 100% matches the reference. Do not copy its background.
LOCATION MAP: foreground wet floorboards; midground the brass lever on the right wall, the hatch on the left wall; background rain-streaked windows, the dark lamp above centre. Camera in the rear-left corner of the room. Light enters from the windows, screen-right.
FIRST FRAME/BLOCKING: the cat mid-squeeze through the half-open hatch, screen-left, body toward frame centre, gaze up at the lamp. Rule for this scene: hatch stays screen-left, lever screen-right.
FORMAT MODE: sequential cuts, two shots, 10 s total — Shot 1 0.0–5.0 s, Shot 2 5.0–10.0 s.
OPTICS: Shot 1 WS at 63°; Shot 2 MS at 47°; no drift mid-segment; soft rounded rendering, no lens flare.
CAMERA: Shot 1 static, lens 40 cm above the floor, 3 m from the cat. Shot 2 static, lens 60 cm high, 1.5 m from the lever; one slow focus pull from the cat to the lever over 1 s as the paws land.
ACTION: SHOT 1 (0.0–5.0 s): the cat lands on the floorboards, shakes rain off in two shakes — droplets catch the window light — then looks up at the dark lamp. HARD CUT; the cat's pose at the end of Shot 1 exactly matches its start in Shot 2. SHOT 2 (5.0–10.0 s): the cat rears up and pushes the brass lever with both forepaws and its whole body weight; the lever tips up with one heavy clunk; only then a warm glow blooms from above and washes the room amber; the cat's eyes widen, ears rise, it settles onto its haunches.
PHYSICS: the lever moves only under the cat's full weight; wet fur clumps and drips; droplets fall at natural speed.
LIGHTING: Shot 1 one cold key from the windows screen-right, 8500K, low exposure, the cat's far side in shadow. Shot 2 the lamp ignites at 7.0 s: warm 3200K top light, 60% brighter than the window key, contact shadows under the cat.
AUDIO: {rain on glass, continuous} {two wet shakes} {one heavy metallic clunk at 7.0 s} {low warm hum from the lamp from 7.0 s} 【no music, no BGM — room tone and effects only】
ENDING STATE: cat seated on its haunches facing the lit lamp, lever up, room in warm amber, rain continuing on the glass.
STYLE: stylized 3D animated-feature look, matte rendered materials, soft global illumination; 24 fps, no grain.
POSITIVE LOCKS: exactly one cat in every frame; the lever starts down and tips up only at the push; the poses at the end of Shot 1 match the start of Shot 2; the camera never crosses the hatch–lever axis; wet-fur state holds in every frame; every frame keeps the stylized 3D rendering.
```
The attachment list lives in the slate's `Inputs` row, never inside the prompt (SKILL rule 10).

**Risk register** (SKILL rule 10 — one table after the last slate of the delivery):
| Shot | Kept risk | List (red/yellow, renderability §2) | Why kept | Rescue |
|---|---|---|---|---|
| 1B | object manipulation (lever push) | yellow | it is the story beat; whole-body push, no toes/fingers visible | paws morph → cut to lever-only insert (`@prop_lever` state pair) + reaction MCU |
| 1A | wide opening in stylized 3D | yellow | single-room interior at close range | positions locked by `@anchor_1A`; if scale breaks, open on the MS and arrive at the wide by transition (pixar-look §10) |

## 4. Take S2 (shots 1C+1D) — extension round (video-prompting ch. 14b; mode routing first)
On Seedance 2.5 a continuation is `video_extension` of the approved take, never a harvested start frame (ch. 14, W4 step 2); the counter-angle is internal shot 2 after a HARD CUT (production-pipeline ch. 16 rung 1), NOT the opening frame — the first frame of an extension is the source's last clean frame. The reverse plate keeps its own tag; tags are never re-used for a different asset. The boundary state is WRITTEN from the harvested last clean frame of the raw S1 export (ch. 14 boundary-frame source).

| Row | Content |
|---|---|
| Render ID | `LIGHTCAT_1C__HF-SD25__EXT__P01` (multi-shot take S2 = 1C+1D) |
| Intent | Cat holds at the lit lamp, then a low counter-angle as the beam starts to turn — 2 internal shots |
| Crew choices | Shot 1 keeps the S1 end position; Shot 2 WS 63° from the lamp side, 0.4 m above the floor; beam rotation as the light event |
| Run in | Higgsfield → web UI → project LIGHTCAT → Video → Seedance 2.5 → video_extension ("Extend", forward) — from reference HF-WEB@2026-09-04, not live-checked this session; confirm the Extend control on the live form before Generate |
| Settings | inherits 16:9 · 720p draft · +10 s · audio on |
| Inputs | 1. `@Video 1` = approved take S1 `LIGHTCAT_1A__HF-SD25__T2V__P01__TK03` (source; upload label per the live form) · 2. `@cat` = identity only · 3. `@loc_lamproom_rev` = set from the counter-angle only, Shot 2 only · 4. `@prop_lever` = lever only, state up |
| Handoff | Boundary = S1 ENDING STATE at the last clean frame (9.8 s of the raw export): cat seated facing the lit lamp, lever up, room warm amber, rain on glass |

```
SCENE CONTEXT: The extended segment directly continues from the last frame of @Video 1: the seated cat faces the lit lamp, lever up, room in warm amber, rain on the glass. Continue forward, do not replay. Two internal shots, 10 s.
ACTIVE REFERENCES: @cat controls only the cat — small grey tabby, wet clumped fur, white chest patch, green eyes. 100% matches the reference. Do not copy its neutral pose. @loc_lamproom_rev controls only the lamp room seen from the counter-angle — windows behind camera, hatch right, lever left; used from Shot 2 on. 100% matches the reference. Do not copy its emptiness. @prop_lever controls only the lever — state: up. 100% matches the reference.
FORMAT MODE: sequential cuts, 2 shots, 10 s — Shot 1 0.0–4.0 s, Shot 2 4.0–10.0 s.
OPTICS: Shot 1 MS at 47°; Shot 2 WS at 63°, low angle; no drift mid-segment.
CAMERA: Shot 1 static, same position as the end of @Video 1. Shot 2 static from the lamp side looking down at the cat, 0.4 m above the floor.
ACTION: SHOT 1 (0.0–4.0 s): the cat blinks slowly in the warm light, breathes out, tail settles. HARD CUT. SHOT 2 (4.0–10.0 s): from the counter-angle the lamp's beam begins a slow rotation overhead; the sweep of light passes across the cat's face; its ears lift and it watches the beam go.
LIGHTING: warm amber 3200K from above, rotating slowly; cold blue 8500K only in the window reflections.
AUDIO: {rain on glass, continuous} {low warm hum} {slow mechanical rotation from 4.0 s} 【no music, no BGM — room tone and effects only】
ENDING STATE: cat watching the rotating beam, lever up, room amber, rain on the glass.
STYLE: stylized 3D animated-feature look, matte rendered materials, soft global illumination; 24 fps, no grain.
POSITIVE LOCKS: exactly one cat; the lever stays up; the hatch–lever axis is never crossed; wet-fur state holds; every frame keeps the stylized 3D rendering.
```
On a model without an extension mode (Seedance 2.0 and others): harvest S1's last clean frame as the literal start frame (the chain case, SKILL rule 1), keep Shot 1 on that angle, place the counter-angle as internal Shot 2 after the HARD CUT.

## 5. QA and log (production-pipeline ch. 10 · post-audio-legal ch. 17–19 · SKILL rules 12, 14)
Batch of 4 (`…__T2V__P01__TK01–TK04`), watched fully — by the director when the agent cannot view the result — in six passes (identity → continuity → timing → camera → audio → style/Verify line), verdict order post-audio-legal ch. 19 (hard rejects → rank by emotion → repair local faults). Failure example: TK02 renders the lever already up at 5.0 s → a hard continuity fault in a rejected take; the fix belongs in the NEXT prompt (`…__T2V__P02`: lever lock moved next to the push line), not in post. TK03 approved → its Render ID becomes the shot board's `Approved-take Render ID`; from now on every local fault on TK03 is a `video_edit` (new Take ID), never a reroll. Grading, trim (±0.5 s, assembled cut only), score and loudness (−14 LUFS) in post.

Bible rows written at close (section B4b render/take log):
| Render ID | KEY | Changed vs previous | Take IDs | Verdict / approved take |
|---|---|---|---|---|
| LIGHTCAT_1A__HF-SD25__T2V__P01 | HF-WEB@2026-09-04 | first package | TK01–TK04 | TK02 lever pre-lit (reject); TK03 approved |
| LIGHTCAT_1C__HF-SD25__EXT__P01 | HF-WEB@2026-09-04 | extension of TK03, counter-angle as shot 2 | TK01–TK04 | TK01 approved |

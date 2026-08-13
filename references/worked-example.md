# Worked Example: 20-Second Spot, End to End

A compact walkthrough applying the pipeline to a fictional brief — read once to see how the chapters connect. Style: Pixar-adjacent stylized 3D. Model path: GPT Image 2 (plates/sheets) → Seedance 2.5 (motion).

## 1. Brief → shot plan (ch. 2)
Logline: a lighthouse keeper's cat sneaks out at night to relight the extinguished lamp. Renderability pass: paw-level object manipulation is risky → rescue: the cat pushes the lever with its whole body (big motion, no finger-class precision). Plan: 2 takes × ~10 s, 2 internal shots each.

## 2. Assets (ch. 3–5, style-control §2)
- **Location master plate** (GPT Image 2): style block FIRST ("This is a still from a Pixar animated feature film — NOT a photograph… painted CG material, subsurface scattering, soft global illumination…"), then scene (lamp room, brass lever, rain-streaked glass, warm practical lamp glow vs. cold blue night), then camera (35mm, f/4). Reverse decision: the lamp room needs a counter-angle for take 2 → generate the reverse plate via an angle tool or layout-map input NOW (ch. 16, rung 3), reverse-test against the master (anchors, light side, palette).
- **Character sheet** (cat): front/side/back/face/detail, neutral light, one canonical face. State sheet #2: "wet fur" (it rains) — a sheet order, not an adjective.
- Detail plate: the brass lever, state pair (down/up).

## 3. Take 1 prompt (ch. 12–14, style-control §5/7)
```
GLOBAL STYLE: whimsical Pixar-style stylized 3D animation, rounded simplified
forms, soft global illumination, subsurface-scattering fur, warm-cool contrast.
Every frame holds this exact rendering style.

REFERENCES: @image1 controls only the lamp-room set — layout, materials, light.
Do not copy its emptiness. @image2 controls only the cat — appearance, face,
markings (wet-fur state). Do not copy its neutral pose or background.
@image3 controls only the brass lever — shape and position, state: down.

SHOT 1 (0.0–5.0s): The wet cat squeezes through the half-open hatch, lands
softly, shakes rain off — droplets catch the cold blue window light. It looks
up at the dark lamp. Static wide from the room's corner.
HARD CUT.
SHOT 2 (5.0–10.0s): Medium shot: the cat rears up and pushes the brass lever
with both forepaws and its full body weight; the lever tips up with a heavy
clunk; a warm glow blooms from above, washing the room amber. The cat's eyes
widen; ears rise; it settles onto its haunches, tail curling.
AUDIO: rain on glass, wet-paw steps, the metallic clunk, a low warm hum as the
lamp ignites. No music.
CONSISTENCY: one continuous space; the camera never crosses the axis between
hatch (left) and lever (right).
ENDING STATE: cat seated facing the lit lamp, lever up, room in warm amber,
rain continuing on the glass.
CONSTRAINTS: no cuts inside shots, no slow motion, no duplicated cat, no
subtitles, no logos.

ATTACH: 1. @image1 = lamp-room master plate · 2. @image2 = cat sheet (wet
state) · 3. @image3 = lever detail (state: down).
```

## 4. Take 2 (state chaining, ch. 14/16)
Harvest the final frame of the approved take 1 as the new start frame (rung 2); prompt opens from the ENDING STATE ("continue forward, do not replay: the seated cat…"), uses the reverse plate as @image2 for the counter-angle, repeats the GLOBAL STYLE block and anchors verbatim.

## 5. QA (ch. 10/19)
Batch of 4, watched fully, five passes (identity → continuity → timing → camera → audio). Failure example: shot 2 renders the lever already up at 5.0 s → continuity fix belongs in the NEXT prompt ("lever starts down; it tips up only at the push"), not in post. Grading, trim (±0.5 s), score, and loudness (−14 LUFS) in post (ch. 17/18).

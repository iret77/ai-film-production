# Pixar/3D Look: Sourced Design Rules

Look bible for Pixar/3D-stylized projects. Rule-oriented, confidence labels as in production-pipeline.md, source per rule. **Verification note:** citations below are consistent with widely documented material and the model's training knowledge, but were not individually re-fetched — treat exact wordings as paraphrase-accurate, not quote-verified. This file owns look knowledge; model failure knowledge stays in renderability.md.

## 1. Core philosophy
🟢 **Believability, not realism.** Pixar's stated goal is believability; pure physical realism doesn't guarantee it. Documented case: a technically perfect skateboard-wheel shader was rejected by the Toy Story art director — correct, but not believable in film context. (Communications of the ACM, "Creating Lifelike Characters in Pixar Movies")
🟢 **Worlds are deliberately caricatured/idealized.** Ratatouille's Paris is "a loving caricature" per its makers; even Finding Nemo's near-photoreal water was intentionally caricatured. (AWN interviews)
**Prompt consequence:** describe worlds as "idealized/caricatured" — never "photorealistic".

## 2. Shape language
🟢 **"Simplexity"** (Ricky Nierva, production designer Up/Monsters Inc.): "the art of simplifying an image down to its essence; the complexity you layer on top — texture, design, detail — is masked by the simplicity of the form; simplexity is selective detail." (Cooper Hewitt exhibition text; The Art of Up)
🟢 Pete Docter: everything must read at first glance as a simple base shape — squares, circles. (AWN)
🟢 **Every shape is a symbol:** round = safe/warm, angular = threat.
**Prompt consequence:** rounded volumes as default; sharpness/edges only as designed exceptions with narrative purpose.

## 3. Color
🟢 **Color scripts are a mandatory document:** sequential paintings mapping light/color/mood per story beat — published by Pixar itself. (The Art of Pixar: The Complete Color Scripts)
🟢 **Saturation dramaturgy, not just hue:** Up runs high saturation while Ellie lives; desaturation to near-grayscale for grief and looming threat. (Nierva) Muted palettes are Pixar-conform when they follow a deliberate emotional curve (Ratatouille: pastel/sepia after Degas/Monet).
**Prompt consequence:** every project defines a mini color script with **temperature AND saturation per block** — the saturation column is not optional.

## 4. Light
🟢 **Sharon Calahan's four criteria** (SIGGRAPH-anchored): light must (1) guide the eye, (2) support the story emotion, (3) keep continuity, (4) add beauty to the composition.
🟢 **Explicit anti-physics stance:** "purely natural or physically correct lighting is often not interesting enough to create drama." (Calahan, SIGGRAPH 1996)
🟢 **Character light convention:** strong rim on the shoulders, soft light on the face — avoid hard direct light on faces. (Pixar lighting artists)
**Prompt consequence:** one motivated key is fine, but emotion beats correctness in the grade; specify "rim on shoulders, soft face light" for characters.

## 5. Camera
🟢 **Real lenses including curated imperfection.** Lens character (flares, distortion, focus breathing, deliberate "mistakes" in zooms/framing) creates the feeling of being filmed — but Pixar deliberately dials real artifacts DOWN where they look bad in CG. Detail evidence: case study WALL-E (§6c).
**Prompt consequence:** a stylized film may specify subtle lens character (soft flares, gentle DoF breathing) — never clean-CG perfection, never unfiltered full artifacts.

## 6. Case studies
### 6a. Piper — reference for miniature/macro worlds
🟢 Look built on macro photography; painterly exaggeration ("at first glance realism, but everything deliberately exaggerated — textures almost become a character", Barillaro); Norman Rockwell as painterly reference; faux nature-doc lens set with unusually consistent shallow depth of field. Core production question: "What does the world look like at the eye level of a sandpiper — four inches tall?" (RenderMan/Pixar official story, fxguide)
**Consequence:** for small-creature worlds, the shallow-DoF macro grammar IS the Pixar signal — set as the sequence-wide camera grammar, not a one-off effect.

### 6b. La Luna — license for material over physics
🟢 An immense pearlescent moon that characters physically climb; watercolor textures mapped onto CG, the moonrise literally a watercolor painting. (IndieWire, Casarosa interviews)
**Consequence:** celestial bodies may be scaled for wonder; painterly texture beats physical correctness.

### 6c. WALL-E — reference for lens character
🟢 Real Panavision anamorphics rented, measured, rebuilt in software — then real lens artifacts deliberately dialed down where they read badly in CG; barrel distortion, lens flares, focus breathing, even intentional "mistakes" in zooms/framing for the filmed feel; Roger Deakins consulted. (AWN, 3D World, press)

## 7. Prompt consequences (checklist for script/prompt writers)
1. **Rounded default forms** — edges only as designed threat exceptions.
2. **Idealized-not-photoreal vocabulary** — "caricatured, idealized, believable", never "photorealistic".
3. **Color script per block** with two columns: temperature + saturation (saturation curve = emotion curve).
4. **Motivated but emotional light** — "rim on shoulders, soft face light" for characters; drama before correctness.
5. **Subtle lens character** — soft flares, gentle DoF breathing; never clean-CG perfection.
6. **Macro-DoF grammar** for miniature/small-creature worlds (sequence-wide, not punctual).
7. **Scale-for-wonder license** for celestial objects; painterly texture before physics.

## 8. The figure as style anchor (hard rule)
🟢 **A Pixar look without a figure in frame does not happen by itself [PP — production-proven].** Isolated Pixar environments default to photoreal on EVERY image model (GPT Image 2, Nano Banana Pro, Seedream, Soul Cinema) — because Pixar environments themselves are near-photoreal (*The Good Dinosaur*: photoreal landscapes under cartoon characters; *Soul*/*Elemental* cityscapes similarly). The model has nothing to stylize against. The figure in frame forces the ENTIRE render into Pixar mode. This is not a workaround — figure + environment together IS the Pixar look, carried by character design and motion (oversized eyes, caricatured proportions, squash & stretch, weight). Two proven counters exist: (a) the figure anchor below, and (b) the prompt-only style-forcing method for figure-less environment stills (pixar-look ch. 9) — brightness-dependent; dark scenes combine both paths via the self-generated style anchor.
🟢 **Pipeline consequence — inverted build order for stylized projects (production-pipeline ch. 1):** (1) character sheets first (neutral grey, no location dependency — they define the project's stylization level) → (2) location ANCHOR plates generated WITH a figure in frame → (3) empty location backgrounds derived via edit model: remove the figure, the style stays baked in. Location-first remains correct only for photoreal projects.
🟢 **Plate judging:** an empty plate derived this way still reads idealized-realistic — that is correct, not a failure. Criteria for figure-less plates: simplified, rounded, slightly chunky geometry · clean uncluttered surfaces · controlled palette · soft light falloff · painted-CG material feel (subsurface glow, no photographic micro-noise). Never judge by "does it look cartoony" — that criterion produces endless, unwinnable regeneration loops.
🟢 **Model choice for the anchor render:** Nano Banana Pro is the strongest Pixar-from-scratch model (environment+figure in one 4K render, superior AO and subsurface scattering) [PP]; GPT Image 2 handles geography consistency, edits, and derivatives — prompt structure per style-control §2 (4-section pattern with the anti-pattern closer). Cinema Studio settings play no role here: they are VIDEO controls, first relevant at the motion test (platforms-models ch. 13).

## 9. Style-forced environment stills WITHOUT a figure (GPT Image 2, prompt-only) [PP]
🟢 Refines the production-pipeline ch. 1 hard rule (inverted build order): there IS a reliable prompt-only path to flat stylized environment stills with no character in frame — the style must be actively FORCED and every realism path explicitly blocked. Five building blocks that work only together:
1. **Priority sentence** placing style above realism: "stylized animated-feature design is more important than realism; favor appealing sculpted shapes and clean color separation over natural geology or accurate [material] physics."
2. **Thumbnail rule:** "every major form must be readable at thumbnail size" — forces large, simple, readable forms over detail density.
3. **Flat-graphic style block:** "graceful graphic color blocking, clean color separation, deliberately simplified sculpted forms, clean readable silhouettes, smooth matte surfaces, minimal surface noise; must read as stylized animated concept art, not as a photograph or physically based render."
4. **Render-treatment block** killing photo signals: "soft global illumination, gentle ambient occlusion only, diffuse matte materials, restrained reflections, no photographic depth of field, no lens flare, no film grain."
5. **Explicit avoid block** naming the realism traps: "photorealism, PBR-render look, gritty texture, fine realistic cracks, naturalistic documentary lighting" + scene-specific unwanted forms. Omission is not enough — the traps must be named and forbidden.

Add "do not imitate any particular studio, film, franchise, or character design" to keep the look generically stylized and IP-clean (also festival-safe).

**Proven template (produced the target look directly, no reference image — bright daylight ice world; swap the Scene block for other environments):**
```
Create an original cinematic Antarctic ice-world establishing shot in a polished, highly
stylized 3D animated-feature aesthetic.
Scene: A vast Antarctic ice shelf stretching to the horizon, entirely frozen. Broad, smooth
snow-covered ice floes form soft, irregular, naturally flowing shapes. Gentle pressure ridges,
a few broad blue-ice fissures, several large tabular icebergs with softly rounded wind-eroded
profiles. Sparse dark rocky nunataks far away on the horizon.
No open water: no ocean surface, meltwater, lake, reflection, wet ice, or visible liquid.
Must read unmistakably as Antarctica — immense, wind-sculpted, frozen.
Style: Premium family-animation environment design. Deliberately simplified sculpted large
forms; clean readable silhouettes; smooth matte snow; translucent cyan blue-ice edges;
graceful graphic color blocking; minimal surface noise. Must read as stylized animated
concept art, not a photograph or physically based render. Do not imitate any particular
studio, film, franchise, or character.
Visual priority: Stylized animated-feature design is more important than realism. Favor
sculpted shapes and clean color separation over natural geology or ice physics. Every major
ice form readable at thumbnail size.
Composition: Ultra-wide 16:9 establishing shot, low viewpoint. Clear three-layer depth:
foreground floes, midground ridges and icebergs, distant nunataks. Generous open sky, level
horizon.
Camera: 24mm wide-angle, eye level; no aerial view, no dramatic tilt.
Lighting/palette: Bright clear polar daylight; saturated turquoise-blue sky; bright white
snow; luminous azure/cyan ice; soft lavender-blue shadows; subtle warm sunlight along
selected edges. Calm, inviting.
Render treatment: Soft global illumination, gentle ambient occlusion only, diffuse matte
materials, restrained reflections, no photographic depth of field, no lens flare, no film
grain.
Constraints: Environment only. No characters, animals, buildings, text, logos, watermark,
frame.
Avoid: Open water, ocean surface, meltwater, reflections, photorealism, PBR-render look,
gritty texture, fine realistic cracks, naturalistic documentary lighting, hard right-angle
cliffs, cuboid icebergs, square slabs, ice castles, needle-like fantasy spires, forests,
Arctic fjord scenery.
```

🟢 **Brightness is the deciding factor — and the method for DARK scenes:** bright + saturated + daylight drives GPT Image 2 into the flat cartoon mode on its own; dark/night scenes (twilight, black sky) pull it back to photo, where prompt mechanics alone often fail. For dark target scenes:
1. First generate a BRIGHT daylight still in the target style with the core method above (reliable).
2. Attach that self-generated bright image as the STYLE reference to the actual dark prompt.
3. Restrict the reference strictly to style/rendering/flatness/stylization level; explicitly instruct NOT to copy lighting, sky, composition, or forms.
4. Mark the dark lighting as a deliberate deviation ("key change from the reference") and add an anti-relapse anchor: the forms stay as graphic and flat in the darkness as in the bright reference — never grim-photographic.
The flat look then survives the dark palette that would otherwise destroy it. Where platform rules require all assets generated in-project (contests/festivals), such a style anchor is only admissible if it was itself generated in-project by prompt — never external imagery.

🟢 **Proven refinements:**
- **"Everything round" is wrong:** the look does not require uniformly round forms. Angular, pointed, faceted, planar silhouettes are fully style-conform — the look comes from flat graphic color separation and clean silhouettes, not from roundness. Prompt shapes as a deliberate mix (pointed spires, planar faces, faceted blocks, some softer forms).
- **Separate silhouette from surface:** demand angular/faceted silhouettes AND flat graphic surfaces at the same time, so faceted material doesn't tip into PBR via realistic shading ("faceted, but every facet a flat color plane — like a low-poly gemstone in an animated feature").
- **Force monumental scale explicitly** (towering, seen from a very small observer's viewpoint) or the world reads too small.
- **Key sky objects (e.g. a moon) as a clearly readable disc** with soft surface shading and a clean round edge — otherwise the model renders only a vague glow.

## 10. Case study: "Passport Rush" — Higgsfield's own hybrid previs-to-AI stylized short (Sep 2026) [H-off, P23]
Source: Higgsfield's first-look thread with a side-by-side of storyboard / Blender previs against the final render, six stated learnings, one copy-ready prompt; a full pipeline breakdown was announced for YouTube (revisit when published). Everything below is read from the published frames and the thread text — the platform's own production, so the pipeline claims are official; the look analysis is ours.

🟡 [our read of the published frames] **The look is a HYBRID, and the hybrid is the method:** 3D-toon characters and hero vehicle (rounded CG volumes, subsurface skin, caricatured proportions — the ch. 8 figure) over **painterly watercolor environments** (visible brush texture on hills, trees, sky; soft edges) with **2D-drawn FX** (the explosion carries hand-drawn swirl doodles, the log crash painted, not simulated). Detail inserts (rope over logs, speedometer) are pure watercolor. Consequence: a "Pixar look" project may deliberately split media — character = sculpted 3D, world = painted, FX = drawn — and the split reads as design, not as inconsistency, PROVIDED one reference is declared the style donor (below).

🟢 **Pipeline order, confirmed on the platform's own film: storyboard → Blender previs → AI, in that order, before a single frame is generated.** The storyboards carry motion arrows (camera/motion in one colour, impact in another) and shot numbers (sc1…sc17); the previs is a COLOURED low-poly blockout (yellow taxi, red truck, blue bus, green ground plane, box buildings) — colour identity travels from previs to final, geometry does not need to; camera moves and cuts of the previs are reproduced 1:1 in the final (low front-bumper tracking, overhead, cabin POV, whip past the truck). Route: production-pipeline ch. 8 (clay render / blockout path); the previs clip is the @Clay Render reference, the character sheet and painted plate carry the visuals.

🟡 [our read of the published frames] **Character sheet as a CG turnaround:** A-pose front and back full-body plus a large face close-up, neutral cream background, rendered as a finished 3D character (fabric weave on the cap, glasses, moustache fibres) and then deliberately DRAWN OVER with pencil hatching and stray sketch strokes on shirt, jeans, cap and skin (visible at full resolution in the vendor's second thread). The sheet defines the project's stylization level (ch. 8) — here "CG figure with hand-drawn marks" — and those drawn marks are what the style-donor prompt below propagates: the background and the untextured taxi picked up painterly texture because the character reference already carried it. Consequence: if the world is to read painted, put the paint on the character sheet first. Small props on the sheet (thin glasses) are identity here, not clutter; the accessory rule (production-pipeline ch. 3) applies to non-identity details only.

🟢 **Wide shots are the failure class of stylized 3D — scale and distance break at wide range.** The fix that held: generate the take as a short CUT SEQUENCE that opens on a close or medium of the character and transitions INTO the wide within the same generation; the model carries scale from the close shot into the wide. A wide shot generated on its own kept breaking. ⚠️ This refines the photoreal habit "open on a wide establishing to lock positions" (renderability ch. 5): in stylized 3D, lock positions with the previs/clay render and let the wide arrive by transition.

🟢 **Faces that must stay blank are hidden by design, not animated.** Two silent passengers in a taxi: instead of asking for neutral faces (the model animates them anyway — micro-expressions, drift), the film hides them behind reflective glass. Copy-ready block (verbatim from the thread; also filed under video-prompting 12e):
```
GLASS: all the taxi's windows are semi-transparent and heavily reflective, sky, road and
passing scenery slide across them, and the interior sits in shadow. The two passengers are
almost invisible, present only as soft dark silhouettes veiled by the reflections and the
tint, their poses and gestures readable purely by shape.
```
Generalize: any performer without a beat gets an occlusion motivated by the world — glass, backlight silhouette, hat brim, distance, frame edge — written as a positive description of what IS visible (ellipsis over simulation, SKILL rule 7).

🟢 **Closing rule of the vendor's thread:** "Don't ask AI to do everything. Use Blender to control the things that need control. Use AI where it gives you leverage." — camera, composition, timing from previs; surfaces, light, motion detail from the model.
🟢 **Style unification by declared donor:** character and background came from two different styles; the prompt that closed the gap: **"take the style of the character and apply it to the background"** — pushed harder or softer to control the blend. Observed effect: the taxi that entered as untextured previs geometry left with watercolor texture on hood and cabin, picked up from the character. This is the ch. 8 figure-anchor rule confirmed by the vendor's own production, with the operational form: name the donor reference and the receiver in the STYLE role line ("@hero donates rendering style to @loc_highway and @taxi; geometry from @Clay Render"), and dose the blend in words (subtle / partial / full transfer).

🟡 [our read of the published frames] **Comedy physics survive because the look absorbs them:** a log through a cabin, a mushroom-cloud explosion — rendered as painted/drawn FX, not simulated. The stylized register forgives what photoreal would expose (renderability ch. 4 format matrix); keep hero physics in stylized projects, never in photoreal ones.

🟡 [our read of the published frames] **Title text arrived in post** (the "PASSPORT RUSH" card over the final frame) — the unified in-frame-text rule holds even for the vendor's showcase.

# Pixar/3D Look: Sourced Design Rules

Look bible for Pixar/3D-stylized projects. Rule-oriented, confidence labels as in pipeline.md, source per rule. **Verification note:** citations below are consistent with widely documented material and the model's training knowledge, but were not individually re-fetched — treat exact wordings as paraphrase-accurate, not quote-verified. This file owns look knowledge; model failure knowledge stays in renderability.md.

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

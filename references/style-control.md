# Style Control: Enforcement, Model Mechanics, Vocabularies

Standalone reference for everything style-related across image AND video models. Confidence labels as in pipeline.md. **Methodology note:** vocabulary packages are marked 🟢 when sources converge; since style blogs copy each other, convergence may partly be citation echo — treat vocabularies as strong starting points, and let your own motion-ladder test (pipeline ch. 19) be the final judge. Pixar look definition: `pixar-look.md`.

## 1. Style stack hierarchy (all models)
🟢 Descending force: **(1) reference images that carry the look → (2) platform settings (CS 4.0 palette/lighting/camera) → (3) prompt style block → (4) model default (usually photorealism).** Video models do not re-stylize on their own: photoreal plate + Pixar prompt = photoreal video; stylized plate + Pixar prompt = stylized video. The look is won in the STILLS (stills-first, pipeline ch. 1); the prompt only secures it.
🟢 Why a single style word fails: models default to photorealism; a label without an anchor is overruled or decays after beat 1. Style needs the stack, not a word.
🟢 **Image block vs. video prompt — do not confuse them.** For IMAGE models (GPT Image 2) the style block goes FIRST and works (§2). For VIDEO prompts there is NO glued style-prefix at the top: style is distributed into the blocks that govern each aspect (pipeline ch. 12, placement rule 1). The old "paste one style prefix on every video prompt" idea came from a single creator's convenience note and did not hold up — GPT Image 2 and Seedance both ignore a floating style prefix; the reference image and the per-block placement carry the look instead.

## 2. GPT Image 2 — style mechanics
🟢 **Reasoning model, not a keyword matcher:** plans composition before generating; natural descriptive sentences beat adjective/tag chains ("8k, masterpiece, trending" do nothing). Conflicting style mixes produce mud — ONE dominant style per prompt.
🟢 **Style block first:** sweet spot 100–300 words; beyond ~500, early instructions get ignored — a long scene description must not push the style block back. Formula: style anchor → subject → details → rendering specs.
🟢 **Actively repel the photoreal default:** "Pixar style" alone is not enough. What works: (a) **early negation as repulsion anchor** — "NOT a photograph. NOT photorealistic. NOT a nature documentary." (community tests: ~80% photoreal without it; the official cookbook uses the same technique inversely: "Avoid cinematic lighting" for documentary realism) — plus (b) **concrete rendering cues**: `subsurface scattering on all surfaces` (strongest single cue), `soft ambient occlusion`, `soft global illumination`, `painted CG material — every surface reads as rendered, not photographed`, `cinematic warm-cool color grade`.
🟢 **Film-reference framing beats technical adjectives:** "This is a still from a Pixar animated feature film / a $200M animated feature."
🟢 **Max 3 edit iterations per asset** — quality degrades after (noise, shadow artifacts) → rewrite the prompt and regenerate. Refinements: one variable per round; preserve list on every edit ("change only X, keep subject identical").
🟢 **Know the weaknesses:** strong at structured, text-heavy production output; weaker at atmospheric painterly imagery — the style block must be extra strong there. In-image text: exact wording in quotes, 1–5 words, state the position. Resolution: >2K experimental — generate lower + upscale.
🟡 **Material rule for critical surfaces** (ice/snow as example; applies to glass/water/metal): the model renders these photoreal (wet, transparent, crystalline). Counter-recipe: anchor the desired material positively AND negate the photo appearance — "matte powdery surface like fresh dry snow — NOT wet, NOT glossy, NOT transparent. Reads as painted CG material."

### Prompt template: stylized environment plates (GPT Image 2)
```
[STYLE — always first]
This is a still from a Pixar animated feature film — a 3D animated world,
NOT a photograph, NOT photorealistic, NOT a nature documentary. Every surface
reads as a painted CG material with soft subsurface scattering, not as a
real-world texture. The geometry is simplified and chunky with soft rounded
edges — caricatured and idealized. Rendering: soft global illumination, soft
ambient occlusion, gentle rim light, cinematic warm-cool color contrast.
The overall look is warm, handcrafted, and unmistakably animated.

[SCENE — natural sentences: geography, objects, light]
[CAMERA — focal length, angle, focus, DoF]
```

## 3. Nano Banana Pro — style mechanics
🟢 **Style-transfer syntax with feature lock:** "Same character as the reference image, redrawn in the style of [X]. Maintain [unique features: scar, hair length, earrings…]." Without explicit feature naming, transfer generalizes the face into a generic anime face. Repeat garment specifics at EVERY zoom level.
🟢 **Placement inverse to GPT Image 2:** lock facial markers via text tokens, put the **new style medium at the END of the prompt**; keep outfit + pose identical to the reference for the first transfer.
🟢 "Too realistic" fix: strengthen style keywords (anime style, cel shaded, comic book art) + attach a style reference image (1–3 refs: character/style/background separate).
🟢 Multi-character: map left-to-right explicitly; from 3 characters, **scaffold** — generate two, lock, then add one character at a time onto the locked image (otherwise feature swapping). Capacity ~5 characters/14 objects.
🟢 Manga/comic specialty: full-page generation (one whole page instead of single panels) keeps characters consistent across panels and lays out itself.

## 4. Soul Cinema & Seedream — style role
🟢 Soul Cinema: cinematic (photoreal) default look — first choice for REALISTIC characters/locations from scratch, not the stylization specialist. For stylized sheets: GPT Image 2 (with §2 stack) or Nano Banana Pro (§3). Seedream 4.5: edits with texture preservation.

## 5. Video layer (Seedance 2.x / Cinema Studio)
🟢 Style comes from the references (§1); the video prompt only secures it, and it does so **distributed, not as a prefix** (pipeline ch. 12): light in LIGHTING, colour in COLOR GRADE or LOCATION, optics in OPTICS, acting/skin in PERFORMANCE, physics in PHYSICS; only the technical look word (photoreal, grain, format) sits in the STYLE suffix near the end. Repeat the load-carrying style aspects in POSITIVE LOCKS. Exclude style bleed from photoreal references ("Use @X for layout and light only. Do not copy its photographic rendering."). Declare mixed styles explicitly ("photorealistic environment, stylized characters"). Motion must match the style (limited animation = static bodies + tableau camera; Pixar = squash & stretch, weight). Official formula: "@image is the first keyframe and style reference."
🟢 CS 4.0: style additionally via settings (palette/lighting/era) — dials before prompt, avoid double control (pipeline ch. 13).

## 5b. Style control per video model
🟢 **Meta-finding (multi-source):** no universal style winner — run a **motion ladder** per style and model (subtle portrait → head turn → walk → fast action → interaction). Never copy prompts 1:1 between models.

🟢 **Seedance 2.x / CS:** style distributed across the block structure (pipeline ch. 12); references carry the look, blocks secure it. Photoreal default is strong — stylized needs look-carrying references AND an explicit anchor.
🟢 **MiniMax H3:** LoRA training is the strongest style-lock path (train a style/character/motion LoRA, then prompt against it); without it, one committed style word + a style reference image, restated per shot.
🟢 **Kling 3.0:** each generation is interpreted independently — repeat the style keywords AND re-attach the style reference image in EVERY prompt of a sequence, or the look drifts. Never mix realism + anime in one prompt.
🟢 **Veo 3.1:** physics-correct realism is the default gravity well; stylized looks need the motion grammar prompted along ("2D limited animation, held cels, no physical inertia") or Veo pulls back toward realism.
🟢 **Grok Imagine:** native stylization bias (cartoon/anime) — style qualifier at the very START; for photoreal intent, push the other way with realism cues, or it drifts cartoonish.

## 6. Style vocabularies (starting points — verify per motion ladder)

### 6a. Animation styles
🟢 **Pixar / feature 3D:** "3D animated feature film, painted CG materials, subsurface scattering, soft global illumination, rounded chunky geometry, caricatured proportions, warm-cool grade." Motion: squash & stretch, weight, anticipation. Full look bible: pixar-look.md.
🟢 **Hanna-Barbera / limited TV animation:** flat color fills, bold outlines, minimal shading, repeating backgrounds. Motion: static bodies, isolated limb movement, tableau camera — do NOT prompt fluid full-body motion.
🟢 **Rubber hose (1930s):** bendable limbs without joints, circular hands, bouncy pie-cut eyes, black-and-white or muted, "on the beat" motion; pairs with old-film grain.
🟢 **Anime (modern TV):** cel shading, hard shadow steps, expressive eyes, speed lines for action, motion-blur smears, held dramatic poses. Anime is a Seedance/Kling strength — high-action is the sweet spot.
🟢 **Chibi:** oversized head, tiny body, minimal features, bouncy motion; keep scenes simple.
🟢 **Stop-motion / claymation:** fingerprint texture on surfaces, slight frame-step judder ("on twos"), handmade imperfections, felt/clay materials.

### 6b. Footage & era styles (rescue-capable — degradation hides artifacts)
🟢 **VHS / 90s home video:** chroma bleed, scan lines, tracking wobble, timestamp overlay (in post, not in-frame), soft focus, blown highlights.
🟢 **16mm / Super 8:** organic grain, gate weave, halation on highlights, slightly desaturated warm cast.
🟢 **CCTV / surveillance:** fixed high angle, fisheye edge distortion, low frame rate, monochrome or desaturated, timestamp (post).
🟢 **Found footage / handheld doc:** operator breathing, whip corrections, focus hunting, lens flares — the UGC realism lane.
🟢 **35mm cinema:** fine grain, anamorphic flares, shallow DoF, filmic highlight roll-off; the "expensive" look.

### 6c. Optical / lens character
🟢 Anamorphic (oval bokeh, horizontal blue flares, 2.39:1 feel) · vintage (low contrast, warm halation, soft corners) · clinical (edge-to-edge sharp, deep focus) · macro (extreme close, razor DoF). Tie to FOV from pipeline ch. 12d.

## 7. Reference integration protocol
🟢 **Attach → address:** every reference image must be (a) attached in the platform AND (b) addressed in the prompt with a job and exclusions. A reference the prompt does not name does not exist for the model; a reference named but not attached forces the model to invent it into frame.
🟢 **One line per reference:** `@tag controls only [job: e.g. face + hair]; do not copy [exclusions: e.g. the photographic rendering, the background]`. End every reference-using prompt with an attachment checklist in upload order.
🟢 **Job separation:** split a reference's roles explicitly — "@plate for layout and light only", "@char for identity only", "@style for rendering medium only" — so the model doesn't blend a photoreal plate's rendering into a stylized character.
🟢 **Per-scene selection:** with large reference pools (2.5: up to 50), select only the references a scene needs — "a casting pool, not a shopping list" (pipeline ch. 14). Unused references drift into frame.

## 8. Style diagnosis (when the look is wrong)
🟢 **Photoreal when you wanted stylized:** the anchor is too weak or a photoreal reference is bleeding rendering → strengthen the style anchor, add rendering cues (§2), exclude the reference's rendering ("do not copy its photographic look").
🟢 **Style decays after beat 1:** the style block sits too late or isn't restated → for images move it first (§2); for video distribute it into home blocks and restate in POSITIVE LOCKS (§5, pipeline ch. 12).
🟢 **Face generalizes under style transfer:** unique features not named → lock markers by text token (§3, Nano Banana).
🟢 **Look drifts across a sequence:** references not re-attached / keywords not repeated (Kling especially) → repeat both every prompt (§5b).
🟢 **Motion contradicts style:** fluid motion on a limited-animation look → match motion to the style medium (§6a).

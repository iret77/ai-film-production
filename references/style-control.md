# Style Control: Enforcement, Model Mechanics, Vocabularies

Standalone reference for everything style-related across image AND video models. Confidence labels as in production-pipeline.md. **Methodology note:** vocabulary packages are marked 🟢 when sources converge; since style blogs copy each other, convergence may partly be citation echo — treat vocabularies as strong starting points, and let your own motion-ladder test (post-audio-legal ch. 19) be the final judge. Pixar look definition: `pixar-look.md`.

## 1. Style stack hierarchy (all models)
🟢 Descending force: **(1) reference images that carry the look → (2) platform settings (CS 4.0 palette/lighting/camera) → (3) prompt style block → (4) model default (usually photorealism).** Video models do not re-stylize on their own: photoreal plate + Pixar prompt = photoreal video; stylized plate + Pixar prompt = stylized video. The look is won in the STILLS (stills-first, production-pipeline ch. 1); the prompt only secures it.
🟢 Why a single style word fails: models default to photorealism; a label without an anchor is overruled or decays after beat 1. Style needs the stack, not a word.
🟢 **The strongest single style carrier for stylized-3D is a FIGURE in frame [PP]:** stylized environments without a character default to photoreal on every image model (their real-world counterparts are near-photoreal); the character forces the whole render into the stylized mode. Hard rule + inverted build order: production-pipeline ch. 1; proven prompt-only alternative for figure-less environments: pixar-look production-pipeline ch. 9 (style-forcing blocks; brightness-dependent).
🟢 **Image block vs. video prompt — do not confuse them.** For IMAGE models (GPT Image 2) the style block goes FIRST and works (§2). For VIDEO prompts there is NO glued style-prefix at the top: style is distributed into the blocks that govern each aspect (video-prompting ch. 12, placement rule 1). The old "paste one style prefix on every video prompt" idea came from a single creator's convenience note and did not hold up — GPT Image 2 and Seedance both ignore a floating style prefix; the reference image and the per-block placement carry the look instead.

## 2. GPT Image 2 — style mechanics
🟢 **Reasoning model, not a keyword matcher:** plans composition before generating; natural descriptive sentences beat adjective/tag chains ("8k, masterpiece, trending" do nothing). Conflicting style mixes produce mud — ONE dominant style per prompt.
🟢 **Style block first:** sweet spot 100–300 words; beyond ~500, early instructions get ignored — a long scene description must not push the style block back. Formula: style anchor → subject → details → rendering specs.
🟢 **Production-proven 4-section Pixar structure [PP] — supersedes keyword-avalanche openers:** a front-loaded keyword chain ("whimsical Pixar-style stylized 3D animation, rounded simplified forms, soft global illumination, subsurface scattering…") as the opening line does NOT hold. What works:
```
[1 FRAME]  A Pixar-quality 3D animation still, [format]. Cinematic feature-film look, [lighting].
[2 SCENE]  Concrete scene: specific objects, materials, light — 5–12 concrete nouns.
[3 CHARACTER]  The figure with explicit Pixar proportions: "expressive, slightly oversized eyes
           (classic Pixar proportions)", sculpted detail, believable surface.
[4 ART DIRECTION]  "full-CG Pixar aesthetic — subsurface scattering on [specific surfaces],
           physically based materials, soft shadow ambient occlusion, [specific light cues].
           Clean stylised shapes consistent with [2–3 Pixar film titles] — not photoreal
           uncanny-valley."
```
The anti-pattern closer ("not photoreal uncanny-valley") at the END of the art-direction section is essential — without it GPT Image 2 drifts back to photoreal. Film titles as aesthetic lineage are established (§6b); characters stay original. And the figure-anchor hard rule applies (production-pipeline ch. 1): a stylized still without a figure defaults to photoreal on EVERY model — section 3 is not optional for look-defining renders.
🟢 **Actively repel the photoreal default:** "Pixar style" alone is not enough. What works: (a) **early negation as repulsion anchor** — "NOT a photograph. NOT photorealistic. NOT a nature documentary." (community tests: ~80% photoreal without it; the official cookbook uses the same technique inversely: "Avoid cinematic lighting" for documentary realism) — plus (b) **concrete rendering cues**: `subsurface scattering on all surfaces` (strongest single cue), `soft ambient occlusion`, `soft global illumination`, `painted CG material — every surface reads as rendered, not photographed`, `cinematic warm-cool color grade`.
🟢 **Film-reference framing beats technical adjectives:** "This is a still from a Pixar animated feature film / a $200M animated feature."
🟢 **Max 3 edit iterations per asset** — quality degrades after (noise, shadow artifacts) → rewrite the prompt and regenerate. Refinements: one variable per round; preserve list on every edit ("change only X, keep subject identical").
🟢 **Object size: relation or mask — NEVER canvas fractions [PP]:** image models have no concept of "percent of image width" — that is a post-hoc measuring unit for humans, not something the model reasons in. It thinks in objects and their relations, not in frame shares, so "~1% of the image width" style size specs fail silently and burn reroll budget (production evidence: four consecutive %-scaled runs, all wrong-sized). What works, in order: (a) **relational anchoring** to an object of known size already in frame — "no larger than the pebbles beside it", "the size of @X in the frame"; (b) for hard size constraints in an EDIT: **masked/region inpaint** — mask exactly the target area and let the object generate only into the mask; the mask, not the text, then defines the size. Know the coupled failure mode: **detail demand inflates size** — the moment the prompt asks for visible detail (facets, engraving, texture) on a small object, the model enlarges the object to fit the detail, and no wording overrides that; the mask path is the only technical fix, the relational anchor the only prompt-level mitigation. Numeric canvas units (%, px, fractions of frame) are ballast at best and actively counterproductive at worst — this applies to every image model, not just GPT Image 2.
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

### Structured image-prompt patterns [G2-gallery]
🟢 **Layout before subject:** when structure matters (sheets, grids, storyboards, posters, plates with fixed composition), allocate space FIRST — canvas, aspect ratio, grid/zone layout — then describe the subject. Stated late, layout gets improvised.
🟢 **JSON/config-schema prompts** are a proven GPT Image 2 pattern for stills with many interacting systems (environment + subject + materials + lighting + particles + render goals): keys name visual subsystems (GLOBAL_SETTINGS / ENVIRONMENT / CORE_ASSETS / DETAIL_SYSTEMS / OUTPUT with an avoid-array), values are concrete visual constraints. Useful for complex hero plates and product/commercial work; JSON needn't be machine-valid — clean and readable suffices.
🟢 **Director-lineage scene formula** (extends the director-signature shorthand): "A [shot type] in the lineage of [director/film aesthetic]'s [signature]. [Scene with 5–12 concrete nouns]. The color palette is a strict scheme of '[Named Tone 1]', '[Named Tone 2]', '[Named Tone 3]'. Lighting: [source, direction, contrast]. Camera: [lens, angle, focus]. The mood is [2–3 words]." Naming palette tones in quotes as proper nouns ('Millennial Pink', 'Amber and Cobalt') binds them noticeably harder than loose color words. Legally safe as aesthetic lineage; keep characters and settings original.
🟢 **Capture-context phrases for photoreal stills** (name HOW it was captured, not that it's realistic): "RAW, unprocessed, full iPhone camera quality" (kills AI polish) · "amateur photo, shot from the crowd at a distance" (real-event feel) · "eye level, 28 mm lens feel" (architectural) · "natural morning side light" (lifestyle). ONE dominant capture frame per prompt — stacked camera specs conflict.
🟢 **Scene density beats adjectives:** 5–12 concrete nouns + 2–4 material/light constraints; empty quality words ("stunning", "professional", "8k") do nothing in a reasoning image model.

## 3. Nano Banana Pro — style mechanics
🟢 **Style-transfer syntax with feature lock:** "Same character as the reference image, redrawn in the style of [X]. Maintain [unique features: scar, hair length, earrings…]." Without explicit feature naming, transfer generalizes the face into a generic anime face. Repeat garment specifics at EVERY zoom level.
🟢 **Placement inverse to GPT Image 2:** lock facial markers via text tokens, put the **new style medium at the END of the prompt**; keep outfit + pose identical to the reference for the first transfer.
🟢 "Too realistic" fix: strengthen style keywords (anime style, cel shaded, comic book art) + attach a style reference image (1–3 refs: character/style/background separate).
🟢 Multi-character: map left-to-right explicitly; from 3 characters, **scaffold** — generate two, lock, then add one character at a time onto the locked image (otherwise feature swapping). Capacity ~5 characters/14 objects.
🟢 Manga/comic specialty: full-page generation (one whole page instead of single panels) keeps characters consistent across panels and lays out itself.

## 4. Soul Cinema & Seedream — style role
🟢 Soul Cinema: cinematic (photoreal) default look — first choice for REALISTIC characters/locations from scratch, not the stylization specialist. For stylized sheets: GPT Image 2 (with §2 stack) or Nano Banana Pro (§3). Seedream 4.5: edits with texture preservation.

## 5. Video layer (Seedance 2.x / Cinema Studio)
🟢 Style comes from the references (§1); the video prompt only secures it, and it does so **distributed, not as a prefix** (video-prompting ch. 12): light in LIGHTING, colour in COLOR GRADE or LOCATION, optics in OPTICS, acting/skin in PERFORMANCE, physics in PHYSICS; only the technical look word (photoreal, grain, format) sits in the STYLE suffix near the end. Repeat the load-carrying style aspects in POSITIVE LOCKS. Exclude style bleed from photoreal references ("Use @X for layout and light only. Do not copy its photographic rendering."). Declare mixed styles explicitly ("photorealistic environment, stylized characters"). Motion must match the style (limited animation = static bodies + tableau camera; Pixar = squash & stretch, weight). Official formula: "@image is the first keyframe and style reference."
🟢 CS 4.0: style additionally via settings (palette/lighting/era) — dials before prompt, avoid double control (platforms-models ch. 13).

## 5b. Style control per video model
🟢 **Meta-finding (multi-source):** no universal style winner — run a **motion ladder** per style and model (subtle portrait → head turn → walk → fast action → interaction). Never copy prompts 1:1 between models.

### Seedance 2.0/2.5
🟢 **Flat 2D is harder than stylized 3D** — the counterintuitive core finding: Pixar-ish 3D forgives (gradients hide frame errors), flat cel punishes every wobble ("lines crawl, the whole frame boils"). Flat 2D needs simpler motion and stricter control.
🟢 **Anti-3D fix for flat anime:** (1) explicit flat rendering terminology: "solid vector lineart, unlit flat tones, traditional anime cel-shading, flat sRGB color space" — suppresses depth maps and forced ambient occlusion, holds line weights in fast motion; (2) targeted negative constraints against 3D depth (conforms with the revised negative rule, video-prompting ch. 14).
🟢 **Style anchor workflow:** declare flat cel style in the first line + limited palette + character references; drafts on Mini/2.0, finals on the full model. Name the production technique, never a mood ("flat cel shading, bold outlines, no motion blur" not "anime feeling").
🟢 **Official whole-video style lock pattern:** "The entire video must match this exact 2D anime illustration aesthetic. Maintain consistent 2D anime illustration style throughout all frames." And mixed media **per element**: "photorealistic environment with real people, cel-shaded flat coloring on hero only, cartoon physics and expressions on hero only."
🟢 Style transfer: attach a style reference + "in the visual style of the reference"; director/DoP/film references as anchors ("Wes Anderson symmetrical framing") — **one** style reference per prompt.
🟡 Also viable: pixel art (limited palette, hard edges, no anti-aliasing, four-frame gait cycle) and oil paint with moving brushstrokes.

### MiniMax H3 (Hailuo 3)
🟢 Stylization strengths: **holds line quality and proportions in 2D/anime** ("which most video models struggle with"); realism trends plastic. Specs: 4–15 s, 24 fps, 768p base + 2K-regenerate module; one beat per shot.
🟢 **Unique capability — LoRA:** trained LoRAs (own clips/keyframes) hard-lock style, character, or motion — the strongest available style lock when a look must stay identical across many clips.
🟢 Prompt logic: action chain (cause→motion→reaction, chronological) instead of scene description; official modes T2VA/I2VA/FL2VA.

### Kling 3.0
🟢 **Strongest stylization flexibility of the photoreal class**; multi-shot mode holds the art style across shots — hence the anime recommendation of several comparisons. But: anime sits outside the comfort zone → **2–3× reroll budget** vs. realism.
🟢 **Style drifts per generation:** Kling interprets each generation independently — repeat identical style keywords in EVERY prompt of the sequence + reuse the same style reference image. Never mix realism and anime in one prompt.
🟢 MotionControl: reference action video + face binding for body/face/hand motion.

### Veo 3.1
🟢 Photorealism-first: overly smooth physics-correct motion works **against** anime aesthetics (stylized movement is exaggerated, not correct). Can stylize when the motion grammar is prompted along: stop-motion via "12 fps judder, frame-to-frame jitter, no motion blur, preserve handmade imperfection"; anime via "squash-and-stretch, impact frames, speed lines" + "keep character on-model across shots"; vector flat for explainers.

### Grok Imagine (1.5)
🟢 **Native stylization bias:** drifts cartoonish/Pixar-like on its own (even converts photoreal intent) — several aggregator matrices list it as THE pick for "stylized: anime, cyberpunk, cartoon, music-video, art-directed". Negatives unreliable → style qualifiers at the prompt START. 720p cap (1.5: 1080p in modes).

### Wan 2.5/2.6 · LTX
🟡 Wan: open-weight, cheap, LoRA-capable, multi-shot + reference-to-video (2.6), 1080p — budget alternative with pipeline ownership; LTX-2.3 for own LoRA pipelines, LTX-2 Retake for partial repairs without full regeneration.

### Restyle path (video-to-video, distinct production route)
🟢 Fully restyling existing footage (live action → anime/Pixar/claymation/pixel art) is production-ready — reference class **Runway Aleph** (in-context V2V: re-skinning, object edits, relighting with preserved motion); alternatives Luma Modify, GoEnhance et al. Prompt pattern: short and specific — "Detailed anime film aesthetic, **stable facial structure**, soft cel shading, cinematic anime lighting"; specificity beats length. ⚠️ The quality test is MOTION: many "restyle" apps are frame filters that fall apart in movement. 🟡 Hard limits (clip length, resolution caps) of the Aleph class are not reliably documented — test with a short clip before planning a sequence around it. Complements the VFX hybrid path (production-pipeline ch. 9) with the inverse direction: live footage as a motion scaffold for a style.

## 6. Style vocabularies (opening-line packages)
- **Pixar/stylized 3D:** whimsical Pixar-style stylized 3D animation, rounded simplified forms, exaggerated character proportions, oversized expressive eyes, soft global illumination, subsurface-scattering skin, rim light on shoulders + soft face light, warm three-point lighting, family-film cinematic composition, believable-not-photoreal. Pixar look = **80% rendering quality, 20% character design** — the rendering cues carry, not the word. Grade: warm-cool contrast (classic teal shadows/warm highlights) — projects with their own color script replace the concrete colors; the warm-cool principle stays. Proven viral format: emotional close-up, big eyes, warm light. ⚠️ For GPT Image 2, deliver this vocabulary via the 4-section structure (§2), never as a front-loaded keyword chain — the avalanche opener is disproven [PP]. First frame locks style, last frame locks the motion target; one variation axis per run. ⚠️ Render-engine tokens ("Unreal Engine 5", "Octane") risk the game-render look; "Pixar Renderman quality" is the safer token. IP line: the glossy 3D style is free, and film titles work as aesthetic lineage anchors ("consistent with …", same class as director names, used in the proven 4-section structure [PP]); Pixar CHARACTERS remain protected IP (documented C&D one day after a model launch) — never reference or reproduce named characters. Full look definition: `pixar-look.md`.
- **Uncanny valley rule:** ~70% realism is the discomfort zone — either clearly stylized OR fully photoreal, never the middle. Environments: chunkier/rounder forms, simplified geometry, soft shadows without photographic edges.
- **Hanna-Barbera/limited TV animation:** 1960s Hanna-Barbera-style limited television animation, thick tapered black outlines + thin interior lines, flat color fills, desaturated/pastel palette, minimal shading, geometric simplified shapes, strong silhouettes, static hand-painted painterly background, economical movement (bodies mostly static, expression via face/small gestures), tableau camera.
- **Rubber hose (1920s/30s):** 1930s rubber-hose animation, bendy tube limbs, pie-cut eyes, white gloves, ink-black flat fills, bouncy synchronized motion, film grain/dust, off-white paper background.
- **Anime (modern):** anime style, cel shading, consistent linework, speed lines + anime motion blur, held poses before action beats; high-action = model sweet spot.
- **Retro-90s anime:** retro 90s anime screenshot, VHS film grain, hand-painted background textures, high-contrast white highlights on hair and eyes, muted color palette, 4:3.
- **Monochrome manga:** strictly black-and-white ink, no grayscale, dense screen-tone dot patterns for shadows, bold ink strokes, exaggerated speed lines, dramatic angles, manga panel aesthetic.
- **Chibi:** super-deformed proportions (head ≈ body), huge sparkling eyes, tiny limbs, bright cel shading, kawaii sticker aesthetic.
- **Ghibli-like / painterly anime:** hand-painted cel animation, soft watercolor/gouache background with visible brushwork, warm golden palette (amber, sage, dusty rose, warm cream — even night scenes warm lamplit, not cold blue), dappled afternoon light, lush botanical background detail, gentle pastoral mood. Strongest single words per community tests: "watercolor" and "cel animation"; "golden hour" as the strongest lighting lever. Actively suppress (negative block): photorealistic, 3D render, CGI, sharp edges, neon/high-contrast — photorealism tokens (4K, Unreal) fight the aesthetic directly. Over-describe the background, under-describe the subject (Ghibli lives in the environment).
- **Claymation/stop-motion (Aardman-like):** plasticine/polymer clay, visible fingerprint and thumbprint texture, hand-sculpted imperfections, slightly lopsided handmade shapes, matte clay surface, button eyes, miniature diorama set (felt grass, paper trees), tilt-shift/shallow DoF, warm soft studio lighting, 12 fps stop-motion stutter (video). Core principle: **imperfection descriptors ARE the style** — without "handmade/slight imperfections" the model renders too polished and the look tips into smooth 3D. Reuse the vocabulary identically across all scenes.
- **Flat 2D TV cartoon / paper cutout (describe generically — named shows are IP):** flat 2D cartoon, thick black outlines (bold 2px vector linework), flat color fills — no gradients, minimal cel-shading, flat ambient light without realistic shadows, simplified geometric shapes, pastel/bright palette; cutout variant adds: paper-cutout aesthetic, crisp cutout edges, round heads, simple dot eyes, paper texture.
- **Saturday-morning cartoon:** classic hand-drawn cartoon, bold shapes, thick outlines, bright primary palette, clean line, minimal background detail.

🟢 **Meta rule for all vocabularies:** the style anchor is a COMPACT package (4–8 specific tokens) reused verbatim across all prompts — "more style words = more style soup = more drift": a 30-word style line gets averaged into unpredictability. One sub-style per prompt; style mixes (Ghibli + cyberpunk) cause drift — mixed styles only as explicit per-element declarations (§5).

## 6b. Non-animation styles: footage authenticity, era looks, technical optics
### A. Footage authenticity (found-footage family)
🟢 **Four-tell rule:** a clip only reads as "genuinely recorded" when FOUR things are named: (1) the recording format (camcorder/VHS shoulder cam, dashcam, bodycam, CCTV, livestream/webcam), (2) a burned-in tell (timecode lower right, REC icon, battery red-light — "battery red-light reflected in breath"), (3) exactly ONE in-frame light source (headlamp, headlights, fluorescent strip), (4) a camera that does NOT behave cinematically (fixed mount or panicked handheld). Name the artifacts in language instead of hoping for filters — "scanline softness on a 1990s shoulder-camcorder, dust in a headlamp beam."
🟢 **Restraint rule:** the scene must stay readable under the damage — "build the fear first, then add only enough tracking drift, timecode, and tape wear to make the clip feel recovered instead of overprocessed."
🟡 Sub-vocabularies: **VHS** — tape grain, tracking errors, scanlines, static bursts, chromatic drift, faded colors, timestamp overlay. **CCTV** — fixed high angle, b/w or IR green-gray, muted tones, noisy shadows, edge blur, burned-in timestamp, corner brackets. **CRT monitor feed** — cool blue tint, phosphor glow, screen curvature, analog noise. **Bodycam/dashcam** — chest-height ultra-wide, motion blur on head/vehicle movement, close distorted audio.
🟢 **Anti-slop bonus:** degraded-media looks have built-in fault tolerance — grain, blur, and compression mask model artifacts (same principle as the UGC path). A footage format is a legitimate rescue style for risk shots.

### B. Era & film-stock looks (prompt layer of the era selector)
🟢 **Named film stocks are precision tools** — models know their signatures: Kodak Portra 400 (soft natural skin, faded blacks), Kodachrome 64 (rich, warm), CineStill 800T (tungsten + halation), Fuji Pro 400H (greenish shadows), Kodak Tri-X (b/w, hard grain), Fujifilm Velvia (hyper-saturated landscape). "Scanned film negative" adds realistic imperfections.
🟡 Look building blocks: **16mm** — blooming highlights, heavy grain, jitter texture, vignette, "avoiding any digital sharpness"; **Super 8/8mm home movie** — warm, flickering, family nostalgia; **newsreel** — 16mm b/w, scratches, slightly sped motion; **Polaroid/Instax** — creamy highlights, chemical streaks, white frame border, pastel fade; **1990s disposable** — harsh direct flash, red-eye, date stamp, washed colors; **daguerreotype/Victorian** — sepia-metallic, oval vignette, long-exposure stillness; plus silent-film 1920s, Technicolor 1950s, French New Wave, Y2K digicam flash as established shorthand.
🟢 **Vintage vs. retro — decide explicitly:** vintage = authentically "shot back then" (period-correct fashion, set, imperfections included); retro = modern subjects in old capture technique. The model needs the decision or it mixes. Always couple an era look with period-correct production design.
🟡 **Director signatures as composition shortcuts** (legally safe — style, not work): "Wes Anderson style" = perfectly symmetrical central composition + flat pastel palette + deadpan storybook framing; works cross-model as shorthand for a whole rule set. Similarly usable: noir 1940s (hard shadows, venetian-blind light), European arthouse (muted, soft, emotional).

### C. Technical optics & special cameras
🟡 Prompt vocabulary for optics beyond preset lenses: **FPV drone** — rapid low-altitude weaving, motion blur at frame edges, lens flare through obstacles (opposite of gimbal drone: "flat, stable, horizon-level" is the anti-FPV look); **action cam/GoPro** — ultra-wide FOV, horizon-locked, hyper-stabilized, helmet/chest mount; **thermal** — heat-signature rendering, white-hot/black-hot, temperature gradients instead of texture; **night vision** — IR green, glowing highlights, noisy shadows, pupil glow; **tilt-shift miniature** — extreme selective focus plane turns real scenes into model worlds. Optics choice = genre signal (military, survival, documentary).

## 7. Reference integration protocol (for prompt-writing agents)
🟢 **Style reverse-engineering via LLM [P17]:** to build a project's reusable style block, feed the look-defining references to the LLM FIRST and have it analyze and write out the style (materials, skin/surface treatment, rendering signals) as a base prompt structure — then reuse that structure across all generations, refining per asset with further references until the cast and locations sit. Beats hand-writing style prose from memory.
🟢 **Rule 0 — a reference only exists if the prompt addresses it.** "Attach an image in the UI" without a prompt role = undefined behavior. Every prompt with references contains a REFERENCE block. Motto: "Use text to direct. Use images to preserve appearance."
🟢 **Rule 1** — one line per reference: tag/name + "controls only [exactly one job]" + "Do not copy [concrete non-transfers]". No tag without a job, no job without a tag.
🟢 **Rule 2** — clarify platform syntax BEFORE writing: @image numbers (upload order!), @element_name (Higgsfield), or Mode B (describe the visible feature). Tags are not portable.
🟢 **Rule 3** — every prompt deliverable ends with an **attachment checklist in upload order** ("Attach: 1. @image1 = sheet X, 2. @image2 = style still Y …").
🟢 **Rule 4** — style references get the same role discipline: "@image2 controls only the rendering style. Do not copy its subject or composition."
🟢 **Diagnosis:** output comes back photoreal despite a style word → the style was a word, not an anchor. Fix order: (1) look-carrying reference/start frame, (2) upgrade opening line to the vocabulary package (+ negation anchor on GPT Image 2), (3) style into the locks. Never just sprinkle the style word a third time.

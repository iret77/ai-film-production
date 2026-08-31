# Image-Model Logic: How Generators Read Prompts — Position, Scale, Count, Negation (ch. 24)

Why this file exists: the agent writing prompts is a text-to-text LLM — trained on argumentative text, writing for readers who reason. The model receiving the prompt is a **caption-conditioned generator** — trained on image-description pairs, where every token is evidence for visible content. These are different machines, and prompts written in reader-logic (rhetoric, emphasis, redundancy, numeric precision, meta commentary) fail on a generator. This chapter is (a) the mechanism, (b) a binding writing contract, (c) exact recipes for the recurring control problems. Confidence labels as usual; deep sources cited inline (papers/vendor docs, researched 2026-08).

## 24a. What a prompt actually is to an image model

🟢 **Two model families, one shared conditioning problem.** (1) Latent diffusion/flow transformers (FLUX, SD3.5, Seedream DiT, Imagen): text steers iterative denoising of a latent grid via attention. (2) Autoregressive/unified multimodal (GPT Image lineage — officially autoregressive per OpenAI's system card; Nano Banana = Gemini-based, AR token stream + decoder): the LLM *is* the conditioning, and since 2026 these run an explicit planning phase before rendering (gpt-image-2 "agentic reasoning", NB Pro thinking phase + low-res draft). AR models therefore follow zone/grid/instruction language far better — but **no family executes numeric geometry** (SpatialGenEval ICLR 2026, 21 SOTA models: spatial precision is the universal bottleneck).

🟢 **A prompt is a scene description, not a spec.** Training captions assert what IS in an image. The model has no execution engine — it renders the statistically plausible scene your tokens describe. Consequences: (a) unmentioned = improvised; (b) metric layout language ("1% of image width", pixels, percent, exact margins) has **no learned mapping** — captions never contain it; an entire research line (GLIGEN, ControlNet, layout-to-image) exists precisely because coordinates must be injected through separate trained channels, not prose; (c) size and position are INFERRED from object class, scene context, and relations.

🟢 **In diffusion models, the noise seed largely pre-decides layout.** Measured: specific patches in the initial noise determine where objects appear; text mostly decides *which* objects occupy pre-set locations (arXiv 2510.11117: count compliance jumps 3%→96% by editing the noise, not the text). Practical: **rerolling the seed is a legitimate spatial-control lever; rewording against a hostile seed is not.** AR models don't share this mechanism — another reason they layout better.

🟢 **Detail budget:** a small object spans few latent cells/tokens and physically cannot carry described fine structure (SOEBench: cross-attention can't align text tokens with few-cell objects; garbled small faces are the canonical symptom). 🟡 **Detail demand inflates size [PP]:** demanding visible detail (facets, engraving) on a small object pushes the model to enlarge it — practitioner canon ("beautiful detailed face" turns compositions into close-ups) + our production evidence; mechanism plausible, not formally measured. Fix: describe detail AS IT READS at target size, or go through a mask (24g).

🟢 **First-mention bias is real and measurable:** the first-named object is rendered far more reliably, and earlier tokens win conflicts (VISOR; ComCO; M3T2IBench). Token order is a control channel: must-have object first.

🟢 **Most "spatial failure" is omission, not misplacement:** when both objects actually render, the stated relation is right much more often (VISOR: ~60% vs ~19%). Before blaming position wording, check whether the second object exists at all — the fix is then presence (first position, simpler scene), not placement language.

## 24b. The generator contract — binding for every prompt-writing agent

Before ANY image/video prompt leaves the agent, it conforms to all seven. This is the T2T→generator translation layer; violating it produces exactly the failures ch. 24c–g repair.

1. **Describe, don't argue.** No rhetoric, no meta commentary ("this is how you set its size"), no addressing the model, no emphasis-by-repetition. Every token must pull toward visible content; a token that doesn't is noise at best, new content at worst.
2. **Zero contradictions — and nobody will warn you.** Generators do not detect conflicts; there is no error, only blending in embedding space or a silent win by the training-entrenched concept (CVPR 2026, arXiv 2506.01929). Lint every prompt for: size vs. detail demand, two styles/materials on one surface, positive claim vs. negation of the same attribute, mood vs. stated lighting. Resolve BEFORE generating — the agent is the only contradiction detector in the pipeline.
3. **The positive statement carries everything.** Negation is a channel decision per model class (24f), never the load-bearing description.
4. **One instruction per axis.** Compliance degrades near-linearly with constraint count (ConceptMix: <25% at 3 bound concepts; M3T2IBench: linear decline with relations; T2ICountBench: prompt decomposition *reduced* counting accuracy 42%→26%). Stacked restatements of one goal dilute it — redundancy is not emphasis, it is interference.
5. **Numbers only into numeric channels.** FOV/km/h/Kelvin in video blocks (ch. 12), coordinates in Seedream's annotation mode, size via mask — never metric values in free prose.
6. **Order by importance.** First-mention bias (24a): the must-have object opens the scene description.
7. **Three failed runs on one axis = wrong channel, not wrong words** (SKILL rule 14, "prompt first, model last"). Escalate to a different control channel — reference image, sketch, mask, seed reroll, other model — instead of a fourth vocabulary variant.

## 24c. Position control — the ladder

Benchmark reality first: coarse position words (left/right/top/bottom) hit ~75% on AR/LLM-conditioned models (GPT Image, Qwen-class) but only ~22–47% on FLUX.1-dev/SD3.5/Seedream 3 (GenEval position); *precise* placement (thirds, quadrants, margins) sits near random for ALL models (SpatialGenEval: spatial comparison/proximity 25–34% vs 20% chance). Climb only as high as the shot requires:

1. **Model choice:** layout-critical stills go to the AR/reasoning class (GPT Image, Nano Banana Pro) — 2–3× the position compliance of prose-conditioned diffusion.
2. **Zone language, layout first** (official across vendors): "logo top-right", "subject centered with negative space on left", "positioned in the bottom-right of the frame". Declare empty zones explicitly ("significant negative space left for text") — declared emptiness holds, implied emptiness doesn't. Canvas/grid/panels before subjects (style-control §2 layout-before-subject).
3. **Named scene geometry, never coordinates:** place relative to what exists — "just under the painting, in the corner", "at the lip of the crevice". This is the placement twin of relational sizing: the model thinks in object relations, so address it in them.
4. **Layout sketch as reference** (official OpenAI/Seedream pattern): a crude blocked sketch + "Preserve the exact layout, proportions, and perspective. Do not add new elements." Right tool whenever WHERE matters more than WHAT — the model keeps geometry and invents surface. (Complements the 3D-blockout path, ch. 8.)
5. **Structure/annotation channels:** FLUX Depth/Canny freeze composition entirely (content/style changes, layout locked); Seedream 5.0 Pro accepts boxes, points, arrows, coordinates, and sketches as edit targets — the ONE place numbers are legitimate, because it is a trained channel.
6. **Pixel-exact = composite in post:** generate background + element layers (Seedream: up to 20 transparent PNG layers) or cut out and place manually. No prompt reaches pixel precision; stop trying at this rung.

Diffusion-only bonus lever: **reroll the seed** — layout is partly pre-decided by noise (24a); a new seed is a new layout lottery, cheaper than prompt surgery.

## 24d. Scale control — the ladder

1. **The object word IS the size spec.** "Pebble" vs. "rock" vs. "boulder" moves size more reliably than any modifier — canonical size priors are the model's native size system (probing-verified: LMs encode relative object-size knowledge). Pick the noun whose canonical size matches the target.
2. **Shot type and lens are the official size dial** (OpenAI + Google + Seedream guides converge): extreme close-up / medium / wide sets subject-in-frame scale; "macro lens" renders tiny things detail-rich, "wide-angle" renders vast scale. For a small prop in a big frame: wide shot vocabulary, not smallness adjectives.
3. **ONE relational anchor** to an in-frame object of known size ("no larger than the pebbles beside it") — style-control §2 rule; one anchor, never a stack.
4. **Don't fight canonical size.** Counter-canonical scaling ("a fly bigger than an elephant") succeeds ~10–30% even with optimized prompts — if the concept requires it, build it via compositing or forced-perspective staging, not insistence.
5. **Hard size constraint → change channel:** mask drawn AT the intended object size (the mask is the size control — but check mask strictness per platform, 24g), Seedream sketch-at-size / bounding box, or layered compositing. For a small object that also needs detail: crop-zoom-inpaint-paste-back (24g).
6. **Compositing/insertion:** demand "matching lighting, perspective, scale, and shadows" verbatim (official OpenAI compositing recipe) + the ground-contact positive lock (style-control §2).

Never numeric size in prose — no vendor guide uses it, no benchmark shows it working, and it displaces tokens that could carry a working lever.

## 24e. Count & multi-object

🟢 Current-gen reliability: counts ≤4 ≈ 85–90% (GenEval); 6–10 → 10–30%; ≥11 → <10% (T2ICountBench). Quantifiers ("a few", "several") and zero ("no X") score WORST of all numeric language — pick an exact small number or control by construction.
🟢 **Do not decompose counts in the prompt** ("two on the left, three on the right") — measured to *reduce* accuracy (42%→26%). One plain count, or build the number via multi-panel/grid generation, scaffolded adds (style-control §3), or the crowd-sheet path (production-pipeline ch. 3).
🟢 Scene complexity roughly halves counting accuracy — count-critical shots get simple backgrounds.
🟢 **Attribute binding:** color/material leakage between objects is systematic (GenEval binding 0.45–0.8). Prompt-side mitigation: unambiguous adjective-directly-before-noun syntax, one attribute set per object in its own short clause, distinctive objects; beyond ~3 attributed objects, scaffold (generate, lock, add) instead of describing everything at once.

## 24f. Negation & exclusion — a channel decision, not a wording choice

🟢 **Mechanism:** captions describe presence, essentially never absence — negation is out-of-distribution for caption-trained conditioning (NegBench, CVPR 2025: CLIP-class encoders ≈3% negation accuracy, chance level). In-prompt "without X" on diffusion models makes X MORE likely — measured 75.5% inversion ("pink elephant", CVPRW 2024). An LLM text encoder does NOT fix this: FLUX/SD3.5 (T5-conditioned) still fail in-prompt negation. The real divide: **caption-trained conditioning (any encoder) vs. genuinely instruction-tuned AR models.**
🟢 **The channel table:**

| Model class | Exclusion channel that works |
|---|---|
| Diffusion stills (FLUX, SD3.5, Midjourney, Imagen) | Dedicated negative field / `--no` only — bare atomic nouns ("people", "wall"), one concept per entry (compounds get split and over-exclude), NEVER "don't/no X" in the prompt body |
| AR/reasoning stills (GPT Image, Nano Banana) | Short in-prompt exclusions are vendor-endorsed ("no watermark, no extra text") and legitimate — but the positive description still carries the composition; Google's own rule: positive framing first ("empty street", not "no cars") |
| Video models | Ch. 14 negative rule governs (it's consistent with this research): Seedance names unwanted elements in-prompt (official: "omission is not a reliable negative instruction"); Veo/Kling use their negative fields with bare keywords, most critical first; models without a dedicated negative field → rewrite prohibitions as the desired state ("the boy waves his hands", not "can't stay still") |

🟢 **Best in-prompt substitute for any negation: a positive replacement occupying the same slot** — name what fills the space instead of banning what shouldn't (+23.5pp measured). "Matte powdery surface" beats "no gloss"; "empty street" beats "no cars"; both together (style-control §2 material rule) is the belt-and-suspenders form for critical surfaces on AR models.
🟢 **Leakage is a training-distribution problem, not a phrasing problem:** concepts overrepresented in training data (Veo's subtitle habit is the canonical case) leak through EVERY channel. Plan the fallback (reroll, crop, post) instead of stacking more prohibitions — stacked prohibitions are instruction dilution (24b.4) plus pink-elephant risk.
🟡 The style repulsion anchor ("NOT photorealistic…", style-control §2) remains legitimate on the AR/reasoning class — vendor-consistent but never formally benchmarked; keep the positive style description primary and the anchor as its closer.

## 24g. Edits & locality

🟢 **Instruction edits regenerate the whole image** — unedited content is *reconstructed*, never copied, so drift is the native behavior, not a malfunction (BFL engineered Kontext specifically to minimize it). Measured (EdiVal, 16 models): GPT-Image is top-tier at FOLLOWING instructions but near-bottom at PRESERVING content — "GPT Image repaints everything" is benchmarked fact, not folklore; Nano Banana and FLUX Kontext preserve best; Seedream 4+ has the best balance.
🟢 **Multi-turn collapse:** by turn 3, instruction-following roughly halves for every model tested; research puts hard degradation at ~5 chained edits (VAE re-encode noise) — our stricter max-3 rule (style-control §2) stands. Branch from the best intermediate or restart from the original with ONE combined instruction; never chain serially toward a deadline.
🟢 **The preserve list is official practice, not a guarantee:** "change only X, keep everything else exactly the same" + repeating the preserve list on EVERY iteration is what OpenAI/Google/BFL all prescribe — necessary, but unmeasured; model choice moves locality more than phrasing.
🟢 **Mask strictness differs per platform — know which kind you hold:**

| Mask type | Platforms | Behavior |
|---|---|---|
| **Hard** (algorithmic clamp: outside-mask content mathematically preserved) | FLUX Fill (binary b/w mask), Imagen/Vertex inpaint (`maskDilation` ~0.01) | Content cannot escape; the mask truly defines region AND size |
| **Soft** (guidance only) | GPT Image `mask` param — official: "entirely prompt-based… may not follow its exact shape"; may repaint globally | Always pair with the full prompt-level preserve list; expect overflow |
| **No pixel mask** | Nano Banana API (semantic masking by prompt only); Seedream (annotation channel: boxes/arrows/coordinates/sketch instead); Higgsfield mask-brush UI over NB Pro (rough mask OK — expand slightly when replacing, widen + regenerate when an edit misses) | Use the platform's native channel; don't assume mask semantics that aren't there |

🟢 **Inserting a small NEW object (the hard case):** inpainting fills the whole masked region → draw the mask AT the intended object size, slightly generous at the edges. Small target that needs detail: **crop-zoom-inpaint-paste-back** (crop around an enlarged edit area, inpaint at full resolution, scale back — the standard fix for the detail-budget problem, 24a). Anchor position to named scene geometry, apply the ground-contact positive lock + "cast a soft shadow, match original shadows" (style-control §2).

## 24h. Quick reference — problem → first move → hard fix

| Problem | First move (prompt-level) | Hard fix (channel change) |
|---|---|---|
| Place an element | Zone language early + named scene geometry | Layout sketch → structure map/annotation → composite layers |
| Set an element's size | Object-class word + shot type/lens + ONE relational anchor | Mask drawn at size (hard-mask platform) / sketch-at-size / composite |
| Small object with detail | Detail described at target scale | Crop-zoom-inpaint-paste-back |
| Exact count | One plain number ≤4–5, simple background | Multi-panel / scaffolded adds / crowd sheet |
| Exclude something | Positive replacement in the same slot | Negative field (diffusion) / short exclusion (AR) / accept-and-post fallback |
| Local edit, keep the rest | "Change only X" + repeated preserve list, ≤3 iterations | Hard mask (FLUX Fill/Imagen) or restart from original with combined instruction |
| Keep composition, change content | Reference + role line ("layout and light only") | FLUX Depth/Canny structure lock |
| Layout fights you twice | Reroll seed (diffusion) or switch to AR-class model | Any of the above — but change CHANNEL, not vocabulary (24b.7) |

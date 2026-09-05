# Current UI & User-Workflow Reference — Higgsfield, fal.ai, Runway, OpenArt, Arcads, ChatGPT

**Reference ID:** `UI-WF@2026-09-04`  
**Research snapshot:** 31 August 2026 · **re-verified against the primary sources:** 4 September 2026 (all `*@2026-09-04` keys below; only Arcads web keeps the 2026-08-31 snapshot)  
**Purpose:** give a production agent a conservative, evidence-based map of what a user can actually select and do in the current web products—and, crucially, **which screen owns each setting**. This is a *platform/UI* reference, not a model-quality ranking or a prompt-writing guide.  
**Scope:** Higgsfield, fal.ai, Runway, OpenArt, Arcads, and ChatGPT image generation—the platforms explicitly requested for this project. “Etc.” is not an authorization to invent a capability for another vendor or model; inspect that vendor's current UI and primary documentation first.

## Contents (jump by heading text; no line numbers)
- §0 Governance — read for EVERY platform task: Version & evidence record (RECEIPT line, ledger keys `HF-CS4@…`, `HF-WEB@…`, `HF-MCP@…`, `HF-BRIDGE-MCP@…`, `FAL-WEB@…`, `RW-WEB@…`, `OA-WEB@…`, `AR-WEB@…`, `*-MCP@…`) · Operating contract + Non-negotiable verification gate (incl. receipt states) · Control-plane map: never transplant a setting · Alternative access paths: web UI / MCP / ChatGPT (route declaration, MCP non-parity rules, GPT Image 2, MCP execution gate)
- §1 Higgsfield — navigation/object model · **Cinema Studio 4.0: what a user sets before generation** (settings table) · **reliable user workflow** (opens with the 🟡 "Do the controls bite?" caveat) · What else the current UI can do (Video, Seedance 2.5 Edit, Blender add-on, Relight, Layers, Upscale, Audio/Lipsync, Supercomputer) · **Seedance 2.5 mode id ↔ UI label** · Output configuration · learning sources
- §2 fal.ai — not an editing studio · browser surfaces · Playground fields · exploration→integration · API workflow · correct/incorrect advice · learning sources
- §3 Runway — surface selection · Tool Mode (Gen-4 Image, Gen-4.5 video, Export) · Apps · Edit Studio/Aleph 2.0 · Agent & Workflows · long-form rule · learning sources
- §4 OpenArt — navigation/persistent assets · Create Image · Video routes (Create Video form, Smart Shot/edit/extensions) · Director · Characters/Worlds/Brand · platform facts · learning sources
- §5 Arcads — purpose · which form owns which choice · safe ad loop · agent/MCP boundary · learning sources
- §6 Cross-platform routing — choose by request · continuity by platform · safe production loop
- §7 Secondary-source audit · §8 Maintenance protocol

Reading rule: §0 plus the § of the platform at hand (plus §6 when choosing between platforms) satisfies "read fully" in SKILL.md's routing table for this file.

## Version & evidence record — mandatory for every platform claim

Every saved capability, workflow, setting, limit, or MCP instruction must carry (explicitly or by inheritance from the nearest **Version scope**) the RECEIPT line (SKILL.md Scope & version — KEY grammar there); its core values are:

`platform → access route → account/workspace (if known) → surface/tool → model + mode id ("UI label") → vendor version or unversioned-UI snapshot → source URL · state (live-checked YYYY-MM-DD | from reference KEY)`

Do **not** manufacture a UI version where the provider publishes none. Record it as `unversioned web UI @ YYYY-MM-DD` plus the exact URL and selected model/mode. For a model/API, record the exact endpoint/model ID and mode. For MCP, record the **server URL**, documented tool/schema set, authentication/account/workspace context, and checked date; a server URL alone is not a version.

The short keys below are internal reference identifiers, not vendor version names. A statement inherits its row until a more specific Version scope says otherwise. Any UI/model/MCP fact that cannot be assigned one of these scopes is **unverified**, not “current.”

| Reference key(s) | Exact scope/version basis | Evidence and refresh trigger |
|---|---|---|
| `HF-CS4@2026-09-04`; `HF-WEB@2026-09-04` | `HF-CS4` = Higgsfield **Cinema Studio 4.0**. `HF-WEB` = other unversioned Higgsfield web tools (Video, Image, Audio, Edit, Upscale, etc.) captured at the check date. | [4.0 guide, published 12 Aug 2026, modified 31 Aug 2026](https://higgsfield.ai/blog/cinema-studio-4-0), [live shell](https://higgsfield.ai/generate/video) and [changelog](https://www.higgsfield.company/creator-hub/changelog) (newest entry 1 Sep 2026, Genjutsu) — all re-read 4 Sep 2026. Recheck after any Cinema release/changelog entry or tool-page change. |
| `HF-MCP@2026-09-04` | Higgsfield MCP at `https://mcp.higgsfield.ai/mcp`; provider guide published 1 Aug 2026, last updated 1 Sep 2026; a Higgsfield CLI (github higgsfield-ai/cli) exists for Claude Code/Codex users (MCP & CLI page). | [MCP differences guide](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp). Recheck its exposed operations and billing before use. |
| `HF-BRIDGE-MCP@2026-09-04` | Higgsfield Blender **Bridge** MCP at `https://bridge.higgsfield.ai/mcp`, paired with the Blender add-on (higgsfield.ai/plugins/blender); unversioned, add-on page re-read 2026-09-04 [P50] (same URL also serves the After Effects plugin connector, changelog 13 Jul 2026). Tool/schema list NOT documented publicly — read it in the connected session (MCP execution gate step 2). | [Add-on page](https://higgsfield.ai/plugins/blender) · sources.md P50. Recheck exposed tools, credit price on Generate and plan-level exclusions before use. |
| `FAL-WEB@2026-09-04`; `FAL-MCP@2026-09-04` | fal Playground/Sandbox are unversioned schema-driven UIs; an exact **endpoint ID + current schema** is the effective version. MCP is `https://mcp.fal.ai/mcp` (Streamable HTTP, `Authorization: Bearer <FAL key>`, 11 tools as of 2026-09-04). | [Playground UI mapping](https://fal.ai/docs/documentation/development/handle-inputs-and-outputs) and [MCP tool reference](https://fal.ai/docs/documentation/setting-up/mcp). Re-fetch the selected endpoint schema on every paid run. |
| `RW-WEB@2026-09-04`; `RW-MCP@2026-09-04` | Runway’s web suite is unversioned; model/tool names (e.g. Gen-4.5, Act-Two, Aleph 2.0) are the specific version identifiers. MCP is `https://mcp.runwayml.com/mcp` (Streamable HTTP only; Explore Mode unsupported; agent-selectable models listed 2026-09-04: Seedance 2.0, Kling, Gen-4.5, Veo, GPT image 2, Nano Banana Pro). | [current Gen-4.5 guide](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5) and [MCP guide](https://help.runwayml.com/hc/en-us/articles/51931843164691-Connecting-to-Runway-MCP). Recheck the active model/tool and plan. |
| `OA-WEB@2026-09-04`; `OA-MCP@2026-09-04` | OpenArt Suite forms are unversioned and model/mode-selected; MCP is `https://mcp.openart.ai/mcp` (Character and Smart Shot still "on the roadmap" for MCP as of 2026-09-04). | [current Video form](https://openart.ai/suite/create-video) and [MCP page](https://openart.ai/mcp/). Recheck selected workspace, current model form and MCP tool availability. |
| `AR-WEB@2026-08-31`; `AR-MCP@2026-06-26` | Arcads Studio/Mark/Workflow web surfaces are unversioned. Its current Getting Started guide is dated 2 Jul 2026; MCP guide is dated 26 Jun 2026 at `https://mcp.arcads.ai`. | [Getting Started](https://intercom.help/arcads/en/articles/14531683-getting-started-with-arcads) · [MCP guide](https://intercom.help/arcads/en/articles/15655699-arcads-mcp). Recheck exposed MCP tools before relying on Studio parity. |
| `CGPT-IMG@gpt-image-2@2026-09-04`; `OPENAI-IMG-API@gpt-image-2@2026-09-04` | ChatGPT web is an unversioned chat surface; the built-in image model identifier is `gpt-image-2` (multi-reference attachments, area-select edits and a Canvas view documented 2026-09-04). The API is a separate surface with the same exact model ID (`gpt-image-2`, plus `gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini`) or the Responses image-generation tool; transparent backgrounds are in preview for `gpt-image-2`. | [ChatGPT image-generation guide](https://learn.chatgpt.com/docs/image-generation) · [OpenAI API guide](https://developers.openai.com/api/docs/guides/image-generation). Recheck plan/workspace availability and API model docs separately. |

**Required wording in agent output:** “Verified for `KEY` — [surface] / [model + mode] / [access route], checked YYYY-MM-DD.” Without a live read this session write instead: “From reference `KEY` — [surface] / [model + mode] / [access route], not live-checked this session.” Never write the first form for a check you did not perform. If a user sees a different label/dropdown/tool list, the live UI supersedes this reference and the agent mints a new project KEY with today's check date per the SKILL.md KEY grammar and records its RECEIPT line in bible section B1b. The "Verified for …" sentence is the user-facing SHORT form; the RECEIPT line is the stored form.

## Operating contract for an agent

These products do not expose the same kind of control. Treat the following distinction as a hard routing rule.

| Platform | What the user is actually using | Best interpretation for an agent |
|---|---|---|
| **Higgsfield** | A film-production workspace plus separate image/video/edit tools. Cinema Studio 4.0 exposes a cinematic control surface around selectable models. | Route a scene/project to Cinema Studio; put film grammar into its selectors and the story/action into the prompt. |
| **fal.ai** | A model/API marketplace. Its browser UI is a test bench whose form is generated from each endpoint’s schema. | Route to a named model endpoint and inspect its exact schema. Do **not** describe fal as a film editor or assume a common set of controls. |
| **Runway** | A creative suite with free-form Tool Mode, task-specific Apps, a conversational Agent, a node editor (Workflows), and a lightweight timeline. | Choose the surface first: single asset, a named task, conversational production, or reusable automation. |
| **OpenArt** | An aggregated creative suite: single-shot image/video tools, saved Characters/Worlds/Brand Kit, structured tools, and the chat-based Director. | Choose between a shot-level tool and Director; retain recurring assets in the platform library rather than re-describing them every time. |
| **Arcads** | A performance-marketing/UGC production platform: product assets, image/video models, AI Actors, scripts/voices, localization, an ad agent, and reusable node workflows. | Choose the ad-production surface first: hands-on Studio, a Talking/Animated Actor, B-roll, Translate, Mark Agent, or a Workflow. It is not a general cinematic-film studio. |
| **ChatGPT** | A conversational image-generation surface using **`gpt-image-2`**, plus an optional host for connected third-party MCP apps. | Use it for conversational still creation/editing and reference-guided iteration. ChatGPT-native image generation is not a video generator and does not inherit an MCP provider’s web UI. |

### Non-negotiable verification gate

Before telling a user that an option is available—or spending credits—an agent must do all of the following.

1. Identify **platform + surface + selected model + mode**. “Use Seedance” is insufficient: Seedance in an OpenArt video tool, in fal’s Playground, and inside Higgsfield are different UIs with different inputs and price/resolution choices.
2. Read the visible model/settings panel and plan entitlement. Aggregators add and remove models, formats, reference counts, durations, and price tiers frequently.
3. Read the upload hint in the active UI. It is the source of truth for accepted format, length, resolution, reference count, and file size.
4. Read the displayed credit/cost estimate immediately before Generate/Run. Do not calculate cost from old tutorials.
5. If a capability is not visible in the selected mode or current official docs, phrase it as a question for the user (“does your dropdown show …?”), not a proposed workflow.
6. Do not transfer an option from an older version or a different product. Examples: Runway Gen-3 is retired; OpenArt Workflows were sunset; Higgsfield Cinema Studio 3.5 restrictions do not define Cinema Studio 4.0.
7. **Receipt states — what to write when you cannot look (SKILL rule 16).** A receipt is in exactly one of two states; always name it. `live-checked <date>` — you read the live form / MCP schema in THIS session, or the user pasted or described the live form in this session; only in this state may a new checked date, UI-snapshot date, credit price, or account/workspace name appear. `from reference <KEY>` — no live read this session: cite the newest stored receipt (the bible's section B1b row, else the matching ledger key above) with ITS check date copied verbatim; leave account/workspace and cost empty. A `from reference` slate is a complete, valid deliverable; writing a `live-checked` date for a check you did not perform is fabrication. Ask the user for a live value only when the route itself is in doubt — never as a gate before drafting.

This document deliberately distinguishes **verified current controls** from **model-dependent controls**. A model-dependent field is not a promise that every dropdown selection supports it.

---

## Control-plane map: never transplant a setting

A product can place the same underlying model in more than one surface. The name of a model alone is therefore never an instruction. The agent must address every proposal as:

> **platform → workspace/tool → selected model → selected mode → setting**

For example, “set `Lens: Vintage Anamorphic` in **Higgsfield → Cinema Studio 4.0**” is valid. “use a vintage-anamorphic Lens setting with **Seedance**” is not: it falsely turns a Cinema Studio control into a Seedance parameter. If the user has selected Seedance inside Cinema Studio, describe it as a **Cinema Studio control applied by that surface**, not as a native Seedance field.

| Control plane | Verified user-selectable scope | What must not be inferred or mixed in | Version scope to cite |
|---|---|---|---|
| **Higgsfield → Cinema Studio 4.0** | Film-direction panels: Genre, Era, Tempo, named-character Emotion Wheel, Colour Palette, Lighting, Camera type, Lens, Aperture, Camera movement, references and project/Element context. | These are **Cinema Studio controls**. Do not call them standalone Seedance, Kling, Veo, FLUX, or fal parameters. | `HF-CS4@2026-09-04 / Cinema Studio 4.0` |
| **Higgsfield → Video → Seedance 2.5** | A named video-model surface: prompt, optional source/reference media, and the currently exposed Seedance mode controls. Higgsfield documents 50 multimodal references (ByteDance class split 30 image / 10 video / 10 audio — video-prompting ch. 14b), native audio, R2V motion guidance (= `omni_reference`, mode table in §1), and region edits as Seedance 2.5 capabilities. | Do not promise Cinema Studio’s Genre/Era/Tempo/Emotion Wheel/camera/lens/aperture panels here. Do not call its image/video/reference behaviour a FLUX workflow. | `HF-WEB@2026-09-04 / Video / Seedance 2.5 / active mode` |
| **Higgsfield → Image → FLUX.2** | A named **image**-model surface. Current Higgsfield categorises FLUX.2 with Image Models and describes reference-led image creation/editing. | FLUX.2 is not a Cinema Studio film-control panel and not a text-to-video model. Never attach video duration, camera movement, native-audio, or Cinema Studio settings to it. | `HF-WEB@2026-09-04 / Image / FLUX.2 / active mode` |
| **Higgsfield → Upscale → FLUX 3 Video Upscaler** | A distinct video-finishing tool: source clip, **Precise** or **Creative** mode, and optional Creative prompt guidance. | This is not FLUX.2 image generation and not Seedance video generation; do not suggest reference-image, cast, Cinema, or shot-planning settings unless the active Upscaler screen itself exposes them. | `HF-WEB@2026-09-04 / Upscale / FLUX 3 Video Upscaler / Precise|Creative` |
| **Higgsfield → Audio / Lipsync Studio / Relight / Colour Palette / Layers** | Separate specialist forms for voice, lip sync, video light/grade, and image decomposition/editing. | An Audio/Lipsync, Relight, grade, or Layer setting is not a generation-model field. Route the user to the specialist tool instead of stuffing the request into a T2V prompt. | `HF-WEB@2026-09-04 / named specialist tool` |
| **fal.ai → exact endpoint → Playground/Sandbox** | Only fields rendered from that endpoint’s current schema. An endpoint may offer a prompt, enum, seed, upload, mask, audio, or visual camera widget—or none of these. | No global fal “video settings,” Cinema-like studio controls, or endpoint parity. A field from `provider/model-A` cannot be proposed for `provider/model-B` without its schema. | `FAL-WEB@2026-09-04 / endpoint_id / schema retrieval date` |
| **Runway → Tool Mode / named App / Agent / Workflow node** | The selected surface owns the form: e.g. Gen-4 Image, Gen-4.5 video, Act-Two, Aleph Edit Studio, an App task form, or node ports. | An App capability is not automatically a Gen-4.5 option; Agent preference is not a reusable Tool Mode parameter; Gen-4 Image reference controls are not Gen-4.5 editing controls. | `RW-WEB@2026-09-04 / named surface / named model + mode` |
| **OpenArt → named tool → selected model → mode** | The Video/Image/Smart Shot/Edit/Director form selected by the user, plus saved assets. Its model picker can change the visible inputs. | A Start/End Frame, Smart Shot, Director, or Edit Video setting is not a universal “OpenArt Seedance” field, even when the same provider model name is displayed. | `OA-WEB@2026-09-04 / URL / selected model + mode` |
| **Arcads → Studio / AI Actor mode / B-roll / Translate / Mark / Workflow** | A product-ad control plane. Each route owns separate fields: image model/prompt, actor/voice/script/emotion, movement, B-roll model, locale/accent, conversational campaign brief, or nodes. | An Arcads actor, script emotion, subtitle, translation, or Workflow-node option is not a Seedance/FLUX/Cinema parameter—and an underlying video-model choice does not make all Arcads ad tools available in that model form. | `AR-WEB@2026-08-31 / named Arcads surface / active model or node` |
| **ChatGPT → ordinary chat → built-in image generation** | Natural-language prompt; attached reference image(s); conversational, targeted follow-up edits. The built-in route uses **`gpt-image-2`**. | It has no native video-generation route in this reference. Do not call a connector automatically and do not represent another provider’s model/mode/asset controls as native ChatGPT controls. | `CGPT-IMG@gpt-image-2@2026-09-04 / native chat` |

### How an agent converts an artistic instruction into an actionable one

| User intent | Correct action | Unsafe shortcut |
|---|---|---|
| “Make it a 1980s noir shot with a slow pan.” | In **Cinema Studio 4.0**, choose Era, Genre, and the visible movement preset; use the prompt for the event and concrete period props. | Claim that Seedance/FLUX/fal has those three selector values. |
| “Use this product image and preserve its label.” | Open the selected model/mode’s reference or image-input control and inspect its current limits; use a dedicated edit/region tool if the task is local replacement. | Assume every image/video model accepts references, masks, region edits, or text fidelity. |
| “Make the actor more fearful.” | In Cinema, use the Emotion Wheel with the actual `@Element`/character reference. Else write the performance intent in the prompt and say that it is not an equivalent control. | Offer the Cinema Emotion Wheel in a standalone Seedance, FLUX, fal, Runway, or OpenArt form. |
| “Change the grade/light after we like the take.” | Use Higgsfield Relight/Colour Palette or the selected platform’s dedicated video-edit tool. | Regenerate through a video model and promise a targeted non-destructive adjustment. |

**Output values are a final-form check, not a routing signal.** Resolution, duration, quantity, price, and plan entitlement are deliberately not used to identify a workflow here. They belong to the active model/mode and subscription form; read them only after the surface and creative controls above are fixed. A displayed output dropdown can be reported as a setting **of that exact form**, never as a platform-wide or model-family guarantee.

The Higgsfield split above is supported by the current product taxonomy, which lists Cinema Studio separately from Video Models and Image Models, and by the current Seedance/FLUX/FLUX-upscaler material. [Higgsfield model categories](https://higgsfield.ai/creator-hub/help-center/ai-models) · [Seedance 2.5](https://higgsfield.ai/seedance/2.5) · [FLUX.2 guide](https://higgsfield.ai/blog/FLUX-2-is-on-Higgsfield-Full-Guide) · [FLUX 3 Video Upscaler update](https://www.higgsfield.company/creator-hub/changelog)

---

## Alternative access paths: web UI, MCP, and ChatGPT

> **Version scope:** Each connector row below uses the matching `*-MCP` key in the version ledger; native ChatGPT uses `CGPT-IMG@gpt-image-2@2026-09-04`; API-only fields use `OPENAI-IMG-API@gpt-image-2@2026-09-04`. A connector is revalidated in the connected session, not merely by this dated page.

**MCP is an alternative way to make the provider generate media; it is not a mirror of the provider’s web UI.** A connected agent can take a prompt/reference and run a provider operation without opening a browser tab. That is useful for an agentic workflow, but it creates a separate control plane with its own tool list, authentication, billing and result destination. A missing MCP tool, a plan restriction, or a different account/workspace is a real capability boundary—not something the agent may fill in with web-UI knowledge.

### Mandatory route declaration

Before any generation, state one of these exact routes in the proposal and user-facing activity log:

1. **Web:** `Provider web UI → workspace/project → tool → model → mode`.
2. **MCP:** `Host agent → named provider MCP → authenticated provider account/workspace → exposed tool → model/mode`.
3. **ChatGPT native:** ChatGPT chat → built-in GPT Image 2 (`gpt-image-2`).
4. **OpenAI API:** `application/agent → OpenAI API → Image API or Responses image-generation tool`.

Do not collapse (2) into (1), or (3) into (4). In particular, a ChatGPT subscription/session does not prove access to the user’s Runway, Higgsfield, OpenArt, Arcads, or fal billing/workspace; an API key/billing relationship is also separate from ChatGPT plan availability. Ask the user to choose/sign in/switch workspace when that identity is not visible.

### Verified MCP routes and their non-parity rules

| Provider MCP | What the current connector can do | Account/workspace and UI boundary an agent must observe | Version scope to cite |
|---|---|---|---|
| **Higgsfield MCP** — `mcp.higgsfield.ai/mcp` | Generate images, video, Soul characters and audio, plus check credit balance, through OAuth to an existing Higgsfield account. Outputs appear in Higgsfield Assets. | It is an automation route, not a Cinema Studio panel. Higgsfield explicitly says web-only Unlimited/free generation access does **not** apply: MCP always spends standard credits. Do not infer Cinema project, camera/Emotion Wheel, finishing-tool, or web-plan behaviour from a successful MCP generation. | `HF-MCP@2026-09-04 / exposed operation` |
| **Higgsfield Bridge MCP** — `bridge.higgsfield.ai/mcp` | Lets a host agent (Claude Desktop custom connector) build and edit gray-box scenes, cameras and cuts in the OPEN Blender file through the add-on; the add-on's tabs then generate/render. | Not the generation MCP: no image/video generation or credit tools verified on this server; output is the open .blend / playblast, not Higgsfield Assets; requires add-on installed and logged in; plan-level unlimited models excluded on plugins/MCP/Canvas. Exposed tool list unverified — read in session. | `HF-BRIDGE-MCP@2026-09-04 / exposed tool` |
| **fal MCP** — `mcp.fal.ai/mcp` | Eleven documented tools (2026-09-04): `search_models`, `get_model_schema`, `get_pricing`, `search_docs`, `recommend_model`, `run_model`, `submit_job`, `check_job`, `get_job_result`, `cancel_job`, `upload_file`. | It is a stateless API path using the user’s **FAL API key**. It can expose any API field only after `get_model_schema`; it is not the Sandbox/Playground comparison UI, generation gallery, or a shared film workspace. | `FAL-MCP@2026-09-04 / endpoint_id + schema retrieval date` |
| **Runway MCP** — `mcp.runwayml.com/mcp` | Generate images/videos in an MCP-capable agent after signing in to the Runway app account; model availability is plan-dependent. | It spends Runway credits, and **Explore Mode is explicitly unsupported** through MCP. Use Streamable HTTP only. Do not promise the full Tool Mode/App/Agent/Workflows/Timeline experience through the connector. | `RW-MCP@2026-09-04 / named model + mode` |
| **OpenArt MCP** — `mcp.openart.ai/mcp` | Generate images/video/I2V, discover models, use library assets/references, upload files, inspect credits, switch workspaces and organize projects via OAuth. Results are saved to the connected OpenArt library/workspace. | On managed plans, an owner/admin must add the connector and each member signs in to an OpenArt account; verify the active workspace. **Character and Smart Shot are explicitly not yet available through MCP** (roadmap), even though they exist in the web suite. | `OA-MCP@2026-09-04 / workspace + exposed tool` |
| **Arcads MCP** — `mcp.arcads.ai` | Create AI video ads from a supported MCP client using the connected Arcads account. | An active Arcads subscription and remaining Arcads credits are required. The current public MCP guide still says examples are forthcoming, so do not infer full Studio/Mark/Workflow/actor-tool parity; inspect the exposed tools and retain the ad-review boundary. | `AR-MCP@2026-06-26 / exposed tool` |

[Higgsfield MCP differences](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp) · [fal MCP tool reference](https://fal.ai/docs/documentation/setting-up/mcp) · [Runway MCP guide](https://help.runwayml.com/hc/en-us/articles/51931843164691-Connecting-to-Runway-MCP) · [OpenArt MCP](https://openart.ai/mcp/) · [Arcads MCP](https://intercom.help/arcads/en/articles/15655699-arcads-mcp)

### ChatGPT native image generation: GPT Image 2

Treat **ChatGPT itself** as a first-class *still-image* route. In a normal ChatGPT chat, the user can describe an image, attach reference image(s), then request iterative or targeted edits in the same conversation. The canonical built-in model name is **`gpt-image-2`** (often described informally as “GPT Image 2.0”). This is appropriate for concept frames, plates, product/still iteration and image edits before handing an approved result to a video platform. It is **not** a native replacement for Seedance, Cinema Studio, an Arcads actor, or any other video/film workspace. [ChatGPT image-generation guide](https://learn.chatgpt.com/docs/image-generation)

| User request | Agent-safe ChatGPT route | Do not claim |
|---|---|---|
| Create or revise a still image conversationally | Use native ChatGPT image generation with a concrete prompt; attach a source/reference image for transform/extension; make small targeted follow-up edits and review the result. | That the chat exposes a named video model, Cinema camera controls, a persistent provider project, or exact external-platform reference semantics. |
| Produce a video from chat | Use a named, authenticated **provider MCP** only if it is available and the user selects/authorizes it; state the provider and its workspace/credits. | That “ChatGPT” alone generates the video, or that an OpenArt/Runway/Higgsfield connector inherits the ChatGPT-native GPT Image 2 controls. |
| Automate/batch GPT Image 2 | Use the OpenAI **Image API** for one-shot generate/edit requests, or the **Responses API** image-generation tool for multi-turn programmatic editing. | That ChatGPT plan limits, API keys, API billing, outputs, or model setting UI are interchangeable. |

In ChatGPT web, image availability and usage limits are plan/workspace dependent. For programmatic use, the current OpenAI docs distinguish the Image API (direct `gpt-image-2` choice) from the Responses API (a mainline model invokes an image-generation tool); both are a different account/billing/control path from ordinary ChatGPT use. The API may expose output parameters such as size, quality, format, compression and background, but an agent must only propose those when using the API—not invent them as ChatGPT-web dropdowns. [OpenAI image-generation API guide](https://developers.openai.com/api/docs/guides/image-generation)

### MCP execution gate

1. Confirm the **host agent**, connector name, provider account, target workspace/project, visible credit balance and intended model/mode.
2. Read the MCP tool schema/list **in that connected session**. If it lacks the required operation, offer the provider web UI instead; do not simulate an unavailable action with prompt wording.
3. Say where the output will land: the conversation only, provider Assets/library/project, or API response URL/file. Download/upload an approved asset deliberately before chaining it to another provider.
4. Show the provider cost/credit consequence and obtain the normal generation approval. MCP convenience never authorizes unreviewed spending, batch creation, or publishing.

---

## 1. Higgsfield — Cinema Studio 4.0 and adjacent creation tools

> **Version scope:** `HF-CS4@2026-09-04` applies only to Cinema Studio 4.0 and its project-specific claims; `HF-WEB@2026-09-04` applies to the other Higgsfield web tools. `HF-MCP@2026-09-04` applies only when explicitly named. Cinema-specific controls never inherit into standalone Video/Image/Audio/Edit tools. `HF-BRIDGE-MCP@2026-09-04` applies only to the Blender add-on's Bridge connector and never to `mcp.higgsfield.ai/mcp`.

### Current navigation and object model

The signed-out Cinema Studio shell exposes **Home, My generations, My elements, My favorites, Community, Academy, and Projects**, with a project search and **New project** action. The broader product navigation (signed-out shell, 2026-09-04) separates **Image, Video, Audio, Edit (Layers), Cinema Studio 4.0, Marketing Studio, 3D Jutsu (new — described only as "AI-powered camera control", surface unverified), MCP & CLI, Supercomputer, Academy, Viral Presets, Community, Contests, Plugins, Canvas, Originals**. A project is therefore the appropriate home for a multi-shot film; a generic Video/Image page is the appropriate home for a single model test. [Cinema Studio shell](https://higgsfield.ai/generate/video) · [Cinema Studio 4.0 overview](https://higgsfield.ai/blog/cinema-studio-4-0)

**Persistent reusable things:**

- **Elements** are the asset layer for characters, locations, and props; the UI calls them from a project rather than requiring repeated manual uploads.
- **AI Cast / Soul ID** are Higgsfield’s recurring-character route. Current studio material describes a trained identity as reusable across scenes/models; retain the actual character/Element name and reference it exactly. Do not promise a training-photo count or cross-model fidelity unless the user’s current Soul ID screen states it.
- **Project Brief, Canvas, subfolders, shared Elements, and live multi-user generation** are collaboration/organization features—not evidence that the system has made a final artistic decision for the user.
- **Personal Assistant** (canonical name in this skill; historically "Mr. Higgs", "Claude Chat" (3.5 docs), "AI Director" in tester videos): the script-to-shots/prompt-writing aid; it never spends credits.
- **Academy** is now a video-lesson surface with copyable prompts in a Keypoints panel. The older course format was retired on 10 August 2026. [Current changelog](https://www.higgsfield.company/creator-hub/changelog)

### Cinema Studio 4.0: what a user sets before generation

Cinema Studio 4.0 is the current filmmaking interface, launched 12 August 2026. Its direct controls are the correct channel for film grammar; the text prompt should principally describe the on-screen event. Higgsfield explicitly says these controls are applied before generation rather than merely as post filters. [Official 4.0 guide](https://higgsfield.ai/blog/cinema-studio-4-0)

| Panel / control | Verified current choices | What the agent should put there |
|---|---|---|
| **Genre** | General, Action, Epic, Drama, Comedy, Horror, Noir | Overall film logic/pacing. General leaves visual logic primarily to the prompt; do not also give contradictory genre directions in prose. |
| **Era** | Auto plus decade looks documented for 1960s, 1980s, 1990s, 2000s, 2020s; the product describes direct decade selection | Temporal capture/grade character, not plot period details that must appear as props/costume. |
| **Tempo / Montage Pacing** | Auto, Chaotic, Dynamic, Calm, Single Shot | Cut rhythm. Use **Single Shot** for one continuous take; do not promise an editable NLE timeline merely because the setting can generate cuts. |
| **Emotion Wheel** | Hope, Anger, Joy, Trust, Fear, Surprise, Sadness, Disgust; used with an `@character_name` tag | Performance for a named character, e.g. `@mara Fear`. It is not a general “make the whole film sad” knob. |
| **Colour Palette** | 50+ named templates; examples include Film Colors, Black Gloss, Candy Pink, Lime Jam, Nostalgic Blue | Colour/tonal direction. Use one deliberate choice and avoid countermanding it with a long incompatible colour recipe. |
| **Lighting** | Auto; Silhouette, Practicals, Window, Overhead Fall, Contre-jour, Soft Cross; manual colour, brightness, diffusion, angle | Source/direction of light. `Practicals` means visible in-frame sources; use it where a lamp, candle, signage, etc. must motivate the light. |
| **Camera type** | Auto, Modern, 35mm Film, 8mm Film, DV Camcorder | Base capture character. This is a look control, not a guarantee of a particular physical camera body. |
| **Lens** | Auto, Clean Sharp, Anamorphic, Vintage Anamorphic, Warm Vintage, Halation Vintage | Optical character. The official page enumerates Auto plus five actual lens looks. |
| **Aperture** | Auto, f/1.4 Wide Open, f/4 Moderate, f/11 Deep Focus | Depth-of-field intent. Use f/11 where environmental continuity matters; use f/1.4 only where loss of background detail is desired. |
| **Camera movement** | 30+ presets; documented examples include POV, Robot Arm, Pan Left, Helicopter Shot, tracking and pedestal-down | A camera path. Pick a single path appropriate to the beat; no need to duplicate it in the prompt unless a timing/detail is essential. |
| **References** | Up to 50 reference slots in one generation (the 4.0 guide's wording is "50 image references"; it does not enumerate classes). With **Seedance 2.5** selected, plan by ByteDance's official class split — 30 image + 10 video + 10 audio, incl. `@Clay Render` and `@Audio` (SKILL.md rule 5, video-prompting ch. 14b) — 🟡 whether the Cinema Studio upload widget exposes the video/audio slots is not yet receipted; confirm on the live subform and record it in the version ledger. Other models: read the active upload hint. | Attach references for identity, product shape, location, composition, style, motion and voice. Name/organize them in Elements where they recur. |

Precedence: the per-class split in SKILL.md rule 5 / video-prompting ch. 14b is the planning budget; any "50" in a Higgsfield table is the total slot count, never a per-class figure, and never a reason to drop @Video/@Audio/@Clay Render references from the checklist.

The source guide lists all above values and their intended visual effect, including the eight Emotion Wheel values and all lighting/camera/lens/aperture choices. [Film setup and character controls](https://higgsfield.ai/blog/cinema-studio-4-0#film-setup-genre-era-and-tempo) · [Camera controls](https://higgsfield.ai/blog/cinema-studio-4-0#camera-settings-camera-lens-and-aperture)

### Cinema Studio 4.0: reliable user workflow

> 🟡 **Do the controls bite? Verify per project [P26, P27 — both Higgsfield-sponsored testers, 2026-08-24 and 2026-09-01].** Two independent walkthroughs report that Film setup (Genre/Era/Tempo), Camera (lens/format) and Lighting presets produced no visible change on Seedance 2.5 video, while the same instruction written in the prompt ("silhouette backlighting") did; only the first of three inline camera movements in one 15-s prompt executed; the Personal Assistant refused dragged assets and produced nothing on 2026-08-24. ⚠️ Conflicts with the official routing above ("direct controls are the correct channel"). Rule until a live receipt settles it: run one A/B at 480p per project — if a control does not bite, carry that aspect in the prompt block that governs it (video-prompting ch. 12), never in both. Same testers: CS 4.0 bills the same credits as plain Seedance 2.5 on the Video page; `Shift+#` inside the video prompt opens the camera-movement picker inline (Snorri cam, rack focus, POV, side tracking, handheld, Robo arm seen); a prompt pasted with element names already in `@tag` form auto-attaches those Elements — let the LLM write the tags.

1. **Create/open a project.** Add the brief, make subfolders for sequences/versions if needed, and create or collect Elements first.
2. **Split the script into shots.** The Personal Assistant can turn a script into individual shots and prefill camera parameters, but the agent/user must review the proposed prompt and settings before any generation. It is documented as a planning/settings aid, not a substitute for approval.
3. **Choose the shot’s model in the current selector when available.** Cinema Studio supports multiple models; route by the current dropdown and model-specific UI, not by a generic promise that every model has every Cinema Studio control.
4. **Set the world in controls:** genre → era → camera/lens/aperture → palette/lighting → tempo. Add a named character’s Emotion Wheel tag where performance matters.
5. **Attach references and write only the remaining scene/action.** With the control surface already chosen, the prompt should state subject, event, order of actions, and continuity locks—not re-specify every optical setting.
6. **Generate, review, and preserve the selected take.** Use a project/Element-aware iteration rather than starting a separate unrelated prompt for every take.
7. **Repair/continue rather than inventing a new shot when appropriate.** Cinema Studio 4.0 has **Forward/Backward Extend** for a continuation or lead-in from an uploaded/existing video. It is not a start/end-frame animation control.
8. **Apply finishing passes separately.** Colour Grading provides temperature, contrast, saturation, sharpness, grain, highlights, and exposure; the same current release family also offers Relight and Colour Palette as standalone video tools. [4.0 workflow](https://higgsfield.ai/blog/cinema-studio-4-0#step-by-step-how-to-direct-a-scene-in-cinema-studio-40) · [Relight/Colour Palette update](https://www.higgsfield.company/creator-hub/changelog)

### What else the current Higgsfield UI can do

These are adjacent routes; do not force them through Cinema Studio when the user asks for the specific operation.

| User goal | Correct current surface | Verified handling |
|---|---|---|
| Test a named third-party/native video model without the film-project framing | **Video** | Use the model selector; model features and resolution are model/plan dependent. The current changelog directs Seedance 2.5 users to Video → model selector; entries up to 2026-09-01 add **Genjutsu** (object swap / motion transfer on an existing clip: one video ≤30 s + up to 30 reference photos, output ≤1080p — a repair/re-skin route, W5), **MiniMax H3 Max** (768p, first/last frame), **Gemini Omni 1.1 Flash** (first/last frame, 360p draft to 4K, ≤10 s), **Wan 3.0 / Wan 3.0 Prime** (≤30 s, 480/720/1080p), Kling 3.0 Turbo, Grok Video 1.5, Seedance 2.0 Mini. |
| Storyboard / multi-frame sequence stills (up to 8 frames, up to 4 image references, Auto or Manual) | **Image → Popcorn** (help-center article modified 2026-08-28) | Frames serve as start frames or references for a video model; chain the final frame into the next clip. Not a video generator. |
| Camera-move presets on a single keyframe image (3 or 5 s clips) | **Video → Create Video → model selector → Higgsfield DoP** ("Higgsfield Standard" preset label; help-center article modified 2026-08-28) | Image-to-video with preset categories (Basic/Epic Camera Control, Effects, Mix); describe the scene in the prompt. The old "preserve the original face, lighting, and geometry" line is practitioner practice, not documented on the help page. |
| Edit an existing Seedance take (region/timestamp-scoped fix) | **Video → model entry "Seedance 2.5 Edit"** (🟡 a draw-over region tool with time handles was seen inside Cinema Studio's Edit → Advanced on 2026-09-01 [P27] — unverified; if real, "describe the region in words" holds for the Video page only) | Its own entry in the video-model selector [PP@2026-08-31]: task dropdown "Edit video", source clip into the **VIDEO TO EDIT** slot, references via @-elements, up to 1080p; regions are described in words (no mask editor). Mode doctrine + prompt format: video-prompting ch. 14b. |
| Block, preview and render a shot from inside Blender; perform a handheld camera with a phone | **Blender add-on** (higgsfield.ai/plugins/blender, unversioned UI @ 2026-09-04; Image tab lists Nano Banana 2, GPT Image, Seedream 5.0 Pro, Z Image) — seven tabs incl. Scene builder, Video (Seedance 2.5) and Camera (phone as tracked virtual camera, 🟡 launch video only) | Same credits as the web platform; plan-level unlimited models excluded on plugins/MCP/Canvas; Bridge MCP for agent-driven blockouts (`HF-BRIDGE-MCP@2026-09-04`). Method: production-pipeline ch. 8. |
| Correct light or grade on an existing clip | **Relight** / **Color Palette** | Relight has six presets plus manual light parameters and up to two custom sources; Colour Palette has 50+ presets plus custom grading. |
| Separate/rebuild a still image | **Layers** | Layer Decomposition, Edit Text, and Remove Background are currently listed actions. |
| Upscale a video | **Upscale / FLUX 3 Video Upscaler** | Precise and Creative modes; outputs listed as 1080p, 2K, or 4K. Creative mode can use optional prompt guidance. |
| Generate voice/change voice/translate and lip-sync | **Audio** / **Lipsync Studio** | Audio exposes Text to Speech, Voice Change, and Translate; Translate includes 18 languages in the 10 August update. Verify the active model’s advanced controls in the UI. |
| Batch variant production | **Supercomputer** or a specialist studio such as Marketing Studio | Treat this as an agent/task workflow and retain human approval at the brief/outputs; it is not evidence that Cinema Studio alone maintains an editorial timeline. |

### Seedance 2.5 mode id ↔ UI label (Higgsfield)
| Mode id (video-prompting ch. 14b) | Higgsfield Video page label | Evidence |
|---|---|---|
| `t2v` | model entry "Seedance 2.5", no source clip attached — task label unverified, read the live task dropdown | `HF-WEB@2026-09-04` |
| `omni_reference` | model entry "Seedance 2.5" with the source clip attached as a REFERENCE (Higgsfield's marketing name for this is "R2V motion guidance") — NOT the "Seedance 2.5 Edit" entry, which locks duration/ratio and bills the source length (production-pipeline ch. 8). Exact task label unverified, read the live task dropdown | `HF-WEB@2026-09-04` + P21 |
| `video_edit` | model entry "Seedance 2.5 Edit", task "Edit video", VIDEO TO EDIT slot | `HF-WEB@2026-09-04` [PP] |
| `video_extension` | the Extend control (product page: "Extend/Transition/Reverse"; Cinema Studio 4.0: "Forward/Backward Extend") | `HF-CS4@2026-09-04` |

Rule: the slate's Run in row writes the mode as `id ("UI label")` — e.g. `video_edit ("Seedance 2.5 Edit")` — and, where the label column says unverified, as `id (UI label unverified — read the live task dropdown; if only "Seedance 2.5 Edit" looks applicable, STOP: that is video_edit, not this mode)`. Never invent a dropdown label. Dreamina and other vendors: no label map exists here — write `id (label unverified)` and cite the RECEIPT line.

### Output configuration: model/plan dependent, not a transferable creative control

- The detailed 4.0 launch guide and changelog verify **up to 30 seconds** and **up to 1080p**; a separate Higgsfield marketing page simultaneously claims native 4K and one-minute generations. These official pages conflict as of the snapshot date. This is an output-form conflict, not an artistic-routing rule: read the active model/plan dropdown before generating. [Detailed guide](https://higgsfield.ai/blog/cinema-studio-4-0) · [conflicting product page](https://higgsfield.ai/cinematic-video-generator)
- Do not recommend the Cinema Studio 2.0/2.5/3.0/3.5 walkthroughs as the current UI. They document historical versions. In particular, their external-upload restrictions must not be projected onto 4.0, which officially accepts up to 50 reference slots (class split per selected model — see the References row above).
- “Multi-model support,” AI Cast, and camera presets do not prove that a given selected provider model has identical reference, native-audio, editing, duration, or resolution support. Inspect the model subform.
- The current product is web-first; no current primary source here establishes an autonomous assistant that may spend credits without user review. Keep the user at the Generate/approval boundary.

### Higgsfield learning sources

- [Cinema Studio 4.0: official control-by-control guide](https://higgsfield.ai/blog/cinema-studio-4-0)
- [Higgsfield Creator Hub help for historical Studio versions](https://higgsfield.ai/creator-hub/help-center/tools/how-do-i-use-cinema-studio) — useful only to recognize old UI labels, not as the 4.0 authority.
- [Current changelog](https://www.higgsfield.company/creator-hub/changelog) — recheck here before a production session.
- [Academy](https://higgsfield.ai/academy) — current interactive video lessons and copyable prompt keypoints.

---

## 2. fal.ai — model marketplace, test UI, and production API

> **Version scope:** `FAL-WEB@2026-09-04` applies to Gallery/Playground/Sandbox/Dashboard UI behaviour. For every actual model claim, replace the inherited scope with `endpoint_id + schema retrieved YYYY-MM-DD`; `FAL-MCP@2026-09-04` applies only to the MCP section.

### The key correction: fal is not a universal editing studio

fal gives access to 1,000+ image, video, audio, 3D, and other endpoints. It has a useful browser UI, but its core product is a unified API/endpoint platform. Its individual controls are generated from a model’s input schema; two video models can expose completely different fields. Therefore an agent may suggest **“open this exact endpoint and inspect its form”**, but may not invent a shared camera panel, storyboard, persistent character system, multi-shot editor, or prompt syntax for all fal models. [Model APIs overview](https://fal.ai/docs/documentation/model-apis/overview)

### The browser surfaces a user can use

| Surface | What it is for | Actual UI behavior |
|---|---|---|
| **Model Gallery / model page** | Find a provider/model or operation | Each model page provides its own Playground and API documentation, pricing, average latency, and copyable examples. |
| **Playground** | Validate one specific model and reproduce the exact request | Fill its auto-generated form, click **Run**, see result(s), change fields and run again. The result retains generated code in Python, JavaScript, and cURL for that exact request. |
| **Sandbox** | Compare alternatives before committing | Run matching input/prompt across multiple models side-by-side; see estimated cost before submitting; search prior generations by text, image similarity, or dominant colour; share a preview link. It does **not** generate integration code. |
| **Dashboard** | Developer/account operations | Manage apps, API keys, billing, monitoring/analytics, requests, errors, and deployments. This is not the creative editing surface. |
| **Free browser tools** | Single-file utility jobs | Some background/remove/upscale/extend/resize tools run in-browser. Video-generation entries direct to Playground, require sign-in, and bill compute per second. |

[Playground manual](https://fal.ai/docs/documentation/model-apis/playground) · [Sandbox manual](https://fal.ai/docs/documentation/model-apis/sandbox) · [Dashboard/resources map](https://fal.ai/docs/documentation/setting-up/resources) · [free tools scope](https://fal.ai/tools)

### What the Playground actually exposes
🟡 Model-form fact (fal Omni for MiniMax H3, snapshot 2026-08-02 [P42]): prompt cap ≈2,000 characters on the fal form vs ≈7,000 for the raw model — condense the official six-section Ref2VA prompt before pasting; 15 s / 2K / 21:9 took ≈10 min inference.

The model author’s schema drives the form. Required fields and `ui.important` fields appear in the main form; optional fields with defaults normally sit under **Additional Settings**. An agent must open the selected endpoint’s **API** tab and treat that schema as canonical.

| Schema pattern / metadata | Browser control rendered by Playground |
|---|---|
| `prompt` or `*_prompt` | Multi-line text area |
| `bool` | Toggle |
| bounded integer/float | Slider plus number input |
| `seed` | Number input plus randomize button |
| enum / literal | Dropdown |
| `*_image_url` / image field | Drag-drop, paste, or URL image upload and preview |
| `*_video_url` / video field | Video upload and preview |
| `*_audio_url` / audio field | Audio upload/player and microphone recording |
| `*_mask_image_url` / `*_mask_url` | Image input with built-in mask painter linked to the image field |
| `face_image_url` | Camera capture plus image upload |
| `camera_control` metadata | Visual movement selector with movement type/value |

Outputs render as galleries/players only when the schema identifies them as Image, Video, or Audio; otherwise they may be raw JSON/download links. A model having a `prompt` does not imply it supports a negative prompt, a seed, a reference image, end frame, mask, audio, or camera UI—only its active schema can establish that. [Full UI mapping](https://fal.ai/docs/documentation/development/handle-inputs-and-outputs)

### User workflow: visual exploration → reliable integration

1. **State the operation, not a brand preference:** text-to-image, image edit, text-to-video, image-to-video, video edit/restyle, upscale, audio, etc.
2. **Use Sandbox for a fair A/B test.** Pick models that accept the same source type, use the same source/prompt, inspect the displayed estimate, then compare outputs. Save/share the winning result.
3. **Open the winner’s individual Playground.** Fill every field from its current schema, including model-specific aspect ratio, duration, output format, safety, reference, seed, or audio controls.
4. **Run and evaluate.** Keep the resulting parameter set; the Playground result can produce exact Python/JS/cURL code.
5. **Only then automate.** Call the endpoint using its identifier and exact request. For a production batch, use a queue/async pattern and retain the returned request ID and output URL(s).
6. **For an internal custom UI/model, deploy an App.** `fal deploy` supplies the App with its own Playground; authors control safe field rendering through their schema.

### API workflow an implementation agent may propose

| Need | fal call pattern | Important boundary |
|---|---|---|
| Quick local prototype / fast request | `run()` | Direct call, no queue/retry/polling. |
| “Synchronous” developer convenience | `subscribe()` | Uses the queue but waits and handles polling. |
| Production parallel/batch work | `submit()` then status/result or webhook | Recommended route for control and reliability; it returns immediately. |
| Progressive updates | `stream()` | Only where endpoint supports it. |
| Very-low-latency interaction | `realtime()` | Persistent WebSocket, only for explicit real-time endpoints. |

An app must keep `FAL_KEY` server-side; a browser frontend uses a server proxy rather than exposing the key. This is an implementation constraint, not a creative setting. [Inference methods](https://fal.ai/docs/documentation/model-apis/inference) · [client setup](https://fal.ai/docs/documentation/model-apis/inference/client-setup)

### Correct and incorrect fal advice

**Safe:** “In Sandbox, compare the current image-to-video endpoints that accept one source image; then open the selected model’s Playground, check duration/reference/audio fields, and copy the exact request.”

**Unsafe:** “fal’s video editor can mask the actor and use a dolly preset.” That may be true for a particular endpoint schema but is not a fal-wide feature.

**Safe:** “A Playground may provide a mask painter when that endpoint has a matching mask field.”

**Unsafe:** “The results will remain as a permanent project asset.” fal returns CDN URLs/metadata; application-level preservation, asset naming, and editorial assembly are the user’s/pipeline’s responsibility unless their custom App implements them.

### fal learning sources

- [Playground](https://fal.ai/docs/documentation/model-apis/playground) and [Sandbox](https://fal.ai/docs/documentation/model-apis/sandbox)
- [Model API reference](https://fal.ai/docs/model-api-reference) — concrete endpoint schemas and prompt/output examples.
- [Documentation index for agents](https://fal.ai/docs/llms.txt) — discover current pages before describing an endpoint.
- [Examples](https://fal.ai/docs/examples) — text/image/video integration examples, including ComfyUI deployment.

---

## 3. Runway — Tool Mode, Apps, Agent, Workflows, and timeline assembly

> **Version scope:** `RW-WEB@2026-09-04`. The named model/tool is part of the version record: e.g. a Gen-4.5 fact means `RW-WEB@2026-09-04 / Gen-4.5 / stated mode`, not all Runway video models. `RW-MCP@2026-09-04` is separate.

### Surface selection: the first decision

Runway deliberately offers several overlapping ways to create. The user’s goal determines the correct one.

| Surface | Use when | What an agent must not assume |
|---|---|---|
| **Tool Mode** | A single image/video generation or a named model’s direct settings | That an App’s convenience control will appear here. |
| **Apps** | A known operation such as keyframes, character swap, product video, relight, remove, or upscale | That the App is API-accessible; current Apps are **not** available through the API. |
| **Agent** | A conversational multi-asset/multi-shot task, planning, scripts, moodboards, an assembled cut, or a guided iteration | That it should act without an outline/review. The user should review its plan before credit-spending. |
| **Workflows** | A reusable, explicit node graph/automation, including custom Apps | That it is an ordinary NLE timeline. It is a graph of model/utility nodes. |
| **Timeline Studio** | Trimming and arranging clips into a shorter cut | That it replaces an advanced local editor for a feature/complex finishing job. |

Tools, Apps, and Agent automatically create a **Session**, which organizes the outputs generated there. Assets can be reused from the Runway library. [Getting started with generative video](https://help.runwayml.com/hc/en-us/articles/37425232841875-Getting-Started-with-Generative-Video) · [long-form workflow](https://help.runwayml.com/hc/en-us/articles/26871350018835-How-to-create-longer-videos-and-films)

### Tool Mode: current base image and video paths

#### Gen-4 Image

Open **Generate Image** from the Dashboard, then choose Gen-4/Gen-4 Turbo Image from the Runway group in the lower-left model selector. Current Gen-4 Image controls are:

- Prompt (text; up to 1,000 characters) and optional image reference; **Describe Image** can make an editable prompt from an upload.
- Aspect ratio: 16:9, 9:16, 1:1, 4:3, 3:4, or 21:9.
- Quantity: 1 or 4 images.
- Advanced: 720p/1080p, Aesthetic Range 0–5, random or fixed seed.
- After generation: **Use** sends the image to generative video; **Vary** starts a new set based on one output.

For persistent/reusable image references, turn on References, upload or pick an Asset, and tag it with a name. A single generation supports up to **three** References. Reference image quality, neutral expression/light, and separate character/environment iteration paths matter more than repeating prose. [Gen-4 Image manual](https://help.runwayml.com/hc/en-us/articles/37053594806419-Creating-with-Gen-4-Image) · [References manual](https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References)

#### Gen-4.5 video

In Tool Mode with **Video** selected, select **Gen-4.5** in the model picker. The current guide confirms Text-to-Video and Image-to-Video only; it says additional input support is coming, so do not offer unsupported reference/keyframe/audio modes as Gen-4.5 features.

| Setting | Current verified value |
|---|---|
| Inputs | Text for T2V; text + one image for I2V |
| Duration | 2–10 seconds |
| Aspect ratios | 16:9, 9:16, 1:1, 4:3, 3:4, 21:9 |
| Output | 720p |
| Frame rate | 24 or 25 fps, in Advanced settings |
| Price | 12 credits per second |
| Iteration | Generate; then favorite, upscale, download, or **Use** the result |

For I2V, the image supplies composition, subject, lighting, and style; prompt primarily for motion/camera/temporal change. Check the image for implied motion that contradicts the requested movement. For T2V, describe both visual content and motion. A simple useful pattern is “The camera [motion] as the subject [action].” [Gen-4.5 creation guide](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5) · [I2V prompting guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide)

#### Export choice

On eligible plans, Gen-4.5 Tool Mode and Aleph 2.0 Edit Studio can choose **MP4**, **ProRes** (six listed profiles), or a **PNG sequence** at generation time. ProRes/PNG adds 5 credits per second to the base generation cost. Check the plan and the current dialog; it is not a universal free download option. [Export guide](https://help.runwayml.com/hc/en-us/articles/54396547993491-Exporting-Videos-in-ProRes-and-PNG-Sequence-Formats)

### Apps: current named operations

Open **Apps** in the left sidebar, search or browse, then select an App. Apps are the right answer when a user asks for one of their clearly scoped operations. Input type and credit cost are shown inside the active App; some may support Explore Mode and others require Credits Mode. The iOS app does not currently expose Apps (a mobile browser can). [Apps manual](https://help.runwayml.com/hc/en-us/articles/45570040112531-Creating-with-Apps)

**Video Apps (current list):**

- Performance Capture with **Act-Two**; Animate with Keyframes; Backdrop; Character Swap; Color Grade; Image to Dialogue; Edit Studio; Lighting; Motion Sketch; Multi-Shot; Product Shot Video Builder; References; Remove; Stitch Video; Stylize Video; Time of Day; Upscale; Weather.

**Image Apps (current list):**

- Ad Concepter; Ad Localization; Character Renderer; Cinematic Brainstorm; Create Ad; Expand Image; Mockup; Panel Upscaler; Product Reshoot; Runway Look; Scene Builder; Slide Maker; Story Panels; Stylize Image; Upscale Image; Vary Image; Vary Ad.

**Audio Apps (current list):**

- Stylize Audio; SFX.

Important concrete App routes:

| Request | Current Runway route | Verified constraints / behavior |
|---|---|---|
| Transfer an actor’s performance to an image/video character | **Apps → Performance Capture with Act-Two** | Needs a driving performance video plus character image/video; up to 30 seconds at 24fps. Gesture control applies to character-image input, not character-video input. |
| Transition from a supplied first to end frame | **Apps → Animate with Keyframes** | Use this rather than claiming Gen-4.5 has keyframe input. |
| Prompted transformation of a supplied clip | **Apps → Edit Studio** (Aleph 2.0) | Current mode is Single edit; choose a keyframe, write a precise change, optionally limit a frame range, then generate across the footage. |
| Combine clips | **Apps → Stitch Video** or **Timeline Studio** | Stitch can combine files up to 60 minutes; selection/order is still the user’s editorial decision. |
| One prompted multi-cut asset | **Apps → Multi-Shot** | Official current app list says up to five shots from one text prompt. |
| Video 4K enhancement | **Apps → Upscale** | App listing says upload a video up to 40 seconds for 4K output. |

For Act-Two, use well-lit single-subject source media, typically waist-up or closer, with clear facial features and no interrupting cuts. An image target can receive environmental/gesture motion; a video target preserves its existing scene/camera motion and has no gesture control. [Act-Two manual](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two)

### Edit Studio / Aleph 2.0: an actual repair route

Open **Apps → Video → Edit Studio**, or search it. Upload/select a Runway asset or drag/drop a video. Current accepted source conditions are conventional aspect ratio, over 2 seconds and under 30 seconds (longer files are trimmed), 480p–1080p, 24–30fps, and no more than 10 cuts/shot changes. An unsupported source should be conformed/split externally before promising an in-platform edit.

Current **Single edit** procedure:

1. Select a keyframe that shows the thing to alter clearly (wide for an environment; close for e.g. eye colour).
2. Use a short, specific change prompt: action verb + desired transformation, e.g. “change the outfit and bag to soft yellow.”
3. Optionally work on a frame range; only the chosen time range spends Aleph generation credits.
4. The keyframe is rendered with an image model, then Aleph applies that appearance through the clip. Review the propagation before accepting it.

Supported creative intents documented by Runway: VFX, relight, background/product/object/wardrobe swap, restyle, and weather/season transformation. **Multi-edit and Expand are marked “coming soon” in the current manual**; do not offer them as an available Edit Studio mode. [Edit Studio manual](https://help.runwayml.com/hc/en-us/articles/51683104370451-Creating-with-Edit-Studio) · [Aleph 2.0 prompting](https://help.runwayml.com/hc/en-us/articles/52150503729171-Aleph-2-0-Prompting-Guide)

### Agent and Workflows

**Runway Agent** is a conversational creative partner. It can plan and generate images, single/multi-shot video, audio/music/voiceover, create storyboards/reference sheets/character sheets, edit images/video, and build/render a timeline. It selects a model automatically (including Gen-4.5 and supported third-party models), but the user may ask for a model. In a sensible workflow the user supplies a brief/assets, reviews Agent’s outline/intent, then asks it to generate or revise the specific scene. A slash command can invoke an Agent Skill such as an ad campaign or mood board. [Agent guide](https://help.runwayml.com/hc/en-us/articles/51601639579667-Creating-with-Runway-Agent)

**Workflows** are node graphs. Create one from **Workflows → + New Workflow**, add input/model/utility nodes, connect compatible ports, use **Run** on one node for isolated testing or **Run All** for the graph, and inspect/cancel parallel runs in Active Runs. Workflows can later be published as custom Apps/endpoints. The canonical stills-first graph is Text → Gen-4 Image → Gen-4 Video, with separate text nodes for still and motion prompting. [First Workflow tutorial](https://help.runwayml.com/hc/en-us/articles/45769159004691-Building-your-first-Workflows)

### Long-form rule and historical traps

- Runway’s own current film guide treats generative clips as short building blocks, typically 5–10-second storyboard shots. Make character and environment plates first; use references to carry them through shots; assemble with Timeline Studio for short pieces or a full editor for complex/long finishing. [Long-form guide](https://help.runwayml.com/hc/en-us/articles/26871350018835-How-to-create-longer-videos-and-films)
- **Gen-3 Alpha and Gen-3 Alpha Turbo were retired in July 2026.** Never give a new user a Gen-3, Act-One, old Video-to-Video, or Gen-3 keyframe workflow. The current replacement routes are Gen-4.5 for T2V/I2V, Animate Frames for keyframes, and Aleph 2.0 Edit Studio for video transformation. [Runway retirement notice](https://help.runwayml.com/hc/en-us/articles/33350169138323-Creating-with-Video-to-Video-on-Gen-3-Alpha-and-Turbo)

### Runway learning sources

- [Help Centre: current product sections](https://help.runwayml.com/hc/en-us/categories/1500001930562-Video-Editing)
- [Prompting guides and current model manuals](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5)
- [Runway Academy](https://academy.runwayml.com/) — current short video lessons, including [Agent 2.0](https://academy.runwayml.com/tutorial/agent-2).
- [Apps reference](https://help.runwayml.com/hc/en-us/articles/45570040112531-Creating-with-Apps) — recheck this list before routing to an App.

---

## 4. OpenArt — shot tools, persistent assets, Smart Shot, and Director

> **Version scope:** `OA-WEB@2026-09-04`. Values labelled “current default display” are observations of the linked **unversioned form and selected model/mode** on the snapshot date, not durable OpenArt defaults. `OA-MCP@2026-09-04` is a separate scope.

### Current suite navigation and persistent assets

The current suite’s left navigation is useful evidence of the product’s information architecture:

- **Chat:** Agent Ori (quick requests) and Director (large projects).
- **Tools:** Video, Image, World, Character, Audio.
- **Assets:** Director Projects, Character & World, Brand Kit, Media.
- **Inspire** plus pinned/all tools.

This matters: OpenArt has a real reusable asset layer. For recurring people, locations, product identity, logo/colours, use saved Character/World/Brand Kit/Media assets and attach/tag them in the actual creation surface. Do not rely on prompt wording alone for continuity. [Current Video suite shell](https://openart.ai/suite/video) · [current Character shell](https://openart.ai/suite/character) · [current World shell](https://openart.ai/suite/world)

### Create Image: current user workflow

1. From Home choose **Create → Create Image**.
2. Select a prompt-only model when text is sufficient; select a reference-capable model when a face/product/pose/style image must guide the output. The picker can filter by capability (e.g. reference or 4K), but availability is dynamic.
3. Write a visually specific prompt. OpenArt’s current starter structure is: **shot type → subject and its attributes → environment and lighting → style**.
4. Set model-exposed resolution, quality, aspect ratio, and quantity. Quality/resolution options vary by model; do not promise them merely because another model supports them.
5. Click **Create**, review the result grid, then download, **Send to Edit Image**, or **Send to Video**. **Image Variations** is a separate tool.
6. Supporting prompt actions: **Prompt from Image** converts an uploaded image into editable text only; it does not turn that source into a visual reference. **Enhance Prompt** revises the text and must be reviewed; Clear Prompt starts over.

[Official current image guide](https://openart.ai/blog/how-to-generate-an-ai-image/)

### Video: direct shot-level routes

The current **Video** tool hub exposes these routes:

- Frame to Video; Text to Video; Smart Shot; Edit Video; Dub Video; Replace Background; Relight Video; VFX; Motion Sync; Lip-Sync; Upscale Video; Replace Character; Extend Video; Add Sound Effect; Restyle Video.

This is a menu of distinct tool modes, not a claim that one generic prompt screen has all controls at once. [Current Video tool hub](https://openart.ai/suite/video)

#### Current Create Video form

The current unauthenticated surface documents the following initial form state; subscription/model selection can alter it:

| Form area | What the user can select/add |
|---|---|
| Mode | **Start/End Frame** or **Text with Reference** |
| Model | Current default display: **Seedance 2.5**; change only through the active model selector |
| Prompt | “Describe your video” |
| Inputs | Upload Media; saved Characters; visual references (JPEG/PNG/WEBP; current hint says 30MB max and 300–6000px per side) |
| References | Current default Seedance view displays **0/50** |
| Controls | Camera; **Auto Polish** prompt; Audio toggle |
| Output | Aspect ratio, resolution, duration, and quantity; current default display is 16:9 / 480p / 5s and 1 of 8 |

This is the exact point at which an agent should say “check the output row after choosing your model,” rather than quoting a platform-wide max. [Current Create Video form](https://openart.ai/suite/create-video)

Use **Frame to Video** where a supplied still/approved opening image should determine the first frame; use **Text to Video** when there is no image anchor; use the Start/End option only when that option is visible for the selected model. Add a saved Character and separate visual references when identity/appearance must persist. Use Audio only after confirming it is on and supported by the chosen model.

#### Smart Shot, direct video edit, and extensions

- **Smart Shot** is OpenArt’s structured multi-angle/storyboard route. The current screen asks for a scene description, supports character/object and environment references (the visible state shows up to three), previews a **Shot Plan**, and shows an output configuration; its current default display is 16:9 / 480p / Pro / 20s. Treat its exact length/resolution/reference allowance as active-UI/model dependent. [Current Smart Shot form](https://openart.ai/suite/smart-shot)
- **Edit Video** accepts a selected/uploaded source and a text edit description. The current form’s default model is Gemini Omni Flash and its visible input constraint is MP4/MOV, up to 100MB, 1–10s, 720–2160px. The source needs to meet those constraints before the agent proposes an in-platform edit. [Current Edit Video form](https://openart.ai/suite/modify-video)
- Use the dedicated **Extend Video** tool for continuation, not an unsupported request to make a single generator run indefinitely. OpenArt’s public current page describes extensions of up to 10 seconds at a time; verify in the chosen model/tool before running. [Video feature guide](https://openart.ai/ai-video-generator/)
- For a local transformation, pick the dedicated mode—VFX, Relight, Replace Background/Character, Restyle, Dub, Lip-Sync, Motion Sync, Upscale, or Add Sound Effect—rather than asking a fresh T2V run to preserve a source video.

### Director: conversation-driven multi-scene production

**OpenArt Director** is distinct from Text/Frame-to-Video. It is a chat-led production route for a concept that should become a multi-scene cut.

1. Start in **Director** and describe the idea. Add an image, scene/person reference, soundtrack, voice, or video if useful; tag a saved Character or World where applicable.
2. Answer the resolution, aspect ratio, and tone questions or let Director choose the initial settings.
3. Review the generated storyboard scene-by-scene before accepting the work.
4. Give conversational changes. The official description says Director should redo the frame/scene requested rather than the entire work.
5. Retain the project in **Director Projects** and use its assets in later revisions.

OpenArt markets Director as capable of coherent videos up to five minutes and edit-by-chat without a timeline. Treat that as a product capability claim—not a guarantee of perfect continuity, a substitute for reviewing the storyboard, or evidence of a frame-accurate conventional timeline. For precision cuts/finishing, the user may still choose individual tools or a conventional editor. [Director guide](https://openart.ai/blog/how-to-use-openart-director/)

### Characters, Worlds, and Brand continuity

| Asset type | Actual current route | What it gives the user | What it does **not** prove |
|---|---|---|---|
| **Character** | Tools → Character; current quick starts include Create Character, Character Image, Character Video, Talking Video, Motion Sync | A saved character library to attach in new visual/video generations. Character Builder also documents Look Vibe, Gender, Ethnicity, Age; Image-to-Character; and Text-to-Character. | Perfect identity or a particular non-human/anime style. The launch material initially limited Character Builder to photorealistic human characters; recheck current type choices. |
| **World** | Tools → World; quick starts include Create World, 3D World Cam, Cast in Scene | Persistent navigable environment from text/image, camera navigation, then a captured 2D image that can become a video keyframe or be edited. | A downloadable mesh/Gaussian-splat/Unreal/Blender asset. The launch source marks those exports as future work. |
| **Brand Kit** | Assets → Brand Kit | Saved recurring brand/logo/colour/style context in the suite. | That every chosen third-party model will obey logos, exact text, or brand identity without review. |

[Character Builder announcement](https://openart.ai/blog/character-builder-pr/) · [Worlds announcement](https://openart.ai/blog/openart-worlds-press-release/)

### OpenArt’s current platform-level model and workflow facts

- The platform currently lists a dynamic aggregation of leading video/image models (marketing page re-read 2026-09-04): video picker Seedance 2.5, Seedance 2.0, Happy Horse, Kling 3.0, Wan 2.7, Veo 3.1; model library additionally Sora 2, SwitchX, LTX-2.3, PixVerse, Gemini Omni Flash, plus a separate **WAN 3.0** model page — so both WAN 2.7 and WAN 3.0 labels exist, read the live picker; image models GPT Image 2, Grok Imagine, Qwen Image 3, Nano Banana 2, Seedream 5.0 Pro. Clip length: usually ≤15 s, 20 s on LTX 2.3, 30 s on Seedance 2.5 only; **Extend Video** continues a shot by up to 10 s at a time; resolution up to 4K on many models, 1080p default. The presence of a name in the library does not make all of its modes/settings available in every tool.
- The former **OpenArt Workflows** (ComfyUI community workflow area) was sunset on **18 January 2026**. Do not recommend creating or editing an OpenArt Workflow as a current production route; use the suite’s current Tools, Director, or external ComfyUI instead. [Sunset notice](https://openart.ai/workflows/home)
- Commercial rights and premium models/longer/higher-quality renders are plan dependent. Read the active plan/terms; current public material says commercial rights apply on Advanced and above, but this is a purchase/legal check, not a creative inference. [Video FAQ](https://openart.ai/ai-video-generator/)

### OpenArt learning sources

- [OpenArt Tutorials](https://openart.ai/tutorials) — official video tutorials; dates/screens must still be cross-checked with the active product form.
- [Create Image guide, 27 Aug 2026](https://openart.ai/blog/how-to-generate-an-ai-image/)
- [Video tool hub](https://openart.ai/suite/video) and [Director guide](https://openart.ai/blog/how-to-use-openart-director/)
- [OpenArt updates](https://openart.ai/blog/category/updates/) — use this to detect shipped/replaced products.

---

## 5. Arcads — UGC/performance-ad production, not a generic video generator

> **Version scope:** `AR-WEB@2026-08-31`; the Getting Started flow cited below is dated 2 Jul 2026. The connector/API material is separately `AR-MCP@2026-06-26`; do not use a Studio/Mark/Workflow statement as an MCP feature without a live tool check.

### What Arcads is actually for

Arcads is a connected **creative-testing and UGC-ad** workspace. Its current product model is: product/campaign context → actors, images, B-roll and ad scenes → localization/variations → reviewed outputs or reusable workflow. It can contain third-party image/video models, but its actor, script, product-placement, subtitle, translation and batch controls belong to **Arcads**, not to those underlying models. An agent must therefore not relabel an Arcads ad feature as “a Seedance setting” or suggest Arcads for a conventional narrative-film workflow merely because it has B-roll/video generation. [Current platform overview](https://www.arcads.ai/) · [Getting Started, 2 July 2026](https://intercom.help/arcads/en/articles/14531683-getting-started-with-arcads)

The current platform has three higher-level routes with different ownership:

| Surface | What the user supplies/chooses | Correct agent interpretation |
|---|---|---|
| **Studio / project** | Product image, image-generation model, scene prompt, selected image/output and downstream ad tools. Arcads auto-detects the uploaded product in its getting-started flow. | The product asset is the campaign anchor. Use it before asking a model to invent packaging, logo, or product details. |
| **Mark Agent** | Product site/assets, brand and audience information, competitor or winning-ad references, then a campaign request. | A conversational campaign-production route: Mark proposes angles/hooks/scripts, selects actors/scenes and produces an assembled UGC ad. It is not a reason to skip approval of factual claims, brand voice, product depiction, or the final ad. |
| **Workflows** | Explicit input/model/tool nodes, connected assets/prompts/actors, then Run. | A reusable batch pipeline. Treat each node’s visible input/output ports as canonical; do not assume that a Studio or Mark control exists as a node, or vice versa. |

[Mark Agent workflow](https://agent.arcads.ai/) · [Workflow feature guide](https://intercom.help/arcads/en/articles/15393713-what-is-the-workflow-feature)

### Arcads: which form owns which user choice

| User objective | Correct current route and verified direct choices | Do not transfer it to |
|---|---|---|
| Create product/lifestyle stills | **New Project → product upload → image generation**: product image, scene prompt, selected image model; the current flow also offers Prompt Builder and downstream changes to colours/background/elements. | Talking Actor, B-roll, or a generic Seedance/FLUX request without first checking the active model form. |
| Make a person deliver a UGC script | **Talking Actor**: choose a character from the generated image, choose a library voice or clone a voice, add script, optionally let Arcads add emotions, and preview audio before full video. | Animated Actor movement or a generic video model. The actor/script/voice/emotion form is its own surface. |
| Give the actor body/action movement | **Animated Actors**: select the visible movement model (current examples: Clean, Dance, Work), then its duration/aspect-ratio fields; after generation, voice/captions can be swapped. | Talking Actor speech settings, B-roll camera generation, or Cinema Studio camera controls. |
| Produce a product cutaway | **B-roll**: start from a product image, describe the shot, select the active B-roll model, then use that form’s short-clip/batch controls. The current guide gives Seedance 2.0 only as an example, not as a platform default. | Actor/voice/emotion options or a claim that every Arcads model exposes the same controls. |
| Localize an approved ad | **Translate**: choose target language and accent; Arcads describes automatic lip-motion matching. Review the language, claims and lip-sync result per locale. | A new Talking Actor or a text-only translation that is assumed to edit the old video automatically. |
| Generate many creative tests | **Workflow**: choose nodes, connect them, run the pipeline; current examples reuse a product image, script and character avatars across actors/languages. | A promise that an ad Agent/Studio generation will automatically preserve every node-level parameter. |

### Safe ad-production loop for an agent

1. Establish the **campaign boundary**: product, market, approved benefit/offer, audience, platform format, brand restrictions, and whether real-person likeness/voice is authorized.
2. Upload/select the approved product asset and decide the execution: product still, Talking Actor UGC, Animated Actor, B-roll, or a complete Mark/Workflow batch.
3. Set choices only in the selected route’s live form. In particular, choose **actor + voice + script** in Talking Actor; choose **movement** in Animated Actors; choose **model + shot description** in B-roll; choose **locale/accent** in Translate.
4. Review one ad for product accuracy, spoken wording, subtitles, actor/voice appropriateness, localization and visual continuity before generating a batch. Neither a good source product image nor an automated emotion pass approves advertising claims.
5. For scale, turn the approved structure into a Workflow and keep the product, script, actor set, locale and output set explicit at the workflow inputs. Review the batch before publish/export.

### Agent/MCP boundary

Arcads now offers a hosted MCP endpoint as an integration path, in addition to its browser surfaces and public API. It requires an Arcads account and an active subscription with remaining credits; a connected agent must retain the same review/credit boundary as a user in Studio. Current public MCP material advertises operations such as competitor-ad analysis and adapting a hook/static ad, but that is a capability description—not permission to make unverified comparative claims, use an unlicensed likeness/creative, or publish without approval. [Arcads MCP help](https://intercom.help/arcads/en/articles/15655699-arcads-mcp) · [Arcads API guide](https://intercom.help/arcads/en/articles/10538922-arcads-ai-api-documentation)

### Arcads learning sources

- [Arcads Help Centre: complete platform guide collection](https://intercom.help/arcads/en/collections/7500987-how-to-use-arcads-platform)
- [Getting Started walkthrough](https://intercom.help/arcads/en/articles/14531683-getting-started-with-arcads) — current UI baseline; recheck the selected model/mode form.
- [Workflow Feature](https://intercom.help/arcads/en/articles/15393713-what-is-the-workflow-feature) — current node/batch concepts and examples.
- [MCP documentation](https://intercom.help/arcads/en/articles/15655699-arcads-mcp) — integration only; does not replace user approval.

---

## 6. Cross-platform workflow routing

> **Version scope:** This is a routing synthesis, not a new platform version. Each row inherits the named platform/surface key from the version ledger; an agent must output that key when applying a row to a real generation.

### What to choose for the actual user request

| User needs | Best first route | Why | Do not promise |
|---|---|---|---|
| Test the same source/prompt against several models, compare cost, then integrate in code | **fal Sandbox → specific Playground → API** | This is fal’s purpose-built comparison/reproducibility flow. | A shared set of model controls or a video-edit timeline. |
| Create or precisely revise a still in a conversational workspace | **ChatGPT native GPT Image 2 (`gpt-image-2`)** | It supports prompt-led reference use and iterative follow-up edits in one chat. | A native video render, external provider workspace, or API-only output controls. |
| Generate a provider image/video without leaving an MCP-capable chat/agent | **Named provider MCP**, after provider sign-in, workspace and credits are verified | MCP can be a direct alternative generation path; it returns provider outputs into the agent conversation and/or provider library. | Web-UI parity, a matching ChatGPT plan/account, free/unlimited web access, or an unexposed feature such as OpenArt Smart Shot. |
| Direct a cinematic shot with direct film-grammar settings, shared cast/assets, and a project context | **Higgsfield Cinema Studio 4.0** | Genre/era/tempo/light/camera/lens/aperture/Emotion Wheel are native UI controls. | 4K/one-minute output until the active dropdown confirms it. |
| Generate a controlled still and animate it with one current Runway model | **Runway Tool Mode: Gen-4 Image → Use → Gen-4.5 I2V** | The output handoff and reference process are documented. | Gen-4.5 start/end frames, video editing, or arbitrary external reference modes. |
| Replace/re-light/restyle/remove something in a short source video | **Runway Edit Studio** or the matching **OpenArt Video** edit tool | Both expose dedicated edit routes; use source constraints to choose. | That an arbitrary long/high-FPS/multi-cut clip will upload successfully. |
| Animate a character’s actual performance from an actor/driving clip | **Runway Act-Two** | It explicitly maps driving performance to character image/video and has gesture rules. | A full-body, multi-character, cut-heavy performance transfer without testing. |
| Make a multi-shot scene without hand-assembling every shot | **OpenArt Smart Shot** or **Runway Multi-Shot App** | Both are explicitly structured multi-shot modes; OpenArt shows a Shot Plan, Runway states up to five shots. | A conventional editable timeline from either generator. |
| Take a concept to an AI-assembled story/campaign/short video by conversation | **OpenArt Director** or **Runway Agent** | Both are chat-based planning/production surfaces, with different asset/timeline approaches. | Autonomous final approval or guaranteed cross-scene continuity. |
| Produce testable UGC/ad variations from product assets, actors, scripts and locales | **Arcads Studio → Talking/Animated Actor or B-roll → Workflow**; use **Mark** where a campaign-level conversational route is wanted | Its asset, actor, localization and batch surfaces are designed for creative testing. | Cinema-Studio film controls, generic model parity, unreviewed advertising claims, or automatic publication. |
| Preserve a recurring person/location/brand in OpenArt | **Character / World / Brand Kit** then the selected shot tool | This uses the suite’s persistent asset model. | Exact text/logo rendering or a model’s undocumented reference support. |
| Need geometry-consistent location views | **OpenArt World → captured keyframes**; otherwise external 3D/blockout | World is a navigable persistent scene and captured output can seed video. | Current export to mesh/splats; it is not shipped in the cited source. |

### Continuity strategy by platform

| Platform | Agent-safe continuity mechanism |
|---|---|
| Higgsfield | Create/reuse Elements and Soul/AI Cast assets inside one project; add relevant references; use one project brief and shot folders. |
| fal.ai | Host/preserve canonical assets yourself and pass the URLs/files the selected endpoint accepts. The API result is a response with media URLs, not a film bible. |
| Runway | Create neutral character/environment plates; tag up to three reusable Gen-4 image References; store in Assets; animate approved stills. |
| OpenArt | Save Character, World, Brand Kit, and Media assets; attach them in the selected tool or tag them in Director. |
| Arcads | Retain the approved product asset, actor/voice choice, script, locale and winning creative structure; make all of them explicit Workflow inputs when scaling. |
| ChatGPT native | Keep the approved image and its reference/prompt context in the conversation while iterating; deliberately download/attach the final still when another provider must use it. |

### A universally safe production loop

1. Define a shot and its intended output shape/length before entering a generator.
2. Establish identity/location/style in a still or persistent asset first.
3. Use the platform’s own continuity/reference channel, not only prose.
4. Select the model **after** choosing the platform/surface and inspect the live settings that remain.
5. Make short validated clips; review in the six passes of post-audio-legal ch. 19 (identity → continuity → timing → camera → audio → style; geography and light are the continuity pass, editability = ENDING STATE reached).
6. Use a dedicated edit/extend route for a local defect; regenerate only where the model/surface cannot make the repair.
7. Assemble longer work in the platform’s stated sequence surface (Higgsfield project/tempo, Runway Timeline Studio/Agent, OpenArt Director/Smart Shot) or a conventional editor as appropriate.

---

## 7. Secondary-source audit: tutorials, blogs, and YouTube

Primary product documentation is the authority for current UI, limits, plan access, and cost. The following external/tutorial pass was still useful as a **staleness check**, not as a replacement authority.

| Source checked | Date / status | How it was used |
|---|---|---|
| [StackPicks: Higgsfield tutorial](https://stackpicks.dev/blog/how-to-use-higgsfield-ai-tutorial-2026) | Updated 16 Aug 2026 | Explicitly **not** used for feature facts: it claims 5–8-second clips and older preset counts, contradicting Higgsfield’s 12 Aug 4.0 guide (30 seconds, 30+ movements, 50 refs). This is the practical reason agents must reject even recent influencer/tutorial claims when the live primary source disagrees. |
| [OpenArt Image-to-Video YouTube tutorial](https://www.youtube.com/watch?v=r6k8EqCQzQY) | 7 Apr 2026 | Found as a beginner walkthrough. It can help a user see a basic upload→motion→generate flow, but it predates current Director, current suite navigation, and current model/tool list; no UI fact above depends on it. |
| [OpenArt official Tutorials](https://openart.ai/tutorials) | Current page | Preferred over third-party videos because it is maintained by the provider; still cross-check the screen/model dropdown. |
| [Runway Academy](https://academy.runwayml.com/) | Current | Preferred learning source for current Agent/Apps usage; current Help Centre remains the authority for constraints. |
| Higgsfield Academy / Creator Hub | Redesigned Aug 2026 | Preferred current learning source; the changelog records that old courses were retired in favour of video lessons/Keypoints. |
| [Arcads Getting Started](https://intercom.help/arcads/en/articles/14531683-getting-started-with-arcads) | 2 July 2026 | Preferred current walkthrough for product → image → Talking Actor/Animated Actor/B-roll/Translate/Workflow routing; it supersedes older avatar-only Arcads videos. |

**Research discipline:** an external walkthrough can contribute a user-experience observation only when it matches a current primary source. It cannot establish a technical limit, price, supported input, plan entitlement, model availability, or button name. Screens in videos age faster than prompts.

---

## 8. Maintenance protocol

This reference is intentionally dated. Re-verify the marked volatile areas before any production run and update the document with the primary URL and date:

- model dropdown contents, model-specific input forms, reference counts, duration/resolution/audio options;
- each MCP server URL, exposed tool/schema list, client transport, account/workspace authorization, result destination and MCP-only billing/plan exceptions; never infer web-UI parity from an integration announcement;
- ChatGPT native image availability and the current `gpt-image-2`/Image API/Responses API boundaries; distinguish ChatGPT plan/workspace limits from API credentials and billing;
- Arcads actor/voice/model/movement/localization forms, Mark abilities, Workflow node ports, MCP/API scope and credit requirements;
- all plan, credit, export, and commercial-use claims;
- current product names, especially Higgsfield Cinema Studio release names and Runway Apps;
- Higgsfield standalone perspective/storyboard tools referenced in production-pipeline ch. 9 and 16 (Angles, Shots, DoP, Popcorn, Start & End Frame, WAN Camera Control): confirm presence and current label in the live tool picker; if confirmed, add a row to the "What else the current Higgsfield UI can do" table with URL + date and replace the undated warning in ch. 16;
- release/retirement notices (Runway and OpenArt have recently retired entire prior surfaces);
- any claim of native 4K, multi-minute generation, “unlimited,” “perfect consistency,” autonomous generation, or third-party model parity.

When a source conflict remains unresolved—as with Higgsfield’s 30s/1080p documentation versus its 1min/native-4K marketing page (both still live on 2026-09-04)—record the conflict, use the lower verified capability as the working assumption, and ask the user to read the live control rather than guessing.

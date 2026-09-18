# Agent Models: Which Model Runs This Skill Well

Tags and confidence labels: legend in sources.md. Read this file when the director asks which model to run a session on, or before skill work is handed to a subagent or a batch run. Everything in the table is first-party measurement [PP 2026-09-18, registry entry in sources.md]: a fresh agent got only the task and the instruction to read SKILL.md first and then what the loading map names; it was judged on the delivery and on the files it actually opened. One run per cell — a result shows what a model CAN do with this skill, never a rate. Model versions age fast: a row is valid for the named version and for v3.5 of this skill.

## Measured

| Model (harness) | One prompt, Caption Spine (W3) | Dialogue prompt, block structure (W3) | New-project intake (W1) | Review of an over-instructed prompt | Loading discipline |
|---|---|---|---|---|---|
| Claude Fable 5.1 (Claude Code subagent) | passed, two runs — full slate, real lint count, a redundant reference left out with its reason | passed — ONE audio notation, the music exclusion as a plain sentence, relative timing, an acting block, two risk rows | passed — one grouped question, the full technique menu | passed | named parts only; of the other technique's chapter only the Lint paragraph |
| GPT-5.6 Sol, medium effort (Codex CLI) | passed, two runs — lint counts real | passed — ONE notation (prose with the quoted line), cause before reaction, the vendor-verbatim lock string | passed — one grouped question, the full technique menu, a reasoned recommendation, the draft-batch offer | not measured | the exact minimal set in one run; in another it opened files by their first hundred lines and saw more |
| GPT-5.6 Terra, medium effort (Codex CLI) | passed, two runs — lint counts within one word | passed with a flaw — one notation in the AUDIO block only after the rule said "never mix" in so many words; the spoken line was written a second time in ACTION | partial — one grouped question and a reasoned recommendation, but the alternatives of the menu were not listed | not measured | reads wider than the map names (look and reference-protocol files), never a large file whole |

Every other model and version: not measured.

## What follows for sessions and subagents (🟡 derived from single runs)

- **Lead session** — intake, the technique decision, canon questions, reviews, a repair that touches the rules: the strongest model the director has. The intake carries the decisions that are expensive to reverse, and the smaller of two same-family models dropped a decision duty exactly there. The same model followed a rule only once it was spelled out as a concrete do and don't — a skill rule that a mid-tier agent must follow states HOW, not only THAT.
- **Subagent or batch work on a running project** — shot prompts from an approved treatment, slates, lint, risk register: a mid-tier model is sufficient once the bible frame is complete (technique decided in bible section B1, assets registered, canon approved). Hand over: the bible frame, the canon passage, the Shot IDs, and the sentence "read SKILL.md first, then only what its loading map names". The lead session recounts the Lint row and re-reads every returned prompt against the canon (checklist step 5) before delivery.
- **Never delegated:** status moves, approvals and PROPOSAL picks (SKILL rules 12 and 14) — they wait for the director, not for another agent.
- **An unmeasured model or a new version:** before it works unattended, run the cold tests below once — a matter of minutes. Offer this once; the director decides.

## The cold-test protocol

Harness, verbatim: `Follow the skill exactly as an agent would when it is triggered: read SKILL.md first, then only what its loading map and routing tell you to read. Do not generate anything on any platform. Deliver exactly what the skill requires. At the end, list every file and chapter you actually read, in order.` Keep the wording identical across models: a sentence such as "the director cannot answer" switches the agent to the ASSUMED path of the interaction contract and tests something else.

- **Prompt test:** a running-project frame (technique decided, two or three registered @assets, one treatment passage) and "write the video prompt for shot X as a complete delivery". Passed when the agent read the runbook, the project's technique chapter, renderability §2–3 and the platform's section — no large file whole, no second technique chapter — and delivered a Render Slate with a Lint row that survives a recount, Crew choices in two halves, a receipt state, a risk register, and cause before reaction in the beats.
- **Dialogue test:** the same frame with technique B decided, two characters and one spoken line in the treatment. Passed when the AUDIO block uses ONE notation (video-prompting 12b), the music exclusion is a plain sentence, the speech count lock is present and the line is written once.
- **Intake test:** a rough idea with format, look and video model named, and "get me started". Passed when the agent read W1, the genre baseline and story-structures ch. 23a, and answered with ONE grouped question that holds the story-gate gaps and the technique menu — three entries, a recommendation with its reason, the draft-batch offer — with defaults marked ASSUMED and bible section B1 named as the place the decision is kept.
- Check the files opened against the harness's own log where it keeps one, and count the lint yourself: a self-reported reading list and a claimed word count are claims, not measurements.

# Evals: the cold tests as files

The three cold tests of `references/agent-models.md` (prompt test, dialogue test, intake test) in the evaluation shape of Anthropic's skill-authoring best practices: one entry per test with `query`, `files` and `expected_behavior`. `fixtures/` holds the fictional project frames the first two tests read as their bible; `SALTLINE` (technique A) and `WHEELHOUSE` (technique B) exist only here. This folder is repo-only: `.github/workflows/release.yml` excludes it from the `.skill` package.

## Harness

Every query opens with the harness sentence of `agent-models.md`, verbatim. Keep that wording identical across models and runs: a sentence such as "the director cannot answer" switches the agent to the ASSUMED path of the interaction contract and tests something else. A fresh agent gets only the query; it reads the skill from the working directory, not from an installed copy.

## Run

Claude, read-only, lean session (the model alias picks the latest version; the stream log records every file read):

```bash
claude -p "$(jq -r '.evals[0].query' evals/evals.json)" --model sonnet \
  --tools Read,Glob,Grep --setting-sources project --strict-mcp-config \
  --no-session-persistence --verbose --output-format stream-json > ../eval-1-sonnet.jsonl
```

Codex (GPT), read-only, from the repo root; the run log records every `sed -n` call:

```bash
timeout 900 codex exec "$(jq -r '.evals[0].query' evals/evals.json)" --sandbox read-only --ephemeral \
  --model gpt-5.6-sol -c model_reasoning_effort=medium -o ../eval-1-sol.md < /dev/null > ../eval-1-sol.log 2>&1
```

In a Claude Code session whose shell CLI is not logged in (Desktop or SDK-hosted sessions authenticate through the host, and a nested `claude -p` then fails with an expired OAuth session), run the query as a native subagent with a model override instead: give it the query, the absolute path of the skill checkout and the instruction to use only Read, Glob and Grep; its transcript lands in the session's `tasks/` folder and yields the same read log with the jq filter below.

Pull the delivery and the read log out of a Claude stream:

```bash
jq -r 'select(.type=="result") | .result' ../eval-1-sonnet.jsonl
jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="tool_use") | "\(.name) \(.input.file_path // .input.pattern // "") \(.input.offset // "") \(.input.limit // "")"' ../eval-1-sonnet.jsonl
```

## Judge

- Check every `expected_behavior` line against the delivery. The first line of each eval (what was read) is scored separately as loading discipline, the way the table in `references/agent-models.md` keeps it in its own column; the remaining lines decide pass/fail, and a test passes only when all of them hold.
- A self-reported reading list and a claimed word count are claims, not measurements: compare the list against the harness's own read log, and recount the Lint row with `python3 scripts/lint_prompt.py <file>` (from the skill checkout) on the fenced prompt.
- One to three runs per cell; a result shows what a model CAN do with this skill, never a rate. Record the outcome as a row in the table of `references/agent-models.md` and the run as a dated [PP] entry in `references/sources.md`.
- Re-run after a change to the always-rules, the loading map or the per-prompt checklist; a row measured on an older SKILL.md revision is cited with that caveat.

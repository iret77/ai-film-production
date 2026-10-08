#!/usr/bin/env python3
"""Count the seven-measure Lint row of a VIDEO prompt (video-prompting.md ch. 12h).

Usage
  python3 scripts/lint_prompt.py prompt.txt         # the fenced prompt, fences optional
  python3 scripts/lint_prompt.py < prompt.txt       # or on stdin
  python3 scripts/lint_prompt.py --json prompt.txt  # machine-readable

What it decides and what it only shows
  Machine-counted: words · prohibition sentences (negations) · numerals outside the
  12h exceptions · absolute measures · timeline continuity of the timecode beats.
  Shown as CHECK, never decided here: a numeral that is a deliberate look control,
  a double-mention candidate (the closing image restates the last frame by contract),
  a prohibition clause inside a reference line (a scoping clause does not count, an
  exclusion after a non-transfer counts once), contradictions (12h checks 1, 5, 6),
  and whether every beat carries its event, end state and an action per character.

Exit code 0 when every machine-counted measure holds, 1 when one fails, so the
repair loop of SKILL rule 15 (remove → change → add, never longer) can gate on it.
Python 3.8+, standard library only. Still prompts use the ch. 24i checks instead.
"""

import json
import re
import sys

# ---------------------------------------------------------------------------
# Conventions (each one justified; change the rule in ch. 12h first, then here)
# ---------------------------------------------------------------------------

# A whitespace token is a word only when it carries a letter or a digit: standalone
# dashes, bullets and fence characters are layout, and `words n` exists to compare
# one revision with the one before (SKILL rule 15), so the convention only has to be
# stable and visible.
WORD_CHAR = re.compile(r"[^\W_]", re.UNICODE)

# Technique B prompts open every block with an upper-case label and a colon
# (SCENE CONTEXT:, ACTIVE REFERENCES:, FIRST FRAME/BLOCKING:, OPTICS+CAMERA:).
BLOCK_LABEL = re.compile(r"^([A-Z][A-Z0-9 /+&\-]{2,40}):\s*(.*)$")

# Technique C carries its one negation as the terminal MUST NOT APPEAR list.
MUST_NOT_APPEAR = re.compile(r"\bMUST NOT APPEAR\b", re.IGNORECASE)

# A prohibition sentence bans something. "without" and "cannot" are left out on
# purpose: in a scene description they describe far more often than they ban.
PROHIBITION = re.compile(
    r"\b(no|never|not|nothing|none|don't|do not|must not|mustn't|avoid)\b", re.IGNORECASE
)

# A reference line addresses an attached reference; its scoping clause ("timbre and
# manner only; do not reuse its words") is not a negation (12h), while an exclusion
# written after a logged non-transfer counts once. The script cannot tell them
# apart, so it reports both as CHECK and counts neither.
REFERENCE_LINE = re.compile(r"^\s*@\w+")
REFERENCE_BLOCKS = {"ACTIVE REFERENCES"}

# Timecode forms the vendor documents (ch. 14): ranges "0–3 s", "0-3s", "0:00–0:08",
# "[0–4 s]", "00:00-00:03"; a time point "at 4 s". A dash of any kind separates.
_T = r"\d{1,2}(?::\d{2})?(?:\.\d)?"  # 4 · 0:04 · 4.0
# No leading or trailing whitespace is consumed: a timecode at a line start must
# not swallow the newline, or two beats would be read as one sentence.
TC_RANGE = re.compile(r"\[?" + _T + r"[ \t]*(?:–|-|—|to)[ \t]*" + _T + r"(?:[ \t]*(?:s|sec|seconds))?\b(?:[ \t]*\])?", re.IGNORECASE)
TC_POINT = re.compile(r"\b(?:at|by|from|until|till)\s+" + _T + r"\s*(?:s|sec|seconds)\b", re.IGNORECASE)

# Numerals that are not numbers (12h): a fixed term, an @tag, a shot label, the take's
# duration in the title sentence or the FORMAT MODE line, a vendor-verbatim lock string.
NOT_A_NUMBER = [
    re.compile(r"\b[23]D\b"),
    re.compile(r"@\w*\d\w*"),
    re.compile(r"@(?:Image|Video|Audio|Clay Render)\s*\d+", re.IGNORECASE),  # the vendor's literal token
    re.compile(r"\bshots?\s*\d+[A-Za-z]?(?:\s*(?:,|and|&|to|–|-)\s*\d+[A-Za-z]?)*\b", re.IGNORECASE),
    re.compile(r"\bTK\d+\b"),
    re.compile(r"\b100\s?%\s+matches\s+the\s+reference\b", re.IGNORECASE),
]
DURATION = re.compile(r"\b(\d{1,2})\s*(?:-|–|\s)?\s*(?:s|sec|second|seconds)\b", re.IGNORECASE)
VENDOR_LOCK_SENTENCES = {"100% matches the reference"}

# Absolute measures (SKILL rule 7): a size or distance in units. Lens millimetres,
# Kelvin and f-stops are look controls, not measures: they stay numerals (CHECK).
NUMBER_WORDS = (
    r"a|an|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|"
    r"twenty|thirty|forty|fifty|sixty|hundred|half a|a few|several|some"
)
_UNITS = (
    r"(?:m|cm|km|metres?|meters?|centimetres?|centimeters?|kilometres?|kilometers?|"
    r"ft|feet|foot|inch|inches|yards?|miles?|body[- ]lengths?|paces|steps|storeys?|stories)\b"
)
# Digits may touch the unit ("2m"); a number word needs a space ("five metres"),
# otherwise "aft" reads as "a ft".
MEASURE = re.compile(
    r"\b(?:\d+(?:[.,]\d+)?\s*" + _UNITS + r"|(?:" + NUMBER_WORDS + r")\s+" + _UNITS + r")",
    re.IGNORECASE,
)
MEASURE_FALSE_FRIENDS = re.compile(r"\b\d+\s*(?:m|s)\s*(?:in|ms)\b|\bsteps? (?:back|forward|aside|in|out|up|down|toward|towards|away)\b", re.IGNORECASE)

# A repeated run of this many words inside two different sentences is a
# double-mention candidate. Six keeps house phrases ("the camera holds still")
# out and catches a sentence said twice in other words.
NGRAM = 6

SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[\"'“”A-Z@\[(0-9])")
QUOTED = re.compile(r"[\"“][^\"”]*[\"”]")


def words(text):
    return sum(1 for tok in text.split() if WORD_CHAR.search(tok))


def strip_fences(text):
    lines = [ln for ln in text.splitlines() if not ln.strip().startswith("```")]
    return "\n".join(lines).strip()


def split_blocks(text):
    """Return (technique, blocks) with blocks as [(label or None, text)]."""
    blocks, label, buf = [], None, []
    labelled = 0
    for ln in text.splitlines():
        m = BLOCK_LABEL.match(ln)
        if m:
            if buf:
                blocks.append((label, "\n".join(buf)))
            label, buf = m.group(1).strip(), [m.group(2)]
            labelled += 1
        else:
            buf.append(ln)
    if buf:
        blocks.append((label, "\n".join(buf)))
    if MUST_NOT_APPEAR.search(text):
        technique = "C"
    elif labelled >= 3:
        technique = "B"
    else:
        technique = "A"
    return technique, blocks


def sentences(text):
    out = []
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        out.extend(s.strip() for s in SENTENCE_END.split(ln) if s.strip())
    return out


def lint(raw):
    text = strip_fences(raw)
    technique, blocks = split_blocks(text)
    report = {"technique": technique, "words": words(text)}
    findings = []

    # --- negations -------------------------------------------------------
    counted, reference_clauses = [], []
    blocks_with_ban = set()
    c_list_seen = False
    for idx, (label, body) in enumerate(blocks):
        for s in sentences(body):
            probe = QUOTED.sub("", s)  # a quoted dialogue line is canon, never a ban
            if not PROHIBITION.search(probe):
                continue
            if technique == "C" and (MUST_NOT_APPEAR.search(s) or c_list_seen):
                c_list_seen = True
                blocks_with_ban.add("MUST NOT APPEAR")
                counted.append(s)
                continue
            if (label in REFERENCE_BLOCKS) or REFERENCE_LINE.match(s):
                reference_clauses.append(s)
                continue
            counted.append(s)
            blocks_with_ban.add(label if label else idx)
    if technique == "B":
        negations = len(blocks_with_ban)  # once per governing block (12h)
    elif technique == "C":
        negations = 1 if blocks_with_ban else 0  # the terminal list is the one negation
    else:
        negations = len(counted)
    report["negations"] = negations
    for s in counted:
        findings.append(("negation", s))
    for s in reference_clauses:
        findings.append(("CHECK reference-line clause (scoping = not counted; exclusion after a non-transfer = counts once)", s))

    # --- numerals outside the exceptions --------------------------------
    scrubbed = text
    first_sentence = sentences(text)[0] if sentences(text) else ""
    duration = None
    for label, body in blocks:
        if label == "FORMAT MODE":
            m = DURATION.search(body)
            if m:
                duration = int(m.group(1))
                scrubbed = scrubbed.replace(m.group(0), " ", 1)
    m = DURATION.search(first_sentence)
    if m and duration is None:
        duration = int(m.group(1))
    if m:
        scrubbed = scrubbed.replace(m.group(0), " ", 1)
    for pat in NOT_A_NUMBER:
        scrubbed = pat.sub(" ", scrubbed)
    scrubbed = TC_RANGE.sub(" ", scrubbed)
    scrubbed = TC_POINT.sub(" ", scrubbed)
    numerals = []
    for s in sentences(scrubbed):
        for n in re.findall(r"\d+(?:[.,:]\d+)?%?", s):
            numerals.append((n, s))
    report["numerals_outside_tc"] = len(numerals)
    for n, s in numerals:
        findings.append(("CHECK numeral %s — a look control named in Crew choices, or a fault" % n, s))

    # --- absolute measures ----------------------------------------------
    measures = []
    for s in sentences(text):
        probe = MEASURE_FALSE_FRIENDS.sub(" ", s)
        for m2 in MEASURE.finditer(probe):
            measures.append((m2.group(0), s))
    report["absolute_measures"] = len(measures)
    for m2, s in measures:
        findings.append(("absolute measure '%s' — write a visible relation between two things in the frame (SKILL rule 7)" % m2, s))

    # --- double mentions --------------------------------------------------
    def normalise(s):
        return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", s.lower())).strip()

    vendor_keys = {normalise(v) for v in VENDOR_LOCK_SENTENCES}
    norm = []
    for s in sentences(text):
        key = normalise(s)
        if key and key not in vendor_keys:
            norm.append((key, s))
    doubles = []
    seen = {}
    for key, s in norm:
        if key in seen:
            doubles.append(("sentence repeated", s))
        seen[key] = s
    # Reference lines repeat a fixed shape by contract, and the closing image restates
    # the last frame by contract, so neither feeds the repeated-phrase search.
    closing = set()
    for label, body in blocks:
        if label == "ENDING STATE":
            closing.update(normalise(s) for s in sentences(body))
    closing.update(normalise(s) for s in sentences(text) if s.lower().startswith("end with"))
    reference_keys = set()
    for label, body in blocks:
        for s in sentences(body):
            if label in REFERENCE_BLOCKS or REFERENCE_LINE.match(s):
                reference_keys.add(normalise(s))
    grams = {}
    for key, s in norm:
        if key in closing or key in reference_keys:
            continue
        toks = key.split()
        for i in range(len(toks) - NGRAM + 1):
            g = " ".join(toks[i:i + NGRAM])
            if g in grams and grams[g] != s:
                doubles.append(("'%s' also in: %s" % (g, grams[g]), s))
                break
            grams.setdefault(g, s)
    report["double_mention_candidates"] = len(doubles)
    for why, s in doubles:
        findings.append(("CHECK double mention (%s; the End with / ENDING STATE sentence restates the last frame by contract)" % why, s))

    # --- beats: timeline continuity --------------------------------------
    # Every range in the text, in order; a reference line may MENTION a shot's range
    # and a multi-shot take restates its shot ranges, so the beats are the longest
    # chain that starts at 0 and continues where the previous beat ended; ranges
    # that do not fit the chain are mentions, not beats.
    ranges = []
    for m3 in TC_RANGE.finditer(text):
        nums = re.findall(_T, m3.group(0))
        if len(nums) >= 2:
            ranges.append((to_seconds(nums[0]), to_seconds(nums[1])))
    timeline_ok = True
    timeline_note = "no timecode beats found"
    if ranges:
        problems = []
        chain = []
        for a, b in ranges:
            if b <= a:
                problems.append("beat %s–%s ends before it starts" % (fmt(a), fmt(b)))
                continue
            if not chain and a == 0:
                chain.append((a, b))
            elif chain and a == chain[-1][1]:
                chain.append((a, b))
        if not chain:
            problems.append("no beat starts at 0 s (first range found: %s–%s)" % (fmt(ranges[0][0]), fmt(ranges[0][1])))
        elif duration is not None and chain[-1][1] != duration:
            problems.append("the beats run consecutively to %s s, the take is %s s — a gap, or a beat missing" % (fmt(chain[-1][1]), duration))
        timeline_ok = not problems
        timeline_note = "consecutive, %s beats, %s s" % (len(chain), fmt(chain[-1][1])) if timeline_ok else "; ".join(problems)
    report["timeline"] = timeline_note
    report["duration"] = duration

    # --- verdict ----------------------------------------------------------
    fails = []
    if negations > 1:
        fails.append("negations %d/1" % negations)
    if measures:
        fails.append("absolute measures %d/0" % len(measures))
    if not timeline_ok:
        fails.append("beats: " + timeline_note)
    report["fails"] = fails
    report["findings"] = findings
    report["lint_row"] = (
        "words %d · negations %d/1 · numerals outside TC %d/0 · absolute measures %d/0 · "
        "double mentions %s · contradictions <read: 12h checks 1, 5, 6> · beats %s"
        % (
            report["words"], negations, len(numerals), len(measures),
            "none" if not doubles else "<CHECK %d>" % len(doubles),
            "complete" if timeline_ok and ranges else ("<CHECK: %s>" % timeline_note if ranges else "<CHECK: no timecodes>"),
        )
    )
    return report


def to_seconds(tok):
    if ":" in tok:
        m, s = tok.split(":", 1)
        return int(m) * 60 + float(s)
    return float(tok)


def fmt(seconds):
    return ("%g" % seconds)


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv[1:] if not a.startswith("--")]
    if paths:
        try:
            with open(paths[0], encoding="utf-8") as fh:
                raw = fh.read()
        except FileNotFoundError:
            sys.stderr.write("lint_prompt: no file at %s — pass the prompt file or pipe the prompt on stdin\n" % paths[0])
            return 2
    else:
        raw = sys.stdin.read()
    if not raw.strip():
        sys.stderr.write("lint_prompt: the prompt is empty\n")
        return 2
    report = lint(raw)
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("technique %s (detected) · duration %s" % (report["technique"], "%s s" % report["duration"] if report["duration"] else "not found"))
        print("Lint: " + report["lint_row"])
        if report["findings"]:
            print("\nFindings (one line each: measure — sentence):")
            for why, s in report["findings"]:
                print("- %s\n    %s" % (why, s))
        print("\nResult: " + ("PASS on the machine-counted measures" if not report["fails"] else "FAIL — " + "; ".join(report["fails"])))
        print("Still yours to read: contradictions (12h checks 1, 5, 6); each CHECK line above; every beat has one event, its end state and an action for every character it names.")
    return 1 if report["fails"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

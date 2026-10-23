#!/usr/bin/env python3
"""Combine the validation batch tables into one scoreboard.

Reads the batch summary table at the top of each
``validation_B*.md`` file, recomputes Sellability (mean of S1-S8) and
Overall (0.6 x Sellability + 0.4 x P) to catch arithmetic slips, and writes:

- research_notes/.../validation_scoreboard.md (sorted by Overall)
- data/saas_ideas_validated.csv

Usage: python3 scripts/build_scoreboard.py
"""

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "research_notes" / "Spanish SME pain points SaaS ideas"
DATA = ROOT / "data"

IDEA_ID_RE = re.compile(r"IDEA-(\d+)")
NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")
SCORES = [f"S{i}" for i in range(1, 9)]
COLUMNS = ["rank", "id", "name", "type", "verdict", "verdict_note", *SCORES,
           "sellability", "P", "overall", "confidence", "batch", "check"]
VERDICT_RE = re.compile(r"^\W*(GO|RESHAPE|KILL)\W*(.*)$", re.IGNORECASE)


def cells(line):
    return [c.strip().strip("*").strip() for c in line.strip().strip("|").split("|")]


def header_map(header):
    mapping = {}
    for index, raw in enumerate(header):
        name = raw.lower().replace("*", "").strip()
        score = re.fullmatch(r"s([1-8])\b.*", name)
        if score:
            mapping.setdefault(f"S{score.group(1)}", index)
        elif name in ("id", "idea") or name.startswith("idea id"):
            mapping.setdefault("id", index)
        elif name.startswith("name") or name == "idea name":
            mapping.setdefault("name", index)
        elif name.startswith("type"):
            mapping.setdefault("type", index)
        elif name.startswith("verdict"):
            mapping.setdefault("verdict", index)
        elif name.startswith("sell"):
            mapping.setdefault("sellability", index)
        elif name == "p" or name.startswith("p ") or "severity" in name:
            mapping.setdefault("P", index)
        elif name.startswith("overall"):
            mapping.setdefault("overall", index)
        elif name.startswith("conf"):
            mapping.setdefault("confidence", index)
    return mapping


def number(text):
    match = NUMBER_RE.search(text or "")
    return float(match.group()) if match else None


def parse_batch(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = []
    for i, line in enumerate(lines):
        if not line.startswith("|") or "S1" not in line or "verall" not in line:
            continue
        mapping = header_map(cells(line))
        for row_line in lines[i + 2:]:
            if not row_line.startswith("|"):
                break
            row = cells(row_line)
            idea = IDEA_ID_RE.search(row[mapping.get("id", 0)])
            if not idea:
                continue
            get = lambda key: row[mapping[key]] if key in mapping and mapping[key] < len(row) else ""
            verdict = VERDICT_RE.match(get("verdict").replace("*", ""))
            entry = {"id": f"IDEA-{int(idea.group(1)):02d}", "name": get("name"),
                     "type": get("type"),
                     "verdict": verdict.group(1).upper() if verdict else get("verdict"),
                     "verdict_note": verdict.group(2).strip(" ,;:()") if verdict else "",
                     "confidence": get("confidence").lower(), "batch": path.stem}
            for key in SCORES + ["sellability", "P", "overall"]:
                entry[key] = number(get(key))
            rows.append(entry)
        if rows:
            break  # only the batch summary table
    return rows


def main():
    rows = []
    for path in sorted(NOTES.glob("validation_B*.md")):
        rows += parse_batch(path)
    for row in rows:
        scores = [row[k] for k in SCORES]
        problems = []
        if None not in scores and row["P"] is not None:
            sellability = round(sum(scores) / 8, 2)
            overall = round(0.6 * sellability + 0.4 * row["P"], 2)
            if row["sellability"] is None or abs(sellability - row["sellability"]) > 0.05:
                problems.append(f"sellability {row['sellability']}→{sellability}")
            if row["overall"] is None or abs(overall - row["overall"]) > 0.05:
                problems.append(f"overall {row['overall']}→{overall}")
            row["sellability"], row["overall"] = sellability, overall
        else:
            problems.append("missing scores")
        row["check"] = "; ".join(problems) or "ok"
    rows.sort(key=lambda r: -(r["overall"] or 0))
    for rank, row in enumerate(rows, 1):
        row["rank"] = rank

    DATA.mkdir(exist_ok=True)
    with open(DATA / "saas_ideas_validated.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    fmt = lambda v: "" if v is None else (f"{v:g}" if isinstance(v, float) else str(v))
    verdicts = Counter(r["verdict"] or "?" for r in rows)
    lines = [
        "# Validation scoreboard",
        "",
        "All validated ideas from `validation_B*.md`, sorted by Overall score. Built by",
        "`scripts/build_scoreboard.py`, which recomputes Sellability (mean of S1–S8) and",
        "Overall (0.6 × Sellability + 0.4 × P); the Check column flags any recomputed value.",
        "This is the validation-stage order, before the adversarial review.",
        "",
        f"**{len(rows)} ideas.** Verdicts: " + ", ".join(
            f"{v} {n}" for v, n in verdicts.most_common()) + ".",
        "",
        "| Rank | ID | Name | Type | Verdict | Verdict note | " + " | ".join(SCORES)
        + " | Sell. | P | Overall | Conf. | Batch | Check |",
        "|" + "---|" * (len(COLUMNS)),
    ]
    for row in rows:
        lines.append("| " + " | ".join(fmt(row[c]) for c in COLUMNS) + " |")
    (NOTES / "validation_scoreboard.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} ideas scored; verdicts {dict(verdicts)}")
    print("rows with recomputed or missing values:",
          [f"{r['id']} ({r['check']})" for r in rows if r["check"] != "ok"] or "none")


if __name__ == "__main__":
    main()

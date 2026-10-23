#!/usr/bin/env python3
"""Collect the stage 2 group outputs into two compact files.

- stage2_noise_log_combined.md: every pain point filtered out in stage 2,
  with its reason code, plus counts by code and by track.
- stage2_idea_index.md: one row per candidate idea (type, buyer, pains, price,
  moat, evidence strength) with a pointer to its full text in the group file.

Usage: python3 scripts/extract_stage2.py
"""

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "research_notes" / "Spanish SME pain points SaaS ideas"

REASONS = {
    "N1": "weak evidence",
    "N2": "not software-solvable",
    "N3": "regulation postponed, annulled, draft or lapse-prone",
    "N4": "already solved cheaply or saturated",
    "N5": "too niche or too small",
    "N6": "legally risky to automate",
    "N7": "duplicate of another pain",
}

NOISE_ROW_RE = re.compile(
    r"^\|\s*\**([A-Z]+-\d+)\**\s*\|(.*?)\|\s*\**(N[1-7])\b[^|]*\|(.*?)\|?\s*$")
IDEA_RE = re.compile(r"^### (G\d-I\d+):?\s*(.*?)\s*$")
FIELD_RE = re.compile(r"^- (?:\*\*)?([A-Za-z][^:*]{0,60}?)(?::\*\*|\*\*:|:)\s*(.*)$")
INDEX_FIELDS = {
    "type": "Type",
    "buyer": "Buyer",
    "pains addressed": "Pains",
    "price hypothesis": "Price",
    "moat in an ai-flooded market": "Moat",
    "evidence strength": "Evidence",
}


def clip(text, limit):
    text = " ".join(text.split()).replace("|", "/")
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def parse_group(path):
    noise, ideas = [], []
    in_noise = False
    idea = field = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            in_noise = "noise log" in line.lower()
            idea = field = None
            continue
        if in_noise:
            match = NOISE_ROW_RE.match(line)
            if match:
                noise.append((match.group(1), match.group(2).strip(),
                              match.group(3), match.group(4).strip(), path.name))
            continue
        match = IDEA_RE.match(line)
        if match:
            idea = {"id": match.group(1), "name": match.group(2), "file": path.name,
                    "line": number}
            ideas.append(idea)
            field = None
            continue
        if line.startswith("### "):
            idea = field = None
            continue
        if idea is None:
            continue
        match = FIELD_RE.match(line)
        if match:
            field = INDEX_FIELDS.get(match.group(1).strip().lower())
            if field:
                idea[field] = match.group(2).strip()
            continue
        if field and line.strip():
            idea[field] = idea.get(field, "") + " " + line.strip()
    return noise, ideas


def main():
    noise, ideas = [], []
    for path in sorted(NOTES.glob("stage2_G*.md")):
        group_noise, group_ideas = parse_group(path)
        noise += group_noise
        ideas += group_ideas

    noise.sort(key=lambda row: (row[0].split("-")[0], int(row[0].split("-")[1])))
    codes = Counter(row[2] for row in noise)
    tracks = Counter(row[0].split("-")[0] for row in noise)
    lines = [
        "# Stage 2 combined noise log",
        "",
        "Every pain point filtered out in stage 2, collected from the six group files",
        "(`stage2_G*.md`) by `scripts/extract_stage2.py`. Pain points not listed here were",
        "carried forward into idea clusters.",
        "",
        f"**{len(noise)} pain points filtered.**",
        "",
        "| Code | Reason | Count |",
        "|---|---|---|",
    ]
    lines += [f"| {code} | {REASONS[code]} | {codes[code]} |" for code in sorted(codes)]
    lines += ["", "Filtered per track: " + ", ".join(
        f"{track} {count}" for track, count in sorted(tracks.items())), ""]
    lines += ["| ID | Title | Code | Justification | Group file |", "|---|---|---|---|---|"]
    lines += [f"| {pid} | {clip(title, 120)} | {code} | {clip(why, 400)} | {src} |"
              for pid, title, code, why, src in noise]
    (NOTES / "stage2_noise_log_combined.md").write_text("\n".join(lines) + "\n",
                                                         encoding="utf-8")

    lines = [
        "# Stage 2 idea index",
        "",
        "One row per candidate idea from the six group files, extracted by",
        "`scripts/extract_stage2.py`. Fields are shortened; the full idea (problem, MVP,",
        "alternatives, channels, build notes, risks, validation questions) is in the",
        "group file at the line given.",
        "",
        f"**{len(ideas)} candidate ideas.**",
        "",
        "| ID | Name | Type | Buyer | Pains | Price | Moat | Evidence | Full text |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for idea in ideas:
        lines.append("| " + " | ".join([
            idea["id"], clip(idea["name"], 110), clip(idea.get("Type", ""), 60),
            clip(idea.get("Buyer", ""), 220), clip(idea.get("Pains", ""), 160),
            clip(idea.get("Price", ""), 140), clip(idea.get("Moat", ""), 160),
            clip(idea.get("Evidence", ""), 140), f"{idea['file']}:{idea['line']}",
        ]) + " |")
    (NOTES / "stage2_idea_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{len(noise)} filtered pain points, codes {dict(sorted(codes.items()))}")
    print(f"{len(ideas)} ideas: " + ", ".join(
        f"{g} {n}" for g, n in sorted(Counter(i['id'][:2] for i in ideas).items())))
    missing = [i["id"] for i in ideas if not all(k in i for k in INDEX_FIELDS.values())]
    print("ideas missing an index field:", missing or "none")


if __name__ == "__main__":
    main()

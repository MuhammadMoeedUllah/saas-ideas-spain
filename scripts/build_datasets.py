#!/usr/bin/env python3
"""Build structured datasets from the stage 1 research notes.

Parses every structured pain-point entry (``### TAX-01: title`` followed by
``- **Field:** value`` lines) in the research notes and writes them to
``data/pain_points.csv`` and ``data/pain_points.jsonl``. When stage 2 noise logs
exist, each entry also gets its stage 2 status (carried forward or the
filter reason code).

Usage: python3 scripts/build_datasets.py
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "research_notes" / "Spanish SME pain points SaaS ideas"
DATA = ROOT / "data"

TRACKS = {
    "TAX": "Tax, invoicing and accounting",
    "LAB": "Labour, HR, payroll and litigation",
    "ADM": "Bureaucracy, licensing, subsidies and procurement",
    "FIN": "Cash flow, finance, insurance and insolvency",
    "LEG": "Legal disputes, sanctions and compliance",
    "HOS": "Hospitality, tourism and short-term rentals",
    "RET": "Retail, e-commerce and personal services",
    "CON": "Construction, trades and real estate",
    "IND": "Transport, industry and agrifood",
    "PRO": "Clinics, professional services, education and care",
    "STA": "Startups and tech ecosystem",
    "CITY": "Cities and macro surveys",
    "VOX": "SME voices and software market",
    "HOU": "Mid-term housing and coliving",
    "EXP": "Expat and relocation bureaucracy",
    "ZBE": "Low-emission zones and fleets",
    "GAM": "Gaming, streaming and creators",
}

# Field labels used in the notes, mapped to dataset columns. The gaming track
# uses adapted labels for the same ideas.
FIELDS = {
    "who": "who",
    "where": "where",
    "day-to-day reality": "reality",
    "reality": "reality",
    "evidence": "evidence",
    "scale": "scale",
    "scale/cost": "scale",
    "cost/impact": "cost_impact",
    "money": "cost_impact",
    "driver & status": "driver_status",
    "how it is solved today": "solved_today",
    "how it is served today": "solved_today",
    "software-solvable?": "software_solvable",
    "opportunity type": "software_solvable",
    "confidence": "confidence",
}

COLUMNS = [
    "id", "track", "title", "who", "where", "reality", "evidence",
    "evidence_url_count", "evidence_urls", "scale", "cost_impact",
    "driver_status", "solved_today", "software_solvable", "confidence",
    "stage2_status", "source_file",
]

ENTRY_RE = re.compile(r"^### ([A-Z]+-\d+):\s*(.+?)\s*$")
# Labels appear as "- **Who:** x", "- **Who**: x" or "- Who: x" depending on the track.
# Some labels carry a qualifier, e.g. "Evidence (self-reported by vendors):".
FIELD_RE = re.compile(r"^- (?:\*\*)?([A-Za-z][^:*]{0,80}?)(?::\*\*|\*\*:|:)\s*(.*)$")
HEADING_RE = re.compile(r"^#{1,3} ")
URL_RE = re.compile(r"\]\((https?://[^)\s]+)\)")
# A noise-log table row: | PAIN-ID | ... | N1 | ...
NOISE_ROW_RE = re.compile(r"^\|\s*\**([A-Z]+-\d+)\**\s*\|.*?\|\s*\**(N[1-7])\b[^|]*\|")


def parse_notes(path):
    entries = []
    current = None
    field = None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ENTRY_RE.match(line)
        if match:
            current = {"id": match.group(1), "title": match.group(2),
                       "source_file": path.name}
            entries.append(current)
            field = None
            continue
        if current is None:
            continue
        if HEADING_RE.match(line):
            current, field = None, None
            continue
        match = FIELD_RE.match(line)
        if match:
            label = re.split(r"[(,]", match.group(1))[0].strip().lower()
            field = FIELDS.get(label)
            if field:
                current[field] = match.group(2).strip()
            continue
        if field and line.strip():
            current[field] = (current.get(field, "") + "\n" + line.strip()).strip()
    return entries


def parse_noise_logs():
    status = {}
    for path in sorted(NOTES.glob("stage2_*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = NOISE_ROW_RE.match(line)
            if match:
                status.setdefault(match.group(1), f"filtered {match.group(2)}")
    return status


def main():
    noise = parse_noise_logs()
    rows = []
    for path in sorted(NOTES.glob("*.md")):
        if path.name.startswith(("00_", "stage2_", "stage3_", "validation_")):
            continue
        for entry in parse_notes(path):
            prefix = entry["id"].split("-")[0]
            urls = list(dict.fromkeys(URL_RE.findall(entry.get("evidence", ""))))
            entry["track"] = TRACKS.get(prefix, prefix)
            entry["evidence_url_count"] = len(urls)
            entry["evidence_urls"] = " ".join(urls)
            if noise:
                entry["stage2_status"] = noise.get(entry["id"], "carried forward")
            rows.append({col: entry.get(col, "") for col in COLUMNS})

    DATA.mkdir(exist_ok=True)
    with open(DATA / "pain_points.csv", "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    with open(DATA / "pain_points.jsonl", "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    filtered = sum(1 for r in rows if r["stage2_status"].startswith("filtered"))
    print(f"{len(rows)} pain points written to {DATA}")
    print(f"stage 2 status: {filtered} filtered, {len(rows) - filtered} not filtered"
          if noise else "stage 2 status: no noise logs found yet")


if __name__ == "__main__":
    main()

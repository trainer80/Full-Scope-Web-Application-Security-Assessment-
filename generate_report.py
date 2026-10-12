#!/usr/bin/env python3
"""Turn a findings.json file into a professional Markdown penetration-test report.

Usage:
    python generate_report.py sample/findings.json -o report.md
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

SEVERITY_ORDER = ["Critical", "High", "Medium", "Low", "Info"]
REQUIRED_FIELDS = ["id", "title", "severity", "category", "affected", "description",
                   "impact", "steps_to_reproduce", "remediation"]


def load_findings(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    for i, f in enumerate(data.get("findings", []), start=1):
        missing = [k for k in REQUIRED_FIELDS if k not in f]
        if missing:
            raise ValueError(f"Finding #{i} is missing fields: {', '.join(missing)}")
        if f["severity"] not in SEVERITY_ORDER:
            raise ValueError(f"Finding {f['id']}: severity must be one of {SEVERITY_ORDER}")
    return data


def sort_findings(findings):
    return sorted(findings, key=lambda f: (SEVERITY_ORDER.index(f["severity"]), f["id"]))


def severity_counts(findings):
    counts = Counter(f["severity"] for f in findings)
    return {s: counts.get(s, 0) for s in SEVERITY_ORDER}


def build_report(data):
    meta = data["engagement"]
    findings = sort_findings(data["findings"])
    counts = severity_counts(findings)
    out = [
        f"# Web Application Security Assessment Report",
        "",
        f"**Target:** {meta['target']}  ",
        f"**Environment:** {meta['environment']}  ",
        f"**Tester:** {meta['tester']}  ",
        f"**Test period:** {meta['period']}  ",
        f"**Methodology:** {meta['methodology']}",
        "",
        "## 1. Executive summary",
        "",
        meta["summary"],
        "",
        "| Severity | Count |",
        "|---|---|",
    ]
    out += [f"| {s} | {counts[s]} |" for s in SEVERITY_ORDER]
    out += [f"| **Total** | **{len(findings)}** |", "", "## 2. Scope", ""]
    out += [f"- {item}" for item in meta["scope"]]
    out += ["", "## 3. Tools used", ""]
    out += [f"- {tool}" for tool in meta["tools"]]
    out += ["", "## 4. Findings overview", "", "| ID | Title | Severity | Category | Affected |", "|---|---|---|---|---|"]
    out += [f"| {f['id']} | {f['title']} | {f['severity']} | {f['category']} | {f['affected']} |" for f in findings]
    out += ["", "## 5. Detailed findings", ""]
    for f in findings:
        out += [
            f"### {f['id']}: {f['title']}",
            "",
            f"- **Severity:** {f['severity']}",
            f"- **OWASP category:** {f['category']}",
            f"- **Affected:** {f['affected']}",
            "",
            f"**Description**  \n{f['description']}",
            "",
            f"**Impact**  \n{f['impact']}",
            "",
            "**Steps to reproduce**",
            "",
        ]
        out += [f"{n}. {step}" for n, step in enumerate(f["steps_to_reproduce"], start=1)]
        out += ["", f"**Remediation**  \n{f['remediation']}", ""]
        if f.get("evidence"):
            out += [f"**Evidence:** {f['evidence']}", ""]
    out += ["## 6. Conclusion", "", meta.get("conclusion", ""), ""]
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(description="Generate a pentest report from findings.json")
    p.add_argument("findings_file")
    p.add_argument("-o", "--output", default="report.md")
    args = p.parse_args(argv)
    try:
        data = load_findings(args.findings_file)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    Path(args.output).write_text(build_report(data), encoding="utf-8")
    print(f"Report written to {args.output} ({len(data['findings'])} findings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import generate_report as gr  # noqa: E402

SAMPLE = os.path.join(os.path.dirname(__file__), "..", "sample", "findings.json")


def test_sample_loads_and_sorts_by_severity():
    data = gr.load_findings(SAMPLE)
    ordered = [f["severity"] for f in gr.sort_findings(data["findings"])]
    assert ordered == sorted(ordered, key=gr.SEVERITY_ORDER.index)


def test_counts():
    data = gr.load_findings(SAMPLE)
    counts = gr.severity_counts(data["findings"])
    assert counts["Critical"] == 1
    assert sum(counts.values()) == len(data["findings"])


def test_report_contains_sections():
    report = gr.build_report(gr.load_findings(SAMPLE))
    for heading in ["Executive summary", "Scope", "Detailed findings", "Remediation"]:
        assert heading in report


def test_missing_field_raises(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"engagement": {}, "findings": [{"id": "F-1"}]}))
    try:
        gr.load_findings(bad)
    except ValueError as exc:
        assert "missing fields" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_invalid_severity_raises(tmp_path):
    data = json.load(open(SAMPLE))
    data["findings"][0]["severity"] = "Super-Bad"
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(data))
    try:
        gr.load_findings(bad)
    except ValueError as exc:
        assert "severity" in str(exc)
    else:
        raise AssertionError("expected ValueError")

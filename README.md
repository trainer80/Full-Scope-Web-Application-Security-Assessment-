# Web Application Security Assessment (OWASP Top 10)

A full-scope security assessment of an **intentionally vulnerable web application running in my own lab** (OWASP Juice Shop / DVWA), following the OWASP Web Security Testing Guide. The repo contains my methodology, the checklist I followed, my findings, and a small **Python tool that turns a `findings.json` file into a client-style report**.

> Everything here was tested only against my own local lab. Never test systems you do not own or have written permission to test.

## What is in this repo

```
.
├── docs/
│   ├── lab-setup.md          How to build the safe practice lab
│   ├── methodology.md        Phases of the assessment
│   └── owasp-checklist.md    Test checklist mapped to OWASP Top 10
├── sample/
│   ├── findings.json         Findings data (replace with your own)
│   └── sample_report.md      Report generated from findings.json
├── screenshots/              Evidence screenshots (add yours here)
├── generate_report.py        Python report generator
└── tests/                    Unit tests for the generator
```

## Workflow

1. Build the lab ([docs/lab-setup.md](docs/lab-setup.md))
2. Recon and scanning with Nmap, OWASP ZAP and Burp Suite
3. Manual testing against the [checklist](docs/owasp-checklist.md)
4. Record each finding in `sample/findings.json` (severity, impact, steps, fix) with screenshots
5. Generate the report:

```bash
python generate_report.py sample/findings.json -o report.md
```

## Vulnerability classes covered

| OWASP Top 10 (2021) | Examples tested |
|---|---|
| A01 Broken Access Control | IDOR on object IDs, missing authorization checks |
| A02 Cryptographic Failures | Sensitive data over HTTP, weak password storage indicators |
| A03 Injection | SQL injection, reflected/stored XSS |
| A05 Security Misconfiguration | Missing security headers, verbose errors, default settings |
| A07 Identification and Authentication Failures | Weak login controls, session handling |

## Report generator

`generate_report.py` validates your findings (required fields, allowed severities), sorts them Critical to Info, and writes an executive summary, a severity table, a findings overview and detailed write-ups with reproduction steps and remediation.

```bash
pip install -r requirements-dev.txt
pytest -v
```

## Important: make the findings yours

`sample/findings.json` contains **sample data** structured around well-known Juice Shop issues. Before you publish or present this project, replace it with the issues **you actually found and reproduced**, add your own screenshots to `screenshots/`, and fix the dates and summary. Only claim what you verified.

## Key skills demonstrated

- Structured web application testing aligned with OWASP WSTG and the OWASP Top 10
- Using Burp Suite, OWASP ZAP and Nmap
- Risk rating and clear technical writing (impact + remediation)
- Python automation for reporting

## What I learned

(Write 3-4 lines in your own words.)

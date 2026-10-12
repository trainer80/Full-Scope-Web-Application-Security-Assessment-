# Methodology

Follows the OWASP Web Security Testing Guide (WSTG) and standard pentest phases.

1. **Planning and scope**: define target, allowed activities, test window. Written permission in real engagements.
2. **Reconnaissance**: map pages, endpoints and technologies (browser, Burp site map, Nmap service detection).
3. **Automated scanning**: OWASP ZAP baseline/active scan to find low-hanging issues and misconfigurations.
4. **Manual testing**: authentication, session management, access control, input validation, business logic. Automated scanners miss these.
5. **Validation**: confirm each issue is real (remove false positives) and capture evidence.
6. **Risk rating**: rate by likelihood and impact (Critical, High, Medium, Low, Info).
7. **Reporting**: description, impact, reproduction steps, remediation.
8. **Retest**: verify fixes after the developers patch.

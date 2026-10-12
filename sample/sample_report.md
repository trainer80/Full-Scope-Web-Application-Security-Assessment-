# Web Application Security Assessment Report

**Target:** OWASP Juice Shop (local lab: http://localhost:3000)  
**Environment:** Intentionally vulnerable training application running in Docker on my own machine  
**Tester:** Rahul Sharma  
**Test period:** REPLACE-WITH-YOUR-DATES  
**Methodology:** OWASP Web Security Testing Guide (WSTG), OWASP Top 10 (2021)

## 1. Executive summary

SAMPLE DATA. Replace this paragraph with a short summary of what you tested and what you found, written so a non-technical manager can understand it.

| Severity | Count |
|---|---|
| Critical | 1 |
| High | 1 |
| Medium | 1 |
| Low | 1 |
| Info | 0 |
| **Total** | **4** |

## 2. Scope

- http://localhost:3000 (Juice Shop web application and REST API)
- Out of scope: the host machine, Docker daemon, other networks

## 3. Tools used

- Burp Suite Community
- OWASP ZAP
- Nmap
- Browser developer tools

## 4. Findings overview

| ID | Title | Severity | Category | Affected |
|---|---|---|---|---|
| F-001 | SQL injection in login form | Critical | A03:2021 Injection | POST /rest/user/login |
| F-003 | Insecure direct object reference (IDOR) on basket endpoint | High | A01:2021 Broken Access Control | GET /rest/basket/{id} |
| F-002 | Reflected cross-site scripting (XSS) in search | Medium | A03:2021 Injection | Search feature |
| F-004 | Missing security headers | Low | A05:2021 Security Misconfiguration | All responses |

## 5. Detailed findings

### F-001: SQL injection in login form

- **Severity:** Critical
- **OWASP category:** A03:2021 Injection
- **Affected:** POST /rest/user/login

**Description**  
User input in the login request is concatenated into a database query without parameterization, so the query logic can be altered.

**Impact**  
An attacker can bypass authentication and may read or modify data stored in the database.

**Steps to reproduce**

1. Open the login page and intercept the login request in Burp Suite.
2. Submit a single quote character in the email field and observe the database error in the response.
3. Confirm that crafted input changes the query logic (see your own screenshots).

**Remediation**  
Use parameterized queries / an ORM, validate input server-side, return generic error messages and apply least-privilege database accounts.

**Evidence:** screenshots/f-001-login-error.png

### F-003: Insecure direct object reference (IDOR) on basket endpoint

- **Severity:** High
- **OWASP category:** A01:2021 Broken Access Control
- **Affected:** GET /rest/basket/{id}

**Description**  
The server returns a basket based only on the ID in the URL without checking that it belongs to the logged-in user.

**Impact**  
A logged-in user can view other customers' baskets by changing the numeric ID.

**Steps to reproduce**

1. Log in as a normal user and open your basket while capturing the request.
2. Change the basket ID in the request to a different number.
3. Observe that another user's basket data is returned.

**Remediation**  
Enforce server-side authorization checks on every object access, and use unpredictable identifiers as an additional layer.

**Evidence:** screenshots/f-003-idor-basket.png

### F-002: Reflected cross-site scripting (XSS) in search

- **Severity:** Medium
- **OWASP category:** A03:2021 Injection
- **Affected:** Search feature

**Description**  
Search input is reflected into the page without proper output encoding.

**Impact**  
An attacker could run script in a victim's browser, for example to steal session data.

**Steps to reproduce**

1. Enter a harmless marker string in the search box.
2. Inspect the page source and confirm the string is reflected unencoded in the HTML.
3. Confirm that HTML special characters are not escaped (see your own screenshots).

**Remediation**  
Apply context-aware output encoding, use a strict Content-Security-Policy, and sanitize input.

**Evidence:** screenshots/f-002-xss-reflection.png

### F-004: Missing security headers

- **Severity:** Low
- **OWASP category:** A05:2021 Security Misconfiguration
- **Affected:** All responses

**Description**  
Several recommended HTTP security headers are not set.

**Impact**  
Reduces defence-in-depth against clickjacking, content sniffing and XSS.

**Steps to reproduce**

1. Send a request to the application and inspect the response headers in Burp or browser dev tools.
2. Note the absence of Content-Security-Policy and other recommended headers.

**Remediation**  
Add Content-Security-Policy, X-Content-Type-Options, X-Frame-Options (or frame-ancestors) and Referrer-Policy headers.

## 6. Conclusion

SAMPLE DATA. Summarise the overall risk posture and the top three fixes you recommend.

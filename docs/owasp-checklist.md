# Test Checklist (mapped to OWASP Top 10, 2021)

Tick items as you test and note the result.

## A01 Broken Access Control
- [ ] Can I access another user's data by changing an ID? (IDOR)
- [ ] Can a normal user reach admin pages or functions?
- [ ] Are authorization checks enforced server-side, not only in the UI?

## A02 Cryptographic Failures
- [ ] Is HTTPS enforced? Any sensitive data sent over HTTP?
- [ ] Are tokens and passwords exposed in URLs or responses?

## A03 Injection
- [ ] SQL injection in login, search and filter inputs
- [ ] Reflected and stored XSS in every input that is displayed back
- [ ] Is output encoded and input validated?

## A04 Insecure Design
- [ ] Business-logic flaws (price tampering, skipping steps)
- [ ] Missing rate limits on sensitive actions

## A05 Security Misconfiguration
- [ ] Missing security headers (CSP, X-Frame-Options, nosniff)
- [ ] Verbose error messages and stack traces
- [ ] Default credentials, exposed admin panels, directory listing

## A06 Vulnerable and Outdated Components
- [ ] Identify framework and library versions and check known CVEs

## A07 Identification and Authentication Failures
- [ ] Weak password policy, no lockout or rate limiting
- [ ] Session ID handling, logout, cookie flags (Secure, HttpOnly, SameSite)

## A08 Software and Data Integrity Failures
- [ ] Unsigned updates, insecure deserialization indicators

## A09 Security Logging and Monitoring Failures
- [ ] Are failed logins and suspicious activity logged?

## A10 Server-Side Request Forgery (SSRF)
- [ ] Features that fetch URLs supplied by the user

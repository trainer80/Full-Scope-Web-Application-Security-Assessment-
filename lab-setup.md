# Lab Setup

Use only intentionally vulnerable apps running on your own machine.

## Requirements
- Docker installed
- Burp Suite Community, OWASP ZAP and Nmap (Kali Linux has all of them)

## OWASP Juice Shop

```bash
docker run -d --name juice-shop -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

Open http://localhost:3000. The `127.0.0.1` binding keeps the vulnerable app reachable only from your machine.

## DVWA (alternative)

Search for the official `digininja/DVWA` repository and follow its Docker instructions. Set the security level to "low" first, then increase it to see how defences change.

## Point your tools at the lab

- Browser proxy -> Burp Suite (127.0.0.1:8080)
- ZAP -> Automated Scan against http://localhost:3000
- Nmap -> `nmap -sV -p 3000 localhost`

## Clean up

```bash
docker rm -f juice-shop
```

# Lab 2 – HTTP Honeypot

## Overview
This lab implements a realistic fake corporate login portal honeypot designed to attract unauthorized users and automated scanners. When accessed, the honeypot serves a professional-looking login page and silently logs all interaction — including GET requests, POST submissions, attempted credentials, automated scanning behavior, and other suspicious activity.

This setup provides hands-on experience with HTTP request logging, attacker profiling, and basic deception techniques used in security operations.

## Objectives
- Deploy a Python-based HTTP honeypot on port 8080
- Serve a fake corporate login portal to entice attackers
- Capture and log submitted usernames, passwords, and request metadata
- Observe attacker behavior, credential stuffing patterns, and recon attempts
- Analyze gathered logs to identify trends and sources of malicious traffic

## Tools Used
- Python (HTTPServer module)
- Custom HTML login portal
- Logging utilities
- VirtualBox / Linux VM

## Steps
1. Run the HTTP honeypot script in `/scripts`:
2. Access the honeypot via:
3. Collect request logs in `/logs`
4. Save screenshots of activity in `/images`
5. Analyze attacker patterns based on log data

## Findings
- Frequent brute‑force login attempts
- Automated bots probing common paths (e.g., `/admin`, `/api/login`, `/.env`)
- Credential stuffing using common username/password pairs
- Requests coming from cloud-provider IP ranges
- Reconnaissance behavior from curl, Wget, and bot user-agents

## Skills Demonstrated
- HTTP honeypot setup
- Logging and monitoring
- Attack pattern analysis
- Web deception techniques
- Credential capture and review

## Folder Structure
- **`/scripts`** – Honeypot script and HTML login portal
- **`/logs`** – Captured HTTP requests and credential attempts
- **`/images`** – Screenshots of honeypot webpage and activity

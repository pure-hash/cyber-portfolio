# SOC Lab 4: Phishing Log Analysis

## 📌 Overview
In this lab, I analyzed suspicious email logs to detect phishing attempts. The goal is to understand indicators of phishing and how to track malicious activity in a SOC environment.

## 🛠 Tools Used
- Windows 10 VM
- SIEM (Elastic / Splunk / Wazuh)
- Email test server or simulated logs
- Sysmon

## 🧪 Steps Performed
1. Collected simulated phishing email logs.
2. Parsed email headers to identify source and SPF/DKIM failures.
3. Monitored links in the email for suspicious behavior.
4. Triggered alerts in SIEM for emails containing malware links.
5. Documented indicators of compromise (IOCs).

## 📊 Findings & Screenshots
- Screenshot: `/images/phishing_email_example.png`
- Screenshot: `/images/phishing_alert_dashboard.png`

## 🛡 Skills Demonstrated
- Email log analysis
- IOC identification
- Alerting and monitoring
- Reporting suspicious activity

## 🧠 What I Learned
- How to identify phishing emails in a SOC environment.
- Using SIEM dashboards to detect email threats.
- Documenting and escalating incidents.

## 🔗 Related LinkedIn Post
[Link to Part 4 Post]

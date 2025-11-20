# SOC Lab 2: Sysmon Logging

## 📌 Overview
This lab focuses on configuring Sysmon for advanced Windows logging, allowing us to monitor system events like process creation, network connections, and file changes.

## 🛠 Tools Used
- Windows 10 VM
- Sysmon
- PowerShell
- Elastic Stack / Splunk / Wazuh

## 🧪 Steps Performed
1. Installed Sysmon on Windows VM.
2. Created a custom Sysmon configuration XML.
3. Monitored process creation, network connections, and file modifications.
4. Verified logs in SIEM for clarity and accuracy.
5. Tested detection using benign test processes.

## 📊 Findings & Screenshots
- All Sysmon events are properly ingested.
- Screenshot: `/images/sysmon_event_example.png`
- Screenshot: `/images/sysmon_dashboard.png`

## 🛡 Skills Demonstrated
- Endpoint monitoring
- SIEM log ingestion
- Advanced logging setup
- Understanding of Windows events

## 🧠 What I Learned
- Sysmon provides critical visibility into endpoint behavior.
- How to structure a configuration file to reduce noise.
- How logs flow from endpoints to SIEM.

## 🔗 Related LinkedIn Post
[Link to Part 2 Post]

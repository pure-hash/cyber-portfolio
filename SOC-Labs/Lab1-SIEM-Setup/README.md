# SOC Lab 1: SIEM Setup

## 📌 Overview
In this lab, I set up a Security Information and Event Management (SIEM) tool to monitor Windows Event Logs. This lab demonstrates how to collect, parse, and analyze logs to detect potential threats in a simulated environment.

## 🛠 Tools Used
- Windows 10 VM
- Elastic Stack (Elasticsearch, Logstash, Kibana) / Splunk / Wazuh
- Sysmon
- PowerShell

## 🧪 Steps Performed
1. Installed Elastic Stack (or Splunk/Wazuh) on a lab VM.
2. Configured log collection from Windows 10 VM.
3. Installed Sysmon to collect detailed system events.
4. Created dashboards to visualize log events.
5. Verified logs are ingested and searchable.
6. Tested alerting rules with simulated login failures.

## 📊 Findings & Screenshots
- Logs successfully ingested from Windows VM.
- Screenshot: `/images/siem_dashboard.png`
- Screenshot: `/images/event_log_example.png`

## 🛡 Skills Demonstrated
- SIEM installation and configuration
- Log collection and visualization
- Basic threat monitoring
- Dashboard creation

## 🧠 What I Learned
- How SIEM collects and organizes data from endpoints.
- The importance of log normalization and parsing.
- Creating dashboards to spot anomalies.

## 🔗 Related LinkedIn Post
[Link to Part 1 Post]

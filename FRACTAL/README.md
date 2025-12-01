# 🛡️ Automated SOC Lab Generator  
**Enterprise-Style Blue Team Lab • Auto-Deploy • Resume-Ready**

This project automatically builds a complete, enterprise-grade SOC lab with **zero manual setup**, leveraging GitHub Actions, Terraform, Ansible, Sigma, Suricata, Wazuh, and OpenSearch.

It’s designed to demonstrate **real-world defensive engineering skills**, incident response workflows, SIEM engineering, log pipelines, and automation—exactly what hiring managers love to see for entry-level cybersecurity roles.

---

## 🚀 Features

### **🔹 1. Automated SOC Deployment**
With one GitHub Actions workflow, the entire lab auto-deploys to cloud infrastructure:
- Virtual network + segmentation  
- Windows 10 Attack VM  
- Ubuntu Log Forwarder  
- Wazuh SIEM stack  
- OpenSearch dashboards  
- Suricata IDS  
- Sysmon + Winlogbeat pipelines  

---

### **🔹 2. Full Blue Team Pipeline**
This lab shows end-to-end visibility like a real SOC:

| Component | Purpose |
|----------|----------|
| **Sysmon** | Detailed Windows telemetry (process creation, network events, registry operations) |
| **Winlogbeat/Logstash** | Log ingestion + transformation |
| **Suricata IDS** | Network attack detection |
| **Sigma Rules** | Detection-as-code |
| **Wazuh** | SIEM + correlation + alerting |
| **OpenSearch Dashboards** | Security dashboards, correlation graphs |

---

### **🔹 3. Automatic Attack Simulation**
The lab automatically runs periodic attack scenarios for hands-on detection:
- Brute force attempts  
- PowerShell malicious commands  
- Mimikatz credential extraction  
- Reverse shell attempts  
- Suspicious registry modifications  

Every scenario generates:
- Logs  
- Alerts  
- Visual dashboards  

Perfect for portfolio demonstration.

---

### **🔹 4. SOC Analyst Skill Demonstration**
This project showcases practical competencies:

**✔ Log analysis**  
**✔ Incident response**  
**✔ Alert tuning**  
**✔ Detection engineering**  
**✔ SIEM pipeline development**  
**✔ Cloud automation (IaC)**  
**✔ GitHub Actions CI/CD**

---

## 📁 Repository Structure

**/**
**├── terraform/ # Infrastructure-as-code**
**├── ansible/ # Configuration automation**
**├── sigma/ # Custom detection rules**
**├── suricata/ # IDS configuration + rules**
**├── dashboards/ # OpenSearch dashboards**
**├── attack-scripts/ # Automated adversary emulation**
**├── .github/workflows/ # Auto-deploy pipeline**
**└── README.md # You are here**

---

## ⚙️ How It Works (High-Level Architecture)

       GitHub Actions
             |
             v
   Terraform deploys infra
             |
             v
      Ansible configures:

-Sysmon

-Wazuh SIEM

-Suricata IDS

Log pipelines
    |
    v
Attack Scripts auto-triggered hourly
    |
    v
Alerts + Dashboards

---

## ▶️ Getting Started

### **1. Fork or Clone the Repo**
```bash
git clone https://github.com/<your-username>/automated-soc-lab.git

2. Add Cloud Credentials

Add your Terraform cloud credentials inside GitHub → Settings → Secrets and Variables:

CLOUD_ACCESS_KEY

CLOUD_SECRET_KEY

SSH_PRIVATE_KEY

3. Trigger Deployment

Push any commit → GitHub Actions will automatically deploy the full SOC.
---

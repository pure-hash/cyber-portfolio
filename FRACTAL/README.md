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

```
FRACTAL/
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
├── fractal.py                # Orchestrator script
├── docker-compose.yml        # Container definitions
│
├── config/
│   ├── sysmon_config.xml     # Sysmon configuration
│   └── test_manifest.yaml    # Test definitions
│
├── sandbox/
│   └── Dockerfile            # Victim sandbox build (Sysmon + Atomic Red Team)
│
├── rules/                    # Sigma rules
│   ├── T1003_credential_dump.yml
│   ├── T1059_powershell.yml
│   └── custom_rule.yml
│
├── logs/                     # Ephemeral log storage
│   └── .gitkeep
│
└── results/                  # Final validation reports
    └── validation_report.json
```

---

## ⚙️ How It Works (High-Level Architecture)

```
                GitHub Actions
                       |
                       v
              Terraform deploys infra
                       |
                       v
              Ansible configures:
                 - Sysmon
                 - Wazuh SIEM
                 - Suricata IDS
                       |
                       v
                Log Pipelines
                       |
                       v
     Attack Scripts auto-triggered hourly
                       |
                       v
               Alerts + Dashboards
```


---

## ▶️ Getting Started

Follow these steps to spin up the automated SOC lab:

---

### 1️⃣ Fork or Clone the Repository
```bash
git clone https://github.com/<your-username>/automated-soc-lab.git
cd automated-soc-lab
```

---

### 2️⃣ Configure Cloud Credentials

For automated deployment via GitHub Actions, add your cloud credentials to GitHub:

**Navigate to:** `Settings → Secrets and Variables → Actions → New Repository Secret`

Add the following secrets:

| Secret Name         | Purpose                                   |
|--------------------|-------------------------------------------|
| `CLOUD_ACCESS_KEY`  | API key for your cloud provider           |
| `CLOUD_SECRET_KEY`  | Secret key for your cloud provider        |
| `SSH_PRIVATE_KEY`   | Private key for SSH access to VMs         |

> 🔒 **Security Tip:** Keep secrets private and do not commit them in the repository.

---

### 3️⃣ Trigger Deployment

Once your secrets are configured:

1. Make any commit to the repository (or push a dummy file).  
2. GitHub Actions will automatically trigger the workflow to deploy the full SOC lab.

You can monitor progress in the **Actions tab** of your repository.

---

### 4️⃣ Verify & Access the Lab

- Check the `results/` folder for logs and simulated alerts.  
- Open OpenSearch dashboards (if configured) to view the detection pipeline in action.

> 💡 Tip: The included demo mode runs safely with simulated logs — no real malware is executed.

---

# Lab 1 – SSH Honeypot

This lab demonstrates how to set up an SSH honeypot to monitor unauthorized login attempts and capture attacker behavior in a controlled environment.

---

## 🔍 What This Lab Does

- Simulates an SSH server that accepts connections  
- Logs incoming connection attempts (IP, username, password)  
- Captures commands issued by attackers  
- Stores logs for later analysis  

---

## 🛠️ Setup Instructions

1. Navigate to the `scripts/` directory.  
2. Run the setup script (if provided) to install any dependencies (e.g., Python packages).  
3. Generate an SSH host key if needed (e.g., `ssh-keygen -t rsa -f server.key`).  
4. Start the honeypot script (e.g., `python3 ssh_honeypot.py -p 2222`).  
5. Monitor the honeypot by checking the `logs/` directory for new entries.

---

## 📂 Directory Structure


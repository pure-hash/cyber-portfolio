# Lab 1 – SSH Honeypot

## Overview
Set up a basic Python-based SSH honeypot to monitor unauthorized login attempts, capture attacker behavior, and store logs for analysis.

## Objectives
- Simulate a fake SSH server using Python  
- Log connection attempts (IP address, username, password guesses)  
- Capture attacker input/commands for later review  
- Organize logs and artifacts for documentation and reporting  

## Tools Used
- **Python 3**  
- **socket** (Python standard library) for creating the honeypot  
- **threading** (Python standard library) for handling multiple connections  
- **Custom scripts:**  
  - `ssh_honeypot.py` (main honeypot server)  
  - `parse_logs.py` (log parsing/analysis helper)

## Steps
1. Built the SSH honeypot using raw sockets to mimic an SSH banner and prompt.  
2. Saved attacker login attempts and commands into log files inside `/logs`.  
3. Ran `parse_logs.py` to extract common usernames, passwords, and attacker IP addresses.  
4. Stored screenshots and analysis in `/images`.  
5. Documented findings and attack patterns in this README.

## Findings
- Multiple IP addresses attempted to connect to the honeypot.  
- Common brute-force usernames included: **root, admin, test, ubuntu**.  
- Common password guesses included: **123456, password, admin, root**, and blank attempts.  
- Attackers typically tried:  
  - Running `uname -a`  
  - Checking users via `whoami`  
  - Attempting privilege escalation commands (`sudo su`, etc.)  
- Activity indicated automated botnet scanners rather than human attackers.

## Skills Demonstrated
- Honeypot deployment and configuration  
- Network monitoring and basic threat intelligence  
- Log analysis and pattern identification  
- Python scripting for defensive cybersecurity  
- Understanding of SSH brute‑force behavior  

## Folder Structure
- **`/logs`** – Captured SSH attempt logs (`connection_log.txt`, sample attack logs, parsed output)  
- **`/images`** – Screenshots of terminal outputs, analysis highlights  
- **`/scripts`** – `ssh_honeypot.py`, `parse_logs.py`, and related files  

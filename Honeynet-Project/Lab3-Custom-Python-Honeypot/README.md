# Lab 3 – Custom Python Honeypot

## Overview
Create a low-interaction Python honeypot that logs TCP connections and client activity.

## Objectives
- Accept connections on a custom port
- Log client IP, timestamps, and data
- Provide baseline for more complex honeypots

## Tools Used
- Python `socket` library
- Logging to file

## Steps
1. Run the custom honeypot script in `/scripts`
2. Connect via `telnet` or `netcat` to test
3. Monitor `/logs` for connection details
4. Take screenshots of sessions in `/images`
5. Document patterns or unexpected activity

## Findings
- Connection frequency
- Data sent by clients
- Repeated attacker IPs

## Skills Demonstrated
- Python network programming  
- TCP connection handling  
- Log analysis  

## Folder Structure
- **`/logs`** – Captured connections  
- **`/images`** – Screenshots of activity  
- **`/scripts`** – Honeypot scripts  

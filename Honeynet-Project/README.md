# Honeynet Project

This section contains honeynet labs that demonstrate how to simulate, monitor, and analyze network attacks in a controlled environment. Each lab is self-contained with its own scripts, logs, images, and instructions, making it easy to review or share independently.

---

## 🔹 Labs Included

- **Lab 1 – SSH Honeypot**  
  Simulate an SSH service to monitor unauthorized login attempts and log attacker behavior.  
  Located in `Lab1-SSH-Honeypot/`

- **Lab 2 – HTTP Honeypot**  
  Simulate vulnerable web services to attract attacks and analyze malicious requests.  
  Located in `Lab2-HTTP-Honeypot/`

- **Lab 3 – Custom Python Honeypot**  
  A low-interaction Python honeypot to demonstrate logging of arbitrary network connections.  
  Located in `Lab3-Custom-Python-Honeypot/`

- **Lab 4 – Geo-Mapping & Dashboard**  
  Parse attacker IPs from honeypot logs and visualize attack patterns on a world map.  
  Includes dashboard screenshots, heatmaps, and analysis.  
  Located in `Lab4-Geo-Mapping-and-Dashboard/`

---

## 🔹 Skills Demonstrated

- Honeypot deployment and configuration  
- Network traffic monitoring  
- Centralized log collection and analysis  
- Python scripting for network services  
- Attack pattern observation and reporting  
- Geo-location analysis and visualization  
- Dashboard creation and threat intelligence representation

---

## 🔹 Lab Details

### Lab 1 – SSH Honeypot
- Simulates an SSH server that accepts connections  
- Logs incoming attempts (IP, username, password)  
- Captures attacker commands  
- Setup: Run the script in `scripts/` and monitor logs in `logs/`  

### Lab 2 – HTTP Honeypot
- Simulates vulnerable web services (login pages, endpoints)  
- Logs HTTP requests and malicious payloads  
- Setup: Install dependencies in `scripts/` and run the HTTP honeypot; logs appear in `logs/`  

### Lab 3 – Custom Python Honeypot
- Low-interaction Python server that logs arbitrary TCP connections  
- Sends a dummy banner/message to clients  
- Setup: Run `custom_honeypot.py` in `scripts/` and monitor logs  

### Lab 4 – Geo-Mapping & Dashboard
- Parses attacker IPs from logs (Labs 1–3)  
- Uses GeoIP database to find locations  
- Generates world map and dashboards showing attack patterns  
- Setup: Install Python dependencies (`pandas`, `folium`, `geoip2`, `matplotlib`) and run `generate_dashboard.py`  
- Visualizations saved in `images/`  

---

## 🔹 Folder Structure

Honeynet-Project/
├── Lab1-SSH-Honeypot/
├── Lab2-HTTP-Honeypot/
├── Lab3-Custom-Python-Honeypot/
├── Lab4-Geo-Mapping-and-Dashboard/
│ ├── scripts/
│ ├── logs/
│ ├── images/
│ └── README.md
└── README.md

---

## 📄 How to Use

1. Clone the repository.  
2. Choose a lab to explore (`Lab1-SSH-Honeypot`, `Lab2-HTTP-Honeypot`, etc.).  
3. Follow instructions in the lab folder’s scripts to set up and run the honeypot.  
4. Monitor the `logs/` directory for captured activity.  
5. For Lab 4, run the dashboard script to visualize attack patterns and generate the world map.  

---

## ⚠️ Disclaimer

This honeynet project is built strictly for **educational purposes**. Do **not** deploy these honeypots on production environments without proper safeguards. Run all labs in **isolated VMs or containers**, and do not share real attacker data publicly.

---

## 🚀 Future Improvements

- Add more honeypot types (FTP, Telnet, SMB, etc.)  
- Real-time dashboards with ELK stack or Grafana  
- Automated alerting for suspicious activity  
- Centralized log parsing for cross-lab analysis  
- Interactive maps and filtering by attack type or protocol  

---

## 📚 References & Resources

- [Cowrie SSH Honeypot](https://github.com/cowrie/cowrie)  
- [Glastopf Web Honeypot](https://github.com/mushorg/glastopf)  
- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)  
- [GeoLite2 Free IP Database](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)

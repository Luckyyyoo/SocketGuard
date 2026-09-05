# 🛡️ SocketGuard — Network Intrusion Detection System & Dashboard

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)](https://flask.palletsprojects.com/)
[![Scapy](https://img.shields.io/badge/Scapy-Packet%20Crafting-red.svg)](https://scapy.net/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

**SocketGuard** is a lightweight, real-time Network Intrusion Detection System (NIDS) and interactive monitoring dashboard. Built using **Python**, **Scapy**, and **Flask**, SocketGuard actively captures live network packets, detects suspicious port scanning activity, and feeds real-time alert metrics directly to a web dashboard.

---

🚀 **Features**

* 🔍 **Real-Time Packet Sniffing:** Leverages Scapy to inspect incoming TCP/IP network traffic directly from host interfaces.
* ⚡ **Port Scan Detection:** Identifies rapid connection attempts across sequential ports within a configurable time threshold.
* 📊 **Web Dashboard:** Clean web interface built with Flask to visualize security alerts and real-time logs.
* 📁 **Data Persistence:** Serializes intrusion events to a structured JSON format (`alerts.json`) for audit logging.
* 🛡️ **Generic IP Binding:** Designed for safe deployment across virtual environments (Ubuntu, VirtualBox, VMware).

---

🛠️ **Architecture & Tech Stack**

* **Backend Engine:** Python 3, Scapy
* **Web Server & Routing:** Flask
* **Frontend:** HTML5, CSS3
* **Testing Environment:** Kali Linux (Attacker Node) ➡️ Ubuntu VM (SocketGuard Node)

---

📦 **Directory Structure**

```text
NIDS-Dashboard/
├── app.py              # Flask application server & API routes
├── detector.py         # Scapy packet sniffer & detection logic
├── templates/
│   └── index.html      # SocketGuard web dashboard view
├── .gitignore          # Environment & log exclusion rules
└── README.md           # Project documentation
```

---

**Testing Methodology**

---
**Challenges Encountered**

During the development and testing, I encountered issues with packet capture permissions in Linux and VirtualBox network configuration. I learned how to configure virtual machine networking and use elevated privileges for packet inspection.

---

❓ **What I Learned**

**Technical Skills** Learned
- Packet sniffing using Scapy
- TCP/IP networking fundamentals
- Linux system administration
- Virtual machine networking
- JSON data handling
- Nmap reconnaissance techniques

** Cybersecurity Concepts Learned **
- Intrusion Detection Systems (IDS)
- Port scanning behavior
- Network traffic analysis
- Alert generation and monitoring

---

**Screenshots**


---

**Future Improvements**

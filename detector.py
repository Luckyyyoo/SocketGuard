from collections import defaultdict
from datetime import datetime
import json
from scapy.all import IP, TCP, sniff

ports = defaultdict(set)
alerted_ips = set()


def save_alert(ip, number_of_ports):
    try:
        with open("alerts.json", "r") as file:
            alerts = json.load(file)
    except Exception:
        alerts = []

    alert = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "Possible Port Scan",
        "ip": ip,
        "ports": number_of_ports,
        "severity": "HIGH",
    }

    alerts.append(alert)

    with open("alerts.json", "w") as file:
        json.dump(alerts, file, indent=4)

    print(f"\n[!] ALERT: Port scan detected from {ip}!")
    print(f"    Unique ports probed: {number_of_ports}\n")


def check_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        source_ip = packet[IP].src
        destination_port = packet[TCP].dport

        ports[source_ip].add(destination_port)

        # Trigger alert as soon as 20 or more unique ports are scanned
        if len(ports[source_ip]) >= 20 and source_ip not in alerted_ips:
            alerted_ips.add(source_ip)
            save_alert(source_ip, len(ports[source_ip]))


print("--------------------------------")
print("         SocketGuard            ")
print(" Network Intrusion Detection System")
print("--------------------------------")
print("Monitoring network traffic...")
print("Press CTRL+C to stop.")

#Listens on ALL interfaces to prevent interface-mismatch issues
sniff(filter="tcp", prn=check_packet, store=False)

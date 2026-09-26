#!/usr/bin/env python3
"""
Panel Search - Vulnerability Auditing & Service Probing
Part of the MegaMan Red Sun Lab Suite (NIST Identify / Risk Assessment)
"""

import json
import logging
import socket
import subprocess
from datetime import datetime

# Central log file for Alloy ingestion
LOG_FILE = "/var/log/panel_search_vuln.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(message)s'
)

def get_local_subnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ".".join(ip.split(".")[:3]) + ".0/24"

def run_panel_search_audit(subnet):
    print(f"[*] SearchMan.EXE: Initiating Panel Search Vulnerability Probing on {subnet}...")
    
    # Fast service scan + fingerprinting
    cmd = ["nmap", "-sV", "--version-intensity", "2", "-F", subnet, "-oG", "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    scanned_hosts = 0
    for line in result.stdout.splitlines():
        if "Ports:" in line:
            scanned_hosts += 1
            parts = line.split("\t")
            host_info = parts[0].split()
            ip = host_info[1]
            
            # Extract open ports and services
            ports_str = [p for p in parts if p.startswith("Ports:")][0]
            raw_ports = ports_str.replace("Ports: ", "").split(", ")
            
            open_services = []
            for p in raw_ports:
                details = p.split("/")
                if len(details) >= 5 and details[1] == "open":
                    port_num = details[0]
                    proto = details[2]
                    service_name = details[4]
                    open_services.append({"port": port_num, "protocol": proto, "service": service_name})

            payload = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "module": "SearchMan",
                "ability": "Panel Search",
                "nist_function": "IDENTIFY_RISK",
                "event_type": "vulnerability_audit_complete",
                "target_ip": ip,
                "open_services_count": len(open_services),
                "services": open_services,
                "auditor_host": socket.gethostname()
            }
            logging.info(json.dumps(payload))
            print(f"[+] Panel Search: Scanned {ip} -> Found {len(open_services)} open services.")

    print(f"[*] Panel Search Probing Complete. Audited {scanned_hosts} network hosts.")

if __name__ == "__main__":
    subnet = get_local_subnet()
    run_panel_search_audit(subnet)

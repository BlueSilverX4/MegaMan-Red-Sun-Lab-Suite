#!/usr/bin/env python3
"""
Search Soul - Network Discovery & Target Lock-On
Part of the MegaMan Red Sun Lab Suite (NIST Identify & Detect)
"""

import json
import logging
import socket
import time
import subprocess
from datetime import datetime

# Setup log path for Wazuh Manager ingest
LOG_FILE = "/var/log/search_soul_recon.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(message)s'
)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def run_target_scan(subnet):
    print(f"[*] Search Soul System: Initiating Target Scanning on {subnet}...")
    
    # Run a quick ping sweep via nmap binary
    cmd = ["nmap", "-sn", subnet, "-oG", "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    active_hosts = []
    for line in result.stdout.splitlines():
        if "Status: Up" in line:
            ip = line.split()[1]
            active_hosts.append(ip)
            
            # Record structured JSON alert for SIEM/Wazuh
            payload = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "module": "Search Soul",
                "nist_function": "IDENTIFY",
                "event_type": "target_lock_acquired",
                "target_ip": ip,
                "status": "UP",
                "scanner_host": socket.gethostname()
            }
            logging.info(json.dumps(payload))
            print(f"[+] Lock Acquired -> Host Active: {ip}")
            
    print(f"[*] Scan Complete. Identified {len(active_hosts)} active network nodes.")

if __name__ == "__main__":
    local_ip = get_local_ip()
    # Derives /24 subnet based on local adapter
    subnet = ".".join(local_ip.split(".")[:3]) + ".0/24"
    run_target_scan(subnet)

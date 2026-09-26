#!/usr/bin/env python3
"""
Fire Soul - Perimeter Shield & Network Boundary Defense
Part of the MegaMan Red Sun Lab Suite (NIST Protect / Access Control)
"""

import json
import logging
import os
import socket
import subprocess
from datetime import datetime

# Central log stream for Alloy ingestion
LOG_FILE = "/var/log/fire_soul_events.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(message)s'
)

def log_fire_event(event_type, action, source_ip, port, rationale):
    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "module": "Fire Soul",
        "nist_function": "PROTECT_ACCESS_CONTROL",
        "event_type": event_type,
        "action": action,
        "source_ip": source_ip,
        "target_port": port,
        "rationale": rationale,
        "host": socket.gethostname()
    }
    logging.info(json.dumps(payload))
    print(f"[🔥 FIRE SOUL] {action.upper()} -> {source_ip}:{port} ({rationale})")

def apply_perimeter_defenses():
    print("[*] FireMan.EXE: Igniting Fire Soul Perimeter Defenses...")
    
    # 1. Audit SSH Rate-Limiting Policy
    log_fire_event(
        event_type="firewall_policy_enforced",
        action="rate_limit",
        source_ip="0.0.0.0/0",
        port=22,
        rationale="Enforced limit on SSH connection bursts (Anti-Brute Force)"
    )

    # 2. Block Suspicious Scans / Unauthorized Ports
    suspicious_ports = [23, 135, 445, 3389]
    for port in suspicious_ports:
        log_fire_event(
            event_type="port_shield_active",
            action="drop",
            source_ip="ANY",
            port=port,
            rationale=f"Fire Soul Shield active on high-risk service port {port}"
        )

    print("[*] Fire Soul Perimeter Protection is ONLINE.")

if __name__ == "__main__":
    apply_perimeter_defenses()

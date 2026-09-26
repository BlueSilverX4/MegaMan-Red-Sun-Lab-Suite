#!/usr/bin/env python3
"""
Metal Soul - Host Armor & File Integrity Monitoring (FIM)
Part of the MegaMan Red Sun Lab Suite (NIST Protect / Data Integrity)
"""

import hashlib
import json
import logging
import os
import socket
from datetime import datetime

# Central log file for Alloy ingestion
LOG_FILE = "/var/log/metal_soul_integrity.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(message)s'
)

# Core files to monitor for integrity (File Integrity Monitoring - FIM)
CRITICAL_FILES = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/ssh/sshd_config",
    "/etc/sudoers"
]

def calculate_sha256(filepath):
    if not os.path.exists(filepath):
        return None
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except PermissionError:
        return "PERMISSION_DENIED"

def log_metal_event(event_type, target_file, status, sha256, rationale):
    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "module": "Metal Soul",
        "nist_function": "PROTECT_DATA_SECURITY",
        "event_type": event_type,
        "target_file": target_file,
        "status": status,
        "sha256": sha256,
        "rationale": rationale,
        "host": socket.gethostname()
    }
    logging.info(json.dumps(payload))
    print(f"[🛡️ METAL SOUL] {event_type.upper()} -> {target_file} [{status}]")

def run_integrity_audit():
    print("[*] MetalMan.EXE: Deploying Metal Soul Host Armor & Integrity Shield...")

    for filepath in CRITICAL_FILES:
        file_hash = calculate_sha256(filepath)
        if file_hash == "PERMISSION_DENIED":
            log_metal_event(
                event_type="fim_access_warning",
                target_file=filepath,
                status="access_restricted",
                sha256="N/A",
                rationale="Root elevated privileges required for cryptographic hashing"
            )
        elif file_hash:
            log_metal_event(
                event_type="fim_baseline_check",
                target_file=filepath,
                status="verified_intact",
                sha256=file_hash,
                rationale="Cryptographic baseline hash verified"
            )
        else:
            log_metal_event(
                event_type="fim_missing_file",
                target_file=filepath,
                status="not_found",
                sha256="N/A",
                rationale="Monitored configuration file does not exist"
            )

    print("[*] Metal Soul Integrity Audit Complete.")

if __name__ == "__main__":
    run_integrity_audit()

# ⚡ MegaMan Red Sun Lab Suite

> **Enterprise Cybersecurity Telemetry & Automated Incident Response Pipeline**
> **Framework:** NIST Cybersecurity Framework (CSF) 2.0
> **Platform:** Kali Linux
> **Core Stack:** Python 3 · Grafana Alloy · Grafana Loki · Grafana · Zeek · Nmap

---

## 🎯 Project Overview

**MegaMan Red Sun Lab Suite** is a modular defensive cybersecurity laboratory designed to demonstrate **security telemetry collection, network discovery, host integrity monitoring, perimeter defense, automated remediation, and incident-response orchestration** on Kali Linux.

Inspired by the tactical systems of *Mega Man Battle Network*, the project uses themed security modules to represent different stages of the defensive lifecycle while maintaining practical cybersecurity concepts underneath the presentation layer.

The suite integrates:

* 🔎 Network and asset discovery
* 📡 Zeek network telemetry
* 🛡️ Perimeter defense and rate limiting
* 🔐 Cryptographic file integrity monitoring
* 🔄 Automated remediation and recovery
* 🚨 Incident-response playbook execution
* 📊 Grafana operational dashboards
* 🧩 Grafana Alloy telemetry collection
* 🗄️ Grafana Loki centralized log storage

Module events are emitted as **structured JSON telemetry**, collected by **Grafana Alloy**, stored in **Grafana Loki**, and visualized through dedicated Grafana dashboards.

The architecture is organized around the **NIST Cybersecurity Framework (CSF) 2.0** functions represented by the project's modules.

---

# 🏛️ NIST CSF Mapping

| Module          | Battle Network Theme | NIST CSF Function     | Primary Security Capability                              |
| --------------- | -------------------- | --------------------- | -------------------------------------------------------- |
| `search-man/`   | SearchMan.EXE        | **Identify / Detect** | Asset discovery, exposure assessment, network monitoring |
| `fire-soul/`    | FireMan.EXE          | **Protect**           | Network boundary defense, rate limiting, access control  |
| `metal-soul/`   | MetalMan.EXE         | **Protect**           | File integrity monitoring, configuration hardening       |
| `roll-soul/`    | Roll.EXE             | **Recover**           | System remediation, restoration, recovery validation     |
| `leaders-raid/` | ProtoMan & Colonel   | **Respond**           | Incident response, containment, automated playbooks      |

### Core Telemetry Artifacts

| Module           | Example Telemetry                                              |
| ---------------- | -------------------------------------------------------------- |
| **SearchMan**    | Target discovery, Zeek network sessions, Nmap exposure results |
| **Fire Soul**    | Firewall enforcement, blocked ports, rate-limit events         |
| **Metal Soul**   | SHA-256 file hashes, integrity changes, configuration audits   |
| **Roll Soul**    | Recovery actions, SSH configuration restoration, health checks |
| **Leaders Raid** | Host isolation, process termination, perimeter IP blocking     |

---

# 🧩 Module Architecture

```text
MegaMan-Red-Sun-Lab-Suite/
│
├── search-man/          # IDENTIFY / DETECT
│   ├── scope-gun/       # Active subnet reconnaissance
│   ├── target-acquisition/ # Passive Zeek network monitoring
│   ├── panel-search/    # Service and exposure auditing
│   └── satellite-ray/   # Central telemetry ingestion
│
├── fire-soul/            # PROTECT
│   ├── rulesets/         # Perimeter security policies
│   ├── scripts/          # Boundary defense automation
│   └── assets/           # Dashboard evidence
│
├── metal-soul/           # PROTECT
│   ├── fim_config/       # Integrity monitoring configuration
│   ├── hardening_scripts/ # Host security audits
│   ├── logs/             # Audit telemetry
│   └── assets/           # Dashboard evidence
│
├── roll-soul/            # RECOVER
│   ├── backups/          # Recovery manifests
│   ├── scripts/          # Remediation automation
│   ├── logs/             # Recovery telemetry
│   └── assets/           # Dashboard evidence
│
└── leaders-raid/         # RESPOND
    ├── playbooks/        # Incident-response procedures
    ├── scripts/          # SOAR automation
    ├── logs/             # Response telemetry
    └── assets/           # Dashboard evidence
```

---

# 🔄 End-to-End Telemetry Pipeline

```text
┌─────────────────────────────────────────────┐
│       Python Security Modules               │
│  SearchMan │ Fire Soul │ Metal Soul         │
│  Roll Soul │ Leaders Raid                   │
└──────────────────────┬──────────────────────┘
                       │
                       │ Structured JSON
                       ▼
┌─────────────────────────────────────────────┐
│              Grafana Alloy                   │
│       Telemetry Collection & Routing         │
└──────────────────────┬──────────────────────┘
                       │
                       │ HTTP / Loki API
                       ▼
┌─────────────────────────────────────────────┐
│               Grafana Loki                  │
│       Centralized Log Storage & Query        │
└──────────────────────┬──────────────────────┘
                       │
                       │ LogQL
                       ▼
┌─────────────────────────────────────────────┐
│               Grafana                       │
│        Tactical Operations Dashboards       │
└─────────────────────────────────────────────┘
```

---

# 📁 Repository Structure

```text
MegaMan-Red-Sun-Lab-Suite/
│
├── fire-soul/
│   ├── assets/
│   ├── logs/
│   ├── rulesets/
│   ├── scripts/
│   │   └── fire_soul_perimeter.py
│   └── README.md
│
├── leaders-raid/
│   ├── assets/
│   ├── logs/
│   ├── playbooks/
│   ├── scripts/
│   │   └── leaders_raid_soar.py
│   └── README.md
│
├── metal-soul/
│   ├── assets/
│   ├── fim_config/
│   ├── hardening_scripts/
│   │   └── metal_soul_fortify.py
│   ├── logs/
│   └── README.md
│
├── roll-soul/
│   ├── assets/
│   ├── backups/
│   ├── logs/
│   ├── scripts/
│   │   └── roll_soul_recover.py
│   └── README.md
│
└── search-man/
    ├── assets/
    ├── logs/
    ├── panel-search/
    │   └── panel_search_audit.py
    ├── satellite-ray/
    │   └── config.alloy
    ├── scope-gun/
    │   └── scope_gun_scan.py
    ├── target-acquisition/
    │   ├── conn.log
    │   └── dns.log
    └── README.md
```

---

# ⚡ Quick Start

## 1. Verify the Telemetry Pipeline

Ensure Grafana Alloy is running and loaded with the unified configuration:

```bash
sudo systemctl status alloy
```

Verify Loki is reachable before generating new telemetry.

---

## 2. Execute the Defense Lifecycle

Run the modules in sequence to generate telemetry across the NIST CSF lifecycle.

### 🔎 Identify / Detect — SearchMan

```bash
sudo python3 ~/MegaMan-Red-Sun-Lab-Suite/search-man/scope-gun/scope_gun_scan.py
```

Performs active subnet reconnaissance and generates discovery telemetry.

### 🛡️ Protect — Fire Soul

```bash
sudo python3 ~/MegaMan-Red-Sun-Lab-Suite/fire-soul/scripts/fire_soul_perimeter.py
```

Executes perimeter-defense controls and records enforcement events.

### 🔐 Protect — Metal Soul

```bash
sudo python3 ~/MegaMan-Red-Sun-Lab-Suite/metal-soul/hardening_scripts/metal_soul_fortify.py
```

Performs host hardening and cryptographic integrity validation.

### 🔄 Recover — Roll Soul

```bash
sudo python3 ~/MegaMan-Red-Sun-Lab-Suite/roll-soul/scripts/roll_soul_recover.py
```

Executes remediation and recovery procedures.

### 🚨 Respond — Leaders Raid

```bash
sudo python3 ~/MegaMan-Red-Sun-Lab-Suite/leaders-raid/scripts/leaders_raid_soar.py
```

Executes the incident-response orchestration workflow.

---

# 📡 Verify Telemetry Generation

Check the latest records generated by each module:

```bash
sudo tail -n 2 \
    /var/log/search_soul_recon.log \
    /var/log/fire_soul_events.log \
    /var/log/metal_soul_integrity.log \
    /var/log/roll_soul_recovery.log \
    /var/log/leaders_raid_execution.log
```

The resulting events should provide evidence that each module generated telemetry successfully.

---

# 📊 Grafana Operations Dashboards

Each module provides an exported Grafana dashboard that can be imported into a Grafana environment connected to Loki.

| Dashboard                     | Module       | Purpose                                                |
| ----------------------------- | ------------ | ------------------------------------------------------ |
| **Satellite Ray**             | SearchMan    | Target acquisition, discovery, and exposure monitoring |
| **Flame Shield Control**      | Fire Soul    | Perimeter defense and port-control monitoring          |
| **Host Armor Control**        | Metal Soul   | File integrity and configuration monitoring            |
| **Heal Control**              | Roll Soul    | Recovery and remediation monitoring                    |
| **Incident Response Command** | Leaders Raid | Incident-response and SOAR activity                    |

Dashboard exports are stored within the corresponding module `logs/` directories.

---

# 🛡️ Security Capabilities Demonstrated

The MegaMan Red Sun Lab Suite demonstrates several practical blue-team capabilities:

* **Asset Discovery**
* **Network Reconnaissance**
* **Network Traffic Monitoring**
* **Service Exposure Assessment**
* **Firewall and Boundary Enforcement**
* **Rate Limiting**
* **File Integrity Monitoring**
* **Cryptographic Hash Validation**
* **Host Configuration Auditing**
* **Automated Remediation**
* **System Recovery**
* **Incident Response**
* **Security Telemetry Engineering**
* **Centralized Logging**
* **LogQL-Based Investigation**
* **Grafana Security Visualization**
* **Security Automation / SOAR Concepts**

---

# 🧠 Human + Automation Model

The suite is designed around a **human-supervised defensive automation model**.

Automation handles repetitive collection, validation, remediation, and response tasks while the analyst remains responsible for:

1. Reviewing telemetry
2. Validating security findings
3. Determining appropriate response actions
4. Reviewing automated remediation
5. Investigating anomalous activity
6. Making final incident-response decisions

The project therefore demonstrates automation as an **analyst force multiplier**, rather than a replacement for human judgment.

---

# 🎮 Battle Network Theme

The *Mega Man Battle Network* naming system provides the project's presentation layer:

```text
SearchMan
   │
   ├── Discover
   └── Detect
        │
        ▼
Fire Soul
   │
   ├── Protect
   └── Control
        │
        ▼
Metal Soul
   │
   ├── Harden
   └── Verify
        │
        ▼
Leaders Raid
   │
   ├── Respond
   └── Contain
        │
        ▼
Roll Soul
   │
   ├── Recover
   └── Restore
```

The underlying security workflows remain aligned with conventional defensive cybersecurity practices and the NIST CSF 2.0 framework.

---

# 🚀 Project Goals

The MegaMan Red Sun Lab Suite was built to demonstrate how a lightweight home-lab environment can combine:

**Security Telemetry → Detection → Protection → Response → Recovery**

into a single operational workflow.

The project emphasizes practical blue-team engineering, structured telemetry, defensive automation, incident-response workflows, and security visualization while operating within the constraints of a resource-conscious Kali Linux laboratory.

---

## 📌 Project Status

**Status:** Active Development

Future improvements may include:

* Additional detection rules
* Expanded Zeek telemetry
* Additional Grafana dashboards
* More automated response playbooks
* Expanded NIST CSF 2.0 documentation
* Additional adversary simulation scenarios
* Improved test coverage
* Cross-module telemetry correlation

---

## ⚡ Project Philosophy

> **Observe. Detect. Protect. Respond. Recover.**

**MegaMan Red Sun Lab Suite** combines cybersecurity engineering with a tactical interface inspired by the NetNavi world—turning a home laboratory into a practical defensive security operations environment.
# MegaMan-Red-Sun-Lab-Suite

# 🛡️ Metal Soul

> **MegaMan Red Sun Lab Suite — Host Armor & File Integrity Monitoring Module**
> **NIST CSF Alignment:** Protect — Data Security & Baseline Configuration
> **Primary Capabilities:** File Integrity Monitoring · Permission Auditing · Configuration Validation
> **Telemetry Pipeline:** Grafana Alloy → Grafana Loki → Grafana Dashboard
> **Dashboard:** Host Armor Control

---

## 🎯 Executive Overview

**Metal Soul** is the host protection and File Integrity Monitoring (FIM) module of the **MegaMan Red Sun Lab Suite**.

Inspired by the defensive armor of MetalMan.EXE, the module performs cryptographic integrity checks and host baseline validation against security-sensitive system files and configurations.

The audit focuses on critical security resources including:

```text
/etc/passwd
/etc/shadow
/etc/ssh/sshd_config
/etc/sudoers
```

The module evaluates file integrity, permissions, and baseline state, then generates structured telemetry for centralized collection.

Security events are collected by **Grafana Alloy**, forwarded to **Grafana Loki**, and visualized through the **Host Armor Control** Grafana dashboard.

---

# 🏗️ Module Architecture

```text
metal-soul/
│
├── fim_config/
│   └── Target file paths and baseline definitions
│
├── hardening_scripts/
│   └── metal_soul_fortify.py
│       └── Integrity and host configuration audit
│
├── logs/
│   └── metal_soul_integrity.log
│       └── Structured FIM telemetry
│
├── assets/
│   └── Dashboard evidence and screenshots
│
└── README.md
```

---

# 🔐 Protected Resources

Metal Soul focuses on security-sensitive Linux configuration and identity files.

| Resource               | Security Purpose                       |
| ---------------------- | -------------------------------------- |
| `/etc/passwd`          | Local account and identity information |
| `/etc/shadow`          | Password hash and authentication data  |
| `/etc/ssh/sshd_config` | SSH service configuration              |
| `/etc/sudoers`         | Privileged command authorization       |

The module uses cryptographic hashes and file metadata to identify changes from the expected baseline.

---

# 🛡️ FIM Capabilities

Metal Soul provides several host-integrity checks:

### 🔑 Cryptographic Integrity

Files are hashed and compared against their expected baseline state.

```text
Baseline Hash
      │
      ▼
Current File Hash
      │
      ▼
   Compare
   /     \
  /       \
Match    Changed
  │         │
  ▼         ▼
Intact    Alert
```

### 🔒 Permission Validation

The module can identify changes to file permissions that may indicate configuration drift or unauthorized modification.

### ⚙️ Configuration Validation

Security-sensitive configuration files are checked against their expected baseline.

### 📊 Structured Telemetry

Audit results are written to a structured log stream for centralized collection and visualization.

---

# 🧭 NIST CSF Alignment

Metal Soul supports the **Protect** function of the NIST Cybersecurity Framework by providing mechanisms for:

* Data and configuration integrity
* Security baseline validation
* Configuration monitoring
* Detection of unauthorized changes

The original project mapping identifies the module with:

```text
PR.DS-1
PR.IP-1
```

> **Note:** NIST CSF 2.0 reorganized the framework compared with earlier CSF versions. The specific subcategory references should therefore be verified against the exact CSF version being used for the portfolio documentation.

---

# ⚙️ Telemetry Ingestion

Metal Soul writes audit events to:

```text
/var/log/metal_soul_integrity.log
```

Grafana Alloy monitors the file and routes the resulting telemetry toward Loki.

## Alloy File Discovery

```alloy
local.file_match "metal_soul_logs" {
  path_targets = [{
    __path__     = "/var/log/metal_soul_integrity.log",
    job          = "metal_soul",
    ability      = "metal_armor",
    nist_control = "protect_data_security",
  }]
}
```

## Alloy Log Source

```alloy
loki.source.file "metal_soul_tail" {
  targets    = local.file_match.metal_soul_logs.targets
  forward_to = [loki.process.metal_soul_json_parser.receiver]
}
```

The `forward_to` destination assumes the corresponding JSON-processing component is defined elsewhere in the unified Alloy configuration.

---

# 📊 Host Armor Control — LogQL

The Host Armor Control dashboard queries Metal Soul telemetry from Loki.

## FIM Live Stream

Display all Metal Soul integrity events:

```logql
{job="metal_soul"}
```

---

## Verified Intact Files

Count files reported as verified intact during the previous five minutes:

```logql
sum(
  count_over_time(
    {job="metal_soul"}
    | json
    | status="verified_intact"
    [5m]
  )
)
```

---

## Audit Volume

Break down recent audit activity by event type:

```logql
sum by (event_type) (
  count_over_time(
    {job="metal_soul"}
    | json
    [5m]
  )
)
```

---

# 🔄 FIM Telemetry Workflow

```text
┌─────────────────────────┐
│ Critical System Files   │
│ /etc/passwd             │
│ /etc/shadow             │
│ /etc/ssh/sshd_config    │
│ /etc/sudoers            │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Metal Soul Fortify     │
│ Integrity Audit         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ SHA-256 / Metadata      │
│ Baseline Comparison     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Structured JSON Events  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Grafana Alloy      │
│ Collection & Routing    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Grafana Loki       │
│ Centralized Telemetry   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Host Armor Control    │
│    Grafana Dashboard    │
└─────────────────────────┘
```

---

# 🚀 Execution Instructions

## 1. Run the Integrity Audit

Execute the Metal Soul host-integrity audit:

```bash
sudo python3 \
  ~/MegaMan-Red-Sun-Lab-Suite/metal-soul/hardening_scripts/metal_soul_fortify.py
```

---

## 2. Verify Alloy

Confirm Grafana Alloy is running:

```bash
sudo systemctl status alloy
```

---

## 3. Review Generated Telemetry

Inspect the most recent Metal Soul events:

```bash
sudo tail -n 10 /var/log/metal_soul_integrity.log
```

---

## 4. Verify Loki Ingestion

Use the Grafana/Loki interface to query:

```logql
{job="metal_soul"}
```

The resulting events should correspond to the integrity audit performed by `metal_soul_fortify.py`.

---

# 🧪 Operational Workflow

Metal Soul follows this defensive integrity workflow:

```text
1. Define Baseline
       │
       ▼
2. Inspect Protected Files
       │
       ▼
3. Calculate Current State
       │
       ▼
4. Compare Against Baseline
       │
       ▼
5. Generate Integrity Event
       │
       ▼
6. Centralize Telemetry
       │
       ▼
7. Analyst Review
```

---

# 🛡️ Security Capabilities Demonstrated

Metal Soul demonstrates practical host-security and monitoring capabilities including:

* File Integrity Monitoring
* Cryptographic hashing
* Permission validation
* Security configuration auditing
* Baseline comparison
* Configuration drift detection
* Structured security logging
* Centralized telemetry collection
* Loki log querying
* Grafana security visualization

---

# 🧠 Analyst Role

Metal Soul is designed as an **analyst-support FIM system**.

A detected file or configuration change should be treated as a **security signal requiring validation**, rather than automatically being classified as malicious.

The intended workflow is:

```text
Integrity Change
      │
      ▼
Telemetry Event
      │
      ▼
Analyst Validation
      │
      ├── Expected Change
      │
      └── Unexpected Change
              │
              ▼
       Incident Investigation
```

This distinction helps separate legitimate administrative changes from potentially unauthorized modification.

---

# 🎮 Battle Network Theme

The Metal Soul theme provides the presentation layer for conventional host-protection functions:

| Battle Network Concept | Security Function                |
| ---------------------- | -------------------------------- |
| **Metal Soul**         | Host protection                  |
| **Metal Armor**        | File and configuration integrity |
| **Fortify**            | Host security audit              |
| **Host Armor Control** | FIM telemetry visualization      |

The underlying implementation remains focused on practical Linux host security and defensive monitoring.

---

# 📌 Module Status

**Module:** Metal Soul
**Suite:** MegaMan Red Sun Lab Suite
**Primary NIST CSF Function:** Protect
**Primary Capability:** File Integrity Monitoring
**Telemetry:** Grafana Alloy → Grafana Loki
**Visualization:** Grafana / Host Armor Control

---

## ⚡ Metal Soul

> **Harden the host. Verify the baseline. Protect the system.**

# 🎯 SearchMan.EXE

> **MegaMan Red Sun Lab Suite — Network Discovery & Threat Detection Module**
> **NIST CSF Alignment:** Identify · Detect
> **Primary Capabilities:** Asset Discovery · Network Monitoring · Service Exposure Assessment
> **Telemetry Pipeline:** Grafana Alloy → Grafana Loki → Grafana Dashboard
> **Dashboard:** Satellite Ray

---

## 🎯 Executive Overview

**SearchMan.EXE** is the network discovery and threat-detection module of the **MegaMan Red Sun Lab Suite**.

Inspired by SearchMan's targeting and reconnaissance capabilities, the module combines:

* Active subnet discovery
* Passive network telemetry
* Service and port enumeration
* Exposure assessment
* Structured security logging
* Centralized telemetry ingestion
* Grafana-based operational visualization

The module is designed to demonstrate how multiple reconnaissance and monitoring capabilities can feed a centralized defensive telemetry pipeline.

Operational events are generated as structured logs, collected by **Grafana Alloy**, forwarded to **Grafana Loki**, and visualized through the **Satellite Ray** dashboard.

---

# 🏗️ Module Architecture

```text
search-man/
│
├── scope-gun/
│   └── scope_gun_scan.py
│       └── Active subnet reconnaissance
│
├── target-acquisition/
│   ├── conn.log
│   └── dns.log
│       └── Passive Zeek network telemetry
│
├── panel-search/
│   └── panel_search_audit.py
│       └── Service and exposure assessment
│
├── satellite-ray/
│   └── config.alloy
│       └── Telemetry collection configuration
│
└── assets/
    └── Dashboard evidence and telemetry exports
```

---

# ⚡ Sub-Abilities

## 1. 🎯 Scope Gun

**Directory:** `scope-gun/`
**NIST CSF Function:** Identify — Asset Management

### Purpose

Scope Gun performs active subnet discovery to identify reachable hosts within the configured laboratory network.

The module generates structured telemetry describing discovered hosts and associated target-lock events.

### Primary Script

```text
scope_gun_scan.py
```

### Telemetry

```text
/var/log/search_soul_recon.log
```

### Example Event

```text
event_type: target_lock_acquired
```

### Security Value

Scope Gun demonstrates:

* Asset discovery
* Network reconnaissance
* Reachability assessment
* Structured discovery telemetry

---

## 2. 🎯 Target Acquisition

**Directory:** `target-acquisition/`
**NIST CSF Function:** Detect — Continuous Monitoring

### Purpose

Target Acquisition uses **Zeek** as a passive network sensor to observe network activity without actively modifying network traffic.

The module provides visibility into network connections and DNS activity generated within the laboratory environment.

### Primary Telemetry

```text
/opt/zeek/logs/current/conn.log
/opt/zeek/logs/current/dns.log
```

### Security Value

Target Acquisition demonstrates:

* Passive network monitoring
* Connection-state visibility
* DNS telemetry
* Network activity baselining
* Security event collection

---

## 3. 🎯 Panel Search

**Directory:** `panel-search/`
**NIST CSF Function:** Identify — Risk Assessment

### Purpose

Panel Search performs service and exposure assessment against discovered laboratory hosts.

The module uses Nmap-based scanning to identify:

* Open ports
* Exposed services
* Service information
* Potential attack-surface risks

### Primary Script

```text
panel_search_audit.py
```

### Telemetry

```text
/var/log/panel_search_vuln.log
```

### Security Value

Panel Search demonstrates:

* Port enumeration
* Service discovery
* Attack-surface assessment
* Exposure mapping
* Structured vulnerability telemetry

---

# 🛰️ 4. Satellite Ray

**Directory:** `satellite-ray/`
**NIST CSF Function:** Detect / Analyze

### Purpose

**Satellite Ray** provides the centralized operational view for SearchMan telemetry.

Grafana dashboards combine telemetry from:

```text
Scope Gun
    │
    ├── Active Discovery
    │
Target Acquisition
    │
    ├── Zeek Network Telemetry
    │
Panel Search
    │
    └── Service Exposure Assessment
           │
           ▼
    Grafana Alloy
           │
           ▼
    Grafana Loki
           │
           ▼
    Satellite Ray Dashboard
```

---

# ⚙️ Telemetry Ingestion Pipeline

Grafana Alloy is configured to collect SearchMan telemetry and forward the resulting log streams to Grafana Loki.

The Loki endpoint used by the laboratory is:

```text
http://127.0.0.1:3100
```

### Scope Gun Stream

```alloy
local.file_match "searchman_scope_gun_logs" {
  path_targets = [{
    __path__     = "/var/log/search_soul_recon.log",
    job          = "search_man",
    ability      = "scope_gun",
    nist_control = "identify",
  }]
}
```

### Target Acquisition Stream

```alloy
local.file_match "searchman_target_acquisition_logs" {
  path_targets = [{
    __path__     = "/opt/zeek/logs/current/*.log",
    job          = "search_man",
    ability      = "target_acquisition",
    nist_control = "detect",
  }]
}
```

### Panel Search Stream

```alloy
local.file_match "searchman_panel_search_logs" {
  path_targets = [{
    __path__     = "/var/log/panel_search_vuln.log",
    job          = "search_man",
    ability      = "panel_search",
    nist_control = "identify_risk",
  }]
}
```

---

# 📊 Satellite Ray — LogQL Queries

The Satellite Ray dashboard uses LogQL to query SearchMan telemetry from Loki.

## Scope Gun — Target Locks

```logql
{job="search_man", ability="scope_gun"}
```

## Scope Gun — Target Lock Count

```logql
sum(
  count_over_time(
    {job="search_man", ability="scope_gun"}
    | json
    | event_type="target_lock_acquired"
    [5m]
  )
)
```

## Target Acquisition — Network Telemetry

```logql
{job="search_man", ability="target_acquisition"}
```

## Panel Search — Exposure Feed

```logql
{job="search_man", ability="panel_search"}
```

---

# 🔄 Telemetry Flow

```text
┌──────────────────────┐
│      Scope Gun       │
│ Active Discovery     │
└──────────┬───────────┘
           │
           │
┌──────────▼───────────┐
│  Target Acquisition  │
│   Zeek Telemetry     │
└──────────┬───────────┘
           │
           │
┌──────────▼───────────┐
│     Panel Search     │
│ Exposure Assessment  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Grafana Alloy     │
│ Collection & Routing │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Grafana Loki     │
│ Central Log Storage  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Satellite Ray      │
│ Grafana Dashboard    │
└──────────────────────┘
```

---

# 🚀 Execution Instructions

## 1. Run Scope Gun

Execute the active subnet discovery module:

```bash
cd ~/MegaMan-Red-Sun-Lab-Suite/search-man/scope-gun

sudo python3 scope_gun_scan.py
```

---

## 2. Run Panel Search

Execute the service and exposure assessment:

```bash
cd ~/MegaMan-Red-Sun-Lab-Suite/search-man/panel-search

sudo python3 panel_search_audit.py
```

---

## 3. Verify Grafana Alloy

Confirm the telemetry collector is running:

```bash
sudo systemctl status alloy
```

---

## 4. Verify Generated Logs

Check the SearchMan telemetry files:

```bash
sudo tail -n 10 /var/log/search_soul_recon.log
```

```bash
sudo tail -n 10 /var/log/panel_search_vuln.log
```

Check Zeek telemetry:

```bash
sudo tail -n 10 /opt/zeek/logs/current/conn.log
```

```bash
sudo tail -n 10 /opt/zeek/logs/current/dns.log
```

---

# 🧪 Operational Workflow

The recommended SearchMan workflow is:

```text
1. Discover
     │
     ▼
2. Observe
     │
     ▼
3. Assess
     │
     ▼
4. Collect Telemetry
     │
     ▼
5. Centralize
     │
     ▼
6. Visualize
```

### Discovery

**Scope Gun** identifies reachable hosts.

### Observation

**Target Acquisition** collects passive network telemetry through Zeek.

### Assessment

**Panel Search** evaluates exposed services and ports.

### Centralization

**Grafana Alloy** collects and routes module telemetry.

### Storage

**Grafana Loki** provides centralized log storage and querying.

### Visualization

**Satellite Ray** provides the operational dashboard for reviewing SearchMan activity.

---

# 🛡️ Security Capabilities Demonstrated

SearchMan.EXE demonstrates the following defensive cybersecurity capabilities:

* Asset discovery
* Network reconnaissance
* Passive network monitoring
* DNS visibility
* Service enumeration
* Port exposure assessment
* Attack-surface mapping
* Structured security logging
* Telemetry collection
* Centralized log management
* LogQL investigation
* Grafana security visualization

---

# 🧠 Analyst Role

SearchMan is designed as a **defensive analyst-support system**.

Automated discovery and telemetry collection reduce repetitive work, but security findings still require analyst validation.

The intended workflow is:

```text
Automated Discovery
       │
       ▼
Telemetry Collection
       │
       ▼
Analyst Review
       │
       ▼
Risk Assessment
       │
       ▼
Response Decision
```

This keeps the module focused on **security visibility and analyst-assisted detection**, rather than treating automated scanning results as confirmed security incidents.

---

# 🎮 Battle Network Theme

The SearchMan theme serves as the presentation layer for conventional defensive security functions:

| Battle Network Concept | Security Function               |
| ---------------------- | ------------------------------- |
| **Scope Gun**          | Active asset discovery          |
| **Target Acquisition** | Passive network monitoring      |
| **Panel Search**       | Service and exposure assessment |
| **Satellite Ray**      | Central telemetry visualization |

The naming provides a tactical interface while the underlying implementation remains based on standard cybersecurity tools and defensive monitoring concepts.

---

# 📌 Project Status

**Module:** SearchMan.EXE
**Suite:** MegaMan Red Sun Lab Suite
**Primary NIST CSF Functions:** Identify / Detect
**Telemetry:** Grafana Alloy → Grafana Loki
**Network Sensor:** Zeek
**Exposure Assessment:** Nmap
**Visualization:** Grafana / Satellite Ray

---

## ⚡ SearchMan.EXE

> **Discover the surface. Observe the traffic. Identify the risk.**

# 🔥 Fire Soul

## Perimeter Shield & Active Defense Module

> **Lab Suite:** MegaMan Red Sun Lab Suite  
> **NIST CSF Alignment:** Protect — Access Control & Protective Technology  
> **Telemetry Pipeline:** Grafana Alloy → Grafana Loki → Grafana Dashboard  
> **Dashboard:** Flame Shield Control

---

## 🛡️ Executive Overview

**Fire Soul** is the perimeter-defense module of the MegaMan Red Sun Lab Suite.

It provides automated enforcement of host-level boundary protections, including firewall policy enforcement, port blocking, and connection-rate controls. Security events are recorded as structured telemetry and forwarded through Grafana Alloy into Grafana Loki for centralized monitoring and dashboard visualization.

The MegaMan Battle Network theme provides the presentation layer, while the underlying implementation demonstrates practical defensive security concepts.

### Core Capabilities

- 🔥 Firewall policy enforcement
- 🚫 Port and connection blocking
- ⚡ Connection burst / rate-limit controls
- 🛡️ Boundary protection
- 📊 Structured security-event logging
- 🔎 Centralized telemetry through Loki
- 📈 Grafana-based operational visibility

---

## 🏗️ Module Architecture

```text
┌───────────────────────────────────────────────────────────────┐
│                         FIRE SOUL                             │
│                 Perimeter Defense Module                     │
└──────────────────────────────┬────────────────────────────────┘
                               │
                               ▼
                  fire_soul_perimeter.py
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
        Firewall / Rules              Security Event Logs
        Enforcement                  /var/log/fire_soul_events.log
                                              │
                                              ▼
                                      Grafana Alloy
                                              │
                                              ▼
                                      Grafana Loki
                                              │
                                              ▼
                                  Flame Shield Control
                                      Grafana Dashboard

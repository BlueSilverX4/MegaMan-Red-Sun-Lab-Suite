# ⚔️ Leaders Raid

## Dual-Squad Automated Incident Response (SOAR) Module

> **Lab Suite:** MegaMan Red Sun Lab Suite  
> **NIST CSF Alignment:** Respond — Incident Analysis & Mitigation  
> **Telemetry Pipeline:** Grafana Alloy → Grafana Loki → Grafana Dashboard  
> **Dashboard:** Leaders Raid Control

---

## 🎯 Executive Overview

**Leaders Raid** is the incident-response orchestration component of the MegaMan Red Sun Lab Suite.

The module provides a controlled Security Orchestration, Automation, and Response (SOAR) workflow for executing predefined defensive response actions.

Inspired by the tactical coordination of **ProtoMan.EXE** and **Colonel.EXE**, Leaders Raid separates response responsibilities into two conceptual squads:

- 🔴 **ProtoMan.EXE — Delta Ray Edge:** Rapid host-focused response and threat triage.
- 🔵 **Colonel.EXE — Screen Divide:** Perimeter-focused containment and access-control response.

The MegaMan terminology provides the presentation layer, while the underlying workflow demonstrates practical incident-response orchestration and defensive automation.

---

# ⚔️ Dual-Squad Response Model

```text
                    SECURITY INCIDENT
                           │
                           ▼
                  Leaders Raid SOAR
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       🔴 ProtoMan Squad          🔵 Colonel Squad
       Host Response              Perimeter Response
              │                         │
              ▼                         ▼
       ┌──────────────┐          ┌──────────────┐
       │ Threat       │          │ Perimeter    │
       │ Triage       │          │ Containment  │
       ├──────────────┤          ├──────────────┤
       │ Isolation    │          │ Firewall     │
       │ Process      │          │ Blocking     │
       │ Response     │          │ Session      │
       │ Validation   │          │ Revocation   │
       └──────┬───────┘          └──────┬───────┘
              │                         │
              └────────────┬────────────┘
                           ▼
                    Response Telemetry
                           │
                           ▼
                    Grafana Alloy
                           │
                           ▼
                    Grafana Loki
                           │
                           ▼
                 Leaders Raid Control

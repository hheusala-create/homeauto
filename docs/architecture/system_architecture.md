# System Architecture

This document defines the target architecture for the home automation system.

It builds on the project core principles:
- physical wall switches must always work
- Shelly is the primary control layer
- IKEA Tradfri is a secondary layer
- critical infrastructure must be protected
- Google Home room structure is the source of truth
- the system must remain usable offline
- hardware control, logic, UI, and voice should stay separated

See also: `docs/architecture/core_principles.md`

---

## 1. Architecture overview

The system is built in layers:

```text
Physical switches
      ↓
   Shelly devices
      ↓
Lights / sockets / critical loads

Tradfri bulbs ──────────────┐
                            ↓
                    Home Assistant
                            ↓
        Logical entities / automations / protections
                            ↓
         Google Home / dashboards / voice / optional Matter

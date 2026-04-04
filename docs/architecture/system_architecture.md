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
- MQTT should be used first where practical
- Home Assistant OS is the initial central platform
- the system must remain portable, recoverable, and migratable

See also: `docs/architecture/core_principles.md`
See also: `docs/architecture/layers.md`

---

## 1. Architecture overview

The system is built in layers:

Physical switches / electrical wiring  
↓  
Shelly devices  
↓  
Lights / sockets / critical loads  

Tradfri bulbs and other smart endpoints  
↓  
Local network and communication  
(MQTT first, local integrations, selective Matter, minimal cloud)  
↓  
Home Assistant OS  
↓  
Home Assistant central logic  
↓  
Logical entities / automations / scenes  
↓  
Google Home / dashboards / voice / UI  

The central design idea is:

- physical use must still work without apps
- Home Assistant is the main local brain
- MQTT is the preferred messaging approach where practical
- cloud is optional, not foundational
- critical fallback logic can live on devices when needed

---

## 2. Central design model

The house is not cloud-centered.

The primary smart-home brain is:
- local
- inside the house
- controlled by the user

Home Assistant running on Home Assistant OS is the main central logic layer.

This means:
- central logic is allowed and expected
- cloud services are optional enhancements
- if internet is down, the local system should still function
- normal automations are expected to live primarily in Home Assistant

---

## 3. Device-local fallback model

Local device-side logic is not the default place for normal automations.

Instead:
- normal automation logic belongs in Home Assistant
- device-local scripts are reserved for critical fallback and recovery cases

Examples:
- FTTH auto-recovery after accidental power-off
- safety timers for critical infrastructure
- last-resort local recovery behavior

---

## 4. Communication model

Preferred communication order:

1. MQTT where practical
2. stable local/native integrations where MQTT is not practical
3. Matter selectively
4. cloud integrations only when needed

---

## 5. Control model

The home has multiple control layers but must behave as one system.

- Physical layer (switches, wiring)
- Hardware control layer (Shelly, bulbs)
- Logical layer (Home Assistant)
- User layer (UI, voice, dashboards)

---

## 6. Lighting model

Each circuit must be classified:

- relay_only
- smart_bulb_only
- shelly_plus_smart_bulb
- critical_power
- socket

---

## 7. Critical infrastructure model

Critical devices:
- must be protected
- must not be exposed casually
- must have recovery logic

---

## 8. Portability and migration model

System must support:
- hardware migration (laptop → mini PC)
- platform migration (HA OS → Linux/Node-RED)

---

## 9. Backup and rollback model

System must:
- support automatic backups
- allow rollback
- restore fully on new hardware

---

## 10. Documentation model

Documentation must include:
- architecture
- devices
- integrations
- MQTT structure
- recovery steps
- migration steps

---

## 11. Operational model

System must be:
- reliable
- maintainable
- understandable
- recoverable
- portable

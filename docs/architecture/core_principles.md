# Core Principles

This document defines the fundamental design principles of the home automation system.

---

## 1. Physical control always works

Lights must always work from normal wall switches.

The system must not depend on:
- internet
- Home Assistant
- apps

The house must behave like a normal house first.

---

## 2. Shelly is the primary control layer

Shelly devices are installed behind switches and form the foundation of the system.

They:
- control power
- maintain smart control
- preserve normal switch behavior

---

## 3. IKEA Tradfri is a secondary layer

IKEA Tradfri is used for:
- multi-bulb setups
- partial lighting
- dimming and ambiance

It must not break normal switch usability.

---

## 4. Control layers must not conflict

Two layers exist:
- Shelly (power / switch)
- IKEA (bulb logic)

The system must avoid:
- loss of power to smart bulbs unintentionally
- inconsistent states between systems

---

## 5. Critical infrastructure must be protected

Devices such as network power must:
- not be easily accessible
- not be visible in normal UI
- have recovery mechanisms

---

## 6. Google Home defines rooms

Room structure is defined in Google Home and used as the source of truth across all systems.

---

## 7. Naming must be consistent

Format:
<room>_<object>_<type>

Examples:
- kitchen_ceiling_light
- bedroom_socket_left

Rules:
- English only
- no duplicates
- no vague names

---

## 8. Inventory-first approach

All devices must be discovered and documented before configuration.

---

## 9. System must be portable

The system must support:
- migration to new hardware
- backup and restore

---

## 10. Offline-first design

Core functionality must work without internet.

Cloud services are optional enhancements.

---

## 11. Separation of concerns

Keep separate:
- devices
- logic
- UI
- voice control

---

## 12. Safe failure behavior

If something fails:
- lights must still work
- switches must still work
- system must remain usable

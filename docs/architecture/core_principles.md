
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
- provide electrical control
- detect physical switch input
- enable local automation

Shelly should be considered the hardware truth layer.

---

## 3. IKEA Tradfri is a secondary layer

IKEA Tradfri is used for:
- multi-bulb setups
- dimming and ambiance
- grouped lighting

It must not break normal switch usability.

---

## 4. Control layers must not conflict

Two layers exist:
- Shelly (power / switch / input)
- IKEA (bulb logic)

The system must avoid:
- loss of power to smart bulbs unintentionally
- inconsistent states between systems
- duplicate or confusing device representations

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

---

## 13. Logical user control should be unified

When multiple technical control layers exist for the same real-world function, users should normally see one logical control.

Examples:
- one room light with both Shelly and IKEA Tradfri involvement
- grouped lights behaving as one

Users must not need to understand technical layers.

---

## 14. Critical devices must be excluded from bulk actions

Critical infrastructure must never be affected by:
- turn off all
- away mode
- shutdown routines

Examples:
- FTTH / network core
- infrastructure relays

---

## 15. Hardware truth and user abstraction must be separate

Keep separate:
- hardware entities (real electrical control)
- logical entities (user-facing)

This is critical for Shelly + Tradfri combined setups.

---

## 16. Native integrations first

Prefer native/local integrations over Matter or cloud.

Reason:
- better reliability
- better debugging
- full feature support
- offline capability

Matter/cloud = secondary layer only.

---

## 17. Smart bulbs and wall switches

Rule: Smart bulbs must not lose power due to wall switches.

Background:
- Smart bulbs (e.g. IKEA TRÅDFRI) go offline if power is cut
- This creates duplicates, delays, and unreliable control

Design rule:
- Smart bulbs must always have constant power

Implementation:
- Shelly relay must remain ON for smart-bulb circuits
- Wall switch must be used as input only (detached mode)
- Home Assistant handles actual light control

Behavior:
1. user presses wall switch
2. Shelly detects input
3. Home Assistant toggles light

---

## 18. Mixed circuits must be explicitly classified

Each lighting circuit must be classified as one of:

- relay_only
- smart_bulb_only
- shelly_plus_smart_bulb
- critical_power
- socket

This classification defines how the system behaves.

---

## 19. No hidden behavior

All automations must be:
- predictable
- documented
- traceable

Avoid:
- silent overrides
- conflicting automations

---

## 20. System must be debuggable

At any time, it must be possible to determine:
- what controls a device
- where power comes from
- what triggered a change

Logs and structure must support troubleshooting.

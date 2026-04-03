# Home Automation Architecture Layers

## Purpose
This file describes the target architecture layers for the home automation system so that future work stays aligned with the core principles.

## Guiding rules
- Normal wall switches must always work for lights.
- Shelly is the primary control layer for switched lights and switched sockets.
- IKEA TRÅDFRI remains a secondary control layer where individual bulbs inside a larger lighting group must be controlled separately.
- Critical connectivity devices must be protected from accidental shutdown.
- Home Assistant becomes the central logic layer, not the only way to operate the home.
- The system must degrade gracefully: if Internet, cloud, voice, or one platform fails, basic use must still work.

---

## Layer 1: Physical power and wiring
This is the real electrical layer in the house.

Examples:
- wall switches
- relays behind switches
- power to bulbs
- power to critical network devices
- fixed wiring and circuits

Rules:
- manual switch use must remain possible
- lights must still turn on/off from normal switches
- no design may depend on cloud or app access for basic light use
- critical devices should not be easy to power off by mistake

---

## Layer 2: Device control hardware
This is the actual device layer that performs switching or device-side control.

Examples:
- Shelly Gen4 relays
- IKEA TRÅDFRI bulbs
- other smart plugs or controllers
- future Matter-capable end devices

Rules:
- Shelly is the main actuator for switched lighting circuits
- TRÅDFRI is used mainly where bulb-level control is needed
- avoid overlapping control logic that creates confusion
- for lights controlled by wall switch, Shelly should preserve reliable power/control behavior

---

## Layer 3: Local network and transport
This is how devices communicate.

Examples:
- Wi-Fi
- LAN IP addressing
- Matter transport where appropriate
- local APIs
- local discovery

Rules:
- prefer local communication where possible
- IP/device inventory must be documented
- critical network paths must be clearly identified
- FTTH power control is a special critical case and must be protected

Notes:
- FTTH controls the main fiber Internet path
- the fiber converter is behind it
- this device must auto-recover power after a short delay if switched off
- it should stay outside normal day-to-day control views to avoid accidental shutdown

---

## Layer 4: Platform integrations
This layer connects devices into the central automation platform.

Examples:
- Home Assistant integrations
- Shelly integration
- IKEA integration
- Matter integration
- vendor integrations for appliances and other systems

Rules:
- use the most stable integration first, not the most fashionable one
- Matter should be evaluated as a transport/standard layer, not automatically forced everywhere
- if a native integration is more complete and reliable than Matter, prefer the native integration
- integration choices must support the project core rules

Preferred approach:
- Shelly devices: primarily via Home Assistant Shelly integration unless Matter later proves equally complete and stable
- IKEA bulbs: integrate in a way that preserves bulb-level control where needed
- Matter: use selectively where it improves portability and simplicity without weakening reliability

---

## Layer 5: Entity and room model
This layer defines how devices are represented logically.

Examples:
- rooms
- device names
- light groups
- socket entities
- critical-device classification

Rules:
- room naming should follow Google Home room names where practical
- entity names must be understandable without technical knowledge
- critical devices must be explicitly labeled
- lighting entities must reflect real-life use, not just hardware structure

Examples:
- “Technical room light”
- “FTTH”
- “Laundry room table socket”
- “Living room ceiling light”
- “Kitchen desk lights”

---

## Layer 6: Automation and scenes
This layer contains logic and rules.

Examples:
- timers
- scenes
- auto-off
- safety logic
- recovery logic
- occupancy and schedule automations

Rules:
- automations must never break manual control
- failure of one automation must not make the home unusable
- critical recovery automations are allowed for network/power continuity
- automations should be easy to explain and document

Special case:
- FTTH auto-recovery script is acceptable because it protects connectivity after accidental shutoff

---

## Layer 7: User control surfaces
This is how people actually use the system.

Examples:
- normal wall switches
- Shelly app
- IKEA app
- Google Home
- future Home Assistant dashboards
- voice assistants
- physical buttons

Rules:
- normal switches are always the first fallback control surface
- for many switched lights, Shelly should be the primary smart control surface
- IKEA app/bulb-level control is secondary and only where genuinely useful
- avoid showing dangerous controls in normal everyday views
- dashboards should reflect how the house is actually used

Important design note:
Some lights currently have two smart control surfaces:
- Shelly controlling the switched circuit
- IKEA TRÅDFRI controlling the bulb itself

This must be modeled carefully so users understand:
- Shelly is the primary control path
- TRÅDFRI is secondary for partial-bulb/group behavior
- confusing duplicate controls should be minimized in future dashboards

---

## Layer 8: Documentation and operations
This layer keeps the system maintainable.

Examples

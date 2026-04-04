# Home Automation Architecture Layers

## Purpose
This file describes the target architecture layers for the home automation system so that future work stays aligned with the core principles.

## Guiding rules
- Normal wall switches must always work for lights.
- Shelly is the primary control layer for switched lights and switched sockets.
- IKEA TRÅDFRI remains a secondary control layer where individual bulbs inside a larger lighting group must be controlled separately.
- Critical connectivity devices must be protected from accidental shutdown.
- Home Assistant becomes the central logic layer, not the only way to operate the home.
- The system must degrade gracefully: if internet, cloud, voice, or one platform fails, basic use must still work.
- Security-critical devices must be modeled separately from normal convenience devices.

---

## Layer 1: Physical power and wiring
This is the real electrical layer in the house.

Examples:
- wall switches
- Shelly relays behind switches
- power to bulbs
- fixed outlets and circuits
- power to critical network devices
- power to appliances and ventilation equipment

Rules:
- manual switch use must remain possible
- lights must still turn on or off from normal switches where the circuit design requires that
- no design may depend on cloud or app access for basic light use
- critical devices should not be easy to power off by mistake

---

## Layer 2: Device control hardware
This is the actual device layer that performs switching, sensing, locking, or device-side control.

Examples:
- Shelly Gen4 relays
- IKEA TRÅDFRI bulbs
- IKEA sockets
- IKEA leak sensors
- Yale Wi-Fi lock
- Deltaco smart sockets
- Parmair ventilation unit
- Electrolux air purifiers
- Samsung washing machine
- Siemens oven, hob, and dishwasher
- Ecovacs robot vacuum
- Dreame robot mower
- LG C2 TV
- future Matter-capable end devices

Rules:
- Shelly is the main actuator for switched lighting circuits
- TRÅDFRI is used mainly where bulb-level control is needed
- avoid overlapping control logic that creates confusion
- for lights controlled by wall switch, Shelly should preserve reliable power and control behavior
- locks, sensors, and security devices must be tagged as security-critical or safety-related where applicable

---

## Layer 3: Local network and transport
This is how devices communicate.

Examples:
- Wi-Fi
- LAN IP addressing
- 2.4 GHz IoT connectivity
- extenders and sub-Wi-Fi segments
- local APIs
- local discovery
- Matter transport where appropriate
- MQTT where practical

Rules:
- prefer local communication where possible
- IP and device inventory must be documented
- critical network paths must be clearly identified
- Wi-Fi placement and SSID dependency must be documented for devices that require them
- FTTH power control is a special critical case and must be protected

Current network notes:
- `koti` = normal 2.4 GHz path for IoT devices such as Yale
- `koti56` = higher-band Wi-Fi for client devices where suitable
- `koti-ext` = extender-backed path currently used by the Parmair ventilation unit

Special critical note:
- FTTH controls the main fiber internet path
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
- Yale integration
- SmartThings integration
- Home Connect integration
- Electrolux integration
- Deltaco integration
- Ecovacs integration
- Dreame integration
- Matter integration
- MQTT integration
- vendor integrations for appliances, media devices, and other systems

Rules:
- use the most stable integration first, not the most fashionable one
- Matter should be evaluated as a transport and standards layer, not automatically forced everywhere
- if a native integration is more complete and reliable than Matter, prefer the native integration
- cloud integrations are acceptable where no good local route exists, but must be documented as cloud-dependent
- integration choices must support the project core rules

Preferred approach:
- Shelly devices: primarily via Home Assistant Shelly integration unless Matter later proves equally complete and stable
- IKEA devices: integrate in a way that preserves bulb-level control and future sensor support where needed
- Yale lock: integrate in a way that preserves stable lock status and controlled lock actions, with security-first UI handling
- Parmair ventilation: prefer local browser or API route if available; document exact access method and its Ethernet-to-extender dependency
- Siemens appliances: Home Connect path first unless a better supported local route appears later
- Samsung washing machine: SmartThings path first
- Electrolux air purifiers: use the most reliable supported integration, likely vendor-cloud-backed initially
- Deltaco sockets, Ecovacs, Dreame: document current vendor path first and revisit local alternatives later
- LG C2 TV: prefer a stable native integration path and document the direct Ethernet connection
- Matter: use selectively where it improves portability and simplicity without weakening reliability

---

## Layer 5: Entity and room model
This layer defines how devices are represented logically.

Examples:
- rooms
- device names
- light groups
- socket entities
- lock entities
- appliance entities
- environmental entities
- critical-device classification

Rules:
- room naming should follow Google Home room names where practical
- entity names must be understandable without technical knowledge
- critical devices must be explicitly labeled
- lighting entities must reflect real-life use, not just hardware structure
- cloud-backed devices must be marked in documentation
- dangerous actions should not appear in ordinary entity naming or default dashboards

Current room list observed from Google Home screenshots:
- Attic
- Backyard
- Bathroom
- Bedroom
- Closet
- Corridor
- Dining Room
- Front Yard
- Hall
- Hobby Room
- Kitchen
- Laundry room
- Living Room
- Office
- Sauna
- Technical room
- Warehouse
- WC

Examples:
- `hall_front_door_lock`
- `laundry_room_washing_machine`
- `technical_room_light`
- `bedroom_air_purifier`
- `living_room_tv_socket`

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
- ventilation mode routines
- lock notifications
- leak alerts

Rules:
- automations must never break manual control
- failure of one automation must not make the home unusable
- critical recovery automations are allowed for network and power continuity
- automations should be easy to explain and document
- do not create casual automatic door unlock behavior
- security automations should prefer alerts, checks, and confirmations over silent actions

Special cases:
- FTTH auto-recovery script is acceptable because it protects connectivity after accidental shutoff
- Yale lock automations should start with lock-state monitoring, reminders, and notifications before any more advanced behavior

---

## Layer 7: User control surfaces
This is how people actually use the system.

Examples:
- normal wall switches
- Shelly app
- IKEA app
- Yale app
- Google Home
- future Home Assistant dashboards
- voice assistants
- physical buttons
- vendor apps for appliances, robots, and air treatment devices

Rules:
- normal switches are always the first fallback control surface
- for many switched lights, Shelly should be the primary smart control surface
- IKEA app or bulb-level control is secondary and only where genuinely useful
- avoid showing dangerous controls in normal everyday views
- dashboards should reflect how the house is actually used
- security-critical actions should be separated from everyday controls

Important design note:
Some real-world functions currently have multiple smart control surfaces:
- Shelly controlling the switched circuit
- IKEA TRÅDFRI controlling the bulb itself
- Google Home exposing grouped user-facing controls
- vendor apps still controlling cloud devices directly

This must be modeled carefully so users understand:
- Shelly is the primary control path for switched circuits
- TRÅDFRI is secondary for partial-bulb or grouped-light behavior
- Home Assistant should become the main unified view over time
- confusing duplicate controls should be minimized in future dashboards

---

## Layer 8: Documentation and operations
This layer keeps the system maintainable.

Examples:
- architecture documents
- room inventory
- device inventory
- IP and SSID inventory
- integration inventory
- MQTT topic structure
- backup procedures
- restore procedures
- migration procedures
- cloud dependency list
- security-critical device list

Rules:
- every device family must be documented before heavy automation work starts
- each device should have a known room, integration path, and fallback behavior
- critical devices must have recovery steps written down
- the documentation must stay migration-friendly so the system can move later from laptop to mini PC or from HA OS to another supported platform model

Operational priority list:
1. document rooms and devices
2. document which devices are local vs cloud-dependent
3. document which devices are critical or security-sensitive
4. document the chosen Home Assistant integration path for each family
5. keep backups and restore steps current

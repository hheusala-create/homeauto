# System Architecture

This document defines the target architecture for the home automation system.

It builds on the project core principles:
- physical wall switches must always work
- Shelly is the primary control layer
- IKEA TRÅDFRI is a secondary layer
- critical infrastructure must be protected
- Google Home room structure is the source of truth
- the system must remain usable offline where practical
- hardware control, logic, UI, and voice should stay separated
- MQTT should be used first where practical
- Home Assistant OS is the initial central platform
- the system must remain portable, recoverable, and migratable
- security-critical devices must be modeled separately
- cloud dependencies must be made explicit

See also: `core_principles_updated.md`
See also: `layers_updated.md`

---

## 1. Architecture overview

The system is built in layers:

Physical switches / electrical wiring  
↓  
Shelly devices and other endpoint hardware  
↓  
Lights / sockets / locks / appliances / robots / environmental devices  

TRÅDFRI bulbs, sockets, leak sensors, and other smart endpoints  
↓  
Local network and communication  
(MQTT first, local integrations, selective Matter, minimal cloud)  
↓  
Home Assistant OS  
↓  
Home Assistant central logic  
↓  
Logical entities / automations / scenes / notifications  
↓  
Google Home / dashboards / voice / UI / vendor apps where still required  

The central design idea is:

- physical use must still work without apps
- Home Assistant is the main local brain
- MQTT is the preferred messaging approach where practical
- cloud is optional where avoidable and documented where unavoidable
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
- cloud services are optional enhancements, not the foundation
- if internet is down, the local system should still function as far as device class allows
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
2. stable local or native integrations where MQTT is not practical
3. Matter selectively
4. cloud integrations only when needed

Current communication notes:
- SSID names such as `koti`, `koti56`, and `koti-ext` are implementation details, not primary architecture layers
- at this stage, the important distinction is whether a device is reachable on the home network, whether it is local or cloud-dependent, and whether it has unusual network dependencies
- Parmair ventilation currently uses Ethernet to a nearby Wi-Fi extender, and that extender joins the network through `koti-ext`
- LG C2 TV is connected directly to the main router by Ethernet
- some current devices are exposed through Google Home mainly via vendor clouds
- Home Assistant should gradually become the main integration point instead of Google Home being the technical hub

---

## 5. Control model

The home has multiple control layers but must behave as one system.

- Physical layer (switches, wiring)
- Hardware control layer (Shelly, TRÅDFRI, Yale, smart plugs, appliances, robots)
- Logical layer (Home Assistant)
- User layer (Google Home, dashboards, apps, voice)

The long-term goal is one logical user experience even when several technical layers exist underneath.

---

## 6. Device domains

The current architecture should be modeled by domain, not only by protocol.

### 6.1 Lighting and switched circuits
Primary hardware truth:
- Shelly relays behind switches

Secondary device layer:
- IKEA TRÅDFRI bulbs and grouped lighting

Rules:
- physical switch behavior must remain reliable
- mixed Shelly + smart-bulb circuits must be documented explicitly

### 6.2 Sockets and smart power
Current known socket/control families:
- Shelly-controlled fixed sockets
- IKEA sockets
- Deltaco smart sockets

Important examples mentioned by the user:
- water distiller socket
- outdoor RV socket

Rules:
- classify every socket as normal, controlled, critical, or security-sensitive
- avoid exposing critical or high-risk power controls casually

### 6.3 Security and access control
Current known devices:
- Yale Wi-Fi main door lock
- front door entity in Google Home room model
- upcoming IKEA water leak sensors

Rules:
- security and safety devices are a separate architectural domain
- avoid casual unlock controls in normal dashboards
- begin with state visibility, notifications, and controlled manual actions
- automatic unlock actions are not a default design choice

### 6.4 Climate and air quality
Current known devices:
- Parmair ventilation unit via browser control over Ethernet through a Wi-Fi extender path
- Electrolux air purifiers x4
- floor-heating related systems already known from earlier inventory work

Rules:
- prefer local control for ventilation if a stable path exists
- cloud-backed air purifiers must be documented with fallback expectations

### 6.5 Appliances and utility devices
Current known devices:
- Samsung washing machine via SmartThings
- Siemens IQ series oven via Home Connect
- Siemens hob via Home Connect
- Siemens dishwasher via Home Connect

Rules:
- appliance entities should be informational first
- only expose controls that are useful, safe, and reliable

### 6.6 Cleaning and outdoor robotics
Current known devices:
- Ecovacs robot vacuum
- Dreame robot lawn mower

### 6.7 Entertainment and media
Current known devices:
- LG C2 TV via LG ThinQ

Rules:
- media devices are not safety-critical, but they should still be inventoried and placed correctly in the room model
- direct Ethernet-connected devices should be documented as such when it improves troubleshooting and integration reliability

### 6.8 Sauna and wellness
Current known devices:
- Harvia systems from earlier inventory discussions
- sauna room lighting and related entities visible in Google Home

Rules:
- sauna control remains its own safety-conscious domain
- do not mix sauna safety logic with general convenience automations

Rules:
- treat these as a separate service domain
- expose status, start, stop, dock, and maintenance states logically


---

## 7. Integration model by device family

This is the current best-fit architectural placement for device families that were not yet properly reflected in the older documents.

| Device family | Current known path | Architectural place | Initial integration stance |
|---|---|---|---|
| Yale lock | Yale Wi-Fi product on home Wi-Fi | Security and access control | Security-first integration, separated UI |
| Parmair ventilation | Browser control via Ethernet to Wi-Fi extender path | Climate and air quality | Prefer local/browser/API route if feasible |
| Samsung washing machine | SmartThings → Google Home | Appliances | SmartThings-backed initially |
| Siemens oven / hob / dishwasher | Home Connect → Google Home | Appliances | Home Connect-backed initially |
| Electrolux air purifiers | Electrolux cloud → Google Home | Climate and air quality | Vendor-cloud-backed initially |
| Deltaco sockets | Deltaco Smart Home → Google Home | Sockets and smart power | Vendor path first, later evaluate alternatives |
| IKEA sockets and leak sensors | IKEA ecosystem | Sockets / Safety | Native IKEA path preferred |
| Ecovacs robot vacuum | Ecovacs app → Google Home | Cleaning robotics | Vendor integration first |
| Dreame robot mower | Dreame app → Google Home | Outdoor robotics | Vendor integration first |
| LG C2 TV | LG ThinQ with direct Ethernet to router | Entertainment and media | Prefer stable native integration path |

---

## 8. Lighting model

Each circuit must be classified:

- relay_only
- smart_bulb_only
- shelly_plus_smart_bulb
- critical_power
- socket

This classification remains valid and should also be extended with architectural tags where useful, such as:
- security_sensitive
- cloud_dependent
- local_api_available
- needs_constant_power

---

## 9. Critical infrastructure model

Critical devices:
- must be protected
- must not be exposed casually
- must have recovery logic where appropriate

Current critical or sensitive examples:
- FTTH / fiber path power
- network core power
- Yale lock and door access entities
- water leak sensors once deployed
- any socket feeding infrastructure that should not be turned off accidentally

---

## 10. Room model

Google Home room structure remains the source of truth for naming and user-facing grouping.

Rooms visible in the provided screenshots and suitable as the current architecture room set:
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

Observed entity examples that support this room model include:
- Hall: front door lock and hall lights
- Bedroom: air purifier, lights, and several sockets
- Hobby Room: air purifier, lights, outlet, and infrared heater
- Laundry room: washing machine, light, purifier, and multiple sockets
- Kitchen: dishwasher, oven, lights, and table outlet
- Bathroom: lights and multiple outlet entities
- Sauna / Technical room / Warehouse / WC: dedicated room-light entities

This room list should now be treated as the baseline until a more complete export confirms additions or corrections.

---

## 11. Portability and migration model

System must support:
- hardware migration (laptop → mini PC)
- platform migration where practical (HA OS → Linux / Node-RED or another supported structure)

This means:
- keep architecture docs platform-neutral where possible
- document all cloud dependencies and credentials requirements separately
- prefer integrations that can be re-created without vendor lock-in where realistic

---

## 12. Backup and rollback model

System must:
- support automatic backups
- allow rollback
- restore fully on new hardware

Backups must eventually include:
- Home Assistant configuration
- automations and scripts
- dashboards
- integration configuration notes
- device inventory and room mapping
- credentials and secrets handling instructions kept separately and securely

---

## 13. Documentation model

Documentation must include:
- architecture
- devices
- integrations
- MQTT structure
- room model
- cloud dependency map
- recovery steps
- migration steps
- security-critical device handling rules

---

## 14. Operational model

System must be:
- reliable
- maintainable
- understandable
- recoverable
- portable
- security-conscious

Current operational priority:
1. finish the device-family inventory
2. document the exact Home Assistant integration path for each family
3. confirm room placement and naming for non-light devices
4. separate critical and security-sensitive controls from everyday views
5. move toward a unified Home Assistant-centered logical model without breaking existing working vendor setups

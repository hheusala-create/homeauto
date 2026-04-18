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

See also: `core_principles.md`
See also: `layers.md`

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

## 2.1 Central host architecture

The Home Assistant system runs on dedicated local hardware.

The recommended host architecture is:

- a minimal Linux server as the base system
- Home Assistant OS running inside a virtual machine on that host

Preferred base distribution:
- Debian (stable)

Rationale:
- allows Home Assistant OS to remain a clean, supported environment with Supervisor and add-ons
- enables running additional services (scripts, automation tools, backups, monitoring) on the host system
- keeps the system flexible and migration-friendly
- avoids coupling all infrastructure to Home Assistant OS

Host responsibilities:
- virtualization platform for Home Assistant OS
- system-level services (e.g. SSH, backups, scripts, monitoring)
- optional additional services (Docker containers, automation scripts, cron/systemd jobs)

Home Assistant OS responsibilities:
- Home Assistant core
- add-ons (e.g. MQTT broker, integrations)
- home automation logic

Important constraints:
- Home Assistant OS must be treated as an isolated appliance-like environment
- host-level services must not interfere with Home Assistant networking or device access
- architecture must remain portable so that Home Assistant OS can be moved to new hardware if needed

Non-recommended approaches:
- running Home Assistant OS directly on bare metal if additional server functionality is required
- using desktop-oriented distributions for the host system
- using deprecated installation types (Home Assistant Core or Supervised)

This model aligns with:
- portability requirements
- separation of concerns
- long-term maintainability

---
## 2.2 Current production deployment

The current intended Home Assistant runtime is now on dedicated local server hardware.

Current host deployment:
- host OS: Debian minimal
- virtualization: KVM/libvirt
- bridge: `br0`
- host IP: `10.107.1.219`

Current Home Assistant guest:
- VM name: `homeassistant`
- VM MAC: `52:54:00:49:06:80`
- reserved LAN IP: `10.107.1.101`
- HA UI: `http://10.107.1.101:8123`

Operational meaning:
- this Debian KVM/libvirt host is now the primary Home Assistant host
- the earlier laptop-hosted HA instance is no longer the active development/runtime platform
- the laptop-hosted HA was retained only long enough to extract migration materials:
  - backup file
  - Backup Emergency Kit / encryption key
  - existing HA login credentials

Migration rule for the current cutover:
- the laptop-hosted HA should remain powered off during restore/cutover so it does not interfere on the LAN
- after cutover, all continuing HA work should happen on the dedicated Debian host

This deployment is aligned with the long-term architecture target:
- minimal Linux host
- HA OS isolated in a VM
- portable guest image and backup-driven recovery
- separation between host responsibilities and HA responsibilities

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

### IKEA lighting integration

Current implementation:
- IKEA smart bulbs and related IKEA Zigbee devices are managed by the IKEA DIRIGERA hub.
- DIRIGERA is connected to Home Assistant via Matter bridge.
- Google Home may also remain connected in parallel.

Current data path:
- Home Assistant -> Matter -> DIRIGERA -> Zigbee -> IKEA devices

Architectural note:
- IKEA lighting is currently not joined directly to a Home Assistant-owned Zigbee network.
- This is the current accepted first integration step to achieve local control with minimal migration effort while keeping future options open.
- A direct Zigbee migration path remains open for the future if Home Assistant-side control fidelity or flexibility is insufficient.
- Thread capability in DIRIGERA does not change the current IKEA bulb data path; current IKEA lighting still reaches Home Assistant through DIRIGERA as a Matter bridge and Zigbee device network.

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

Rules:
- treat these as a separate service domain
- expose status, start, stop, dock, and maintenance states logically

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

Rooms visible in the current Home Assistant area model:

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
- Laundry Room
- Living Room
- Office
- Sauna
- Technical Room
- Warehouse
- WC

Naming representation rule:
- canonical room keys in repo and YAML use lowercase snake_case
- Home Assistant Areas use Title Case visible names
- alias mappings preserve legacy room-name variants where needed

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

For encrypted Home Assistant backups, the recovery package must also preserve:
- the backup file itself
- the Backup Emergency Kit / encryption key
- the old HA login credentials needed after restore

Current confirmed migration pattern:
- old HA instance acts as the source for the final backup package
- new HA instance is restored from that package on the target hardware
- old HA must not remain actively running on the same LAN during restore/cutover unless explicitly isolated for testing

This model supports:
- hardware migration
- controlled cutover
- rollback readiness
- disaster recovery on replacement hardware

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

# Documentation: Home Assistant Voice Control Setup

## 1. System Architecture & Operation
The current voice control system is built on a modular pipeline called **"Gemini"**, which orchestrates the communication between the user's voice and the smart home hardware.

* **Speech-to-Text (STT):** Uses **Google AI STT** (Finnish) to transcribe voice commands into text.
* **Conversation Agent:** Powered by the **Google AI Conversation** integration.
    * **Model:** Configured to use `gemini-flash-latest`. This alias ensures the system always points to a valid and stable version of the Flash model provided by the API.
    * **Temperature:** Set to **0.7**. This provides a balance between deterministic device control and flexible natural language understanding.
    * **System Instructions (The Prompt):** The agent is explicitly instructed to:
        1. Prioritize tool usage for device control.
        2. **Always** return a short text confirmation (e.g., "Tehty") immediately after a successful device operation.
        3. Respond only in Finnish and avoid any Markdown formatting.
* **Text-to-Speech (TTS):** Uses the **Google Translate TTS** integration (Finnish). This takes the text response from Gemini and converts it back to audio to be played on the local speaker.

---

## 2. Documented Issues and Resolutions

During the implementation, several critical technical hurdles were identified and resolved to stabilize the system.

### I. The "Unable to Get Response" Error
* **Problem:** Commands would trigger the device (e.g., light on), but the voice assistant would report an error instead of speaking.
* **Cause:** The Gemini model would execute the tool call but fail to generate a text-based confirmation. Without a text response, the TTS engine had nothing to process, causing the Assist pipeline to report a failure.
* **Resolution:** Implemented a strict **System Prompt** that forces the model to generate a verbal confirmation ("Tehty") after every action.

### II. Model Availability & 404 Errors
* **Problem:** Attempting to use specific model versions like `gemini-1.5-flash` or `gemini-2.0-flash` resulted in **404 NOT_FOUND** or "Model no longer available" errors.
* **Cause:** Rapid changes in Google's API availability and how the integration handles versioned aliases. Certain models were removed or the endpoints were changed by the provider.
* **Resolution:** Switched to the **`gemini-flash-latest`** alias. This redirect ensures the API calls are routed to a functioning and available model version, bypassing the 404 errors.

### III. Interaction Stability
* **Problem:** Randomness in responses or failure to follow the control logic.
* **Resolution:** Locked the **Temperature to 0.7**. This ensures that the model remains focused on the instructions provided in the System Prompt, making the interaction predictable and reliable for daily home automation use.

---

**Status:** The system is currently stable. Commands are transcribed correctly, Gemini executes the actions, and the user receives a verbal confirmation in Finnish.

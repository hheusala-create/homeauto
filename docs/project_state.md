# Project State

Last reviewed: 2026-04-10

## Purpose

This file is the fast-entry anchor for the home automation project.
It exists so the project can be re-grounded quickly without relying on memory alone.

## Source of truth

The Git repository is the source of truth for:
- architecture
- principles
- mappings
- naming decisions
- current implementation status

If an assistant does not have the current repo contents available, it must ask for the repo or the relevant documentation files instead of inventing structure or duplicating decisions.

## Core implementation direction

- Home Assistant OS is the initial central platform
- MQTT should be used first where practical
- The setup must be migration-friendly from laptop to future dedicated hardware
- Backups and rollback capability must be preserved
- Physical wall switches must always work
- Shelly is the primary control layer
- IKEA TRÅDFRI is a secondary lighting layer
- Critical and security-sensitive devices must be modeled separately
- Cloud dependencies must be explicit and minimized where practical

## Current phase

Infrastructure migration and production cutover phase.

## Current infrastructure status

1. The new primary Home Assistant server now runs on a dedicated Debian minimal host with KVM/libvirt.
2. Current host details:
   - host OS: Debian minimal
   - virtualization: KVM/libvirt
   - bridge: `br0`
   - host IP: `10.107.1.219`
3. Current Home Assistant VM details:
   - VM name: `homeassistant`
   - VM MAC: `52:54:00:49:06:80`
   - reserved LAN IP: `10.107.1.101`
4. Home Assistant UI opens at:
   - `http://10.107.1.101:8123`
5. The old laptop-hosted Home Assistant is no longer an active development target.
6. The old laptop-hosted Home Assistant was used only as the source for migration material:
   - backup file
   - Backup Emergency Kit / encryption key
   - existing HA login credentials
7. Current restore prerequisites are ready:
   - actual backup file from the old HA
   - Backup Emergency Kit / encryption key
   - old HA username and password for post-restore login

## Current implementation priorities

1. Restore the backup to the new Home Assistant VM at `10.107.1.101`
2. Log in using the old Home Assistant credentials after restore
3. Confirm the restored system on the new dedicated host
4. Continue all future HA work only on the new server
5. Keep the old laptop HA powered off during restore/cutover so it does not interfere on the LAN
6. Resume Shelly, IKEA, MQTT, naming, and integration work only after the restore baseline is confirmed

## Shelly relay naming rule in Home Assistant

When a Shelly relay is exposed in `configuration.yaml`, its entity naming must always follow the repository naming standard.

Rule:
- Do not use generic names such as `relay` in the final entity naming.
- Use the standard power suffix pattern:

`switch.<room>_light_<fixture>_power`

Examples:
- `switch.hall_light_ceiling_power`
- `switch.corridor_light_ceiling_power`

Related light entity rule:
- The matching smart light entity should follow:

`light.<room>_light_<fixture>`

Examples:
- `light.hall_light_ceiling`
- `light.corridor_light_ceiling`

Automation alignment rule:
- If a Shelly relay or light entity name is changed in `configuration.yaml`, all matching references in `automations.yaml` must be updated immediately to the same naming-standard-compliant entity name.
- Configuration and automations must never be left using different names for the same circuit.

Operational rule:
- New Shelly entities must be named correctly at creation time to avoid later cleanup work.
- Avoid temporary names like `*_relay` when the standard target name is already known.

These are defined at and need to be respected always:
https://github.com/hheusala-create/homeauto/blob/main/docs/standards/entity_name_mapping.md
https://github.com/hheusala-create/homeauto/blob/main/docs/standards/entity_naming_standard.md

## Practical reminder

Before giving or applying new Home Assistant snippets:
1. Check the repository naming standard first.
2. Use naming-standard-compliant entity names already in the first version.
3. For `configuration.yaml`, format snippets using the repository-specific indentation style.
4. When an entity name changes, update both configuration and automations together.

## Naming enforcement reminder

Home Assistant entity naming must follow `docs/standards/entity_naming_standard.md` exactly.

Operational rule:
- check the repo naming standard before suggesting any new entity names
- use final naming immediately instead of temporary relay-style names
- update `configuration.yaml` and `automations.yaml` together when entity names change
- for MQTT switches, the visible `name` field must also preserve the light/socket distinction, not only `unique_id`

## ChatGPT code snippet formatting rule for repo guidance

Home automation repo guidance must always provide code blocks so they are easy to copy-paste directly from chat.

General rule:
- All code blocks must start visually from the far left in chat.
- Do not wrap snippets inside extra parent keys when the user is adding content into an existing block.
- Give only the lines that should be inserted or replaced, unless a full block replacement is explicitly needed.

Special rule for `home_assistant/configuration.yaml`:
- When adding entries into the existing structure, do not include parent keys such as `mqtt:` or `switch:` in the snippet.
- Snippets must be formatted for this repository so that:
  - `- name` lines start with 4 leading spaces
  - child lines under that entry start with 6 leading spaces
- This rule is specific to `configuration.yaml`.

Other files:
- Code blocks must still start from the far left in chat for easy copy-paste.
- Indentation rules may differ by file.
- `automations.yaml` and other files should be given in the indentation style that matches that file, not forced to follow the `configuration.yaml` indentation rule.

## Current restore path for cutover

Locked current path for this migration:

1. Ensure the old laptop-hosted HA is powered off and not active on the network
2. Open the new HA UI at `http://10.107.1.101:8123`
3. If the new HA is still in onboarding/welcome state, choose `Upload backup`
4. Select the backup file taken from the old HA
5. Enter the Backup Emergency Kit encryption key
6. Restore the full backup
7. Wait for restore completion
8. Log in using the old HA account credentials

Operational note:
- the laptop-hosted HA is not to be further developed
- the laptop existed only to extract the backup and emergency kit
- the new Debian KVM/libvirt host is now the intended HA runtime platform

## Current remote access decision

- Primary remote admin approach: WireGuard
- Stable hostname approach: DuckDNS
- Home Assistant web UI should not be exposed directly to the internet
- Initial implementation may run on Home Assistant OS add-on
- Later migration of VPN to router/firewall/dedicated host remains possible

## Important migration rule

When moving Home Assistant to new hardware:

- the old instance becomes a source-only system after the final migration backup is taken
- active development must continue only on the target system after cutover
- only one HA instance should be active on the same LAN during restore/cutover unless there is a deliberate isolated test setup
- backup file, Backup Emergency Kit, and old login credentials must be preserved before cutover

## Important recent Shelly pilot lesson

A critical lesson was confirmed during the Hobby Room Shelly pilot:

- early interpretation from MQTT logs alone was misleading
- a wrong conclusion was almost generalized toward the wider house rollout
- the real cause was a device-side Shelly setting mismatch

Confirmed lesson:
- before making any larger Shelly rollout, architecture, or automation conclusions, always verify the actual Shelly device settings first
- especially verify:
  - input mode (`Switch` vs `Button`)
  - relay/input relationship (`Detached` vs direct relay control)
  - relay power-on behavior
  - MQTT-related device settings

Confirmed correct pattern for normal 2-position wall switches in `shelly_plus_smart_bulb` circuits:
- input mode: `Switch`
- relay mode: `Detached`
- relay should remain ON so the smart bulb keeps constant power
- Home Assistant should react based on the verified device behavior, not guessed interpretation of MQTT event output

Operational reminder:
- do not generalize from pilot MQTT/event behavior until the exact Shelly settings have been checked on the device
- device-side verification comes before broader rollout decisions

This rule should be treated as locked process guidance for future Shelly rollout work.

## Current Shelly migration status

The MQTT YAML rollout has progressed from the pilot stage to a broader active-lighting baseline.

Confirmed working pattern for Shelly Gen4:
- command topic: `<device_id>/rpc`
- state topic: `<device_id>/status/switch:0`
- availability topic: `<device_id>/online`
- command method: `Switch.Set`
- state derived from `value_json.output`
- availability derived from retained online topic

Confirmed practical rollout rule:
- Do not use manually added MQTT devices in the Home Assistant UI for Shelly rollout
- Use YAML-managed MQTT entities for Shelly rollout so entities remain editable and repo-manageable

## Confirmed Shelly + smart bulb wall-switch operating model

Confirmed from the Hobby room and Walk-in closet pilot comparison:

- the reference implementation model is the Hobby room model
- for this rollout pattern, Home Assistant automation listens directly to the Shelly MQTT input topic
- a separate HA `binary_sensor` entity for the wall switch is optional and not part of the default model
- the default model should stay minimal:
  - one YAML-managed Shelly relay entity in HA
  - one HA automation reacting to the Shelly input MQTT topic
  - one target light entity for the actual smart bulb/light control

Important confirmed lesson:

- the effective wall-switch direction for `shelly_plus_smart_bulb` circuits is defined in the Home Assistant automation logic
- in practice, the automation YAML decides whether `true` means light on or light off
- this means switch-direction normalization is handled in HA automation logic, not primarily in Shelly settings

Observed pilot outcome:

- Hobby room and Walk-in closet had the same Shelly-side settings
- with the same automation structure, the two rooms still initially behaved with opposite physical switch directions
- the most likely reason is physical switch orientation / wiring differences, not a meaningful Shelly settings difference
- after adjusting the HA automation mapping, both rooms now follow the intended house rule

Locked operating rule for normal 2-position light switches:

- up = light on
- down = light off

Rollout implication:

- all normal 2-position wall switches in lighting circuits must be normalized to the above rule through Home Assistant automation logic where needed
- do not assume that identical Shelly settings alone guarantee identical physical switch direction across rooms

### Open design question: switch behavior model (toggle vs state-based)

Current implementation uses state-based control:
- switch position defines light state (up = on, down = off)

However, there is an open design question for the full-house rollout:

- should all wall switches behave as toggle switches instead?

Toggle model:
- every switch action toggles the light
- physical position of the switch does not strictly define light state

State-based model:
- switch position directly defines light state
- up = on, down = off (current target rule)

Current status:
- not yet decided
- both models are technically possible with Shelly + Home Assistant

Important consideration:
- toggle model may feel more natural in mixed smart-bulb scenarios
- state-based model provides consistent physical predictability

Decision required before large-scale rollout (44 devices):
- confirm whether:
  - A) state-based (current approach)
  - B) toggle-based (alternative approach)

Until decision:
- do not lock the behavior as final architecture
- treat current implementation as a working reference, not final standard

## Current YAML implementation rules (locked)

The current working Home Assistant YAML pattern is now locked more explicitly.

### MQTT switch state mapping rule

For YAML-managed `mqtt.switch` entities, use the working `ON/OFF` mapping pattern.

Use:
- `value_template` that maps `value_json.output` to `ON` / `OFF`
- `payload_on: "ON"`
- `payload_off: "OFF"`
- `state_on: "ON"`
- `state_off: "OFF"`

Do not introduce a separate `true/false` state mapping model for `mqtt.switch` entities in this rollout.

Reason:
- the `ON/OFF` pattern is the currently verified working pattern in this setup
- mixing two different MQTT switch state-mapping styles creates avoidable confusion and regression risk

### Where `true/false` is still used

`true/false` remains valid in Home Assistant automations that react to Shelly input state topics.

Example pattern:
- trigger topic: `<device_id>/status/input:0`
- automation conditions/actions interpret:
  - `trigger.payload_json.state == true`
  - `trigger.payload_json.state == false`

So the locked rule is:

- MQTT relay/switch entity state mapping = `ON/OFF`
- Shelly input automation logic = `true/false`

These must not be mixed conceptually.

## Current living room lighting status

Living room lighting has now been clarified into active lights and waiting Shelly circuits.

### Active now

- `light.living_room_light_spotlight`
  - control model: `shelly_plus_smart_bulb`
  - Shelly device ID: `shelly1g4-a085e3bcdf24`
  - Shelly is configured for detached smart-bulb wall-switch use
  - wall switch controls the spotlight through Home Assistant automation
  - target user rule: up = on, down = off

- `light.living_room_wall`
  - control model: `smart_bulb_only`
  - no Shelly behind this light
  - no wall switch
  - this is a TRÅDFRI bulb in a socket
  - remains separately controllable
  - may still belong to the logical living room light grouping later

### Present in MQTT and prepared for later use

- living room window light
  - Shelly device ID: `shelly1g4-a085e3c16eec`
  - current model: `relay_only`
  - no lamp decision finalized yet

- living room ceiling light
  - Shelly device ID: `shelly1g4-ccba97c89790`
  - current model: `relay_only`
  - no lamp decision finalized yet

Operational rule for the two waiting living room circuits:
- MQTT enabled
- no detached mode yet
- no smart-bulb automation yet
- normal relay behavior retained for now

## Current kitchen YAML recovery notes

Two kitchen YAML-managed Shelly relay entities were restored into active Home Assistant configuration:

- kitchen desk light relay
- kitchen breakfast cabin power

Confirmed lesson:
- if a Shelly is online and working but the HA entity appears unavailable, the cause may be:
  - the YAML entity missing from `configuration.yaml`
  - or an old duplicate/offline entity still remaining in Home Assistant

This was confirmed specifically with the breakfast cabin relay, where an old duplicate offline entity existed in Home Assistant and caused confusion.

## Repo tracking decision for active HA YAML

The project now treats active Home Assistant YAML files as repo-worthy technical source material.

Files to keep in the repository:
- `home_assistant/configuration.yaml`
- `home_assistant/automations.yaml`

Reason:
- they now contain real production logic
- they help future sessions re-ground quickly
- backup files alone are not a sufficient substitute for readable version-controlled logic
- this supports the project rule that GitHub is the canonical source of truth

### Naming approach (confirmed after pilot)

- Shelly device names are NOT changed during migration
- MQTT device IDs remain unchanged
- Home Assistant entity IDs are created using final mapping-based names immediately
- Entity renaming is done in Home Assistant UI after YAML creation

Rationale:
- preserves current Google Home behavior
- enables clean HA abstraction layer immediately
- avoids later bulk renaming step

## IKEA / Dirigera Matter status

- IKEA DIRIGERA added successfully to Home Assistant via Matter.
- Existing setup already had DIRIGERA connected to Google Home.
- Home Assistant `already in use` flow led to a Google Home sharing loop and did not provide a place to enter the Matter code in this setup.
- Working workaround in the current setup: add DIRIGERA through the Matter integration using the `No. It's new` path, then enter the pairing code generated from the IKEA Home smart app.
- Result: DIRIGERA is now visible in Home Assistant and IKEA devices are exposed there.
- Initial integration is working, but control quality and architectural fit are still under evaluation.

### Current architectural interpretation

- IKEA lighting currently remains under DIRIGERA for Zigbee network management.
- Home Assistant consumes IKEA through Matter bridge.
- This is accepted as the current practical path because it is local, quick to deploy, and low-risk.
- Direct Zigbee from Home Assistant remains a future option if Matter bridge limitations appear in brightness, color temperature, transitions, grouping, or reliability.

### Next validation tasks

- Test brightness control reliability in HA
- Test color temperature / color control reliability in HA
- Test room/group synchronization
- Test interaction with Shelly-based always-powered lighting model
- Decide later whether IKEA stays on DIRIGERA Matter bridge or moves to direct Zigbee in HA

## Current Home Assistant area baseline

Home Assistant Areas have now been created manually in the UI as the current room baseline.

Current HA Areas:
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

Locked naming rule for room representation:
- canonical room key in repo / YAML = lowercase snake_case
- visible Home Assistant Area name = Title Case
- room aliases in tooling preserve older display variants and legacy names

Important mapping rule:
- creating or normalizing Home Assistant Areas does not rename Shelly devices
- does not rename IKEA / Google Home names
- does not replace existing mapping tables
- old names remain preserved through mapping documents and aliases until any later controlled cleanup

## Current fixed-Shelly light exposure pattern

A new practical pattern is now in use for fixed/non-smart Shelly-controlled lights.

Pattern:
- keep the YAML-managed MQTT relay as the technical source entity
- expose a user-facing `light.*` entity through Home Assistant `switch_as_x`
- use the `light.*` wrapper in normal UI / voice-facing use
- keep the underlying `switch.*` entity as the technical relay layer

Reason:
- these circuits are real lights from the user perspective
- this keeps UI and voice use more natural
- while still preserving the technical relay model underneath

Current examples include:
- bathroom ceiling light
- bathroom mirror light
- sauna bench light
- sauna wall light
- warehouse light ceiling
- back yard lights living room
- attic light ceiling

Important rule:
- this does not replace the technical relay model in documentation
- the relay remains the electrical truth layer
- the `light.*` wrapper is a user-facing abstraction

## Current backyard split decision

Back yard lighting is now explicitly split into two separately documented circuits:

1. Back yard lights living room
2. Back yard lights laundry room

Current decisions:

Back yard lights living room:
- control model: `relay_only`
- reason: mixed circuit
- this branch currently includes a normal non-TRÅDFRI lamp in the yard
- because of that, detached smart-bulb handling is not currently suitable
- this branch must currently cut power normally

Back yard lights laundry room:
- control model: `shelly_plus_smart_bulb`
- current Home Assistant automation target is the currently used backyard light entity
- current implementation should be documented exactly as implemented in HA

## Current attic exception

Attic is currently treated as a practical exception.

Reality:
- attic has Shelly + TRÅDFRI behind it

Current decision:
- the user-facing implementation is intentionally simplified
- attic is currently exposed and used effectively as a Shelly-only light
- smart-bulb complexity is intentionally hidden because the space is visited rarely
- this is considered acceptable for the current phase

## Current cleanup reminders from active HA state

The active HA state shows a few cleanup items that should be tracked:

- remove duplicate `Back yard lights laundry room` MQTT block from configuration
- review typo / legacy entity remnants such as `light.back_your_lights`
- review still-generic Matter light names such as `light.light_15` to `light.light_18`
- normalize any remaining user-facing names that still look duplicated or awkward

## Locked process rule for future sessions

When repo contents matter, work from the repo or the relevant files.
Do not recreate architecture, naming, mappings, or standards from memory if the current repo is not available.

## Documents to read first

Start with these when re-entering the project:
1. `docs/project_state.md`
2. `docs/architecture/core_principles.md`
3. `docs/architecture/layers.md`
4. `docs/architecture/system_architecture.md`
5. `docs/architecture/remote_access.md`
6. relevant files under `docs/mapping/` and `docs/standards/`

## Notes

- Secrets such as tokens, private keys, WireGuard client configs, and exported QR/config material must not be committed to git.
- DuckDNS hostname may be documented.
- DuckDNS token must be stored outside the repo.
- Home Assistant backups should be taken before further Shelly migration steps.
- The GitHub repository is the canonical source of truth for this project.
- Windows, WSL, Termux, and other local repositories are working copies only.
- Google Drive and exported files are mirror or access copies only.
- Changes are not authoritative until they are committed and pushed to GitHub.
- If any copy conflicts with GitHub, GitHub wins.

## Recent Shelly socket rollout and inventory confirmation

Recent work has extended the Shelly rollout beyond the earlier lighting-focused baseline.

### What was done

- Shelly Gen4 MQTT rollout was expanded toward non-critical socket/power circuits in addition to light-power circuits.
- The active Home Assistant YAML baseline already contains a broad MQTT-managed Shelly switch set in `home_assistant/configuration.yaml`.
- Active MQTT wall-switch automations remain in `home_assistant/automations.yaml` for Shelly + smart-bulb and selected grouped-light circuits.

### Current operational rollout rule

- Bulk MQTT enablement must exclude critical infrastructure devices.
- Bulk MQTT enablement must also exclude any Shelly currently powering the active Home Assistant server or other critical runtime dependency.
- Practical reboot rule confirmed during rollout:
  - after applying MQTT settings to Shelly Gen4 devices, a reboot is required for MQTT operation to come up reliably
- Firmware update must not be bundled into the same bulk rollout script.
- A tested update attempt stalled during device update, so the safe bulk pattern is:
  1. apply MQTT settings
  2. reboot device
  3. verify operation after reboot

### Inventory confirmation from latest full Shelly scan

A new full-house Shelly scan was used to confirm:
- current reachable Shelly Gen4 devices
- model family per device (`S1G4` vs `S1PMG4`)
- MQTT device IDs / device prefixes
- several current IP addresses that had drifted from older documentation

Confirmed practical rule:
- `device_id` is the stable key identifier for Shelly inventory work
- IP address may change and must therefore be treated as mutable inventory data
- inventory matching should prefer `device_id` first and IP second

### Important recent corrections

Recent scan and rollout work confirmed or highlighted at least these points:

- WC Shelly confirmed as:
  - model family: `S1G4`
  - device ID: `shelly1g4-a085e3bd81e4`
  - current IP observed in latest scan: `10.107.1.185`
- Critical network-power Shelly remains:
  - device ID: `shelly1pmg4-a085e3bdd5f4`
  - IP: `10.107.1.221`
  - must remain excluded from bulk actions
- One previously unresolved Shelly entry needs inventory correction from the older unresolved IP-based placeholder:
  - older unresolved placeholder: `10.107.1.223`
  - newer scan indicates current unresolved device at: `10.107.1.224`
  - device ID: `shelly1g4-a085e3bcd2a8`
  
### Copy-paste rule for markdown table row updates

When giving repository updates for markdown tables, provide each table row in its own separate copy-paste block only when existing rows need to be replaced in different places of a long table.

Rule scope:
- this rule applies only to markdown table rows
- use separate copy-paste blocks when replacing existing markdown table rows that belong in different places
- if multiple new markdown table rows are added into the same place, they may be given together in one block
- do not apply this rule to CSV content
- CSV content should be given as one complete copy-paste block when the user needs the whole file or a full CSV section

### Documentation implication

The repo should now be updated so that:
- `docs/devices/shelly.md` reflects latest confirmed device IDs and current IP corrections
- the new `docs/devices/device_registry.csv` becomes the centralized all-device master inventory
- `shelly.md` remains the detailed Shelly-specific reference
- device-level matching and future rollout work use `device_id` as the primary identity key

### Shelly inventory identity rule

For Shelly devices, the primary identity key is the Shelly `device_id` / MQTT prefix.

Rule:
- use `device_id` as the main identity key in inventory, mapping, and rollout work
- treat IP address as mutable supporting data only
- IP may still be stored in inventory as the latest known address
- do not rely on IP as the primary identifier when matching Shelly devices across scans, YAML, or documentation

Reason:
- IP addresses can change over time
- `device_id` remains stable and is also the key used in MQTT topics and rollout logic
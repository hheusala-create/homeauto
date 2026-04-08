# Project State

Last reviewed: 2026-04-09

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

First Shelly MQTT YAML pilot is working.

Pilot device:
- `Harrastushuone valo`
- Shelly 1 Gen4
- Connected to Mosquitto through Home Assistant at `10.107.1.101`

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
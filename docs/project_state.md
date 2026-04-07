# Project State

Last reviewed: 2026-04-07

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

Foundation complete enough to begin controlled device migration.

Current infrastructure status:
1. WireGuard remote access is working
2. Mosquitto broker is installed and running in Home Assistant
3. MQTT integration is connected
4. Home Assistant server IP for current setup is `10.107.1.101`
5. Current Shelly / Google Home / IKEA names remain in use as migration anchors for now
6. Target HA naming layer is applied immediately for new MQTT entities in Home Assistant (entity IDs follow mapping and naming standards)

Current implementation priorities:
1. Stabilize and document the confirmed Shelly MQTT pattern
2. Migrate additional Shelly pilot devices using the same YAML-managed pattern
3. Keep current live naming as anchors until enough devices are migrated safely
4. Apply target HA naming layer immediately for new MQTT entities while keeping current live names as migration anchors in other systems
5. Continue device integrations and logic migration
6. Refine UI / dashboard / voice later
7. Target host architecture defined:
   - future dedicated hardware will run a minimal Linux host (Debian preferred)
   - Home Assistant OS will run as a virtual machine on that host
   - current laptop setup remains valid for development and migration staging

## Current remote access decision

- Primary remote admin approach: WireGuard
- Stable hostname approach: DuckDNS
- Home Assistant web UI should not be exposed directly to the internet
- Initial implementation may run on Home Assistant OS add-on
- Later migration of VPN to router/firewall/dedicated host remains possible

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

Secrets such as tokens, private keys, WireGuard client configs, and exported QR/config material must not be committed to git.
DuckDNS hostname may be documented.
DuckDNS token must be stored outside the repo.
Home Assistant backups should be taken before further Shelly migration steps.

## Source of truth

The GitHub repository is the canonical source of truth for this project.

- Windows, WSL, Termux, and other local repositories are working copies only.
- Google Drive and exported files are mirror or access copies only.
- Changes are not authoritative until they are committed and pushed to GitHub.
- If any copy conflicts with GitHub, GitHub wins.

TEST_SYNC_W11_2026-04-06

## IKEA / Dirigera Matter status

- IKEA DIRIGERA added successfully to Home Assistant via Matter.
- Existing setup already had DIRIGERA connected to Google Home.
- Home Assistant "already in use" flow led to a Google Home sharing loop and did not provide a place to enter the Matter code.
- Home Assistant "already in use" flow led to a Google Home sharing loop and did not provide a place to enter the Matter code in this setup.
- Working workaround in the current setup: add DIRIGERA through the Matter integration using the "No. It's new" path, then enter the pairing code generated from the IKEA Home smart app.
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

# Home Automation

Central repository for my home automation setup.

## Goals
- Build first on a laptop
- Later migrate to dedicated low-power hardware
- Keep the setup rebuildable and migration-friendly
- Prefer local/native integrations and MQTT where practical
- Keep documentation and inventories versioned

## Planned core
- Home Assistant OS initially
- Shelly as the primary control layer
- IKEA TRÅDFRI as a secondary lighting layer
- MQTT where practical from the start

## Structure
- docs/architecture/ = design rules and architecture
- docs/devices/ = human-maintained device notes
- docs/mapping/ = control mappings
- scripts/ = helper scripts
- data/raw/ = raw discovery exports
- data/processed/ = merged inventories generated from raw scans

## Status
Architecture and inventory phase.

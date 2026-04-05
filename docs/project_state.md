# Project State

Last reviewed: 2026-04-05

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

Architecture and inventory phase, with foundation setup in progress.

Current infrastructure priorities:
1. Secure remote admin access
2. MQTT foundation
3. Naming cleanup and entity normalization
4. Device integrations and logic migration
5. UI / dashboard / voice refinement

## Current remote access decision

- Primary remote admin approach: WireGuard
- Stable hostname approach: DuckDNS
- Home Assistant web UI should not be exposed directly to the internet
- Initial implementation may run on Home Assistant OS add-on
- Later migration of VPN to router/firewall/dedicated host remains possible

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
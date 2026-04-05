# Remote Access

Last reviewed: 2026-04-05

## Purpose

This document defines the remote access architecture for the home automation system.

The main goals are:
- secure remote administrative access
- no unnecessary direct internet exposure
- compatibility with Home Assistant OS in the initial phase
- easy migration later to other hardware or a dedicated network edge device

## Current decision

Chosen main user clients:
- Home Assistant Android app
- Home Assistant web UI

Client access model:
- at home, the Home Assistant app and web UI connect directly to Home Assistant over the local network
- away from home / abroad, the Home Assistant app and web UI connect to Home Assistant through the WireGuard VPN tunnel

Reason:
The Home Assistant app and web UI are required parts of the practical remote access design because users need working daily-use access to lights and other controls both locally and remotely.

Chosen remote admin path:
- WireGuard

Chosen stable external hostname approach:
- DuckDNS

Explicit non-goal:
- do not expose the Home Assistant web UI directly to the public internet as the primary access method

## Why this approach

WireGuard fits the project principles well:
- local-first
- secure
- simple client model
- portable to future hardware
- not dependent on keeping Home Assistant directly exposed

DuckDNS provides a stable hostname even if the home public IP changes.

## Phase 1 implementation

Client behavior in Phase 1:
- Home Assistant Android app used on household phones
- Home Assistant web UI used on admin and user devices as needed
- direct local access when connected to the home network
- WireGuard used when remote access is needed outside the home network

Practical requirement:
Remote access is not considered complete unless the main user clients work both:
- locally at home without VPN friction
- remotely through WireGuard when away from home

Initial implementation target:
- Home Assistant OS
- WireGuard add-on running on Home Assistant
- remote peers such as phone and laptop
- router UDP port forwarding to the WireGuard service

Expected components:
- Home Assistant OS host
- WireGuard add-on
- DuckDNS hostname
- router port forward for WireGuard UDP traffic
- WireGuard clients on admin devices

## Phase 2 target

Possible later migration targets:
- router-level WireGuard
- firewall-level WireGuard
- dedicated mini PC or other always-on network host

Reason:
Running VPN at the network edge may be preferable long term because remote access can remain available even if Home Assistant itself is down.

## Security rules

- Do not expose Home Assistant directly unless there is a separate deliberate architecture decision to do so
- Use WireGuard as the primary remote administrative path
- Keep security-sensitive devices separated in the architecture and dashboards
- Treat remote access as infrastructure, not as part of naming cleanup or device logic work
- Keep private keys, exported client configs, and QR materials out of git

## Secrets handling

May be documented:
- DuckDNS hostname
- selected architecture decisions
- high-level setup notes

Must not be committed:
- DuckDNS token
- WireGuard private keys
- WireGuard exported client configuration files
- QR codes or screenshots that reveal private config
- any copied secret values from Home Assistant secrets/config stores

## Current hostname

Current DuckDNS hostname:
- `hhh-home.duckdns.org`

Note:
Store the DuckDNS token outside the repo.

## Operational sequence

Recommended order for project implementation:
1. remote access via WireGuard
2. MQTT foundation
3. naming and entity cleanup
4. device integration refinement
5. automation and dashboard polish

## Open items

- confirm final WireGuard peer naming convention
- confirm final router port-forward details
- decide later whether VPN should stay on Home Assistant or move to the network edge
- verify Home Assistant app and web UI local and WireGuard remote behavior during rollout
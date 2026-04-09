# Entity Naming Standard

Status: agreed baseline  
Scope: Home Assistant technical entity naming for this project  
Purpose: define stable technical naming rules before any friendly/spoken naming is designed

---

## Practical reminder

Before giving or applying new Home Assistant snippets:
1. Check the repository naming standard first.
2. Use naming-standard-compliant entity names already in the first version.
3. For `configuration.yaml`, format snippets using the repository-specific indentation style.
4. When an entity name changes, update both configuration and automations together.

---

## Core principle

Technical names are for:
- Home Assistant entity IDs
- project documentation
- mapping between systems
- automation logic
- avoiding ambiguity across Shelly, IKEA, Google Home, and Home Assistant

These technical names do **not** need to be the same as:
- spoken names
- Google Home names
- Shelly display names
- IKEA app names
- friendly UI labels

Those can be designed later.

---

## Final terminology rules

Use exactly these naming words:

- `light` = one actual light, bulb, lamp, LED light entity, or one lighting circuit
- `lights` = a light group / room-level grouped lighting entity
- `socket` = any socket / outlet entity, always singular in the naming word

This means:

- single bulb or lamp → `light`
- grouped room lighting entity → `lights`
- outlet power entity → `socket`

---

## Functional rule

Naming must follow the **purpose of the circuit**, not just the hardware type.

Examples:
- a Shelly controlling a lighting circuit is named with `light`
- a Shelly controlling a wall outlet is named with `socket`

Even though both are technically power relays.

This prevents lighting controls and socket controls from being mixed conceptually.

---

## Naming grammar

### 1. Light group
Room-level or area-level grouped lighting entity:

`light.<room>_lights`

Examples:
- `light.kitchen_lights`
- `light.hall_lights`
- `light.bedroom_lights`
- `light.living_room_lights`

### 2. Individual light
One actual light / bulb / lamp / smart light entity:

`light.<room>_light_<fixture>`

Examples:
- `light.hall_light_ceiling`
- `light.office_light_ceiling`
- `light.kitchen_light_led`

If there are multiple lights of the same fixture type:

`light.<room>_light_<fixture>_<n>`

Examples:
- `light.kitchen_light_ceiling_1`
- `light.kitchen_light_ceiling_2`
- `light.kitchen_light_ceiling_3`
- `light.kitchen_light_ceiling_4`

### 3. Shelly relay for a lighting circuit
A relay that cuts or restores power to a lighting circuit:

`switch.<room>_light_<fixture>_power`

Examples:
- `switch.kitchen_light_ceiling_power`
- `switch.kitchen_light_desk_power`
- `switch.hall_light_ceiling_power`
- `switch.bathroom_light_mirror_power`

Important:
- domain is `switch`
- naming category remains `light` because the relay serves lighting

### 4. Shelly relay for a socket circuit
A relay that controls a wall outlet / outlet circuit:

`switch.<room>_socket_<fixture>_power`

Examples:
- `switch.kitchen_socket_counter_power`
- `switch.office_socket_right_power`
- `switch.corridor_socket_vacuum_power`

---

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

---

## Domain rules

Home Assistant still requires the normal domains:
- `light.`
- `switch.`

So room-first naming starts **after** the domain prefix.

Correct:
- `light.kitchen_lights`
- `switch.kitchen_light_ceiling_power`

Not used:
- `kitchen_light_ceiling_power`
- `Kitchen_Light_Ceiling_Power`

---

## Room naming rules

Use lowercase snake_case room names.

Examples:
- `hall`
- `kitchen`
- `bathroom`
- `living_room`
- `technical_room`
- `front_yard`
- `back_yard`
- `hobby_room`

---

## Fixture naming rules

Use short physical or logical fixture names.

Examples:
- `ceiling`
- `mirror`
- `desk`
- `wall`
- `bench`
- `window`
- `spotlight`
- `counter`
- `door`
- `vacuum`
- `outdoor`

Avoid:
- current vendor-specific names
- mixed-language names in target HA names
- ambiguous temporary names when a clearer physical term is known

---

## Numbering rules

When multiple similar lights exist under one fixture, use numeric suffixes.

Example:
- `light.kitchen_light_ceiling_1`
- `light.kitchen_light_ceiling_2`
- `light.kitchen_light_ceiling_3`
- `light.kitchen_light_ceiling_4`

Use numbering only where needed.

---

## Group vs single-light rule

Use:
- `lights` only for the grouped room/area lighting entity
- `light` for every single light entity and every light-related power relay

Examples:
- room group → `light.office_lights`
- actual smart light → `light.office_light_ceiling`
- Shelly relay for that light circuit → `switch.office_light_ceiling_power`

This distinction is intentional and must stay consistent.

---

## Why this standard is used

This standard is designed to make the following immediately clear:

1. Which entities belong to the same room
2. Which entities are light-related
3. Which entities are socket-related
4. Which entities are actual lights
5. Which entities are relays cutting power
6. Which entities are grouped room lighting entities

This is especially important because the house has:
- Shelly relays behind light circuits
- Shelly relays behind socket circuits
- smart bulbs behind some light relays
- dumb embedded lights behind other light relays
- grouped light entities in Google Home / IKEA / HA

---

## Examples by type

### Example: room light group
- `light.kitchen_lights`

### Example: single smart light
- `light.kitchen_light_led`

### Example: multiple smart lights on one fixture
- `light.kitchen_light_ceiling_1`
- `light.kitchen_light_ceiling_2`
- `light.kitchen_light_ceiling_3`
- `light.kitchen_light_ceiling_4`

### Example: relay feeding a light circuit
- `switch.kitchen_light_ceiling_power`

### Example: relay feeding a socket circuit
- `switch.kitchen_socket_counter_power`

---

## Example interpretation

### Hall
- grouped room lighting: `light.hall_lights`
- actual light: `light.hall_light_ceiling`
- Shelly power relay for that lighting circuit: `switch.hall_light_ceiling_power`

### Bathroom
- grouped room lighting: `light.bathroom_lights`
- Shelly-only ceiling lighting circuit: `switch.bathroom_light_ceiling_power`
- Shelly-only mirror lighting circuit: `switch.bathroom_light_mirror_power`

### Kitchen
- grouped room lighting: `light.kitchen_lights`
- ceiling relay: `switch.kitchen_light_ceiling_power`
- ceiling smart lights:  
  - `light.kitchen_light_ceiling_1`  
  - `light.kitchen_light_ceiling_2`  
  - `light.kitchen_light_ceiling_3`  
  - `light.kitchen_light_ceiling_4`
- desk relay: `switch.kitchen_light_desk_power`
- LED smart light: `light.kitchen_light_led`
- socket relay example: `switch.kitchen_socket_counter_power`

---

## Out of scope for this document

This document does **not** yet define:
- spoken names
- Google Home naming
- Shelly display names
- IKEA naming
- dashboard-friendly labels
- alias handling for voice assistants

Those will be defined later after the technical naming structure is locked.

---

## Repo usage recommendation

Use this document as the source of truth when updating:
- light mapping documentation
- Shelly inventory documentation
- IKEA / Tradfri inventory documentation
- future Home Assistant entity planning

Suggested follow-up docs:
- spoken/friendly naming standard
- mapping table from current names to target HA technical names

## Visible MQTT switch name rule

For MQTT switches in `configuration.yaml`, the visible `name` field must follow the same functional naming logic as the technical entity name.

Use:
- `<Room> light <fixture> power` for lighting circuits
- `<Room> socket <fixture> power` for socket circuits

Examples:
- `Hall light ceiling power`
- `Kitchen light ceiling power`
- `Closet light ceiling power`
- `Kitchen socket counter power`

Do not use:
- generic names like `relay`
- mixed temporary legacy wording when the final target naming is already known
- old room wording that is no longer part of the target architecture

Reason:
- this keeps light circuits visually distinct from socket circuits in Home Assistant UI
- and keeps the visible name aligned with the technical naming standard
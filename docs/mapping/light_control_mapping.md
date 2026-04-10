# Light Control Mapping

Purpose:
Map physical Shelly circuits to smart-light entities and define the future Home Assistant control model.

Control models:
- `relay_only`
- `shelly_plus_smart_bulb`
- `critical_power`
- `socket`
- `smart_bulb_only`

---

## Mapping table

| Area | Current user-facing light | Shelly device | Shelly IP / device ID | Tradfri / Google Home light | Control model | Planned HA entity | Notes |
|---|---|---|---|---|---|---|---|
| Technical room | Technical room ceiling light | Technical room light ceiling | shelly1g4-a085e3bd87d0 | Technical room light ceiling | shelly_plus_smart_bulb | light.technical_room_light_ceiling | Current HA automation active |
| Hall | Hall ceiling light | Hall ceiling light | shelly1pmg4-a085e3bd0210 | Hall ceiling light | shelly_plus_smart_bulb | light.hall_light_ceiling | Current HA automation active |
| Laundry room | Laundry room ceiling light | Laundry room light ceiling | shelly1g4-a085e3bd8af0 | Laundry room light ceiling | shelly_plus_smart_bulb | light.laundry_room_light_ceiling | Current HA automation active |
| Bathroom | Bathroom ceiling light | Bathroom ceiling light | shelly1g4-ccba97c8cbf8 | Bathroom ceiling light | relay_only | light.bathroom_ceiling_light | Fixed Shelly light exposed in HA through light wrapper |
| Bathroom | Bathroom mirror light | Bathroom mirror light | shelly1g4-a085e3bcd118 | Bathroom mirror light | relay_only | light.bathroom_mirror_light | Fixed Shelly light exposed in HA through light wrapper |
| Living room | Living room ceiling light | Living room ceiling light | shelly1g4-ccba97c89790 | Living Room Ceiling Light | relay_only | light.living_room_ceiling | Shelly present in MQTT; no lamp installed yet; keep as normal relay-only circuit for now |
| Living room | Living room spotlight | Living room spotlight | shelly1g4-a085e3bcdf24 | Living Room Ceiling Spotlight | shelly_plus_smart_bulb | light.living_room_light_spotlight | Active Shelly + smart bulb circuit; detached mode; wall switch controls light through HA automation |
| Living room | Living room window light | Living room window light | shelly1g4-a085e3c16eec | Living Room Window Light | relay_only | light.living_room_window | Shelly present in MQTT; no lamp installed yet; keep as normal relay-only circuit for now |
| Living room | Living room wall light | - | - | Living room wall light | smart_bulb_only | light.living_room_wall | Active TRÅDFRI bulb in socket; no Shelly and no wall switch |
| Hobby room | Hobby room light | Hobby room light | shelly1g4-ccba97c89350 | Hobby room light | shelly_plus_smart_bulb | light.hobby_room_light_ceiling | Current HA automation active |
| Kitchen | Kitchen ceiling lights | Kitchen ceiling lights | shelly1g4-a085e3bd891c | Kitchen Ceiling Light | shelly_plus_smart_bulb | light.kitchen_lights | 4 individual TRÅDFRI ceiling bulbs controlled together through HA group |
| Kitchen | Kitchen desk lights | Kitchen desk lights | shelly1pmg4-a085e3bcfb14 | Kitchen led | relay_only | light.kitchen_led | Dedicated socket-fed kitchen LED lighting circuit; Shelly 1PM Gen4; no wall-switch input automation |
| Kitchen | Breakfast cabin light | Kitchen breakfast cabinet light | shelly1g4-ccba97c89b84 | Breakfast cabinet | relay_only | light.breakfast_cabin | Dedicated socket-fed breakfast cabinet light circuit; no wall-switch input automation |
| Sauna | Sauna wall light | Sauna wall light | shelly1g4-ccba97c89804 | Sauna wall light | relay_only | light.sauna_wall_light | Fixed Shelly light exposed in HA through light wrapper |
| Sauna | Sauna bench light | Sauna bench light | shelly1g4-ccba97c8a044 | Sauna bench light | relay_only | light.sauna_bench_light | Fixed Shelly light exposed in HA through light wrapper |
| Bedroom | Bedroom ceiling lights | Bedroom ceiling lights | shelly1g4-ccba97c888c8 | Bedroom Lights | shelly_plus_smart_bulb | light.bedroom_lights | Current HA automation active |
| Closet | Walk-in closet light | Walk-in closet light | shelly1g4-ccba97c8a17c | Walkin closet | shelly_plus_smart_bulb | light.closet_light_ceiling | One Shelly + one IKEA bulb in closet |
| WC | WC ceiling light | WC ceiling light | shelly1g4-a085e3bd81e4 | WC light ceiling | shelly_plus_smart_bulb | light.wc_light_ceiling | Current HA automation active |
| Front yard | Front yard lights | Front yard lights | shelly1pmg4-a085e3bbd280 | Front yard lights | shelly_plus_smart_bulb | light.front_yard_lights | Current HA automation active |
| Back yard | Back yard lights living room | Back yard lights living room | shelly1g4-ccba97c8856c | Back yard lights living room | relay_only | light.back_yard_lights_living_room | Mixed circuit with one normal yard lamp; no detached mode for now |
| Back yard | Back yard lights laundry room | Back yard lights laundry room | shelly1g4-a085e3c16c94 | Back yard lights laundry room | shelly_plus_smart_bulb | light.backyard_light_3 | Current HA automation target is the renamed backyard TRÅDFRI light |
| Attic | Attic light ceiling | Attic light ceiling | shelly1g4-a085e3c197b0 | Attic | relay_only | light.attic_light_ceiling | Practical exception: Shelly + TRÅDFRI exists underneath, but current user-facing implementation is Shelly-only style |
| Warehouse | Warehouse light ceiling | Warehouse light ceiling | shelly1pmg4-a085e3bbb77c | Warehouse light ceiling | relay_only | light.warehouse_light_ceiling | Fixed Shelly light exposed in HA through light wrapper |
| FTTH | FTTH | Network core power | 10.107.1.221 | - | critical_power | switch.network_core_power | Must never be in bulk off automations |

---

## Notes

### Current Home Assistant truth beats older generic mapping

This file has now been aligned more closely with the currently active Home Assistant YAML and registry state.

That means:
- the actual YAML relay names are treated as authoritative
- the actual current automation target entities are treated as authoritative
- older shorter placeholders such as `light.hall` or `light.technical_room` are no longer preferred when the active HA implementation uses more specific entity names

### Backyard split

Back yard is no longer modeled as one vague light branch.

Current split:
- `Back yard lights living room`
- `Back yard lights laundry room`

These must stay separate in further documentation and implementation.

### Attic exception

Attic remains a deliberate exception.

Architecture reality:
- Shelly + TRÅDFRI exists underneath

Current practical implementation:
- exposed and used effectively as a Shelly-only light
- hidden smart-bulb complexity is acceptable because the space is used rarely

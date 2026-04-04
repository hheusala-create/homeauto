# Entity Name Mapping

Status: working mapping baseline  
Purpose: connect current real-world names across Shelly / IKEA / Google Home to the target Home Assistant technical naming, friendly naming, and spoken naming.

Related standard:
- `docs/standards/entity_naming_standard.md`

---

## Status notes

Meaning of status values:
- `confirmed` = explicitly confirmed by user
- `likely` = strongly supported by existing docs / screenshots, but not yet explicitly confirmed
- `needs_confirmation` = still needs user confirmation before final rename work

---

## Lighting entities

| Room / Area | Entity type | Current Shelly name | Current IKEA / Tradfri name | Current Google Home / group name | Target HA technical name | Target HA friendly name | Proposed spoken name | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Hall | light_group | - | - | Hall Lights | `light.hall_lights` | Hall lights | Hall lights | confirmed | Logical room lighting group |
| Hall | light_power_relay | Hall Light | - | Hall Light | `switch.hall_light_ceiling_power` | Hall ceiling power | Hall light | confirmed | Shelly relay for hall ceiling light |
| Hall | light | - | Hall Light Ceiling | Hall Light Ceiling | `light.hall_light_ceiling` | Hall ceiling light | Hall ceiling light | confirmed | IKEA / Tradfri light behind Shelly |

| Bathroom | light_group | - | - | Bathroom lights | `light.bathroom_lights` | Bathroom lights | Bathroom lights | confirmed | Logical room lighting group |
| Bathroom | light_power_relay | Bathroom ceiling lights | - | Bathroom Ceiling Lights | `switch.bathroom_light_ceiling_power` | Bathroom ceiling power | Bathroom ceiling light | confirmed | Shelly-only embedded non-smart light |
| Bathroom | light_power_relay | Bathroom mirror light | - | Bathroom Mirror Light | `switch.bathroom_light_mirror_power` | Bathroom mirror power | Bathroom mirror light | confirmed | Shelly-only embedded non-smart light |

| Kitchen | light_group | - | - | Kitchen Lights | `light.kitchen_lights` | Kitchen lights | Kitchen lights | confirmed | Logical room lighting group |
| Kitchen | light_power_relay | Kitchen Ceiling Light / Kitchen ceiling lights | - | Kitchen Ceiling Light | `switch.kitchen_light_ceiling_power` | Kitchen ceiling power | Kitchen ceiling lights | confirmed | Shelly cuts power to Kitchen Light 1-4 |
| Kitchen | light | - | Kitchen Light 1 | Kitchen Light 1 | `light.kitchen_light_ceiling_1` | Kitchen ceiling light 1 | Kitchen ceiling light 1 | confirmed | Smart light member under ceiling circuit |
| Kitchen | light | - | Kitchen Light 2 | Kitchen Light 2 | `light.kitchen_light_ceiling_2` | Kitchen ceiling light 2 | Kitchen ceiling light 2 | confirmed | Smart light member under ceiling circuit |
| Kitchen | light | - | Kitchen Light 3 | Kitchen Light 3 | `light.kitchen_light_ceiling_3` | Kitchen ceiling light 3 | Kitchen ceiling light 3 | confirmed | Smart light member under ceiling circuit |
| Kitchen | light | - | Kitchen Light 4 | Kitchen Light 4 | `light.kitchen_light_ceiling_4` | Kitchen ceiling light 4 | Kitchen ceiling light 4 | confirmed | Smart light member under ceiling circuit |
| Kitchen | light_power_relay | Kitchen desk lights | - | Kitchen desk lights | `switch.kitchen_light_desk_power` | Kitchen desk power | Kitchen table lights | confirmed | Shelly cuts power to Kitchen led |
| Kitchen | light | - | Kitchen led | Kitchen led | `light.kitchen_light_led` | Kitchen LED lights | Kitchen table lights | confirmed | IKEA Tradfri LED lights behind desk circuit |
| Kitchen | socket_power_relay | Kitchen counter socket | - | Kitchen counter socket | `switch.kitchen_socket_counter_power` | Kitchen counter socket | Kitchen counter socket | likely | From Shelly inventory |
| Kitchen | socket_power_relay | Kitchen breakfast cabinet socket | - | Breakfast cabinet | `switch.kitchen_socket_breakfast_cabinet_power` | Kitchen breakfast cabinet socket | Kitchen breakfast cabinet socket | likely | From Shelly inventory |

| Living room | light_group | - | - | Living Room Lights | `light.living_room_lights` | Living room lights | Living room lights | confirmed | Logical room lighting group |
| Living room | light_power_relay | Living room ceiling light | - | Living Room Ceiling Light | `switch.living_room_light_ceiling_power` | Living room ceiling power | Living room ceiling light | likely | Docs support Shelly + smart light mapping |
| Living room | light | - | Living Room Ceiling Light | Living Room Ceiling Light | `light.living_room_light_ceiling` | Living room ceiling light | Living room ceiling light | likely | Smart light behind Shelly |
| Living room | light_power_relay | Living room ceiling spotlight | - | Living Room Ceiling Spotlight | `switch.living_room_light_spotlight_power` | Living room spotlight power | Living room spotlight | likely | Docs support Shelly + smart light mapping |
| Living room | light | - | Living Room Ceiling Spotlight | Living Room Ceiling Spotlight | `light.living_room_light_spotlight` | Living room spotlight | Living room spotlight | likely | Smart light behind Shelly |
| Living room | light_power_relay | Living room window light | - | Living Room Window Light | `switch.living_room_light_window_power` | Living room window power | Living room window light | likely | Docs support Shelly + smart light mapping |
| Living room | light | - | Living Room Window Light | Living Room Window Light | `light.living_room_light_window` | Living room window light | Living room window light | likely | Smart light behind Shelly |
| Living room | light | - | Living room wall | Living room wall | `light.living_room_light_wall_lamp` | Living room wall lamp | Living room wall lamp | confirmed | Plug-in IKEA Tradfri bulb, not on Shelly lighting circuit |
| Living room | socket_power_relay | Living room sockets | - | Living room sockets | `switch.living_room_socket_main_power` | Living room main socket power | Living room main socket | likely | From Shelly inventory |
| Living room | socket_power_relay | TV electronics | - | Television etc | `switch.living_room_socket_tv_electronics_power` | Living room TV electronics power | TV electronics socket | likely | From Shelly inventory |

| Bedroom | light_group | - | - | Bedroom Lights | `light.bedroom_lights` | Bedroom lights | Bedroom lights | confirmed | Logical room lighting group |
| Bedroom | light_power_relay | Bedroom ceiling lights | - | Bedroom Lights | `switch.bedroom_light_ceiling_power` | Bedroom ceiling power | Bedroom lights | confirmed | Shelly master power/control circuit |
| Bedroom | light | - | Bedroom 1 | Bedroom 1 | `light.bedroom_light_1` | Bedroom light 1 | Bedroom light 1 | confirmed | IKEA Tradfri light behind Shelly |
| Bedroom | light | - | Bedroom 2 | Bedroom 2 | `light.bedroom_light_2` | Bedroom light 2 | Bedroom light 2 | confirmed | IKEA Tradfri light behind Shelly |
| Bedroom | light | - | Bedroom 3 | Bedroom 3 | `light.bedroom_light_3` | Bedroom light 3 | Bedroom light 3 | confirmed | IKEA Tradfri light behind Shelly |
| Bedroom | socket_power_relay | Bedroom left sockets | - | Bedroom left sockets | `switch.bedroom_socket_left_power` | Bedroom left socket power | Bedroom left socket | likely | From Shelly inventory |
| Bedroom | socket_power_relay | Bedroom right bed socket | - | Bedroom right bed socket | `switch.bedroom_socket_right_bed_power` | Bedroom right bed socket power | Bedroom right bed socket | likely | From Shelly inventory |
| Bedroom | socket_power_relay | Bedroom door socket | - | Bedroom door socket | `switch.bedroom_socket_door_power` | Bedroom door socket power | Bedroom door socket | likely | From Shelly inventory |
| Bedroom | socket_power_relay | Bedroom 2 socket | - | Bedroom 2 socket | `switch.bedroom_socket_2_power` | Bedroom 2 socket power | Bedroom 2 socket | likely | From Shelly inventory |

| Closet | light_group | - | - | Closet lights | `light.closet_lights` | Closet lights | Closet lights | confirmed | Logical closet lighting group for closet-area lights |
| Closet | light_power_relay | Walkin closet | - | Walkin closet | `switch.closet_light_walk_in_power` | Walk-in closet power | Walk-in closet light | confirmed | Standard Shelly-in-switch light circuit controlling the closet smart bulb |
| Closet | light | - | Bedroom closet | Bedroom closet | `light.closet_light_bedroom_closet` | Bedroom closet light | Bedroom closet light | confirmed | IKEA Tradfri bulb behind the closet Shelly-controlled light circuit |
| Closet | socket_power_relay | Walk-in closet socket | - | Walkin closet | `switch.closet_socket_walk_in_power` | Walk-in closet socket power | Walk-in closet socket | likely | Separate socket entry from Shelly inventory; keep as-is until device-by-device cleanup later |

| Hobby room | light_group | - | - | Hobby Room Lights | `light.hobby_room_lights` | Hobby room lights | Hobby room lights | confirmed | Logical room lighting group |
| Hobby room | light_power_relay | Hobby room light / Harrastushuone valo | - | Hobby room light | `switch.hobby_room_light_ceiling_power` | Hobby room ceiling power | Hobby room light | confirmed | Shelly side of pair |
| Hobby room | light | - | Hobby room ceiling | Hobby room ceiling | `light.hobby_room_light_ceiling` | Hobby room ceiling light | Hobby room ceiling light | confirmed | Smart light behind Shelly |
| Hobby room | socket_power_relay | Hobby room socket | - | Hobby room socket | `switch.hobby_room_socket_main_power` | Hobby room socket power | Hobby room socket | likely | From Shelly inventory |

| Office | light_group | - | - | Office Lights | `light.office_lights` | Office lights | Office lights | confirmed | Logical room lighting group |
| Office | light_power_relay | Office Ceiling Light | - | Office Ceiling Light | `switch.office_light_ceiling_power` | Office ceiling power | Office light | confirmed | Shelly and IKEA currently share same visible name |
| Office | light | - | Office Ceiling Light | Office Ceiling Light | `light.office_light_ceiling` | Office ceiling light | Office ceiling light | confirmed | IKEA / Tradfri light with same current name as Shelly |
| Office | socket_power_relay | Office right socket | - | Office right socket | `switch.office_socket_right_power` | Office right socket power | Office right socket | likely | From Shelly inventory |
| Office | socket_power_relay | Office door socket | - | Office door socket | `switch.office_socket_door_power` | Office door socket power | Office door socket | likely | From Shelly inventory |

| Corridor | light_group | - | - | Corridor Lights | `light.corridor_lights` | Corridor lights | Corridor lights | confirmed | Primary corridor light control should activate the whole corridor group |
| Corridor | light_power_relay | Corridor lights | - | Corridor Lights | `switch.corridor_light_group_power` | Corridor group power | Corridor lights | confirmed | Shelly power relay for the corridor lighting group |
| Corridor | light | - | Corridor Lights | Corridor Lights | `light.corridor_light_group` | Corridor light group member | Corridor lights | confirmed | Group-visible Tradfri lighting entity aligned to everyday use |
| Corridor | light | - | Corridor light 2 | Corridor light 2 | `light.corridor_light_2` | Corridor light 2 | Corridor light 2 | likely | Tradfri group member |
| Corridor | light | - | Corridor light 3 | Corridor light 3 | `light.corridor_light_3` | Corridor light 3 | Corridor light 3 | likely | Tradfri group member |
| Corridor | light | - | Corridor spotlight | Corridor spotlight | `light.corridor_light_spotlight` | Corridor spotlight | Corridor spotlight | likely | Tradfri group member |
| Corridor | socket_power_relay | Corridor vacuum socket | - | Corridor vacuum socket | `switch.corridor_socket_vacuum_power` | Corridor vacuum socket power | Corridor vacuum socket | likely | From Shelly inventory |
| Corridor | socket_power_relay | Corridor office socket | - | Corridor office socket | `switch.corridor_socket_office_power` | Corridor office socket power | Corridor office socket | likely | From Shelly inventory |

| Technical room | light_group | - | - | Technical room lights | `light.technical_room_lights` | Technical room lights | Technical room lights | confirmed | Normal Finnish technical room / utility room lighting area |
| Technical room | light_power_relay | Technical room light / Technical room | - | Technical room | `switch.technical_room_light_ceiling_power` | Technical room ceiling power | Technical room light | confirmed | Shelly controlling the technical room light circuit |
| Technical room | light | - | Technical room light | Technical room | `light.technical_room_light_ceiling` | Technical room ceiling light | Technical room ceiling light | confirmed | IKEA bulb on same light per docs |

| Sauna | light_group | - | - | Sauna lights | `light.sauna_lights` | Sauna lights | Sauna lights | confirmed | Logical room lighting group |
| Sauna | light_power_relay | Sauna wall light | - | Sauna Wall Light | `switch.sauna_light_wall_power` | Sauna wall power | Sauna wall light | confirmed | Shelly-only embedded non-smart light |
| Sauna | light_power_relay | Sauna bench lights | - | Sauna Bench Lights | `switch.sauna_light_bench_power` | Sauna bench power | Sauna bench light | confirmed | Shelly-only embedded non-smart light |

| Front yard | light_group | - | - | Front Yard Lights | `light.front_yard_lights` | Front yard lights | Front yard lights | confirmed | Logical outdoor lighting group |
| Front yard | light_power_relay | Front yard lights | - | Front yard lights | `switch.front_yard_light_power` | Front yard power | Front yard lights | confirmed | Shelly controlling power to Front yard 1 and Front yard 2 |
| Front yard | light | - | Front yard light 1 | Front yard light 1 | `light.front_yard_light_1` | Front yard light 1 | Front yard light 1 | confirmed | IKEA Tradfri light bulb behind Shelly circuit |
| Front yard | light | - | Front yard 2 | Front yard 2 | `light.front_yard_light_2` | Front yard light 2 | Front yard light 2 | confirmed | IKEA Tradfri light bulb behind Shelly circuit |
| Front yard | socket_power_relay | Front yard outdoor socket | - | Front yard outdoor socket | `switch.front_yard_socket_outdoor_power` | Front yard outdoor socket power | Front yard outdoor socket | likely | From Shelly inventory |

| Back yard | light_group | - | - | Back yard Lights | `light.back_yard_lights` | Back yard lights | Back yard lights | confirmed | Logical outdoor lighting group |
| Back yard | light_power_relay | Back yard lights | - | Back Yard Lights | `switch.back_yard_light_living_room_power` | Back yard living room power | Back yard lights | confirmed | Shelly for backyard lights; wall switch is located in living room |
| Back yard | light_power_relay | Back yard left light / Takapihan valo vasen | - | Takapihan valo vasen | `switch.back_yard_light_laundry_room_left_power` | Back yard laundry room left power | Back yard left light | confirmed | Shelly for backyard left branch; wall switch is located in laundry room |
| Back yard | light | - | Back Yard Lights | Back Yard Lights | `light.back_yard_light_main` | Back yard main light | Back yard main light | likely | Main group-visible light entity |
| Back yard | light | - | Back yard light 1 | Back yard light 1 | `light.back_yard_light_1` | Back yard light 1 | Back yard light 1 | likely | Tradfri member |
| Back yard | light | - | Back yard light 2 | Back yard light 2 | `light.back_yard_light_2` | Back yard light 2 | Back yard light 2 | likely | Tradfri member |
| Back yard | light | - | Back yard light 3 / Backyard light 3 | Backyard light 3 | `light.back_yard_light_3` | Back yard light 3 | Back yard light 3 | likely | Tradfri member; normalize later |

| Attic | light_group | - | - | Attic Lights | `light.attic_lights` | Attic lights | Attic lights | confirmed | Logical room lighting group |
| Attic | light_power_relay | Attic lights / Ullakkovalot | - | Ullakkovalot | `switch.attic_light_ceiling_power` | Attic ceiling power | Attic light | confirmed | Shelly inside switch for attic lighting circuit |
| Attic | light | - | Attic | Attic | `light.attic_light_ceiling` | Attic ceiling light | Attic light | confirmed | IKEA Tradfri light bulb behind attic Shelly circuit |

| Storage | light_group | - | - | Storage lights | `light.storage_lights` | Storage lights | Storage lights | confirmed | Logical room lighting group; user also referred to warehouse |
| Storage | light_power_relay | Storage light | - | Storage light | `switch.storage_light_ceiling_power` | Storage ceiling power | Storage light | confirmed | Shelly-only embedded non-smart light; user called this warehouse lights |

| WC | light_group | - | - | WC lights | `light.wc_lights` | WC lights | WC lights | confirmed | Logical room lighting group |
| WC | light_power_relay | WC ceiling light | - | WC Ceiling Light | `switch.wc_light_ceiling_power` | WC ceiling power | WC light | confirmed | Shelly-only embedded fixed/non-smart light |

---

## Critical infrastructure entities

| Area | Entity type | Current Shelly name | Current visible name | Target HA technical name | Target HA friendly name | Proposed spoken name | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| Network core | critical_power_relay | Network core power / Ftth | FTTH | `switch.network_core_power` | Network core power | Network core power | confirmed | Critical infrastructure; should remain separate from room/socket naming |

---

## Socket-only entities

| Room / Area | Entity type | Current Shelly name | Current visible name | Target HA technical name | Target HA friendly name | Proposed spoken name | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| Laundry room | socket_power_relay | Laundry room wall socket | Laundry room wall socket | `switch.laundry_room_socket_wall_power` | Laundry room wall socket power | Laundry room wall socket | likely | From Shelly inventory |
| Laundry room | socket_power_relay | Laundry room table socket | Laundry room table socket | `switch.laundry_room_socket_table_power` | Laundry room table socket power | Laundry room table socket | likely | From Shelly inventory |
| Laundry room | socket_power_relay | Laundry room lower cabinet socket | Laundry room lower cabinet socket | `switch.laundry_room_socket_lower_cabinet_power` | Laundry room lower cabinet socket power | Laundry room lower cabinet socket | likely | From Shelly inventory |
| Laundry room | socket_power_relay | Laundry room backyard door socket | Laundry room backyard door socket | `switch.laundry_room_socket_backyard_door_power` | Laundry room backyard door socket power | Laundry room backyard door socket | likely | From Shelly inventory |
| Bathroom | socket_power_relay | Bathroom cabinet socket | Bathroom cabinet socket | `switch.bathroom_socket_cabinet_power` | Bathroom cabinet socket power | Bathroom cabinet socket | likely | From Shelly inventory |
| Bathroom | socket_power_relay | Bathroom counter socket | Bathroom counter socket | `switch.bathroom_socket_counter_power` | Bathroom counter socket power | Bathroom counter socket | likely | From Shelly inventory |

---



## Legacy / parking rooms

- `X - Not in use` is a legacy Google Home holding / parking room
- it is **not** a real room in the target home architecture
- devices found there should be treated as:
  - temporarily parked
  - legacy leftovers
  - stale links pending cleanup
  - or unassigned devices waiting for proper placement
- this room must **not** be used as the basis for target HA room names or entity names
- if a device is found there in future API reads or exports, the device itself should still be mapped normally, but the room should be treated as operational/legacy metadata rather than architectural truth

## Later refinement items

These are not blockers for the technical mapping. They can be fine-tuned later once Home Assistant is running:

- spoken-name polishing for the most natural everyday commands
- optional cleanup of legacy current names across Shelly / IKEA / Google Home after the HA naming is in use
- device-by-device cleanup of any leftover duplicate-looking inventory entries during implementation

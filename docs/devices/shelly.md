# Shelly device inventory

This file is the main Shelly reference for the house.

Purpose:
- keep the full Shelly inventory in one place
- map IP addresses to the original Shelly names
- map those to current user-facing English names
- support future Home Assistant entity naming
- preserve source names from Shelly where they still exist

Naming rules:
- `original_shelly_name` = the original/device-side Shelly name
- `current_name` = the main English reference name for this project
- `google_home_name` = current visible Google Home name when known
- `planned_ha_name` = future preferred Home Assistant entity-friendly name

---

## Device table

| IP | current_name | original_shelly_name | google_home_name | planned_ha_name | type | notes |
|---|---|---|---|---|---|---|
| 10.107.1.21 | Hobby room light | Harrastushuone valo | Hobby room light | light.hobby_room_light | shelly_switch_light | Shelly-controlled light circuit |
| 10.107.1.23 | Corridor vacuum socket | Käytävä pistorasia imuri | Corridor vacuum socket | switch.corridor_vacuum_socket | shelly_socket | Vacuum socket in corridor |
| 10.107.1.24 | Kitchen desk lights | Kitchen desk lights | Kitchen desk lights | light.kitchen_desk_lights | shelly_switch_light | English Shelly name already used |
| 10.107.1.33 | Living room ceiling spotlight | Olohuone kattovalo spotti | Living Room Ceiling Spotlight | light.living_room_ceiling_spotlight | shelly_switch_light | |
| 10.107.1.35 | Laundry room wall socket | Kodinhoitohuone seinäpistoke | Laundry room wall socket | switch.laundry_room_wall_socket | shelly_socket | |
| 10.107.1.43 | Technical room light | Technical room | Technical room | light.technical_room_light | shelly_switch_light | Shelly controls technical room light; one IKEA bulb and one Shelly control same light |
| 10.107.1.48 | Laundry room table socket | Kodinhoitohuone pöytäpistoke | Laundry room table socket | switch.laundry_room_table_socket | shelly_socket | Table in laundry room |
| 10.107.1.52 | Office right socket | Työhuone oikea pistorasia | Office right socket | switch.office_right_socket | shelly_socket | |
| 10.107.1.56 | Living room window light | Olohuone ikkunavalo | Living Room Window Light | light.living_room_window_light | shelly_switch_light | |
| 10.107.1.70 | Living room sockets | Olohuone pistorasia | Living room sockets | switch.living_room_sockets | shelly_socket | |
| 10.107.1.72 | TV electronics | Televisio jne | Television etc | switch.tv_electronics | shelly_socket | TV / electronics power |
| 10.107.1.75 | Kitchen breakfast cabinet socket | Aamiaiskaappi | Breakfast cabinet | switch.kitchen_breakfast_cabinet_socket | shelly_socket | Cabinet/small-appliance power point |
| 10.107.1.77 | Bedroom ceiling lights | Makuuhuone kattovalot | Bedroom Lights | light.bedroom_ceiling_lights | shelly_switch_light | |
| 10.107.1.78 | Front yard lights | Etupiha valot | Front yard lights | light.front_yard_lights | shelly_switch_light | |
| 10.107.1.86 | Living room ceiling light | Olohuone kattovalo | Living Room Ceiling Light | light.living_room_ceiling_light | shelly_switch_light | |
| 10.107.1.90 | Back yard left light | Takapihan valo vasen | Back Yard Lights | light.back_yard_left_light | shelly_switch_light | |
| 10.107.1.98 | Laundry room lower cabinet socket | Kodinhoitohuone alakaappi | Laundry room lower cabinet socket | switch.laundry_room_lower_cabinet_socket | shelly_socket | |
| 10.107.1.118 | Corridor office socket | Käytävä työhuone pistorasia | Corridor office socket | switch.corridor_office_socket | shelly_socket | Socket near office/corridor area |
| 10.107.1.124 | Hall ceiling light | Eteinen kattovalo | Hall ceiling light | light.hall_ceiling_light | shelly_switch_light | |
| 10.107.1.130 | Sauna wall light | Sauna seinävalo | Sauna Wall Light | light.sauna_wall_light | shelly_switch_light | |
| 10.107.1.137 | Office door socket | Työhuone Ovi pistorasia | Office door socket | switch.office_door_socket | shelly_socket | |
| 10.107.1.138 | Laundry room light | Kodinhoitohuone valo | Laundry room light | light.laundry_room_light | shelly_switch_light | |
| 10.107.1.140 | Bathroom mirror light | Kylpyhuone peilivalo | Bathroom Mirror Light | light.bathroom_mirror_light | shelly_switch_light | |
| 10.107.1.143 | Office ceiling light | Työhuone kattovalo | Office Ceiling Light | light.office_ceiling_light | shelly_switch_light | |
| 10.107.1.164 | Bedroom 2 socket | Makuuhuone 2 pistorasia | Bedroom 2 socket | switch.bedroom_2_socket | shelly_socket | |
| 10.107.1.168 | Terrace light | Terassivalo | Terrace light | light.terrace_light | shelly_switch_light | |
| 10.107.1.179 | Front yard outdoor socket | Etupiha pistorasia | Front yard outdoor socket | switch.front_yard_outdoor_socket | shelly_socket | Outside socket at front of house |
| 10.107.1.180 | Kitchen counter socket | Keittiö työpöytä pistorasia | Kitchen counter socket | switch.kitchen_counter_socket | shelly_socket | |
| 10.107.1.184 | WC ceiling light | Wc kattovalo | WC Ceiling Light | light.wc_ceiling_light | shelly_switch_light | |
| 10.107.1.190 | Attic lights | Ullakkovalot | Attic lights | light.attic_lights | shelly_switch_light | |
| 10.107.1.191 | Bedroom door socket | Makuuhuone Ovi pistorasia | Bedroom door socket | switch.bedroom_door_socket | shelly_socket | |
| 10.107.1.192 | Walk-in closet socket | Walkin closet | Walkin closet | switch.walk_in_closet_socket | shelly_socket | |
| 10.107.1.195 | Laundry room backyard door socket | Kodinhoitohuone ulko-oven pistorasia | Laundry room backyard door socket | switch.laundry_room_backyard_door_socket | shelly_socket | Socket next to backyard/outside door |
| 10.107.1.196 | Sauna bench lights | Sauna laudevalot | Sauna Bench Lights | light.sauna_bench_lights | shelly_switch_light | |
| 10.107.1.203 | Bathroom ceiling lights | Kylpyhuone kattovalo | Bathroom Ceiling Lights | light.bathroom_ceiling_lights | shelly_switch_light | |
| 10.107.1.204 | Bathroom cabinet socket | Kylpyhuone kaappipistoke | Bathroom cabinet socket | switch.bathroom_cabinet_socket | shelly_socket | |
| 10.107.1.207 | Bathroom counter socket | Kylpyhuone pöytäpistoke | Bathroom counter socket | switch.bathroom_counter_socket | shelly_socket | |
| 10.107.1.221 | Network core power | Ftth | FTTH | switch.network_core_power | shelly_power_critical | Critical connectivity device; router + fiber chain behind this |
| 10.107.1.222 | Bedroom left sockets | Makuuhuone vasemmat pistorasiat | Bedroom left sockets | switch.bedroom_left_sockets | shelly_socket | |
| 10.107.1.223 | Unresolved real Shelly device | Unknown | Unknown | unresolved.10_107_1_223 | unresolved_real_device | Real device from verified 45-device scan; still needs identification |
| 10.107.1.227 | Bedroom right bed socket | Makuuhuone sänky oikea | Bedroom right bed socket | switch.bedroom_right_bed_socket | shelly_socket | |
| 10.107.1.228 | Corridor lights | Käytävä valot | Corridor lights | light.corridor_lights | shelly_switch_light | |
| 10.107.1.231 | Kitchen ceiling lights | Keittiö kattovalot | Kitchen Ceiling Light | light.kitchen_ceiling_lights | shelly_switch_light | |
| 10.107.1.232 | Hobby room socket | Harrastushuone pistorasia | Hobby room socket | switch.hobby_room_socket | shelly_socket | |
| 10.107.1.251 | Storage light | Varasto valo | Storage light | light.storage_light | shelly_switch_light | |

---

## Notes

### Laundry room
Laundry room has:
- one inside door
- one door to bathroom
- one door to backyard/outside

`10.107.1.195` is the socket right next to the backyard/outside door.

### Technical room
`10.107.1.43` is the Shelly for the technical room light.
There is one IKEA Tradfri bulb and one Shelly controlling the same light.

### FTTH
`10.107.1.221` is the critical FTTH Shelly.
This should be treated as `network_core_power`.

### Matter
All Shelly devices in this inventory are Gen4 and support Matter.
Even so, project design currently treats Shelly native/local control as primary and Matter as optional/secondary unless a later design decision changes this.

### Important modeling rule for Shelly + smart bulb circuits
Current reality in some rooms:
- a Shelly may physically cut power to a smart bulb circuit
- the smart bulb is therefore not assumed to stay powered at all times
- automations must respect real electrical state, not only logical state

Future target architecture may move selected smart-bulb circuits toward always-powered smart-bulb design where practical.

---

## Confirmed Shelly Gen4 MQTT rollout pattern

### Working pilot
- Device: Harrastushuone valo
- IP: 10.107.1.21
- Shelly device ID / MQTT prefix: shelly1g4-ccba97c89350
- HA server IP: 10.107.1.101

### Shelly MQTT settings
- Enable: on
- Connection type: No TLS
- Enable MQTT Control: on
- Enable RPC over MQTT: on
- RPC status notifications over MQTT: on
- Generic status update over MQTT: on
- Server: 10.107.1.101:1883
- Username/password: Mosquitto user
- MQTT prefix: keep device prefix as-is during migration

### Home Assistant YAML pattern
- command_topic: <device_id>/rpc
- state_topic: <device_id>/status/switch:0
- availability_topic: <device_id>/online
- command via Switch.Set RPC
- state from value_json.output

### Important rules
- Do NOT use manually created MQTT devices in HA UI for Shelly rollout
- Use YAML-managed MQTT entities
- Keep current Shelly / Google Home names as migration anchors
- Apply final naming later in HA layer


---

## Naming policy during migration

- Shelly device names are NOT changed during MQTT rollout
- Home Assistant entity names MUST follow entity_name_mapping.md
- Final naming is applied at the HA layer only
- Google Home and IKEA naming remain unchanged during migration

This ensures stable operation while transitioning control to Home Assistant.


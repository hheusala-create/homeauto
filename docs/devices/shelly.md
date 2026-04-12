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

| IP | mqtt_device_id | current_name | original_shelly_name | google_home_name | planned_ha_name | type | notes |
|---|---|---|---|---|---|---|---|
| 10.107.1.21 | shelly1g4-ccba97c89350 | Hobby room light | Harrastushuone valo | Hobby room light | light.hobby_room_light | shelly_switch_light | Shelly-controlled light circuit |
| 10.107.1.23 |  | Corridor vacuum socket | Käytävä pistorasia imuri | Corridor vacuum socket | switch.corridor_vacuum_socket | shelly_socket | Vacuum socket in corridor |
| 10.107.1.24 | shelly1pmg4-a085e3bcfb14 | Kitchen desk lights | Kitchen desk lights | Kitchen desk lights | light.kitchen_led | shelly_switch_light | Dedicated socket-fed kitchen LED lighting circuit; Shelly 1PM Gen4; YAML-managed MQTT relay active |
| 10.107.1.33 |  | Living room ceiling spotlight | Olohuone kattovalo spotti | Living Room Ceiling Spotlight | light.living_room_ceiling_spotlight | shelly_switch_light | |
| 10.107.1.35 |  | Laundry room wall socket | Kodinhoitohuone seinäpistoke | Laundry room wall socket | switch.laundry_room_wall_socket | shelly_socket | |
| 10.107.1.43 | shelly1g4-a085e3bd87d0 | Technical room light ceiling | Technical room | Technical room | switch.technical_room_light_ceiling_power | shelly_switch_light | Shelly + TRÅDFRI circuit; YAML-managed MQTT relay active; wall-switch automation active |
| 10.107.1.48 |  | Laundry room table socket | Kodinhoitohuone pöytäpistoke | Laundry room table socket | switch.laundry_room_table_socket | shelly_socket | Table in laundry room |
| 10.107.1.52 |  | Office right socket | Työhuone oikea pistorasia | Office right socket | switch.office_right_socket | shelly_socket | |
| 10.107.1.56 |  | Living room window light | Olohuone ikkunavalo | Living Room Window Light | light.living_room_window_light | shelly_switch_light | |
| 10.107.1.70 |  | Living room sockets | Olohuone pistorasia | Living room sockets | switch.living_room_sockets | shelly_socket | |
| 10.107.1.72 |  | TV electronics | Televisio jne | Television etc | switch.tv_electronics | shelly_socket | TV / electronics power |
| 10.107.1.75 | shelly1g4-ccba97c89b84 | Kitchen breakfast cabinet light | Aamiaiskaappi | Breakfast cabinet | light.breakfast_cabin | shelly_switch_light | Dedicated socket-fed breakfast cabinet LED lighting circuit; YAML-managed MQTT relay active |
| 10.107.1.77 | shelly1g4-ccba97c888c8 | Bedroom ceiling lights | Makuuhuone kattovalot | Bedroom Lights | light.bedroom_ceiling_lights | shelly_switch_light | |
| 10.107.1.78 | shelly1pmg4-a085e3bbd280 | Front yard lights | Etupiha valot | Front yard lights | switch.front_yard_light_power | shelly_switch_light | Shelly + TRÅDFRI circuit; YAML-managed MQTT relay active; wall-switch automation active |
| 10.107.1.86 |  | Living room ceiling light | Olohuone kattovalo | Living Room Ceiling Light | light.living_room_ceiling_light | shelly_switch_light | |
| 10.107.1.90 |  | Back yard left light | Takapihan valo vasen | Back Yard Lights | light.back_yard_left_light | shelly_switch_light | Legacy inventory row; newer backyard split documented separately below |
| 10.107.1.98 |  | Laundry room lower cabinet socket | Kodinhoitohuone alakaappi | Laundry room lower cabinet socket | switch.laundry_room_lower_cabinet_socket | shelly_socket | |
| 10.107.1.118 |  | Corridor office socket | Käytävä työhuone pistorasia | Corridor office socket | switch.corridor_office_socket | shelly_socket | Socket near office/corridor area |
| 10.107.1.124 | shelly1pmg4-a085e3bd0210 | Hall ceiling light | Eteinen kattovalo | Hall ceiling light | switch.hall_light_ceiling_power | shelly_switch_light | Shelly + TRÅDFRI circuit; YAML-managed MQTT relay active; wall-switch automation active |
| 10.107.1.130 | shelly1g4-ccba97c89804 | Sauna wall light | Sauna seinävalo | Sauna Wall Light | switch.sauna_light_wall_power | shelly_switch_light | Fixed light; exposed in HA also through user-facing light wrapper |
| 10.107.1.137 |  | Office door socket | Työhuone Ovi pistorasia | Office door socket | switch.office_door_socket | shelly_socket | |
| 10.107.1.138 | shelly1g4-a085e3bd8af0 | Laundry room ceiling light | Kodinhoitohuone valo | Laundry room light | switch.laundry_room_light_ceiling_power | shelly_switch_light | Shelly + TRÅDFRI circuit; YAML-managed MQTT relay active; wall-switch automation active |
| 10.107.1.140 | shelly1g4-a085e3bcd118 | Bathroom mirror light | Kylpyhuone peilivalo | Bathroom Mirror Light | switch.bathroom_light_mirror_power | shelly_switch_light | Fixed light; exposed in HA also through user-facing light wrapper |
| 10.107.1.143 | shelly1g4-ccba97c8968c | Office ceiling light | Työhuone kattovalo | Office Ceiling Light | switch.office_light_ceiling_power | shelly_switch_light | Shelly + TRÅDFRI circuit; YAML-managed MQTT relay active; wall-switch automation active |
| 10.107.1.164 |  | Bedroom 2 socket | Makuuhuone 2 pistorasia | Bedroom 2 socket | switch.bedroom_2_socket | shelly_socket | |
| 10.107.1.168 |  | Terrace light | Terassivalo | Terrace light | light.terrace_light | shelly_switch_light | |
| 10.107.1.179 |  | Front yard outdoor socket | Etupiha pistorasia | Front yard outdoor socket | switch.front_yard_outdoor_socket | shelly_socket | Outside socket at front of house ||
| 10.107.1.190 | shelly1g4-a085e3c197b0 | Attic light ceiling | Ullakkovalot | Attic lights | switch.attic_light_ceiling_power | shelly_switch_light | Practical exception: Shelly + TRÅDFRI exists underneath, but user-facing implementation is intentionally simplified to Shelly-only style; exposed in HA through light wrapper | |
| 10.107.1.192 | shelly1g4-ccba97c8a17c | Walk-in closet light | Walkin closet | Walkin closet | light.walk_in_closet | shelly_switch_light | Confirmed Shelly + one IKEA bulb in closet |
| 10.107.1.195 |  | Laundry room backyard door socket | Kodinhoitohuone ulko-oven pistorasia | Laundry room backyard door socket | switch.laundry_room_backyard_door_socket | shelly_socket | Socket next to backyard/outside door |
| 10.107.1.196 | shelly1g4-ccba97c8a044 | Sauna bench light | Sauna laudevalot | Sauna Bench Lights | switch.sauna_light_bench_power | shelly_switch_light | Fixed light; exposed in HA also through user-facing light wrapper |
| 10.107.1.203 | shelly1g4-ccba97c8cbf8 | Bathroom ceiling light | Kylpyhuone kattovalo | Bathroom Ceiling Lights | switch.bathroom_light_ceiling_power | shelly_switch_light | Fixed light; exposed in HA also through user-facing light wrapper | |
| 10.107.1.207 |  | Bathroom counter socket | Kylpyhuone pöytäpistoke | Bathroom counter socket | switch.bathroom_counter_socket | shelly_socket | |
| 10.107.1.221 |  | Network core power | Ftth | FTTH | switch.network_core_power | shelly_power_critical | Critical connectivity device; router + fiber chain behind this |
| 10.107.1.222 |  | Bedroom left sockets | Makuuhuone vasemmat pistorasiat | Bedroom left sockets | switch.bedroom_left_sockets | shelly_socket | |
| 10.107.1.227 |  | Bedroom right bed socket | Makuuhuone sänky oikea | Bedroom right bed socket | switch.bedroom_right_bed_socket | shelly_socket | |
| 10.107.1.228 |  | Corridor lights | Käytävä valot | Corridor lights | light.corridor_lights | shelly_switch_light | |
| 10.107.1.231 | shelly1g4-a085e3bd891c | Kitchen ceiling lights | Keittiö kattovalot | Kitchen Ceiling Light | light.kitchen_ceiling_lights | shelly_switch_light | |
| 10.107.1.232 |  | Hobby room socket | Harrastushuone pistorasia | Hobby room socket | switch.hobby_room_socket | shelly_socket | |
| 10.107.1.251 | shelly1pmg4-a085e3bbb77c | Warehouse light ceiling | Varasto valo | Storage light | switch.warehouse_light_ceiling_power | shelly_switch_light | Fixed light; exposed in HA also through user-facing light wrapper |
| - | - | Living room wall light | - | Living room wall light | light.living_room_wall | smart_bulb_only | TRÅDFRI bulb in socket; no Shelly and no wall switch |
| - | shelly1g4-a085e3bcdf24 | Living room spotlight | Living room ceiling spotlight | Living Room Ceiling Spotlight | light.living_room_spotlight | shelly_switch_light | Active Shelly + smart bulb circuit; detached mode; wall switch controls light through HA automation |
| - | shelly1g4-a085e3c16eec | Living room window light | Olohuone ikkunavalo | Living Room Window Light | light.living_room_window | shelly_switch_light | Shelly present in MQTT; relay_only for now; no final lamp decision yet |
| - | shelly1g4-ccba97c89790 | Living room ceiling light | Olohuone kattovalo | Living Room Ceiling Light | light.living_room_ceiling | shelly_switch_light | Shelly present in MQTT; relay_only for now; no final lamp decision yet |
| - | shelly1g4-ccba97c8856c | Back yard lights living room | - | Back yard lights living room | switch.back_yard_light_living_room_power | shelly_switch_light | Relay-only mixed circuit; includes normal non-TRÅDFRI lamp; must currently cut power normally; exposed in HA also through user-facing light wrapper |
| - | shelly1g4-a085e3c16c94 | Back yard lights laundry room | - | Back yard lights laundry room | switch.back_yard_light_laundry_room_power | shelly_switch_light | Shelly + TRÅDFRI circuit; current HA automation targets `light.backyard_light_3` | | 10.107.1.181 | shelly1pmg4-a085e3bc8c14 | Kitchen counter socket | Keittiö työpöytä pistorasia | Kitchen counter socket | switch.kitchen_counter_socket | shelly_socket | Current IP corrected from latest full scan; older documented IP was 10.107.1.180 |
| 10.107.1.185 | shelly1g4-a085e3bd81e4 | WC ceiling light | Wc kattovalo | WC Ceiling Light | switch.wc_light_ceiling_power | shelly_switch_light | Shelly + TRÅDFRI circuit; YAML-managed MQTT relay active; wall-switch automation active; current IP corrected from latest full scan |
| 10.107.1.192 | shelly1g4-a085e3c18bb4 | Bedroom door socket | Makuuhuone Ovi pistorasia | Bedroom door socket | switch.bedroom_door_socket | shelly_socket | Current IP corrected from latest full scan; older documented IP was 10.107.1.191 |
| 10.107.1.203 | shelly1g4-a085e3bcd294 | Bathroom cabinet socket | Kylpyhuone kaappipistoke | Bathroom cabinet socket | switch.bathroom_cabinet_socket | shelly_socket | Current IP corrected from latest full scan; older documented IP was 10.107.1.204 |
| 10.107.1.224 | shelly1g4-a085e3bcd2a8 | Unresolved real Shelly device | Unknown | Unknown | unresolved.10_107_1_224 | unresolved_real_device | Real device from verified full scan; current IP corrected from older unresolved placeholder 10.107.1.223 |

---

## Recent inventory corrections and rollout notes

### Latest confirmed full-scan identity rule

Recent rollout work confirmed that Shelly inventory matching must prefer:

1. `mqtt_device_id` / Shelly device ID
2. IP address only as secondary mutable data

Reason:
- several Shelly devices were confirmed to have changed IP addresses
- device ID stayed stable and is the correct primary identity key for matching inventory, MQTT topics, and rollout targets

### Recent confirmed IP corrections

The following inventory corrections were confirmed from the latest full scan:

- WC ceiling light
  - device ID: `shelly1g4-a085e3bd81e4`
  - current IP: `10.107.1.185`
  - older documented IP was outdated

- Kitchen counter socket
  - device ID: `shelly1pmg4-a085e3bc8c14`
  - current IP: `10.107.1.181`
  - older documented IP was `10.107.1.180`

- Bedroom door socket
  - device ID: `shelly1g4-a085e3c18bb4`
  - current IP: `10.107.1.192`
  - older documented IP was `10.107.1.191`

- Bathroom cabinet socket
  - device ID: `shelly1g4-a085e3bcd294`
  - current IP: `10.107.1.203`
  - older documented IP was `10.107.1.204`

- Previously unresolved real Shelly device
  - current IP: `10.107.1.224`
  - device ID: `shelly1g4-a085e3bcd2a8`
  - older unresolved placeholder IP was `10.107.1.223`

### Recent bulk MQTT rollout rule confirmation

During recent Shelly socket rollout work, the practical safe pattern was confirmed as:

1. apply MQTT settings
2. reboot Shelly
3. verify after reboot

Important rule:
- do not combine firmware update into the same bulk rollout script
- one tested firmware update stalled during update and required manual reboot recovery
- therefore bulk rollout should use MQTT configuration + reboot only

### Critical exclusions during bulk rollout

The following Shelly devices must stay excluded from bulk MQTT actions unless handled deliberately:

- `10.107.1.221`
  - device ID: `shelly1pmg4-a085e3bdd5f4`
  - role: network core power
  - reason: critical infrastructure

- `10.107.1.232`
  - device ID: `shelly1pmg4-a085e3bc5718`
  - role: hobby room socket
  - reason at time of rollout: actively powering the Home Assistant server path

### Recent non-critical socket rollout target set

A recent non-critical rollout set was prepared and validated from full-scan data using device ID matching and latest IP confirmation.

This confirmed that recent Shelly rollout work is no longer only about light circuits:
- socket/power Shelly inventory is now part of the active rollout baseline
- future Shelly documentation must keep light-power circuits and socket circuits clearly separated

## Notes

### Laundry room
Laundry room has:
- one inside door
- one door to bathroom
- one door to backyard/outside

`10.107.1.195` is the socket right next to the backyard/outside door.

### Technical room
The earlier technical room inventory row used older incomplete metadata.
The currently active Shelly mapping in Home Assistant uses:
- MQTT device ID: `shelly1g4-a085e3bd87d0`
- technical relay entity: `switch.technical_room_light_ceiling_power`
- wall-switch automation active

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

### Confirmed smart-bulb wall-switch pattern for normal 2-position wall switches

For Shelly + smart bulb circuits with a normal wall switch:

- input mode must be set to `Switch`
- relay mode must be set to `Detached`
- relay power-on default should keep the relay ON so the smart bulb remains powered
- Home Assistant should react to switch state/input, not assume button-style events unless the Shelly configuration has been verified

Do **not** use `Button` input mode for normal 2-position wall switches.

Reason:
- `Button` mode can produce button-style events such as `btn_down`, `btn_up`, and `long_push`
- this can misrepresent the real physical behavior of a normal wall switch
- a wrong assumption here can lead to wrong architectural conclusions for the broader rollout

Confirmed pilot result for `Harrastushuone valo`:
- misleading intermediate test setting: `Button` + `Detached`
- correct working model for a normal wall switch: `Switch` + `Detached`

Verification rule before rollout decisions:
- before making broader Shelly design decisions from a pilot, first verify the exact device-side Shelly settings
- especially confirm input mode (`Button` vs `Switch`)
- do not generalize MQTT/event behavior until the physical Shelly settings have been checked on the device

### Confirmed default rollout model for Shelly + smart bulb circuits

The Hobby room implementation is the reference model for this rollout.

Default model:
- one YAML-managed Shelly relay entity in HA
- no separate wall-switch `binary_sensor` by default
- one HA automation listening directly to:
  - `<device_id>/status/input:0`
- one target light entity representing the actual smart bulb / logical light

Reason:
- keeps the HA entity model cleaner during wider rollout
- avoids unnecessary extra entities for all Shelly devices
- still provides full required control for `shelly_plus_smart_bulb` circuits

A separate wall-switch `binary_sensor` is optional and may still be used in selected cases for:
- debugging
- visibility
- more advanced logic

It is not the default rollout requirement.

### Confirmed switch-direction normalization rule

For normal 2-position wall switches in lighting circuits, the target behavior is:

- up = light on
- down = light off

Important implementation note:

- in the current Shelly + smart bulb model, this direction is effectively decided in the Home Assistant automation YAML
- the automation mapping determines whether:
  - `trigger.payload_json.state == true` turns the light on or off
  - `trigger.payload_json.state == false` turns the light on or off

Confirmed lesson from pilot comparison:
- Hobby room and Walk-in closet had matching Shelly-side settings
- despite that, their initial physical switch directions differed
- this indicates that physical wiring or switch orientation can cause opposite behavior even when device settings match

Therefore:
- switch-direction consistency must be validated room by room
- when needed, normalize direction in HA automation logic
- the required user-facing result is always:
  - up = light on
  - down = light off

---

## Naming policy during migration

- Shelly device names are NOT changed during MQTT rollout
- Home Assistant entity names MUST follow entity_name_mapping.md
- Final naming is applied at the HA layer only
- Google Home and IKEA naming remain unchanged during migration

This ensures stable operation while transitioning control to Home Assistant.

### YAML-managed Shelly relay rule

When a Shelly relay is represented in Home Assistant through YAML-managed MQTT `switch` entities, use the verified working `ON/OFF` mapping pattern.

Use:
- `value_template` mapping `value_json.output` to `ON` / `OFF`
- `payload_on: "ON"`
- `payload_off: "OFF"`
- `state_on: "ON"`
- `state_off: "OFF"`

Do not switch these MQTT relay entities to a `true/false` state-mapping model.

Important distinction:
- YAML-managed MQTT relay entities use `ON/OFF`
- Shelly input automations may still use `trigger.payload_json.state == true/false`

### Fixed-light wrapper pattern now in active use

Some fixed Shelly-controlled lights are now exposed in Home Assistant through a `switch_as_x` light wrapper.

Meaning:
- technical relay remains the MQTT `switch.*` entity
- user-facing everyday control uses `light.*`

Current examples:
- bathroom ceiling light
- bathroom mirror light
- sauna bench light
- sauna wall light
- warehouse light ceiling
- back yard lights living room
- attic light ceiling

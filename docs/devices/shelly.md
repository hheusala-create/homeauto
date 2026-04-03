# Shelly device inventory

This file is the main Shelly reference for the house.

Purpose:
- keep the full Shelly inventory in one place
- map IP addresses to the original Shelly names
- map those to current user-facing English names
- support future Home Assistant entity naming
- preserve Finnish source names from Shelly where they still exist

Naming rules:
- `original_shelly_name` = the original/device-side Shelly name, often Finnish
- `current_name` = the name currently most useful for the user
- `google_home_name` = current visible Google Home name when known
- `planned_ha_name` = future preferred Home Assistant entity-friendly name
- do not delete original Finnish names even if English is used elsewhere

---

## Device table

| IP | current_name | original_shelly_name | google_home_name | planned_ha_name | type | notes |
|---|---|---|---|---|---|---|
| 10.107.1.221 | FTTH | Ftth | FTTH | switch.ftth | shelly_power_critical | Critical connectivity device |
| 10.107.1.43 | Technical room light Shelly | Technical room light Shelly | Technical room | light.technical_room_power | shelly_switch_light | Shelly for technical room light power; one IKEA bulb and one Shelly control same light |
| 10.107.1.179 | Front yard socket | Etupiha pistorasia | Front yard socket | switch.front_yard_socket | shelly_socket | Outside socket at front yard |
| 10.107.1.232 | Hobby room socket | Harrastushuone pistorasia | Hobby room socket | switch.hobby_room_socket | shelly_socket | |
| 10.107.1.21 | Hobby room light | Harrastushuone valo | Hobby room ceiling | light.hobby_room_light_power | shelly_switch_light | Shelly cuts power to smart bulb/light circuit |
| 10.107.1.168 | Terrace light | Terassivalo | Terrace light | light.terrace_light | shelly_switch_light | |
| 10.107.1.130 | Sauna wall light | Sauna seinävalo | Sauna Wall Light | light.sauna_wall_light | shelly_switch_light | |
| 10.107.1.124 | Front hall ceiling light | Eteinen kattovalo | Hall / Front hall ceiling light | light.front_hall_ceiling | shelly_switch_light | |
| 10.107.1.78 | Front yard lights | Etupiha valot | Front yard lights | light.front_yard_lights | shelly_switch_light | |
| 10.107.1.190 | Attic lights | Ullakkovalot | Attic / Ullakkovalot | light.attic_lights | shelly_switch_light | |
| 10.107.1.138 | Laundry room light | Kodinhoitohuone valo | Laundry room | light.laundry_room_light | shelly_switch_light | |
| 10.107.1.48 | Laundry room table socket | Kodinhoitohuone Pöytäpistoke | Laundry room table socket | switch.laundry_room_table_socket | shelly_socket | Table in laundry room |
| 10.107.1.195 | Laundry room outdoor-door socket | Kodinhoitohuone ulko-oven pistorasia | Laundry room outdoor-door socket | switch.laundry_room_outdoor_door_socket | shelly_socket | Socket next to backyard/out door |
| 10.107.1.35 | Laundry room wall socket | Kodinhoitohuone seinäpistoke | Laundry room wall socket | switch.laundry_room_wall_socket | shelly_socket | |
| 10.107.1.98 | Laundry room lower cabinet socket | Kodinhoitohuone alakaappi | Laundry room lower cabinet socket | switch.laundry_room_lower_cabinet_socket | shelly_socket | |
| 10.107.1.140 | Bathroom mirror light | Kylpyhuone peilivalo | Bathroom Mirror Light | light.bathroom_mirror_light | shelly_switch_light | |
| 10.107.1.203 | Bathroom ceiling lights | Kylpyhuone kattovalo | Bathroom Ceiling Lights | light.bathroom_ceiling_lights | shelly_switch_light | |
| 10.107.1.207 | Bathroom table socket | Kylpyhuone pöytäpistoke | Bathroom table socket | switch.bathroom_table_socket | shelly_socket | |
| 10.107.1.204 | Bathroom cabinet socket | Kylpyhuone kaappipistoke | Bathroom cabinet socket | switch.bathroom_cabinet_socket | shelly_socket | |
| 10.107.1.56 | Living room window light | Olohuone ikkunavalo | Living Room Window Light | light.living_room_window_light | shelly_switch_light | |
| 10.107.1.86 | Living room ceiling light | Olohuone kattovalo | Living Room Ceiling Light | light.living_room_ceiling_light | shelly_switch_light | |
| 10.107.1.33 | Living room ceiling spotlight | Olohuone kattovalo spotti | Living Room Ceiling Spotlight | light.living_room_ceiling_spotlight | shelly_switch_light | |
| 10.107.1.70 | Living room wall socket | Olohuone pistorasia | Living room wall | switch.living_room_wall_socket | shelly_socket | Confirm if this is the wall light/power point circuit you referred to |
| 10.107.1.72 | Television etc | Televisio jne | Television etc | switch.television_etc | shelly_socket | |
| 10.107.1.222 | Bedroom left sockets | Makuuhuone vasemmat pistorasiat | Bedroom left sockets | switch.bedroom_left_sockets | shelly_socket | |
| 10.107.1.227 | Bedroom right bed socket | Makuuhuone sänky oikea | Bedroom right bed socket | switch.bedroom_right_bed_socket | shelly_socket | |
| 10.107.1.191 | Bedroom door socket | Makuuhuone Ovi pistorasia | Bedroom door socket | switch.bedroom_door_socket | shelly_socket | |
| 10.107.1.164 | Bedroom 2 socket | Makuuhuone 2 pistorasia | Bedroom 2 socket | switch.bedroom_2_socket | shelly_socket | |
| 10.107.1.77 | Bedroom ceiling lights | Makuuhuone kattovalot | Bedroom Lights / Bedroom ceiling lights | light.bedroom_ceiling_lights | shelly_switch_light | |
| 10.107.1.192 | Walk-in closet | Walkin closet | Walkin closet | switch.walk_in_closet | shelly_socket | Confirm whether this should be closet light or socket naming |
| 10.107.1.180 | Kitchen worktop socket | Keittiö työpöytä pistorasia | Kitchen desk lights / Kitchen worktop socket | switch.kitchen_worktop_socket | shelly_socket | Check final user-facing name |
| 10.107.1.75 | Breakfast cabinet | Aamiaiskaappi | Breakfast Cabin Light / Aamiaiskaappi | switch.breakfast_cabinet | shelly_socket | Confirm whether this is socket, cabinet light, or grouped power |
| 10.107.1.231 | Kitchen ceiling lights | Keittiö kattovalot | Kitchen Ceiling Light | light.kitchen_ceiling_lights | shelly_switch_light | |
| 10.107.1.184 | WC ceiling light | Wc kattovalo | WC Ceiling Light | light.wc_ceiling_light | shelly_switch_light | |
| 10.107.1.90 | Back yard left light | Takapihan valo vasen | Back Yard Lights / left | light.back_yard_left_light | shelly_switch_light | |
| 10.107.1.24 | Kitchen desk lights | Kitchen desk lights | Kitchen desk lights | light.kitchen_desk_lights | shelly_switch_light | English device name already used |
| 10.107.1.71 | Unknown | Unknown | Unknown | unknown.10_107_1_71 | unknown | Not yet mapped |
| 10.107.1.73 | Unknown | Unknown | Unknown | unknown.10_107_1_73 | unknown | Not yet mapped |
| 10.107.1.74 | Unknown | Unknown | Unknown | unknown.10_107_1_74 | unknown | Not yet mapped |
| 10.107.1.76 | Unknown | Unknown | Unknown | unknown.10_107_1_76 | unknown | Not yet mapped |
| 10.107.1.79 | Unknown | Unknown | Unknown | unknown.10_107_1_79 | unknown | Not yet mapped |
| 10.107.1.87 | Unknown | Unknown | Unknown | unknown.10_107_1_87 | unknown | Not yet mapped |
| 10.107.1.88 | Unknown | Unknown | Unknown | unknown.10_107_1_88 | unknown | Not yet mapped |
| 10.107.1.89 | Unknown | Unknown | Unknown | unknown.10_107_1_89 | unknown | Not yet mapped |
| 10.107.1.91 | Unknown | Unknown | Unknown | unknown.10_107_1_91 | unknown | Not yet mapped |
| 10.107.1.92 | Unknown | Unknown | Unknown | unknown.10_107_1_92 | unknown | Not yet mapped |

---

## Notes

### Laundry room
Laundry room has:
- one inside door
- one door to bathroom
- one door to backyard/outside

`10.107.1.195` is the socket right next to the backyard/out door.

### Technical room
`10.107.1.43` is the Shelly for the technical room light.
There is one IKEA Tradfri bulb and one Shelly controlling the same light.

### FTTH
`10.107.1.221` is the critical FTTH Shelly.

### Matter
All Shelly devices in this inventory are Gen4 and support Matter.
Even so, project design currently treats Shelly native/local control as primary and Matter as optional/secondary unless a later design decision changes this.

### Important modeling rule for Shelly + smart bulb circuits
Where a Shelly physically cuts power to a smart bulb circuit:
- the Shelly remains the real power authority
- the bulb is not assumed to stay powered if the wall switch/Shelly cuts power
- automations must respect real electrical state, not only logical state

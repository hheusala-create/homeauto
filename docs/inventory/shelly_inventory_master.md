# Shelly inventory master

## Purpose
Master inventory of all Shelly devices.  
Used for Home Assistant setup, naming, and automation design.

---

## Core rules
- Physical wall switches must always work
- Shelly = primary control layer
- IKEA Tradfri = secondary layer
- Critical devices must be protected
- Naming follows Google Home structure

---

## Critical device

| IP | Name | Notes |
|----|------|------|
| 10.107.1.221 | network_core_power | FTTH / router / fiber power – CRITICAL |

---

## Device inventory

| IP | Name |
|----|------|
| 10.107.1.21  | hobby_room_light |
| 10.107.1.23  | hallway_socket_vacuum |
| 10.107.1.24  | kitchen_desk_lights |
| 10.107.1.33  | living_room_ceiling_spots |
| 10.107.1.35  | laundry_room_wall_socket |
| 10.107.1.43  | technical_room_light |
| 10.107.1.48  | laundry_room_table_socket |
| 10.107.1.52  | office_right_socket |
| 10.107.1.56  | living_room_window_light |
| 10.107.1.70  | living_room_sockets |
| 10.107.1.72  | television_area |
| 10.107.1.75  | kitchen_breakfast_cabinet_socket |
| 10.107.1.77  | bedroom_ceiling_lights |
| 10.107.1.78  | frontyard_lights |
| 10.107.1.86  | living_room_ceiling_light |
| 10.107.1.90  | backyard_left_light |
| 10.107.1.98  | laundry_room_lower_cabinet_socket |
| 10.107.1.118 | hallway_office_socket |
| 10.107.1.124 | entrance_ceiling_light |
| 10.107.1.130 | sauna_wall_light |
| 10.107.1.137 | office_door_socket |
| 10.107.1.138 | laundry_room_light |
| 10.107.1.140 | bathroom_mirror_light |
| 10.107.1.143 | office_ceiling_light |
| 10.107.1.164 | bedroom_2_sockets |
| 10.107.1.168 | terrace_light |
| 10.107.1.179 | front_yard_outdoor_socket |
| 10.107.1.180 | kitchen_counter_socket |
| 10.107.1.184 | wc_ceiling_light |
| 10.107.1.190 | attic_lights |
| 10.107.1.191 | bedroom_door_socket |
| 10.107.1.192 | walk_in_closet_socket |
| 10.107.1.195 | laundry_room_backyard_door_socket |
| 10.107.1.196 | sauna_bench_lights |
| 10.107.1.203 | bathroom_ceiling_light |
| 10.107.1.204 | bathroom_cabinet_socket |
| 10.107.1.207 | bathroom_counter_socket |
| 10.107.1.222 | bedroom_left_sockets |
| 10.107.1.227 | bedroom_bed_right_socket |
| 10.107.1.228 | hallway_lights |
| 10.107.1.231 | kitchen_ceiling_lights |
| 10.107.1.232 | hobby_room_socket |
| 10.107.1.251 | storage_light |

---

## Notes

- Naming is aligned with Google Home rooms
- All devices verified manually via Shelly app
- This is the authoritative source for HA setup

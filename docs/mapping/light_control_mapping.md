# Light Control Mapping

Purpose:
Map physical Shelly circuits to smart-light entities and define the future Home Assistant control model.

Control models:
- `relay_only`
- `shelly_plus_smart_bulb`
- `critical_power`
- `socket`

---

## Mapping table

| Area | Current user-facing light | Shelly device | Shelly IP | Tradfri / Google Home light | Control model | Planned HA entity | Notes |
|---|---|---|---|---|---|---|---|
| Technical room | Technical room | Technical room light | 10.107.1.43 | Technical room | shelly_plus_smart_bulb | light.technical_room | One Shelly + one IKEA bulb on same light |
| Hall | Hall ceiling light | Hall ceiling light | 10.107.1.124 | Hall Light | shelly_plus_smart_bulb | light.hall | |
| Laundry room | Laundry room light | Laundry room light | 10.107.1.138 | Laundry room | shelly_plus_smart_bulb | light.laundry_room | |
| Bathroom | Bathroom ceiling lights | Bathroom ceiling lights | 10.107.1.203 | Bathroom Ceiling Lights | shelly_plus_smart_bulb | light.bathroom_ceiling | |
| Bathroom | Bathroom mirror light | Bathroom mirror light | 10.107.1.140 | Bathroom Mirror Light | shelly_plus_smart_bulb | light.bathroom_mirror | |
| Living room | Living room ceiling light | Living room ceiling light | 10.107.1.86 | Living Room Ceiling Light | shelly_plus_smart_bulb | light.living_room_ceiling | |
| Living room | Living room ceiling spotlight | Living room ceiling spotlight | 10.107.1.33 | Living Room Ceiling Spotlight | shelly_plus_smart_bulb | light.living_room_spotlight | |
| Living room | Living room window light | Living room window light | 10.107.1.56 | Living Room Window Light | relay_only | light.living_room_window | Confirm if no Tradfri behind this |
| Hobby room | Hobby room light | Hobby room light | 10.107.1.21 | Hobby room light | shelly_plus_smart_bulb | light.hobby_room | |
| Kitchen | Kitchen ceiling lights | Kitchen ceiling lights | 10.107.1.231 | Kitchen Ceiling Light | shelly_plus_smart_bulb | light.kitchen_ceiling | |
| Kitchen | Kitchen desk lights | Kitchen desk lights | 10.107.1.24 | Kitchen desk lights | relay_only | light.kitchen_desk | Confirm if no Tradfri behind this |
| Sauna | Sauna wall light | Sauna wall light | 10.107.1.130 | Sauna Wall Light | shelly_plus_smart_bulb | light.sauna_wall | |
| Sauna | Sauna bench lights | Sauna bench lights | 10.107.1.196 | Sauna Bench Lights | shelly_plus_smart_bulb | light.sauna_bench | |
| Bedroom | Bedroom ceiling lights | Bedroom ceiling lights | 10.107.1.77 | Bedroom Lights | shelly_plus_smart_bulb | light.bedroom_ceiling | |
| WC | WC ceiling light | WC ceiling light | 10.107.1.184 | Wc Ceiling Light | shelly_plus_smart_bulb | light.wc | |
| Front yard | Front yard lights | Front yard lights | 10.107.1.78 | Front yard lights | shelly_plus_smart_bulb | light.front_yard | |
| Back yard | Back yard left light | Back yard left light | 10.107.1.90 | Back Yard Lights | shelly_plus_smart_bulb | light.back_yard | Needs grouping confirmation |
| Attic | Attic lights | Attic lights | 10.107.1.190 | Attic | shelly_plus_smart_bulb | light.attic | |
| FTTH | FTTH | Network core power | 10.107.1.221 | - | critical_power | switch.network_core_power | Must never be in bulk off automations |

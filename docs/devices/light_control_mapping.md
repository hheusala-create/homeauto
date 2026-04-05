
---

## Confirmed MQTT pilot

### Hobby room (Harrastushuone valo)

Status:
- Working Shelly Gen4 MQTT pilot via Home Assistant YAML

Technical mapping:
- Shelly device ID: shelly1g4-ccba97c89350
- Command topic: shelly1g4-ccba97c89350/rpc
- State topic: shelly1g4-ccba97c89350/status/switch:0
- Availability topic: shelly1g4-ccba97c89350/online

Notes:
- Uses YAML-managed MQTT entity (not HA UI-created MQTT device)
- Serves as reference implementation for all Shelly rollout
- Final HA logical naming will follow planned entity:
  light.hobby_room


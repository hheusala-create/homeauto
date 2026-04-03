# Critical Devices

## Network Core Power

This device controls the main internet connection power.

It powers:
- router
- fiber converter (kuitumuunnin)

If this device is turned off:
- internet connection is lost
- remote control from outside home is lost
- remote troubleshooting may be lost

### Current behavior
- In Shelly there is a script that turns the power back on after about 10-20 seconds
- The device is intentionally not assigned to a room to avoid accidental presses

### Rules
- Must never be turned off accidentally
- Must not be shown as a normal room device in dashboards
- Must be treated as critical infrastructure
- Must keep the auto-recovery logic unless a better safe solution is implemented later

### Planned Home Assistant naming
- Entity purpose: network core power
- Suggested name: `network_core_power`

### Notes
- This is not a normal socket
- This is a critical infrastructure control point

## Emergency:

This is the Emergency stop state that disables propulsion and engages break actuators. It can be entered from any other state if abnormal behavior is detected.

The causes for engagement are as follows:

- Any sensor malfunction
- Short distance sensor hazard detected
- Tempature sensor detects temperatures out of range
- Pressure sensor detects pressure out of range
- IMU reads an acceleration too elevated
- Inductive Proximity Sensor or IMU show pod positioning is hazardous
- Manual command is issued
- State is likely to fail

## Drive States:

### Verification:

Ensures state integrity and sensor functionality and can transition to stop or to pre-acceleration states.

### Pre-acceleration:

Opens brake calipers and prepares any other actuators for propulsion.

### Acceleration:

Engages propulsion system while monitoring sensor values to reach target speed.

### Cruise:

Pod is at target speed with consistent velocity. Positioning and sensor integrity are being continuously verified.

### Deceleration:

Decreases velocity gradually to bring the pod to a halt at the target location.

## Stop:

Pod is fully halted with the brake calipers closed. This state can be entered from `Deceleration`, `Emergency`, or `Verification`, and can transition into an `Off` state or a `Crawl` state.

## Crawl:

Low-Speed system engaged. Pod begins slow acceleration from the stopped state towards the end of the track and can re-enter `Deceleration`.

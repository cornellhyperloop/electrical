# Modules

# Fiducial Detector

### Inputs

- Optical Sensor
  - Data source: Arduino

### Objective

- Detects optical markings within the tube at a high frequency to allow for accurate pod positioning

### Technical Requirements

- TBD

# Flight Controller

### Inputs

- IMUs
  - Data source: Arduino
- Fiducial Detector

### Objective

- Leverages sensor data to estimate pod position
- Dispatches controls to the pod to produce braking commands to ensure pod trajectory is intended

### Technical Requirements

- TBD

# Low-Speed Module

### Inputs

- Braking Commands
- Analog sensor data

### Objective

- Actuates everything on the pod including motors and brakes

### Technical Requirements

- TBD

# Front and Rear Analog

### Inputs

- Variety of pod sensors (lateral distance, pod suspension, temperature of batteries)

### Objective

- Provide data to the Low-Speed Module

### Technical Requirements

- TBD

# Modules

# Fiducial Detector

### Inputs

#### Ideal

- Optical Sensor
  - Data source: Arduino

#### Current

- Long-range Laser Rangefinder
- Retroreflective Sensor (Marshall Wolf SA1E-PN2)

### Objective

- Detects optical markings within the tube at a high frequency to allow for accurate pod positioning

### Technical Requirements

- Markings
  - These marks are 4” wide and occur at 100 ft intervals. Assuming a relative pod speed of 110 m/sec, the marks will be measurable for 400 μs. Therefore, the optical sensor must have a minimum sampling rate of 5 kHz.

# Flight Controller

### Inputs

- IMUs
  - A single Vectornav VN-100 Rugged will serve as the IMU input
  - Data source: Arduino
- Fiducial Detector

### Objective

- Leverages sensor data to estimate pod position
- Dispatches controls to the pod to produce braking commands to ensure pod trajectory is intended

# Low-Speed Module

### Inputs

- Braking Commands
- Analog sensor data

### Objective

- Actuates everything on the pod including motors and brakes

### Actuators

- (1) Solenoid Valve w/ 24V input
  - Used for the air tank
- Mechanical braking mechanisms

# Front and Rear Analog

### Inputs

- (\*) 10kohm NTC thermistors to measure temperature of batteries
- (4) Pressure sensor (Model unknown; see FDP for possible options. Number will correspond to the number of pressure vessels in use—likely about 4)
- (4) Inductive proximity sensor (Model unknown)

### Objective

- Provide data to the Low-Speed Module

# Use live data for graph
LIVE_DATA = False
ARDUINO_SERIAL = "/dev/cu.usbmodem11101"

GRAPH_IMG_NAME = "Graph.png"

# FSM Data
CURRENT_STATE = "Deceleration"
STATES = {
    'Stop': 'state_icons/stop.png',
    'Crawl': 'state_icons/crawl.png',
    'Deceleration': 'state_icons/deceleration.png',
    'Cruise': 'state_icons/cruise.png',
    'Emergency': 'state_icons/emergency.png',
    'Verification': 'state_icons/verification.png',
    'Pre-Acceleration': 'state_icons/pre_acceleration.png',
    'Acceleration': 'state_icons/acceleration.png',
    'Overheating': 'state_icons/overheating.png',
    'Extreme Overheating': 'state_icons/extreme_overheating.png'
}

# Battery Pack Data
# Numbers in the lists are dummy data
BATTERY_CURRENT_TEMP = 0
BATTERY_MAXIMUM_TEMP = 100
BATTERY = [1, 2, 3, 4, 5]
VOLTAGE = [5, 10, 15, 20, 25]
CURRENT = [5, 10, 15, 20, 25]


# Inductive Proximity Sensor Data
PROXIMITY_INPUT1 = 2
PROXIMITY_LED1 = 13
PROXIMITY_SENSOR_STATE1 = "high"
PROXIMITY_INPUT2 = 2
PROXIMITY_LED2 = 13
PROXIMITY_SENSOR_STATE2 = "high"
PROXIMITY_INPUT3 = 2
PROXIMITY_LED3 = 13
PROXIMITY_SENSOR_STATE3 = "high"
PROXIMITY_INPUT4 = 2
PROXIMITY_LED4 = 13
PROXIMITY_SENSOR_STATE4 = "high"

# Vibration Sensor Data
VIBRATIONLEVEL = "low"

# Inertial Measurement Unit Data
CURRENT_VELOCITY = 50
ACCELERATION = 70
VELOCITY_THRESHOLD = 60
ACCELERATION_THRESHOLD = 60
PITCH = [90, -132, 54, 2]
YAW = [129, 0, -83, 324]
ROLL = [-12, 55, 39, 360]

# Pressure Sensor Data
ABSOLUTE_PRESSURE = 30.29
RELATIVE_PRESSURE = 29.80
ALTITUDE = 33000

# Long Distance Range Finder Data
DISTANCE = 30

# Progress Bar Data
LABEL_STYLE_SHEET = "color: white; background-color: #2B26c1; selection-color: grey; selection-background-color: blue; border: 1px grey"
PBAR_LOW_PROGRESS = "QProgressBar::chunk {background-color: red;}"
PBAR_MED_PROGRESS = "QProgressBar::chunk {background-color: gold;}"
PBAR_HIGH_PROGRESS = "QProgressBar::chunk {background-color: green;}"

# Live plotting
NUM_PLOTS = 2
# For now, have the second plot increase much faster than the first
PLOT_INCREMENTS = [1, 10]

# File names
GRAPH_IMG_NAME = "Graph.png"

WIDGETS = "widgets/widgets.css"
REDWIDGETS = "widgets/redwidgets.css"

# **Sensor Dashboard Application**

Welcome to the **Sensor Dashboard Application**! This application is built using **Dash** and **Dash Bootstrap Components** to provide a real-time dashboard for monitoring various sensors. The application is modular, allowing easy addition of new sensors and tabs without modifying the core codebase.

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Adding New Sensors](#adding-new-sensors)
- [Adding New Tabs](#adding-new-tabs)
- [Data Handlers](#data-handlers)
- [Key Files and Modules](#key-files-and-modules)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## **Project Overview**

The Sensor Dashboard Application allows users to:

- Monitor real-time data from multiple sensors.
- Visualize sensor data through interactive graphs.
- Dynamically select which sensors to display.
- Easily extend functionality by adding new sensors or tabs.

The application uses a **modular architecture** to promote scalability and maintainability.

---

## **Features**

- **Dynamic Tab Management**: Automatically discovers and loads tabs without manual updates.
- **Sensor Cards**: Modular sensor cards display sensor-specific data and graphs.
- **Data Handlers**: Process and format raw sensor data for display.
- **Real-Time Updates**: Sensor data is updated at configurable intervals.
- **Emergency Button**: A global emergency button for critical actions.
- **Responsive Design**: Uses Dash Bootstrap Components for mobile-friendly layouts.

---

## **Project Structure**

```
sensor_dashboard/
├── app.py
├── layout.py
├── callbacks.py
├── sensors/
│   ├── __init__.py
│   ├── load_sensors.py
│   └── communication.py
├── tabs/
│   ├── __init__.py
│   ├── sensor_tab/
│   │   ├── __init__.py
│   │   ├── layout.py
│   │   ├── callbacks.py
│   │   ├── components.py
│   │   ├── data_handlers/
│   │   │   ├── __init__.py
│   │   │   ├── base_data_handler.py
│   │   │   ├── accelerometersensor_data_handler.py
│   │   │   └── temperaturesensor_data_handler.py
│   │   └── sensor_cards/
│   │       ├── __init__.py
│   │       ├── base_sensor_card.py
│   │       ├── accelerometersensor_card.py
│   │       └── temperaturesensor_card.py
│   └── another_tab/
│       ├── __init__.py
│       ├── layout.py
│       └── callbacks.py
├── assets/
│   └── custom.css
├── requirements.txt
└── README.md
```

---

## **Installation**

### **Prerequisites**

- Python 3.7 or higher
- pip (Python package installer)

### **Steps**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/sensor_dashboard.git
   cd sensor_dashboard
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Serial Communication (If Using PySerialCommunication)**

   Ensure you have the correct serial port and permissions set up for your environment.

---

## **Usage**

To run the application, execute:

```bash
python app.py
```

The dashboard will be accessible at `http://127.0.0.1:8050/` in your web browser.

---

## **Configuration**

### **Serial Communication**

- **File**: `sensors/communication.py`
- **Class**: `PySerialCommunication`
- **Parameters**:
  - `port`: The serial port (e.g., `/dev/ttyUSB0` or `COM3`).
  - `baudrate`: Communication speed (e.g., `9600`).
  - `timeout`: Read timeout in seconds.

### **Adjusting Update Intervals**

- Each sensor card has an "Update Interval" input to adjust the data refresh rate.
- Default interval is set to 5 seconds.

---

## **Adding New Sensors**

To add a new sensor:

1. **Create Sensor Class**

   - **File**: `sensors/your_sensor.py`
   - **Example**:

     ```python
     # sensors/your_sensor.py
     class YourSensor:
         def __init__(self, communication):
             self.name = "Your Sensor Name"
             self.data_fields = ['field1', 'field2']
             self.communication = communication

         def get_data(self):
             # Implement data retrieval logic
             pass
     ```

2. **Update `load_sensors` Function**

   - **File**: `sensors/load_sensors.py`
   - **Add Your Sensor to the List**

     ```python
     from .your_sensor import YourSensor

     def load_sensors(communication):
         sensors = [
             YourSensor(communication),
             # ... other sensors
         ]
         return sensors
     ```

3. **Create Sensor Card (Optional for Custom Behavior)**

   - **File**: `tabs/sensor_tab/sensor_cards/your_sensor_card.py`
   - **Example**:

     ```python
     # tabs/sensor_tab/sensor_cards/your_sensor_card.py
     from .base_sensor_card import BaseSensorCard

     class YourSensorCard(BaseSensorCard):
         def __init__(self, app, sensor_name, sensor):
             super().__init__(app, sensor_name, sensor)
             # Custom initialization if needed

         def register_callbacks(self):
             # Implement sensor-specific callbacks
             pass
     ```

4. **Implement Sensor-Specific Callbacks (If Needed)**

   - **Override** the `register_callbacks` method in your sensor card class.

5. **Create Data Handler (If Data Processing is Required)**

   - **File**: `tabs/sensor_tab/data_handlers/yoursensor_data_handler.py`
   - **Example**:

     ```python
     # tabs/sensor_tab/data_handlers/yoursensor_data_handler.py
     from .base_data_handler import BaseSensorDataHandler

     class YourSensorDataHandler(BaseSensorDataHandler):
         def process_data(self, df, parameters=None):
             # Implement data processing logic
             return df

         def format_current_values(self, latest_data, parameters=None):
             # Format the current values for display
             return {}

         def get_yaxis_title(self, field, parameters=None):
             # Return y-axis title for graphs
             return f"{field.capitalize()} (Units)"
     ```

---

## **Adding New Tabs**

To add a new tab:

1. **Create Tab Directory**

   - **Directory**: `tabs/your_new_tab/`
   - **Files Needed**:
     - `__init__.py`
     - `layout.py`
     - `callbacks.py` (if callbacks are required)

2. **Define Tab Attributes in `__init__.py`**

   ```python
   # tabs/your_new_tab/__init__.py
   tab_id = 'your-new-tab'
   tab_label = 'Your New Tab'

   from .layout import get_layout
   from .callbacks import register_callbacks
   ```

3. **Implement `get_layout` Function**

   - **File**: `tabs/your_new_tab/layout.py`
   - **Example**:

     ```python
     # tabs/your_new_tab/layout.py
     from dash import html

     def get_layout(sensors):
         return html.Div([
             html.H3('Welcome to Your New Tab'),
             # Add your layout components here
         ])
     ```

4. **Implement Callbacks (Optional)**

   - **File**: `tabs/your_new_tab/callbacks.py`
   - **Example**:

     ```python
     # tabs/your_new_tab/callbacks.py
     def register_callbacks(app, sensors):
         @app.callback( ... )
         def your_callback(...):
             pass
     ```

5. **No Need to Update Core Files**

   - The application will automatically discover and include your new tab.

---

## **Data Handlers**

Data handlers are responsible for processing raw sensor data before it is displayed. They can apply transformations, formatting, and calculations specific to each sensor type.

### **Base Data Handler**

- **File**: `tabs/sensor_tab/data_handlers/base_data_handler.py`
- **Class**: `BaseSensorDataHandler`

  ```python
  # tabs/sensor_tab/data_handlers/base_data_handler.py
  class BaseSensorDataHandler:
      def __init__(self, sensor_name, sensor):
          self.sensor_name = sensor_name
          self.sensor = sensor

      def process_data(self, df, parameters=None):
          # Implement generic data processing
          return df

      def format_current_values(self, latest_data, parameters=None):
          # Implement generic formatting of current values
          return {}

      def get_yaxis_title(self, field, parameters=None):
          # Return generic y-axis title
          return field.capitalize()
  ```

### **Creating a Data Handler for a Sensor**

1. **Create Sensor-Specific Data Handler**

   - **File**: `tabs/sensor_tab/data_handlers/yoursensor_data_handler.py`
   - **Class**: `YourSensorDataHandler`

     ```python
     # tabs/sensor_tab/data_handlers/yoursensor_data_handler.py
     from .base_data_handler import BaseSensorDataHandler

     class YourSensorDataHandler(BaseSensorDataHandler):
         def process_data(self, df, parameters=None):
             # Apply sensor-specific data processing
             return df

         def format_current_values(self, latest_data, parameters=None):
             # Format current values with units and precision
             return {}

         def get_yaxis_title(self, field, parameters=None):
             # Provide y-axis titles for graphs
             return f"{field.capitalize()} (Units)"
     ```

2. **Implement Data Processing Logic**

   - **`process_data` Method**: Clean, filter, or transform the raw data as needed.
   - **`format_current_values` Method**: Prepare the latest data point for display, including units and formatting.
   - **`get_yaxis_title` Method**: Provide appropriate y-axis labels for graphs.

3. **Ensure Dynamic Loading**

   - The sensor card callbacks dynamically load the appropriate data handler based on the sensor name.
   - **Naming Convention**: The data handler file and class should be named following the pattern:

     - **File**: `<sensorname>_data_handler.py` (e.g., `accelerometersensor_data_handler.py`)
     - **Class**: `<SensorName>DataHandler` (e.g., `AccelerometerSensorDataHandler`)

4. **Example: Accelerometer Sensor Data Handler**

   ```python
   # tabs/sensor_tab/data_handlers/accelerometersensor_data_handler.py
   from .base_data_handler import BaseSensorDataHandler

   class AccelerometerSensorDataHandler(BaseSensorDataHandler):
       def process_data(self, df, parameters=None):
           # Apply scaling factors or filters
           return df

       def format_current_values(self, latest_data, parameters=None):
           # Format acceleration values with units
           current_values = {}
           for field in ['Acceleration_X', 'Acceleration_Y', 'Acceleration_Z']:
               value = latest_data.get(field, 'N/A')
               current_values[field] = f"{value:.2f} m/s²" if value != 'N/A' else 'N/A'
           return current_values

       def get_yaxis_title(self, field, parameters=None):
           return "Acceleration (m/s²)"
   ```

### **Integration with Sensor Cards**

- Sensor cards use data handlers to process and display data.
- In the sensor card callback:

  ```python
  # Within the sensor card's callback function
  data_handler = data_handler_class(sensor_name, sensor)
  df = data_handler.process_data(df, parameters)
  current_values = data_handler.format_current_values(latest_data, parameters)
  yaxis_title = data_handler.get_yaxis_title(field, parameters)
  ```

---

## **Key Files and Modules**

### **`app.py`**

- Initializes the Dash app and server.
- Loads sensors and assigns the main layout.
- Registers general callbacks (e.g., Emergency button).

### **`layout.py`**

- Defines the main layout of the application.
- Includes the Navbar, Emergency button, tabs, and tab content container.

### **`callbacks.py`**

- Contains general application callbacks.
- Currently handles the Emergency button logic.

### **`tabs/__init__.py`**

- Dynamically discovers and registers tabs.
- Sets up the `tabs-content` callback to render selected tab content.

### **`tabs/sensor_tab/`**

- Contains the implementation for the "Sensors" tab.
- **`layout.py`**: Defines the layout for the sensor tab.
- **`callbacks.py`**: Handles sensor-specific callbacks.
- **`components.py`**: Contains functions to create sensor cards.
- **`data_handlers/`**: Contains data handler classes for processing sensor data.

### **`sensors/`**

- Contains sensor classes and the `load_sensors` function.
- **`communication.py`**: Defines communication classes for sensors.

---

## **Troubleshooting**

### **Graphs Not Appearing at Initialization**

- Ensure that the default tab is set correctly in `layout.py`.
- Verify that the `tabs-content` callback is rendering the initial content.
- Check that placeholder graphs are included in the sensor cards.
- Confirm that data handlers are correctly processing and providing data.

### **Duplicate Callback Errors**

- Ensure that each `Output` is only targeted by one callback.
- Avoid setting `allow_duplicate=True` unless necessary.
- Check that sensor-specific callbacks do not overlap with general callbacks.

### **Sensors Not Updating**

- Verify the communication setup in `sensors/communication.py`.
- Check that the sensor's `get_data` method is implemented correctly.
- Ensure that the `dcc.Interval` components are triggering updates.
- Confirm that data handlers are correctly processing the data.

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

   ```bash
   git clone https://github.com/yourusername/sensor_dashboard.git
   ```

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make Changes and Commit**

   ```bash
   git add .
   git commit -m "Add your feature"
   ```

4. **Push to Your Fork and Submit a Pull Request**

   ```bash
   git push origin feature/your-feature
   ```

---

## **License**

This project is licensed under the MIT License.

---

## **Updates and Notes**

- **Modular Architecture**: The project is designed to be modular. Adding new sensors or tabs does not require changes to the core files.
- **Placeholder Graphs**: Sensor cards now include placeholder graphs at initialization to enhance the user experience.
- **Data Handlers**: Added data handlers for processing and formatting sensor data before display.
- **Callback Management**: Callbacks are organized to prevent duplication errors and ensure maintainability.
- **Layout Separation**: The main layout is defined in `layout.py`, keeping `app.py` clean and focused on initialization and callback registration.
- **Dynamic Tab Discovery**: Tabs are automatically discovered and registered, simplifying the process of adding new tabs.

---

Thank you for using the Sensor Dashboard Application! If you have any questions or need further assistance, please feel free to reach out.

---

**Note on Data Handlers:**

Data handlers play a crucial role in the application by ensuring that sensor data is properly processed and presented to the user. When adding new sensors, it is recommended to create a corresponding data handler if the sensor data requires specific processing or formatting. This ensures consistency and clarity in the data presented on the dashboard.

If you need further assistance with data handlers or any other part of the application, please let me know!

int pin_hallEffect_north = 2; // Pin that the North Hall Effect Sensor is connected to
int pin_hallEffect_south = 3; // Pin that the South Hall Effect Sensor is connected to

int rotation_count = 0; // Number of total rotations that we have counted
double previous_time = -1; // Last time at which the north hall effect sensor was active

int state; // Current State

// System State Definitions
#define POWER_UP 0 // When the device has been powered up
#define TRAVEL_NORTH 1 // When the magnet on the wheel is traveling north
#define TRAVEL_SOUTH 2 // When the magnet on the wheel is traveling south

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(pin_hallEffect_north, INPUT); // We will be reading from these pins, so they're setup as an INPUT pin
  pinMode(pin_hallEffect_south, INPUT);

  state = POWER_UP; // Starting state of the FSM
}

boolean check_north_sensors()
{
  return pin_hallEffect_north = 0; // Hall Effect Sensors are active low
}

boolean check_south_sensors()
{
  return pin_hallEffect_south == 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  if (state == POWER_UP)
  {
    if (check_north_sensors())
    {
      state = TRAVEL_SOUTH;
    }
    else
      if(check_south_sensors())
      {
        state = TRAVEL_NORTH;
      }
  }
  else
  {
    if (state == TRAVEL_NORTH && check_north_sensors())
    {
      state = TRAVEL_SOUTH;
      rotation_count++;

      if (previous_time == -1)
        previous_time = micros();
      else
      {
        double curr_time = micros();
        Serial.print("Current Instantaneous RPM: ");
        Serial.println(60000000 / (curr_time - previous_time));
        previous_time = curr_time;
      }
    }
    else
    {
      if (state == TRAVEL_SOUTH && check_south_sensors())
        state = TRAVEL_NORTH;
    }
  }
}

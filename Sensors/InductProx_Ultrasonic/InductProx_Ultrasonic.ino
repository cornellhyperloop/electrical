/*
Code for Inductive Proximity Sensor, Ultrasonic Rangefinder, and Thermistor
Goal is to have the LED turn on when the inductive proximity sensor detects something 
and to print values for all sensors to serial so we can read them in C++

March 21, 2023
*/

//////////////////////////////////////////////////////////
// Inductive Proximity Sensor Variables
//////////////////////////////////////////////////////////

// Input Output
const int proximityInput = 2;
const int LED = 13;

// Sensor Variable
int InductiveSensorState;

// String to C
String InductMessage;

//////////////////////////////////////////////////////////
// Ultrasonic Rangefinder Variables
//////////////////////////////////////////////////////////

// Use digital pin 7 to read PW from the device. Pin number does not change in this code
const int pwPin = 7;

// Store calculated value
long pW;
float inches, cm, meters;

// Sensor Variable
float UltrasonicSensorState;

// String to C
String UltrasonicMessage;

//////////////////////////////////////////////////////////
// Thermistor Variables
//////////////////////////////////////////////////////////
int ThermistorPin = A0;
int Vo;
float R1 = 100000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;
String ThermistorMessage;

//////////////////////////////////////////////////////////
// Setup both sensors and serial connection
//////////////////////////////////////////////////////////

void setup() {
  // Sets up pins as Input and Output (Inductive Proximity Sensor)
  pinMode(proximityInput, INPUT_PULLUP);
  pinMode(LED, OUTPUT); 
  
  // Sets up pins as Input and Output (Ultrasonic Rangefinder)
  pinMode(pwPin, INPUT);

  // Setup the serial connection
  Serial.begin(115200);
}

//////////////////////////////////////////////////////////
// Function to read ultrasonic rangefinder (returns distance in meters)
//////////////////////////////////////////////////////////

float read_usRange() { 
  // Read pulse sent by device
  // Conversion for PW: 147 uS per Inch
  pW = pulseIn(pwPin, HIGH);

  inches = pW/147;
  cm = inches * 2.54;
  meters = cm/100;
  
  return meters;
}

//////////////////////////////////////////////////////////
// Short delay (500 ms) to allow everything to be transmitted before sending new value
//////////////////////////////////////////////////////////
void short_delay() {
  delay(500);
}

//////////////////////////////////////////////////////////
// Read both sensors and transmit their values
//////////////////////////////////////////////////////////

void loop() {

  //////////////////////////////////////////////////////////
  // Read and transmit inductive proximity sensor value
  //////////////////////////////////////////////////////////

  // Reads the value as either high or low
  InductiveSensorState = digitalRead(proximityInput);

  // Get the value as a string with its identifier
  if ( InductiveSensorState == LOW ) {
    InductMessage = "I,0\n\r";
  }
  else {
    InductMessage = "I,1\n\r";
  }
  
  // Print the sensor data to serial
  Serial.print(InductMessage);

  // sensorState == LOW means there is a detectable object within sensor's proximity
  if (InductiveSensorState == HIGH) {
    // Turn the LED on
    digitalWrite(LED, HIGH);
  }
  else {
    digitalWrite(LED, LOW);
  }

  //////////////////////////////////////////////////////////
  // Short delay
  //////////////////////////////////////////////////////////
  short_delay();

  //////////////////////////////////////////////////////////
  // Read and transmit ultrasonic rangefinder value
  //////////////////////////////////////////////////////////

  // Read the data
  UltrasonicSensorState = read_usRange();

  // Get the value as a string with its identifier
  UltrasonicMessage = "U," + String(UltrasonicSensorState) + "\n\r";

  // Print sensor data to serial
  Serial.print(UltrasonicMessage);

  //////////////////////////////////////////////////////////
  // Short delay
  //////////////////////////////////////////////////////////
  short_delay();

  //////////////////////////////////////////////////////////
  // Read and transmit ultrasonic rangefinder value
  //////////////////////////////////////////////////////////

  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0;

  // Get the value as a string with its identifier
  ThermistorMessage = "T," + String(-Tf) + "\n\r";

  Serial.print(ThermistorMessage);

  //////////////////////////////////////////////////////////
  // Short delay
  //////////////////////////////////////////////////////////
  short_delay();

}

/*
As the main file, it will raise a flag if there are errors detected by
the Pressure, Vibration, Ultrasonic_Rangefinder, Inductive Proximity Sensor.

The output meaning will be stored in a string with each integer representing detection from a certain sensor:
alert = Inductive Ultrasonic Vibration Pressure

Inductive: 0 = object within sensor proximity ; 1 = otherwise
Ultrasonic: 0 = object is too close ; 1 = otherwise
Vibration: 0 = pushbutton is pressed ; 1 = otherwise
Pressure: 0 = pressure is too high ; 1 = Error Retrieving Some Measurement; 2 = Otherwise 

Note: For the ultrasonic and pressure function, we need to have a constant setup for an accepted threshold value
They are currently both set equal to zero. 

This uses a transmitter module that is designed for Arduino Mega

Updated: December 8, 2020
*/

// Set up code and variables needed for the various sensors

// Vibration Variables
const int buttonPin = 2;    // the number of the pushbutton pin
const int buzzer =  3;      // the number of the buzzer pin
int buttonState = 0;        // variable for reading the pushbutton status

// Ultrasonic Rangefinder Variables
// Use PulseWidth (PW) to detect range. Digital pin 7 will read PW from the device (won't change)
const int pwPin = 7;
// Variables to store calculated value
long pW, inches, cm, meters; 

// Inductive Proximity Variables
// Input Output Constants 
const int proximityInput = 2;
const int LED = 13;
int sensorState;

// Pressure Set Up
// Your sketch must #include this library, and the Wire library (a standard library included with Arduino.):
#include <SFE_BMP180.h>
#include <Wire.h>

// Create an SFE_BMP180 object
SFE_BMP180 pressure;
#define ALTITUDE 123.0 // Altitude of Ithaca, NY according to Wikipedia

// Pressure Set Up Function
void pressSet(){
  Serial.begin(9600);
  // Initialize the sensor (it is important to get calibration values stored on the device).
  if (pressure.begin())
    Serial.println("BMP180 init success");
  else
  {
    // Something went wrong (usually a connection problem). 
    Serial.println("BMP180 init fail\n\n");
    while(1); // Pause forever.
  }
}

// Necessary for Transmitter
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001"; // can be any 5 letter string

void setup() {
  // Most of this set up probably isn't needed 
  // Vibration 
  pinMode(buzzer, OUTPUT);      // initialize the LED pin as an output
  pinMode(buttonPin, INPUT);    // initialize the pushbutton pin as an input
  
  // Ultrasonic Rangefinder
  // Creates serial connection to send results back to PC Console 
  Serial.begin(9600);
  pinMode(pwPin, INPUT);
  
  // Inductive Proximity
  // Sets up pins as Input and Output
  pinMode(proximityInput, INPUT_PULLUP);
  pinMode(LED, OUTPUT); 
  
  // Pressure
  pressSet();
  
  // Transmitter
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening(); // for receiver
}

int inductive(){
  // Code for inductive proximity sensor. Return true if detects an object within sensor proximity. False otherwise
  
  // Reads the value as either high or low 
  sensorState = digitalRead(proximityInput);
  // sensorState == LOW means there is a detectable object within sensor's proximity
  if(sensorState == LOW){
    return 0;
  }
  else{
    return 1;
  }
}

// Ultrasonic Rangefinder 
void read_sensor() { 
  // Helper function to read pulse sent by device
  // Conversion for PW: 147 uS per Inch
  pW = pulseIn(pwPin, HIGH);
}

bool range(){
  // Helper function to determine if an object is too close
  // Convert to appropriate units
  inches = pW/147;
  cm = inches * 2.54;
  meters = cm/100;
  
  // Need threshold value to warrant a flag raised
  const int tooClose = 0; 
  if(meters > tooClose){
    return 0;
  }
  else{
    return 1;
  }}
  
bool ultrasonic(){
  // Code for ultrasonic rangefinder sensor
  // range() is the function that will return a boolean value
  // Returns true if an object is too close. False otherwise. 
  read_sensor();
  range();
}
  
// Vibration
int vibration(){
  // Code for vibration sensor
  // Return true if pushbutton is pressed. False otherwise

  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  // check if the pushbutton is pressed. 
  if (buttonState == HIGH) {
    return 0;
  } else {
    return 1;
  }
}

// Pressure 
int pressLoop(){
  // Code for pressure function.
  // Return true if pressure is too high. False otherwise (Note that this might not always mean there isn't a problem, there could be an error
  // retrieving a measurement, so it may be beneficial to have that as a print statement as well)
  
  char status;
  double T,P,p0,a;

  // You must first get a temperature measurement to perform a pressure reading.
  // Start a temperature measurement:
  // If request is successful, the number of ms to wait is returned.
  // If request is unsuccessful, 0 is returned.

  status = pressure.startTemperature();
  if (status != 0)
  {
    // Wait for the measurement to complete:
    delay(status);

    // Retrieve the completed temperature measurement:
    // Note that the measurement is stored in the variable T.
    // Function returns 1 if successful, 0 if failure.

    status = pressure.getTemperature(T);
    if (status != 0)
    {
      // Print out the measurement (Not Needed for our case- just to test)
      // Serial.print("temperature: ");
      // Serial.print(T,2);
      
      // Start a pressure measurement:
      // The parameter is the oversampling setting, from 0 to 3 (highest res, longest wait).
      // If request is successful, the number of ms to wait is returned.
      // If request is unsuccessful, 0 is returned.
      status = pressure.startPressure(3);
      if (status != 0)
      {
        // Wait for the measurement to complete:
        delay(status);

        // Retrieve the completed pressure measurement:
        // Note that the measurement is stored in the variable P.
        // Note also that the function requires the previous temperature measurement (T).
        // (If temperature is stable, you can do one temperature measurement for a number of pressure measurements.)
        // Function returns 1 if successful, 0 if failure.

        status = pressure.getPressure(P,T);
        if (status != 0)
        {
          // The pressure sensor returns abolute pressure, which varies with altitude.
          // Parameters: P = absolute pressure in mb, ALTITUDE = current altitude in m.
          // Result: p0 = sea-level compensated pressure in mb

          p0 = pressure.sealevel(P,ALTITUDE); 
          // Need threshold value to warrant a flag raised
          const int tooMuchPressure = 0;
          if(p0 > tooMuchPressure){
            return 0;
          }
          else{
            return 2; 
          }
          
        }
        else return 1; // error retrieving pressure measurement
      }
      else return 1; // error starting pressure measurement
    }
    else return 1; // error retrieving temperature measurement
  }
  else return 1; // error starting temperature measurement
}


void loop() {
  // See comments above for what the numbers and position means
  String alert = "";
  String text = alert + inductive() + ultrasonic() + vibration() + pressLoop();

    // For Transmitter
    if (radio.available()) {
    radio.write(&text, sizeof(text));
  }
  delay(500); // Delay reading by 5 seconds
}


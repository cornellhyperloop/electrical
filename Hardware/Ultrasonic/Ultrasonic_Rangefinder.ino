/*
This code helps with distance detection using a MaxSonar ultrasonic rangefinder
A library is available at: https://github.com/Diaoul/arduino-Maxbotix
This code's original author belongs to Bruce Allen

Added: LED Lights to blink if sensor detects an object that is too close

Updated: February 27, 2021
*/

// This code will use the PulseWidth (PW) to detect range

// Use digital pin 7 to read PW from the device. Pin number does not change in this code
const int pwPin = 7;

// Input Output Variables
const int proximityInput = 2;
const int LED = 13;

// Store calculated value
long pW, inches, cm, meters; 
// Sensor Variable
int sensorState;


void setup() {
  // Creates serial connection to send results back to PC Console 
  Serial.begin(9600);
  pinMode(pwPin, INPUT);
  
  // Sets up pins as Input and Output
  pinMode(proximityInput, INPUT_PULLUP);
  pinMode(LED, OUTPUT); 
}

void read_sensor() { 
  // Read pulse sent by device
  // Conversion for PW: 147 uS per Inch
  pW = pulseIn(pwPin, HIGH);

  inches = pW/147;
  cm = inches * 2.54;
  meters = cm/100;
  
  Serial.print("Distance from object is: ");
  Serial.print(meters);
}

void lights(){
  // Reads the value as either high or low 
  sensorState = digitalRead(proximityInput);
  // sensorState == LOW means there is a detectable object within sensor's proximity
  if(sensorState == LOW){
    // Turn the LED on for two seconds then turns it off
    digitalWrite(LED, HIGH);
    delay(2000);                  
    digitalWrite(LED, LOW);
  }
}


  
void loop() { 
  read_sensor();
  lights();
  delay(500); // Delay reading by 500 milliseconds
}


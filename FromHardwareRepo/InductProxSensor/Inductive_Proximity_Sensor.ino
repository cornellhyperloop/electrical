/*
Code for Inductive Proximity Sensor
Goal is to have the LED blink when the sensor detects something 

October 26, 2020
*/

// Input Output
const int proximityInput = 2;
const int LED = 13;

// Sensor Variable
int sensorState;

void setup() {
  // Sets up pins as Input and Output
  pinMode(proximityInput, INPUT_PULLUP);
  pinMode(LED, OUTPUT); 
}

void loop() {
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

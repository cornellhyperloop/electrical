#include <Wire.h>
#include <SparkFun_VL6180X.h>

#define VL6180X_ADDRESS 0x29

VL6180xIdentification identification;
VL6180x sensor(VL6180X_ADDRESS);

void setup() {

  Serial.begin(115200); //Start Serial at 115200bps
  Wire.begin(); //Start I2C library
  delay(100); // delay .1s

  sensor.getIdentification(&identification); // Retrieve manufacture info from device memory
//  printIdentification(&identification); // Helper function to print all the Module information

    if(sensor.VL6180xInit() != 0){
    Serial.println("FAILED TO INITALIZE"); //Initialize device and check for errors
  }; 

  sensor.VL6180xDefautSettings(); //Load default settings to get started.

  pinMode(2, INPUT_PULLUP);  
  
  delay(1000); // delay 1s
}

void loop() {
//  Serial.println("Distance measured (mm) = ");
//  Serial.println( sensor.getDistance() ); 
  if(sensor.getDistance() < 20){
    Serial.println(digitalRead(2));
  }
  else{
    Serial.println(sensor.getDistance());
  }
  delay(50);  
}

/*
Receiver code 
Date: November 1, 2020
*/

#include <RH_ASK.h>
#include <SPI.h> // Not actualy used but needed to compile

RH_ASK driver;

// Constants for detecting when the temperature is too high or the pod is too close
// Numbers at the current moment are arbitrary, input when we have more information
const int maxTemp = 100;

void setup()
{
    Serial.begin(9600);  // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}

void loop()
{
    uint8_t buf[12];
    uint8_t buflen = sizeof(buf);
    if (driver.recv(buf, &buflen)) // Non-blocking
    {
      int i;
      
      // Stores the message sent by the transmitter
      String msg = (char*)buf;
      //Create a character array to store the message
      char command[12]; 
      //convert the message from a string to your character array
      msg.toCharArray(command, 12); 
      //Take the first and second characters of the array
      //and covert them into their equivilent intiger value
      int n1 = command[0] - '0';    // Assume this stores temperature 
      int n2 = command[1] -'0';     // Assume this stores distance
      if(n1 > maxTemp){
        Serial.println("1"); // Temperature is too high 
      }
      if(n2 == 1){
        Serial.println("2"); // There is something too close to the pod 
      }
    delay(1000);
    }
}
#include <RH_ASK.h>
#include <SPI.h>

RH_ASK driver;

const int RELAY_PIN = 3;  // the Arduino pin, which connects to the IN pin of relay

void setup() {
    pinMode(RELAY_PIN, OUTPUT);
    Serial.begin(9600);  // Debugging only
    if (!driver.init())
        Serial.println("init failed");
}

// the loop function runs over and over again forever
void loop() {
    uint8_t buf[12];
    uint8_t buflen = sizeof(buf);
    if (driver.recv(buf, &buflen)) // Non-blocking
    {
        if ((char*)buf == "Problem") // disable the sensor if there's a problem
        {
            digitalWrite(RELAY_PIN, HIGH);
            delay(500);
        } 
        else 
        {
            digitalWrite(RELAY_PIN, LOW);
            delay(500);
        }
    }
}


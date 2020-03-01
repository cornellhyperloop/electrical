
#include <Wire.h>
#include <SparkFun_MS5803_I2C.h>

//uses https://github.com/sparkfun/SparkFun_MS5803-14BA_Breakout_Arduino_Library

MS5803 sensor(ADDRESS_HIGH);

double pressure_abs, double pressure_bar;

//returns 1 if pressure below threshold
//returns 0 otherwise
void checkPressure() {
    Serial.begin(9600);
    sensor.reset();
    sensor.begin();
    //read pressure in mbar
    pressure_abs = sensor.getPressure(ADC_4096);
    pressure_bar = pressure_abs / 1000.0;
    if (pressure_bar > 6.49){
      return 0;
    }
    return 1;
}

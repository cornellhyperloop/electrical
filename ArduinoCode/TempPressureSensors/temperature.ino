#include <tsd305.h>

//uses https://github.com/TEConnectivity/TSD305_Arduino_Library

//returns 0 if exceeded safe operating range
//returns positive difference in temperature if closer to high operating limit
//returns negative difference in temperature if closer to low operating limit
int checkTemp() {
  tsd305 m_tsd305;
  tsd305_status status;
  float temperature;
  float object_temperature;

  status = m_tsd305.read_temperature_and_object_temperature(
      &temperature, &object_temperature);

  if (temperature > 60 || temperature < -10){
    return 0;
  }
  int fromHigh = (60 - temperature);
  int fromLow = (-10 - temperature);

  if (fromHigh > (-1 * fromLow)){
    return fromHigh;
  }
  else{
    return fromLow;
  }
}

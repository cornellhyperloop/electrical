int sensorIn = 2;
int valOut = 4;
int sensorVal;

void setup(){
  //configure pin2 as an input and enable the internal pull-up resistor
  pinMode(sensorIn, INPUT_PULLUP);
  pinMode(valOut, OUTPUT);
}

void loop(){

  sensorVal = digitalRead(sensorIn);
  // The Logic is inverted a low on pin 2 means a sinking switch is activated
  // and a high on pin 2 means the switch is unactivated and pulled up by the internal resistor
  // this is not a problem since the controller can interpret the data any way we tell it to

  if (sensorVal == HIGH) {
    digitalWrite(valOut, HIGH);
 }
  else { //sensorVal = LOW
    digitalWrite(valOut, LOW);
 }
}

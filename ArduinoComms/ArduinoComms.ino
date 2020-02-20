int valIn = 52;
int sensorVal;

void setup() {
  // put your setup code here, to run once:
  pinMode(valIn, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    sensorVal = digitalRead(valIn);
  // The Logic is inverted a low on pin 2 means a sinking switch is activated
  // and a high on pin 2 means the switch is unactivated and pulled up by the internal resistor
  // this is not a problem since the controller can interpret the data any way we tell it to

  if (sensorVal == HIGH) {
    Serial.println("TOO CLOSE");
 }
  else { //sensorVal = LOW
    Serial.println("SAFE DISTANCE");
 }
}


#define SENSOR_PIN   A0

int sensor_value;

void setup() {
  
  Serial.begin(9600);
  
}

void loop() {
  
  sensor_value = analogRead(SENSOR_PIN);
  
  Serial.print(sensor_value);
  
  if(sensor_value < 200) {
    Serial.print("ooooooooooooooooooooooooooooo");
  } else {
    Serial.print("|||||||||||||||||||||||||||||");
  }
  
  Serial.println(' ');

}

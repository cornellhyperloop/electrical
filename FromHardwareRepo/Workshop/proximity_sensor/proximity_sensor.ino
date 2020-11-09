
#define SENSOR_PIN   A0

int sensor_value;
int i = 0;

void setup() {
  
  Serial.begin(9600);
  
}

void loop() {
  
  sensor_value = analogRead(SENSOR_PIN);
  
  Serial.print(sensor_value);
  
  while( i < sensor_value/10) {
    Serial.print("_");
    i++;
  }
  
  Serial.println(' ');

  i = 0;

  delay(50);

}

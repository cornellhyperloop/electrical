void setup() {
  Serial.begin(9600);
  Serial2.begin(9600);
}

void loop() {
  Serial.println(Serial2.read());
}

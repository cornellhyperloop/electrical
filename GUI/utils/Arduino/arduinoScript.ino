void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  double accx= 11.5;
  double accy= 9.6;
  double accz= 7.7;
  double gyro= 4.5;
  double mag= 7.8;
  int pressure= 180;
  int temp=56;
  int proximity= 2;
  int distance= 150;

  Serial.println("\"IMU\":{ \"accelerometer\": ["+String(accx)+", "+String(accy)+", "+String(accz)+"],\"gyroscope\": " +String(gyro)+ ",\"magnetometer\": "+String(mag)+ "},\"Pressure\":{\"pressure\": "+String(pressure)+ "},\"Temperature\":{\"temperature\": "+String(temp)+ "},\"Inductive Proximity\":{\"proximity\": "+String(proximity)+ "},\"Long-range sensor\":{\"distance\": "+String(distance)+ "}");
}

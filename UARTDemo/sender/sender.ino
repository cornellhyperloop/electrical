int i= 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(i>10){ i= 0;}
  Serial.write(i);
  i++;
}


int inputPin = 20;

void setup() {
  Serial.begin(9600);
  
  pinMode(inputPin, INPUT);
}

void loop() {
  int buttonState = digitalRead(inputPin);

  if (buttonState == LOW) {
    Serial.println("Button Pressed!");
  }

  delay(1000);
}

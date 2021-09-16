#include <math.h>
#define BTN_PIN 2

int pinOut = 10;
int lastBtnState;
int currentBtnState;
int state = HIGH;

void setup() {
  
  Serial.begin(9600);
  // initialize relay kinda sorta maybe???
  pinMode(pinOut, OUTPUT);

  // initialize digital pin BTN_PIN as an input.
  pinMode(BTN_PIN, INPUT);
  
}

void loop() {

  Serial.print(lastBtnState);
  Serial.print(", ");
  Serial.println(state);
  
  lastBtnState    = currentBtnState;      // save the last state
  currentBtnState = digitalRead(BTN_PIN); // read new state

  if (lastBtnState == LOW && currentBtnState == HIGH) {
    state = !state;
    digitalWrite(pinOut, state);
  }
  
}

// Code used for Thermistors

//Function that takes the pin number as an input and returns T 
float readTemp(int thermistorPin) {
  Vo = analogRead(thermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  return T;
}


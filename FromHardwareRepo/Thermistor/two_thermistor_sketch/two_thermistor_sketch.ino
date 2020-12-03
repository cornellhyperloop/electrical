int thermistorPin[] = {A0, A1}; //analog input pins
int thermistorNum = sizeof(thermistorPin)/sizeof(int);
int Vo;
float R1 = 10000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

void setup() {
  Serial.begin(9600);
}

//Function that takes the pin number as an input and returns T 
float readTemp(int thermistorPin) {
  Vo = analogRead(thermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  return T;
}


// minT and maxT for each thermistor, A0, A1, A2
float minT[3] = {100000, 100000, 100000};
float maxT[3] = {-1, -1, -1};
// Sum of T, to print mean at end
float sumT[3] = {0, 0, 0};
int numTrials = 10;

void loop() {
  for (int i = 0; i < numTrials; i ++ ){
    T = readTemp(0);
    Tc = T - 273.15;
    Tf = (Tc * 9.0)/ 5.0 + 32.0;
    sumT[0] = sumT[0] + Tf;
    if ( T < minT[0] ) minT[0] = Tf;
    if ( T > maxT[0]) maxT[0] = Tf;
    Serial.print("Temperature A0: "); 
    Serial.print(Tf);
    Serial.print(" F0; ");
    Serial.print(Tc);
    Serial.print(" C0       ");   //change from println to print and add a large space between them!!

    T = readTemp(1);
    Tc = T - 273.15;
    Tf = (Tc * 9.0)/ 5.0 + 32.0; 
    sumT[1] = sumT[1] + Tf;
    if ( T < minT[1] ) minT[1] = Tf;
    if ( T > maxT[1]) maxT[1] = Tf;
    Serial.print("Temperature A1: "); 
    Serial.print(Tf);
    Serial.print(" F1; ");
    Serial.print(Tc);
    Serial.println(" C1");  
  
    delay(500);
  }
  
  float maxTherm = maxT[0]; 
  int maxThermNum = 0;
  for (int i = 0; i < thermistorNum; i ++){
    if ( maxT[i] >= maxTherm ){
      maxTherm = maxT[i];
      maxThermNum = i;
    }
  }
  
  float minTherm = minT[0]; 
  int minThermNum = 0;
  for (int i = 0; i < thermistorNum; i ++){
    if ( minT[i] <= minTherm ){
      minTherm = minT[i];
      minThermNum = i;
    }
  }
  Serial.print("Max: ");
  Serial.print(maxTherm);
  Serial.print(" occured in thermistor at pin A");
  Serial.println(maxThermNum);
  Serial.print("Min: ");
  Serial.print(minTherm);
  Serial.print(" occured in thermistor at pin A");
  Serial.println(minThermNum);
  Serial.print("Avg A0: ");
  Serial.println(sumT[0]/numTrials);
  Serial.print("Avg A1: ");
  Serial.println(sumT[1]/numTrials);
  
}

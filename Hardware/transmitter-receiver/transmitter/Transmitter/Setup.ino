void setup()
{
  // Sets up pins as Input and Output
  pinMode(proximityInput, INPUT_PULLUP);
  pinMode(LED, OUTPUT); 
  
  Serial.begin(9600);	  // Debugging only
  if (!driver.init())
    Serial.println("init failed");
}
void loop()
{
    // Reads temp and senses distance; Sends Message
    T = readTemp(0);
    Tc = T - 273.15;
    Tf = (Tc * 9.0)/ 5.0 + 32.0;
    
    sensorState = digitalRead(proximityInput);
    // sensorState == LOW means there is a detectable object within sensor's proximity
    if(sensorState == LOW){
        dist = 1;
      }
    else{
        dist = 0; 
    }
    // 0 means nothing was detected; 1 means there was a detectable object within sensor's proximity
    // Sends message
    dtostrf(Tf, 6, 2, temp);
    dtostrf(dist, 1, 0, distance);
    driver.send((uint8_t *)temp, strlen(temp));
    driver.send((uint8_t *)distance, strlen(distance));
    driver.waitPacketSent();
    delay(1000);
}


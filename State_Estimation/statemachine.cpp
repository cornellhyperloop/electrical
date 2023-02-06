#include <stdio.h>

enum states
{
  Verification,
  PreAcceleration,
  Acceleration,
  Cruise,
  Emergency,
  Deceleration,
  Crawl,
  Stop,
  PodOff,
};

int main()
{
  states curr = Verification;
  states prev = Verification;
  while (1)
  {
    switch (curr)
    {
    case Verification:
    {
      // Task 1: Turn on all sensors and motor(if necessary)
      /* Task 2: Make a verifySensors function to check they're all on,
                  and ensure readings are in a reasonable range.
      **/
      curr = verifySensors();
      prev = Verification;
    };
    case PreAcceleration:
    {
      curr = openBrakes();
      prev = PreAcceleration;
    };
    case Acceleration:
    {
      curr = accelerate();
      prev = Acceleration;
    };
    case Cruise:
    {
      curr = cruise();
      prev = Cruise;
    };
    case Deceleration:
    {
      curr = decelerate();
      prev = Deceleration;
    };
    case Crawl:
    {
      curr = accelerate(); // accelerate with slower speed
      prev = Crawl;
    };
    case Emergency:
    {
      curr = emergency();
      prev = Emergency;
    };
    case Stop:
    {
      curr = stop();
    };
    case PodOff:
    {
      break;
    }
    }
  }
}

states verifySensors()
{
  // If sensors function correctly, go to PreAcceleration, otherwise go to Stop
  // TODO: Implement and return correct state
  return NULL;
}

states openBrakes()
{
  // Go to Emergency if does not work, otherwise go to Acceleration
  // Add manual interrupt to go into Emergency state
  // Check if there is a sensor/mechanism to get feedback on the Brake states, i.e opened/closed.
  // TODO: Implement and return correct state
  return NULL;
}

states accelerate()
{
  // Go to Emergency if does not work, otherwise go to Cruise or Deceleration
  // Add a while loop to stay in this case till it reaches the required velocity
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  return NULL;
}

states cruise()
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Maintain the desired velocity while constantly reading form the sensor
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  return NULL;
}
states decelerate()
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Add a while loop to stay in this case till it needs to start to slow down
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  closeBrakes();
  return NULL;
}

states stop()
{
  // Go to Crawl if does not work, otherwise go to PodOff
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  if (checkDistance())
  {
    return PodOff;
  }
  else
  {
    return Crawl;
  }
  return NULL;
}

states emergency()
{
  // Close brakes rapidly and stop any propulsion
  decelerate();
  closeBrakes();
  return NULL;
}

void closeBrakes()
{
  // TODO: Implement
  return;
}

void turnOff()
{
  // TODO: Implement
  return;
}

bool checkDistance()
{
  // TODO: Implement
  return false;
}

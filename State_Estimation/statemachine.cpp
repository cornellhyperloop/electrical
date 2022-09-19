#include <stdio.h>
#include <stdlib.h>

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
const double minSensor1 = 1.0;
const double maxSensor1 = 1.0;
const double minSensor2 = 1.0;
const double maxSensor2 = 1.0;
const double desiredVelocity = 1.0;

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

states verifySensors(double sensor1, double sensor2)
{
  // TODO: Add more sensor parameters as needed with average values,
  // create functionality for average data value
  // double sensor1, sensor2 are average values of sensors over x amount of time
  // If sensors function correctly, go to PreAcceleration, otherwise go to Stop
  // TODO: Implement and return correct state

  if (sensor1 < minSensor1 || sensor1 > maxSensor1)
    return Stop;
  if (sensor2 < minSensor2 || sensor2 > maxSensor2)
    return Stop;
  return PreAcceleration;
}

states openBrakes()
{
  // Go to Emergency if does not work, otherwise go to Acceleration
  // Add manual interrupt to go into Emergency state
  // Check if there is a sensor/mechanism to get feedback on the Brake states, i.e opened/closed.
  // TODO: Implement and return correct state
  return NULL;
}

states accelerate(double sensor1)
{
  // Go to Emergency if does not work, otherwise go to Cruise or Deceleration
  // Add a while loop to stay in this case till it reaches the required velocity
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  if (sensor1 > desiredVelocity)
  {
    return Cruise;
  }
  else
  {
    return NULL;
  }
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
  if (checkDistance(1, 5))
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

bool checkDistance(double totalDist, double travelDist, const float epsilon = 1E-5f)
{
  // TODO: Calibrate epsilon value after confirming with the mechanical team
  // Check if the pod has reached the total distance
  return (abs(totalDist - travelDist) <= epsilon);
}

#include <stdio.h>
#include <stdlib.h>
#include <constants.h>
#include <helperFunctions.h>

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
      //  Update function call for verifySensors() with  appropriate parameters
      curr = verifySensors(stubValue, stubValue);
      prev = Verification;
    };
    case PreAcceleration:
    {
      curr = openBrakes();
      prev = PreAcceleration;
    };
    case Acceleration:
    {
      curr = accelerate(stubValue);
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
      curr = accelerate(stubValue); // accelerate with slower speed
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
  return Acceleration;
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
    return Emergency;
  }
}

states cruise()
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Maintain the desired velocity while constantly reading form the sensor
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  return Deceleration;
}
states decelerate()
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Add a while loop to stay in this case till it needs to start to slow down
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  closeBrakes();
  return Deceleration;
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
  return Emergency;
}

states emergency()
{
  // Close brakes rapidly and stop any propulsion
  decelerate();
  closeBrakes();
  return Stop;
}

void closeBrakes()
{
  // TODO: Implement closeBrakeMain in helperFunctions.h
  bool brakeClosed = closeBrakeMain();
  // Use bool brakeClosed to verify if the sensor implementation works correctly
}

void turnOff()
{
  // TODO: Implement killPower in helperFunctions.h
  killPower();
}

bool checkDistance(double totalDist, double travelDist, const float epsilon = 1E-5f)
{
  // TODO: Calibrate epsilon value after confirming with the mechanical team
  // Check if the pod has reached the total distance
  return (abs(totalDist - travelDist) <= epsilon);
}

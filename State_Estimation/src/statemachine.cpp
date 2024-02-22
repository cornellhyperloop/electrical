#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "constants.hpp"
#include "helperFunctions.hpp"


states verifySensors(double accelerometer[], double thermistor, double lidar_distance[], double ultrasonic) {
  // TODO: Add more sensor parameters as needed with average values,
  // create functionality for average data value
  // double sensor1, sensor2 are average values of sensors over x amount of time
  // If sensors function correctly, go to PreAcceleration, otherwise go to Stop
  // TODO: Implement and return correct state
  // Accelerometer - 9 output values
  // Thermistor - 1 output value
  // Lidar - 2 output values
  // Ultrasonic - 1 output value

  // Accelerometer
  // std::this_thread::sleep_for(std::chrono::milliseconds(1000));
  for (int i = 0; i < 9; i++) {
    // printf("%f\n", accelerometer[i]);
    if (accelerometer[i] < accelerometerMin[i] || accelerometer[i] > accelerometerMax[i]) {
      return Stop; 
    }
  }

  // Thermistor
  // printf("%f\n", thermistor);
  if (thermistor < thermistorMin || thermistor > thermistorMax)
    return Stop;

  // Lidar for Distance
  for (int i = 0; i < 2; i++)
  {
    // printf("%f\n", lidar_distance[i]);
    if (lidar_distance[i] < lidar_distanceMin[i] || lidar_distance[i] > lidar_distanceMax[i])
      return Stop;
  }

  // Ultrasonic
  // printf("%f\n", ultrasonic);
  if (ultrasonic < ultrasonicMin || ultrasonic > ultrasonicMax)
    return Stop;
  // printf("It has successfully passed\n");
  return PreAcceleration;
}

bool checkDistance(double totalDist, double travelDist, const float epsilon = 1E-5f)
{
  // TODO: Calibrate epsilon value after confirming with the mechanical team
  // Check if the pod has reached the total distance
  //return 0; //delete later
  return (abs(totalDist - travelDist) <= epsilon);
}

states openBrakes()
{
  // Go to Emergency if does not work, otherwise go to Acceleration
  // Add manual interrupt to go into Emergency state
  // Check if there is a sensor/mechanism to get feedback on the Brake states, i.e opened/closed.
  // TODO: Implement and return correct state

  // if (!writeData((char *)"Open", 4)) {
  //   printf("Error: Couldn't write data succesfully");
  // }

  double relay_status = 0.0; // assuming 0 for open, 1 for close
  // ReadData(); // read relay status from arduino

  if (relay_status == 1)
  {
    return Emergency;
  }
  return Acceleration;

}

void closeBrakes()
{
  // TODO: Implement closeBrakeMain in helperFunctions.h
  // bool brakeClosed = closeBrakeMain(); // Commented for now since it's causing causing compilation errors due to function not being defined
  // Use bool brakeClosed to verify if the sensor implementation works correctly

  // TODO: Test functionality of writing to Serial
  // if (!writeData((char *)"Close", 5)) {
  //   printf("Error: Couldn't write data succesfully");
  // }

  // TODO: extract data of relay
  // serial.ReadData();
  double relay_status = 0.0; // assuming 0 for open, 1 for close
  if (relay_status == 1)
  {
    return;
  }
  return;

  // return Emergency;
}

states accelerate(double sensorVelocity, double traveledDist)
{
  // Go to Emergency if does not work, otherwise go to Cruise or Deceleration
  // Add a while loop to stay in this case till it reaches the required velocity
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  if (checkDistance(traveledDist, totalDist - decelRange))
  {
    return Deceleration;
  }
  else
  {
    if (sensorVelocity < desiredVelocity)
    {
      return Acceleration;
    }
    else
    {
      return Cruise;
    }
  }
  return Emergency;
}

states cruise(double sensorVelocity, double traveledDist)
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Maintain the desired velocity while constantly reading form the sensor
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  // logic is taken care off in acceleration!
  return accelerate(sensorVelocity, traveledDist);
}

states decelerate(double traveledDist)
{
  // Go to Emergency if does not work, otherwise go to Deceleration
  // Add a while loop to stay in this case till it needs to start to slow down
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  closeBrakes();
  if (checkDistance(traveledDist, totalDist))
  {
    return Stop;
  }
  else
  {
    return Deceleration;
  }
  return Emergency;
}

states stop(double traveledDist)
{
  // Go to Crawl if does not work, otherwise go to PodOff
  // Add manual interrupt to go into Emergency state
  // TODO: Implement and return correct state
  if (checkDistance(traveledDist, totalDist))
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
  decelerate(0.0);
  closeBrakes();
  return Stop;
}

void turnOff()
{
  // TODO: Implement killPower in helperFunctions.h
  // killPower(); // Commented out for now since it's causing compilation errors due to function not being defined
}

// int main()
// {
//   states curr = Verification;
//   states prev = Verification;
//   // traveledDist = Serial Read for LIDAR to get Traveled Distance
//   double traveledDist = 0.0;

//   while (1)
//   {
//     switch (curr)
//     {
//     case Verification:
//     {
//       // Task 1: Turn on all sensors and motor(if necessary)
//       /* Task 2: Make a verifySensors function to check they're all on,
//                   and ensure readings are in a reasonable range.
//       **/
//      double t1[1] = {1.0};
//      double t3[1] = {1.0};
//       //  Update function call for verifySensors() with  appropriate parameters
//       curr = verifySensors(t1, 0.0, t3, 0.0); // CHANGE
//       // curr = verifySensors(std::get<0>(readData()), stubValue);
//       prev = Verification;
//     };
//     case PreAcceleration:
//     {
//       curr = openBrakes();
//       prev = PreAcceleration;
//     };
//     case Acceleration:
//     {
//       curr = accelerate(lidar_distanceMax[0], traveledDist);
//       prev = Acceleration;
//     };
//     case Cruise:
//     {
//       curr = cruise(lidar_distanceMax[0], traveledDist);
//       prev = Cruise;
//     };
//     case Deceleration:
//     {
//       curr = decelerate(traveledDist);
//       prev = Deceleration;
//     };
//     case Crawl:
//     {
//       curr = accelerate(lidar_distanceMax[0], traveledDist); // accelerate with slower speed
//       prev = Crawl;
//     };
//     case Emergency:
//     {
//       curr = emergency();
//       prev = Emergency;
//     };
//     case Stop:
//     {
//       curr = stop(traveledDist);
//     };
//     case PodOff:
//     {
//       break;
//     }
//     }
//   }
//   return 0;
// }
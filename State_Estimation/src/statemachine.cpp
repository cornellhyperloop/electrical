#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "stateMachineFuncs.cpp"
// TODO: Fix FSM logic

// int main()
// {
//   states curr = Verification;
//   states prev = Verification;
//   // traveledDist = Serial Read for LIDAR to get Traveled Distance
//   double traveledDist = 0.0;

//   while (1)
//   {
  // make sure to check for emergency input
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
//       curr = openBrakes(1);
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
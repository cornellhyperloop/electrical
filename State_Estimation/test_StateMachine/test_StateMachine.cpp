#include <stdio.h>
#include <stdlib.h>
#include "../src/statemachine.cpp"
#include <gtest/gtest.h>

/**
 * Navigate to test file
 * Test Commands: 
 * -cmake -S . -B build
 * -cmake --build build
 * -cd build && ctest
*/
// 1. Test if the correct states are being entered from the relevant states
// 2. Test possible wrong ways of getting to those states and seeing if we can break our code
//      e.g. Having different sensors fail in Verification and see if all correctly cause transition to Stop
// 3. Test all possible paths in the FSM
// 4. Create some mock trajectories with different outcomes/states visited, see if behavior is correct
// TODO: Write test cases covering all possibilities in the FSM
// TODO: Using Google Test to write test cases

// Test Plan:

// void test1()
// {
//   // TODO: Write test case. Test if the current state == desired state
// }

//checkDistance
TEST(CheckDistance, BasicAssertions){
  double total_distance = 10.0; //actual distance traveled
  double traveled_distance = 10.0; //according to our sensors
  double failed_traveled_distance = 9.0;
  const float epsilon = 0.1; //low number 

  EXPECT_EQ(checkDistance(total_distance, traveled_distance, epsilon), true); //Pass
  EXPECT_EQ(checkDistance(total_distance, failed_traveled_distance, epsilon), false); // Fail
}

//verify state
TEST(VerifyTest, BasicAssertions){ 
  double accelerometerFAIL[9] = {-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0};
  double accelerometerPASS[9] = {1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0};
  double thermistorFAIL = -1.0;
  double thermistorPASS = 3.0;
  double lidar_distanceFAIL[2] = {-1.0, -1.0};
  double lidar_distancePASS[2] = {2.0, 2.0};
  double ultrasonicFAIL = -1.0;
  double ultrasonicPASS = 2.0;
  EXPECT_EQ(verifySensors(accelerometerFAIL, thermistorPASS, lidar_distancePASS, ultrasonicPASS), Stop); // accelerometer misses threshold
  EXPECT_EQ(verifySensors(accelerometerPASS, thermistorFAIL, lidar_distancePASS, ultrasonicPASS), Stop); // thermister sensor misses threshold
  EXPECT_EQ(verifySensors(accelerometerPASS, thermistorPASS, lidar_distanceFAIL, ultrasonicPASS), Stop); // lidar sensor misses threshold
  EXPECT_EQ(verifySensors(accelerometerPASS, thermistorPASS, lidar_distancePASS, ultrasonicFAIL), Stop); // ultrasonic sensor misses threshold
  EXPECT_EQ(verifySensors(accelerometerFAIL, thermistorFAIL, lidar_distanceFAIL, ultrasonicFAIL), Stop); // all sesnors miss threshold
  EXPECT_EQ(verifySensors(accelerometerPASS, thermistorPASS, lidar_distancePASS, ultrasonicPASS), PreAcceleration); // all sensors meet threshold
}

// pre-acceleration state
// test with opoenBrakes
// no inputs, read directly form aruduino to work, maybe write a testing verison of this function
TEST(PreAccelerationTest, BasicAssertions){
  int close = 1;
  int open = 0;

  EXPECT_EQ(openBrakes(0), Acceleration);
  EXPECT_EQ(openBrakes(1), Emergency);
}

//acceleration state
  //states accelerate(double sensorVelocity, double traveledDist)
//how do we test manual interrupt?
/*
are the confluence test cases up to date or statemachine up to date?
the code says it returns deceleration if its close to finish line, but
that's not a case on confluence. we added another case below for this.
This is a test case for Cruise, but not acceleration, though. 
*/
TEST(AccelerationTest, BasicAssertions){
  double sensorVelocityunder = 5.0;
  double sensorVelocityover = 15.0;
  double sensorVelocitygood = 10.0;
  double sensorVelocitybad = -1.0;
  double traveledDist = 30.0;
  double traveledDistEnd = 80.0;
  EXPECT_EQ(accelerate(sensorVelocityunder, traveledDist), Acceleration); // under desired vel
  EXPECT_EQ(accelerate(sensorVelocityover, traveledDist), Cruise); // over desired vel
  EXPECT_EQ(accelerate(sensorVelocitygood, traveledDist), Cruise); // desired
  EXPECT_EQ(accelerate(sensorVelocitygood, traveledDistEnd), Deceleration); // near end of track
  EXPECT_EQ(accelerate(sensorVelocitybad, traveledDist), Emergency); // sensor malfunction

  //manual interrupts can't be tested from here
  // EXPECT_EQ(accelerate(sensorVelocitybad, traveledDist), Emergency); // manual interrupt
}

//cruise state
  //states cruise(double sensorVelocity, double traveledDist)
TEST(CruiseTest, BasicAssertions){
  double sensorVel = 10.0;
  // double sensorVelNo = 0.0;
  double traveledDist = 50.0;
  double traveledDistEnd = 80.0;
  // TODO: Fix when we figure out automatic emergency transitions
  // EXPECT_EQ(cruise(sensorVelNo, traveledDist), Emergency); // undesired velocity
  EXPECT_EQ(cruise(sensorVel, traveledDist), Cruise); // desired velocity
  // EXPECT_EQ(cruise(sensorVel, traveledDist), Emergency); // manual interrupt
  EXPECT_EQ(cruise(sensorVel, traveledDistEnd), Deceleration); // near end of track
}

//deaceleration state
  //states decelerate(double traveledDist)
TEST(DecelerationTest, BasicAssertions){
  //what is the purpose of epsilon at this point then?
  // epsilon for calibration
  // will continuously calling closeBrakes cause any problem on the arduino?

  double traveledDistEnd = 0.00;
  double traveledDistMid = 50.0;
  EXPECT_EQ(decelerate(traveledDistEnd), Stop);
  EXPECT_EQ(decelerate(traveledDistMid), Deceleration);

  // manual interrrupt 
  // EXPECT_EQ(decelerate(traveledDistMid), Emergency);
}

//emergency state
  //states emergency()
//simply returns Stop after executing 
TEST(EmergencyTest, BasicAssertions){
  EXPECT_EQ(emergency(), Stop);
}

//stop state
  //states stop(double traveledDist)
TEST(StopTest, BasicAssertions){
  double traveledDistEnd = 0.0;
  double traveledDistMid = 0.0;
  EXPECT_EQ(stop(traveledDistMid), Crawl); //used to be crawl, need to change bc Crawl DNE
  EXPECT_EQ(stop(traveledDistEnd), PodOff);
}

//unsure about what crawl is supposed to do. review statemachine.cpp file!

//how to start google test in terminal:
  // cmake -S . -B build
  // cmake --build build

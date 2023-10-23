#include <stdio.h>
#include <stdlib.h>
// #include "src/constants.hpp"
#include "../src/statemachine.cpp"
#include "../src/statemachine.hpp"
#include "../src/helperFunctions.hpp"
#include <gtest/gtest.h>

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

// void main()
// {
//   printf("Running tests: \n");
//   printf("Running test1: \n");
//   test1();
//   // test_n();
//   printf("All tests are completed!");
// }

int Factorial(int n)
{
  if (n == 0)
  {
    return 1;
  }
  return n * Factorial(n - 1);
}

// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions)
{
  // Expect two strings not to be equal.
  EXPECT_STRNE("hello", "world");
  // Expect equality.
  EXPECT_EQ(7 * 6, 42);
  // Expect equality.
  EXPECT_EQ(Factorial(5), 120);
}

//checkDistance
TEST(CheckDistance, BasicAssertions){
  EXPECT_EQ(checkDistance(double distance, double desiredDistance, const float epsilon), Acceleration); //Pass
  EXPECT_EQ(checkDistance(double distance, double desiredDistance, const float epsilon), Deceleration); // Fail
}

//verify state
TEST(VerifyTest, BasicAssertions){ 
  EXPECT_EQ(verifySensors(double accelerometerFAIL, double thermistorPASS, lidar_distancePASS, ultrasonicPASS), Stop); //1fail
  EXPECT_EQ(verifySensors(double accelerometer, double thermistorFAIL, lidar_distancePASS, ultrasonicPASS), Stop); //1fail
  EXPECT_EQ(verifySensors(double accelerometerFAIL, double thermistorFAIL, lidar_distanceFAIL, ultrasonicFAIL), Stop); // all fail
  EXPECT_EQ(verifySensors(double accelerometerPASS, double thermistorPASS, lidar_distancePASS, ultrasonicPASS), PreAcceleration); // all pass
}

//pre-acceleration state
//test with opoenBrakes
//no inputs, read directly form aruduino to work, maybe write a testing verison of this function
TEST(PreAccelerationTest, BasicAssertions){
  EXPECT_EQ(openBrakes(), Acceleration);
  EXPECT_EQ(openBrakes(), Emergency);
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
  EXPECT_EQ(accelerate(double sensorVelocity-underDesired, double traveledDist), Acceleration); // under desired vel
  EXPECT_EQ(accelerate(double sensorVelocity-overDesired, double treveledDist), Cruise); // over desired vel
  EXPECT_EQ(accelerate(double sensorVelocity, double treveledDist), Cruise); // desired
  EXPECT_EQ(accelerate(double sensorVelocity, double treveledDist-closeToEnd), Deceleration); // near end of track
  EXPECT_EQ(accelerate(double sensorVelocity, double treveledDist), Emergency); // sensor malfunction
  EXPECT_EQ(accelerate(double sensorVelocity, double treveledDist), Emergency); // manual interrupt
}

//cruise state
  //states cruise(double sensorVelocity, double traveledDist)
TEST(CruiseTest, BasicAssertions){
  EXPECT_EQ(cruise(double sensorVelocity-notDesired, double traveledDist), Emergency); // undesired velocity
  EXPECT_EQ(cruise(double sensorVelocity, double traveledDist), Cruise); // desired velocity
  EXPECT_EQ(cruise(double sensorVelocity, double traveledDist), Emergency); // manual interrupt
  EXPECT_EQ(cruise(double sensorVelocity, double treveledDist-closeToEnd), Deceleration); // near end of track
}

//deaceleration state
  //states decelerate(double traveledDist)
TEST(DecelerationTest, BasicAssertions){
  EXPECT_EQ(decelerate(double traveledDist-Reached), Stop) ;
  EXPECT_EQ(decelerate(double traveledDist-Not-Reached), Emergency);
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
  EXPECT_EQ(stop(traveledDist-Not-Reached), Crawl); //used to be crawl, need to change bc Crawl DNE
  EXPECT_EQ(stop(traveledDist-Reached), PodOff);
}

//unsure about what crawl is supposed to do. review statemachine.cpp file!

//how to start google test in terminal:
  // cmake -S . -B build
  // cmake --build build

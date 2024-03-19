#include <stdio.h>
#include <stdlib.h>
#include "../src/statemachine.cpp"
#include <gtest/gtest.h>
using ::testing::Return;

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

//how to start google test in terminal:
  // cmake -S . -B build
  // cmake --build build

TEST(MockSerialTests, BasicAssertions) {
  MockSensors serial;
  EXPECT_CALL(serial, ReadData(0,0))
    .Times(3)
    .WillRepeat(Return());
    //figure out the format of the output from the arduino that is being read from serial
    //use that as our guide for what this mock serial object outputs


}
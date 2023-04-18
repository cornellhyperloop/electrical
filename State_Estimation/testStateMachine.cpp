#include <stdio.h>
#include <stdlib.h>
// #include "src/constants.hpp"
#include "src/statemachine.cpp"
#include "src/statemachine.hpp"
#include "src/helperFunctions.hpp"
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

// cmake -S . -B build
// cmake --build build
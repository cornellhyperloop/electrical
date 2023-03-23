#include <stdio.h>
#include <stdlib.h>
#include <src/constants.hpp>
#include <src/statemachine.cpp>
#include <src/statemachine.hpp>
#include <src/helperFunctions.hpp>

// 1. Test if the correct states are being entered from the relevant states
// 2. Test possible wrong ways of getting to those states and seeing if we can break our code
//      e.g. Having different sensors fail in Verification and see if all correctly cause transition to Stop
// 3. Test all possible paths in the FSM
// 4. Create some mock trajectories with different outcomes/states visited, see if behavior is correct
// TODO: Write test cases covering all possibilities in the FSM
// TODO: Using Google Test to write test cases

void test1()
{
  // TODO: Write test case. Test if the current state == desired state
}

void main()
{
  printf("Running tests: \n");
  printf("Running test1: \n");
  test1();
  // test_n();
  printf("All tests are completed!");
}
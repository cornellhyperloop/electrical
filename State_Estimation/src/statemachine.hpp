// header file for statemachine.cpp

#include "stdio.h"
#include "stdlib.h"
#include "constants.hpp"

// Runs the state machine for the pod
int main();

// Verifies that the sensors are working properly
states verifySensors(double sensor1, double sensor2);

// Opens the brakes
states openBrakes();

// Accelerates the pod
states accelerate(double desiredVelocity);

// Cruises the pod
states cruise();

// Decelerates the pod
states decelerate();

// Emergency state
states emergency();

// Stops the pod
states stop();

// Close the brakes
void closeBrakes();

// Turns off the pod
void turnOff();

// Checks if the pod is in the desired range
bool checkDistance(double distance, double desiredDistance, const float epsilon);
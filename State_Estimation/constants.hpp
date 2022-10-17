#include <stdio.h>
#include <stdlib.h>

const double minSensor1 = 1.0;
const double maxSensor1 = 1.0;
const double minSensor2 = 1.0;
const double maxSensor2 = 1.0;
const double desiredVelocity = 1.0;
const double stubValue = 24.24;

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
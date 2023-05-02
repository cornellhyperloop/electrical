#include <stdio.h>
#include <stdlib.h>

// sensor min/max values
const double accelerometerMin[9] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
const double accelerometerMax[9] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

const double thermistorMin = 0.0;
const double thermistorMax = 0.0;

const double lidar_distanceMin[2] = {0.0, 0.0};
const double lidar_distanceMax[2] = {0.0, 0.0};

const double ultrasonicMin = 0.0;
const double ultrasonicMax = 0.0;

const double desiredVelocity = 1.0;
const double stubValue = 0.5;

const double totalDist = 0.0;
const double decelRange = 0.0;

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
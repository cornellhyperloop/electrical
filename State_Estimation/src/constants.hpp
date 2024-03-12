#include <stdio.h>
#include <stdlib.h>

// sensor min/max values
const double accelerometerMin[9] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
const double accelerometerMax[9] = {100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0};

const double thermistorMin = 0.0;
const double thermistorMax = 100.0;

const double lidar_distanceMin[2] = {0.0, 0.0};
const double lidar_distanceMax[2] = {100.0, 100.0};
// Min is 11.8 inches = 29.972 cm

const double ultrasonicMin = 0.0;
const double ultrasonicMax = 100.0;

const double desiredVelocity = 10.0;
const double stubValue = 0.5;

const double totalDist = 100.0;
const double decelRange = 20.0;
const double stopRange = 5.0;

const double sensorStopEps = 1E-3f;

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

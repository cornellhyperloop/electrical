#include <stdio.h>

double maxPressure;
double minSideDistance;
double maxEndDistance;
double maxAccel;
double avgAccel;
int overheatingTemp = 35;
int exOverheatingTemp = 55;

int main()
{

    enum
    {
        s0,
        s1,
        s2,
        s3,
        s4,
        s5,
        s6,
        s7,
        s8,
        s9,
        s10
    } currState;
    currState = s0;

    while (1)
    {

        // Read sensor values
        double thermistor;
        double pressure;
        double shortDistance;
        double longDistance;
        double accel;

        switch (currState)
        {
            // Condition subject to change. Placeholder for now.
            if (thermistor > overheatingTemp)
            {
                currState = s9;
            }
        case s0: // Pod ON
            currState = s1;
            break;
        case s1: // Verification
        case s2: // Overheating
            // Activate cooling mechanism
            if (thermistor < overheatingTemp)
            {
                currState = s4;
            }
            break;
        case s3: // Pre-Acceleration
            // Brake locks opened
            currState = s4;
            break;
        case s4: // Acceleration
                 // Start motors
        case s5: // Cruise
            if (thermistor > overheatingTemp)
            {
                currState = s2;
            }
            else if (thermistor > exOverheatingTemp || pressure >= maxPressure)
            {
                currState = s9;
            }
            else if (shortDistance < minSideDistance)
            {
                // Adjust orientation of pod
            }
            else if (longDistance >= maxEndDistance)
            {
                currState = s7;
            }
            else if (accel >= maxAccel)
            {
                currState = s6;
            }
            break;
        case s6: // Deceleration
            if (accel < avgAccel)
            {
                currState = s5;
            }
            break;
        case s7: // Crawl
            if (accel == 0)
            {
                currState = s8;
            }
            break;
        case s8:  // Stop
        case s9:  // Emergency
        case s10: // Pod OFF
        }
    }

    return 0;
}

#include <sstdio.h>

int main() {
    enum {s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11} currState;

    currState = s0;

    while (1) {
        switch (currState) {
            if (anything bad) {
                currState = s10;
            }
            case s0: // Pod ON
                currState = s1;
                break;
            case s1: // Verification
            case s2: // Overheating
                if (temperature > 35) {
                    currState = s3;
                }
                break;
            case s3: // Extreme Overheating
                currState = s10;
                break;
            case s4: // Pre-Acceleration
                // Brake locks opened
                currState = s5;
            case s5: // Acceleration
                // Start motors
            case s6: // Cruise
            case s7: // Deceleration
            case s8: // Crawl
            case s9: // Stop
            case s10: // Emergency
            case s11: // Pod OFF
        }
    }

    return 0;
}
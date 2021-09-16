#include <stdio.h>

#define MAX 38000000.0 //The maximum value the raw data can have
#define MIN 0.0 //The minimum value the raw data can have

/*
 * Returns: [sensor_valid(raw_data)] is 1 if [raw_data] is
 * a value between MIN and MAX inclusive; 0 otherwise.
 * Requires: raw_value must be a double
 */
int sensor_valid(double raw_value)
{
    if (MIN <= raw_value && raw_value <= MAX) {
        return 1;
    } else {
        return 0;
    }
}

int main () {
    double input;
    printf("Enter a float: ");
    scanf("%lf",&input);
    printf("The function outputted a %d", sensor_valid(input));
    printf("\n");
}

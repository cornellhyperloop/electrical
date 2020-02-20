#include <stdio.h>

/* Length of track: 4150 feet (1.25 km)*/
/* input should be in feet*/
int checkVal(float input){
	if(input < 0 || input > 4150){
		return 0;
	}
	return 1;
}

int main()
{
    printf("%d", checkVal(4500));

    return 0;
}
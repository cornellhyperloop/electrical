/*
 ============================================================================
 Name        : shortDistance.c
 Author      : Siddarth Sankaran
 Version     :
 ============================================================================
 */
/* The digital short range sensor is being used to account for distance from 0-20 mm. */ 
/* The analog short range sensor is being used to account for distance from 20 - 30 mm. */
/* The accepted values are 1.0, (since the digital sensor returns 1.0 when something is detected within 0-20 mm range) */
/* and any values between 20.0 and 30.0 inclusive since these range of values are actually returned by the analong sensor */
/* whenever something is detected within that mm range.



#include <stdio.h>
#include <stdlib.h>

int validVal(float f)
{

	if( f==1.0 || (f>=20.0 && f<=30.0))    
		return 1;

	return 0;
}

int main(void) {

	int check = validVal(1.0);
	printf("%d", check);
	check = validVal(0)
	printf("%d", check);
	check = validVal(-3.0)
	printf("%d", check);
	check = validVal(15.0)
	printf("%d", check);
	check = validVal(24.5)
	printf("%d", check);
	check = validVal(32)
	printf("%d", check);
	return check;
}

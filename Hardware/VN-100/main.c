#include <stdio.h>

/* Include files needed to use VnEzAsyncData. */
#include "vn/sensors/ezasyncdata.h"

int processErrorReceived(char* errorMessage, VnError errorCode);

bool extremeMotion(float y1, float p1, float r1, float y2, float p2, float r2) {
	//detect if ypr changes at least by these values
	//roll is low to also detect rumbling
	return abs(y1 - y2) >= 60 || abs(p1 - p2) >= 45 || abs(r1 - r2) >= 20;
}

int main(void)
{
	VnEzAsyncData ez;
	VnError error = E_NONE;
	size_t i = 0;
	char oldYPR[50];
	char newYPR[50];
	FILE * file;
	VnCompositeData oldData;
	VnCompositeData currData;
	bool problem = false;
	char acc[50];
	char quat[50];
	char vel[50];
	char mag[50];
	char angRate[50];
	char temp[100];
	char pressure[100];

	const char SENSOR_PORT[] = "COM5"; 	/* Windows format for physical and virtual (USB) serial port. */
	const uint32_t SENSOR_BAUDRATE = 115200;

	/* We call the initialize and connect method to connect with our VectorNav sensor. */
	if ((error = VnEzAsyncData_initializeAndConnect(&ez, SENSOR_PORT, SENSOR_BAUDRATE)) != E_NONE)
		return processErrorReceived("Error connecting to sensor.", error);

	while(1)
	{
		oldData = VnEzAsyncData_currentData(&ez);
		VnThread_sleepMs(500);
		currData = VnEzAsyncData_currentData(&ez);

		//Determine if theres extreme movement or rumbling
		problem = extremeMotion(oldData.yawPitchRoll.c[0], oldData.yawPitchRoll.c[1], oldData.yawPitchRoll.c[2],
			currData.yawPitchRoll.c[0], currData.yawPitchRoll.c[1], currData.yawPitchRoll.c[2]);

		// Track the other data
		str_vec3f(vel, currData.velocityEstimatedBody);
		str_vec3f(acc, currData.acceleration);
		str_vec3f(mag, currData.magnetic);
		str_vec3f(angRate, currData.angularRate);
		str_vec4f(quat, currData.quaternion);

		gcvt(currData.temperature, 6, temp);
		gcvt(currData.pressure, 6, pressure);

		if (problem) {
			printf("Problem: %s\n", "Problem!");
		}
		else {
			printf("Problem: %s\n", "No problem!");
		}

		file = fopen("test.txt", "a");
		fprintf(file, vel);
		fprintf(file, " ");
		fprintf(file, acc);
		fprintf(file, " ");
		fprintf(file, mag);
		fprintf(file, " ");
		fprintf(file, angRate);
		fprintf(file, " ");
		fprintf(file, quat);
		fprintf(file, " ");
		fprintf(file, temp);
		fprintf(file, " ");
		fprintf(file, pressure);
		fprintf(file, "\n");
		fclose(file);
	}

	/* Now disconnect from the sensor since we are finished. */
	if ((error = VnEzAsyncData_disconnectAndUninitialize(&ez)) != E_NONE)
		return processErrorReceived("Error disconnecting from sensor.", error);

	return 0;
}

int processErrorReceived(char* errorMessage, VnError errorCode)
{
	char errorCodeStr[100];
	strFromVnError(errorCodeStr, errorCode);
	printf("%s\nERROR: %s\n", errorMessage, errorCodeStr);
	return -1;
}

#include <unistd.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");
	FILE *serialPort;
	system( "MODE COM4: BAUD=9600 PARITY=n DATA=8 STOP=1" );
  serialPort = fopen("COM4:", "r" );
	sensor_info_t msg;
<<<<<<< Updated upstream

	// struct sensor_info_t
	// {
	//   float imu_acceleration_x;
	//   float imu_acceleration_y;
	//   float imu_acceleration_z;
	//   float imu_gyroscope;
	//   float imu_magnetometer;
	//   float pressure;
	//   float temperature;
	//   float proximity;
	//   float distance;
	// }

	msg.imu_acceleration_x = 1.0;
	msg.imu_acceleration_y = 2.0;
	msg.imu_acceleration_z = 3.0;
	msg.imu_gyroscope = 4.0;
	msg.imu_magnetometer = 5.0;
	msg.pressure = 6.0;
	msg.temperature = 7.0; //TODO: Get value from arduino
	msg.proximity = 8.0;
	msg.distance = 9.0;
=======
	msg.velocity = 10;
	msg.fiducial_detector_value = 20;
	msg.thermistor_value = serialPort;
>>>>>>> Stashed changes

	while (1) {
		sensor_info_t_publish(zcm, "SENSOR_INFO", &msg);
		usleep(1000000); /* sleep for a second */
	}

	zcm_destroy(zcm);
	return 0;
}

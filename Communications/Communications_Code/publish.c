#include <unistd.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");

	sensor_info_t msg;

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

	while (1) {
		sensor_info_t_publish(zcm, "SENSOR_INFO", &msg);
		usleep(1000000); /* sleep for a second */
	}

	zcm_destroy(zcm);
	return 0;
}

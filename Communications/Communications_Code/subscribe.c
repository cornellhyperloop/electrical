#include <stdio.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>


void writeJson(char* fileName, const sensor_info_t *msg, size_t size);
// void writeJson(char *fileName, int *arr, size_t size);

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

void callback_handler(const zcm_recv_buf_t *rbuf, const char *channel, const sensor_info_t *msg, void *usr)
{
	printf("Received a message on channel '%s'\n", channel);
	printf("msg->imu_acceleration_x = '%f'\n", msg->imu_acceleration_x);
	printf("msg->imu_acceleration_y = '%f'\n", msg->imu_acceleration_y);
	printf("msg->imu_acceleration_z = '%f'\n", msg->imu_acceleration_z);
	printf("msg->imu_gyroscope = '%f'\n", msg->imu_gyroscope);
	printf("msg->imu_magnetometer = '%f'\n", msg->imu_magnetometer);
	printf("msg->pressure = '%f'\n", msg->pressure);
	printf("msg->temperature = '%f'\n", msg->temperature);
	printf("msg->proximity = '%f'\n", msg->proximity);
	printf("msg->distance = '%f'\n", msg->distance);
	printf("\n");
	writeJson("../../GUI/example.json", msg, 5);
}

// void writeJson(char *fileName, int *arr, size_t size)
// {
void writeJson(char* fileName, const sensor_info_t *msg, size_t size) {
	size_t i;
	FILE *fp = fopen(fileName, "w+"); /* open file for writing */

	if (!fp)
	{ /* validate file is open, or throw error */
		fprintf(stderr, "writeJson() error: file open failed '%s'.\n",
						fileName);
		return;
	}
	// TODO : Add other sensor fields later
	// {
	// 	"Temperature": {
	// 		"temperature": 100
	// 	}
	// }

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

	// 	{
	//   "IMU":{
	//     "accelerometer": [11.5, 9.6, 7.7],
	//     "gyroscope": 4.5,
	//     "magnetometer": 7.8
	//   },
	//   "Pressure":{
	//     "pressure": 180
	//   },
	//   "Temperature":{
	//     "temperature": 56
	//   },
	//   "Inductive Proximity":{
	//     "proximity": 2
	//   },
	//   "Long-range sensor":{
	//     "distance": 150
	//   }
	// }

	// IMU
	fprintf(fp, "{ \n\"IMU\" : \n{");
	// Accelerometer
	fprintf(fp, "\"accelerometer\" : [");
	// Print value
	fprintf(fp, "%f, %f, %f", msg->imu_acceleration_x, msg->imu_acceleration_y, msg->imu_acceleration_z);
	// fprintf(fp, "%f, %f, %f", 1, 2, 3);
	fprintf(fp, "],\n");

			// Gyroscope
			fprintf(fp, "\"gyroscope\" : ");
	// Print value
	fprintf(fp, "%f", msg->imu_gyroscope);
	// fprintf(fp, "%f", 1);
	fprintf(fp, ",\n");

			// Magnetometer
			fprintf(fp, "\"magnetometer\" : ");
			// Print value
			fprintf(fp, "%f", msg->imu_magnetometer);
			// fprintf(fp, "%f", 1);
			fprintf(fp, "\n");
					fprintf(fp, "},\n");

	// Pressure
	fprintf(fp, "\"Pressure\" : \n{");
	fprintf(fp, "\"pressure\" : ");
	// Print value
	fprintf(fp, "%f", msg->pressure);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, "\n },");

			// Temperature
			fprintf(fp, "\"Temperature\" : \n{");
	fprintf(fp, "\"temperature1\" : ");
	// Print value
	fprintf(fp, "%f,\n", msg->temperature);
	fprintf(fp, "\"temperature2\" : ");
	// Print value
	fprintf(fp, "%f", msg->temperature);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, "\n },");

			// Inductive Proximity
			fprintf(fp, "\"Inductive Proximity\" : \n{");
	fprintf(fp, "\"proximity\" : ");
	// Print value
	fprintf(fp, "%f", msg->proximity);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, "\n },");

			// Long-range sensor
			fprintf(fp, "\"Long-range sensor\" : \n{");
	fprintf(fp, "\"proximity\" : ");
	// Print value
	fprintf(fp, "%f", msg->distance);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, "\n }");

			fprintf(fp, "}\n");

	fclose(fp);
}

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");
	sensor_info_t_subscribe(zcm, "SENSOR_INFO", callback_handler, NULL);

	zcm_run(zcm);

	zcm_destroy(zcm);
	// int array[] = {1, 2, 3, 4, 5, 6, 7, 8};
	// writeJson("../../GUI/example.json", array, 5);
	return 0;
}

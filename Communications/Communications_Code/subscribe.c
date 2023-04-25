#include <stdio.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>

void writeJson(char *fileName, const sensor_info_t *msg, size_t size);
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
	printf("msg->accelerometer_x = '%f'\n", msg->accelerometer_x);
	printf("msg->accelerometer_y = '%f'\n", msg->accelerometer_y);
	printf("msg->accelerometer_z = '%f'\n", msg->accelerometer_x);
	printf("msg->gyroscope_x = '%f'\n", msg->gyroscope_x);
	printf("msg->gyroscope_y = '%f'\n", msg->gyroscope_y);
	printf("msg->gyroscope_z = '%f'\n", msg->gyroscope_z);
	printf("msg->pressure = '%f'\n", msg->pressure);
	printf("msg->temperature1 = '%f'\n", msg->temperature1);
	printf("msg->temperature2 = '%f'\n", msg->temperature2);
	printf("msg->short_dist = '%f'\n", msg->short_dist);
	printf("msg->long_dist = '%f'\n", msg->long_dist);
	printf("\n");
	writeJson("../../GUI/example.json", msg, 5);
}

// void writeJson(char *fileName, int *arr, size_t size)
// {
void writeJson(char *fileName, const sensor_info_t *msg, size_t size)
{
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

	// {
	// "Temperature":{
	//   "temperature1" : 56,
	//   "temp2" : 56
	// 	},
	//  "Accelerometer" : [11.5, 9.6, 7.7],
	//  "Gyroscope" : [4.5, 5.7, 2.3],
	//  "Pressure" : 180,
	//  "Short-range distance" : 12,
	//  "Long-range distance" : 150
	// }

	// Temperature
	fprintf(fp, "{ \n\"Temperature\" : \n{\n");
	fprintf(fp, "\"temperature1\" : ");
	// Print value
	fprintf(fp, "%f,\n", msg->temperature1);
	fprintf(fp, "\"temperature2\" : ");
	// Print value
	fprintf(fp, "%f", msg->temperature2);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, "\n },\n");

	// Accelerometer
	fprintf(fp, "\"accelerometer\" : [");
	// Print value
	fprintf(fp, "%f, %f, %f", msg->accelerometer_x, msg->accelerometer_y, msg->accelerometer_z);
	// fprintf(fp, "%f, %f, %f", 1, 2, 3);
	fprintf(fp, "],\n");

	// Gyroscope
	fprintf(fp, "\"gyroscope\" : [");
	// Print value
	fprintf(fp, "%f, %f, %f", msg->gyroscope_x, msg->gyroscope_y, msg->gyroscope_z);
	// fprintf(fp, "%f", 1);
	fprintf(fp, "],\n");

	// Pressure
	fprintf(fp, "\"Pressure\" : ");
	// Print value
	fprintf(fp, "%f", msg->pressure);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, ",\n");

	// Long-range sensor
	fprintf(fp, "\"Long-range sensor\" : ");
	// Print value
	fprintf(fp, "%f", msg->long_dist);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, ",\n");

	// Short-range sensor
	fprintf(fp, "\"Short-range sensor\" : ");
	// Print value
	fprintf(fp, "%f", msg->short_dist);
	// fprintf(fp, "%f", 5.6);
	fprintf(fp, "\n");
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

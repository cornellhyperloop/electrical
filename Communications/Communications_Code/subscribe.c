#include <stdio.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>


void writeJson(char* fileName, const sensor_info_t *msg, size_t size);

void callback_handler(const zcm_recv_buf_t *rbuf, const char *channel, const sensor_info_t *msg, void *usr)
{
	printf("Received a message on channel '%s'\n", channel);
	printf("msg->velocity = '%f'\n", msg->velocity);
	printf("msg->fiducial_detector_value = '%f'\n", msg->fiducial_detector_value);
	printf("msg->thermistor_value = '%f'\n", msg->thermistor_value);
	printf("\n");

	writeJson("test.json", msg, 5);
}

// void writeJson(char* fileName, int* arr, size_t size) {
void writeJson(char* fileName, const sensor_info_t *msg, size_t size) {
	size_t i;
    FILE *fp = fopen (fileName, "w+"); /* open file for writing */

    if (!fp) {  /* validate file is open, or throw error */
        fprintf (stderr, "writeJson() error: file open failed '%s'.\n", 
                fileName);
        return;
    }
	// TODO : Add other sensor fields later
  // {
	// 	"Temperature": {
	// 		"temperature": 100
	// 	}
	// }

		fprintf (fp, "{ \n\"Temperature\" : \n{");
		fprintf (fp, "\"temperature\" : ");
		//Print value
		fprintf (fp, "%f", msg->thermistor_value);

		fprintf (fp, "}\n");
		fprintf(fp, "}\n");

    fclose (fp);
}

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");
	sensor_info_t_subscribe(zcm, "SENSOR_INFO", callback_handler, NULL);

	zcm_run(zcm);

	zcm_destroy(zcm);
	return 0;
}

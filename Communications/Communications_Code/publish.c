#include <unistd.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("udpm://234.255.76.67:7667?ttl=1");

	sensor_info_t msg;
	msg.velocity = 10;
	msg.fiducial_detector_value = 20;
	msg.thermistor_value = 30;

	while (1) {
		sensor_info_t_publish(zcm, "SENSOR_INFO", &msg);
		usleep(1000000); /* sleep for a second */
	}

	zcm_destroy(zcm);
	return 0;
}

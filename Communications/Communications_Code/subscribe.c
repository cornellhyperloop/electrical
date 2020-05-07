#include <stdio.h>
#include <zcm/zcm.h>
#include <sensor_info_t.h>

void callback_handler(const zcm_recv_buf_t *rbuf, const char *channel, const sensor_info_t *msg, void *usr)
{
	printf("Received a message on channel '%s'\n", channel);
	printf("msg->velocity = '%f'\n", msg->velocity);
	printf("msg->fiducial_detector_value = '%f'\n", msg->fiducial_detector_value);
	printf("msg->thermistor_value = '%f'\n", msg->thermistor_value);
	printf("\n");
}

int main(int argc, char *argv[])
{
	zcm_t *zcm = zcm_create("ipc");
	sensor_info_t_subscribe(zcm, "SENSOR_INFO", callback_handler, NULL);

	zcm_run(zcm);

	zcm_destroy(zcm);
	return 0;
}

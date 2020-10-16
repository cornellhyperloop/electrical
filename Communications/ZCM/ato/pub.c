#include <zcm/zcm.h>
#include "otp_t.h"
#include <unistd.h>

int main (int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");

	ato_t msg;
	msg.pressure = 0.0;
	msg.temperature = 0.0;
	msg.close = false;
	msg.velocity = 0.0;
	msg.roll = 0.0;
	msg.pitch = 0.0;
	msg.yaw = 0.0;
	msg.acceleration = 0.0;
	msg.position = 0.0;
	msg.angular_rate = 0.0;

	while (1) {
		ato_t_publish(zcm, "ATO_TEST_CHANNEL", &msg);
		usleep(1000000);
	}

	zcm_destroy(zcm);
	return 0;
}


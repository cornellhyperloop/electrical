#include <zcm/zcm.h>
#include "otp_t.h"
#include <unistd.h>

int main (int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");

	otp_t msg;
	msg.state = 1;
	msg.roll = 0.0;
	msg.yaw = 0.0;
	msg.acceleration = 0.0;
	msg.position = 0.0;
	msg.angular_rate = 0.0;

	while (1) {
		otp_t_publish(zcm, "OTP_TEST_CHANNEL", &msg);
		usleep(1000000);
	}

	zcm_destroy(zcm);
	return 0;
}


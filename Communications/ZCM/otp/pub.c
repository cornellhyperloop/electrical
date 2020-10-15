#include <zcm/zcm.h>
#include "otp_t.h"
#include <unistd.h>
#include <stdio.h>

int main (int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");

	otp_t msg;
	msg.state = 1;
	msg.roll = 0.0;
	msg.yaw = 0.0;
	msg.acceleration = 0.0;
	msg.position = 0.0;
	msg.angular_rate = 0.0;

	int set_state = 0;
	while (1) {
		scanf("%d", &set_state);
		msg.state = (int8_t) set_state;

		printf("Sending message to pilot computer with state %d\n", msg.state);
		fflush(stdout);
		otp_t_publish(zcm, "OTP_TEST_CHANNEL", &msg);
	};

	zcm_destroy(zcm);
	return 0;
}


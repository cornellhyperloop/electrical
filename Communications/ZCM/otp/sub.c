#include <zcm/zcm.h>
#include "otp_t.h"
#include <stdio.h>

void handle_packet(const zcm_recv_buf_t *rbut, const char *channel, const otp_t *msg, void *usr) {
	printf("Odroid to Pod message recv'd on channel: %s\n", channel);
	printf("msg->state : %d\n", msg-> state);
}

int main(int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");
	otp_t_subscribe(zcm, "OTP_TEST_CHANNEL", handle_packet, NULL);

	zcm_run(zcm);

	zcm_destroy(zcm);
	return 0;
}

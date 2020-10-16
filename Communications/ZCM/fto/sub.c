#include <zcm/zcm.h>
#include "fto_t.h"
#include <stdio.h>

void handle_packet(const zcm_recv_buf_t *rbut, const char *channel, const fto_t *msg, void *usr) {
	printf("Fiducial to ODROID message recv'd on channel: %s\n", channel);
	printf("msg->distance : %d\n", msg-> distance);
	printf("msg->obstructed : %b\n", msg-> obstructed;
}

int main(int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");
	fto_t_subscribe(zcm, "FTO_TEST_CHANNEL", handle_packet, NULL);

	zcm_run(zcm);

	zcm_destroy(zcm);
	return 0;
}

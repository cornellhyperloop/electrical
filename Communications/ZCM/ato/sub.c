#include <zcm/zcm.h>
#include "ato_t.h"
#include <stdio.h>

void handle_packet(const zcm_recv_buf_t *rbut, const char *channel, const ato_t *msg, void *usr) {
	printf("Analog to ODROID message recv'd on channel: %s\n", channel);
	printf("msg->position : %d\n", msg-> position);
}

int main(int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");
	ato_t_subscribe(zcm, "ATO_TEST_CHANNEL", handle_packet, NULL);

	zcm_run(zcm);

	zcm_destroy(zcm);
	return 0;
}

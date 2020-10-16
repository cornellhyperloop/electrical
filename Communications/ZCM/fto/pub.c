#include <zcm/zcm.h>
#include "fto_t.h"
#include <unistd.h>

int main (int argc, char *argv[]) {
	zcm_t *zcm = zcm_create("ipc");

	fto_t msg;
	msg.distance = 0;
	msg.obstructed = false;

	while (1) {
		fto_t_publish(zcm, "FTO_TEST_CHANNEL", &msg);
		usleep(1000000);
	}

	zcm_destroy(zcm);
	return 0;
}


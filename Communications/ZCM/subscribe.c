#include <stdio.h>
#include <zcm/zcm.h>
#include <msg_t.h>

void callback_handler(const zcm_recv_buf_t *rbuf, const char *channel, const msg_t *msg, void *usr)
{
	    printf("Received a message on channel '%s'\n", channel);
	        printf("msg->str = '%s'\n", msg->str);
		    printf("\n");
}

int main(int argc, char *argv[])
{
	    zcm_t *zcm = zcm_create("ipc");
	        msg_t_subscribe(zcm, "HELLO_WORLD", callback_handler, NULL);

		    zcm_run(zcm);

		        zcm_destroy(zcm);
			    return 0;
}

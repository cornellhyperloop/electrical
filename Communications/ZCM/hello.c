#include <unistd.h>
#include <zcm/zcm.h>
#include <msg_t.h>

int main(int argc, char *argv[])
{
    zcm_t *zcm = zcm_create("ipc");

    msg_t msg;
    msg.str = (char*)"Hello, World!";

    while (1) {
        msg_t_publish(zcm, "HELLO_WORLD", &msg);
        usleep(1000000); /* sleep for a second */
    }

    zcm_destroy(zcm);
    return 0;
}


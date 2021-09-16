#pragma once
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string>

using namespace std;

class Server
{
    public:
        Server();
        ~Server();
        int create_server();
        int send_message(const char *message);
        string receive_message();
};

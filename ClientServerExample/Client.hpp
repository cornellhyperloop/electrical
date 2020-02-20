#pragma once
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string>

using namespace std;

class Client
{
	public:
		Client();
		~Client();
		int create_client();
		int send_message(const char *message);
		string receive_message();
};

#include "Client.hpp"
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <unistd.h>

#define PORT 8321 // This is just a random high port that doesn't conflict with other things
#define HOST "10.147.131.39" // Change this IP address, depending on the device that the server is on

using namespace std;

int clientSocket;
sockaddr_in serverAddr;
char buffer[100]; // This buffer will store any data that is received, so if you want to receive larger amounts of data, you'll have to increase the size of the buffer

int Client::create_client()
{
    memset(buffer, '0', sizeof(buffer));
    // Creating a socket for the Client
    if ((clientSocket = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
		cerr << "ClientSocket not created!" << endl;
        throw "ClientSocket not created!";
        return -1;
    }
    cout << "ClientSocket created successfully!" << endl;
    // Storing information about the address of the server to use to connect the client to the server
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT); // Port that the server has bound to(We will be communicating through this port)
    serverAddr.sin_addr.s_addr = inet_addr(HOST); // IP Address of the server

    // Connecting the client to the server
    if(connect(clientSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0)
    {
		cerr << "Connection failed due to either port or IP problems!" << endl;
        throw "Connection failed due to either port or IP problems!";
        return -1;
    }
    cout << "Connected to server!" << endl;
}

Client::Client()
{
	create_client();
}

Client::~Client()
{
	 
}

// Function that sends a message to the server
int Client::send_message(const char *message)
{
    if (send(clientSocket, message, strlen(message), 0) == -1)
    {
		cerr << "There was an error sending the message!" << endl;
        throw "There was an error sending the message!";
        close(clientSocket);
    }
    else
        cout << "The message being sent is \"" << message << "\"" << endl;
    return 0;
}

// Function that receieves a message from the server
string Client::receive_message()
{
	recv(clientSocket, buffer, 100, 0);
	return buffer;
}

int main()
{
    // Create a Client object
	Client first_client;

    // Wait for user input, which will be sent from the client to the server
	while(1)
	{
        string message;
        cout << "Enter the message that you would like to send to the server: " << endl;
        cin >> message; // There may be problems if you send multiple words at a time, since cin is meant just to read the first word that you send
        first_client.send_message(message.c_str());
	}
	return 0;
}

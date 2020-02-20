#include "Server.hpp"
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <unistd.h>

#define PORT 8321 // This is just a random high port number that isn't used for other things

using namespace std;

int sockfd, client_sockfd;
struct sockaddr_in serverAddr, clientAddr;
char buffer[100]; // Right now the buffer is fairly small in size, but you should change the buffer size if you would like to send and receive information that's larger in size

int Server::create_server()
{
   // Creating a socket for the server
   sockfd = socket(AF_INET, SOCK_STREAM, 0);
   if (sockfd < 0)
   {
	   cerr << "Error creating server socket!" << endl;
       throw "Error creating server socket!";
       return -1;
   }
   cout << "Server socket created successfully!" << endl;
   // Initializing the address of the server to their initial values
   bzero((char *) &serverAddr, sizeof(serverAddr));
   // Storing the values associated with the server address
   serverAddr.sin_family = AF_INET;
   serverAddr.sin_addr.s_addr = INADDR_ANY;
   serverAddr.sin_port = htons(PORT);

   // Binding the server socket to the specified port
   if (bind(sockfd, (struct sockaddr *) &serverAddr, sizeof(serverAddr)) < 0)
   {
	   cerr << "Error when trying to bind to the port!" << endl;
       throw "Error when trying to bind to the port!";
       return -1;
   }
   cout << "Port bound correctly!" << endl;
   listen(sockfd, 1); // Number of clients that the server can accept a connection from -- change if you would like to have server connect to more than one client
   socklen_t clilen = sizeof(clientAddr);
   // Accepting a connection from a client socket
   client_sockfd = accept(sockfd, (struct sockaddr *) &clientAddr, &clilen);
   if (client_sockfd < 0)
   {
	   cerr << "Error when trying to accept a client!" << endl;
       throw "Error when trying to accept a client!";
       return -1;
   }
   cout << "Successfully accepted a client..." << endl;
   return 0;
}

Server::Server()
{
    create_server();
}

Server::~Server()
{
    
}

int Server::send_message(const char *message)
{
    bzero(buffer, 100);
    int message_send = write(client_sockfd, message, strlen(message));
    if (message_send < 0)
    {
		cerr << "Error sending message to client socket!";
        throw "Error sending message to client socket!";
        return -1;
    }
    return 0;
}

string Server::receive_message()
{
    bzero(buffer, 100);
    int message_read = recv(client_sockfd, buffer, 100, 0);
    // Prints out the message that was received
    if (strlen(buffer) != 0)
		cout << "The message received was \"" << buffer << "\"" << endl;
    return (string)buffer;
}

int main()
{
    // Creating a server object
	Server first_server;

    // Polling to check whether the client has sent a message
	while(1)
	{
		first_server.receive_message();
	}
    return 0;
}

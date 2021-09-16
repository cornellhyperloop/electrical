For the Python client-server example:

Run the following command on the server machine:
```shell
python3 server.py <port_number>
```

Run the following command on the client machine:
```shell
python3 client.py <server_ip_address> <server_port_number>
```

The IP address of the server can be found using `ifconfig` or a similar command. Make sure to use a high port number to prevent conflicts with existing processes (ex: `12345`). For those with no networking background, the server and client machine must be on the same network. If they are on different networks, you will need to find the public IP address of the server machine (i.e. the router's IP address) and set up port forwarding on the router.

For the C++ client-server example:

First, you'll have to find the IP address of the server machine(you can use the method detailed above) and change the IP address that's been defined at the top of "Client.cpp" accordingly. After doing so, you can compile the two files. You will need a C++ compiler to do this, so install one if you don't already have one. g++ can be very easily installed via the command line.

Then, assuming you have g++(the steps are very similar using other compilers as well), run the following command on the server machine:
```shell
g++ -o server Server.cpp Server.hpp
```

And run the following command on the client machine:
```shell
g++ -o client Client.cpp Client.hpp
```
Afterwards, make sure you run the server executable first, on the server machine, via:
```shell
./server
```

Lastly, you can run the client executable:
```shell
./client
```

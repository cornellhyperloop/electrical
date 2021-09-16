import sys
import socket

def start_server(port):
    # create server socket
    # this socket does send or receive data; it only establishes connections with clients
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind to port number on any address on machine
    # machines may have multiple ip addresses (ex: Ethernet, WiFi, etc.)
    serversocket.bind(('', port))
    # listen for connections; can set bound for max number of queued connection requests
    serversocket.listen()
    # accept a connection; will block if no connection requests have been received
    # sock is socket to communicate with client, addr is ip address of client
    (sock, addr) = serversocket.accept()
    while True:
        chunk = sock.recv(4096)
        if chunk == b'':
            break
        else:
            print(chunk.decode(), end='')

if __name__ == '__main__':
    start_server(int(sys.argv[1]))
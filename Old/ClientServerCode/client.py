import sys
import socket

def start_client(server_ip, server_port):
    # create client socket; uses ipv4 adresses and the tcp protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    sock.connect((server_ip, server_port))
    # send 1000 messages; tcp ensures that messages are received in order
    for n in range(1000):
        # sock sends bytes so messages need to be encoded
        sock.sendall("msg#: {}\n".format(n).encode())

if __name__ == '__main__':
    # ip address and port number of server are passed in via command line
    start_client(sys.argv[1], int(sys.argv[2]))
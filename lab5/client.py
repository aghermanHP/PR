#!/usr/bin/env python3
import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 10000
Message = "Hello, Server"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    clientSock.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
    response, address = clientSock.recvfrom(1024)
    if response:
        print(response.decode("utf8"))
        break
    else:
        print("error of tretriving data")
        break

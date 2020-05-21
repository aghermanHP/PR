#!/usr/bin/env python3
import socket

UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("File name:", data.strip().decode("utf8"))
        file_name = data.strip().decode("utf8")

    with open(file_name, 'wb') as f:

        data, addr = sock.recvfrom(10024)
        f.write(data)

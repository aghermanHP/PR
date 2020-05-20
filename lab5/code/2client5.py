
import socket

HOST, PORT = "localhost", 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((HOST, PORT))
while True:
    received = sock.recvfrom(1024)
    print("Received: {}".format(received))

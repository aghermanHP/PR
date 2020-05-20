import threading
import socket


def run_server():
    """start udp server"""
    client_adress = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "localhost"
    port = 10000
    sock.bind((host, port))
    while True:
        data, adr = sock.recvfrom(1024)
        client_adress.append(adr)
        for i in client_adress:
            if client_adress[i] == data:
                print(adr)
            else:
                print(len(client_adress), data, client_adress)
if __name__ == '__main__':
    run_server()

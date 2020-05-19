#!/usr/bin/env python3
from threading import Thread
from zlib import compress
import socket

from mss import mss


WIDTH = 1900
HEIGHT = 1000


def retreive_screenshot(conn, addr):
    with mss() as sct:
        # # The region to capture
        # rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}
        mesage = "hello dear client"
        conn.sendto(mesage.encode(), addr)
        # while 'recording':
        #     # Capture the screen
        #     img = sct.grab(rect)
        #     # Tweak the compression level here (0-9)
        #     pixels = compress(img.rgb, 6)
        #
        #     # Send the size of the pixels length
        #     size = len(pixels)
        #     size_len = (size.bit_length() + 7) // 8
        #     conn.send(bytes([size_len]))
        #
        #     # Send the actual pixels length
        #     size_bytes = size.to_bytes(size_len, 'big')
        #     conn.send(size_bytes)
        #
        #     # Send pixels
        #     conn.sendall(pixels)


def main():
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 10000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    try:
        while True:
            conn, addr = sock.recvfrom(1024)
            print('Client connected IP:', addr)
            thread = Thread(target=retreive_screenshot, args=(sock, addr,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
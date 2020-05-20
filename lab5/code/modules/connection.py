import cv2
import numpy as np
import pyautogui
import socket
import sys

# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    HOST, PORT = "localhost", 8888


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(cv2.imshow("screenshot", frame), (HOST, PORT))
    received = sock.recv(1024)

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break
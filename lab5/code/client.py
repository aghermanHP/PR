import socket
import time
import sys
import re
try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    from tkinter import messagebox
except ImportError:
    import tkMessageBox as messagebox
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog

root = tk.Tk()

style = ttk.Style(root)
style.theme_use("clam")
root.title('Text Editor')

root.geometry('500x500')


def call_server(file_name, file):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(file_name, "utf8"), (UDP_IP, UDP_PORT))
    print("Sending %s ..." % file_name)
    if sock.sendto(bytes(file, "utf8"), (UDP_IP, UDP_PORT)):
        time.sleep(0.02)  # Give receiver a bit time to save
    time.sleep(2)
    messagebox.showinfo("Title", "File trannssfered with success")
    time.sleep(20)
    root.destroy()
#UI

def c_open_file_old():
    rep = filedialog.askopenfilenames(
        parent=root,
        initialdir='~/',
        initialfile='testss',
        filetypes=[
            ("All files", "*"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpg")])
    print(rep)
    try:
        with open(rep[1], "r") as f:
            x = (f.read())
            name = rep[1].split("/")
            print("name=", x)
            tk.Label(root, text=x).grid(row=0)
            call_server(name[-1], x)
    except IndexError:
        print("No file selected")


ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')

root.mainloop()
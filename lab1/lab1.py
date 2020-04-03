import socket
import re
import ssl
from threading import Thread


class OpenThruSocket:
    def __init__(self, host, PORT):
        self.host = host
        self.PORT = PORT
        self.dd = ""
        self.links_to_images = []

    def recive_data(self):
        """
        :return:
        data of site
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.PORT))
            if self.PORT == 443:
                sock = ssl.wrap_socket(sock, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                                    ssl_version=ssl.PROTOCOL_SSLv23)
            request_header = 'GET / HTTP/1.0\r\nHOST: {}\r\n\r\n'.format(self.host).encode("utf-8")
            sock.send(request_header)
            self.dd = b''
            while True:
                temp = sock.recv(8048)
                if len(temp) == 0:
                    break
                else:
                    self.dd += temp
            sock.close()
        code_of_page = (self.dd.decode("utf-8"))
        with open('demofile2.txt', "w+") as file:
            file.write(code_of_page)
        with open('demofile2.txt', 'r') as file:

            x = file.readlines()
            for line_in_file in x:
                if self.PORT == 443:
                    timg = re.search('\/wp-content\/(.*?)\.(png|jpg)', line_in_file, re.MULTILINE)
                else:
                    timg = re.search('\/images\/(.*?)\.(png|jpg)', line_in_file)
                if timg is not None:
                    self.links_to_images.append(timg.group(0))
            return self.links_to_images


class DownloadImages(Thread):
    def __init__(self, IMAGESLIST, HOST, PORT):
        Thread.__init__(self)
        self.HOST = HOST
        self.IMAGESLIST = IMAGESLIST
        self.PORT = PORT
        self.array1 = []
        self.array2 = []
        self.array3 = []
        self.array4 = []
    def DivideList(self):
        first_array = []
        second_array = []
        for i in range(len(self.IMAGESLIST)):
            if (i%2==0):
                first_array.append(self.IMAGESLIST[i])
            else:
                second_array.append(self.IMAGESLIST[i])
        for i in range(len(first_array)):
            if (i % 2 == 0):
                self.array1.append(first_array[i])
            else:
                self.array2.append(first_array[i])
        for i in range(len(second_array)):
            if (i % 2 == 0):
                self.array3.append(second_array[i])
            else:
                self.array4.append(second_array[i])

    def download_thru_sockets(self, name, list_of_images):
        all_images = []
        x = 1
        for i in list_of_images[0]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            if self.PORT == 443:
                s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                                    ssl_version=ssl.PROTOCOL_SSLv23)
            request_header = 'GET {} HTTP/1.0\r\nHOST: {}\r\n\r\n'.format(i, self.HOST).encode()
            s.send(request_header)
            images = s.recv(8024)
            s.close()
            image_content = re.findall(b'\r\n\r\n(.*)', images, re.S)
            all_images.append(images)
            if images != b'' and image_content is not None:
                nameOfFile = "image{}{}".format(name, x)
                with open(nameOfFile, 'wb') as file:
                    file.write(image_content[0])
                x += 1

    def test(self):
            self.DivideList()
            t1 = Thread(target=self.download_thru_sockets, args=(1, [self.array1], ))
            t2 = Thread(target=self.download_thru_sockets, args=(2, [self.array2], ))
            t3 = Thread(target=self.download_thru_sockets, args=(3, [self.array3], ))
            t4 = Thread(target=self.download_thru_sockets, args=(4, [self.array4], ))
            t1.start()
            t2.start()
            t3.start()
            t4.start()


host = input("give the host: \n")
port = input("give the port: \n")
list_of_links = OpenThruSocket(host, int(port)).recive_data()
DownloadImages(list_of_links, host, int(port)).test()



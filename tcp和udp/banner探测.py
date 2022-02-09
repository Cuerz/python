# -*- encoding: UTF-8 -*-
from scapy.all import *

def main():
    ip = '192.168.1.108'
    port = 3306
    s = socket.socket()
    s.connect((ip,port))
    s.send('xxx'.encode("utf-8"))
    banner = s.recv(1024)
    s.close()
    print("banner is {}".format(banner))

    pass

if __name__ == '__main__':
    main()
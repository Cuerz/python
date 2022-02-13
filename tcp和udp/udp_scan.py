# -*- encoding: UTF-8 -*-
from scapy.all import *

def main():
    ip = '192.168.1.108'
    ans,uans = sr(IP(dst=ip)/UDP(dport=80))
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is up"))

    pass

if __name__ == '__main__':
    main()
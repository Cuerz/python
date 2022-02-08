# -*- encoding: UTF-8 -*-
from scapy.all import *

def main():
    #输入目标ip
    ans,uans = sr(IP(dst="xx.xx.xx.xx")/ICMP())
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is alive now"))

    pass
if __name__ == '__main__':
    main()
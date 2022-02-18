# -*- encoding: UTF-8 -*-
import time
from scapy.all import *
from random import randint

def main():
   while 1:
       pdst = "%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
       psrc = "192.168.1.200"
       packet = IP(src=psrc,dst=pdst)/ICMP()
       sendp(packet)
       print(packet.summary())

   pass

if __name__ == '__main__':
    main()
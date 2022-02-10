# -*- encoding: UTF-8 -*-
from scapy.all import *
from random import randint
import time

def main():
   ip = '192.168.1.108'
   dport = randint(1,65535)
   packet = IP(dst=ip)/TCP(flags="A",dport=dport)
   response = sr1(packet,timeout=1,verbose=False)
   if response:
       #RST
       if int(response[TCP].flags)==4:
           time.sleep(0.5)
           print(ip+' is up')
   else:
       print(ip+' is down')

   pass
if __name__ == '__main__':
    main()
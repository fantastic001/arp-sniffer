#! /usr/bin/env python
from scapy.all import *

def arp_monitor_callback(pkt):
    if arp in pkt and pkt[arp].op in (1,2): #who-has or is-at
        op = ""
        if pkt[arp].op == 1: 
            op = "who has "
        else:
            op = "is at"
        return op + pkt.sprintf("%arp.hwsrc% %arp.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)

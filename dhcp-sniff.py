
#! /usr/bin/env python
from scapy.all import *

def dhcp_monitor_callback(pkt):
    if DHCP in pkt:
        hostname =  [v[1] for v in pkt[DHCP].options if type(v) == tuple and v[0]  == "hostname"][0]
        ips =  [v[1] for v in pkt[DHCP].options if type(v) == tuple and v[0]  == "requested_addr"]
        ip = ""
        if len(ips) > 0:
            ip = " ".join(ips)
        return "Hostname: %s IP: %s" % (hostname, ip)

sniff(prn=dhcp_monitor_callback, filter="dhcp", store=0)

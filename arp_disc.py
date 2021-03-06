#!/usr/bin/python
"""ARP scan a given network"""
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__email__ = "james.aylesworth@gmail.com"
__status__ = "Production"

if len(sys.argv) != 2:
    print "Usage - ./arp_disc.py [interface]"
    print "Example - ./arp_disc.py eth0"
    print "Example will perform an ARP scan on the local subnet to which eth0 is assigned"
    sys.exit()

interface = str(sys.argv[1])

ip = subprocess.check_output("ip -o addr show | grep inet\\ | grep " +
                             interface + " | cut -d ' ' -f 7", shell=True).strip()

print("\nNetwork found ==> " + ip)

prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + \
    '.' + ip.split('.')[2] + '.'

print("\nScanning ==> " + prefix + "0/24\n")

for addr in range(0, 254):
    answer = sr1(ARP(pdst=prefix + str(addr)), timeout=1, verbose=0)
    if answer == None:
        pass
    else:
        print prefix + str(addr)

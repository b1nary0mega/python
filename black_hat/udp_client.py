#!/usr/bin/env python
'''quick-n-dirty udp server'''
import socket
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

target_host = "127.0.0.1"
target_port = 80

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AAABBBCCC", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print data

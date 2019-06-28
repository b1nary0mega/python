#!/usr/bin/env python
'''quick-n-dirty tcp client'''
import socket
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

'''
NOTES:
1.0.0 - Initial file creation
'''

target_host = "127.0.0.1"
target_port = 9999

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("Hello from a client!")

# receive some data
response = client.recv(4096)

print response

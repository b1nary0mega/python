#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
  print "Usage: vrfy.py <MAIL-SERVER> <USER>"
  sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#create a socket
connect=s.connect((sys.argv[1],25))		#connect to server
banner=s.recv(1024)				#receive the banner
print banner
s.send('VRFY ' + sys.argv[2] + '\r\n')		#VRFY user
result=s.recv(1024)				#store results
print result
s.close()					#close the socket


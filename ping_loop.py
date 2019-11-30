#!/usr/bin/python

import subprocess
from multiprocessing import Pool 

#based on os.cpu_count(), there are 4 cores to work with
num_cores = range(5)

p = Pool()

# BASH REF
# "for ip in $(seq 1 10); do ping -c 1 10.11.1.$ip | grep \"bytes from\" | cut -d\" \" -f4 | cut -d\":\" -f1 & done"
#

pingCMDs = []

for i in range(25):
  IP = "10.11.1." + str(i)
  pingCMDs.append("ping -c1 " + IP + " | grep \"bytes from\" | cut -d\" \" -f4 | cut -d\":\" -f1 &")
  pingCMD = ("ping -c1 " + IP + " | grep \"bytes from\" | cut -d\" \" -f4 | cut -d\":\" -f1 &")
  EX = p.map(pingCMD, num_cores)

print(len(pingCMDs))

#CMDs = p.map(pingCMDs, num_cores)

p.close()
p.join()


/usr/bin/python2

#!/usr/bin/python
'''
file:	file_data-parse_by_week.py
test:	unit_tests/rpc_flow_all.txt

desc: split file contents to output folder, by week,
      calculating how many connections were initiatied 
      from one IP to another

author: Sparc FLOW
source: Investigate Like a Rockstar; pg 62-63

modified: b1nary0mega
changes: refer to github pages
'''

# parse file data out by week
import os
import datetime
import re
import sys

outputDir = "output"
UT_Test_DIR = "unit_tests"
UT_Test_Output = str(UT_Test_DIR)+"/"+str(outputDir)
filePath = "./"+str(UT_Test_DIR)+"/"
fileName = "rpc_flow_all.txt"
fileOutPrefix = "/flow_"

if not os.path.exists(str(UT_Test_Output)):
    os.makedirs(str(UT_Test_Output))

flow_count = {}
current = 1

with open(str(filePath)+"/"+str(fileName), 'r') as infile:
    for line in infile:
        # get and extract date of stream
        date_str = str(line.split(" ")[0].strip())

        # if not a date, pass
        if re.search('[a-zA-Z]', date_str) or date_str == "":
            continue

        date_record = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

        # extract IP address
        ip_src = str(line.split(";")[3].split(":")[0].strip())
        ip_dst = str(line.split(";")[4].split(":")[0].strip())
        key_ip = ip_src + "," + ip_dst

        # get julian week
        week_number = date_record.isocalendar()[1]

        # deal with change in weeks
        if (current != week_number) and len(flow_count.keys()) > 0:
            # write to appropriate week file
            out = open("./"+str(UT_Test_Output)+"/" +
                       fileOutPrefix+str(current)+".csv", "w")
            out.write("Source IP,Destination IP,Connections\n")
            for key, value in flow_count.items():
                out.write(key+","+str(value)+"\n")
            out.close()
            flow_count = {}
            current = week_number

        # if same week, store in a dictionary
        else:
            if key_ip in flow_count.keys():
                flow_count[key_ip] = flow_count[key_ip] + 1
            else:
                flow_count[key_ip] = 1
    print("[+] Done")
infile.close()

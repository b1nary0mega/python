#!/usr/bin/python

# script to keep machine awake via mouse movement and benign key press (shift)
# for added 'sleep protection' I recommend streaming a live youtube channel
# in the foreground; set it to 144p to be bandwidth courteous ;)

import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
numMin = None

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 2
else:
    numMin = int(sys.argv[1])

while (True):
    x = 0
    
    while (x < numMin):
        time.sleep(60)
        x += 1
    
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    
    pyautogui.moveTo(1,1)
    
    # caution: pressing SHIFT too many times close together triggers sticky keys
    for i in range(0,3):
        pyautogui.press("shift")
    
    print("Movement made at {}".format(datetime.now().time()))

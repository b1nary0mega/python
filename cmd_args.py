#!/usr/bin/env python
'''display cmd line args'''
import sys
import os
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

print('Arg Count ' + str(len(sys.argv)))
print('===================')
for x in sys.argv:
    print(x)

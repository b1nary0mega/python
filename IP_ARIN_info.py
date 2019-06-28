#!/usr/bin/env python
"""pull ARIN info for IP to | to other programs"""
import sys
import os
import ipwhois
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

obj = ipwhois.IPWhois(sys.argv[1])
results = obj.lookup_rdap(depth=1)
print(results)


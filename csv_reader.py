#!/usr/bin/env python
'''csv reader'''
import csv
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

with open('CSV_FILENAME', 'r+', newline='') as csv_file
    reader = csv.reader(csv_file)
    for row in reader:
        print(str(row))

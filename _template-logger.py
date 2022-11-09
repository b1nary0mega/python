#!/usr/bin/python3
""" 
NAME: logger.py
AUTH: Jimmi Aylesworth
DATE: Thu 8/3/2022
DESC: This is a basic outline/example for a program with logging
"""

# Imports
import logging
import sys

# Logger - manual @ https://docs.python.org/3/library/logging.html
logging.basicConfig(filename="logger_template.log", format='%(asctime)s - %(levelname)s [Line %(lineno)s] - %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) # debug, info, warning, error & critical

# Methods
def getFiles(fileLocation):
    try:
        logger.info('getFiles called with \"' + fileLocation + '\"')
        print("Ingesting files from --> " + fileLocation)
    except Exception as e:
        logger.error("Exeption occurred", exc_info=True)

    logger.info('getFiles done')
    
    return "...files got..."



# Main
if __name__ == "__main__":
    logger.info('*** program started ***')
    someFiles = getFiles("c:\\temp\\*")
    logger.info('=== program ended ===')
    sys.exit(0)

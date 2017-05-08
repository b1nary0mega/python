#!/usr/bin/env python
""" Program to collect unique websites in given file then output to same directory """
import sys, os, re
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "jarhed323@gmail.com"
__status__ = "Production"

#validate system args
if len(sys.argv) == 2:
	#verify the path and file names before setting any variables
	if os.path.exists(os.path.dirname(sys.argv[1])) & os.path.isdir(os.path.dirname(sys.argv[1])):
		if not os.path.isfile(sys.argv[1]):
			print('File does not appear at given path.')
			exit()
	else:
		print('Given path does is incorrect, or is not a directory.')
		exit()
	#if all verified, set variables for referance later on
	strFileDirectory = os.path.dirname(sys.argv[1])
	strFileBaseName = os.path.basename(sys.argv[1])
	strFileAndLocation = os.path.join(strFileDirectory, strFileBaseName)
else:
	print('Usage: python.exe getWebsites.py [FILE_LOCATION\FILE_NAME]')
	exit()

print('\nReading in: ' + strFileAndLocation + '...')

#open, read, store data, and close
fileObject = open(strFileAndLocation)
strFileData = fileObject.read()
fileObject.close()

print('File size: ' + str(os.path.getsize(sys.argv[1])))
print('\nSearching for websites...')

#search for websites
reWebsiteMatches = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', strFileData)

#put unique websites into list, sort and then output to file
outputWebsiteLIST = []
for x in range(len(reWebsiteMatches)):
	if outputWebsiteLIST.count(reWebsiteMatches[x]) == 0:
		outputWebsiteLIST.append(reWebsiteMatches[x])

outputWebsiteLIST.sort()

print('websites found: ' + str(len(outputWebsiteLIST)))

#open a new file, write out websites and close file
strOutputPath = os.path.join(strFileDirectory, '_websiteOutput.txt')
outputFile = open(strOutputPath, 'w')

for website in outputWebsiteLIST:
	outputFile.write(website + '\n')

outputFile.close()

print('\nwebsites saved to: ' + strOutputPath)
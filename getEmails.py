#!/usr/bin/env python
""" Program to collect unique emails in given file then output to same directory """
import sys, os, re
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
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
	print('Usage: python.exe getEmails.py [FILE_LOCATION\FILE_NAME]')
	exit()

print('\nReading in: ' + strFileAndLocation + '...')

#open, read, store data, and close
fileObject = open(strFileAndLocation)
strFileData = fileObject.read()
fileObject.close()

print('File size: ' + str(os.path.getsize(sys.argv[1])))
print('\nSearching for emails...')

#search for emails
reEmailMatches = re.findall(r'[\w\.-]+@[\w\.-]+', strFileData)

#put unique emails into list, sort and then output to file
outputEmailLIST = []
for x in range(len(reEmailMatches)):
	if outputEmailLIST.count(reEmailMatches[x]) == 0:
		outputEmailLIST.append(reEmailMatches[x])

outputEmailLIST.sort()

print('Emails found: ' + str(len(outputEmailLIST)))

#open a new file, write out emails and close file
strOutputPath = os.path.join(strFileDirectory, '_emailOutput.txt')
outputFile = open(strOutputPath, 'w')

for email in outputEmailLIST:
	outputFile.write(email + '\n')

outputFile.close()

print('\nEmails saved to: ' + strOutputPath)
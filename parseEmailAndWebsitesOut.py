#!/usr/bin/env python
"""Program to collect unique emails & websites in file from KnowBe4"""
import sys
import os
import re
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.1.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Production"


def validateArgs(fileLocation):
    # verify the path and file names before setting any variables
    if os.path.exists(os.path.dirname(sys.argv[1])) & os.path.isdir(os.path.dirname(sys.argv[1])):
        if not os.path.isfile(sys.argv[1]):
            print('File does not appear at given path.')
            return False
        else:
            return True
    else:
        print('Given path does is incorrect, or is not a directory.')
        return False


def getEmails(searchString, sorted):
    print('\nSearching for emails...')
    reEmailMatches = re.findall(r'[\w\.-]+@[\w\.-]+', str(searchString))

    # put unique emails into list, sort and then output to file
    outputEmailLIST = []
    for x in range(len(reEmailMatches)):
        if outputEmailLIST.count(reEmailMatches[x]) == 0:
            outputEmailLIST.append(reEmailMatches[x])

    if sorted:
        outputEmailLIST.sort()

    print('Emails found: ' + str(len(outputEmailLIST)))

    return outputEmailLIST


def getWebsites(searchString, sorted):
    print('\nSearching for websites...')
    reWebsiteMatches = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(searchString))

    # put unique websites into list, sort and then output to file
    outputWebsiteLIST = []
    for x in range(len(reWebsiteMatches)):
        if outputWebsiteLIST.count(reWebsiteMatches[x]) == 0:
            outputWebsiteLIST.append(reWebsiteMatches[x])

    if sorted:
        outputWebsiteLIST.sort()

    print('Websites found: ' + str(len(outputWebsiteLIST)))

    return outputWebsiteLIST


def removeWebsites(siteStrings):
    questionableAddresses = []

    for site in siteStrings:
        reMyPersonalSites = re.search(
            r'\bmypersonalwebsite01.gov\b|\bfamilywebsite.info\b|\bmyfoundationswebsite.org\b', site)
        reOtherGoodSites = re.search(r'\bpython.org\b|\bgithub.com\b', site)

        if (not reMyPersonalSites) & (not reOtherGoodSites):
            questionableAddresses.append(site)

    print('Questionable Addresses: ' + str(len(questionableAddresses)))
    return questionableAddresses


def printToFile(itemList, pathToWriteTo, filenameToUse):
    # open a new file, write out websites and close file
    strOutputPath = os.path.join(pathToWriteTo, filenameToUse)
    outputFile = open(strOutputPath, 'w')

    for item in itemList:
        outputFile.write(item + '\n')

    outputFile.close()

    print('\nData saved to: ' + os.path.join(pathToWriteTo, filenameToUse))


def main():
    # should the data be sorted?
    sortOutput = False

    # validate system args using above function
    if len(sys.argv) == 2:
        if validateArgs(sys.argv):
            strFileDirectory = os.path.dirname(sys.argv[1])
            strFileBaseName = os.path.basename(sys.argv[1])
            strFileAndLocation = os.path.join(
                strFileDirectory, strFileBaseName)
        else:
            exit()  # already gave reason in above method
    else:
        print('Usage: python.exe parseKnowBe4.py [FILE_LOCATION\FILE_NAME]')
        exit()

    print('\nReading in: ' + strFileAndLocation + '...')

    # open, read, store data, and close
    fileObject = open(strFileAndLocation)
    strFileData = fileObject.readlines()
    fileObject.close()

    print('File size: ' + str(os.path.getsize(sys.argv[1])))

    # find and write out emails (sorted)
    emailsFound = getEmails(strFileData, sortOutput)
    if sortOutput:
        printToFile(emailsFound, strFileDirectory, 'email_output-sorted.txt')
    else:
        printToFile(emailsFound, strFileDirectory, 'email_output.txt')

    # find and write out websites (sorted)
    websitesFound = getWebsites(strFileData, sortOutput)
    websitesInQuestion = removeWebsites(websitesFound)
    if sortOutput:
        printToFile(websitesFound, strFileDirectory,
                    'website_output-sorted.txt')
    else:
        printToFile(websitesFound, strFileDirectory, 'website_output.txt')

main()

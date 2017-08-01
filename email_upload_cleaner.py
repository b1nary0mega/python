#!/usr/bin/env python
"""Program to parse and update email upload list"""
import sys
import os
import re
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.2.0"
__maintainer__ = "James R. Aylesworth"
__email__ = "jarhed323@gmail.com"
__status__ = "Production"

'''
NOTES:
1.2.0 - Added method to remove known bad emails from provided list
        All output is now in complete lowercase
        Provided option to order list
        Created BAT file that will move to appropriate directory and fire off script, outputing
        all program output to "kb4-email_upload_cleaner-OUTPUT.txt"
1.1.3 - General cleanup, additional commenting, and better worded output
1.1.2 - Broke out file open, read and close into its own function
1.1.1 - Updates to validateFile function to utilize passed variable instead of array referance
'''


def validateFile(fileLocation):
    print('\nValidating ' + fileLocation)

    # verify the path and file names before setting any variables
    print('File Path: ' + str(fileLocation))
    print('File Directory: ' + os.path.dirname(fileLocation))

    if os.path.exists(os.path.dirname(fileLocation)) & os.path.isdir(os.path.dirname(fileLocation)):
        if not os.path.isfile(fileLocation):
            print('*** File does not appear at given path. ***')
            return False
        else:
            print('*VALIDATED*')
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
            outputEmailLIST.append((reEmailMatches[x]).lower())

    if sorted:
        outputEmailLIST.sort()

    print('Emails found: ' + str(len(outputEmailLIST)))

    return outputEmailLIST


def printToFile(itemList, pathToWriteTo, filenameToUse):
    # open a new file, write out websites and close file
    strOutputPath = os.path.join(pathToWriteTo, filenameToUse)
    outputFile = open(strOutputPath, 'w')

    for item in itemList:
        outputFile.write(item + '\n')

    outputFile.close()

    print('\nData saved to: ' + os.path.join(pathToWriteTo, filenameToUse))


def readInFile(strFileAndLocation):
    print('\nReading in ' + strFileAndLocation)

    # open, read, store data, and close
    fileObject = open(strFileAndLocation)
    strFileData = fileObject.readlines()
    fileObject.close()
    print('*COMPLETE*')
    return strFileData


def removeEmails(goodEmailList, badEmailList):
    print('\nRemoving bad emails...')
    for x in badEmailList:
        for y in goodEmailList:
            if x == y:
                print('Removing ' + x)
                goodEmailList.remove(x)
    return goodEmailList


def main():
    # validate system args using above function
    if len(sys.argv) == 3:
        if validateFile(sys.argv[1]):
            strFileDirectory = os.path.dirname(sys.argv[1])
            strFileBaseName = os.path.basename(sys.argv[1])
            strFileAndLocation = os.path.join(
                strFileDirectory, strFileBaseName)
        if validateFile(sys.argv[2]):
            strFileDirectory2 = os.path.dirname(sys.argv[2])
            strFileBaseName2 = os.path.basename(sys.argv[2])
            strFileAndLocation2 = os.path.join(
                strFileDirectory2, strFileBaseName2)

        else:
            exit()  # already gave reason in above method
    else:
        print(
            'Usage: python.exe email_upload_cleaner.py [FILE_LOCATION\EMAIL_LIST] [FILE_LOCATION\REMOVE_LIST]')
        exit()

    # read files into lists
    strFileData = getEmails(readInFile(strFileAndLocation), False)
    strFileData2 = getEmails(readInFile(strFileAndLocation2), False)

    # create good email list
    cleanEmailList = removeEmails(strFileData, strFileData2)

    # find and write out emails (sorted)
    sortOutput = True  # should the data be sorted?
    if sortOutput:
        printToFile(cleanEmailList, strFileDirectory,
                    'email_clean_OUTPUT--sorted.txt')
    else:
        printToFile(cleanEmailList, strFileDirectory,
                    'email_clean_OUTPUT--unsorted.txt')

main()

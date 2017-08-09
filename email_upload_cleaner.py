#!/usr/bin/env python
"""Program to parse and update email upload list"""
import sys
import os
import re
import csv
import datetime
__author__ = "James R. Aylesworth"
__contributor__ = "Tim Wesline"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.3.0"
__maintainer__ = "James R. Aylesworth"
__email__ = "jamesaylesworth@monroecounty.gov"
__status__ = "PRODUCTION"

'''
NOTES:
1.3.0 - Email validation added
        Removal of emails in provided exemptions list working
        Cleaned up output
1.2.3 - Tim Wesline found correct RegEx to split out OU's
1.2.2 - Added section for parsing CSV files, completing import and indexing of headers
1.2.1 - Added beginning break in print out as well as script run date
        Logically re-ordered functions
1.2.0 - Added method to remove known bad emails from provided list
        All output is now in complete lowercase
        Provided option to order list
1.1.3 - General cleanup, additional commenting, and better worded output
1.1.2 - Broke out file open, read and close into its own function
1.1.1 - Updates to validateFile function to utilize passed variable instead of array referance
'''


def validateFile(fileLocation):
    print('Validating ' + fileLocation)

    # verify the path and file names before setting any variables
    #print('File Path: ' + str(fileLocation))
    #print('File Directory: ' + os.path.dirname(fileLocation))

    if os.path.exists(os.path.dirname(fileLocation)) & os.path.isdir(os.path.dirname(fileLocation)):
        if not os.path.isfile(fileLocation):
            print('*** File does not appear at given path. ***')
            return False
        else:
            print('--> VALIDATED\n')
            return True
    else:
        print('Given path does is incorrect, or is not a directory.')
        return False


def csvParse(csvFile):
    # read in csv
    csvRows = []
    csvFileObject = open(csvFile)
    csvReaderObject = csv.reader(csvFileObject)

    # required headers for upload file
    csvRequiredHeaders = ['Email', 'First Name', 'Last Name', 'Phone Number', 'Extension', 'Group', 'Location',
                          'Division', 'Manager Name', 'Manager Email', 'Employee Number', 'Job Title', 'Password', 'Mobile', 'AD Managed']
    lotusHeaders = ['Internet Address', 'First Name', 'Last Name', 'Business Phone', 'Extension', 'Full Name', 'Company',
                    'Department', 'Manager', 'Manager Email', 'Employee Number', 'Job Title', 'Password', 'Mobile Phone', 'AD Managed']
    lotusHeadersFull = ['Title', 'First Name', 'Middle Name', 'Last Name', 'Full Name', 'Short Name', 'Phonetic Name', 'Suffix', 'Company', 'Department',
                        'Messaging ID', 'Job Title', 'Business Street', 'Business City', 'Business State', 'Business Postal Code',
                        'Business Country/Region', 'Home Street', 'Home City', 'Home State', 'Home Postal Code', 'Home Country/Region',
                        'Other Street', 'Other City', 'Other State', 'Other Postal Code', 'Other Country/Region', 'Assistant\'s Phone', 'Fax',
                        'Business Phone', 'Business Phone 2', 'Fax 2', 'Home Phone', 'Home Phone 2', 'Mobile Phone', 'Mobile Phone 2', 'Pager',
                        'Anniversary', 'Manager', 'Assistant\'s Name', 'Birthday', 'Category', 'Children', 'Directory Server', 'Business Mail',
                        'Internet Address', 'Personal Mail', 'Assistant\'s Mail', 'Business Mail 2', 'Personal Mail 2', 'Location', 'Comments',
                        'Spouse', 'Web Site', 'Blog Site']

    headerIndices = []

    for headerItem in lotusHeaders:
        try:
            headerIndices.append(lotusHeadersFull.index(headerItem))
        except Exception as e:
            print('Error trying to add ' + headerItem)
            # add a blank so we don't mess up header order
            headerIndices.append('')
            continue
        else:
            continue

    print('\nHeader Indices are: ' + str(headerIndices) + '\n')

    # Create storage, set headers, and build rows for new output
    dataToOutput = []
    dataToOutput.append(csvRequiredHeaders)

    for csvItem in csvReaderObject:
        rowToAdd = []

        # skip first row (incorrect header)
        if csvReaderObject.line_num == 1:
            continue

        for rowLoc in headerIndices:
            if(rowLoc == ''):
                rowToAdd.append('')
            else:
                # check if this is OU listing
                reOUMatch = re.findall(r'OU([+=]\w+)', csvItem[rowLoc])
                if(reOUMatch):
                    rowToAdd.append(reOUMatch[0].split("=")[1])
                    continue
                else:
                    if(isEmailAddress(str(csvItem[rowLoc]))):
                        if(isGoodEmail(csvItem[rowLoc].lower(), readInFile(sys.argv[2]))):
                            rowToAdd.append(csvItem[rowLoc].lower())
                        else:
                            #print('email excluded')
                            break
                    elif(rowLoc > 0):
                        rowToAdd.append(csvItem[rowLoc])
                    else:
                        continue
        dataToOutput.append(rowToAdd)

    csvFileObject.close()

    return dataToOutput


def writeCSV(fileToWriteOut, locationToWriteTo, fileNameToUse):

    filenameAndPathToUse = (os.path.join(locationToWriteTo, fileNameToUse))

    with open(filenameAndPathToUse, 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in fileToWriteOut:
            csvWriter.writerow(row)

    print("\nUpload file written to: " + filenameAndPathToUse + '\n\n')


def readInFile(strFileAndLocation):
    #print('\nReading in ' + strFileAndLocation)

    # open, read, store data, and close
    fileObject = open(strFileAndLocation)
    strFileData = fileObject.readlines()
    fileObject.close()
    #print('*COMPLETE*')
    return strFileData

def isEmailAddress(stringToTest):
    reEmailMatches = re.findall(r'[\w\.-]+@[\w\.-]+', str(stringToTest))
    if (reEmailMatches):
        return True
    else:
        return False

def isGoodEmail(email, badEmailList):
    result = ''
    for x in badEmailList:
        if(email.lower().rstrip() == x.lower().rstrip()):
            result = False
            print("--> removing " + email.lower() + " ... ")
            break
        else:
            result = True
            #print("Good Email returning - " + str(result))
    return result

def getEmails(searchString, sorted):
    print('\nSearching for emails...')
    reEmailMatches = re.findall(r'[\w\.-]+@[\w\.-]+', str(searchString))

    # put unique emails into list, sort and then output to file
    outputEmailLIST = []
    for x in range(len(reEmailMatches)):
        if outputEmailLIST.count(reEmailMatches[x]) == 0:
            outputEmailLIST.append((reEmailMatches[x]))

    if sorted:
        outputEmailLIST.sort()

    print('Emails found: ' + str(len(outputEmailLIST)))

    return outputEmailLIST


def removeEmails(goodEmailList, badEmailList):
    outputToSendBack = []
    print('\nRemoving bad emails...')
    for x in badEmailList:
        x = x.lower()
        print('Removing ' + x)
        for y in outputToSendBack:
            y = y.lower()
            if(y.find(x)):
                continue
            else:
                outputToSendBack.append(y)

    return outputToSendBack


def printToFile(itemList, pathToWriteTo, filenameToUse):
    strOutputPath = os.path.join(pathToWriteTo, filenameToUse)
    outputFile = open(strOutputPath, 'w', newline='')

    for item in itemList:
        if item != '':
            outputFile.write(item)

    outputFile.close()

    print('\nData saved to: ' + os.path.join(pathToWriteTo, filenameToUse))


def main():

    print('------------------------------------------------------------')
    print('Script run ' + str(datetime.datetime.now()) + '\n')

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

    # clean up the input file (match formatting and seperate out OU)
    cleanedData = csvParse(sys.argv[1])
    tempFileAndLocation = (os.path.join(strFileDirectory, '_temp_output.csv'))
    writeCSV(cleanedData, strFileDirectory, 'KnowBe4_Email_Upload.csv')

    # read files into lists
    #strFileData = readInFile(tempFileAndLocation)
    #strFileData2 = getEmails(readInFile(strFileAndLocation2), False)

    # create good email list
    #cleanEmailList = removeEmails(strFileData, strFileData2)

    #printToFile(cleanEmailList, strFileDirectory,
    #            'KnowBe4_Email_Upload.csv')

    print('------------------------------------------------------------')

main()

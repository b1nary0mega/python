#!/usr/bin/python

"""
FILE:   defender_for_endpoints.py
DATE:   09-SEP-22
DESC:   Module for advanced hunting in Microsoft Defender for Endpoint.
"""
__author__ = "Microsoft"
__copyright__ = "Copyright 2022"
__license__ = "N/A"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/run-advanced-query-sample-python"
__status__ = "Development"

import json
import urllib.request
import urllib.parse
import csv


def get_token():
    # Initialize variables based on app
    tenantId = "00000000-0000-0000-0000-000000000000"
    appId = "11111111-1111-1111-1111-111111111111"
    appSecret = "22222222-2222-2222-2222-222222222222"

    # Application sign-in = OAuth 2.0
    url = "https://login.microsoftonline.com/%s/oauth2/token" % (tenantId)

    # Application Base URL
    resourceAppIdUri = "https://api-us.securitycenter.microsoft.com"

    # Application Body
    body = {
        "resource": resourceAppIdUri,
        "client_id": appId,
        "client_secret": appSecret,
        "grant_type": "client_credentials",
    }

    # URL Encode the request
    data = urllib.parse.urlencode(body).encode("utf-8")

    # Make the request and store the token
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    jsonResponse = json.loads(response.read())
    aadToken = jsonResponse["access_token"]

    return aadToken


def run_query(aadToken, query):

    url = "https://api.securitycenter.microsoft.com/api/advancedqueries/run"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " + aadToken,
    }

    data = json.dumps({"Query": query}).encode("utf-8")

    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    jsonResponse = json.loads(response.read())

    return jsonResponse


def get_query_schema(jsonResponse):
    schema = jsonResponse["Schema"]

    return schema


def get_query_results(jsonResponse):
    results = jsonResponse["Results"]

    return results


def print_details(qResults):
    for result in qResults:
        print(result)

    return


def export_csv(qResults, outputPath):
    outputFile = open(outputPath, "w")
    output = csv.writer(outputFile)
    output.writerow(qResults[0].keys())

    for result in qResults:
        output.writerow(result.values())

    outputFile.close()

    return


if __name__ == "__main__":

    # Sample KQL Query to get last 10 Registry Events
    query = "DeviceRegistryEvents | limit 10"

    aadToken = get_token()  # get auth token
    resultSet = run_query(aadToken, query)  # run query
    qSchema = get_query_schema(resultSet)  # store query schema
    qResults = get_query_results(resultSet)  # store query results
    print_details(qResults)  # print results
    export_csv(qResults, "C:\\Temp\\fileOutput.csv")  # save output to a csv

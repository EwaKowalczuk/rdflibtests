#!/usr/bin/env python
import os
import re
import sys
import subprocess
import glob
import SPARQLWrapper
import sets

#check if query result matches answer

if(len(sys.argv) != 4):
    exit("python3 checkLubmAnswers.py <queryDirectory> <answerDirectory> <sparqlAddress>")

        
queryDirectory = sys.argv[1]
answerDirectory = sys.argv[2]
sparqlAddress = sys.argv[3]

#TODO should it be customizable?
QUERY_FILE_PREFIX = 'query'
ANSWER_FILE_PREFIX = 'answers_'
NO_ANSWERS = 'NO ANSWERS.'


#prepare connection to store
sparql = SPARQLWrapper.SPARQLWrapper(sparqlAddress)


for queryFileName in glob.glob(os.path.join(queryDirectory, QUERY_FILE_PREFIX + '*.txt')):
    #issue query
    sparqlOutput = []
    variableNames = []
    with open(queryFileName) as queryFile:
        print("---query: %s---" % queryFileName)
        query = [line.rstrip('\n') for line in queryFile.readlines() if not line.startswith('#')]
        query.insert(0, "DEFINE input:inference 'lubmruleset'")
        queryString = "\n".join(query)
        
        sparql.setQuery(queryString)
        sparql.setReturnFormat(SPARQLWrapper.JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
            sparqlOutput.append(" ".join([k + ":" + result[k]["value"] + " " for k in sorted(result.keys())]))



    #parse answers into rows + variables names
    answerFileName = os.path.join(answerDirectory, ANSWER_FILE_PREFIX + os.path.split(queryFileName)[1])
    expectedOutput = None
    with open(answerFileName) as answerFile:
        answerLines = answerFile.readlines();
        #check if answer should be empty set
        if answerLines[0].strip() == NO_ANSWERS:
            if len(sparqlOutput) == 0:
                print("OK")
            else:
                print("ERR: received result where expected no result")
            continue
        
        variableNames = answerLines.pop(0).split()

        expectedOutput = []
        for line in answerLines:
            values = line.split()

            valDict = {} 
            for i in range(len(values)):
                valDict[variableNames[i]] = values[i]
            #TODO refactor to function that compares two lists of dictionaries
            #however, there is probem because the first one is a dict of dicts...
            expectedOutput.append(" ".join([k + ":" + valDict[k] + " " for k in sorted(valDict.keys())]))

    #compare sizes
    sizeDifference = len(expectedOutput) - len(sparqlOutput)
    if sizeDifference != 0:
        print("ERR: results differ in length: expected: %s, sparql: %s" % (len(expectedOutput), len(sparqlOutput)))

    #there is a special case when
    expectedOutputSet = set(sorted(expectedOutput))
    sparqlOutputSet = set(sorted(sparqlOutput))
    if(expectedOutputSet == sparqlOutputSet):
        if(sizeDifference != 0):
            print("ERR: results differ because of different number of duplicated triples.")
        else:
            print("OK")
    else:
        print("ERR: content of results differs.")
        onlyInSparql = sparqlOutputSet - expectedOutputSet
        onlyInExpected = expectedOutputSet - sparqlOutputSet
        for element in onlyInSparql:
            print("ERR: only in sparql: %s" % element)
        for element in onlyInExpected:
            print("ERR: only in expected: %s" % element)



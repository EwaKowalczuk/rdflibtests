#!/usr/bin/env python3
import os
import re
import sys
import subprocess
import glob

#check if query result matches answer

if(len(sys.argv) != 4):
    exit("python3 checkLubmAnswers.py <queryDirectory> <answerDirectory> <sparqlAddress>")

        
queryDirectory = sys.argv[1]
answerDirectory = sys.argv[2]
sparqlAddress = sys.argv[3]

#TODO should it be customizable?
QUERY_FILE_PREFIX = 'query'
ANSWER_FILE_PREFIX = 'answers_query'

#TODO add inference
#TODO use sets while comparing answers
        
for queryFileName in glob.glob(os.path.join(queryDirectory, QUERY_FILE_PREFIX + '*.txt')):
    #issue query
    #TODO use SPARQL instead of isql
    #TODO use rdflib instead of sparel
    with open(queryFileName) as queryFile:
        print("---query: %s---" % queryFileName)
        query = [line.rstrip('\n') for line in queryFile.readlines() if not line.startswith('#')]
        query.insert(0, "SPARQL")
        query.append(";")
        queryString = "\n".join(query)
        #TODO add SPARQL + ;
        proc = subprocess.Popen(["/home/nuoritoveri/install/virtuoso/virtuoso/bin/isql" , "1111", "dba", "dba"], 
                stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
        stdout, stderr = proc.communicate(queryString)
        print(stdout)
        print()
        print()
    #m = re.match('uba1.7\\\\(University.+.owl)', f)
    #if m:
    #    newname = m.groups()[0]
    #    os.rename(os.path.join(directory,f), os.path.join(directory, newname))
    #with open(dir_entry_path, 'r') as my_file:
    #        data[dir_entry] = my_file.read()

#!/usr/bin/env python3
import os
import re
import sys

#check if query result matches answer

if(len(sys.argv) != 4):
    exit("python3 checkLubmAnswers.py <queryDirectory> <answerDirectory> <sparqlAddress>")

#TODO use SPARQL instead of isql
        
queryDirectory = sys.argv[1]
answerDirectory = sys.argv[2]
sparqlAddress = sys.argv[3]

#TODO should it be customizable?
QUERY_FILE_PREFIX = 'query'
ANSWER_FILE_PREFIX = 'answers_query'

for f in os.listdir(queryDirectory):
    print(f)
    #m = re.match('uba1.7\\\\(University.+.owl)', f)
    #if m:
    #    newname = m.groups()[0]
    #    os.rename(os.path.join(directory,f), os.path.join(directory, newname))
    #with open(dir_entry_path, 'r') as my_file:
    #        data[dir_entry] = my_file.read()

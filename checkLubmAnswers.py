#!/usr/bin/env python
import os
import re
import sys
import subprocess
import glob
import SPARQLWrapper

#check if query result matches answer

if(len(sys.argv) != 4):
    exit("python3 checkLubmAnswers.py <queryDirectory> <answerDirectory> <sparqlAddress>")

        
queryDirectory = sys.argv[1]
answerDirectory = sys.argv[2]
sparqlAddress = sys.argv[3]

#TODO should it be customizable?
QUERY_FILE_PREFIX = 'query'
ANSWER_FILE_PREFIX = 'answers_query'



#from rdfalchemy.sparql import SPARQLGraph
#from rdflib import Namespace
#
#endpoint = "http://dbpedia.org/sparql"
#graph = SPARQLGraph(endpoint)
#
#DB = Namespace("http://dbpedia.org/resource/")
#DBONTO = Namespace("http://dbpedia.org/ontology/")
#
#metal_bands = graph.subjects(predicate=DBONTO.genre, object=DB.Apocalyptic_and_post-apocalyptic_fiction)
#
#for band in metal_bands:
#    print(band)


#from SPARQLWrapper import SPARQLWrapper, JSON

query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ub: <http://www.lehigh.edu/~zhp2/2004/0401/univ-bench.owl#>
SELECT ?X	
WHERE
{?X rdf:type ub:GraduateStudent .
  ?X ub:takesCourse
<http://www.Department0.University0.edu/GraduateCourse0>}
"""

sparql = SPARQLWrapper.SPARQLWrapper(sparqlAddress)
sparql.setQuery(query)
sparql.setReturnFormat(SPARQLWrapper.JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
	print(result["X"]["value"])




#prepare connection to store
#store = rdflib.plugins.stores.sparqlstore.SPARQLStore()
#store.open((sparqlAddress, sparqlAddress))
#
##store=rdfextras.store.SPARQL.SPARQLStore(sparqlAddress)
#g=rdflib.Graph(store)
#
#qres = g.query(""" select distinct ?g where { graph ?g { ?s ?p ?o } } """)

#for row in qres:
#    print("result: %s" % row)

#TODO add inference
#TODO use sets while comparing answers
        
#for queryFileName in glob.glob(os.path.join(queryDirectory, QUERY_FILE_PREFIX + '*.txt')):
#    #issue query
#    #TODO use SPARQL instead of isql
#    #TODO use rdflib instead of sparql
#    with open(queryFileName) as queryFile:
#        print("---query: %s---" % queryFileName)
#        query = [line.rstrip('\n') for line in queryFile.readlines() if not line.startswith('#')]
#        query.insert(0, "SPARQL")
#        query.append(";")
#        queryString = "\n".join(query)
#        #TODO add SPARQL + ;
#        proc = subprocess.Popen(["/home/nuoritoveri/install/virtuoso/virtuoso/bin/isql" , "1111", "dba", "dba"], 
#                stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
#        stdout, stderr = proc.communicate(queryString)
#        stdoutLines = stdout.split('\n')
#        for line in stdoutLines:
#            print(line)
#        print()
#        print()
#
#Define the Stardog store
#endpoint = 'http://localhost:5820/demo/query'
#store = sparqlstore.SPARQLUpdateStore()
#store.open((endpoint, endpoint))
##Identify a named graph where we will be adding our instances.
#default_graph = URIRef('http://example.org/default-graph')
#ng = Graph(store, identifier=default_graph)
##Load our SKOS data from a file into an in-memory graph.
#g = Graph()
#g.parse('./sample-concepts.ttl', format='turtle')
##Serialize our named graph to make sure we got what we expect.
#print g.serialize(format='turtle')
##Issue a SPARQL INSERT update query to add the assertions
##to Stardog.
#ng.update(
#u'INSERT DATA { %s }' % g.serialize(format='nt')
#
#    #m = re.match('uba1.7\\\\(University.+.owl)', f)
#    #if m:
#    #    newname = m.groups()[0]
#    #    os.rename(os.path.join(directory,f), os.path.join(directory, newname))
#    #with open(dir_entry_path, 'r') as my_file:
#    #        data[dir_entry] = my_file.read()

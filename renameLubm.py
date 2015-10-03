#!/usr/bin/env python3
import os
import re
import sys

#rename ugly Lubm files

if(len(sys.argv) != 2):
    exit("python3 renameLubm.py <directory>")
        
directory = sys.argv[1]
onlyfiles = [ f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f)) ]

for f in onlyfiles:
    m = re.match('uba1.7\\\\(University.+.owl)', f)
    if m:
        newname = m.groups()[0]
        os.rename(os.path.join(directory,f), os.path.join(directory, newname))

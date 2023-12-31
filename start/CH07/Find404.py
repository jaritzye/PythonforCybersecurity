#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Jaritzy Esquivel``

import os
#Get script dir
script_dir = os.path.dirname(__file__)

#Prompt for file to analyze
log_file = input("Which file to analyze?")

#Open file
f = open(script_dir + "/" + log_file, "r")

#Read file line by line 
while True:
    line = f.readline()
    if not line:
        break
    #Check for *
    if "*" in line:
        print(line.strip())

# Close file
f.close()
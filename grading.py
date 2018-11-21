"""
A program to automate unzipping and executing Canvas submission files.

@author: Ziyi Huang

date: 11/20/18
"""

from zipfile import ZipFile
import os
import sys

# modificable variables

# folder that the submissions are stored in
filepath = "submissions/"

# the common postfix you want to enforce
postfix = "hw1.zip"

# Modify to not None or 0 to view the content within every zip file
view = None

# set the flag to not None or 0 to execute the file you wanto executre
# put the file path to execFile
execFlag = 1
execFile = "hw1/main.py"

dir = os.listdir(filepath)

for file in dir:
    try:
        if file.endswith(postfix):
            with ZipFile(filepath + file, 'r') as zip:
                zip.extractall()

                print "extracted all files from " + file

                if view:
                    print zip.namelist()
                if execFlag:
                    execfile(execFile)

                zip.close()

                con = raw_input("waiting to review..." + file)
        else:
            print "skipping file not end with" + postfix + "file name:", file
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print e
        con = raw_input("press Enter to continue or Ctrl+C to terminate")

"""
A program to automate unzipping and Canvas submission files.

@author: Ziyi Huang

date: 11/20/18
"""

from zipfile import ZipFile
import os
import sys

dir = os.listdir('.')

for file in dir:
    try:
        if file.endswith('hw3.zip') or file.endswith('HW3.zip'):
            with ZipFile(file, 'r') as zip:
                zip.extractall("hw3/")

                con = raw_input("waiting to review..." + file)
                if con == '\n':
                    continue
        else:
            print "skipping file not end with hw3.zip", "file name:", file
    except:
        raise

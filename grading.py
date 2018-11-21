from zipfile import ZipFile
import os
import sys

dir = os.listdir('.')

# for grading specific file
# with ZipFile('mangalamsaket_late_3722525_51186346.zip', 'r') as zip:
#     # zip.extract('hw1/main.py')
#     print zip.listdir()
#     print 'Extracted main.py from', file

# first loop, done 13
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
    # except:
    #     print "errors with ", file
    #     continue

# working with other files with error reason
# file = dir[int(sys.argv[1])]
# if file.endswith('hw1.zip'):
#     print 'Working with', file
#     filename = 'hw1/main.py'
#     with ZipFile(file, 'r') as zip:
#         zip.extract(filename)
#     execfile('hw1/main.py')
#
# else:
#     print file, "skipping file not end with hw1.zip"

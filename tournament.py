# Google Sheet APIs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Local fild operation
from zipfile import ZipFile
import os
import sys
import random

FILEPATH = 'submissions/'
RANGE = 'D35:D39'

def find_in_zip(filepath, keyword, dir):
    """
    finds files that ends with the keyword in the filepath and extract them to
    the dir
    """
    with ZipFile(filepath, 'r') as zip:
        for target in zip.infolist():
            tname = target.filename
            if not tname.startswith("__MACOSX") and tname.endswith(keyword):
                target.filename = keyword
                zip.extract(target, dir)
    zip.close()

dir = os.listdir(FILEPATH)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# enter credential information
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.JSON', SCOPES)

gc = gspread.authorize(credentials)

# enter the worksheet you want to open
wks = gc.open("Test").worksheet("Sheet2")

# change the range here to get the winners of the last round
# comment this line if it's the first round
winner_list = wks.range(RANGE)

# remove the null values in winners
for w in winner_list:
    if w.value == '':
        winner_list.remove(w)

while len(winner_list) > 1:
    # generate 2 random and non-repeating players
    playerA = winner_list[random.randint(0, len(winner_list) - 1)]
    winner_list.remove(playerA)
    playerB = winner_list[random.randint(0, len(winner_list) - 1)]
    winner_list.remove(playerB)

    # get their names, note the file name must follow Canvas format
    # aka name_"late"_num_num
    nameA = playerA.value.split("_")[0]
    nameB = playerB.value.split("_")[0]

    # put the info to the spreadsheet
    data = "[" + nameA + "]" + " vs. " + "[" + nameB + "]"
    wks.append_row([data])

    # unzip files in the local directory
    for file in dir:
        filepath = FILEPATH + file

        # try to extract file from the players, if error occurs, raise but continue
        if file.startswith(nameA):
            try:
                find_in_zip(filepath, 'ai.py', 'tournament')
                print "extraction for A finished"
            except Exception as e:
                print "ERROR with A:", e
                pass
        elif file.startswith(nameB):
            try:
                find_in_zip(filepath, 'ai.py', 'tournament_B')
                print "extraction for B finished"
            except Exception as e:
                print "ERROR with B:", e
                pass

    # wait for a match to be completed
    con = raw_input("waiting to compete...: " + nameA + " vs. " + nameB)
    os.remove("tournament/ai.py")
    print "successfully removed A"

    os.remove("tournament_B/ai.py")
    print "successfully removed B"

    con = raw_input("push Enter to continue...")

for left in winner_list:
    wks.append_row([left])

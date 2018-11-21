# Google Sheet APIs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Local fild operation
from zipfile import ZipFile
import os
import sys
import random

dir = os.listdir('submissions')

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# enter credential information
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.JSON', SCOPES)

gc = gspread.authorize(credentials)

# enter the worksheet you want to open
wks = gc.open("Test").worksheet("Sheet2")

# change the range here to get the winners of the last round
# comment this line if it's the first round
winner_list = wks.range('D24:D32')

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
        filepath = "submissions/" + file
        target = "hw3/ai.py"

        # try to extract file from the players, if error occurs, raise but continue
        if file.startswith(nameA):
            try:
                with ZipFile(filepath, 'r') as zip:
                    zip.extract(target, "tournament")
                    print "extraction for A finished"
            except:
                print "extraction error with A"
                pass
        elif file.startswith(nameB):
            try:
                with ZipFile(filepath, 'r') as zip:
                    zip.extract(target, "tournament_B")
                    print "extraction for B finished"
            except:
                print "extraction error with B"
                pass

    # wait for a match to be completed
    con = raw_input("waiting to compete...: " + nameA + " vs. " + nameB)
    os.remove("tournament/hw3/ai.py")
    print "successfully removed A"

    os.remove("tournament_B/hw3/ai.py")
    print "successfully removed B"
    continue

for left in winner_list:
    print left

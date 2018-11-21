# Google Sheet APIs
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Local fild operation
from zipfile import ZipFile
import os
import sys
import random

FILEPATH = 'submissions'

dir = os.listdir(FILEPATH)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.JSON', SCOPES)

gc = gspread.authorize(credentials)

wks = gc.open("Test").worksheet("Sheet2")

while len(dir) > 1:
    playerA = dir[random.randint(0, len(dir) - 1)]
    dir.remove(playerA)
    playerB = dir[random.randint(0, len(dir) - 1)]
    dir.remove(playerB)
    nameA = playerA.split("_")[0]
    nameB = playerB.split("_")[0]
    data = "[" + nameA + "]" + " vs. " + "[" + nameB + "]"
    wks.append_row([data])

for player in dir:
    print player.split("_")[0]

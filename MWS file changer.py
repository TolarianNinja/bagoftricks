# -*- coding: utf-8 -*-
import shutil, os, re, string, zipfile

# MWS file changer.py   Changes file names from MWSHQ standard to Magic Album
#                       standard and adds them to the specified type of ZIP
#                       file. Can add tags to file names for convention promo
#                       cards, etc.
#                       Written by Alex Hartshorn

cardPattern = re.compile(r"(.*?)(.full|.xlhq)(.jpg)")
directory = "C:\\MWS Images"
os.chdir(directory)
con_suffix = ''

    
    for fileName in os.listdir(directory):
        mo = cardPattern.search(fileName)

        if mo == None:
            continue

        oldCardName = mo.group(1)
        full = mo.group(2)
        extension = mo.group(3)

        cardName = oldCardName
    
        i = 0
        while i < len(cardName):
            if cardName[i] == 'Â»' or cardName[i] == '╗':
                cardName = cardName[:i] + '_' + cardName[i+1:]
            i += 1

        if cardName[-1].isdigit():
            cardName = cardName[:-1] + " [" + cardName[-1] + "]"

        if len(suffix) > 1:
            newFileName = cardName + con_suffix + extension
        else:
            newFileName = cardName + extension
        absWorkingDir = os.path.abspath(directory)

        pathName = os.path.join(absWorkingDir, fileName)
        newPathName = os.path.join(absWorkingDir, newFileName)

        shutil.move(pathName, newPathName)
        ENG_archive.write(fileName)
        os.remove(fileName)
        
        print("Processed " + cardName + "...")

    ENG_archive.close()    
    print('Work complete.')

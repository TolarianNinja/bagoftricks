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

while True:  
    archive_type = raw_input("""What sort of card archive do you need?
           1) Normal
           2) Foil
           3) Token
           4) None
> """)

    if archive_type == '4':
        con_suffix = raw_input("Is there a tag for the file names? (Enter tag or press enter for none)\n> ")
        if con_suffix != '\n':
            con_suffix = " " + con_suffix
        else:
            con_suffix = ''
        break
    else:    
        if archive_type == '1':
            zipFilename = os.path.join(directory, "ENG.zip")
            break
        elif archive_type == '2':
            zipFilename = os.path.join(directory, "ENG FOIL.zip")
            break
        elif archive_type == '3':
            zipFilename = os.path.join(directory, "ENG TOK.zip")
            break
        else:
            print("Invalid archive type selected.")
        ENG_archive = zipfile.ZipFile(zipFilename, 'w')
    
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

    if con_suffix != '' or con_suffix != 'n':
        newFileName = cardName + con_suffix + extension
    else:
        newFileName = cardName + extension
    absWorkingDir = os.path.abspath(directory)

    pathName = os.path.join(absWorkingDir, fileName)
    newPathName = os.path.join(absWorkingDir, newFileName)

    shutil.move(pathName, newPathName)
    if archive_type != '4':
        ENG_archive.write(newFileName)
        os.remove(newFileName)

    print("Processed " + cardName + "...")

if archive_type != '4':
    ENG_archive.close()
print('Work complete.')

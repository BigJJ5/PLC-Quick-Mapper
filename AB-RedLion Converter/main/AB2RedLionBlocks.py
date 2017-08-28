import csv

def convert():
    lines = list(csv.reader(open('ABTags.csv', 'r')))
    newfile = open("abredlionconversionINPUT.txt", 'w+')
    blocksize = input("Enter block size (array size in RSLogix): ")
    linesCounted = 0
    wordNumber = 0
    wordFound = False
    while (wordNumber <= blocksize-1):
        while (linesCounted < len(lines)):
            if lines[linesCounted][0] == "ALIAS":
                if lines[linesCounted][5].startswith('RedlionDSP:I.Data[' + str(wordNumber) + ']') and wordFound == False:
                    print("Exit.C02:" + '{:04d}'.format(wordNumber) + ".WORD:BITS=0")
                    newfile.write("Exit.C02:" + '{:04d}'.format(wordNumber) + ".WORD:BITS=0\n")
                    if lines[linesCounted][5].startswith('RedlionDSP:I.Data[' +str(wordNumber) + '].'):
                        description = raw_input("Multiple bits in word detected, manual name required (e.g, CommandsFromSpinnbau): ")
                        print str(description)
                        newfile.write(str(description)+ "\n")
                        wordNumber+=1
                        wordFound = True
                        linesCounted = 0
                        break
                    else:
                        print(lines[linesCounted][2].replace('"', ''))
                        newfile.write(lines[linesCounted][2].replace('"', '') + "\n")
                        wordNumber+=1
                        wordFound = True
                        linesCounted = 0
                        break
            linesCounted+=1
        if wordFound == False:    
            print("Exit.C02:" + '{:04d}'.format(wordNumber) + ".WORD:BITS=0")
            newfile.write("Exit.C02:" + '{:04d}'.format(wordNumber) + ".WORD:BITS=0\n")
            print("*")
            newfile.write("*\n")
            wordNumber+=1
        else:
            wordFound = False                         
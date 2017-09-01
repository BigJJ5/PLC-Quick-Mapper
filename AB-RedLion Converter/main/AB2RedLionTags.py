import csv
from tkinter import *
import tkinter as tk
writeBeginning = [[''],
                  ['[Numeric.0.0]'],
                  [''],
                  ['Name','Value','Extent','Manipulation','TreatAs','Access','ScaleTo', 'Sim', 'OnWrite', 'HasSP', 'Label', 'Desc', 'Class', 'FormType', 'LimitMin', 'LimitMax', 'LimitType', 'ColType', 'Event1 / Mode', 'Event2 / Mode', 'Trigger1 / Mode', 'Trigger2 / Mode', 'QuickPlot / Mode', 'Sec / Access', 'Sec / Logging']]
class ABRedLionTags:
    global somethingFound
    somethingFound = False  
    def convert(self, blocksize, PLCName, filename, tagname):
        lines = list(csv.reader(open(filename, 'r')))       
        with open("abredlionconversionINPUT.csv", "w")  as my_csv:                                                 #open export
            csvWriter= csv.writer(my_csv, delimiter=',', lineterminator = '\n') 
            csvWriter.writerows(writeBeginning)                                               #create new tag file for RedLion                                         #define number of tags to do before stopping
        #name = input("Enter the controller tag name to import (e.g, RedlionDSP)(CAPS MATTER):")            #tag could vary, but is typically RedLionDSP 
        linesCounted = 0
        wordFound = False                                                                                  #Initializing variables
        wordNumber = 0 
        while (wordNumber < blocksize):
            while (linesCounted < len(lines)):
                if lines[linesCounted][0] == "ALIAS":                                               #Is possibly a tag name we want
                    if lines[linesCounted][5].startswith(tagname + ':I.Data[' + str(wordNumber) + ']'):
                        if lines[linesCounted][5].startswith(tagname + ':I.Data[' +str(wordNumber) + '].'):
                            description = raw_input("Multiple bits in word detected, manual name required (e.g, CommandsFromSpinnbau): ")
                            wordNumber+=1
                            wordFound = True
                            somethingFound = True
                            
                            linesCounted = 0
                            break
                        else:
                            print str(wordNumber) + ' PLC1.' +lines[linesCounted][2]
                            newTag = [lines[linesCounted][2], '[' + PLCName + '.' + lines[linesCounted][2] + ']', '0', 'None', 'Default Integer', 'Read and Write', 'Do Not Scale', '', '', 'No', '', '', '', 'General', '', '', 'Automatic', 'General', 'Disabled', 'Disabled', 'Disabled', 'Disabled', 'Disabled', 'Default for Object', 'Default for Object']
                            with open("abredlionconversionINPUT.csv", "a") as my_csv:
                                csvWriter = csv.writer(my_csv, delimiter=',', lineterminator = '\n')
                                csvWriter.writerow(newTag)
                            wordNumber+=1
                            wordFound = True
                            somethingFound = True
                            linesCounted = 0
                            break 
                linesCounted+=1   
            if wordFound == False:
                print "Nothing found " + str(wordNumber) 
                wordNumber+=1
                linesCounted = 0
            else:
                wordFound = False
        print "Searching for outputs"
        wordNumber = 0
        linesCounted = 0
        wordFound = False
        while (wordNumber < blocksize):
            while (linesCounted < len(lines)):
                if lines[linesCounted][0] == "ALIAS":                                               #Is possibly a tag name we want
                    if lines[linesCounted][5].startswith(tagname + ':O.Data[' + str(wordNumber) + ']'):
                        if lines[linesCounted][5].startswith(tagname + ':O.Data[' +str(wordNumber) + '].'):
                            description = raw_input("Multiple bits in word detected, manual name required (e.g, CommandsFromSpinnbau): ")
                            wordNumber+=1
                            wordFound = True
                            somethingFound = True
                            linesCounted = 0
                            break
                        else:
                            print str(wordNumber) + ' PLC1.' +lines[linesCounted][2]
                            newTag = [lines[linesCounted][2], '[' + PLCName +'.' + lines[linesCounted][2] + ']', '0', 'None', 'Default Integer', 'Read and Write', 'Do Not Scale', '', '', 'No', '', '', '', 'General', '', '', 'Automatic', 'General', 'Disabled', 'Disabled', 'Disabled', 'Disabled', 'Disabled', 'Default for Object', 'Default for Object']
                            with open("abredlionconversionINPUT.csv", "a") as my_csv:
                                csvWriter = csv.writer(my_csv, delimiter=',', lineterminator = '\n')
                                csvWriter.writerow(newTag)
                            wordNumber+=1
                            wordFound = True
                            somethingFound = True
                            linesCounted = 0
                            break 
                linesCounted+=1   
            if wordFound == False:
                print "Nothing found " + str(wordNumber) 
                wordNumber+=1
                linesCounted = 0
            else:
                wordFound = False
        global somethingFound
        return somethingFound
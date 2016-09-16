import os
import time
import sys
from shutil import copyfile

print("\nPlease enter the router template folder name to be generated: ")
templateName = input()
print("The template name is: ",templateName)
print("Press Y if this is this correct?")
myChoice = input()

##if myChoice != "Y" :
##    print("Wrong Input") #Validation should go here
##
##else:
##    print("OK")

osPath = "working_templates"
osNewPath = osPath + "/" + templateName

if not os.path.isdir(osNewPath):

    print("\n*** File Creation Started ***")
    os.makedirs(osNewPath)
    print("Created folder in " + osNewPath)
else:
    print("\n*** Folder Error ***")
    print(osNewPath + " already exists")
    
#Define variables
outputFileName = osNewPath + "/template.jinja2"

osFolderSrc = "template_files"
osFileSrc = "template.jinja2"
osPathSrc = osFolderSrc + "/" + osFileSrc

osNewFileDst = templateName + ".jinja2"
osPathDst = osNewPath + "/" + osNewFileDst

print("\n*** Checking ***")
print("\nChecking for " + osFileSrc+ " file in " + osPathDst)

if os.path.exists(osNewPath):
    print("\nFile Exists, creating named copy of " + osFileSrc)
    copyfile(osPathSrc, osPathDst)
    print("\n*** File Copy Complete ***")
    print("\nWritten file: " + osPathDst + " to disk")
    time.sleep(5)
    print("\n*** NADs Configuration Uploader to jina2 template named: " + osPathDst + "  ***")
    print("\nPress enter then CTRL+Z on new line after pasting")
    print("\nPlease Paste in the NADs Configuration File below: ")
    inputConfiguration = sys.stdin.read()

    f = open(outputFileName, "r")
    contents = f.readlines()
    f.close()

    contents.insert(27, inputConfiguration) # write to line 27 and apply input configuration

    #write the file
    f = open(outputFileName, "w") 
    contents = "".join(contents)
    f.write(contents)
    f.close()
    print("Written to file: ",outputFileName)

else:
    print('\nError: ',outputFileName,'does not exist! Check and retry')



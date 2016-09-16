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
print("\n*** Provisining Required Files ***")

if not os.path.isdir(osNewPath):


    os.makedirs(osNewPath)
    print("Created folder in " + osNewPath)
else:
    print("Error: " + osNewPath + " already exists")
    print("Continuing.....")
    
#Define variables
outputFileName = osNewPath + "/template.jinja2"

osFolderSrc = "template_files"
osFileSrc = "template.jinja2"
osPathSrc = osFolderSrc + "/" + osFileSrc

osNewFileDst = templateName + ".jinja2"
osPathDst = osNewPath + "/" + osNewFileDst

if os.path.exists(osNewPath):
    print("\nCopying " + osPathSrc + " template file to: " + osPathDst)
    copyfile(osPathSrc, osPathDst)
    print("\nRenaming " + osPathSrc +" to file: " + osPathDst)
    print("\n*** File Copy Complete ***")
    time.sleep(5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n*** NADs Config Loader ***")
    print("Destination : " + osPathDst)
    print("\nPress enter then CTRL+Z on new line after pasting")
    print("\nPlease Paste in the NADs Configuration File below: ")
    inputConfiguration = sys.stdin.read()

    f = open(osPathDst, "r")
    contents = f.readlines()
    f.close()

    contents.insert(27, inputConfiguration) # write to line 27 and apply input configuration

    #write the file
    f = open(osPathDst, "w") 
    contents = "".join(contents)
    f.write(contents)
    f.close()
    print("Written to file: ",osPathDst)

else:
    print('\nError: ',outputFileName,'does not exist! Check and retry')



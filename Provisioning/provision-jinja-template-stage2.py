import os
import time
import sys

print("\nPleae enter the router template folder name to be generated : ")
templateName = input()
print("The template name is: ",templateName)
print("Press Y if this is this correct?")
myChoice = input()

if myChoice != "Y" :
    print("Quitting")

else:
    print("OK")

osPath = "Working_Templates"
osNewPath = osPath + "/" + templateName

if not os.path.isdir(osNewPath):

    os.makedirs(osNewPath)
    print("Created folder " + osNewPath)

else:
    print("Error: Folder " + osNewPath + " already exists")

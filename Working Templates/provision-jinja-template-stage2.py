import os
import time
import sys

print("\nPleae enter the router template name to be generated : ")
templateName = input()
print("The template name is: ",templateName)
print("Press Y if this is this correct?")
myChoice = input()

if myChoice != "Y" :
    print("Quitting")

else:
    print("OK")

osPath = templateName

if not os.path.isdir(osPath):
    print(os.path.makedirs(osPath))
    print("Created folder" + osPath)

else:
    print("Error: Folder already exists")


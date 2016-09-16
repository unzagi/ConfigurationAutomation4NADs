import os
import time
import sys

print("\nPleae enter the router template name to be generated : ")
templateName = sys.stdin.read()
print("The template name is: ",templateName)
print("Press Y if this is this correct?")
myChoice = input()

if myChoice not ("Y") :
    print("Quitting")

else:
    print("OK")


if not os.path.exits

filename = "/my/directory/filename.txt"
dir = os.path.dirname(filename)

try:
    os.stat(dir)
except:
    os.mkdir(dir)       

f = file(filename)

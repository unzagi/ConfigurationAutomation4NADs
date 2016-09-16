import os
import time
import sys

#Define variables
outputFileName = "template.jinja2"
print("\nChecking for ", outputFileName, " file in working directory")
print("\n", outputFileName, "exists")
print("\n*** NADs Configuration Uploader to jina2 template... ***")
print("\nPress enter then CTRL+Z on new line after pasting")

if os.path.exists(outputFileName):
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
    print('n\Error: ',outputFileName,'does not exist! Check and retry')


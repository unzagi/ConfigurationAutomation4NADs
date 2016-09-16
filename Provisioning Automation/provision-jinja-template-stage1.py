import os
import time
import sys

#Define variables
outputFileName = "template.jinja2"

print("\nNADs Configuration Uploader to jina2 template...")
print("\nPlease Paste in the NADs Configuration File")
inputConfiguration = sys.stdin.read()
print(inputConfiguration)
print("\n Checking for ", outputFileName, " file in working directory")

if os.path.exists(outputFileName):

    print("\n", outputFileName, " exists")
    f = open(outputFileName, "r")
    contents = f.readlines()
    f.close()

    contents.insert(27, inputConfiguration) # write to line 27 and apply input configuration

    #write the file
    f = open(outputFileName, "w") 
    contents = "".join(contents)
    f.write(contents)
    f.close()

    print("written to file: ",outputFileName)

else:
    print('n\Error: ',outputFileName,'does not exist! Check and retry')


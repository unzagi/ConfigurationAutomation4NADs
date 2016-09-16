Provisioning List
-----------------

#Generate the router Template Folder

```python
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
```

#Change directory to the Template Folder

#Generate the Template File

```python
from shutil import copyfile

osFolderSrc = "template_files"
osFileSrc = "template.jinja2"
osPathSrc = osFolderSrc + "/" + osFileSrc

print(osPathSrc)

osPathDst = "no.jinja2"

copyfile(osPathSrc, osPathDst)
print("Written file: " + osPathDst)
```

#Paste in the NADs Configuration File

```python

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
```

#Generate the Python Variable Folder

#Generate the Python Runtime File
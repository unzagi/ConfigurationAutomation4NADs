## Copy the python template file and rename
print(osFolderSrc)
osFileSrc = "jinja_variables_template.py"
osPathSrc = osFolderSrc + "/" + osFileSrc
print("osPathSrc: " + osPathSrc)
print(templateName)
osNewFileDst = "jinja2_" + templateName + "_variables.py"
print("osNewFileDst: " + osNewFileDst)
osPathDst = osNewPath + "/" + osNewFileDst
print("osPathDst: " + osPathDst)
print("osNewPath: "+ osNewPath)
if os.path.exists(osNewPath):

    copyfile(osPathSrc, osPathDst)

    
    print("osPathSrc: " + osPathSrc)
    print("\nCopying " + osPathSrc + " template file to: " + osPathDst)

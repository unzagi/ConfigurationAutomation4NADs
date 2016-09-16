## Copy the python template file and rename
print(osFolderSrc)
osFileSrc = "jinja_variables_template.py"
osPathSrc = osFolderSrc + "/" + osFileSrc
print("osPathSrc: " + osPathSrc)

osNewFileDst = "jinja2_" + templateName + "variables.py"
osPathDst = osNewPath + "/" + osNewFileDst
print("osPathDst: "osPathDst)
print("osNewPath: "osNewPath)
if os.path.exists(osNewPath):
    print("osPathSrc: " + osPathSrc)
    print("\nCopying " + osPathSrc + " template file to: " + osPathDst)

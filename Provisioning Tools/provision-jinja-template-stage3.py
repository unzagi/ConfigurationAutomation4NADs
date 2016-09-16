from shutil import copyfile

osFolderSrc = "Template"
osFileSrc = "template.jinja2"
osPathSrc = osFolderSrc + "/" + osFileSrc

print(osPathSrc)

osPathDst = "no.txt"

copyfile(osPathSrc, osPathDst)
print("Written")

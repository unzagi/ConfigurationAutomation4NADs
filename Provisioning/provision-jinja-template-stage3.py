from shutil import copyfile

osFolderSrc = "template_files"
osFileSrc = "template.jinja2"
osPathSrc = osFolderSrc + "/" + osFileSrc

print(osPathSrc)

osPathDst = "no.jinja2"

copyfile(osPathSrc, osPathDst)
print("Written file: " + osPathDst)

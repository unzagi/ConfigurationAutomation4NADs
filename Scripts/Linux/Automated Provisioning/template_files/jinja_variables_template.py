# Import python time module
import time

# Variables Template
# Set the template specific description variables - information from NADS excel spreadsheet
hardwareMake = 'Juniper'
hardwareModel = 'Juniper SRX300'
projectTemplateName = 'template'
previousTemplateName = 'none'

#Router Template information
telcoName = 'Telco Name'
circuitName = 'Circuit Name'
bandwidth = 'bandwidth'
routing = 'routng protocol'
connectionType = 'Connection Type'
customerLans = 1
customerStaticRoutes = 0
outOfScope = "What is out of Scope?"

#Generated File information
outputFileName = "template.txt"
jinja2TemplateName = 'template.jinja2'
dateNow = time.strftime("%c") # set the time/date
engineerName = 'Simon Brooks'

#Set the configuration file variables - use 'lowercase' and '_' for Jijna2 Variables
#These will be subject to change/additions based on the template
ifaceLanName = 'ge-0/0/0'
ifaceWanName = 'ge-0/0/7'

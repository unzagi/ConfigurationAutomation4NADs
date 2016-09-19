# Import python time module
import time

# Variables Template
# Set the template specific description variables - information from NADS excel spreadsheet
hardwareMake = 'Juniper'
hardwareModel = 'Juniper SRX300'
projectTemplateName = 'JU06'
previousTemplateName = 'JN43'

#Router Template information
telcoName = 'TTB  Ethernet - 10Gb NNI'
circuitName = 'EAD100'
bandwidth = '100Mbps'
routing = 'BGP'
connectionType = 'Core - C'
customerLans = 1
customerStaticRoutes = 0
outOfScope = "More than one static NAT, DHCP, VPN, Backup/Redundancy, Secondary IP Addresses & ANYTHING else"

#Generated File information
outputFileName = "JU06-template.txt"
jinja2TemplateName = 'JU06.jinja2'
dateNow = time.strftime("%c") # set the time/date
engineerName = 'Simon Brooks'

#Set the configuration file variables - use 'lowercase' and '_' for Jijna2 Variables
#These will be subject to change/additions based on the template
ifaceLanName = 'ge-0/0/0'
ifaceWanName = 'ge-0/0/6'

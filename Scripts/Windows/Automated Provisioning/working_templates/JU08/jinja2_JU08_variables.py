# Import python time module
import time

# Variables Template
# Set the template specific description variables - information from NADS excel spreadsheet
hardwareMake = 'Juniper'
hardwareModel = 'SRX340+SRX-MP-1SFP-GE'
projectTemplateName = 'JU07'
previousTemplateName = 'JN49'

#Router Template information
telcoName = 'TTB  Ethernet - 10Gb NNI'
circuitName = 'EAD1000'
bandwidth = '200Mbps - 1Gbps'
routing = 'BGP'
connectionType = 'Core - B'
customerLans = 1
customerStaticRoutes = 0
outOfScope = "DHCP, VPN, Backup/Redundancy, Secondary IP Addresses & ANYTHING else"

#Generated File information
outputFileName = "JU08-template.txt"
jinja2TemplateName = 'JU08.jinja2'
dateNow = time.strftime("%c") # set the time/date
engineerName = 'Simon Brooks'

#Set the configuration file variables - use 'lowercase' and '_' for Jijna2 Variables
#These will be subject to change/additions based on the template
ifaceLanName = 'ge-0/0/0'
ifaceWanName = 'ge-0/0/6'

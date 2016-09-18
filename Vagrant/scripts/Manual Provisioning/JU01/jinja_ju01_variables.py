import time

# Set the template specific description variables - information from NADS template excel spreadsheet
hardwareMake = 'Juniper'
hardwareModel = 'Juniper SRX300+SRX-MP-1SFP-GE'
projectTemplateName = 'JU01'
previousTemplateName = 'JN46'

telcoName = 'TTB  Ethernet - 10Gb NNI'
circuitName = 'EAD1000'
bandwidth = '100-200Mbps'
routing = 'BGP'
connectionType = 'Core - A'
customerLans = 1
customerStaticRoutes = 0
outOfScope = "DHCP, VPN, Backup/Redundancy, Secondary IP Addresses & ANYTHING else"

outputFileName = "JU01-template.txt"
jinja2TemplateName = 'JU01.jinja2'
dateNow = time.strftime("%c") # set the time/date
engineerName = 'Simon Brooks'

#Set the configuration file variables - use 'lowercase' and '_' for Jijna2 Variables
ifaceLanName = 'ge-0/0/0'
ifaceWanName = 'ge-0/0/7'

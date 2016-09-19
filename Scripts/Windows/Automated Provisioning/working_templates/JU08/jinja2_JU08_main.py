# Jinja2 Template from https://vimeo.com/120005103
# Requires Jinja2 to be installed into python- http://jinja.pocoo.org/docs/dev/intro/
# Requires a Jinja2 template file to have already been created and variables set

# import librarys
import jinja2
import os

# Variables
from jinja2_JU08_variables import *

# Setup jinja2
# tell jinja2 where to load templates from ( this should be your current working directory)
loader = jinja2.FileSystemLoader(os.getcwd())

#Create a jinja2 environment and reference the above loader
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

#Render the template based on jinja2 file name variable
template = jenv.get_template('JU08.jinja2')

#Render the configuration based on the variables then print the output
output = template.render(hardware_make=hardwareMake,hardware_model=hardwareModel,template_name=projectTemplateName,previous_template_name=previousTemplateName,jinja2_template_name=jinja2TemplateName, 
                         telco_name=telcoName,circuit_name=circuitName,bandwidth=bandwidth,routing=routing,connection_type=connectionType,customer_lans=customerLans,customer_static_routes=customerStaticRoutes,out_of_scope=outOfScope,
                         date_time=dateNow,engineer_name=engineerName,iface_lan_name=ifaceLanName,iface_wan_name=ifaceWanName)
#Write the configuration to file if the file does not already exist
if not os.path.exists(outputFileName):
    with open(outputFileName, 'wt') as f:
        f.write(output)
        print(output)
        print("\nTempate written to file: ",outputFileName)
else:
    print('n\Error: ',outputFileName,'already exists! Check and retry')

Provisioning List
-----------------

provisioning_script.py

0. Enter the router template name
1. Create the router template configration folder to disk
2. Copy the template.jinja2 file to sed folder
3. Rename a copy of the template.jinja2 file to the name of the router template
4. Prompt for user input and paste in NADs configuration file
5. Add configuration file into router template 

# Manual Part 1

0. Use notepad++ and run the compare on the NADS + jinja2 templates
1. Audit the configuration jinja2 file against the existing NADs configuration
2. Add the base jinja2 variables

#Generate the Python Variable File

0. Now generates python variable file with default information
1. Read_file.py code created but not yet used

#Manual Part 2
0. Update the default variables in jinja2_'templateName'_variables.py
1. Add any additional variables defined in manual part 1 point 2

#Generate the Python Runtime File
0. Now populates the template name folder with the python runtime 'jinja-template.py'
1. Renames file to jinja2_'templateName'_main.py

#Manual Part 3
0. Need to manually update the include template statement
```python
from jinja_variables_template import *
```
1. Need to manually update the template variable to point to the jinja2 'osPathDst' variable, not the
'osPathDst' variable when populated with jinja2_'templateName'_main.py" 
```python
#Render the template based on jinja2 file name variable
template = jenv.get_template('template.jinja2')
```
2. Need to manually update the jinja2 variables based on Manual Part 1
```python
#Render the configuration based on the variables then print the output
output = template.render(hardware_make=hardwareMake,hardware_model=hardwareModel,template_name=projectTemplateName,previous_template_name=previousTemplateName,jinja2_template_name=jinja2TemplateName, 
                         telco_name=telcoName,circuit_name=circuitName,bandwidth=bandwidth,routing=routing,connection_type=connectionType,customer_lans=customerLans,customer_static_routes=customerStaticRoutes,out_of_scope=outOfScope,
                         date_time=dateNow,engineer_name=engineerName,iface_lan_name=ifaceLanName,iface_wan_name=ifaceWanName)
```
Wish List
---------

1. Tidy up the Input/Output variables in the provisioning_script
2. Write a provisioning menu
3. All the template files are copied to disk, then a copy is created. Tidy this up.
4. PROFIT?
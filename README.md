Automation of NADs Configurations
---------------------------------

Scripts Folder: Contains the NADs configuration python files. There are Windows and Linux versions I am currently developing.

Vagrant Folder: This contains the vagrant file and two folders scripts and sites. Please check the README.md.

You can run the scripts without having to build the VM in vagrant. Just download the file and run them in python.
Python isn't OS specific, but I've split the scripts up according to the OS type I've been developing them on, the Windows scripts written first.

Change Log
----------

1. Created vagrant file for a web/python/jijnja2 environment

2. In the /scripts folder you have:

  1. Windows Scripts - Tested on Python 3 for Windows - See Readme.md
  2. Linux Scripts - Currently being tested in the Vagrant environment


3. In each /scripts/linux & /scripts/windows folder you have:

 1. Manual Provisioning - Contains the original python scripts using Windows.

 2. Automated Provisioning - An automated process

 Check the readme.md file in automated Provisioning

 3. A copy of these scripts are located to Vagrant\scripts. These scripts will be developed in a linux environment.

Wish list
---------
Create text color formatting on the Linux Scripts

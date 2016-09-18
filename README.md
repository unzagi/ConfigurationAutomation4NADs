Automation of NADs Configurations
---------------------------------

I've now created a basic environment that can be run using vagrant.
This has been built from my other repo: https://github.com/unzagi/vagrant-php-box

My Atlas webpage is: https://atlas.hashicorp.com/unzagi/boxes/ubuntu/

We're currently using v0.1 of the ubuntu box.

I've only included the jinja2 dependencies, and pip3 for python.
If I add any additional python modules or other dependencies I will update the box file
and I've documented the process for this.

You can run the scripts without having to build the VM in vagrant, just work from the scripts file and run using
python 3 on your windows/linux/unix box.

As the vagrant environment is linux and the base python scripts have been tested on windows there may be some unknown bugs.

The python scripts in the vagrant folder will start to differ.

You will need to type CTRL + D for Linux, and CTRL + Z for windows for the end of line file.

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

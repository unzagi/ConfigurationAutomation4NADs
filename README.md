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

Change Log
----------

1. Created vagrant file for a web/python/jijnja2 environment

2. NADs configuration README.md has been moved to the \scripts folder

In the scripts folder you have:

 1. Manual Provisioning - Original python scripts created

 2. Automated Provisioning - Automating the process using - see README.md in folder


 To make changes to the .box file
 -----------------------------

 To make additional changes to the vagrant .box file

 Instructions are taken from: [scotch.io](https://scotch.io/tutorials/how-to-create-a-vagrant-base-box-from-an-existing-one)

 1. The box should be running, so SSH into it

 ```shell
 vagrant ssh
```
 2. Setup the server by running any installation or mkfile commands
 ```shell
 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install vim
 sudo apt-get install apache2
 sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql
 sudo mysql_install_db
 sudo /usr/bin/mysql_secure_installation
 sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt
 sudo apt-get install php5-cgi php5-cli php5-curl php5-common php5-gd php5-mysql
 sudo service apache2 restart
```
 3. Make the Box as Small as possible
 ```shell
 sudo apt-get clean
```
4.Then, “zero out” the drive (only for Ubuntu) :
 ```shell
  sudo dd if=/dev/zero of=/EMPTY bs=1M
  sudo rm -f /EMPTY
```

Repackage the box file
----------------------
```shell
vagrant package --output mynew.box
```

Upload .box file to Atlas area

1. If a new box

  1. Log into [Atlas](https://atlas.hashicorp.com/vagrant)

  2. Select new box

  3. Give it a name, select create box

  4. Set box provider

  5. Set description

  6. Set version number

  7. Set it to release

2. If a version change to a box

  1. Select existing box i.e. unzagi/ubuntu/

  2. Select New Version

  3. Set version number

  4. Set description

  5. Create version

Once the new box is updated it the vagrant file will might need to be set to the version if you have made changes. I've not yet tested this.

You may specify an explicit version of a box by specifying config.vm.box_version for example:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.box_version = "1.1.0"
end
```
Vagrant File
--------------

This is a recent copy of the current vagrant file

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant development environment requires a box to build off of.
  config.vm.box_url = "https://atlas.hashicorp.com/unzagi/boxes/ubuntu"
  config.vm.box = "unzagi/ubuntu"

    forward_port = ->(guest, host = guest) do
    config.vm.network :forwarded_port,
      guest: guest,
      host: host,
      auto_correct: true
  end

  # Sync between the web root of the VM and the 'sites' directory
  config.vm.synced_folder "sites/", "/var/www"
  # Sync between the scripts foldr in the VM and the 'sites' directory
  config.vm.synced_folder "scripts/", "/home/vagrant/scripts/"

  forward_port[1080]      # mailcatcher
  forward_port[3306]      # mysql
  forward_port[80, 8080]  # nginx/apache

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file = "default.pp"
  end

  config.vm.network :private_network, ip: "172.16.1.10"
end
```
What does the code do?
----------------------

This code sets the URL of the box hosted in Atlas, and sets up port forwarding.

```ruby
 Vagrant.configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant development environment requires a box to build off of.
  config.vm.box_url = "https://atlas.hashicorp.com/unzagi/boxes/ubuntu"
  config.vm.box = "unzagi/ubuntu"

    forward_port = ->(guest, host = guest) do
    config.vm.network :forwarded_port,
      guest: guest,
      host: host,
      auto_correct: true
  end
```

This code sets copies files and sets ports.
```ruby
   # Sync between the web root of the VM and the 'sites' directory
  config.vm.synced_folder "sites/", "/var/www"
  # Sync between the scripts foldr in the VM and the 'sites' directory
  config.vm.synced_folder "scripts/", "/home/vagrant/scripts/"

  forward_port[1080]      # mailcatcher
  forward_port[3306]      # mysql
  forward_port[80, 8080]  # nginx/apache

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file = "default.pp"
  end
 ```

This code sets the network IPs for the added VM network.

```ruby
  config.vm.network :private_network, ip: "172.16.1.10"
```

I've not yet tested any other types of commands but it gives a general idea to work from.

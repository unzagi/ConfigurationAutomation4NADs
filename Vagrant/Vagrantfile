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

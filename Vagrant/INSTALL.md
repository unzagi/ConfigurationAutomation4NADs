Automation of NADs Configurations
--

Requirements
--

[Vagrant](https://www.vagrantup.com/)

A [git](https://git-scm.com/downloads) management app


Windows Install
--

1. Clone repo https://github.com/unzagi/ConfigurationAutomation4NADs
2. Create a folder e.g. C:\nadsautomation
3. Copy the contents of vagrant folder in the cloned repo to C:\nadsautomation
4. Open a new command line in CMD
5. Run vagrant up

  ```
  C:\nadsautomation>vagrant up
  ```

6. You should see something along the lines of:

  ```
  C:\nadsautomation>vagrant up
  Bringing machine 'default' up with 'virtualbox' provider...
  ==> default: Importing base box 'unzagi/ubuntu'...
  ==> default: Matching MAC address for NAT networking...
  ==> default: Checking if box 'unzagi/ubuntu' is up to date...
  ==> default: Setting the name of the VM: nadsautomation_default_1474218966128_43174
  ==> default: Fixed port collision for 3306 => 3306. Now on port 2200.
  ==> default: Clearing any previously set network interfaces...
  ==> default: Preparing network interfaces based on configuration...
      default: Adapter 1: nat
      default: Adapter 2: hostonly
  ==> default: Forwarding ports...
      default: 1080 (guest) => 1080 (host) (adapter 1)
      default: 3306 (guest) => 2200 (host) (adapter 1)
      default: 80 (guest) => 8080 (host) (adapter 1)
      default: 22 (guest) => 2222 (host) (adapter 1)
  ==> default: Booting VM...
  ==> default: Waiting for machine to boot. This may take a few minutes...
      default: SSH address: 127.0.0.1:2222
      default: SSH username: vagrant
      default: SSH auth method: private key
      default: Warning: Remote connection disconnect. Retrying...
  ==> default: Machine booted and ready!
  ==> default: Checking for guest additions in VM...
      default: The guest additions on this VM do not match the installed version of
      default: VirtualBox! In most cases this is fine, but in rare cases it can
      default: prevent things such as shared folders from working properly. If you see
      default: shared folder errors, please make sure the guest additions within the
      default: virtual machine match the version of VirtualBox you have installed on
      default: your host and reload your VM.
      default:
      default: Guest Additions Version: 4.3.36
      default: VirtualBox Version: 5.1
  ==> default: Configuring and enabling network interfaces...
  ==> default: Mounting shared folders...
      default: /var/www => C:/nadsautomation/sites
      default: /vagrant => C:/nadsautomation
      default: /home/vagrant/scripts => C:/nadsautomation/scripts
      default: /tmp/vagrant-puppet/manifests-a11d1078b1b1f2e3bdea27312f6ba513 => C:/nadsautomation/manifests
  ==> default: Running provisioner: puppet...
  ==> default: Running Puppet with default.pp...
  ==> default: stdin: is not a tty
  ==> default: Notice: Compiled catalog for vagrant-ubuntu-trusty-64.brooksy.local in environment production in 0.16 seconds
  ==> default: Notice: /Stage[main]/Base/Exec[apt-get update]/returns: executed successfully
  ==> default: Notice: /Stage[main]/Mysql/Exec[set-mysql-password]/returns: mysqladmin: connect to server at 'localhost' failed
  ==> default: Notice: /Stage[main]/Mysql/Exec[set-mysql-password]/returns: error: 'Access denied for user 'root'@'localhost' (using password: NO)'
  ==> default: Error: mysqladmin -u root password root returned 1 instead of one of [0]
  ==> default: Error: /Stage[main]/Mysql/Exec[set-mysql-password]/returns: change from notrun to 0 failed: mysqladmin -u root password root returned 1 instead of one of [0]
  ==> default: Notice: /Stage[main]/Phpmyadmin/Exec[load_phpmyadmin_conf]/returns: executed successfully
  ==> default: Notice: /Stage[main]/Phpmyadmin/Exec[reload_apache]/returns: executed successfully
  ==> default: Notice: /Stage[main]/Phpmyadmin/Exec[reload_apache]: Triggered 'refresh' from 1 events
  ==> default: Notice: Finished catalog run in 4.00 seconds
  The SSH command responded with a non-zero exit status. Vagrant
  assumes that this means the command failed. The output for this command
  should be in the log above. Please read the output to determine what
  went wrong.
  ```

  Ignore the SSH error for now

7. Run vagrant ssh and you should something along the lines of the below:

  ```
  C:\nadsautomation>vagrant ssh
  Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-95-generic x86_64)

   * Documentation:  https://help.ubuntu.com/

    System information as of Sun Sep 18 17:16:20 UTC 2016

    System load:  0.24              Processes:           99
    Usage of /:   4.4% of 39.34GB   Users logged in:     0
    Memory usage: 21%               IP address for eth0: 10.0.2.15
    Swap usage:   0%                IP address for eth1: 172.16.1.10

    Graph this data and manage this system at:
      https://landscape.canonical.com/

    Get cloud support with Ubuntu Advantage Cloud Guest:
      http://www.ubuntu.com/business/services/cloud

  New release '16.04.1 LTS' available.
  Run 'do-release-upgrade' to upgrade to it.


  Last login: Sun Sep 18 13:47:13 2016 from 10.0.2.2
  vagrant@vagrant-ubuntu-trusty-64:~$
  ```

8. Copy the Linux NADs scripts into the folder scripts


Troubleshooting
--
```
C:\nadsautomation>vagrant ssh
`ssh` executable not found in any directories in the %PATH% variable. Is an
SSH client installed? Try installing Cygwin, MinGW or Git, all of which
contain an SSH client. Or use your favorite SSH client with the following
authentication information shown below:

Host: 127.0.0.1
Port: 2222
Username: vagrant
Private key: C:/Users/sbrooks/.vagrant.d/boxes/unzagi-VAGRANTSLASH-ubuntu/0.1/virtualbox/vagrant_private_key
```

http://stackoverflow.com/questions/27768821/ssh-executable-not-found-in-any-directories-in-the-path


System Properties > Environment Variables > Add Add C:\Program Files\Git\usr\bin to the PATH environment variable.

Please refer to Vagrant Docs
Please refer to Oracle Virtualbox

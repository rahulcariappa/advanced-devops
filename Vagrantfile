# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.


  config.vm.box = "hashicorp/bionic64"


  config.vm.define "redisdev"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "redisdev"
    vb.gui = true
  end

  config.vm.synced_folder "/Users/rcheyand/AdvDevOps/advanced-devops/", "/home/vagrant", disabled: false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:9001" will access port 6379 on the guest machine.
  # NOTE: This will enable public access to the opened por
  config.vm.network "forwarded_port", guest: 6379, host: 9001
  #, host_ip: "127.0.0.1"


  # Enter the list of shell commands sequentially that need to be executed on the Guest instance which gets launched
  # using command: vagrant up
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y redis
    systemctl status redis
    redis-cli
    SHELL

  # Check the output of vagrant global-status to see the nodes and thier statuses
  # To destroy a node type in command: vagrant destroy 1a2b3c [vagrant destroy id]

end






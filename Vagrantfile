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

  config.vm.provider "virtualbox" do |vb|
    vb.name = "redisdev"
    vb.gui = true
  end

  config.vm.synced_folder "/Users/rcheyand/AdvDevOps/advanced-devops/", "/home/vagrant", disabled: true

  config.vm.network "forwarded_port", guest: 6379, host: 9001, host_ip: "127.0.0.1"


  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y redis
    redis-cli --version
    export DEBIAN_FRONTEND=noninteractive
    redis-server $HOME/redis.conf
    systemctl status redis
    SHELL

  # redis-server --port 7777 --slaveof 127.0.0.1 9001

  # config.vm.box = "adigiovanni/redis"
  # config.vm.box_version = "4.0.2"
end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 9001

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"







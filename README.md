# advanced-devops
This repo will let you clone a development environment in your local machine

# Clone this repo: In order to successfully clone and use this repo please execute the below commands:

git clone git@github.com:rahulcariappa/advanced-devops.git

cd advanced-devops

git branch master

git checkout master

git fetch origin master

git reset --hard origin/master

# Usage: Be sure to source the virtual environment within the repo directory

## For Linux based machines 
source vagrantenv/bin/activate # Source the virtual envrionment within this repo

## For Windows
source vagrantenv/Scripts/activate.bat

# Setup - to instantiate the Development Vagrant instance in your local machine, you can just call 'make' too
make setup

# Clean - to destroy the Development Vagrant instance in your local machine
make clean

# To kick start the instantiation of the Development Vagrant instance in your local machine in case make fails
python redis-server.py --redis_repo_path "/your/path/redis-repo"

# Commands that are helpful:
vagrant ssh redisdev - to SSH into the redisdev instance;
vagrant global-status - to view the list of instances running;
vagrant destroy id - to destroy the instance, id available in the output of command: vagrant global-status;
redis-cli -h 127.0.0.1 -p 9001  - to connect to the redis server from your host with port 9001 acting as port forwarding to the redisdev instance;

Note: If you cannot find the vagrantenv file, it might be found in .gitignore folder

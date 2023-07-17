# advanced-devops
This repo will let you clone a development environment in your local machine

# Clone this repo: In order to successfully clone and use this repo please execute the below commands:

git clone git@github.com:rahulcariappa/advanced-devops.git

cd advanced-devops

git branch master

git checkout master

git fetch origin master

git reset --hard origin/master

# Usage: Be sure to execute the source commands below in the repo directory

## For Linux based machines 
source vagrantenv/bin/activate # Source the virtual envrionment within this repo

## For Windows
source vagrantenv/Scripts/activate.bat

# Setup - to instantiate the Development Vagrant instance in your local machine
make setup

# Clean - to destroy the Development Vagrant instance in your local machine
make clean

# To kick start the instantiation of the Development Vagrant instance in your local machine
python redis-server.py --redis_repo_path "/your/path/redis-repo"

Note: If you cannot find the vagrantenv file, it might be found in .gitignore folder

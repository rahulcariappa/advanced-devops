# advanced-devops
This repo will let you clone a development environment in your local machine

# Clone this repo: In order to successfully clone and use this repo please execute the below commands:

git clone git@github.com:rahulcariappa/advanced-devops.git

cd advanced-devops

git branch master

git checkout master

git fetch origin master

git reset --hard origin/master

# Usage: be sure to execute the source commands below in the repo directory

# For Linux based machines 
source vagrantenv/bin/activate # Source the virtual envrionment within this repo

# For Windows
source vagrantenv/Scripts/activate.bat

# Make - to begin the Development vagrant instance
make setup

# To kill the Vagrant Instance and perform cleanup
make clean

# If you cannot find the vagrantenv file, it might be found in .gitignore folder
python3 redis-server.py --redis_repo_path "/your/path/redis-repo"

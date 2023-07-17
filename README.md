# advanced-devops
This repo will serve as the directory for all current and future activities

# Clone this repo:

In order to use this repo please execute the below commands:

git clone git@github.com:rahulcariappa/advanced-devops.git

cd advanced-devops

git branch master

git checkout master

git fetch origin master

git reset --hard origin/master

# Usage:
# For Linux
source vagrantenv/bin/activate # Source the virtual envrionment within this repo
# For Windows
source vagrantenv/Scripts/activate.bat
# If you cannot find the vagrantenv file, it might be found in .gitignore folder
python3 redis-server.py --redis_repo_path "/your/path/redis-repo"

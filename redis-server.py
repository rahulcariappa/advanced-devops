#!/usr/local/bin/python
import argparse
import os
from pip._vendor.requests.compat import str
# import vagrant

vagrantfile = os.path.join(os.getcwd(), "Vagrantfile")

def vagrant_up(redis_repo=""):
    os.system("vagrant up")
    return

def launch_vagrant_instance():
    vagrant_instance = vagrant.Vagrant(vagrantfile)
    vagrant_instance.up()
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kickstart redis-server service on a guest VM, '
                                                 'whose configuration is maintained in a Vagrantfile')
    parser.add_argument('--redis_repo_path', action='store', type=str, help='absolute path of the redis-server repo')
    args = parser.parse_args()
    redis_repo_path = ""
    # print(args)
    if args.redis_repo_path:
        redis_repo_path = args.redis_repo_path
    vagrant_up(redis_repo_path)

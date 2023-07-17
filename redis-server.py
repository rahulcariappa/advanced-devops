#!/usr/bin/env python3
import argparse
from pip._vendor.requests.compat import str
import os


def vagrant_up(redis_repo=""):
    os.system("vagrant up")
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
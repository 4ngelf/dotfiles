#!/bin/env python3
# Checks whether the owner of a repository is myself or a thirdparty
# Use: repo_owner.py <user> <args>
# Returns: 'personal' if user is user in address else 'third'

import sys
import re

def get_ssh_or_http_address(iterable: iter) -> str:
    ssh_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+:.+$" 
    http_regex = r"^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?$"

    for elm in iterable:
        is_ssh = re.match(ssh_regex, elm)
        is_http = re.match(http_regex, elm)

        if is_ssh or is_http:
            return elm
        
    return ""

def get_user_from_address(address: str) -> str:
    user_regex = r"(?::|\/)([A-za-z0-9-]+)\/.+\.git"
    user = re.search(user_regex, address)[1]

    return user or ""

def main():
    user = sys.argv[1]
    args = sys.argv[2:]
     
    if len(args) == 0:
        sys.exit(1)

    address = get_ssh_or_http_address(args)
    repo_user = get_user_from_address(address)

    if user == repo_user:
        print("personal")
    else:
        print("third")

if __name__ == "__main__":
    main()


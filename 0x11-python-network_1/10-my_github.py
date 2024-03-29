#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    authn = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=authn)
    print(req.json().get("id"))

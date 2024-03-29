#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve
this challenge with the following requirements.
-The first argument will be the repository name
-The second argument will be the owner name
-You must use the packages requests and sys
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'
    req = requests.get(url.format(argv[2], argv[1]))
    new_commits = req.json()
    for commit in new_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

#!/usr/bin/python3
"""Displays the 10 most recent commits"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    resp = requests.get(url)
    commits = resp.json()[:10]
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))

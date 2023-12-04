#!/usr/bin/python3
"""Takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"

    username = sys.argv[1]
    password = sys.argv[2]

    with requests.Session() as session:
        session.auth = (username, password)
        resp = session.get(url)

    try:
        print('{}'.format(resp.json()['id']))
    except:
        print("None")

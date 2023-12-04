#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io from cli"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        req_id = response.getheader('X-Request-Id')
        if req_id:
            print(req_id)

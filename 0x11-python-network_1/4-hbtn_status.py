#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""  
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    resp = requests.get(url)
    status = resp.text

    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))

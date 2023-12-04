#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    content = resp.text
    print("Body response:")
    print("\t- type: ", type(content))
    print("\t- content: ", content)


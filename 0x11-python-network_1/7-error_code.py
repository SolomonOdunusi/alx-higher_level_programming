#!/usr/bin/python3
"""Displays the body of the response"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1] 
    resp = requests.get(url)
    if resp.status_code >= 400:
        print('Error code: {}'.format(resp.status_code))
    else:
        print(resp.text)

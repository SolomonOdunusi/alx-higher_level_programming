#!/usr/bin/python3
"""Displays the request id from the header"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    resp = requests.get(url)
    x_request_id = resp.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)

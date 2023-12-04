#!/usr/bin/python3
""" Module that takes in a letter
and sends a POST request
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    req = requests.post(url, values)
    try:
        if (len(req.json()) > 0):
            print('[{}] {}'.format(req.json()['id'], req.json()['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

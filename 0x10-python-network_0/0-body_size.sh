#!/usr/bash
# A script that takes a URL and
# displays size of the body of the resp
curl -sI "$1" | grep Content-Length | awk '{print $2}'

#!/bin/bash
# Script that sends a req to a URL -> arg and displays status code
curl -s -o /dev/null -w "%{http_code}" "$1"

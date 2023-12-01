#!/bin/bash
# JSON POST req to UEL as first arg
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

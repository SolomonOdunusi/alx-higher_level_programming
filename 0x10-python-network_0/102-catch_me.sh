#!/bin/bash
# Makes a req to 0.0.0.0:5000/catch_me
curl -s -X POST -d "user_id=42&status=You%20got%20me%21" http://0.0.0.0:5000/catch_me

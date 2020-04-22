#!/bin/bash
# Bash script that displays the body of the response.
curl -sX POST -H "Content-type: application/json" -d @"$2" "$1"

#!/bin/bash
# Bash script that displays only the status code of the response.
curl -sLI "$1" -o /dev/null -w '%{http_code}'

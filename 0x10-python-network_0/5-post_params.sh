#!/bin/bash
# Show the result of a POST request with some parameters.
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" | cat

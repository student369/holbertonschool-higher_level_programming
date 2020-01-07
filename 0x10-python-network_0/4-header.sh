#!/bin/bash
# Show the response of a get request with a header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98;" "$1" | cat

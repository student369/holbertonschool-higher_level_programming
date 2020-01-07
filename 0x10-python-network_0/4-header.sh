#!/bin/bash
# Show the response of a get request with a header
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98" | cat

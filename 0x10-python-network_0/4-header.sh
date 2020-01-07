#!/bin/bash
# Show the response of a get request with a header
curl "$1" -X GET -H "X-HolbertonSchool-User-Id: 98" | cat

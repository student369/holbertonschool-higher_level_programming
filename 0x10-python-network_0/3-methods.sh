#!/bin/bash
# Show the methods supported by the server
curl -s -X OPTIONS "$1" | cat

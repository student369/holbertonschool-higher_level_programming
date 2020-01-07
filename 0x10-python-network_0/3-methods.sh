#!/bin/bash
# Show the methods supported by the server
curl -s -i -X OPTIONS "$1" | grep Allow | cut -c8-

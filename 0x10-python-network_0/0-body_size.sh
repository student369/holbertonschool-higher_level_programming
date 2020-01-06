#!/bin/bash
# Get a resource and show the length
curl -s "$1" | wc -c

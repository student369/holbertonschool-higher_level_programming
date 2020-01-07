#!/bin/bash
# Use the method DELETE in the URL and show the response body
curl -s -X DELETE "$1" | cat

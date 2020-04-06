#!/bin/bash
# Display the body of the response when post a json file
curl -X POST -H "Content-Type: application/json" -d @$2 $1

#!/bin/bash
# Display the Allow variable header after Option request
curl -sI -X OPTIONS $1 | grep -i Allow | cut --complement -d ' ' -f 1 

#!/bin/bash
# Display the size of body of the response in bytes
curl -sI $1 | grep -i Content-Length | awk '{print $2}'

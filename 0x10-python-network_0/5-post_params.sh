#!/bin/bash
# Display the body after sent a header variable and GET request
curl -X POST -L $1 -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'

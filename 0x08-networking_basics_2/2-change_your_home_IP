#!/usr/bin/env bash
# Change your home IP
cp /etc/hosts ~/hosts.new
sed -i 's/^127.0.0.1.*/127.0.0.2 localhost/g' ~/hosts.new
echo "8.8.8.8 facebook.com" >> ~/hosts.new
cp -f ~/hosts.new /etc/hosts

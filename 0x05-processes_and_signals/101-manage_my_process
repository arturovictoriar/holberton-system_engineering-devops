#!/usr/bin/env bash
# This script is displaying "Holberton School" 10 times
if [ "$#" -ne 1 ]
then
    echo "Usage: manage_my_process {start|stop|restart}"
    exit $?
fi

if [ "$1" != "start" ] && [ "$1" != "stop" ] && [ "$1" != "restart" ]
then
    echo "Usage: manage_my_process {start|stop|restart}"
    exit $?
fi

if [ "$1" == "start" ]
then
    ./manage_my_process &
    echo "$!" > /var/run/my_process.pid
    echo "manage_my_process started"

elif [ "$1" == "stop" ]
then
    kill "$(cat /var/run/my_process.pid)"
    rm /var/run/my_process.pid
    echo "manage_my_process stopped"

elif [ "$1" == "restart" ]
then
    kill "$(cat /var/run/my_process.pid)"
    rm /var/run/my_process.pid
    ./manage_my_process &
    echo "$!" > /var/run/my_process.pid
    echo "manage_my_process restarted"

fi

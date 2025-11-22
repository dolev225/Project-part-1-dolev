#!/bin/bash

#error stop
set -e 

echo " installating Nginx "

#check update
if ! sudo apt update;
then
    echo "failed to update package list"
    exit 1
fi

#check instalion
if ! sudo apt install -y nginx;
then
    echo "failed to install Nginx"
    exit 1
fi

#check if prosses enable
if ! sudo systemctl enable nginx;
then
    echo "failed to enable Nginx"
    exit 1
fi

if ! sudo systemctl start nginx;
then
    echo "failed to start Nginx"
    exit 1
fi

echo "nginx is running "
exit 0

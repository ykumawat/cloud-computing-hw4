#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt-get install -y python3-pip
pip3 install --upgrade flask

# download the code
wget http://storm.cis.fordham.edu/ji/cisc5550cloud/hw4/todolist_api.py
wget http://storm.cis.fordham.edu/ji/cisc5550cloud/hw4/todolist.db

python3 todolist_api.py

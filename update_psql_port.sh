#!/bin/bash

PORT_PSQL=${1:-"5437"}
PORT_SITE=${2:-"8000"}
PROJECT_NAME=${3:-"ServerChecker"}

sudo sed -i "s/port = [[:digit:]]*/port = ${PORT_PSQL}/" /etc/postgresql/12/main/postgresql.conf
sed -i "s/'PORT': '[[:digit:]]*'\,/'PORT': '${PORT_PSQL}'\,/" ${PROJECT_NAME}/settings.py
sudo service postgresql restart

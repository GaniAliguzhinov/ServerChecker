#!/bin/bash

PORT_PSQL=${1:-"5437"}
PORT_SITE=${2:-"8000"}
PROJECT_NAME=${3:-"urlchecker"}

# Install pip, postgres, nginx
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

# Run postgres
sudo service postgresql restart

# Create db for website
sudo -u postgres psql -U postgres postgres -f db_create.sql

# Create virtualenv
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
virtualenv venv

# Install packages inside virtualenv
source venv/bin/activate
pip install -r requirements.txt

sudo ufw allow ${PORT_SITE}

# python testsite/manage.py runserver 0.0.0.0:${PORT_SITE}

# gunicorn --bind 0.0.0.0:8000 testsite.wsgi

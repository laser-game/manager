#!/bin/sh
# create and install python enviroment
# wykys 2018

echo "remove old venv"
rm .venv -rf

echo "create new venv"
python3 -m venv .venv

echo "activate venv"
. .venv/bin/activate

echo "upgrade pip"
pip install --upgrade pip

echo "install modules from requirements"
pip install -r requirements.txt

echo "installed modules"
pip freeze

echo "migrated - created tables in database"
python manage.py migrate

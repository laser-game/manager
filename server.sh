#!/bin/sh
# actavated venv ans run django server
# wykys 2018

echo "activate venv"
. .venv/bin/activate

python lgm/manage.py runserver

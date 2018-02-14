#!/bin/sh
# created and init databese
# wykys 2018

echo "activate venv"
. .venv/bin/activate

cd lgm
rm db.sqlite3 db.sqlite3_old -f
mv db.sqlite3 db.sqlite3_old
mv core/migrations/0002_initial_data.py ./
./manage.py migrate
./manage.py makemigrations
mv 0002_initial_data.py core/migrations
./manage.py migrate
./manage.py createsuperuser

#!/usr/bin/env bash
# wait until postgres up
/wait-for-it.sh postgres:5432

cd simple_site_requester

python manage.py makemigrations ssr_api
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

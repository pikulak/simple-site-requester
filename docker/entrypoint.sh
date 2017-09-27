#!/bin/bash
set -eo pipefail

# check requirements.txt everytime container stars,
# it allows you to dynamically edit requirements.txt without rebuilding image
pip install -r requirements.txt

# wait until postgres up
/wait-for-it.sh postgres:5432
python simple_site_requester/manage.py makemigrations
python simple_site_requester/manage.py migrate

exec "$@"
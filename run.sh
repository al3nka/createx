#!/bin/bash

set -e

python manage.py makemigrations --noinput
python manage.py migrate --noinput

if [ "$CREATE_SUPERUSER" == "true" ]; then
  python manage.py createsuperuser --noinput
fi

python manage.py collectstatic --clear --noinput
cp -r ../static/admin static/
uwsgi --ini uwsgi.ini
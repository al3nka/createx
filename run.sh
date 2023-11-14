#!/bin/bash

set -e

python manage.py makemigrations --noinput
python manage.py migrate --noinput

if [ -z "$DJANGO_SUPERUSER_USERNAME" ]; then
  export DJANGO_SUPERUSER_USERNAME=admin
fi
if [ -z "$DJANGO_SUPERUSER_EMAIL" ]; then
  export DJANGO_SUPERUSER_EMAIL=admin@email.com
fi
if [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py createsuperuser --noinput
fi

python manage.py collectstatic --clear --noinput
uwsgi --ini uwsgi.ini
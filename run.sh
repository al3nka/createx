#!/bin/bash

python manage.py migrate --noinput
if [ -z "$DJANGO_SUPERUSER_USERNAME" ]; then
  export DJANGO_SUPERUSER_USERNAME=admin
fi
if [ -z "$DJANGO_SUPERUSER_EMAIL" ]; then
  export DJANGO_SUPERUSER_EMAIL=admin@email.com
fi
python manage.py createsuperuser --noinput

python manage.py collectstatic --clear --noinput
gunicorn createx.wsgi:application --bind 0.0.0.0:8000

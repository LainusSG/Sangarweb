#!/bin/sh

echo 'Running collectsatic...'
python manage.py collectstatic --no-input --settings=backendbarber.settings.production


echo 'apliying migrations...'
python manage.py wait_for_db --settings=backendbarber.settings
python manage.py migrate --settings=backendbarber.settings
python manage.py migrate --run-syncdb --settings=backendbarber.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=core.settings core.wsgi:application --bind 0.0.0.0:8000
#!/bin/bash

# Exit if any command fails
set -e

# Run migrations (make sure the database is created and up to date)
# python manage.py migrate --noinput

# Start Gunicorn server (exec replaces the shell with gunicorn, allowing it to take control of the process)
exec gunicorn jobapp.wsgi:application --bind=0.0.0.0:$PORT
#!/bin/sh

# python3 manage.py makemigrations --no-input
python3 manage.py migrate
gunicorn --workers=2 --timeout 3000 favorites.wsgi --log-level=debug -b 0.0.0.0:8000 --preload
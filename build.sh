#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py seed_products
# Creates an admin on first deploy if DJANGO_SUPERUSER_USERNAME/EMAIL/PASSWORD are set
python manage.py createsuperuser --no-input || true

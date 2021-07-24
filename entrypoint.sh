#!/bin/sh -x
cd app

echo
python manage.py wait_for_db
echo "Run migrations"
python manage.py migrate

exec "$@"

#!/bin/sh -x
cd app

echo
echo "Run migrations"
python manage.py migrate

exec "$@"

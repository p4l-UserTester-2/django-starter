#!/bin/bash
# wait-for-postgres.sh

set -e

cmd="$@"

until psql postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/${DB_NAME} -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
python manage.py migrate 
exec python manage.py runserver 0.0.0.0:8000

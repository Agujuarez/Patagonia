#!/bin/bash
set -e

echo "Aplicando migraciones..."
python manage.py migrate

echo "Ejecutando seed de tenants..."
python manage.py shell -c "from tenants.seed import run; run()"

echo "Compilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Arrancando el servidor..."
python manage.py runserver 0.0.0.0:8000
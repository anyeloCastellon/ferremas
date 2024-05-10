#!/bin/bash
source ambiente_desarrollo_virtual/bin/activate

python3 manage.py makemigrations
python3 manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '123456')" | python3 manage.py shell
python3 manage.py runserver 0.0.0.0:8000
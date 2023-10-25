
export ATN_PROD='True'
export ATN_DB_ENGINE='django.db.backends.postgresql_psycopg2'
export ATN_DB='postgres'
export ATN_DB_USER='postgres'
export ATN_DB_PASSWD='postgres'
export ATN_DB_HOST='172.21.21.12'
export ATN_DB_PORT='5432'

sudo docker-compose -f docker-compose.qa.yml up --build -d db_eps pgadmin
python3 manage.py makemigrations
python3 manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', '123456')" | python3 manage.py shell
python3 manage.py runserver 0.0.0.0:8000


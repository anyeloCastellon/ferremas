
sudo docker network create reverseproxy-nw

echo "STARING COMPOSE UP"
sudo docker-compose -f docker-compose.prod.yml up -d --build
echo "COMPOSE DONE end"


echo "REGISTERING CRON 1 Start"
sudo docker-compose -f docker-compose.prod.yml exec backend service cron start
echo "REGISTERING CRON 2 add"
sudo docker-compose -f docker-compose.prod.yml exec backend python3 manage.py crontab add
echo "REGISTERING CRON 3 Finished"


echo "Migrating Start"
sudo docker-compose -f docker-compose.prod.yml exec backend python3 manage.py migrate
sudo docker-compose -f docker-compose.prod.yml exec backend python3 manage.py makemigrations
echo "Migrating End"


echo "COLLECT STATIC"
sudo docker-compose -f docker-compose.prod.yml exec backend python3 manage.py collectstatic --noinput --clear
echo "COLLECT STATIC end"
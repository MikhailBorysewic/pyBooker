# Run project
These step suppose you have docker-compose installed.
```commandline
docker-compose build
docker-compose up
```
# Run migrations
```commandline
docker exec blogapp_web_1 python manage.py migrate --noinput
```
where `blogapp_web_1` app container name, you can use container name or container ID.

Open http://127.0.0.1:8000/ in your browser.
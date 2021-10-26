# weather_data_api

## dependencies

 - redis-server
 - docker

## running

 - Start the celery app:

    [celery -A weather_app worker -l info]

 - Start the project:

    [docker-compose up]

## environment

 - Set project:

    [export DJANGO_SETTINGS_MODULE=weathr_app.settings]
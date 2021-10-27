# weather_data_api

## dependencies

 - redis-server
 - docker

## running with container

 - Build the container:

   $ docker-compose build

 - Start service:

    $ docker-compose up

 - Swagger API access:

    http://0.0.0.0:8000/api-docs/


## running with local env

  - Build local env

    $ make create-venv

  - Run the celery-beat

    $ celery -A weather_app beat -l info
   
  - Run the celery worker

    $ celery -A weather_app worker --loglevel=info

  - Swagger API access:

    http://0.0.0.0:8000/api-docs/


## environment

 - Set project:

    [export DJANGO_SETTINGS_MODULE=weathr_app.settings]
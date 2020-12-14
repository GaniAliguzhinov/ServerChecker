# ServerChecker
Django based web service for checking remote servers for availability.

Celery: [tutorial](https://testdriven.io/blog/django-and-celery/)


# Deployment

To deploy on Ubuntu with configured `ufw` that allows connections on desired port:

* Clone the project

* `./init.sh`

* `./update_psql_port.sh`

* `source venv/bin/activate`

* `./manage.py makemigrations` and `./manage.py migrate`

* `./manage.py createsuperuser`

* In one console, run `./start_celery`, or setup a cron job.

* In another console, run `redis-server`

* In another console, run server: `./manage.py runserver 0.0.0.0:<desired_port>`


# Usage

Once deployed, the initial Excel sheet can be uploaded via `localhost:8000/sheets/`. 
Results can be viewed by refreshing `localhost:8000/queries/`.

It will then be processed: all urls in the sheet will be queried, results visible on `localhost:8000/admin/`.

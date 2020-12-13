# ServerChecker
Django based web service for checking remote servers for availability.


# Deployment

To deploy on Ubuntu with configured `ufw` that allows connections on desired port:

1. Clone the project

2. Install python3 and pip3

3. `pip install -r requirements.txt`

4. `./manage.py makemigrations` and `./manage.py migrate`

5. `./manage.py createsuperuser`

6. `./manage.py runserver 0.0.0.0:<desired_port>`

To use a database other than SQLite, configure `DATABASES` in `ServerChecker/settings.py`.


# Usage

Once deployed, the initial Excel sheet can be uploaded via `localhost:8000/sheets/`. 

It will then be processed: all urls in the sheet will be queried, results visible on `localhost:8000/admin/`.

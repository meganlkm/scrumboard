scrumboard
==========

## Installation:

#### via git

````
git clone https://github.com/meganlkm/scrumboard.git
cd scrumboard
````

#### environment variables

````
export DJANGO_SETTINGS_MODULE="scrumboard.settings.local"
````

#### install requirements

````
pip install -r requirements.txt
````

#### install schema

````
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
````

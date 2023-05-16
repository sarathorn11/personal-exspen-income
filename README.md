# personal-exspen-income

python3 -m venv env

. env/bin/activate

pip3 install Django

django-admin startproject exspens .

python manage.py runserver

python manage.py migrate

python manage.py runserver | python manage.py runserver port
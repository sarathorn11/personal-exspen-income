# personal-exspen-income
-->create venv
python3 -m venv env
--> activate venv
. env/bin/activate
--> install django
pip3 install Django
--> create app 
django-admin startproject exspens .
-->run project
python manage.py runserver
--> migrate project
python manage.py migrate

python manage.py runserver | python manage.py runserver port


--> create superuser
python manage.py createsuperuser

--> create templet home
python manage.py startapp home

-->migrate someting updates
python manage.py makemigrations
python manage.py migrate


# personal-exspen-income
-->create venv <br />   
python3 -m venv env
--> activate venv<br />  
. env/bin/activate
--> install django<br />  
pip3 install Django
--> create app <br />  
django-admin startproject exspens .
-->run project<br />  
python manage.py runserver
--> migrate project<br />  
python manage.py migrate

python manage.py runserver | python manage.py runserver port


--> create superuser<br />  
python manage.py createsuperuser

--> create templet home<br />  
python manage.py startapp home

-->migrate something updates<br />  
python manage.py makemigrations
python manage.py migrate


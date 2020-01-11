pip install django
django-admin startproject iniciando_django3
python manage.py runserver
python manage.py runserver 0.0.0.0:8000
python manage.py migrate
python3 manage.py createsuperuser

#em um msm projeto djando posso ter varios modulos/apps

djando-admin startapp my_app

#criando migration para uma app instalada
python3 manage.py makemigrations my_app
python3 manage.py sqlmigrate my_app 0001
python3 manage.py shwmigrations

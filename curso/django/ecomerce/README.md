/Documentos/pythonc/curso/django/ecomerce$ 

# ambiente virtual

python3 -m venv venv
source venv/bin/activate
python manage.py runserver

# django

pip install django
pip install django-crispy-forms
pip install pillow

# inicio do projeto

django-admin startproject loja .
python manage.py migrate
python manage.py createsuperuser

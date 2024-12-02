python3 -m venv venv

source ambvirtual/bin/activate
pip install django
django-admin startproject project 'nome-project'
python manage.py runserver


git config --global user.name 'Seu nome'
git config --global user.email 'Seu email'
git config --global init.defaultBranch main
git init 
git add . 
git commit -m "mensagem"

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py createsuperuser
python3 manage.py changepassword USERNAME

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
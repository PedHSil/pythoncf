python3 -m venv venv

source ambvirtual/bin/activate
pip install django
django-admin startproject project 'nome-project'

git config --global user.name 'Seu nome'
git config --global user.email 'Seu email'
git config --global init.defaultBranch main
git init 
git add . 
git commit -m "mensagem"
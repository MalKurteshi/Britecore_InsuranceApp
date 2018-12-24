# FrontEnd

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

npm install axios

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

For detailed explanation on how things work, consult the [docs for vue-loader](http://vuejs.github.io/vue-loader).

# Backend

> A Django project 

# install Python then pip and Django 

python get-pip.py
pip install -e django/

For detailed explanation on how things work, consult the [docs for Django Instalation](https://docs.djangoproject.com/en/2.1/topics/install/).  

## Build Setup

``` bash
# install dependencies

npm install --save-dev webpack-bundle-tracker

pip install django-webpack-loader

pip install djangorestframework

pip install django-cors-headers

pip install django-rest-auth

pip install django-staticfiles

pip install django-messages

pip install django-sessions

pip install django-contenttypes

pip install django-auth0-auth

pip install django-admin

# start the django project 
python manage.py runserver
```

# Configure the Application

## First start the Front end Project

cd FrontEnd

npm run dev 

OR

npm run build

## Then start the Django Backend Project

python manage.py runserver

If any migration needed 

python manage.py makemigrations Backend

python manage.py sqlmigrate XXXX(Last verstion) Backend

python manage.py migrate

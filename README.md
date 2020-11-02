# dbwares-django-project

#### This is a try project incorporating the basics of Django routing, templating and simple model manipulation

## Cheat Sheet

1. Create a virtual environment


`$ virtualenv virtual-env-name`


2. Install Django


`$ pip install Django[==version_name]`


3. If pip not found : goto the following address C:\Python39\Scripts and write the following command


`$ easy_install pip`


4. Create Django Project


`$ django-admin startproject project_name`


5. Create a Django app


`$ python manage.py startapp app_name`


## Connect to mysql database

1. Run Xampp and create a Database



2. In the **settings.py** file remove the default and add the following


```python
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'name_of_db',
'USER': 'root',
'PASSWORD': "",
'HOST': "",
'PORT': "",
'OPTIONS': {
'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
 }
   }
      }
```

3. Install the **mysqlclient** using pip

`$ pip install mysqlclient[==version_number]`

4. If any problem: install mysqlclient whl file manaully 


`$ pip install path\mysqlclient-1.4.6-cp39-cp39-win_amd64.whl`

5. Create a superuser

`$ python manage.py createsuperuser`


6. Create data models in **models.py**

7. Run the following commands
```python
$ python manage.py makemigrations
$ python manage.py migrate
```

8. Add the migration to the admin panel
 * In the **admin.py** file add the following code
 ```python
 from django.contrib import admin

 from .models import Name_of_model1, Name_of_model2, 

 admin.site.register(Name_of_model1, Name_of_model2)
 
 ```


# TODO
 #### Create a separate app and join the app to a SQL database
 #### Create a simple CRUD application
 

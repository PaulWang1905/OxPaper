# OxPaper
## Run server:

## 1. create the .env file and setting.ini

### .env

SECRET_KEY = 

### setting.ini

```
[Default]
blogName = thisTestBlog
welcomeWord = hello, this is a test blog
```

## 2. run the server

```
python manage.py migrate
```
### set the admin user name and password

```
python manage.py createsuperuser
```

```
python manage.py runserver
```
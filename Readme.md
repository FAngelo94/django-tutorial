# Django tutorial

List of example application where django is used:

- **firstsite**: Application done following Django guide for learning: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
- **django-react-auth**: Example of how to use an authentication system with django and react folllowing this guide: https://blog.devgenius.io/django-rest-framework-react-authentication-workflow-2022-part-2-d299b7fef875
- **django-todo-react**: Example of how to use django and react to create a todo list, to improve the project I followed this documentation: https://www.django-rest-framework.org/tutorial/3-class-based-views/
- **docker-compose-django-react**: Application that use 4 docker container to run 1 Django server, 1 react application, 1 db mysql and 1 phpmyadmin (in order to interact with the DB using an UI)
- **django-rest-swagger**: Example, not fully tested, about how to use swagger for django API

## Commands
Every commands start with **python manage.py**, then:
- **startproject <name>** create project in folder with the same name passed. A project can contains multiple apps
- **startapp <name>** create an app in folder with same name passed. An app can be included in different progects
- **shell** open interactive Python shell and play around with the free API Django gives you
- **createsuperuser** create a user who can login to the admin site in order to access to Django Admin section
- **runserver <port (default: 8000)>** command starts the development server. Add */admin/* to the url to navigate to admin section
- **test <name_folder_app (default: all)>** command to execute all test in a folder or in the entire project

### Commands for DB
- **migrate**  is responsible for *applying* and unapplying migrations. We create tables in the database for each applications in *INSTALLED_APPS* that needs a table
- **makemigrations <folder>** is responsible for *creating* new migrations based on the changes you have made to your models. We can use this commands before run migrate
- **sqlmigrate <folder> <version>** displays the SQL statements for a migration.

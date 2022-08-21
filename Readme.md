# Django tutorial

Application done following Django guide for learning: https://docs.djangoproject.com/en/4.1/intro/tutorial01/

## Commands
Every commands start with **python manage.py runserver**, then:
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

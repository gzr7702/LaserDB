#The Laser Database

This is a database to track the Service Order forms completed in the field by engineers
who are repairing lasers. It also tracks the parts that they use for the repairs.

##Dependencies: 

Python 3.4 
Django 1.8.6
django-formtools 1.0
whoosh 2.7.0
haystack 2.4.1
selenium 2.48.0
chromedriver 2.19
psycopg2
postgresql

##To start the application:

For development, you can run using the Django dev server. CD to the home dir of the project and run:

$ python manage.py runserver

For production, you need to run using a full web server like nginx or apache

##To run the tests:

python3 manage.py test - run all tests
python3 manage.py test service_orders - test back end
python3 manage.py test functional_tests - test front end


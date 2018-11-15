@author  : Santiago Quiroga Turdera
@version : 1.0


Description
===============
This application is a short and simple REST API for the Problem 1, it contains 2 models (Class and Student) for which 
all CRUD methods are available.


Installation
============
This application requires the following to work properly:

- python 3.6.6
- pip 18.1
- virtualenv 16.0.0

First we create a virutal enviroment

    $ virtualenv --python=python3.6 venv

It is important to work on the virtual enviroment you just created from now on, to do so, type

    $ . venv/bin/activate

After this, it's necessary to install all the dependencies for the app.

    $(venv) pip install -r requirements.txt


Running the application
=======================
Before running the application for the first time it's necessary to setup the database
to do so, type the following command

    $(venv) python manage.py migrate


To launch the application you just have to issue the next command

    $(venv) python manage.py runserver




Testing
=======
To execute all the existing tests, type as follows

    $(venv) python manage.py test


Documentation
=============
It is posible to see a Swagger Documentation for the application (the application must be running) in the next URL
        
        http://127.0.0.1:8000/api/swagger/


TODOs
=====
On the current version is necessary to add 

Test Cases
----------
For **Students** model:

- Create a Student with incomplete information.
- Create two different Students with the exact same information (first_name, last_name).
- Update the information of a determined Student.
- Delete a single Student.
- Register a Student to an existing Class.
- Register a Student to a non existing Class.
- Get a list of all the existing Students.
- Get a list of all the Students that are enrolled to a particular Class.


For **Classes** model:

- Create a Class with incomplete information.
- Create two different Classes with the exact same code.
- Update the information of a determined Class.
- Delete a single Class.
- Get a list of all the existing Classes.
- Get a list of all the Classes that a given Student has taken.
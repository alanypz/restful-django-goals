restful-django-goals
====================

A web application that implements Django Rest Framework to create a model-backed Restful API with token-based authentication.


Requirements
------------
* Python 3.0+
* Django 1.8+

Running
-------

Grab the project.

```
git clone https://github.com/alanypz/restful-django-goals.git
```

(Optional) Create and activate a virtual environment.

```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
```

Install project dependencies.

```
pip install requirements.txt
```

Navigate into the `djangogoals` directory and create a test user. Enter the fields prompted.

```
python3 manage.py createsuperuser
```

Run server.

```
python3 manage.py runserver
```

The server will load on `http://localhost:8000/goals/`. Log in with the newly created user.

To exit the virtual environment:

```
deactivate
```


Testing
-------

The project was created using a test driven development strategy. 

You don't need to launch an instance of the server to run the test cases. To run the test cases in `api/tests.py`:
```
python3 manage.py test
```

References
----------
* Django Rest Framework
	* http://www.django-rest-framework.org

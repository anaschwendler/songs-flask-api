# songs-flask-api

Just another RESTful API for me to study :)

Soon more information on how to run that (I still don't know how to do that, but soon)

We will use [PostgreSQL](https://postgresapp.com/), so be sure to have installed, and running on `5432`.

# autoenv

Install [Autoenv](https://github.com/kennethreitz/autoenv) globally. It helps us to set commands that will run every time we `cd` into our directory.

`pip install autoenv`

# how to run

`flask run`

# resources:
Base article: https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way#toc-create-the-app

Keeping your requirements.txt updated: https://wakatime.com/blog/22-keeping-your-pip-requirements-fresh

# questions

1. What does FlaskAPI does?  
Implementation of the same web browseable APIs that Django REST provide.

2. What does SQLAlchemy does?  
It is a ORM (Object Relational Mapper). An ORM converts the raw SQL data (called querysets) into data we can understand called objects in a process called serialization and vice versa (deserialization).
Translate querysets (raw SQL data) into objects, process: serialization.

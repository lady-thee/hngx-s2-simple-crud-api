# Introduction

This is a simple API that handles CRUD operations **(Create, Read, Update and Delete)**

# Table of Contents:

- [Prerequisites](#prerequisites)



## Prerequisites

- [Python]()
- [Django]()
- [DjangoRestFramework]()
- Pipenv/Pip
- Psycopg2/Psycopg2-binary

## Getting Started

### Installation:

1. **Clone the repository**:
   In the bash or vscode terminal:

    `git clone [https://github.com/lady-thee/hngx-s2-simple-crud-api.git]`

2. Run `pipenv shell` in vscode terminal or any console opened in the directory of the project to activate the virtual environment. 

3. Run `pipenv run pip install -r requirements.txt` to create the requirements and install them. 
5. Run `pipenv run pip freeze > requirements.txt` to install dependencies from Pipfile 
4. Run `py manage.py runserver` or `python manage.py runserver` to start the django server.

There, you're good!


### Configuration

Create a `.env` file in the root directory. 
These are the variables the settings will make use of. In the settings.py cnfigure the settings to read variables in the .env file:

```
from pathlib import Path

import dj_database_url

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

import os


class GeneralSettings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: str
    DATABASE_URL: PostgresDsn

GENERAL_SETTINGS = GeneralSettings()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY","")

DEBUG = GENERAL_SETTINGS.DEBUG

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
```

### Usage of the API

This API is used to perform CRUD operations such as:
**1. CREATE:** To create a new instance (is initialized with the `POST` request)

**2. READ:** To fetch a user details (is initialized with the `GET` request)

**3. UPDATE:** To modify the details of an existing user (is initialized with the `PUT/PATCH` request)

**4. DELETE:** To delete an existing user


# UML DIAGRAM LINK

[https://drawsql.app/teams/the-a-team-9/diagrams/hngx-stage-2]


# SOURCE CODE FOR ACTUAL VIEW

[https://github.com/lady-thee/hngx-s2-simple-crud-api/blob/main/api/views.py]


# HOSTED ON RENDER
*Create*
[https://hngx-s2.onrender.com/api/]

*READ*
[https://hngx-s2.onrender.com/api/read/] <id-of-created-user> or [https://hngx-s2.onrender.com/api/read/] `?name=<name-of-created-user>`  

*UPDATE*
[https://hngx-s2.onrender.com/api/update/]<id-of-created-user>  or [https://hngx-s2.onrender.com/api/read/] `?name=<name-of-created-user>`

*DELETE*
[https://hngx-s2.onrender.com/api/delete/]<id-of-created-user>  or [https://hngx-s2.onrender.com/api/delete/] `?name=<name-of-created-user>`


**Got a problem?**
Raise an issue
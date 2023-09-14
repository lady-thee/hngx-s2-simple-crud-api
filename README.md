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

2. Run `pipenv shell` in vscode terminal or any console opened in the directory of the project. 

## Usage of the API

This API is used to perform CRUD operations such as:
**1. CREATE:** To create a new instance (is initialized with the `POST` request)

**2. READ:** To fetch a user details (is initialized with the `GET` request)

**3. UPDATE:** To modify the details of an existing user (is initialized with the `PUT/PATCH` request)

**4. DELETE:** To delete an existing user


## How to run the API

This is a pretty simple CRUD endpoint so running it is not hard either. First of you have to have
1. A virtual engine/machine such as Pipenv installed
2. Since the project Pipfile has locked the dependencies, you do not need to reinstall. 
This is the reason I chose to use `pipenv` over `pip`

Clone the project using `git clone <project-url>`

Once the project is cloned and django is running. Run `pipenv shell` to activate the virtual environment. Then run: `python manage.py runserver`

To see the url format, [https://github.com/lady-thee/hngx-s2-simple-crud-api.git]



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
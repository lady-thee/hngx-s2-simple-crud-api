# Documentation

This is the overly simplified documentation for this very simple and easy to use CRUD API. I have tried to describe the processes as easily as I can. 

## Standard Formats:

**Requests**: Each CRUD view is modified to handle basic URL routing and also Dynamic Parameter Handling(DPH), which means that each endpoint, except for CREATE, can make request queries using basic routing and query parameters. (FYI, this was the most interesting thing!)

*CREATE* : The request  in the url goes like: `/api/`.The `CREATE` endpoint takes the name, username and email of a request to create a user. When a user data is passed in `json' format like below:
```
{
    "name": "theola",
    "email": "janedoe@gmail.com",
    "username": "tee-tee"
}
```
The `CREATE` endpoint creates a user and returns a `Response` which is a `json` object of values containing the success message, a nested user object which contains the user's id and name and then finally, a status code (which is `HTTP_201_CREATED`).

```
@csrf_exempt
@api_view(['GET', 'POST'])
def createAPIView(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                id = serializer.data.get('id')
                name = serializer.data.get('name')
                res = {
                    'id': id,
                    'name': name,
                }
                return Response({'message':'User successfully created', 'user': res}, status.HTTP_201_CREATED)
            else:
                return Response({'Validation erros': serializer.errors}, status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            raise ValidationError('Serializer not valid', serializer.errors)

```
*Expected results*:

```
HTTP 201 Created
Allow: OPTIONS, POST, GET
Content-Type: application/json
Vary: Accept

{
    "message": "User successfully created",
    "user": {
        "id": 10,
        "name": "Jane Doe"
    }
}
```

If a request is empty or the request is not valid, an `Exception` error is thrown:
```
except Exception as e:
            raise ValidationError('Serializer not valid', serializer.errors)
```

*Serializers* : Serializers are used in this project to validate and parse the requests and the model queries. This is best practice and helps to protect the database from invalid injections. **All endpoints in this project uses serializers to validated database queries.**

The data in the request is serialized and if it is valid, it creates the user successfully. If it is invalid, then it raises the `Exception` above. 



*READ* : The `READ` endpoint makes use of Dynamic Parameter Handling and basic URL query handling. This means a user instance can be retrieved or read using:

`/api/read/<id-of-user>/` or `/api/read?name=Jane Doe`

And of course, you cannot pass numbers if using the Dynamic Handling Parameter format. An error will be raised if anything other than a string is passed in the parameter:

```
@api_view(['GET'])
def readUserAPIViewSearch(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        
        if name is not None and not re.match("^[A-Za-z]+$", name):
                return error_handler('Parameter must be an a string', status.HTTP_400_BAD_REQUEST)

```
When a user is successfully retrieved from the request query, the `READ` endpoint returns a Response object with the user details and a status code `HTTP_200_OK`.

```
 try:
            if name is not None:
                user = Person.objects.filter(name=name).get()
                serializer = PersonSerializer(user, many=False)
                return Response(serializer.data)
               
 except ObjectDoesNotExist:
    return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)
    
```

*Expected results:*

```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "id": 10,
    "name": "Jane Doe",
    "email": "janedoe@gmail.com",
    "username": "janey"
}
```

When a request query does not exist an ObjectionDoesNotExist error returns and a Response object showing the status code and the message is returned.



*UPDATE* : Much like the `READ` endpoint, `UPDATE` uses DPH to retrieve request queries and basic URL parameter querying. The endpoint in both cases queries the database, retrieves a user, serializes the new input and then saves the updated user input.

The request is in a `json` format:

```
{
    "email": "jane@gmail.com",
    "name": "Jane Doe",
    "username": "janey"
}
```

The above format is in a `json` format. The view below handles the updating process

```
 if request.method == 'PUT':
            serializer = UpdateUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success_handler('User details updated successfully!', status.HTTP_200_OK)
            else:
                return Response({'Validation erros': serializer.errors}, status.HTTP_400_BAD_REQUEST)
            
    except ObjectDoesNotExist:
        return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)

```
When a user is successfully updated, the endpoint returns a Response object a success message and a status code `HTTP_200_OK`. 

*Expected result:*

```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "id": 10,
    "name": "Jane Doe",
    "email": "jane@gmail.com",
    "username": "janey"
}
```

When a user is updated, you have to use the updated versions of their names if using the DPH format. *Remember that!*


*DELETE* : The `DELETE` endpoint is pretty much the less stressful part. The request query handling works the same way as `READ` and `UPDATE`. So you can get a user using either the ID or the name in the URL query. 

```
 try:
        user = Person.objects.filter(name=name).get()
        if request.method == 'DELETE':
            user.delete()
            return success_handler('User successfully deleted!', status.HTTP_200_OK)
        
 except ObjectDoesNotExist:
        return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)

```

Once a user is deleted, the endpoint returns a Response object with a status code and a success message that tthe user is deleted.

*Expected results:*

```
HTTP 200 OK
Allow: OPTIONS, GET, DELETE
Content-Type: application/json
Vary: Accept

{
    "message": "User successfully deleted!"
}

```

*That's how it works! Simple right?*


# Limitations AND Assumptions

My major limitation was network. I had initially planned to use Docker for this project but was stumped because of some data issues. Other limitations include:
1. Time: There may not have been enough timw to adeqautely improve this work. 
2. Limited knowledge and access to information: I know this project can be better, but I did the best to my knowledge capabilities. It can still be improved upon.

# How to Deploy On Render

1. First create an account with [https://render.com]
2. Create a `render.yml` file in root folder. 
3. Create a service in the `render.yml` file, inside the file, put the following code:

```
services:
  - type: web
    name: hngxS2
    env: web
    runtime: python
    buildCommand: pipenv install --deploy --ignore-pipfile && pipenv run python manage.py migrate 
    startCommand: "gunicorn config.wsgi:application"
    envVars:
      - key: SECRET_KEY
        generateValue: False
      - key: WEB_CONCURRENCY
        value: 4

```
Let's break down the concepts:
*type*: web: Specifies that this is a web service.

*name*: hng-s1: Sets the name of the service.

*env*: web: Specifies that environment variables are configured under the web section. The project has a .env file for the variables.

*runtime*: python: Indicates that the service runs a Python application.

*buildCommand*: This indicates the base build command for the application.

4. Push the code to GitHub. Render wil deploy from the GitHub repository. 

5. On render dashbord, create a new PostgreSQL database. Fill the form for the database.
6. Link database to project using `dj_database_url`. This can be installed using `pipenv install dj_database_url` . The url is gotten from the PostgreSQL database that was created in the previous step. 

    In the settings.py, change the database settings to include the url from the .env file like this: 
    ```
    DATABASE_URL = os.environ.get("DATABASE_URL")

    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL)
    }
    ```
    This reads the database url directly from the .env file in the root folder. The `GENERAL_SETTINGS.DATABASE_URL` is from a pydantic settings class which was set up from the beginning of the project and at the top of the settings.py file. Like so:

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

    ```

    In the .env file created in the root folder, write the following:

    ```
    SECRET_KEY=+SV8S2ga3SgYMdJN1AOwwdZZoV5v0aM1eJh39yDxEzY=
    ALLOWED_HOSTS=localhost,127.0.0.1
    DEBUG=True

    # database settings
    DATABASE_URL=postgres://hngx2_user:lqytEW47YNocro5zhWpXW2unUklQrVen@dpg-ck13su7dorps73b4acig-a.oregon-postgres.render.com/hngx2   
    ```
    Next, run `py manage.py makemigrations` and `py manage.py migrate` to ensoure that the connection is successful. 

    Don't forget to push any and all new features to the GitHub repo codebase so that all recent changes will be saved to the repository. 

7. On the render dashboard, 
# Documentation

This is the overly simplified documentation for this very simple and easy to use CRUD API. I have tried to describe the processes as easily as I can. 

## Standard Formats:

**Requests**: Each CRUD view is modified to handle basic URL routing and also Dynamic Parameter Handling(DPH), which means that each endpoint, except for CREATE, can make request queries using basic routing and query parameters. (FYI, this was the most interesting thing!)

*CREATE* : The request format goes like: `/api/`.The `CREATE` endpoint takes the name, username and email of a request to create a user. When a user data is passed in `json' format like below:
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
3. Create a service in the `render.yml` file:


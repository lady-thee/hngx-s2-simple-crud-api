from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer, UpdateUserSerializer

import re



def success_handler(message, status_code):
    response_data = {
        'message': message,
    }
    return Response(response_data, status_code)
    

def error_handler(message,  status_code):
    response_data = {
        'message': message,
    }
    return Response(response_data, status_code)
   

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
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)


@api_view(['GET'])
def readUserAPIViewSearch(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        
        if name is not None and not re.match("^[A-Za-z ]+$", name):
                return error_handler('Parameter must be an a string', status.HTTP_400_BAD_REQUEST)
        try:
            if name is not None:
                user = Person.objects.filter(name=name).get()
                serializer = PersonSerializer(user, many=False)
                return Response(serializer.data)
               
        except ObjectDoesNotExist:
            return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)
    
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)


@api_view(['GET'])
def readUserAPIViewModel(request, pk):
    if request.method == 'GET':
        try:
            user = Person.objects.get(id=pk)
            serializer = PersonSerializer(user, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)

    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)
   

@csrf_exempt
@api_view(['GET', 'PUT'])
def updateUserAPIViewModel(request, pk):
    try:
        user = Person.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = UpdateUserSerializer(user, data=request.data)
            if serializer.is_valid():
                # print(serializer.data)
                serializer.save()
                return success_handler('User details updated successfully!', status.HTTP_200_OK)
            else:
                return Response({'Validation erros': serializer.errors}, status.HTTP_400_BAD_REQUEST)
            
    except ObjectDoesNotExist:
        return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)
    
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)


@csrf_exempt
@api_view(['GET', 'PUT'])
def updateUserAPIViewSearch(request):
    name = request.GET.get('name')
    if name is not None and not re.match("^[A-Za-z ]+$", name):
            return error_handler('Parameter must be an a string', status.HTTP_400_BAD_REQUEST)
    try:
        user = Person.objects.filter(name=name).get()
        
        if request.method == 'PUT':
            serializer = UpdateUserSerializer(user, data=request.data)
            if serializer.is_valid():
                # print(serializer.data)
                serializer.save()
                return success_handler( 'User details updated successfully!', status.HTTP_200_OK)
            else:
                return Response({'Validation erros': serializer.errors}, status.HTTP_400_BAD_REQUEST)
            
    except ObjectDoesNotExist:
        return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)
    
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)



@api_view(['GET', 'DELETE'])
def deleteUserAPIViewModel(request, pk):
    try:
        user = Person.objects.get(id=pk)
        if request.method == 'DELETE':
            user.delete()
            return success_handler('User successfully deleted!', status.HTTP_200_OK)
        
    except ObjectDoesNotExist:
        return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)
    
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)


@api_view(['GET', 'DELETE'])
def deleteUserAPIViewSearch(request):
    name = request.GET.get('name')
    if name is not None and not re.match("^[A-Za-z ]+$", name):
                return error_handler('Parameter must be an a string', status.HTTP_400_BAD_REQUEST)
    try:
        user = Person.objects.filter(name=name).get()
        if request.method == 'DELETE':
            user.delete()
            return success_handler('User successfully deleted!', status.HTTP_200_OK)
        
    except ObjectDoesNotExist:
        return error_handler('User does not exist', status.HTTP_400_BAD_REQUEST)
    
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer, UpdateUserSerializer

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
                return Response({'message': 'User successfully created', 'user': res}, status.HTTP_201_CREATED)
        except Exception as e:
            raise ValidationError('Serializer not valid', str(e))
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)


@api_view(['GET'])
def readUserAPIViewSearch(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        print( name)
        try:
            if name:
                user = Person.objects.filter(name=name).get()
                serializer = PersonSerializer(user, many=False)
                return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'message': 'User does not exist'}, status.HTTP_400_BAD_REQUEST)
    
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
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'message': 'User does not exist'}, status.HTTP_400_BAD_REQUEST)

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
                return Response({'message': 'User details updated successfully!'}, status.HTTP_200_OK)
            else:
                print('not valid')
    except:
        raise ObjectDoesNotExist('User does not exist!')
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)

@csrf_exempt
@api_view(['GET', 'PUT'])
def updateUserAPIViewSearch(request):
    try:
        name = request.GET.get('name')
        user = Person.objects.filter(name=name).get()
        if request.method == 'PUT':
            serializer = UpdateUserSerializer(user, data=request.data)
            if serializer.is_valid():
                # print(serializer.data)
                serializer.save()
                return Response({'message': 'User details updated successfully!'}, status.HTTP_200_OK)
            
    except:
        raise ObjectDoesNotExist('User does not exist!')
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
            return Response({'message': 'User successfully deleted!', }, status.HTTP_200_OK)
    except:
        raise ObjectDoesNotExist('User does not exist!')
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)
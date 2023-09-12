from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer

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



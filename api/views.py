from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
@api_view(['GET', 'POST'])
def createAPIView(request):
    
    safe = {
        'detail': 'API loaded successfully!',
        'status': status.HTTP_200_OK
    }
    return Response(safe)


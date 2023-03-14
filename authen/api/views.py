from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth import logout
from django.http import JsonResponse


@api_view(['GET'])

def View(request):
    api_urls = {
        'HOME PAGE':'/'
    }
 
    return Response(api_urls)

@api_view(['POST'])

def Reg_user(request):
    Users = UserSerializer(data=request.data)
   
    if Users.is_valid():
        user_data = Users.validated_data
        email = user_data['email']
        if Users.Meta.model.objects.filter(email=email).exists():
            raise serializers.ValidationError('This User is already registered')
        Users.save()
        return Response(Users.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
        
    if Users is not None:
        return Response({'success': True},"LOGGED IN")
    else:

        return Response({'success': False},"Wrong Creditentials")    
    
    

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True},"LOGGET OUT")

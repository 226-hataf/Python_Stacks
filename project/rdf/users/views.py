


from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from django.http import HttpResponse
from .serializers import RegisterSerializer
from django.views.decorators.csrf import csrf_protect
from .models import User


@csrf_protect
#@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # _, token =AuthToken.objects.create(user)
        user= User.objects.create()
        
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email        
            },
            # 'token': token
        })
    else:
        return HttpResponse("Error")
      

def register_api(request):
  
 if request.method == 'POST':
  serializers = RegisterSerializer(data = request.data)
  serializers .is_valid(raise_exception=True)
  
 
  user= User.objects.create(user) 
  
  return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email        
            },
            #  'token': token
        })
  
 else:
    return HttpResponse("Error Cannot Register")
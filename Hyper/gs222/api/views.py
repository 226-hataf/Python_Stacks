from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
# Create your views here.



class StudentMoodelViewSet(viewsets.ModelViewSet):
    
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
        
            
    

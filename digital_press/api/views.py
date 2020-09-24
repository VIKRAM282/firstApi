from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *



class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    

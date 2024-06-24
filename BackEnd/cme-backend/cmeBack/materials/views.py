from django.shortcuts import render
from rest_framework import generics
from .models import Materiais
from .serializers import MateriaisSerializer

class MateriaisListCreate(generics.ListCreateAPIView):
    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer

class MateriaisRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer

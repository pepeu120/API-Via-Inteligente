from django.shortcuts import render
from rest_framework import viewsets
from .models import Acidente, Status
from .serializers import AcidenteSerializer, StatusSerializer

class AcidenteCreateView(viewsets.ModelViewSet):
    queryset = Acidente.objects.all()
    serializer_class = AcidenteSerializer

class StatusCreateView(viewsets.ModelViewSet):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer



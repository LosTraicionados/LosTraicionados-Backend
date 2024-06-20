from django.shortcuts import render
from rest_framework import viewsets
from .models import worker
from .serializers import WorkerSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = worker.objects.all()
    serializer_class = WorkerSerializer
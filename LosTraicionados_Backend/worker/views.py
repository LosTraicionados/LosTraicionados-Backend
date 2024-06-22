from rest_framework import viewsets
from .models import Worker
from .serializers import WorkerSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
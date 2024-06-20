from rest_framework import serializers
from .models import worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = worker
        fields = '__all__'
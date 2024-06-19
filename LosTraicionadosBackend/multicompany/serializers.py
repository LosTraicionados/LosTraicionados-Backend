from rest_framework import serializers
from .models import MultiCompany

class MultiCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiCompany
        fields = '__all__'
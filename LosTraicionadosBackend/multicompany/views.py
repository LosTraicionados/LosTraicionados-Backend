from rest_framework import viewsets
from .models import MultiCompany
from .serializers import MultiCompanySerializer

class MultiCompanyViewSet(viewsets.ModelViewSet):
    queryset = MultiCompany.objects.all()
    serializer_class = MultiCompanySerializer
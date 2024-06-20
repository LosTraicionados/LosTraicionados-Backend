from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MultiCompanyViewSet

router = DefaultRouter()
router.register(r'multicompany', MultiCompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
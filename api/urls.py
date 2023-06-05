from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'', viewsets.indexSet, basename='index')
router.register(r'salary', viewsets.getSalarySet, basename='get_salary')
router.register(r'organisms', viewsets.getOrganismsSet, basename='get_organisms')

urlpatterns = [
    path('', include(router.urls)),
]
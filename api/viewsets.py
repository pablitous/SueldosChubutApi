from rest_framework import generics, viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter
from . import views, serializers


class indexSet(generics.GenericAPIView, viewsets.ViewSet):
    serializer_class = serializers.indexSerializer
    def list(self, request):
        queryset = views.index(request)
        return queryset

class getSalarySet(generics.GenericAPIView, viewsets.ViewSet):
    serializer_class = serializers.salarySerializer

    @extend_schema(description='text',
                   parameters=[
                    serializers.salarySerializer,  # serializer fields are converted to parameters
                    ],
                   filters=[OpenApiParameter(name='format', required=False, enum=[])]
                   ,
                   )
    def list(self, request):
        queryset = views.get_salary(request)
        return queryset

class getOrganismsSet(generics.GenericAPIView, viewsets.ViewSet):
    serializer_class = serializers.organismSerializer
    def list(self, request):
        queryset = views.get_organisms(request)
        return queryset
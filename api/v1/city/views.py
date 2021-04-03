from rest_framework import viewsets

from api.v1.city.serializers import CitySerializer
from core.models import City
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all().order_by('-id')
    serializer_class = CitySerializer
    permission_classes = []

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY, description="Enter city name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[name_param])
    def list(self, request, *args, **kwargs):
        queryset = City.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        page = self.paginate_queryset(queryset)
        serializer = CitySerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response



from rest_framework import viewsets

from api.v1.industry.serializers import IndustrySerializer
from core.models import Industry
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class IndustryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Industry.objects.all().order_by('-id')
    serializer_class = IndustrySerializer
    permission_classes = []

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY, description="Enter industry name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[name_param])
    def list(self, request, *args, **kwargs):
        queryset = Industry.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        page = self.paginate_queryset(queryset)
        serializer = IndustrySerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response



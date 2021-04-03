from rest_framework import viewsets

from api.v1.department.serializers import DepartmentSerializer
from core.models import Department
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all().order_by('-id')
    serializer_class = DepartmentSerializer
    permission_classes = []

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY, description="Enter department name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[name_param])
    def list(self, request, *args, **kwargs):
        queryset = Department.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        page = self.paginate_queryset(queryset)
        serializer = DepartmentSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response



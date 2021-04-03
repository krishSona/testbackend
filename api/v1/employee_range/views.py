from rest_framework import viewsets

from api.v1.employee_range.serializers import EmployeeRangeSerializer
from core.models import EmployeeRange
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class EmployeeRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeRange.objects.all().order_by('-id')
    serializer_class = EmployeeRangeSerializer
    permission_classes = []

    number_param = openapi.Parameter(
        'number', openapi.IN_QUERY, description="Enter number", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[number_param])
    def list(self, request, *args, **kwargs):
        queryset = EmployeeRange.objects.all().order_by('-id')
        number = self.request.query_params.get('number', None)
        if number is not None:
            queryset = queryset.filter(number__icontains=number)
        page = self.paginate_queryset(queryset)
        serializer = EmployeeRangeSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

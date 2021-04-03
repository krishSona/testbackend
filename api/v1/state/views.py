from rest_framework import viewsets

from api.v1.state.serializers import StateSerializer
from core.models import State
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = State.objects.all().order_by('-id')
    serializer_class = StateSerializer
    permission_classes = []

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY, description="Enter state name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[name_param])
    def list(self, request, *args, **kwargs):
        queryset = State.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        page = self.paginate_queryset(queryset)
        serializer = StateSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response



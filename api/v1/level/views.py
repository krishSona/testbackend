from rest_framework import viewsets
from api.v1.level.serializers import LevelSerializer
from core.models import Level
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all().order_by('-id')
    serializer_class = LevelSerializer
    permission_classes = []

    title_param = openapi.Parameter(
        'title', openapi.IN_QUERY, description="Enter title", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[title_param])
    def list(self, request, *args, **kwargs):
        queryset = Level.objects.all().order_by('-id')
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        page = self.paginate_queryset(queryset)
        serializer = LevelSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

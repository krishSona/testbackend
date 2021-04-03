from rest_framework import viewsets

from api.v1.domain.serializers import DomainSerializer
from core.models import Domain
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from django.http.response import JsonResponse


class DomainViewSet(viewsets.ModelViewSet):

    queryset = Domain.objects.all().order_by('-id')
    serializer_class = DomainSerializer
    permission_classes = []

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY,
        description="Enter Domain name",
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[name_param])
    def list(self, request, *args, **kwargs):
        queryset = Domain.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        else:
            queryset = queryset.filter(category=0)
        if name is not None:
            queryset = queryset.filter(name=name)
        if queryset:
            return JsonResponse({"generic": True})
        else:
            return JsonResponse({"generic": False})

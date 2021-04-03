from rest_framework import viewsets

from api.v1.ifs.serializers import IfsSerializer
from core.models import Ifs
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from django.http import JsonResponse

from rest_framework.exceptions import ValidationError


class IfsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create or list ifs.
    """
    queryset = Ifs.objects.all().order_by('-id')
    serializer_class = IfsSerializer
    permission_classes = []

    code_param = openapi.Parameter(
        'code', openapi.IN_QUERY, description="Enter code", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[code_param])
    def list(self, request, *args, **kwargs):
        queryset = Ifs.objects.all().order_by('-id')
        code = self.request.query_params.get('code', None)
        if code:
            ifs = queryset.filter(code=code).first()
            if ifs:
                return JsonResponse({
                    "id": ifs.id,
                    "code": str(ifs.code),
                    "bank": {
                        "id": ifs.bank.id if ifs.bank else None,
                        "name": str(ifs.bank.name) if ifs.bank else None
                    }
                })
            if not ifs:
                return JsonResponse({
                    "id": None,
                    "code": str(code),
                    "bank": {
                        "id": None,
                        "name": None
                    }
                })
        raise ValidationError({"message": "Invalid arguments"})

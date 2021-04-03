from django.http import JsonResponse
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from rest_framework import views
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from authentication.models import User


class UserCheckView(views.APIView):

    response_schema_dict = {
        "200": openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    "user_exists": True,
                }
            }
        ),
        "200: ok": openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    "user_exists": False,
                }
            }
        ),
    }

    username_param = openapi.Parameter(
        'username', openapi.IN_QUERY,
        description="Enter user's username",
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(
        method='get', manual_parameters=[username_param], responses=response_schema_dict)
    @action(detail=False, methods=['GET'])
    def get(self, request):
        username = request.GET.get('username', None)
        if not username:
            raise ValidationError({"message": "Username is Required."})
        user = User.objects.filter(username=username)
        if user:
            return JsonResponse({"user_exists": True})
        else:
            return JsonResponse({"user_exists": False})

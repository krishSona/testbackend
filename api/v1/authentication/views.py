import datetime
import pytz

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import permissions, views
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from rest_framework.decorators import api_view, action
from rest_framework.exceptions import ValidationError

from daily_salary import settings


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return refresh


def get_utc_datetime(datetime):
    utc = pytz.UTC
    return utc.localize(datetime)


class UserLoginView(views.APIView):
    """
    API endpoint that allows users to authenticate and login
    """

    response_schema_dict = {
        "200": openapi.Response(
            description="when use password",
            examples={
                "application/json": {
                    "refresh": "string",
                    "access": "string",
                }
            }
        ),
        "200:ok": openapi.Response(
            description="when use otp",
            examples={
                "application/json": {
                    "status": "true",
                    "refresh": "string",
                    "access": "string",
                }
            }
        ),
        "200:Ok": openapi.Response(
            description="when source=app",
            examples={
                "application/json": {
                    "employee": {
                        "id": 1,
                        "phone": "string",
                        "name": "string",
                        "email": "string",
                        "net_monthly_salary": 0,
                        "company": {
                            "id": 1,
                            "name": "string"
                        }
                    },
                    "status": "True",
                    "message": "Logged in successfully",
                    "token": {
                        "refresh": "string",
                        "access": "string",
                    }
                }
            }
        ),
        "400:Bad": openapi.Response(
            description="when use password",
            examples={
                "application/json": {
                    "message": "authenticated failed.",
                    "status": False
                }
            }
        ),
        "400:BAd": openapi.Response(
            description="when use otp",
            examples={
                "application/json": {
                    "message": "otp expired.",
                    "status": False
                }
            }
        ),
        "400:BAD": openapi.Response(
            description="when use otp",
            examples={
                "application/json": {
                    "message": "otp Invalid.",
                    "status": False
                }
            }
        ),
        "400:bad": openapi.Response(
            description="400 custom error",
            examples={
                "application/json": {
                    "message": "otp or password is not given.",
                    "status": False
                }
            }
        ),
    }

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'otp': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ), responses=response_schema_dict)
    @action(detail=False, methods=['POST'])
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        otp = request.data.get('otp', None)
        source = self.request.query_params.get('source', None)
        if not username:
            raise ValidationError({
                "message": "Username is required.", "status": False
            })
        if not password and not otp:
            raise ValidationError({
                "message": "Password or OTP is required.", "status": False
            })
        if otp:
            if len(str(otp)) != 6:
                raise ValidationError({
                    "message": "OTP should have 6 digits only.", "status": False
                })

        try:
            user = User.objects.get(username=username)
            employee = user.employee_set.filter(deleted_at=None).last()
            if not employee:
                raise ObjectDoesNotExist
        except ObjectDoesNotExist:
            raise ValidationError(
                {
                    "message": "User does not exist",
                    "status": 404
                }
            )

        if password:
            auth = authenticate(username=user.username, password=password)
            if auth:
                refresh = get_tokens_for_user(user=user)
                return JsonResponse(
                        {
                            "refresh": str(refresh),
                            "access": str(refresh.access_token),
                            "x-karza-key": str(settings.CORE_X_KARZA_KEY)
                        }
                    )
            else:
                raise ValidationError({"message": "authenticated failed.", "status": False})
        elif otp:
            cur_datetime = datetime.datetime.now()
            cur_datetime = get_utc_datetime(cur_datetime)
            if user.otp == otp:
                if cur_datetime < user.otp_valid_till:
                    refresh = get_tokens_for_user(user=user)
                    if source == 'app':
                        employee = user.employee_set.filter(deleted_at=None).last()
                        return JsonResponse(
                            {
                                "employee": {
                                    "id": int(employee.id),
                                    "phone": str(employee.phone),
                                    "name": str(employee.name),
                                    "email": str(employee.email) if employee.email else None,
                                    "net_monthly_salary": int(employee.net_monthly_salary),
                                    "company": {
                                        "id": int(employee.company.id) if employee.company else None,
                                        "name": str(employee.company.name) if employee.company else None
                                    }
                                },
                                "status": "True",
                                "message": "Logged in successfully",
                                "token": {
                                    "refresh": str(refresh),
                                    "access": str(refresh.access_token),
                                    "x-karza-key": str(settings.CORE_X_KARZA_KEY)
                                }
                            }
                        )
                    return JsonResponse(
                            {
                                "status": "True",
                                "refresh": str(refresh),
                                "access": str(refresh.access_token),
                                "x-karza-key": str(settings.CORE_X_KARZA_KEY)
                            }
                        )
                else:
                    raise ValidationError(
                        {"message": "otp expired.", "status": False}
                    )

            else:
                raise ValidationError(
                    {"message": "Invalid otp.", "status": False}
                )
        else:
            data = {
                "message": "otp or password not given.", "status": False
            }
            raise ValidationError(data)


class RefreshTokenView(views.APIView):
    """
    API endpoint that allows users to get access token from refresh token.
    """

    response_schema_dict = {
       "200": openapi.Response(
           description="Success",
           examples={
               "application/json": {
                   "access": "string",
               }
           }
       ),
        "400": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "message": "Token is invalid or expired."
                }
            }
        ),
        "400: Bad": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "message": "Token is required."
                }
            }
        ),
    }

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='string')
        }
    ), responses=response_schema_dict)
    @action(detail=False, methods=['POST'])
    def post(self, request, *args, **kwargs):
        refresh = request.data.get('refresh', None)
        if refresh:
            try:
                refresh_token = RefreshToken(refresh)
            except:
                raise ValidationError({"message": "Refresh Token is invalid or expired."})
            return JsonResponse({
                "refresh": str(refresh_token),
                "access": str(refresh_token.access_token),
                "x-karza-key": str(settings.CORE_X_KARZA_KEY)
            })
        raise ValidationError({"message": "Refresh Token is required."})

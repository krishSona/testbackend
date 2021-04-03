from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import action

from authentication.models import User

import datetime
import pytz

from rest_framework import views
from rest_framework.exceptions import ValidationError
from django.http import JsonResponse

from services.sms.send import call
import utilities
from services.email.send import send_email


def get_utc_datetime(date_time):
    utc = pytz.UTC
    return utc.localize(date_time)


class SmsOtpView(views.APIView):
    """
    API endpoint that allows users to send sms
    """
    permission_classes = []

    response_schema_dict = {
        "200": openapi.Response(
           description="Success",
           examples={
               "application/json": {
                   "body": "Hello! Your OTP for login is 154622. And this OTP is valid for 2 minutes only.",
                   "sender": "NSQURD",
                   "type": "OTP",
                   "source": "API",
                   "id": "83fd53e3-e183-401e-8411-9a3d2e409c02",
                   "createdDateTime": "2020-12-12 12:22:11+00:00",
                   "totalCount": 1,
                   "data": [
                       {
                           "message_id": "83fd53e3-e183-401e-8411-9a3d2e409c02:1",
                           "recipient": "917007501490"
                       }
                   ],
                   "error": {},
                   "otp": "154622"
               }
           }
        ),
    }

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'phone': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'template': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ), responses=response_schema_dict)
    @action(detail=False, methods=['POST'])
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', None)
        template = request.data.get('template', None)
        if not phone:
            raise ValidationError({"message": "Phone is Required."})
        if not template:
            raise ValidationError({"message": "Template is Required."})
        user = User.objects.filter(username=phone).first()

        # get otp and send to the user
        otp = utilities.generate_random_number(6)
        data = call(phone, template, otp)
        data['otp'] = str(otp) if otp else ""

        if user:
            user.otp = otp
            expiry_datetime = datetime.datetime.now() + datetime.timedelta(seconds=120)
            expiry_datetime = get_utc_datetime(expiry_datetime)
            user.otp_valid_till = expiry_datetime
            user.save()
        return JsonResponse(data)


class ActivationEmailView(views.APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject')
        message = request.data.get('message')
        from_email = request.data.get('from_email')
        to_email = request.data.get('to_email')

        if subject and message and from_email and to_email:
            send_email(subject, message, from_email, to_email)
        else:
            raise ValidationError({"message": "Enter subject, message, from_email and to_email"})



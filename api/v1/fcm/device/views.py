from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

from api.v1.fcm.device import serializers
from fcm_django.models import FCMDevice
from django.http import JsonResponse
from core.models import Employee


class FCMDeviceViewSet(viewsets.ModelViewSet):

    queryset = FCMDevice.objects.all().order_by('-id')
    serializer_class = serializers.FCMDeviceSerializer
    permission_classes = []

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'fcm_registration_token': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'employee_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'device_type': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    def create(self, request):
        fcm_registration_token = request.data.get('fcm_registration_token', None)
        device_type = request.data.get('device_type', None)
        employee_id = request.data.get('employee_id', None)
        if not fcm_registration_token:
            raise ValidationError({"message": "fcm_registration_token is required field"})
        if not device_type:
            raise ValidationError({"message": "device_type is required field"})
        if device_type not in ['web', 'android', 'ios']:
            raise ValidationError({"message": "Invalid device_type is required field"})
        if not employee_id:
            raise ValidationError({"message": "employee_id is required field"})
        if employee_id:
            employee = Employee.objects.filter(id=employee_id, deleted_at=None).first()
            if not employee:
                raise ValidationError({"message": "Employee Does Not Exists."})
        fcm_obj = FCMDevice.objects.filter(user=employee.user).first()
        if fcm_obj:
            fcm_obj.registration_id = fcm_registration_token
            fcm_obj.device_type = device_type
            fcm_obj.active = True
            fcm_obj.save()
            return JsonResponse({"status": "True"})
        device_data = {
            "registration_id": fcm_registration_token,
            "user": employee.user.id,
            "type": device_type,
            "active": True
        }
        serializer = serializers.FCMDeviceSerializer(data=device_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        raise ValidationError({"message": "Invalid arguments"})

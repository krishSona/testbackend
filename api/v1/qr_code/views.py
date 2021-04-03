from rest_framework import viewsets
from api.v1.qr_code.serializers import QrCodeSerializer
from core.models import QrCode, Employee, Company, Setting

from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

from rest_framework.exceptions import ValidationError
from django.http.response import JsonResponse

from utilities import distance_between_two_points

import os
from daily_salary.settings import BASE_DIR


class QrCodeViewSet(viewsets.ModelViewSet):
    queryset = QrCode.objects.all().order_by('-id')
    serializer_class = QrCodeSerializer
    permission_classes = []

    response_schema_dict = {
        "200": openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    "valid": True,
                    "message": "Valid QR Code"
                }
            }
        ),
        "200:ok": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "valid": False,
                    "message": "Invalid QR Code"
                }
            }
        ),
        "200:Ok": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "valid": False,
                    "message": "Invalid Location"
                }
            }
        ),
        "200:OK": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "valid": False,
                    "message": "You are not registered"
                }
            }
        ),
        "200: OK": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "valid": False,
                    "message": "You are not verified"
                }
            }
        ),
        "400": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "valid": False,
                    "message": "Params are missing"
                }
            }
        ),
        "400: Bad": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "valid": False,
                    "message": "Employee's Company has no QrCode."
                }
            }
        ),
    }

    qr_id_param = openapi.Parameter(
        'qr_id', openapi.IN_QUERY, description="Enter Company QrCode",
        type=openapi.TYPE_STRING
    )
    source_param = openapi.Parameter(
        'source', openapi.IN_QUERY,
        description="Enter source param", type=openapi.TYPE_STRING)
    fieldset_param = openapi.Parameter(
        'fieldset', openapi.IN_QUERY,
        description="Enter fieldset param", type=openapi.TYPE_STRING)
    longitude_param = openapi.Parameter(
        'longitude', openapi.IN_QUERY,
        description="Enter longitude param", type=openapi.TYPE_STRING)
    latitude_param = openapi.Parameter(
        'latitude', openapi.IN_QUERY,
        description="Enter latitude param", type=openapi.TYPE_STRING)
    employee_id_param = openapi.Parameter(
        'employee_id', openapi.IN_QUERY,
        description="Enter Employee ID", type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(manual_parameters=[
        qr_id_param, source_param, fieldset_param, longitude_param,
        latitude_param, employee_id_param], responses=response_schema_dict)
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        qr_id = self.request.query_params.get('qr_id', None)
        employee_id = self.request.query_params.get('employee_id', None)
        source = self.request.query_params.get('source', None)
        fieldset = self.request.query_params.get('fieldset', None)
        if source == 'app' and fieldset == 'qr':
            longitude = self.request.query_params.get('longitude', None)
            latitude = self.request.query_params.get('latitude', None)
            if not (employee_id and qr_id and longitude and latitude):
                return JsonResponse({"valid": "False", "message": "Params are missing"})
            try:
                qr_code = QrCode.objects.get(qr_id=qr_id)
            except:
                raise ValidationError({"valid": "False", "message": "Invalid QR Code"})
            employee_obj = Employee.objects.filter(id=employee_id, deleted_at=None).first()
            if not employee_obj:
                raise ValidationError({"message": "Employee Does not Exists"})
            if employee_obj.check_location:
                distance_between_location = distance_between_two_points(
                    longitude1=float(qr_code.longitude),
                    latitude1=float(qr_code.latitude),
                    longitude2=float(longitude),
                    latitude2=float(latitude),
                )
                with open(os.path.join(BASE_DIR, 'locations.log'), 'a') as f:
                    string = str(qr_code.longitude) + "," + str(qr_code.latitude) \
                             + "," + str(longitude) + "," + str(latitude) + "," + \
                             str(distance_between_location)
                    f.write(string)
                    f.write("\n")
                try:
                    distance = Setting.objects.get(key='distance')
                except:
                    raise ValidationError({"valid": "False", "message": "Setting Not Found"})
                if distance_between_location < float(distance.value):
                    return JsonResponse({"valid": "True", "message": "Valid QR Code"})
                return JsonResponse({"valid": "False", "message": "Invalid Location."})
            else:
                return JsonResponse({"valid": "True", "message": "Valid QR Code"})

        if qr_id:
            queryset = queryset.filter(qr_id=qr_id)
        page = self.paginate_queryset(queryset)
        serializer = QrCodeSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'qr_id': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'longitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='decimal'),
            'latitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='decimal'),
        }
    ))
    def create(self, request, *args, **kwargs):
        qr_id = request.data.get('qr_id', None)
        longitude = request.data.get('longitude', None)
        latitude = request.data.get('latitude', None)
        if not qr_id:
            raise ValidationError({'status': 'False', "message": "Empty QR Code"})
        if qr_id:
            try:
                company_code = qr_id.split('-')[0]
            except:
                raise ValidationError({'status': 'False',"message": "Invalid QR Code format"})
            try:
                company = Company.objects.get(code=company_code)
            except:
                raise ValidationError({'status': 'False',"message": "Company not found"})
        if qr_id and longitude and latitude:
            queryset = QrCode.objects.filter(
                qr_id=qr_id).first()
            if queryset:
                raise ValidationError({'status': 'False',"message": "QR Code already registered"})
        data = {
            "qr_id": qr_id,
            "longitude": longitude,
            "latitude": latitude,
            "company": company.id
        }
        serializer = QrCodeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        raise ValidationError({'status': 'False',"message": "Invalid details"})

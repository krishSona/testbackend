from rest_framework import viewsets
from api.v1.booking.serializers import BookingSerializer
from core.models import Booking
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

from django.http.response import JsonResponse
from rest_framework.exceptions import ValidationError
from services.email.send import send_email

import re


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-id')
    serializer_class = BookingSerializer
    permission_classes = []

    status_param = openapi.Parameter(
        'status', openapi.IN_QUERY, description="Enter status", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[status_param])
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        page = self.paginate_queryset(queryset)
        serializer = BookingSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

    response_schema_dict = {
        "200": openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    "message": "Booking created successfully.",
                    "status": "True"
                }
            }
        ),
        "400": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "message": "Invalid arguments",
                    "status": "False"
                }
            }
        ),
        "400:Bad": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "message": "Phone is required.",
                    "status": "False"
                }
            }
        ),
    }

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'phone': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'company': openapi.Schema(
                type=openapi.TYPE_STRING, description='string'),
            'status': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
            'category': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
        }
    ), responses=response_schema_dict)
    def create(self, request, *args, **kwargs):
        name = request.data.get('name', None)
        if not name:
            raise ValidationError({
                "status": 'False',
                "message": "Name is required."
            })
        phone = request.data.get('phone', None)
        if not phone:
            raise ValidationError({
                "status": 'False',
                "message": "Phone is required."
            })
        if phone:
            if len(phone) != 10:
                raise ValidationError({
                    "status": 'False',
                    "message": "Phone length should be 10 digits."
                })
        email = request.data.get('email', None)
        if not email:
            raise ValidationError({
                "status": 'False',
                "message": "Email is required"
            })
        if email:
            regex = '^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$'
            match = re.match(regex, email)
            if not match:
                raise ValidationError({
                    "status": 'False',
                    "message": "Email is Invalid"
                })
        company = request.data.get('company', None)
        category = request.data.get('category', None)
        booking_data = {
            "name": name,
            "phone": phone,
            "email": email,
            "company": company,
            "category": category,
        }
        serializer = BookingSerializer(data=booking_data)
        if serializer.is_valid():
            serializer.save()

            company_first_name = company.split(' ')[0]

            # mail to user
            send_email(
                "Activate your " + str(company_first_name) + " Employee Wallet",
                "booking_email",
                [email],
                'contact@dailysalary.in',
                None,
                name,
                company_first_name,
            )

            # mail to admin
            send_email(
                str(name) + " from " + str(company) + " wants to connect with you",
                "booking_admin_email",
                ['basuki@dailysalary.in', 'shantanu@dailysalary.in', 'ravi@dailysalary.in'],
                'contact@dailysalary.in',
                None,
                name,
                company,
                email,
                phone,
            )

            return JsonResponse({
                "status": 'True',
                "message": "Booking created successfully."
            })
        raise ValidationError({
            "status": 'False',
            "message": "Invalid arguments"
        })

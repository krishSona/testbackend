from rest_framework import viewsets
from core.models import Verifier, Employee
from api.v1.verifier import serializers

from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

from rest_framework.exceptions import ValidationError
from django.http import JsonResponse


class VerifierViewSet(viewsets.ModelViewSet):
    queryset = Verifier.objects.all().order_by('-id')
    serializer_class = serializers.VerifierSerializer
    permission_classes = []

    email_param = openapi.Parameter(
        'email', openapi.IN_QUERY,
        description="Enter Email",
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[email_param])
    def list(self, request, *args, **kwargs):
        queryset = Verifier.objects.all().order_by('-id')
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email__icontains=email)
        page = self.paginate_queryset(queryset)
        serializer = serializers.VerifierSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'employee_id': openapi.Schema(
                type=openapi.TYPE_STRING, description='string'),
            'verifiers': openapi.Schema(
                type=openapi.TYPE_STRING, description='array of string')
        }
    ))
    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee_id', None)
        verifiers = request.data.get('verifiers', None)     # Array of string
        if not employee_id:
            raise ValidationError({
                "status": "False",
                "message": "EmployeeId is required"})
        if employee_id:
            employee = Employee.objects.filter(id=employee_id, deleted_at=None).first()
            if not employee:
                raise ValidationError({
                    "status": "False",
                    "message": "Employee does not exists"
                })
        if not verifiers:
            raise ValidationError({
                "status": "False",
                "message": "Verifiers list is required"})
        if verifiers:
            if len(verifiers) < 1:
                raise ValidationError({
                    "status": "False",
                    "message": "No Verifiers in list."})
        for verifier_email in verifiers:
            if verifier_email.split('@')[1] == str(employee.email).split('@')[1]:
                verifier_obj = Verifier.objects.create(
                    email=verifier_email
                )
                verifier_obj.employee.add(employee)
                verifier_obj.save()
        return JsonResponse({
            "status": "True",
            "message": "Verifiers created successfully"
        })

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets

from api.v1.employer.serializers import EmployerSerializer
from api.v1.company.serializers import PrincipalCompanyListSerializer
from authentication.models import User
from core.models import Employer, Company, Department, Designation
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class EmployerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to list, create,retrieve, update, delete.
    """
    queryset = Employer.objects.all().order_by('-id')
    serializer_class = EmployerSerializer
    permission_classes = []

    response_schema_dict = {
        "200": openapi.Response(
           description="source == 'web' and fieldset == 'principal'",
           examples={
               "application/json": {
                   "count": 1,
                   "next": "",
                   "previous": "",
                   "results": [
                       {
                           "id": 22,
                           "user": {
                               "id": 44,
                               "username": "string"
                           },
                           "rid": "string",
                           "name": "string",
                           "phone": "string",
                           "email": "string",
                           "company": 1,
                           "department": 1,
                           "designation": 1,
                           "principal_companies": [
                               1
                           ]
                       },
                   ]
               }
           }
        ),
    }
    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY, description="Enter employer's name",
        type=openapi.TYPE_STRING)
    email_param = openapi.Parameter(
        'email', openapi.IN_QUERY, description="Enter employer's email",
        type=openapi.TYPE_STRING
    )
    source_param = openapi.Parameter(
        'source', openapi.IN_QUERY, description="Enter source param",
        type=openapi.TYPE_STRING)
    fieldset_param = openapi.Parameter(
        'fieldset', openapi.IN_QUERY, description="Enter fieldset param",
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[
        name_param, email_param, source_param, fieldset_param],
        responses=response_schema_dict)
    def list(self, request, *args, **kwargs):
        queryset = Employer.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        email = self.request.query_params.get('email', None)
        source = self.request.query_params.get('source', None)
        fieldset = self.request.query_params.get('fieldset', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if email:
            queryset = queryset.filter(email=email)
        if email and source == 'web' and fieldset == 'principal':
            employer = queryset.first()
            principal_companies = employer.principal_companies.all()
            page = self.paginate_queryset(principal_companies)
            serializer = PrincipalCompanyListSerializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response
        page = self.paginate_queryset(queryset)
        serializer = EmployerSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                description='object'),
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'phone': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'department': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
            'designation': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
            'company': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
        }
    ))
    def create(self, request):
        employer_data = request.data

        # user data validation
        username = employer_data['user'].get('username', None)
        if not username:
            raise ValidationError({"message": "username is required field"})
        if username:
            user = User.objects.filter(username=username).first()
            if user:
                raise ValidationError({
                    "message": "User already exists with this username."})

        # employer_data validation
        name = employer_data.get('name', None)
        phone = employer_data.get('phone', None)
        email = employer_data.get('email', None)
        photo = employer_data.get('photo', None)
        department = employer_data.get('department', None)
        designation = employer_data.get('designation', None)
        company = employer_data.get('company', None)

        if not email:
            raise ValidationError({"message": "email is required."})
        if not name:
            raise ValidationError({"message": "name is required."})
        if not phone:
            raise ValidationError({"message": "phone is required."})
        if email:
            employer = Employer.objects.filter(email=email).first()
            if employer:
                raise ValidationError({
                    "message": "employer already exists with this email."})
        if department:
            try:
                Department.objects.get(id=department)
            except:
                raise ValidationError({"message": "department does not exist."})
        if designation:
            try:
                Designation.objects.get(id=designation)
            except:
                raise ValidationError({"message": "designation does not exist."})
        if company:
            try:
                Company.objects.get(id=company)
            except:
                raise ValidationError({"message": "company does not exist."})

        serializer = EmployerSerializer(data=employer_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        raise ValidationError({"message": "Invalid arguments"})

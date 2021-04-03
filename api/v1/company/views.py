from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

from rest_framework import viewsets

from api.v1.company.serializers import (
    CompanySerializer,
    CompanyAutoCompleteListSerializer,
    PrincipalCompanyListSerializer,
    CompanyDomainListSerializer,
)
from core.models import Company, Industry, EmployeeRange, \
    City, State, Designation, Department, Employee
from authentication.models import User
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
    permission_classes = []

    response_schema_dict = {
        "200": openapi.Response(
           description="source=app and fieldset=autocomplete",
           examples={
               "application/json": {
                   "count": 1,
                   "next": "",
                   "previous": "",
                   "results": [
                       {
                           "id": 1,
                           "name": "string"
                       }
                   ]
               }
           }
        ),
        "200:ok": openapi.Response(
            description="source == 'web' and fieldset == 'principal'",
            examples={
                "application/json": {
                    "count": 1,
                    "next": "",
                    "previous": "",
                    "results": [
                        {
                            "id": 1,
                            "name": "string",
                            "rid": "53973782-0198-4511-9d5e-ab11b50f780e"
                        }
                    ]
                }
            }
        ),
    }
    source_param = openapi.Parameter(
        'source', openapi.IN_QUERY,
        description="Enter source param", type=openapi.TYPE_STRING)
    fieldset_param = openapi.Parameter(
        'fieldset', openapi.IN_QUERY,
        description="Enter fieldset param", type=openapi.TYPE_STRING)
    domain_param = openapi.Parameter(
        'domain', openapi.IN_QUERY,
        description="Enter domain param", type=openapi.TYPE_STRING)
    longitude_param = openapi.Parameter(
        'longitude', openapi.IN_QUERY,
        description="Enter longitude param", type=openapi.TYPE_STRING)
    latitude_param = openapi.Parameter(
        'latitude', openapi.IN_QUERY,
        description="Enter latitude param", type=openapi.TYPE_STRING)

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY,
        description="Enter company name", type=openapi.TYPE_STRING)
    qr_id_param = openapi.Parameter(
        'qr_id', openapi.IN_QUERY,
        description="Enter company qr_id", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[
        source_param, fieldset_param, domain_param, longitude_param,
        latitude_param, name_param, qr_id_param], responses=response_schema_dict)
    def list(self, request, *args, **kwargs):
        queryset = Company.objects.all().order_by('-id')
        name = self.request.query_params.get('name', None)
        qr_id = self.request.query_params.get('qr_id', None)
        source = self.request.query_params.get('source', None)
        fieldset = self.request.query_params.get('fieldset', None)
        domain = self.request.query_params.get('domain', None)
        if source == 'app' and fieldset == 'autocomplete':
            page = self.paginate_queryset(queryset)
            serializer = CompanyAutoCompleteListSerializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response
        if source == 'web' and fieldset == 'principal':
            queryset = queryset.filter(category=1)
            page = self.paginate_queryset(queryset)
            serializer = PrincipalCompanyListSerializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response
        if source == 'web' and fieldset == 'name':
            queryset = queryset.filter(name=name)
            page = self.paginate_queryset(queryset)
            serializer = CompanySerializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response
        if source == 'app' and fieldset == 'domain':
            if not domain:
                raise ValidationError({"message": "Domain Param is required"})
            queryset = queryset.filter(domain=domain)
            page = self.paginate_queryset(queryset)
            serializer = CompanyDomainListSerializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return response
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if qr_id:
            queryset = queryset.filter(qr_id=qr_id)
        page = self.paginate_queryset(queryset)
        serializer = CompanySerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'employer_set': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.TYPE_OBJECT,
                description='string'),
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'office_address': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'pincode': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'gstin': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'average_monthly_salary_payout': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
            'monthly_salary_day': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
            'industry': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'employee_range': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'city': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'state': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
        }
    ))
    def create(self, request):
        company_data = request.data
        employers_data = company_data.get('employer_set')

        # employers_data data validation
        for employer in employers_data:
            username = employer.get('username', None)
            if username:
                user_object = User.objects.filter(username=username).first()
                if user_object:
                    raise ValidationError(
                        {"message": "User already exists with this username."})
            department = employer.get('department', None)
            if department:
                try:
                    Department.objects.get(id=department)
                except:
                    raise ValidationError({"message": "department does not exist."})
            designation = employer.get('designation', None)
            if designation:
                try:
                    Designation.objects.get(id=designation)
                except:
                    raise ValidationError({"message": "designation does not exist."})

        # company data validation
        company_name = company_data.get('name', None)
        industry = company_data.get('industry', None)
        employee_range = company_data.get('employee_range', None)
        office_address = company_data.get('office_address', None)
        city = company_data.get('city', None)
        state = company_data.get('state', None)
        pincode = company_data.get('pincode', None)
        gstin = company_data.get('gstin', None)
        if not company_name:
            raise ValidationError({"message": "company_name is required."})
        if not industry:
            raise ValidationError({"message": "industry is required."})
        if not employee_range:
            raise ValidationError({"message": "employee_range is required."})
        if not office_address:
            raise ValidationError({"message": "office_address is required."})
        if not city:
            raise ValidationError({"message": "city is required."})
        if not state:
            raise ValidationError({"message": "state is required."})
        if not pincode:
            raise ValidationError({"message": "pincode is required."})
        if not gstin:
            raise ValidationError({"message": "gstin is required."})
        if company_name:
            company = Company.objects.filter(name=company_name)
            if len(company) > 0:
                raise ValidationError(
                    {"message": "company exists with the same name"})
        if industry:
            try:
                Industry.objects.get(id=industry)
            except:
                raise ValidationError({"message": "Industry does not exist."})
        if employee_range:
            try:
                EmployeeRange.objects.get(id=employee_range)
            except:
                raise ValidationError({"message": "employee_range does not exist."})
        if city:
            try:
                City.objects.get(id=city)
            except:
                raise ValidationError({"message": "city does not exist."})
        if state:
            try:
                State.objects.get(id=state)
            except:
                raise ValidationError({"message": "state does not exist."})

        serializer = CompanySerializer(data=company_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        raise ValidationError({"message": "Invalid company arguments"})

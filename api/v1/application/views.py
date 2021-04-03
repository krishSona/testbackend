from rest_framework import viewsets

from tools import do_quess_employee_signup
from services.quess.attendance import create_attendance_and_verify

from api.v1.application.serializers import ApplicationSerializer
from core.models import Application
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

from django.http.response import JsonResponse
from rest_framework.exceptions import ValidationError


class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.filter(deleted_at=None).order_by('-id')
    serializer_class = ApplicationSerializer
    permission_classes = []

    name_param = openapi.Parameter(
        'name', openapi.IN_QUERY, description="Enter application name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[name_param])
    def list(self, request, *args, **kwargs):
        queryset = Application.objects.filter(deleted_at=None).order_by('-id')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        page = self.paginate_queryset(queryset)
        serializer = ApplicationSerializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return response

    def create(self, request, *args, **kwargs):
        name = request.data.get('name', None)
        company_email = request.data.get('company_email', None)
        employee_id = request.data.get('employee_id', None)
        phone = request.data.get('phone', None)
        company_name = request.data.get('company_name', None)
        net_monthly_salary = request.data.get('net_monthly_salary', None)
        salary_day = request.data.get('salary_day', None)
        bank_name = request.data.get('bank_name', None)
        bank_account_name = request.data.get('bank_account_name', None)
        bank_account_number1 = request.data.get('bank_account_number1', None)
        bank_account_number2 = request.data.get('bank_account_number2', None)
        ifsc = request.data.get('ifsc', None)
        utm_source = request.data.get('utm_source', None)
        utm_medium = request.data.get('utm_medium', None)
        utm_campaign = request.data.get('utm_campaign', None)

        application = Application.objects.filter(phone=phone, deleted_at=None).first()
        if application:
            application.name = name if name else application.name
            application.phone = phone if phone else application.phone
            application.company_name = company_name if company_name else application.company_name
            application.company_email = company_email if company_email else application.company_email
            application.employee_id = employee_id if employee_id else application.employee_id
            application.net_monthly_salary = net_monthly_salary if net_monthly_salary else application.net_monthly_salary
            application.salary_day = salary_day if salary_day else application.salary_day
            application.bank_name = bank_name if bank_name else application.bank_name
            application.bank_account_name = bank_account_name if bank_account_name else application.bank_account_name
            application.bank_account_number1 = bank_account_number1 if bank_account_number1 else application.bank_account_number1
            application.bank_account_number2 = bank_account_number2 if bank_account_number2 else application.bank_account_number2
            application.ifsc = ifsc if ifsc else application.ifsc
            application.utm_source = utm_source if utm_source else application.utm_source
            application.utm_medium = utm_medium if utm_medium else application.utm_medium
            application.utm_campaign = utm_campaign if utm_campaign else application.utm_campaign

            application.save()
            return JsonResponse({
                "id": application.id,
                "status": 'True',
                "message": "Application created successfully."
            })

        application_data = {
            "name": name,
            "phone": phone,
            "company_email": company_email,
            "company_name": company_name,
            "employee_id": employee_id,
            "net_monthly_salary": net_monthly_salary,
            "salary_day": salary_day,
            "bank_name": bank_name,
            "bank_account_name": bank_account_name,
            "bank_account_number1": bank_account_number1,
            "bank_account_number2": bank_account_number2,
            "ifsc": ifsc,
            "utm_source": utm_source,
            "utm_medium": utm_medium,
            "utm_campaign": utm_campaign
        }
        serializer = ApplicationSerializer(data=application_data)
        if serializer.is_valid():
            serializer.save()

            employee_obj = None
            if utm_source == 'quess' and utm_medium == 'banner' and utm_campaign == 'blue_collar':
                employee_obj = do_quess_employee_signup(employee_id=employee_id)
            if employee_obj:
                create_attendance_and_verify(employee_obj)

            return JsonResponse({
                "id": serializer.data.get('id'),
                "status": 'True',
                "message": "Application created successfully."
            })
        raise ValidationError({
            "id": None,
            "status": 'False',
            "message": "Invalid arguments"
        })

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        name = request.data.get('name', None)
        company_email = request.data.get('company_email', None)
        employee_id = request.data.get('employee_id', None)
        phone = request.data.get('phone', None)
        company_name = request.data.get('company_name', None)
        net_monthly_salary = request.data.get('net_monthly_salary', None)
        salary_day = request.data.get('salary_day', None)
        bank_name = request.data.get('bank_name', None)
        bank_account_name = request.data.get('bank_account_name', None)
        bank_account_number1 = request.data.get('bank_account_number1', None)
        bank_account_number2 = request.data.get('bank_account_number2', None)
        ifsc = request.data.get('ifsc', None)
        utm_source = request.data.get('utm_source', None)
        utm_medium = request.data.get('utm_medium', None)
        utm_campaign = request.data.get('utm_campaign', None)

        updated_data = {
            "name": name if name else instance.name,
            "phone": phone if phone else instance.phone,
            "company_email": company_email if company_email else instance.company_email,
            "company_name": company_name if company_name else instance.company_name,
            "employee_id": employee_id if employee_id else instance.employee_id,
            "net_monthly_salary": net_monthly_salary if net_monthly_salary else instance.net_monthly_salary,
            "salary_day": salary_day if salary_day else instance.salary_day,
            "bank_name": bank_name if bank_name else instance.bank_name,
            "bank_account_name": bank_account_name if bank_account_name else instance.bank_account_name,
            "bank_account_number1": bank_account_number1 if bank_account_number1 else instance.bank_account_number1,
            "bank_account_number2": bank_account_number2 if bank_account_number2 else instance.bank_account_number2,
            "ifsc": ifsc if ifsc else instance.ifsc,
            "utm_source": utm_source if utm_source else instance.utm_source,
            "utm_medium": utm_medium if utm_medium else instance.utm_medium,
            "utm_campaign": utm_campaign if utm_campaign else instance.utm_campaign
        }
        serializer = ApplicationSerializer(instance, data=updated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "id": serializer.data.get('id'),
                "status": 'True',
                "message": "Application submitted successfully."
            })
        raise ValidationError({
            "id": None,
            "status": 'False',
            "message": "Invalid arguments"
        })

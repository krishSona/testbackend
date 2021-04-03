import datetime

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets

import utilities
from api.v1.statement.serializers import (
    StatementSerializer,
    StatementListSerializer
)
from core.models import Statement, Employee, Company
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi

from services.email.send import send_email
import math


def calculate_fees_with_gst(debit):
    fees = (debit * 2.5) / 100
    fees = math.ceil(fees)
    c_gst = (fees * 9.0) / 100
    s_gst = (fees * 9.0) / 100
    gst = round(c_gst) + round(s_gst)
    return fees, gst


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.filter(employee__deleted_at=None).order_by('-id')
    serializer_class = StatementSerializer
    #permission_classes = [permissions.IsAuthenticated]

    from_date_param = openapi.Parameter(
        'from_date', openapi.IN_QUERY, description="Enter from_date (YYYY-MM-DD)",
        type=openapi.TYPE_STRING)
    to_date_param = openapi.Parameter(
        'to_date', openapi.IN_QUERY, description="Enter to_date (YYYY-MM-DD)",
        type=openapi.TYPE_STRING)
    employee_param = openapi.Parameter(
        'employee', openapi.IN_QUERY, description="Enter employee Id",
        type=openapi.TYPE_STRING)
    source_param = openapi.Parameter(
        'source', openapi.IN_QUERY, description="Enter source",
        type=openapi.TYPE_STRING)
    fieldset_param = openapi.Parameter(
        'fieldset', openapi.IN_QUERY, description="Enter fieldset",
        type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[from_date_param, to_date_param, source_param,
                           fieldset_param, employee_param])
    def list(self, request, *args, **kwargs):
        queryset = Statement.objects.filter(employee__deleted_at=None).order_by('-id')
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)
        employee = self.request.query_params.get('employee', None)
        source = self.request.query_params.get('source', None)
        fieldset = self.request.query_params.get('fieldset', None)
        if source == 'app' and fieldset == 'debit':
            queryset = queryset.filter(debit__gt=0.0)
        if from_date:
            try:
                datetime.datetime.strptime(from_date, "%Y-%m-%d")
            except:
                raise ValidationError({"message": "Invalid from_date format."})
            queryset = queryset.filter(date__gte=from_date)
        if to_date:
            try:
                datetime.datetime.strptime(to_date, "%Y-%m-%d")
            except:
                raise ValidationError({"message": "Invalid to_date format."})
            queryset = queryset.filter(date__lte=to_date)
        if employee:
            queryset = queryset.filter(employee_id=employee)
            serializer = StatementSerializer(queryset, many=True)

            last_statement = Statement.objects.filter(employee=employee).last()
            if last_statement:
                response_data = {
                    "total_due": float(last_statement.balance) + float(last_statement.previous_due),
                    "balance": float(last_statement.balance),
                    "current_due": float(last_statement.current_due),
                    "previous_due": float(last_statement.previous_due),
                    "statements": serializer.data,
                }
            else:
                response_data = {
                    "total_due": 0.0,
                    "balance": 0.0,
                    "current_due": 0.0,
                    "previous_due": 0.0,
                    "statements": []
                }
            return Response(response_data)
            
        page = self.paginate_queryset(queryset)
        serializer = StatementListSerializer(queryset, many=True)
        response = self.get_paginated_response(serializer.data)
        return response


    response_schema_dict = {
        "200": openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    "message": "Statement created successfully.",
                    "otp": "154622"
                }
            }
        ),
    }

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'credit': openapi.Schema(type=openapi.TYPE_NUMBER, description='decimal'),
            'debit': openapi.Schema(type=openapi.TYPE_NUMBER, description='decimal'),
            'balance': openapi.Schema(
                type=openapi.TYPE_NUMBER, description='decimal'),
            'status': openapi.Schema(
                type=openapi.TYPE_STRING, description='string'),
            'employee': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
            'company': openapi.Schema(
                type=openapi.TYPE_INTEGER, description='integer'),
        }
    ), manual_parameters=[source_param, fieldset_param])
    def create(self, request, *args, **kwargs):
        description = request.data.get('description', None)
        credit = request.data.get('credit', None)
        debit = request.data.get('debit', None)
        status = request.data.get('status', None)
        employee = request.data.get('employee', None)
        company = request.data.get('company', None)
        source = self.request.query_params.get('source', None)
        fieldset = self.request.query_params.get('fieldset', None)
        device_name = request.data.get('device_name', None)
        device_id = request.data.get('device_id', None)
        ip_address = request.data.get('ip_address', None)
        disbursement_id = request.data.get('disbursement_id', None)
        loan_id = request.data.get('loan_id', None)

        if not description:
            raise ValidationError({"message": "Description is required."})
        if not employee:
            raise ValidationError({"message": "Employee is required field."})
        if not company:
            raise ValidationError({"message": "Company is required field."})
        if employee:
            employee_object = Employee.objects.filter(id=employee, deleted_at=None).first()
            if not employee_object:
                raise ValidationError({"message": "Employee does not exists."})
            if not employee_object.mail_enabled:
                raise ValidationError({"message": "Please Verify Your Email."})
            if not employee_object.ifs or not employee_object.bank_account_number:
                raise ValidationError({"message": "Please Add Your Bank Details."})

        if company:
            try:
                Company.objects.get(id=company)
            except:
                raise ValidationError({"message": "Company does not exists."})
        if source == 'app' and fieldset == 'debit':
            if debit:
                if float(debit) <= 0:
                    raise ValidationError({
                        "status": "False",
                        "message": "Invalid Transfer Amount"})
                if float(debit) > float(employee_object.get_available_balance()):
                    raise ValidationError({
                        "status": "False",
                        "message": "Insufficient Balance"})
                if float(debit) < 500:
                    raise ValidationError({
                        "status": "False",
                        "message": "Minimum withdrawal amount: Rs.500"})

            digital_time_stamp = None
            if employee_object.name and device_name and device_id and ip_address:
                digital_time_stamp = utilities.generate_digital_time_stamp(
                    employee_object.name, device_name, device_id, ip_address)

            fees, gst = calculate_fees_with_gst(debit)
            total_debit = debit + fees + gst
            last_statement = Statement.objects.filter(employee=employee_object).last()
            if last_statement:
                balance = last_statement.balance + total_debit
                current_due = last_statement.current_due
                previous_due = last_statement.previous_due
            else:
                balance = total_debit
                current_due = 0
                previous_due = 0

            statement_data = {
                "description": description,
                "debit": total_debit,
                "withdraw": debit,
                "fees": fees,
                "gst": gst,
                "balance": balance,
                "current_due": current_due,
                "previous_due": previous_due,
                "employee": employee,
                "company": company,
                "digital_time_stamp": digital_time_stamp
            }

            serializer = StatementSerializer(data=statement_data)
            if serializer.is_valid():
                serializer.save()

                employee_object.balance = float(employee_object.balance) - float(debit)
                employee_object.debited = float(employee_object.debited) + float(total_debit)
                employee_object.withdraw = float(employee_object.withdraw) + float(debit)
                employee_object.fees = float(employee_object.fees) + float(fees)
                employee_object.gst = float(employee_object.gst) + float(gst)

                employee_object.save()

                # send email to Admin for withdraw request
                if employee_object:
                    send_email(
                        "Withdraw Request",               # subject
                        "withdraw_request",               # template
                        ['ravi@dailysalary.in', 'shantanu@dailysalary.in', 'ops@dailysalary.in'],  # to_emails
                        'contact@dailysalary.in',
                        None,                              # attachment=None
                        str(employee_object.name),
                        str(debit),
                        str(employee_object.ifs.bank.name),
                        str(employee_object.bank_account_number),
                        str(employee_object.ifs.code),
                        str(employee_object.id),
                    )

                return JsonResponse({
                    "status": "True",
                    "message": "Statement created successfully.",
                    "description": serializer.data.get('description', None),
                    "debit": debit
                })
            raise ValidationError({
                "status": "False",
                "message": "Invalid Arguments."})
        raise ValidationError({
            "status": "False",
            "message": "Missing source and fieldset Params."})

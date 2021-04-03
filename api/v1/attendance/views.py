from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework import viewsets
from core.models import Attendance, Employee, Company, Statement
from api.v1.attendance.serializers import (
    AttendanceSerializer,
    AttendanceStatementListSerializer
)

import datetime
import time

from rest_framework.exceptions import ValidationError
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi


def find_employee_is_working(employee_obj):
    today = datetime.datetime.now()
    day = today.strftime("%a")
    working_days = employee_obj.work_days.get('days')
    if day in working_days:
        is_working = True
    else:
        is_working = False
    return is_working


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.filter(employee__deleted_at=None).order_by('-id')
    serializer_class = AttendanceSerializer
    permission_classes = []

    employee_id_param = openapi.Parameter(
        'employee_id', openapi.IN_QUERY, description="Enter employee ID", type=openapi.TYPE_INTEGER)
    source_param = openapi.Parameter(
        'source', openapi.IN_QUERY, description="Enter source", type=openapi.TYPE_STRING)
    date_param = openapi.Parameter(
        'fieldset', openapi.IN_QUERY, description="Enter fieldset", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[employee_id_param])
    def list(self, request, *args, **kwargs):
        queryset = Attendance.objects.filter(employee__deleted_at=None).order_by('-id')
        source = self.request.query_params.get('source', None)
        fieldset = self.request.query_params.get('fieldset', None)
        employee_id = self.request.query_params.get('employee_id', None)
        if source == "app" and fieldset == "statement":
            if employee_id:
                queryset = queryset.filter(
                    employee=employee_id,
                    date__month=datetime.datetime.now().month,
                    date__year=datetime.datetime.now().year,
                )
            serializer = AttendanceStatementListSerializer(queryset, many=True)
            employee_obj = Employee.objects.filter(id=employee_id, deleted_at=None).first()
            if employee_obj:
                last_statement = employee_obj.statement_set.all().order_by('id').last()

            statements = Statement.objects.filter(
                employee=employee_obj,
                date__month=datetime.datetime.now().month,
                date__year=datetime.datetime.now().year,
            )
            withdraw = sum([s.withdraw for s in statements if s.withdraw])
            return Response({
                "total_due": float(withdraw) if withdraw else 0.0,
                "statements": serializer.data
            })
        raise ValidationError({"message": "Invalid arguments"})

    response_schema_dict = {
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json": {
                    "status": True,
                    "message": "Attendance marked successfully",
                    "employee": {
                        "daily_salary": 0.0,
                        "balance": 0.0
                    }
                }
            }
        ),
        "400": openapi.Response(
            description="Duplicate attendance error",
            examples={
                "application/json": {
                    "status": False,
                    "message": "Attendance already created for this employee.",
                    "employee": {}
                }
            }
        ),
        "400:bad": openapi.Response(
            description="custom 400 description",
            examples={
                "application/json": {
                    "status": False,
                    "message": "Invalid arguments",
                    "employee": {}
                }
            }
        ),
    }

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'status': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'duration': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'start_time': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'end_time': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'qr_code_scanned': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='boolean'),
            'face_detected': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='boolean'),
            'location': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'employee': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'company': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'image': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ), responses=response_schema_dict)
    def create(self, request):
        today_date = str(datetime.datetime.now().date())
        date = request.data.get('date', None)
        duration = request.data.get('duration', None)
        start_at = request.data.get('start_time', None)
        end_at = request.data.get('end_time', None)
        qr_code_scanned = request.data.get('qr_code_scanned', None)
        face_detected = request.data.get('face_detected', None)
        work_location = request.data.get('location', None)
        employee = request.data.get('employee', None)
        company = request.data.get('company', None)
        image = request.data.get('image', None)
        status = request.data.get('status', None)
        if not employee:
            raise ValidationError({
                "status": False,
                "message": "Employee is Required.",
                "employee": {}
            })
        if not company:
            raise ValidationError({
                "status": False,
                "message": "Company is Required.",
                "employee": {}
            })
        if not status:
            raise ValidationError({
                "status": False,
                "message": "Status is Required.",
                "employee": {}
            })
        if date:
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except:
                raise ValidationError({
                    "status": False,
                    "message": "Date format should be like %Y-%m-%d.",
                    "employee": {}
                })
        if start_at or end_at:
            try:
                time.strptime(start_at, "%I:%M %p")
                time.strptime(end_at, "%I:%M %p")
            except:
                raise ValidationError({
                    "status": False,
                    "message": "Time format should be like 'HH:MM AM/PM'",
                    "employee": {}
                })
        if status:
            if status not in ['present', 'absent']:
                raise ValidationError({
                    "status": False,
                    "message": "Invalid Status",
                    "employee": {}
                })
        if duration:
            if duration not in ['full_day', 'half_day']:
                raise ValidationError({
                    "status": False,
                    "message": "Invalid Duration",
                    "employee": {}
                })
        if work_location:
            if work_location not in ['office', 'home', 'other']:
                raise ValidationError({
                    "status": False,
                    "message": "Invalid Work Location.",
                    "employee": {}
                })

        employee_obj = Employee.objects.filter(id=employee, deleted_at=None).first()
        company_obj = Company.objects.get(id=company)

        # to find working day
        is_working = find_employee_is_working(employee_obj)

        # check attendance already exists
        attendance = Attendance.objects.all().filter(
            date=date if date else today_date,
            employee_id=employee,
            company_id=company
        )
        if attendance:
            raise ValidationError({
                "status": False,
                "message": "Today's allowance has already been added to your wallet",
                "employee": {},
                "company": {},
                "working_day": is_working,
                "attendance_marked": True
            })

        if status == 'absent':
            attendance_data = {
                "date": date if date else today_date,
                "status": status,
                "employee": employee,
                "company": company,
            }
            serializer = AttendanceSerializer(data=attendance_data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "status": True,
                    "message": "Attendance marked successfully",
                    "employee": {
                        "id": int(employee_obj.id),
                        "name": str(employee_obj.name),
                        "balance": float(employee_obj.balance) \
                            if employee_obj.balance else 0.0,
                        "daily_salary": float(employee_obj.daily_salary) \
                            if employee_obj.daily_salary else 0.0,
                        "bank_account_number": str(employee_obj.bank_account_number) \
                            if employee_obj.bank_account_number else "",
                        "ifs": {
                            "code": str(employee_obj.ifs.code) if employee_obj.ifs else "",
                            "bank": {
                                "name": str(employee_obj.ifs.bank.name) \
                                    if employee_obj.ifs else ""
                            }
                        }
                    },
                    "company": {
                        "id": int(employee_obj.company.id) if employee_obj.company else None,
                        "Name": str(employee_obj.company.name) if employee_obj.company else ""
                    },
                    "working_day": is_working,
                    "attendance_marked": True
                }
                return JsonResponse(response_data)
            raise ValidationError({
                "status": False,
                "message": "Invalid arguments",
                "employee": {},
                "company": {},
                "working_day": is_working,
                "attendance_marked": False
            })
        else:
            attendance_data = {
                "date": date if date else today_date,
                "status": status,
                "duration": duration,
                "start_at": start_at,
                "end_at": end_at,
                "work_location": work_location,
                "qr_code_scanned": qr_code_scanned,
                "face_detected": face_detected,
                "employee": employee,
                "company": company,
                "image": image if image else '',
            }
            serializer = AttendanceSerializer(data=attendance_data)
            if serializer.is_valid():
                serializer.save()
                try:
                    # update 'balance' of employee after attendance created
                    employee_obj.balance = float(employee_obj.balance) + float(employee_obj.daily_salary)
                    employee_obj.save()
                    response_data = {
                        "status": True,
                        "message": "Attendance marked successfully",
                        "employee": {
                            "id": int(employee_obj.id),
                            "name": str(employee_obj.name),
                            "balance": float(employee_obj.balance) \
                                if employee_obj.balance else 0.0,
                            "daily_salary": float(employee_obj.daily_salary) \
                                if employee_obj.daily_salary else 0.0,
                            "bank_account_number": str(employee_obj.bank_account_number) \
                                if employee_obj.bank_account_number else "",
                            "ifs": {
                                "code": str(employee_obj.ifs.code) if employee_obj.ifs else "",
                                "bank": {
                                    "name": str(employee_obj.ifs.bank.name) \
                                        if employee_obj.ifs else ""
                                }
                            }
                        },
                        "company": {
                            "id": int(employee_obj.company.id) if employee_obj.company else None,
                            "Name": str(employee_obj.company.name) if employee_obj.company else ""
                        },
                        "working_day": is_working,
                        "attendance_marked": True
                    }
                    return JsonResponse(response_data)
                except:
                    raise ValidationError({
                        "status": False,
                        "message": "Something Went Wrong",
                        "employee": {},
                        "company": {},
                        "working_day": is_working,
                        "attendance_marked": False
                    })
            print(str(serializer.errors))
            raise ValidationError({
                "status": False,
                "message": "Invalid arguments",
                "employee": {},
                "company": {},
                "working_day": is_working,
                "attendance_marked": False
            })

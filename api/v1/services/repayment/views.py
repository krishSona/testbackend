from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from rest_framework import views
from django.http import JsonResponse

from core.models import Employee
import json
import requests

from daily_salary.settings import PG_BASE_URL


def _json(response):
    return json.loads(response._content.decode('utf-8'))


class RegisterView(views.APIView):
    permission_classes = []

    response_schema_dict = {
        "200": openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    'status': 'True',
                    'message': 'Subscription Created Successfully',
                    'auth_link': 'https://...'
                }
            }
        ),
        "400": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    'status': 'False',
                    'message': 'Can not be Created',
                    'auth_link': {}
                }
            }
        ),
    }

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'employee_id': openapi.Schema(type=openapi.TYPE_STRING, description='string')
        }
    ), responses=response_schema_dict)
    @action(detail=False, methods=['POST'])
    def post(self, request, *args, **kwargs):
        employee_id = request.data.get('employee_id', None)
        if not employee_id:
            raise ValidationError({
                "status": "False",
                "message": "Employee Id is required."})

        employee_obj = Employee.objects.filter(id=employee_id, deleted_at=None).first()
        if not employee_obj:
            raise ValidationError({
                "status": "False",
                "message": "Employee Does Not Exists"
            })
        if not employee_obj.mail_verified:
            raise ValidationError({
                "status": "False",
                "message": "Employee is not verified yet."})
        employee_rid = str(employee_obj.rid) if employee_obj.rid else None
        name = str(employee_obj.name) if employee_obj.name else None
        phone = str(employee_obj.phone) if employee_obj.phone else None
        email = str(employee_obj.email) if employee_obj.email else "contact@dailysalary.in"
        net_monthly_salary = int(employee_obj.net_monthly_salary) if employee_obj.net_monthly_salary else None
        if not employee_rid:
            raise ValidationError({
                "status": "False",
                "message": "Employee has no Employee RId"})
        if not phone:
            raise ValidationError({
                "status": "False",
                "message": "Employee has no Phone"})
        if not email:
            raise ValidationError({
                "status": "False",
                "message": "Employee has no Email"})
        if not net_monthly_salary:
            raise ValidationError({
                "status": "False",
                "message": "Employee has no Net Monthly Salary"})
        payload = {
            "employee_rid": employee_rid,
            "name": name,
            "phone": phone,
            "email": email,
            "net_monthly_salary": net_monthly_salary,
        }
        try:
            response = requests.post(
                PG_BASE_URL + '/api/v1/services/repayment/register/',
                data=json.dumps(payload),
                headers={"content-type": "application/json"}
            )
            response_data = _json(response)
            return JsonResponse({
                "status": response_data['status'],
                "message": response_data['message'],
                "auth_link": response_data['auth_link']
            })
        except Exception as e:
            print("Exception error:", e)
            return JsonResponse({
                "status": 'False',
                "message": 'We are unable to process your bank details right now',
                "auth_link": {}
            })

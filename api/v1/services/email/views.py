from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import action

from rest_framework.exceptions import ValidationError
from django.http import JsonResponse

from rest_framework import views
import background_jobs
from core.models import Employee
from services.email.send import send_email


class SendView(views.APIView):

    response_schema_dict = {
        "200": openapi.Response(
           description="Success",
           examples={
               "application/json": {
                   "status": "True",
                   "message": "Email has been sent successfully"
               }
           }
        ),
        "400": openapi.Response(
            description="Failed",
            examples={
                "application/json": {
                    "status": "False",
                    "message": "Can't sent email, Please Try again !"
                }
            }
        ),
    }

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'employee_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='string'),
            'template': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ), responses=response_schema_dict)
    @action(detail=False, methods=['POST'])
    def post(self, request, *args, **kwargs):
        employee_id = request.data.get('employee_id', None)
        template = request.data.get('template', None)
        if not template:
            raise ValidationError({"status": "False", "message": "Email Template is required"})

        if template:
            if template == "verify_email":
                if not employee_id:
                    raise ValidationError({
                        "mail_verified": "False",
                        "status": "False",
                        "message": "EmployeeId is required"})
                if employee_id:
                    employee_obj = Employee.objects.filter(id=employee_id, deleted_at=None).first()
                    if not employee_obj:
                        raise ValidationError({"status": "False", "message": "Employee does not exists"})
                if employee_obj.mail_verified:
                    raise ValidationError({
                        "mail_verified": "True",
                        "status": "True",
                        "message": "Email already verified"
                    })

                response = background_jobs.verify_email(employee_obj)
                if response.status_code == 202:
                    return JsonResponse({
                        "mail_verified": "False",
                        "status": "True",
                        "message": "Email has been sent successfully"
                    })
                raise ValidationError({
                    "mail_verified": "False",
                    "status": "False",
                    "message": "Can't sent email, Please Try again !"})
            if template == "quess_registration_request":
                name = request.data.get('name', None)
                email = request.data.get('company_email', None)
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

                if bank_account_number2 and bank_account_number1:
                    if not (bank_account_number2 == bank_account_number1):
                        return JsonResponse({
                            "status": "False",
                            "message": "Bank account number not matched"
                        })

                response = send_email(
                    "Quess Registration Request",
                    "quess_registration_request",
                    ['ops@dailysalary.in'],
                    'contact@dailysalary.in',
                    None,
                    str(name) if name else "",
                    str(employee_id) if employee_id else "",
                    str(phone) if phone else "",
                    str(company_name) if company_name else "",
                    str(net_monthly_salary) if net_monthly_salary else "",
                    str(bank_name) if bank_name else "",
                    str(bank_account_name) if bank_account_name else "",
                    str(bank_account_number1) if bank_account_number1 else "",
                    str(ifsc) if ifsc else "",
                    str(salary_day) if salary_day else "",
                    str(email) if email else "",
                    str(utm_source) if utm_source else "",
                    str(utm_medium) if utm_medium else "",
                    str(utm_campaign) if utm_campaign else "",
                )
                if response and response.status_code == 202:
                    return JsonResponse({
                        "status": "True",
                        "message": "Employee registered successfully"
                    })
                else:
                    raise ValidationError({"status": "False", "message": "Something Went Wrong"})
            raise ValidationError({"status": "False", "message": "Template Not Found"})
        raise ValidationError({"status": "False", "message": "Template Not Given"})

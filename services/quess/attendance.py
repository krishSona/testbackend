import json

from daily_salary import settings
import requests
import datetime

from core.models import Attendance
from services.sms.send import call


def get_base_url():
    if settings.ENV == "production":
        base_url = "https://marqet-api.inedgeretail.com"
    else:
        # base_url = "http://worq-marqet-api.heptagon.tech"
        base_url = "https://marqet-api.inedgeretail.com"
    return base_url


def get_employee_attendance(applicant_id, identifier, start_date, end_date):
    base_url = get_base_url()
    payload = {
        "identifier": identifier,
        "employee_id": applicant_id,
        "start_date": start_date,
        "end_date": end_date
    }
    try:
        response = requests.post(
            url=base_url + "/thirdparty/api/v1/get_employees_attendance",
            data=json.dumps(payload),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + settings.CORE_QUESS_AUTH_TOKEN
            }
        )
        return response.json()
    except Exception as e:
        print(e)


def create_attendance_and_verify(employee):
    employee_id = employee.employee_id if employee.employee_id else None
    employee_id_ = None
    if employee_id:
        employee_id_ = employee_id.split('$')[0]
    identifier = employee.extra_data.get('identifier') if employee.extra_data else None
    start_date = datetime.datetime.now().replace(day=1).strftime('%Y-%m-%d')
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    if employee_id_ and identifier and start_date and end_date:
        response_data = get_employee_attendance(
            employee_id_, identifier, start_date, end_date)
        attendance_data = None
        if response_data and response_data.get('data'):
            if response_data.get('data').get('attendance'):
                attendance_data = response_data.get('data').get('attendance')
        if attendance_data:
            daily_salary = employee.get_daily_salary()
            balance = 0.0
            for data in attendance_data:

                created_date = data.get('date')
                date_obj = datetime.datetime.strptime(created_date, '%Y-%m-%d')

                date_string = date_obj.strftime('%-d, %Y')
                month_name = date_obj.strftime('%b')
                date_string_ = month_name + ' ' + date_string
                description = "Salary credited for " + str(date_string_)

                status = data.get('status')
                status = status.lower()
                if status == 'present' or status == 'present on weekoff':
                    Attendance.objects.create(
                        date=date_obj.strftime('%Y-%m-%d'),
                        status=status,
                        duration="full_day",
                        salary=float(daily_salary),
                        verified_salary=float(daily_salary),
                        description=description,
                        employee=employee,
                        company=employee.company,
                    )
                    balance += float(daily_salary)
                elif status == 'absent' or status == 'week off' or status == 'leave':
                    Attendance.objects.create(
                        date=date_obj.strftime('%Y-%m-%d'),
                        status=status,
                        duration="full_day",
                        salary=0.0,
                        verified_salary=0.0,
                        description=description,
                        employee=employee,
                        company=employee.company,
                    )
                elif status == 'half day present':
                    Attendance.objects.create(
                        date=date_obj.strftime('%Y-%m-%d'),
                        status=status,
                        duration="half_day",
                        salary=float(daily_salary),
                        verified_salary=float(daily_salary)/2,
                        description=description,
                        employee=employee,
                        company=employee.company,
                    )
                    balance += float(daily_salary)
                else:
                    pass

            employee.mail_verified = True
            employee.mail_token = None
            employee.save()

            # credit balance of employee in wallet
            employee.balance = balance
            employee.credited = balance
            employee.save()

            if employee.phone and employee.name:
                try:
                    call(
                        employee.phone,
                        "play_store_link",
                        str(employee.name).split(' ')[0],
                        "https://tinyurl.com/sq5ewi5c",
                    )
                except Exception as e:
                    print(e)

    print("Employee verified Successfully!")

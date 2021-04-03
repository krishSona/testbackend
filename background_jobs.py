import datetime
import json

import utilities
from daily_salary import settings
import requests
from django.db.models import Q
from core.models import Employee, Pricing
from core.models import Statement, Attendance, Verifier, Company
import payout
from services.email.send import send_email

import os
import base64
from daily_salary.settings import BASE_DIR
from sendgrid.helpers.mail import (
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
    ContentId
)

import tools

from services.firebase.firebase_cloud_messaging.send import send_notification

from services.quess.attendance import get_employee_attendance


def validate_bank_account_details():
    employees = Employee.objects.filter(is_verified=False)
    for employee in employees:
        if employee.bank_account_number and employee.ifs:
            message = payout.validate_bank_details(
                employee.name, employee.phone, employee.bank_account_number,
                employee.ifs.code)
            if message == 'Bank Account details verified successfully.':
                employee.is_verified = True
                employee.save()
            elif message == 'Invalid account number or ifsc provided.':
                employee.is_verified = False
                employee.save()
    add_beneficiaries()


def add_beneficiaries():
    employees = Employee.objects.filter(is_verified=True)
    for employee in employees:
        if employee.bank_account_number and employee.ifs:
            beneficiary_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            message = payout.add_beneficiary(
                beneficiary_id, employee.name, 'upendra@instasalary.app', employee.phone,
                'Gurugram', employee.bank_account_number, employee.ifs.code)
            if message == 'Beneficiary added successfully':
                employee.is_beneficiary = True
                employee.beneficiary_id = beneficiary_id
                employee.save()
            elif message == 'Entered bank account already exist':
                employee.is_beneficiary = True
                employee.beneficiary_id = payout.get_beneficiary_id(
                    employee.bank_account_number, employee.ifs.code)
                employee.save()


# def request_transfers():
#     transfers = Transfer.objects.filter(utr=None)
#     for transfer in transfers:
#         beneficiary_id = transfer.account.beneficiary_id
#         transfer_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
#         transfer_mode = 'banktransfer'
#         remarks = 'Advance Salary'
#         # str(transfer.amount)
#         response = payout.request_transfer(beneficiary_id, 1.0, transfer_id, transfer_mode, remarks)
#         if response['message'] == 'Transfer completed successfully':
#             transfer.transfer_id = transfer_id
#             transfer.utr = response['data']['utr']
#             transfer.save()
#     get_transfers_status()
#
#
# def get_transfers_status():
#     transfers = Transfer.objects.filter(status=None)
#     for transfer in transfers:
#         transfer_id = transfer.transfer_id
#         response = payout.get_transfer_status(transfer_id)
#         if response['status'] == 'SUCCESS':
#             transfer.status = response['data']['transfer']['status']
#             transfer.processed_on = datetime.datetime.strptime(response['data']['transfer']['processedOn'] + ' +0530',
#                                                                '%Y-%m-%d %H:%M:%S %z')
#             transfer.save()


# cron job to be run at 10:00 (every monday) to send email to verifiers
def send_viral_loop_email():
    verifier_objects = Verifier.objects.filter(counter__lte=3)
    for verifier_obj in verifier_objects:
        # check if verifier is not an existing employee
        employee_exists = Employee.objects.filter(
            email=str(verifier_obj.email),
            deleted_at=None,
        ).first()
        if not employee_exists:
            username = str(verifier_obj.email).split('@')[0]
            company = verifier_obj.employee.all().first().company
            employee_objects = company.employee_set.all().order_by('-id')[:3]
            emp_names = ""
            for emp in employee_objects:
                emp_names = emp_names + str(emp.name).split(' ')[0] + ", "
            unsubscribe_token = ""
            response = send_email(
                "Activate your " + str(company.name).split(' ')[0] + " Salary Wallet",
                "viral_loop" if verifier_obj.counter == 0 else "reminder_viral_loop",
                [str(verifier_obj.email)],
                'contact@dailysalary.in',
                None,
                username,
                str(company.name).split(' ')[0],
                str(employee_objects.count()),
                str(emp_names),
                str(unsubscribe_token)
            )
            if response.status_code == 202:
                verifier_obj.counter += 1


def verify_email(employee_object):
    if employee_object and employee_object.email:
        base_url = settings.BASE_URL
        mail_token = employee_object.mail_token
        if not mail_token:
            mail_token = utilities.get_random_time_based_token()
            employee_object.mail_token = mail_token
            employee_object.save()
        response = send_email(
            "Daily Salary : Verify email address",  # subject
            "verify_email",  # template
            [str(employee_object.email)],  # to_emails
            'contact@dailysalary.in',       # from_email
            None,
            str(employee_object.name) if employee_object.name else '',
            str(mail_token),
            str(employee_object.unsubscribe_token),
            str(employee_object.id),
            str(base_url)
        )
        return response


def auto_credited_email(employee_object):
    # send email to employee for auto credited money to wallet ( not a cron job)
    date_time_string = datetime.datetime.now().strftime('%b %d, %Y (%a)')
    # get email attachment
    file_path = os.path.join(
        BASE_DIR, 'static/images/auto_credited.png')
    with open(file_path, 'rb') as f:
        image = f.read()
        f.close()
    image_encoded = base64.b64encode(image).decode()

    attachment = Attachment()
    attachment.file_content = FileContent(image_encoded)
    attachment.file_type = FileType('image/png')
    attachment.file_name = FileName('auto_credited.png')
    attachment.disposition = Disposition('inline')
    attachment.content_id = ContentId('auto_credited')
    get_daily_salary = employee_object.get_daily_salary()
    base_url = settings.BASE_URL
    if employee_object and employee_object.email:
        date_string = datetime.datetime.now().strftime('%b %-d, %Y')
        company_first_name = utilities.get_company_first_name(employee_object)
        response = send_email(
            "Rs." + str(get_daily_salary) + " salary credited for " + str(date_string),  # subject
            "auto_credited",  # template
            [str(employee_object.email)],  # to_emails
            'salary@dailysalary.in',       # from_email
            attachment,
            str(employee_object.name) if employee_object.name else '',
            int(get_daily_salary),
            int(employee_object.balance),
            str(employee_object.unsubscribe_token),
            str(base_url),
            str(company_first_name)
        )
        return response


# cron job to be run every day:
# 1) send auto_credited email
# 2) send auto_credited notification
def send_auto_credited_email_everyday():
    employees = Employee.objects.filter(deleted_at=None,active=True).order_by('id')
    for employee in employees:
        attendance_count = Attendance.objects.filter(
            employee=employee,
            company=employee.company
        ).all().count()
        if attendance_count > 0:
            employee_work_days = employee.work_days.get('days')
            today = datetime.datetime.now().strftime('%a')
            if today in employee_work_days:
                attendance = Attendance.objects.filter(
                    date=datetime.datetime.now().date(),
                    employee=employee,
                    company=employee.company
                ).first()
                if not attendance:
                    daily_salary = employee.get_daily_salary()
                    # create attendance
                    description = "Salary credited for " + str(datetime.datetime.now().strftime('%b %-d, %Y'))
                    Attendance.objects.create(
                        status="present",
                        salary=daily_salary,
                        description=description,
                        employee=employee,
                        company=employee.company
                    )

                    # update balance of employee
                    employee.balance = employee.balance + daily_salary
                    employee.credited = employee.credited + daily_salary
                    employee.save()

                    # send auto_credited mail to employee
                    if employee.email and employee.mail_enabled and employee.mail_verified:
                        response = auto_credited_email(employee)

                        if response and response.status_code == 202:
                            # update verified attendance
                            attendance = Attendance.objects.filter(
                                employee=employee,
                                company=employee.company,
                                date=datetime.datetime.now().date()
                            ).last()
                            attendance.verified_salary = attendance.salary
                            attendance.save()

                        elif response and response.status_code != 202:
                            employee.mail_bounced += 1
                            if employee.mail_bounced >= 3:
                                employee.mail_enabled = False
                            employee.save()
                        else:
                            pass

                    # send auto_credited notification
                    if employee.user and employee.user.fcmdevice_set.all():
                        date_string = datetime.datetime.now().strftime('%b %-d, %Y')
                        send_notification(
                            [employee.user.id],  # user ids
                            "INR " + str(daily_salary) + " salary credited for " + str(date_string),  # title
                            "auto_credited_notification",  # template
                            {"view": "auto_credited"},  # data
                        )


# cron job to be run on last day of month: create subscription statement
def create_subscription_statement_at_last_day_of_month():
    today = datetime.datetime.now().day
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).day
    if today > tomorrow:
        employees = Employee.objects.filter(
            Q(company__subscription_amount_gt=0) & Q(deleted_at=None)
        )
        for employee in employees:
            subscription_amount = int(employee.company.subscription_amount) if employee.company else 0
            if subscription_amount > 0:
                last_statement = Statement.objects.filter(employee=employee).last()
                if last_statement:
                    balance = last_statement.balance + subscription_amount
                    current_due = balance
                    previous_due = last_statement.previous_due
                    Statement.objects.create(
                        description="Subscription Charge",
                        debit=subscription_amount,
                        balance=balance,
                        current_due=current_due,
                        previous_due=previous_due,
                        employee=employee,
                        company=employee.company
                    )

                    # update employee
                    employee.balance = employee.balance - subscription_amount
                    employee.debited = employee.debited + subscription_amount
                    employee.save()
                else:
                    balance = subscription_amount
                    current_due = balance
                    previous_due = 0
                    Statement.objects.create(
                        description="Subscription Charge",
                        debit=subscription_amount,
                        balance=balance,
                        current_due=current_due,
                        previous_due=previous_due,
                        employee=employee,
                        company=employee.company
                    )

                # update employee
                employee.balance = employee.balance - subscription_amount
                employee.debited = employee.debited + subscription_amount
                employee.save()


def calculate_last_date_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)


# cronjob
def month_end_notification():
    curr_date = datetime.datetime.now().date()
    last_date_of_month = calculate_last_date_of_month(curr_date)
    days_left_month_end = last_date_of_month.day - curr_date.day
    if days_left_month_end < 3:
        employees = Employee.objects.filter(deleted_at=None)
        for employee in employees:
            if employee.user and employee.user.fcmdevice_set.all():
                send_notification(
                    [employee.user.id],                                                         # user ids
                    str(days_left_month_end + 1) + " days left to withdraw salary from Wallet",  # title
                    "month_end_notification",                                               # template
                    {"view": "home_view"},                                                      # data
                )


# cron job to be run at first day of month: reset employee data
def reset_employee_at_every_first_day_of_month():
    # reset debited and credited
    employees = Employee.objects.filter(deleted_at=None)
    for employee in employees:
        employee.balance = 0.0
        employee.debited = 0.0
        employee.credited = 0.0
        employee.withdraw = 0.0
        employee.save()


# cron job to be run on due date of month : Re-payment
def collect_repayment():
    today = datetime.datetime.now().day
    employees = Employee.objects.filter(due_day=today, deleted_at=None)
    for employee in employees:
        last_statement = Statement.objects.filter(employee=employee).last()
        if last_statement:
            repayment_amount = last_statement.current_due + last_statement.previous_due
            employee_rid = str(employee.rid)
            payload = {
                "amount": repayment_amount,
                "employee_rid": employee_rid
            }
            if int(repayment_amount) > 0:
                try:
                    response = requests.post(
                        'https://pg.instasalary.app/api/v1/services/repayment/collect',
                        data=json.dumps(payload),
                        headers={"content-type": "application/json"}
                    )
                    response_data = json.loads(response._content.decode('utf-8'))
                    if response_data['payment']['status'] == 'SUCCESS':
                        # create credit statement of the repayment
                        credit = repayment_amount
                        balance = last_statement.balance - repayment_amount
                        current_due = 0
                        previous_due = 0
                        Statement.objects.create(
                            description="Payment Received",
                            credit=credit,
                            balance=balance,
                            current_due=current_due,
                            previous_due=previous_due,
                            employee=employee,
                            company=employee.company,
                        )
                    print("response_data:", response_data)
                except Exception as e:
                    print("Exception error:", e)
                    pass


def fetch_quess_attendance_daily():
    employees = Employee.objects.filter(Q(company=44))
    print(str(employees.count()) + " employees found")
    for employee in employees:
        employee_id = employee.employee_id
        if employee_id:
            print(employee_id + " employee id found")
            employee_id_ = employee_id.split('$')[0]
            identifier = employee.extra_data.get('identifier', None) if employee.extra_data else None
            if identifier:
                print(identifier + " identifier found")
            # calculate start_date to fetch attendance
            start_date = tools.get_start_date_of_attendance(employee)
            print(str(start_date) + " start date")
            end_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
            print(str(end_date) + " end date")
            if employee_id_ and identifier and start_date and end_date:
                if start_date <= end_date:
                    response_data = get_employee_attendance(
                        employee_id_, identifier, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                    print(str(response_data) + " response data")
                    attendance_data = None
                    if response_data and response_data.get('data'):
                        if response_data.get('data').get('attendance'):
                            attendance_data = response_data.get('data').get('attendance')
                    if attendance_data:
                        daily_salary = employee.get_daily_salary()
                        balance = float(employee.balance)
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
                                    verified_salary=float(daily_salary) / 2,
                                    description=description,
                                    employee=employee,
                                    company=employee.company,
                                )
                                balance += float(daily_salary)
                            else:
                                print('New Status ' + status)
                                pass
                        employee.balance = balance
                        employee.credited = balance
                        employee.save()
                        print(str(employee.id) + " Attendance created successfully")
                    else:
                        print(str(employee.id) + " Attendance not found")
                else:
                    print("Invalid start and end date")
            else:
                print("Invalid arguments")

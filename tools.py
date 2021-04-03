import re
import datetime
import os
from services.sms.send import call

import requests

from core.models import Employee
from rest_framework.exceptions import ValidationError

from services.quess.applicants import get_employee_details

from authentication.models import User
from core.models import Bank, Ifs, Company, Attendance


def delete_an_employee(employee_id):
    employee = Employee.objects.filter(id=employee_id).first()
    if employee:
        employee.attendance_set.all().delete()
        employee.statement_set.all().delete()
        user = employee.user
        employee.delete()
        user.delete()


# correct salary of employee on sign up day
def correct_employee_salary(employee_phone, correct_salary):
    employee = Employee.objects.get(phone=str(employee_phone))
    if employee:
        employee.net_monthly_salary = correct_salary
        employee.save()
        daily_salary = employee.get_daily_salary()
        work_days = employee.calculate_work_day(datetime.datetime.now().day)
        total_salary = daily_salary * work_days

        employee.balance = total_salary
        employee.credited = total_salary
        employee.save()

        attendance_set = employee.attendance_set.all()
        if attendance_set.count() == 1:
            attendance = attendance_set.first()
            attendance.salary = total_salary
            if employee.email:
                attendance.verified_salary = total_salary
            attendance.save()
        else:
            raise ValidationError("more than one attendance found")


def mask_email(email_id):
    if email_id is not None:
        _split = email_id.split('@')
        _id = _split[0]
        if len(_split) == 2:
            _domain = _split[1]
            length = len(_id)
            if length == 0:
                return _id + '@' + _domain
            elif length == 1:
                return _id.replace(_id, '*') + '@' + _domain
            elif length == 2:
                return _id.replace(_id[1], '*') + '@' + _domain
            elif length == 3:
                return _id.replace(_id[1], '*') + '@' + _domain
            elif length == 4:
                return _id.replace(_id[1:3], '**') + '@' + _domain
            else:
                return _id.replace(_id[2:-2], '*' * (length - 4)) + '@' + _domain
        else:
            return 'invalid email id'


def mask_phone(phone):
    if phone is not None:
        if len(phone) == 10:
            return phone.replace(phone[2:-2], '*' * 6)
        else:
            return 'invalid phone'


def get_name(first_name, last_name):
    name = ""
    if first_name:
        name = name + first_name
    if last_name:
        name = name + last_name
    return name.strip().capitalize()


def get_ifs_object(bank_name, ifsc):
    bank_name = bank_name.capitalize()
    ifsc = ifsc.upper()
    ifs = Ifs.objects.filter(code=ifsc).first()
    if not ifs:
        bank = Bank.objects.filter(name=bank_name).first()
        if not bank:
            bank = Bank.objects.create(name=bank_name)
        ifs = Ifs.objects.create(bank=bank, code=ifsc)
    return ifs


def get_bank_name(ifsc):
    try:
        url = "https://ifsc.razorpay.com/"
        response_data = requests.get(url + str(ifsc)).json()
        if response_data and response_data.get('BANK'):
            return response_data.get('BANK')
        else:
            return None
    except Exception as e:
        print(e)
        return None


def get_salary_and_due_day(salary_data):
    
    salary_day = None

    if salary_data:
        salary_data_list = [salary_data[i]['credited_date'] for i in range(len(salary_data))]
        date_list = [datetime.datetime.strptime(i, '%Y-%m-%d').date().day for i in salary_data_list]
        maxd = max(date_list)
        mind = min(date_list)
        tempnext = datetime.datetime.now().replace(month = datetime.datetime.now().month + 1)
    
        if (maxd>=20 and mind>=20) or (maxd<20 and mind<20):
            temp_due_day = (mind+maxd)//2
        else:
            tempcurr = datetime.datetime.now()

            tempmax = tempcurr.replace(day = maxd)
            tempmin = tempnext.replace(day= mind)
        
            temp = (tempmin - tempmax)//2
            temp_due_day = (tempmax+temp).day
        
        salary_day = 1 if temp_due_day > 28 else temp_due_day    
    
    return salary_day, temp_due_day


def repayment_due_date(temp_due_day):
    curr_date = datetime.datetime.now()
    next_date = curr_date.replace(day=1, month = curr_date.month+1)
    
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if curr_date.year%4==0 and (curr_date.year%100 != 0 or curr_date.year%400==0):
        day_count_for_month[2] = 29
    
    if temp_due_day <= curr_date.day:
        if temp_due_day > day_count_for_month[next_date.month]:
            return curr_date.replace(day = temp_due_day ,month = curr_date.month+1)
        else:
            return curr_date.replace(day=temp_due_day, month = curr_date.month+1)
            
    else:
        if temp_due_day > day_count_for_month[curr_date.month]:
            if day_count_for_month[curr_date.month] == curr_date.day:
                return curr_date.replace(day = day_count_for_month[next_date.month], month = curr_date.month+1)
            else:
                return curr_date.replace(day = day_count_for_month[curr_date.month])
        else:
            return curr_date.replace(day = temp_due_day)


def do_quess_employee_signup(employee_id):
    response_data = get_employee_details(applicant_id=employee_id)
    employee_data = None
    identifier = None
    if response_data and response_data.get('status'):
        identifier = response_data.get('identifier', None)
        employee_data = response_data.get('response', None)
    if employee_data and identifier:
        first_name = employee_data.get('first_name', None)
        last_name = employee_data.get('last_name', None)
        phone = employee_data.get('contact_no', None)
        net_monthly_salary = employee_data.get('salary', None)
        print(net_monthly_salary)
        if net_monthly_salary:
            if int(net_monthly_salary) >= 10000 and int(net_monthly_salary) < 200000:
                if employee_data.get('salary_info'):
                    salary_day, due_day = get_salary_and_due_day(employee_data.get('salary_info'))
                    if salary_day and (int(salary_day) > 0 and int(salary_day) <= 31):
                        joining_date = employee_data.get('joining_date', None)
                        bank_account_number = employee_data.get('account_number', None)
                        ifsc = employee_data.get('ifsc_code', None)
                        bank_name = None
                        if ifsc:
                            bank_name = get_bank_name(ifsc)

                        ifs = None
                        if bank_name and ifsc:
                            ifs = get_ifs_object(bank_name, ifsc)

                        name = get_name(first_name, last_name)
                        company_obj = Company.objects.filter(name='Quess').first()
                        if not company_obj:
                            company_obj = Company.objects.create(name='Quess')

                        if net_monthly_salary and phone and employee_id:
                            regex = '^[6-9]{1}[0-9]{9}$'
                            match = re.match(regex, phone)
                            if match:
                                user_exists = User.objects.filter(username=phone).last()
                                employee_exists = Employee.objects.filter(phone=phone, deleted_at=None).first()
                                if not user_exists:
                                    user_exists = User.objects.create(username=phone)
                                if not employee_exists:
                                    employee_obj = Employee.objects.create(
                                        user=user_exists,
                                        employee_id=employee_id,
                                        name=name,
                                        phone=phone,
                                        company=company_obj,
                                        joining_date=joining_date,
                                        net_monthly_salary=int(net_monthly_salary),
                                        salary_day=salary_day,
                                        due_day=due_day,
                                        salary_type="net",
                                        agreed_with_terms_and_conditions=False,
                                        confirmed=True,
                                        bank_account_number=bank_account_number,
                                        ifs=ifs,
                                        extra_data={"identifier": identifier}
                                    )
                                    return employee_obj


def mark_employee_attendance(employee_id, attendance_days):
    employee = Employee.objects.filter(id=employee_id, deleted_at=None).last()
    if employee:
        month_count = datetime.datetime.now().month
        year_count = datetime.datetime.now().year
        attendance_curr_month = employee.attendance_set.filter(date__year=year_count, date__month=month_count)
        daily_salary = employee.get_daily_salary()
        balance = daily_salary * attendance_days
        for att in attendance_curr_month:
            if not att.verified_salary:
                if balance > 0:
                    att.verified_salary = daily_salary
                    att.save()
                    balance = balance - daily_salary
        print("Attendance verified successfully for: ", employee_id)
    else:
        print("Employee Does Not exists for : ", employee_id)


def get_start_date_of_attendance(employee):
    attendance_exists = employee.attendance_set.filter(
        date__year=datetime.datetime.now().year,
        date__month=datetime.datetime.now().month
    ).order_by('id').last()
    if attendance_exists:
        start_date = attendance_exists.date + datetime.timedelta(days=1)
    else:
        start_date = datetime.datetime.now().replace(day=1).date()

    return start_date

def log(path, filename, content):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    os.chdir(path)
    with open(filename, 'a') as file:
        file.write(str(content) + '\n')
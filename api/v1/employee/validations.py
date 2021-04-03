from rest_framework.exceptions import ValidationError
import re
from core.models import Company, Employee, Domain


def validate_employee_data(data):
    employee_id = data.get('employee_id', None)
    phone = data.get('phone', None)
    name = data.get('name', None)
    email = data.get('email', None)
    joining_date = data.get('joining_date', None)
    salary_day = data.get('salary_day', None)
    net_monthly_salary = data.get('net_monthly_salary', None)
    salary_type = data.get('salary_type', None)
    requested_company = data.get('company', None)
    work_days = data.get('work_days', None)

    if not phone:
        raise ValidationError({"message": "Phone is required."})
    if not net_monthly_salary:
        raise ValidationError({"message": "Net Monthly Salary is required."})
    if not requested_company:
        raise ValidationError({"message": "Company is required."})
    if not work_days:
        raise ValidationError({"message": "Work days is required"})
    if phone:
        if len(phone) > 10 or not phone.isdigit():
            raise ValidationError({"message": "phone is not valid"})
    if salary_day:
        if type(salary_day) is not int:
            raise ValidationError({"message": "Invalid salary day"})
    if name:
        regex = '^([A-Za-z]+)([\sA-Za-z])*$'
        match = re.match(regex, name)
        if (not match) or len(name) > 50:
            raise ValidationError({"message": "Invalid Name"})
    if work_days:
        if not work_days.get('days'):
            raise ValidationError({"message": "Invalid Work Days"})
    if net_monthly_salary:
        if net_monthly_salary < 10000:
            raise ValidationError({"message": "Monthly Salary should be greater than 10000"})
    if email:
        email = email.lower()
        emp_with_email = Employee.objects.filter(email=email, deleted_at=None).first()
        if emp_with_email:
            raise ValidationError({"message": "Employee exists with this Email"})
    if phone:
        emp_with_phone = Employee.objects.filter(phone=phone, deleted_at=None).first()
        if emp_with_phone:
            raise ValidationError({"message": "Employee exists with this Phone"})
    if requested_company:
        company_name = requested_company.get('name', None)
        if email:
            company_domain = requested_company.get('domain').get('name', None)
        else:
            company_domain = None
        
        if not company_name:
            raise ValidationError({"message": "Company Name is required"})
        if email and not company_domain:
            raise ValidationError({"message": "Company Domain is required"})
        if company_name:
            company_name = company_name.capitalize() 
        if company_domain:
            company_domain = company_domain.lower()

        domain_exists = Domain.objects.filter(name=company_domain, category=1).last()
        company_exists = Company.objects.filter(name=company_name).last()
        if email and domain_exists:
            mapped_company = domain_exists.company if domain_exists.company else None
            if not mapped_company:
                if company_exists:
                    domain_exists.company = company_exists
                    domain_exists.save()
                else:
                    company_obj = Company.objects.create(name=company_name)
                    domain_exists.company = company_obj
                    domain_exists.save()
            return_company_obj = domain_exists.company
        elif email and not domain_exists:
            if company_exists:
                domain_obj = Domain.objects.create(
                    name=company_domain,
                    category=1,
                    company=company_exists
                )
            else:
                company_obj = Company.objects.create(name=company_name)
                domain_obj = Domain.objects.create(
                    name=company_domain,
                    category=1,
                    company=company_obj
                )
            return_company_obj = domain_obj.company
        else:
            if company_exists:
                return_company_obj = company_exists
            else:
                return_company_obj = Company.objects.create(name=company_name)

    return return_company_obj



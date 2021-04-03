from core.models import *
from authentication.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from rest_framework.test import APIRequestFactory, force_authenticate
import json
from api.v1.employee.views import EmployeeViewSet, EmployeeBulkCreateView

import os
from daily_salary.settings import BASE_DIR


class EmployeeModelTestCase(TestCase):
    def test_employee_required_fields(self):
        employee = Employee(name='abc')
        with self.assertRaises(ValidationError):
            employee.full_clean()


class EmployeeViewTestCase(TestCase):
    # Test for GET(employee details when fields='confirm')
    def test_employee_details_for_confirm(self):
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        emp_user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=emp_user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
        )
        request = APIRequestFactory().get(
            "/api/v1/employee/", {'fields': 'confirm'})
        employee_list = EmployeeViewSet.as_view({'get': 'retrieve'})
        response = employee_list(request, pk=employee.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(employee details when source='app', fieldset='home')
    def test_employee_details_for_home(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        emp_user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=emp_user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
            company=company,
        )
        request = APIRequestFactory().get(
            "/api/v1/employee/", {'source': 'app', 'fieldset': 'home'})
        employee_list = EmployeeViewSet.as_view({'get': 'retrieve'})
        response = employee_list(request, pk=employee.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(employee details when source='app', fieldset='deposit')
    def test_employee_details_for_deposit(self):
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        emp_user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=emp_user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
        )
        request = APIRequestFactory().get(
            "/api/v1/employee/", {'source': 'app', 'fieldset': 'deposit'})
        employee_list = EmployeeViewSet.as_view({'get': 'retrieve'})
        response = employee_list(request, pk=employee.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(employee list for dashboard)
    def test_employee_list(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        user = User.objects.create(username="upendra@gmail.com")
        employer = Employer.objects.create(
            name="Upendra Kumar",
            phone="7897897895",
            email="upendra@gmail.com",
            user=user,
            company=company
        )
        request = APIRequestFactory().get(
            "/api/v1/employee/")
        employee_list = EmployeeViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=user)
        response = employee_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for employee list ('source': 'pg', 'fieldset': 'salary')
    def test_employee_list_for_salary(self):
        request = APIRequestFactory().get(
            "/api/v1/employee/",
            {'source': 'pg', 'fieldset': 'salary', 'employee_phone_array': '7007501490'})
        employee_list = EmployeeViewSet.as_view({'get': 'list'})
        response = employee_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for employee list ('source': 'web', 'fieldset': 'payment')
    def test_employee_list_for_payment(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        user = User.objects.create(username="upendra@gmail.com")
        employer = Employer.objects.create(
            name="Upendra Kumar",
            phone="7897897895",
            email="upendra@gmail.com",
            user=user,
            company=company
        )
        request = APIRequestFactory().get(
            "/api/v1/employee/",
            {'source': 'web', 'fieldset': 'payment', 'employee_phone_array': '7007501490'})
        employee_list = EmployeeViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=user)
        response = employee_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST (employee create from web)
    def test_employee_create(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        user = User.objects.create(username="upendra@gmail.com")
        employer = Employer.objects.create(
            name="Upendra Kumar",
            phone="7897897895",
            email="upendra@gmail.com",
            user=user,
            company=company,
        )
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        data = json.dumps({
            "user": {
                "username": "8052463080"
            },
            "name": "MIHIR Verma",
            "phone": "8052463080",
            "email": "mihir@gmail.com",
            "net_monthly_salary": 20000,
            "bank_account_number": "5858565236523562",
            "ifs": ifs.id,
        })
        request = APIRequestFactory().post(
            '/api/v1/employee/', data=data, content_type='application/json')
        employee_data = EmployeeViewSet.as_view({'post': 'create'})
        force_authenticate(request, user=user)
        response = employee_data(request)
        self.assertEqual(response.status_code, 200)

    # Test for employee create from app
    def test_employee_create_from_app(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        bank = Bank.objects.create(name="HDFC")
        ifs = Ifs.objects.create(code="HDFC2525", bank=bank)
        company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        data = json.dumps({
            "name": "MIHIR Verma",
            "phone": "8052463055",
            "email": "mihir@gmail.com",
            "company": {
                "id": company.id,
                "name": str(company.name),
                "domain": "instasalary.app"
            },
            "net_monthly_salary": 25000,
            "salary_type": "net",
            "agreed_with_terms_and_conditions": True,
            "confirmed": True
        })
        request = APIRequestFactory().post(
            '/api/v1/employee/?source=app', data=data, content_type='application/json')
        employee_data = EmployeeViewSet.as_view({'post': 'create'})
        response = employee_data(request)
        self.assertEqual(response.status_code, 200)

    # Test for employee bulk create from excel sheet (validate api)
    def test_employee_bulk_create_validate(self):
        c = Client()
        with open(os.path.join(BASE_DIR, 'sample_employee_sheet.xlsx'), 'rb') as f:
            response = c.post('/api/v1/employee/upload/', {
                "fields": "validate",
                'employee_sheet': f})
        self.assertEqual(response.status_code, 200)

    # Test for employee bulk create from excel sheet (upload api)
    def test_employee_bulk_create_upload(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        user = User.objects.create_user(
            username="upendra@gmail.com", password='django1234')
        employer = Employer.objects.create(
            name="Upendra Kumar",
            phone="7897897895",
            email="upendra@gmail.com",
            user=user,
            company=company,
        )
        with open(os.path.join(BASE_DIR, 'sample_employee_sheet.xlsx'), 'rb') as f:
            request = APIRequestFactory().post(
                '/api/v1/employee/upload/',
                data={'fields': 'upload', 'employee_sheet': f})
        force_authenticate(request, user=user)
        employee_data = EmployeeBulkCreateView.as_view()
        response = employee_data(request)
        self.assertEqual(response.status_code, 200 or 204)

    # Test for PATCH ( employee service status update)
    def test_employee_service_status_update(self):
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        emp_user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=emp_user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
        )
        data = json.dumps({
            "service_status": 1
        })
        request = APIRequestFactory().patch(
            '/api/v1/employee/?source=app&fieldset=service_status',
            data=data, content_type='application/json')
        employee_data = EmployeeViewSet.as_view({'patch': 'partial_update'})
        response = employee_data(request, pk=employee.pk)
        self.assertEqual(response.status_code, 200 or 204)

    # Test for PATCH ( employee partial update)
    def test_employee_partial_update(self):
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        emp_user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=emp_user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
        )
        data = json.dumps({
            "name": "upendra kumar",
            "phone": "7007501485",
            "email": "upendra@gmail.com",
            "company": {
            },
            "monthly_salary": 15000,
            "salary_type": "net",
            "work_timings": "9:00 AM-6:00 PM",
            "work_days": {
                "days": [
                    "Sun",
                    "Mon",
                    "Tue",
                    "Wed",
                    "Thu",
                    "Fri"
                ]
            },
            "agreed_with_terms_and_conditions": False,
            "confirmed": True
        })
        request = APIRequestFactory().patch(
            '/api/v1/employee/',
            data=data, content_type='application/json')
        employee_data = EmployeeViewSet.as_view({'patch': 'partial_update'})
        response = employee_data(request, pk=employee.pk)
        self.assertEqual(response.status_code, 200 or 204)


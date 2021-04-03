from core.models import Statement, Bank, Ifs, Employee,\
    Company, Industry, City, State, EmployeeRange
from authentication.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory, force_authenticate
import json
from api.v1.statement.views import (
    StatementViewSet
)


class StatementModelTestCase(TestCase):
    def test_statement_required_fields(self):
        statement = Statement()
        with self.assertRaises(ValidationError):
            statement.full_clean()


class StatementViewTestCase(TestCase):
    # Test for GET(list)
    def test_statement_list(self):
        user = User.objects.create(username="upendra@gmail.com")
        request = APIRequestFactory().get("/api/v1/statement/")
        statement_list = StatementViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=user)
        response = statement_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for statement list when source=app and fieldset=debit
    def test_statement_list_for_debit_only(self):
        user = User.objects.create(username="upendra@gmail.com")
        request = APIRequestFactory().get(
            "/api/v1/statement/", {'source': 'app', 'fieldset': 'debit'})
        statement_list = StatementViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=user)
        response = statement_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_statement_create(self):
        bank = Bank.objects.create(name='BOB')
        ifs = Ifs.objects.create(code='123456', bank=bank)
        user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
            balance=2000,
        )
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
            gstin="8755425",
            domain="instasalary.app"
        )
        data = json.dumps({
            "description": "My statement",
            "debit": 200.0,
            "employee": employee.id,
            "company": company.id
        })
        request = APIRequestFactory().post(
            '/api/v1/statement/?source=app&fieldset=debit', data=data, content_type='application/json')
        statement_data = StatementViewSet.as_view({'post': 'create'})
        force_authenticate(request, user=user)
        response = statement_data(request)
        self.assertEqual(response.status_code, 200)

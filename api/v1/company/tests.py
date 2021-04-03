from core.models import Company, Industry, EmployeeRange, City, State
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.company.views import CompanyViewSet


class CompanyViewTestCase(TestCase):
    def test_company_domain_required_field(self):
        company = Company(name='abc')
        with self.assertRaises(ValidationError):
            company.full_clean()

    def test_company_name_required_field(self):
        company = Company(domain_name='instasalary.app')
        with self.assertRaises(ValidationError):
            company.full_clean()

    def test_company_required_field(self):
        company = Company()
        with self.assertRaises(ValidationError):
            company.full_clean()

    # Test for GET(list)
    def test_company_list(self):
        request = APIRequestFactory().get("/api/v1/company/")
        company_list = CompanyViewSet.as_view({'get': 'list'})
        response = company_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for GET(company list when source='app' and fieldset='autocomplete')
    def test_company_list_for_autocomplete(self):
        request = APIRequestFactory().get(
            "/api/v1/company/", {'source': 'app', 'fieldset': 'autocomplete'})
        company_list = CompanyViewSet.as_view({'get': 'list'})
        response = company_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for GET(company list when source='web' and fieldset='principal')
    def test_company_list_for_principal(self):
        request = APIRequestFactory().get(
            "/api/v1/company/", {'source': 'web', 'fieldset': 'principal'})
        company_list = CompanyViewSet.as_view({'get': 'list'})
        response = company_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_company_create(self):
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        data = json.dumps({
            "name": "Global",
            "industry": industry.id,
            "employee_range": employee_range.id,
            "office_address": "Sohana Road",
            "city": city.id,
            "state": state.id,
            "pincode": "123456",
            "gstin": "8755425",
            "domain_name": "instasalary.app",
            "employer_set": [
                {
                    "user": {
                        "username": "employer@gmail.com",
                        "password": "django1234"
                    },
                    "name": "employer singh",
                    "phone": "8052463090",
                    "email": "employer@gmail.com"
                }
            ],
        })
        request = APIRequestFactory().post(
            '/api/v1/company/', data=data, content_type='application/json')
        company_data = CompanyViewSet.as_view({'post': 'create'})
        response = company_data(request)
        self.assertEqual(response.status_code, 200)

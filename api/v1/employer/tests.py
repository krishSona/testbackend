from core.models import *
from authentication.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.employer.views import EmployerViewSet


class EmployerModelTestCase(TestCase):
    def test_employer_required_fields(self):
        employer = Employer(name='abc')
        with self.assertRaises(ValidationError):
            employer.full_clean()


class EmployerViewTestCase(TestCase):
    # Test for GET(list)
    def test_employer_list(self):
        request = APIRequestFactory().get("/api/v1/employer/")
        employer_list = EmployerViewSet.as_view({'get': 'list'})
        response = employer_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for GET(employer list when source='web' and fieldset='principal')
    def test_employer_list_for_principal(self):
        user = User.objects.create(username="upendra@gmail.com")
        industry = Industry.objects.create(name='IT')
        employee_range = EmployeeRange.objects.create(number='0-100')
        city = City.objects.create(name='Delhi')
        state = State.objects.create(name='Delhi')
        employer_company = Company.objects.create(
            name="Global",
            industry=industry,
            employee_range=employee_range,
            office_address="Sohana-Road",
            city=city,
            state=state,
            pincode="123456",
            gstin="8755425"
        )
        employer = Employer.objects.create(
            name="Upendra Kumar",
            phone="7897897895",
            email="upendra@gmail.com",
            user=user,
            company=employer_company
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
            gstin="87504500"
        )
        employer.principal_companies.add(company)
        request = APIRequestFactory().get(
            "/api/v1/employer/",
            {'source': 'web', 'fieldset': 'principal', 'email': 'upendra@gmail.com'})
        employer_list = EmployerViewSet.as_view({'get': 'list'})
        response = employer_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_employer_create(self):
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
        data = json.dumps({
            "user": {
                "username": "employer12@gmail.com",
                "password": "django1234"
            },
            "name": "Employer-12",
            "phone": "8052463083",
            "email": "employer12@gmail.com",
            "company": company.id
        })
        request = APIRequestFactory().post(
            '/api/v1/employer/', data=data, content_type='application/json')
        employer_data = EmployerViewSet.as_view({'post': 'create'})
        response = employer_data(request)
        self.assertEqual(response.status_code, 200)

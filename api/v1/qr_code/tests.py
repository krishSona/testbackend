from django.test import TestCase
from rest_framework.exceptions import ValidationError
from core.models import *
from authentication.models import User

import json
from rest_framework.test import APIRequestFactory
from api.v1.qr_code.views import QrCodeViewSet


class QrCodeModelTestCase(TestCase):
    def test_qr_code_required_fields(self):
        try:
            QrCode.objects.create(qr_id='IS-QR-ID-20201123080622')
        except:
            self.assertRaises(ValidationError)


class QrCodeViewTestCase(TestCase):
    def test_qr_code_list(self):
        request = APIRequestFactory().get('api/v1/qr_code/')
        qr_code_list = QrCodeViewSet.as_view({'get': 'list'})
        response = qr_code_list(request)
        self.assertEqual(response.status_code, 200)

    # QrCode list when source='app' and fieldset='qr'
    def test_qr_code_match_api(self):
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
        user = User.objects.create(username='upendra.kumar')
        employee = Employee.objects.create(
            user=user,
            name="smile",
            phone="7007501460",
            email="upendra@gmail.com",
            net_monthly_salary=10000,
            bank_account_number="5858565236523562",
            ifs=ifs,
            company=company,
        )
        Setting.objects.create(key='distance', value=50)
        qr_code = QrCode.objects.create(
            qr_id="IS-QR-ID-20201123080622",
            longitude="82.2224560",
            latitude="-31.4567230",
            company=company,
        )
        request = APIRequestFactory().get(
            'api/v1/qr_code/',
            {'source': 'app', 'fieldset': 'qr', 'qr_id': 'IS-QR-ID-20201123080622',
             'employee_id': employee.pk, 'longitude': '82.2224560', 'latitude': '-31.4567230'})
        qr_code_list = QrCodeViewSet.as_view({'get': 'list'})
        response = qr_code_list(request)
        self.assertEqual(response.status_code, 200)

    def test_qr_code_create(self):
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
            code="000001",
        )
        data = json.dumps({
            "qr_id": "000001-20201123080622",
            "longitude": "82.2224560",
            "latitude": "-31.4567230",
        })
        request = APIRequestFactory().post(
            'api/v1/qr_code/', data=data, content_type='application/json'
        )
        qr_code_data = QrCodeViewSet.as_view({'post': 'create'})
        response = qr_code_data(request)
        self.assertEqual(response.status_code, 200)

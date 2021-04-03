from core.models import Attendance, Employee, Company, Bank,\
    Ifs, Industry, EmployeeRange, City, State
from authentication.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.attendance.views import AttendanceViewset
import datetime


class AttendanceModelTestCase(TestCase):
    def test_attendance_required_fields(self):
        attendance = Attendance(status='present')
        with self.assertRaises(ValidationError):
            attendance.full_clean()


class AttendanceViewTestCase(TestCase):
    # Test for GET(list)
    def test_attendance_list(self):
        request = APIRequestFactory().get("/api/v1/attendance/")
        attendance_list = AttendanceViewset.as_view({'get': 'list'})
        response = attendance_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE ( create attendance when employee is present)
    def test_attendance_create_for_present(self):
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
            gstin="8755425"
        )
        data = json.dumps({
            "status": "present",
            "duration": "full_day",
            "start_time": "09:00 AM",
            "end_time": "06:00 PM",
            "qr_code_scanned": False,
            "face_detected": False,
            "location": "office",
            "employee": employee.id,
            "company": company.id
        })
        request = APIRequestFactory().post(
            '/api/v1/attendance/', data=data, content_type='application/json')
        attendance_data = AttendanceViewset.as_view({'post': 'create'})
        response = attendance_data(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE ( create attendance when employee is absent)
    def test_attendance_create_for_absent(self):
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
            gstin="8755425"
        )
        data = json.dumps({
            "status": "absent",
            "employee": employee.id,
            "company": company.id
        })
        request = APIRequestFactory().post(
            '/api/v1/attendance/', data=data, content_type='application/json')
        attendance_data = AttendanceViewset.as_view({'post': 'create'})
        response = attendance_data(request)
        self.assertEqual(response.status_code, 200)
